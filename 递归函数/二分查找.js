function find(l, target, start=0, end=null) {
	end = end == null ? l.length : end
	let mid_index = Math.round((end-start) / 2) + start
	console.log(l[mid_index], target)
	if(start <= end){
		if(l[mid_index] < target){
			return find(l, target, start = mid_index + 1, end = end)
		} else if (l[mid_index] > target) {
			return find(l, target, start = 0, end = mid_index - 1)
		}else{
			console.log(mid_index)
			return mid_index
		}
	}else{
		return '找不到结果'
	}
}
let arr = [1,2,45,67,89,100,110,120,150,180,190]
let result = find(arr, 180)
console.log(result) //undefined


