#include <iostream>
#include <string>
#include <list>
#include <vector>
std::list<char> parse(std::string parse)
{
    int a = parse.length();
    std::list<char> t;
    for (int i = 0; i < a; i++)
    {
        char c = parse[i];
        t.push_back(c);
    }
    return t;
}
template<typename x>
bool scan(x scanfor,std::list<x> in)
{
    std::vector<x> inp (in.begin(),in.end());
    int tester = 0;
    for (int count = 0; count < (in.size());count++)
    {
        if (scanfor == inp[count])
        {
            return true;
        }
        else
        {
            tester++;
        }
    }
    return false;
}
