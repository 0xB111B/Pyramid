#include <string>
#include <vector>

using namespace std;

bool isPyramidWord(const string& s)
{
    if (s.length() == 0)
        return false;
    
    vector<int> count('z'-'a', 0);
    for (int i = 0; i < s.length(); i++)
    {
        if (!isalpha(s[i]))
            return false;
        count[tolower(s[i])-'a']++;
    }
    sort(count.begin(), count.end());
        
    for (int i = 0; i < count.size(); i++)
    {
        if (count[i] == 0) continue;
        if (i > 0 && (count[i] != count[i-1]+1))
            return false;
    }
    
    return true;
}
