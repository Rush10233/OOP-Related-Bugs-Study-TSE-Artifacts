#include "Mutator_base.h"

/**
 * mut1
 * Expand useless template type parameter
 */ 
class MutatorFrontendAction_1 : public MutatorFrontendAction {
public:
  MUTATOR_FRONTEND_ACTION_CREATE_ASTCONSUMER(1)

private:
  class MutatorASTConsumer_1 : public MutatorASTConsumer {
    public:
      MutatorASTConsumer_1(Rewriter &R) : TheRewriter(R) {}
      void HandleTranslationUnit(ASTContext &Context) override;
    private:
      Rewriter &TheRewriter;
  };
  
  class Callback : public MatchFinder::MatchCallback {
    public:
      Callback(Rewriter &Rewrite) : Rewrite(Rewrite) {}
      virtual void run(const MatchFinder::MatchResult &Result);
    private:
      Rewriter &Rewrite;
  };
};