#include "Mutator_base.h"

/**
 * mut3
 * Create empty base classes
 */ 
class MutatorFrontendAction_3 : public MutatorFrontendAction {
public:
  MUTATOR_FRONTEND_ACTION_CREATE_ASTCONSUMER(3)

private:
  class MutatorASTConsumer_3 : public MutatorASTConsumer {
    public:
      MutatorASTConsumer_3(Rewriter &R) : TheRewriter(R) {}
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
      int targets = 0;
  };
};