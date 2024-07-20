import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the data
df = pd.read_json('C:/Users/kungs/Dashboard/Dashboard03/pp3-4_2566_province.json')

# Mock latitude and longitude data for all provinces
province_coordinates = {
    'กรุงเทพมหานคร': {'latitude': 13.7563, 'longitude': 100.5018},
    'กระบี่': {'latitude': 8.0863, 'longitude': 98.9063},
    'กาญจนบุรี': {'latitude': 14.0041, 'longitude': 99.5483},
    'กาฬสินธุ์': {'latitude': 16.4314, 'longitude': 103.5061},
    'กำแพงเพชร': {'latitude': 16.4727, 'longitude': 99.5215},
    'ขอนแก่น': {'latitude': 16.4419, 'longitude': 102.8356},
    'จันทบุรี': {'latitude': 12.6113, 'longitude': 102.1039},
    'ฉะเชิงเทรา': {'latitude': 13.6904, 'longitude': 101.0772},
    'ชลบุรี': {'latitude': 13.3611, 'longitude': 100.9847},
    'ชัยนาท': {'latitude': 15.1855, 'longitude': 100.1253},
    'ชัยภูมิ': {'latitude': 15.8069, 'longitude': 102.0312},
    'ชุมพร': {'latitude': 10.4931, 'longitude': 99.1801},
    'เชียงราย': {'latitude': 19.9106, 'longitude': 99.8406},
    'เชียงใหม่': {'latitude': 18.7883, 'longitude': 98.9853},
    'ตรัง': {'latitude': 7.5563, 'longitude': 99.6114},
    'ตราด': {'latitude': 12.2458, 'longitude': 102.5154},
    'ตาก': {'latitude': 16.8833, 'longitude': 99.1285},
    'นครนายก': {'latitude': 14.2065, 'longitude': 101.2130},
    'นครปฐม': {'latitude': 13.8198, 'longitude': 100.0588},
    'นครพนม': {'latitude': 17.3923, 'longitude': 104.7697},
    'นครราชสีมา': {'latitude': 14.9799, 'longitude': 102.0977},
    'นครศรีธรรมราช': {'latitude': 8.4304, 'longitude': 99.9631},
    'นครสวรรค์': {'latitude': 15.7047, 'longitude': 100.1372},
    'นนทบุรี': {'latitude': 13.8591, 'longitude': 100.5144},
    'นราธิวาส': {'latitude': 6.4265, 'longitude': 101.8253},
    'น่าน': {'latitude': 18.7755, 'longitude': 100.7731},
    'บึงกาฬ': {'latitude': 18.3609, 'longitude': 103.6492},
    'บุรีรัมย์': {'latitude': 14.9947, 'longitude': 103.1029},
    'ปทุมธานี': {'latitude': 14.0206, 'longitude': 100.5250},
    'ประจวบคีรีขันธ์': {'latitude': 11.8129, 'longitude': 99.7977},
    'ปราจีนบุรี': {'latitude': 14.0506, 'longitude': 101.3664},
    'ปัตตานี': {'latitude': 6.8699, 'longitude': 101.2505},
    'พระนครศรีอยุธยา': {'latitude': 14.3532, 'longitude': 100.5689},
    'พังงา': {'latitude': 8.4506, 'longitude': 98.5256},
    'พัทลุง': {'latitude': 7.6167, 'longitude': 100.0809},
    'พิจิตร': {'latitude': 16.4477, 'longitude': 100.3485},
    'พิษณุโลก': {'latitude': 16.8219, 'longitude': 100.2659},
    'เพชรบุรี': {'latitude': 13.1111, 'longitude': 99.9390},
    'เพชรบูรณ์': {'latitude': 16.418, 'longitude': 101.1606},
    'แพร่': {'latitude': 18.1450, 'longitude': 100.1403},
    'พะเยา': {'latitude': 19.1636, 'longitude': 99.9096},
    'ภูเก็ต': {'latitude': 7.8804, 'longitude': 98.3923},
    'มหาสารคาม': {'latitude': 16.1807, 'longitude': 103.2986},
    'มุกดาหาร': {'latitude': 16.5453, 'longitude': 104.7206},
    'แม่ฮ่องสอน': {'latitude': 19.3020, 'longitude': 97.9654},
    'ยะลา': {'latitude': 6.5416, 'longitude': 101.2800},
    'ยโสธร': {'latitude': 15.7942, 'longitude': 104.1451},
    'ร้อยเอ็ด': {'latitude': 16.0538, 'longitude': 103.6531},
    'ระนอง': {'latitude': 9.9528, 'longitude': 98.6085},
    'ระยอง': {'latitude': 12.6814, 'longitude': 101.2773},
    'ราชบุรี': {'latitude': 13.5283, 'longitude': 99.8134},
    'ลพบุรี': {'latitude': 14.7995, 'longitude': 100.6534},
    'ลำปาง': {'latitude': 18.2888, 'longitude': 99.4902},
    'ลำพูน': {'latitude': 18.5742, 'longitude': 99.0087},
    'เลย': {'latitude': 17.4860, 'longitude': 101.7223},
    'ศรีสะเกษ': {'latitude': 15.1184, 'longitude': 104.3225},
    'สกลนคร': {'latitude': 17.1560, 'longitude': 104.1451},
    'สงขลา': {'latitude': 7.1756, 'longitude': 100.6144},
    'สตูล': {'latitude': 6.6238, 'longitude': 100.0674},
    'สมุทรปราการ': {'latitude': 13.5991, 'longitude': 100.5995},
    'สมุทรสงคราม': {'latitude': 13.4143, 'longitude': 99.9631},
    'สมุทรสาคร': {'latitude': 13.5472, 'longitude': 100.2744},
    'สระแก้ว': {'latitude': 13.8240, 'longitude': 102.0644},
    'สระบุรี': {'latitude': 14.5289, 'longitude': 100.9103},
    'สิงห์บุรี': {'latitude': 14.8874, 'longitude': 100.3988},
    'สุโขทัย': {'latitude': 17.0078, 'longitude': 99.8237},
    'สุพรรณบุรี': {'latitude': 14.4745, 'longitude': 100.1235},
    'สุราษฎร์ธานี': {'latitude': 9.1382, 'longitude': 99.3214},
    'สุรินทร์': {'latitude': 14.8818, 'longitude': 103.4937},
    'หนองคาย': {'latitude': 17.8783, 'longitude': 102.7423},
    'หนองบัวลำภู': {'latitude': 17.2047, 'longitude': 102.4265},
    'อ่างทอง': {'latitude': 14.5896, 'longitude': 100.4550},
    'อุดรธานี': {'latitude': 17.4138, 'longitude': 102.7877},
    'อุทัยธานี': {'latitude': 15.3874, 'longitude': 100.0239},
    'อุตรดิตถ์': {'latitude': 17.6235, 'longitude': 100.0993},
    'อุบลราชธานี': {'latitude': 15.2442, 'longitude': 104.8487},
    'อำนาจเจริญ': {'latitude': 15.8572, 'longitude': 104.6258}
}

