#include <mtglang 2\inputhandle.hpp>
#include <iostream>
#include <vector>
#include <list>


template<typename datatype, typename b, typename a, typename c>

class utils
{
    int adresser = 0;


    class variable
    {
        std::string name;
        datatype data;

        int adress = adresser;
    };


    std::vector<variable> mem;


    int writer (int adress, datatype datum,bool newvar)
    {
        return 0;
    }


    datatype variablehandle (std::string name,bool write,datatype data)
    {
        if (write = true)
        {
            for (int i = 0; i < mem.size(); i++)
            {
                if ( mem[i].name == name )
                {
                    writer(datum= data adress = i);
                }

                if ( i == (mem.size() - 1))
                {
                    if (writer(datum= data, adress = adresser, newvar = true)==1)
                    {
                        return "VARWRITE<SUCCESS>"
                    }

                    adresser++;
                }
            }
        }
    }
};