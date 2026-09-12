
import time
from data_loader.data_loader import SalesDataLoader
from business.company import Company
from sorter.bubble_sort import BubbleSort
if __name__ == "__main__":
    print("====================================")
    print(" Sales Company Sorting Demo")
    print("====================================\n")
    # -----------------------------------
    # 1. Load Data
    # -----------------------------------
    loader = SalesDataLoader("data/source/sales.csv")
    sales_data = loader.get_data_by_size(1000)
    print(f"Loaded {len(sales_data)} sales records.\n")
    # -----------------------------------
    # 2. Create Company Object
    # -----------------------------------
    company = Company("TechCorp", sales_data)
    print("Company Summary:")
    print(f"Total Records: {company.total_sales_count()}")
    print(f"Total Revenue:{company.total_revenue():,.2f}\n")
    # -----------------------------------
    # 3. Choose Sorting Algorithm
    # -----------------------------------
    bubble_sort = BubbleSort()
    # -----------------------------------
    # 4. Time Sorting Operation
    # -----------------------------------
    start = time.perf_counter()
    sorted_sales = company.sort_sales(bubble_sort,key_function=lambda sale: sale.total_sales)
    end = time.perf_counter()
    print(f"Sorting Time: {end - start:.6f} seconds\n")
    # -----------------------------------
    # 5. Display Top 10 Sales
    # -----------------------------------
    print("Top 10 Sales (Highest Total Sales):\n")
    top_sales = company.get_top_sales(bubble_sort,n=10)
    for sale in top_sales:
        print(sale)
        print("\nDemo Complete.")
