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
    };


    std::vector<variable> mem;


    int writer (int adress, datatype datum,bool newvar = false, std::string name)
    {
        if (newvar == true)
        {
            mem[adresser] = variable;

            mem[adresser].name = name;
            mem[adresser].data = datum;

            adresser++;
            return 0;
        }
        else if (newvar = false)
        {
            mem[adress].data = datum;

            return 0;
        }
        else
        {
            return 1;
        }
    }


    datatype variablehandle (std::string name,bool write,datatype data)
    {
        if (write = true)
        {
            for (int i = 0; i < mem.size(); i++)
            {
                if ( mem[i].name == name )
                {
                    switch (writer(datum= data adress = i))
                    {
                        case 0:
                        {
                            return "VARWRITE<SUCCESS>";
                            break;
                        }
                        case 1: 
                        {
                            return "VARWRITE<ERROR>";
                            break;
                        }
                        case default:
                        {
                            return 0;
                            break;
                        }
                    }
                }

                if ( i == (mem.size() - 1))
                {
                    switch (writer(datum= data,newvar = true))
                    {
                        case 0:
                        {
                            return "VARWRITE<SUCCESS>";
                            break;
                        }
                        case 1:
                        {
                            return "VARWRITE<ERROR>";
                            break;
                        }
                        case default:
                        {
                            return 0;
                            break;
                        }
                    }
                }
            }
        }
    }
};