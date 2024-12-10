#include "../include/Initialization.h"

// ========================================================================================================
#define MUT2_OUTPUT 1

void MutatorFrontendAction_2::Callback::run(const MatchFinder::MatchResult &Result) {
  if (auto *DL = Result.Nodes.getNodeAs<clang::CXXRecordDecl>("Classes")) {
    if (!DL || !Result.Context->getSourceManager().isWrittenInMainFile(
                   DL->getLocation()))
      return;
    // DL->dump();
    if ((!DL->isStruct() && !DL->isClass()) || DL->isLambda())
      return;
    if (DL->isCompleteDefinition() == false)
      return;
    auto ctors = DL->ctors();
    for (auto ctor : ctors) {
      if (ctor->isImplicit())
        continue;
      auto acc = ctor->getAccess();
      int judge = getrandom::getRandomIndex(1);
      llvm::outs() << judge << '\n';
      // if(!judge) continue;
      if (acc == AccessSpecifier::AS_private ||
          acc == AccessSpecifier::AS_protected) {
        Rewrite.ReplaceText(ctor->getBeginLoc(), 0, "\n/*mut2*/public:\n");
      }

      else {
        Rewrite.ReplaceText(ctor->getBeginLoc(), 0, "\n/*mut2*/protected:\n");
      }
    }
    auto dtor = DL->getDestructor();
    int judge_dtor = getrandom::getRandomIndex(1);
    if (judge_dtor && !dtor->isImplicit()) {
      auto acc = dtor->getAccess();
      if (acc == AccessSpecifier::AS_private ||
          acc == AccessSpecifier::AS_protected) {
        Rewrite.ReplaceText(dtor->getBeginLoc(), 0, "\n/*mut2*/public:\n");
      }

      else {
        Rewrite.ReplaceText(dtor->getBeginLoc(), 0, "\n/*mut2*/protected:\n");
      }
    }
  }
}

void MutatorFrontendAction_2::MutatorASTConsumer_2::HandleTranslationUnit(ASTContext &Context) {
    MatchFinder classFinder;
    auto matcher = cxxRecordDecl().bind("Classes");
    Callback callback(TheRewriter);
    classFinder.addMatcher(matcher, &callback);
    classFinder.matchAST(Context);
}

// ========================================================================================================
#define MUT4_OUTPUT 1

void MutatorFrontendAction_4::Callback::run(const MatchFinder::MatchResult &Result) {
  if (auto *OD = Result.Nodes.getNodeAs<clang::DeclStmt>("Objectdecl")) {
    if (!OD || !Result.Context->getSourceManager().isWrittenInMainFile(
                   OD->getBeginLoc()))
      return;
    auto decl = stringutils::rangetoStr(*(Result.SourceManager), OD->getSourceRange());
    bool judgeclass = false;
    for (auto classname : classnames) {
      if (decl.find(classname) != string::npos) {
        judgeclass = true;
        break;
      }
    }
    if (judgeclass) {
      llvm::outs() << decl << '\n';
      if (decl.find('(') != string::npos) {
        std::replace(decl.begin(), decl.end(), '(', '{');
        std::replace(decl.begin(), decl.end(), ')', '}');
        decl = "/*mut4*/" + decl;
      } else if (decl.find('{') == string::npos) {
        decl.insert(decl.rfind(';'), "{}");
        decl = "/*mut4*/" + decl;
      }
    }
    Rewrite.ReplaceText(CharSourceRange::getTokenRange(OD->getSourceRange()), decl);
  } else if (auto CL =
                 Result.Nodes.getNodeAs<clang::CXXRecordDecl>("Classes")) {
    if (!CL || !Result.Context->getSourceManager().isWrittenInMainFile(
                   CL->getLocation()))
      return;
    // llvm::outs()<<CL->getNameAsString()<<'\n';
    classnames.push_back(CL->getNameAsString());
  }
}

void MutatorFrontendAction_4::MutatorASTConsumer_4::HandleTranslationUnit(ASTContext &Context) {
    MatchFinder classFinder;
    auto decl_matcher = declStmt().bind("Objectdecl");
    auto class_matcher = cxxRecordDecl().bind("Classes");
    Callback callback(TheRewriter);
    classFinder.addMatcher(decl_matcher, &callback);
    classFinder.addMatcher(class_matcher, &callback);
    classFinder.matchAST(Context);
}