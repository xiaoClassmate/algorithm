#include <stdio.h> 
#include <stdlib.h>

void quicksort(int *data, int left, int right);
void swap(int *x, int *y);

int main(void)
{
    int i, n, data[10];
    printf("請輸入資料筆數 n(<= 10): ");
    scanf("%d", &n);

    for (i = 0; i < n; i++){
        printf("請輸入第 %d 筆資料: ", i + 1);
        scanf("%d", &data[i]);
    }

    // 執行快速排序法
    quicksort(data, 0, n-1);

    printf("\n排序後的結果: ");
    for (i = 0; i < n; i++){
        printf("%d ", data[i]);
    }

    printf("\n");
    system("pause");
}

void quicksort(int *data, int left, int right)
{
    int pivot, i, j;
    if (left >= right) { return; }
    pivot = data[left];
    i = left + 1;
    j = right;

    while (1){
        while (i <= right){
            if (data[i] > pivot){
                break;
            }
            i = i + 1;
        }

        while (j > left){
            if (data[j] < pivot){
                break;
            }
            j = j - 1;
        }

        if (i > j) { break; }
        swap(&data[i], &data[j]);
    }

    swap(&data[left], &data[j]);

    quicksort(data, left, j - 1);
    quicksort(data, j + 1, right);
}

void swap(int *x, int *y){
    *x = *x ^ *y;
    *y = *x ^ *y;
    *x = *x ^ *y;
}