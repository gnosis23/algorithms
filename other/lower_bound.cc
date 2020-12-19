/**
 * 寻找下界（如果没有会返回最大的小于目标数加一）
 * 参考：https://en.cppreference.com/w/cpp/algorithm/lower_bound
 * 
 * 1) 如果目标不重复，可以在里面加个相等的分支，直接返回；剩下的就是下界
 * 2) 用前闭后开的方式实现“二分法”，可以避开一些 bug，如 [2,3]
 */
#include <vector>
using std::vector;

int lower_bound(vector<int>& nums, int val) {
    int last = nums.size();
    int first = 0;
    int count = last;
    while (count > 0) {
        int it = first;
        int step = count / 2;
        it += step;
        bool comp = nums[it] < val;
        if (comp) {
            first = ++it;
            count -= step + 1;
        }
        else {
            count = step;
        }
    }
    return first;
}
