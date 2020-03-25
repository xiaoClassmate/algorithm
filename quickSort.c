var swap = function(data, i, j){ 
    var tmp = data[i];
    data[i] = data[j];
    data[j] = tmp;
};
    
// 以data[left]為Pivot，left相當於最左邊第一個元素    
var quickSort = function(data, left, right){    
    if(left < right){
        var i=left, j=right+1;
        while(true){
            // 向右找小於Pivot的數值的位置
            while(i+1 < data.length && data[++i] < data[left]); 
            
            // 向左找大於Pivot的數值的位置
            while(j-1 > -1 && data[--j] > data[left]);
            
            // 若i,j的位置交叉
            //     代表範圍內，Pivot右邊已無比Pivot小的數值
            //     代表範圍內，Pivot左邊已無比Pivot大的數值            
            if(i >= j)    
                break;
            
            // 將比Pivot大的數值換到右邊，比Pivot小的數值換到左邊
            swap(data, i, j);           
        }
        swap(data, left, j);    // 將Pivot移到中間
        quickSort(data, left, j-1);    // 對左子串列進行快速排序
        quickSort(data, j+1, right);   // 對右子串列進行快速排序
    }
};