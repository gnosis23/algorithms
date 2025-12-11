/**
 * return top k numbers of nums
 * O(nlogn) - O(n^2)
 * @param {number[]} nums 
 * @param {number} k 
 * @return {number[]}
 */
function topk(nums, k) {
  if (k <= 0) return [];
  if (nums.length <= k) return nums;
  let [sa, sb] = partition(nums);
  return topk(sa, k).concat(topk(sb, k - sa.length));
}

function partition(nums) {
  let small = [];
  let big = [];

  let pivot = Math.floor(Math.random() * nums.length);
  swap(nums, 0, pivot);

  pivot = nums[0];
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] <= pivot) {
      small.push(nums[i]);
    } else {
      big.push(nums[i]);
    }
  }
  small.length < big.length ? small.push(pivot) : big.push(pivot);

  return [small, big];
}

function swap(arr, i, j) { 
  let t = arr[i]; arr[i] = arr[j]; arr[j] = t; 
}


module.exports = topk;