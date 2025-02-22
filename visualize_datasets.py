import json
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def load_json_data(file_path):
    """加载JSON文件数据，返回物种名称列表"""
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return list(data.values())

def create_visualizations(plantclef_path, plantnet_path):
    """生成可视化图表并保存为HTML文件"""
    # 加载数据
    plantclef_data = load_json_data(plantclef_path)
    plantnet_data = load_json_data(plantnet_path)
    
    # 转换为集合以便比较
    plantclef_species = set(plantclef_data)
    plantnet_species = set(plantnet_data)
    
    # 计算统计信息
    common_species = plantclef_species.intersection(plantnet_species)
    only_in_plantclef = plantclef_species - plantnet_species
    only_in_plantnet = plantnet_species - plantclef_species
    
    # 创建文件夹
    if not os.path.exists('visualizations'):
        os.makedirs('visualizations')
    
    # 创建子图
    fig = make_subplots(rows=6, cols=1, 
                        subplot_titles=("物种总数对比", "物种分布情况", "物种数量分布", "物种重叠度热力图", "物种数量箱线图", "物种数量散点图"),
                        specs=[[{"type": "bar"}], [{"type": "pie"}], [{"type": "bar"}], [{"type": "heatmap"}], [{"type": "box"}], [{"type": "scatter"}]])

    # 1. 物种总数的柱状图
    fig.add_trace(go.Bar(x=['PlantCLEF2015', 'PlantNet300K'], 
                          y=[len(plantclef_species), len(plantnet_species)],
                          marker_color=['blue', 'orange']),
                  row=1, col=1)

    # 2. 共同物种和独有物种的饼图
    sizes = [len(common_species), len(only_in_plantclef), len(only_in_plantnet)]
    labels = ['共同物种', '仅在PlantCLEF2015中', '仅在PlantNet300K中']
    fig.add_trace(go.Pie(labels=labels, values=sizes, hole=.3),
                  row=2, col=1)

    # 3. 物种数量的条形图
    fig.add_trace(go.Bar(x=['共同物种', '仅在PlantCLEF2015中', '仅在PlantNet300K中'], 
                          y=[len(common_species), len(only_in_plantclef), len(only_in_plantnet)],
                          marker_color=['green', 'red', 'purple']),
                  row=3, col=1)

    # 4. 物种重叠度的热力图
    overlap_matrix = [
        [len(common_species), len(only_in_plantclef), len(only_in_plantnet)],
        [len(only_in_plantclef), len(common_species), len(only_in_plantnet)],
        [len(only_in_plantnet), len(common_species), len(only_in_plantclef)]
    ]
    
    fig.add_trace(go.Heatmap(z=overlap_matrix, 
                           x=['共同物种', '仅在PlantCLEF2015中', '仅在PlantNet300K中'],
                           y=['共同物种', '仅在PlantCLEF2015中', '仅在PlantNet300K中'],
                           colorscale='Viridis'),
                  row=4, col=1)

    # 5. 物种数量的箱线图
    fig.add_trace(go.Box(y=[len(plantclef_species), len(plantnet_species)], 
                          name='物种数量', 
                          marker_color='lightblue'),
                  row=5, col=1)

    # 6. 物种数量的散点图
    fig.add_trace(go.Scatter(x=['PlantCLEF2015', 'PlantNet300K'], 
                              y=[len(plantclef_species), len(plantnet_species)],
                              mode='markers+lines', 
                              marker=dict(size=10, color='red')),
                  row=6, col=1)

    # 更新布局
    fig.update_layout(title_text='植物数据集分析', height=1500)
    
    # 添加meta标签以指定字符集为UTF-8
    fig_html = fig.to_html(full_html=True)
    fig_html = fig_html.replace('<head>', '<head><meta charset="UTF-8">')

    # 保存为HTML文件
    with open('visualizations/species_analysis.html', 'w', encoding='utf-8') as f:
        f.write(fig_html)

if __name__ == "__main__":
    plantclef_path = "plantclef2015.json"
    plantnet_path = "plantnet300k.json"
    create_visualizations(plantclef_path, plantnet_path)
