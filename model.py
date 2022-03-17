from pydantic import BaseModel,conlist
import joblib
# classes = {
#     0: 'clust1',
#     1: 'clust2',
#     2: 'clust3'
# }

class Feature_type(BaseModel):
    Item_Weight:                    float
    Item_Visibility:                float
    Item_Type:                      int
    Item_MRP:                       float
    Outlet_Years:                   int
    Outlet:                         int
    Item_Fat_Content_0:             int
    Item_Fat_Content_1:             int
    Item_Fat_Content_2:             int
    Outlet_Size_0:                  int
    Outlet_Size_1:                  int
    Outlet_Size_2:                  int
    Outlet_Location_Type_0:         int
    Outlet_Location_Type_1:         int
    Outlet_Location_Type_2:         int
    Outlet_Type_0:                  int
    Outlet_Type_1:                  int
    Outlet_Type_2:                  int
    Outlet_Type_3:                  int
    New_Item_Type_0:                int
    New_Item_Type_1:                int
    New_Item_Type_2:                int

model = joblib.load("rf_model.pkl")
