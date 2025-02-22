import json

def load_json_data(file_path):
    """加载JSON文件数据，返回物种名称列表"""
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return list(data.values())

def analyze_species(plantclef_path, plantnet_path):
    """分析两个数据集的物种信息并返回统计结果"""
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
    
    total_unique_species = len(plantclef_species | plantnet_species)  # 并集
    
    return {
        "plantclef_count": len(plantclef_species),
        "plantnet_count": len(plantnet_species),
        "common_count": len(common_species),
        "only_in_plantclef_count": len(only_in_plantclef),
        "only_in_plantnet_count": len(only_in_plantnet),
        "total_unique_count": total_unique_species
    }

def generate_report(stats, report_path):
    """生成分析报告"""
    # 生成报告内容
    report_content = f"""
    植物数据集分析报告

    1. 数据集概述:
    - PlantCLEF2015 数据集物种总数: {stats['plantclef_count']}
    - PlantNet300K 数据集物种总数: {stats['plantnet_count']}

    2. 共同物种和独有物种数量:
    - 共同物种数量: {stats['common_count']}
    - 仅在 PlantCLEF2015 中出现的物种数量: {stats['only_in_plantclef_count']}
    - 仅在 PlantNet300K 中出现的物种数量: {stats['only_in_plantnet_count']}

    3. 总的植物种类数量:
    - 合并后的植物种类数量: {stats['total_unique_count']}
    """
    
    # 将报告写入文件
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print(f"分析报告已生成: {report_path}")

if __name__ == "__main__":
    plantclef_path = "plantclef2015.json"
    plantnet_path = "plantnet300k.json"
    report_path = "analysis_report.txt"
    
    # 分析物种信息
    stats = analyze_species(plantclef_path, plantnet_path)
    
    # 生成报告
    generate_report(stats, report_path) 