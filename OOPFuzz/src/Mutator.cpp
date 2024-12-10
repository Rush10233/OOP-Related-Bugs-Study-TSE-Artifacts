#include "Mutator.h"

std::map<int, clang::tooling::FrontendActionFactory *> factoryMap = {
    {1, newFrontendActionFactory<MutatorFrontendAction_1>().release()},
    {2, newFrontendActionFactory<MutatorFrontendAction_2>().release()},
    {3, newFrontendActionFactory<MutatorFrontendAction_3>().release()},
    {4, newFrontendActionFactory<MutatorFrontendAction_4>().release()},
};

clang::tooling::FrontendActionFactory *getMutatorNewFrontendActionFactory(int mutator) {
    auto it = factoryMap.find(mutator);
    if (it != factoryMap.end()) {
        return it->second;
    }
    assert(false && "No mutator matched\n");
    return nullptr; 
}