# Add latitude and longitude columns to the DataFrame
df['latitude'] = df['schools_province'].map(lambda x: province_coordinates[x]['latitude'] if x in province_coordinates else None)
df['longitude'] = df['schools_province'].map(lambda x: province_coordinates[x]['longitude'] if x in province_coordinates else None)

# Initialize the Dash app
app = dash.Dash(__name__)

# Create a list of provinces
provinces = df['schools_province'].unique()

# Create the layout of the app with dropdown
app.layout = html.Div([
    html.H1("Student Graduates by Province in 2566"),
    dcc.Dropdown(
        id='province-dropdown',
        options=[{'label': province, 'value': province} for province in provinces],
        value='กรุงเทพมหานคร',  # Default value
        clearable=False
    ),
    dcc.Graph(id='map-graph'),
    dcc.Graph(id='bar-graph')
])

# Create the map figure
@app.callback(
    [Output('map-graph', 'figure'),
     Output('province-dropdown', 'value')],
    [Input('province-dropdown', 'value'),
     Input('map-graph', 'clickData')]
)
def update_map(province, clickData):
    # If a point is clicked, update the province based on clickData
    if clickData is not None:
        province = clickData['points'][0]['hovertext']

    # Filter the DataFrame for the selected province
    filtered_df = df[df['schools_province'] == province]

    fig = px.scatter_geo(
        df,
        lat='latitude',
        lon='longitude',
        size='totalstd',
        hover_name='schools_province',
        hover_data={
            'latitude': False,
            'longitude': False,
            'totalmale': True,
            'totalfemale': True,
            'totalstd': True
        },
        projection='natural earth',
        title=f"Number of Male and Female Students Graduated in 2566 in {province}"
    )
    fig.update_layout(
        geo=dict(
            scope='asia',
            resolution=50,
            showland=True,
            landcolor='rgb(217, 217, 217)',
            showcountries=True,
            countrycolor='rgb(255, 255, 255)'
        )
    )
    return fig, province

# Create the bar chart figure
@app.callback(
    Output('bar-graph', 'figure'),
    [Input('province-dropdown', 'value')]
)
def update_bar_chart(province):
    filtered_df = df[df['schools_province'] == province]

    fig = go.Figure(data=[
        go.Bar(name='Total Students', x=filtered_df['schools_province'], y=filtered_df['totalstd']),
        go.Bar(name='Male Students', x=filtered_df['schools_province'], y=filtered_df['totalmale']),
        go.Bar(name='Female Students', x=filtered_df['schools_province'], y=filtered_df['totalfemale'])
    ])
    fig.update_layout(
        barmode='group',  # Set the barmode to group to place bars side by side
        title=f"Number of Students Graduated in 2566 in {province}",
        xaxis_title="Province",
        yaxis_title="Number of Students"
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
