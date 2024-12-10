#include "Mutator_base.h"

/**
 * mut2
 * Change access specifier of ctors/dtors
 */ 
class MutatorFrontendAction_2 : public MutatorFrontendAction {
public:
  MUTATOR_FRONTEND_ACTION_CREATE_ASTCONSUMER(2)

private:
  class MutatorASTConsumer_2 : public MutatorASTConsumer {
    public:
      MutatorASTConsumer_2(Rewriter &R) : TheRewriter(R) {}
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

/**
 * mut4
 * Replace object initilization exp.
 */ 
class MutatorFrontendAction_4 : public MutatorFrontendAction {
public:
  MUTATOR_FRONTEND_ACTION_CREATE_ASTCONSUMER(11)

private:
  class MutatorASTConsumer_4 : public MutatorASTConsumer {
    public:
      MutatorASTConsumer_4(Rewriter &R) : TheRewriter(R) {}
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
      std::vector<string> classnames;
  };
};