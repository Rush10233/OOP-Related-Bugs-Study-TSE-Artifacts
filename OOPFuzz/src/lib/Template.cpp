#include "../include/Template.h"

// ========================================================================================================
#define MUT1_OUTPUT 1

void MutatorFrontendAction_1::Callback::run(const MatchFinder::MatchResult &Result) {
  if (auto *TP = Result.Nodes.getNodeAs<clang::ClassTemplateDecl>("TemplateClasses")) {
    if (!TP || !Result.Context->getSourceManager().isWrittenInMainFile(
                   TP->getLocation()))
      return;
    auto params = TP->getTemplateParameters();
    auto paralist = stringutils::rangetoStr(*(Result.SourceManager),
                                            params->getSourceRange());
    int judge = getrandom::getRandomIndex(2);
    llvm::outs() << judge + 1 << '\n';
    // Regular
    if (judge == 1 || judge == 0) {
      paralist.insert(paralist.rfind('>'), ",/*mut1*/typename NOS=int");
    }
    // Non type
    else if (judge == 2) {
      paralist.insert(paralist.rfind('>'), ",/*mut1*/ int NON=0");
    }
    Rewrite.ReplaceText(CharSourceRange::getTokenRange(params->getSourceRange()), paralist);
  }
}

void MutatorFrontendAction_1::MutatorASTConsumer_1::HandleTranslationUnit(ASTContext &Context) {
    MatchFinder classFinder;
    DeclarationMatcher matcher = classTemplateDecl().bind("TemplateClasses");
    Callback callback(TheRewriter);
    classFinder.addMatcher(matcher, &callback);
    classFinder.matchAST(Context);
}