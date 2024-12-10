#include "../include/Inheritance.h"

// ========================================================================================================
#define MUT3_OUTPUT 1

void MutatorFrontendAction_3::Callback::run(const MatchFinder::MatchResult &Result) {
  if (auto *DL = Result.Nodes.getNodeAs<clang::CXXRecordDecl>("Inderived")) {
    if (!DL || !Result.Context->getSourceManager().isWrittenInMainFile(
                   DL->getLocation()))
      return;
    if ((!DL->isStruct() && !DL->isClass()) || DL->isLambda())
      return;
    // DL->dump();

    if (DL->isCompleteDefinition() == false)
      return;
    
    // llvm::outs()<<DL->getNameAsString()<<'\n';
    auto definition = stringutils::rangetoStr(*(Result.SourceManager), DL->getSourceRange());
    auto newdefinition = definition.insert(definition.find("{"), ": /*mut7*/public mut7_empty");

    if (targets == 0) {
      newdefinition = "\nstruct mut3_empty{\n\n};\n" + newdefinition;
    }
    targets++;

    Rewrite.ReplaceText(CharSourceRange::getTokenRange(DL->getSourceRange()), newdefinition);
  } else if (auto *TP = Result.Nodes.getNodeAs<clang::ClassTemplateDecl>(
                 "Templated")) {
    if (!TP || !Result.Context->getSourceManager().isWrittenInMainFile(
                   TP->getLocation()))
      return;
    if (targets == 0) {
      llvm::outs() << TP->getNameAsString() << '\n';
      targets = 1;
      Rewrite.ReplaceText(TP->getBeginLoc(), 0, "\nstruct mut3_empty{\n\n};\n");
    }
  }
}

void MutatorFrontendAction_3::MutatorASTConsumer_3::HandleTranslationUnit(ASTContext &Context) {
    MatchFinder classFinder;
    DeclarationMatcher matcher = cxxRecordDecl(unless(hasAnyBase(hasType(cxxRecordDecl())))).bind("Inderived");
    auto template_matcher=classTemplateDecl().bind("Templated");
    Callback callback(TheRewriter);
    classFinder.addMatcher(matcher, &callback);
    classFinder.addMatcher(template_matcher, &callback);
    classFinder.matchAST(Context);
}