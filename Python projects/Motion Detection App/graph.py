##Importing the df variable from the motion detection script- this also automatically calls the script
from cctv_smart import df
from bokeh.plotting import show,output_file,figure
from bokeh.models import HoverTool, ColumnDataSource
import pandas

##Parsing the column to datetime so Bokeh library can read it as time
df["Date_Appeared"]=pandas.to_datetime(df['Date_Appeared'])
df["Date_Disappeared"]=pandas.to_datetime(df["Date_Disappeared"])

## The Hover tool needs a string to display info so we create two additional columns with str version
df["Date_Appeared_Str"]=df["Date_Appeared"].apply(lambda n: str(n))
df["Date_Disappeared_Str"]= df["Date_Disappeared"].apply(lambda n: str(n))

##Using this we don't need to refrence df
cds=ColumnDataSource(df)


p=figure(height=300,width=900,title="Motion Graph",x_axis_type="datetime")

hover=HoverTool(tooltips=[("Start","@Date_Appeared_Str"),("End","@Date_Disappeared_Str")])
p.add_tools(hover)

p.quad(top=2,bottom=0,left="Date_Appeared",right="Date_Disappeared",color="Green",source=cds)

output_file=("Motion Graph.html")
show(p)
