#include "src/Mutator.h"

static llvm::cl::OptionCategory MyToolCategory("my-tool options");

static cl::extrahelp CommonHelp(CommonOptionsParser::HelpMessage);

static cl::extrahelp MoreHelp("\nMore help text...\n");

static cl::opt<int> Mutator_selector("mutator",cl::desc("Selected mutator"),cl::cat(MyToolCategory));
static cl::opt<string> Sourcedir("sourcedir",cl::desc("Directory path of the test source files"),cl::value_desc("directory_path"),cl::cat(MyToolCategory)) ;

string SRCDIR="";

int main(int argc, const char **argv) {
  auto ExpectedParser = CommonOptionsParser::create(argc, argv, MyToolCategory);
  if (!ExpectedParser) {
    llvm::errs() << ExpectedParser.takeError();
    return 1;
  }

  auto mutator=int(Mutator_selector);
  SRCDIR=Sourcedir.c_str();


  CommonOptionsParser& OptionsParser = ExpectedParser.get();
  RefactoringTool Rtool(OptionsParser.getCompilations(),OptionsParser.getSourcePathList());

  llvm::errs() << "Mutator: " << mutator << "\n";

  clang::tooling::FrontendActionFactory * FrontendFactory;
  FrontendFactory = getMutatorNewFrontendActionFactory(mutator);
  return Rtool.run(FrontendFactory);










  // std::unique_ptr<FrontendActionFactory> FrontendFactory;
  // FrontendFactory = getMutatorNewFrontendActionFactory(mutator);
  // return Rtool.run(FrontendFactory.get());
}
