import json
from collections import Counter
import pandas as pd
from datetime import datetime

def load_json_data(file_path):
    """加载JSON文件数据，返回物种名称列表"""
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        # 只返回物种名称（JSON中的值），忽略序号（键）
        return list(data.values())

def analyze_datasets(plantclef_path, plantnet_path):
    """分析两个数据集的异同"""
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
    
    # 打印分析结果
    print(f"数据集分析结果:")
    print(f"PlantCLEF2015 物种总数: {len(plantclef_species)}")
    print(f"PlantNet300K 物种总数: {len(plantnet_species)}")
    print(f"两个数据集共有物种数: {len(common_species)}")
    print(f"仅在PlantCLEF2015中出现的物种数: {len(only_in_plantclef)}")
    print(f"仅在PlantNet300K中出现的物种数: {len(only_in_plantnet)}")
    
    # 生成详细的Excel报告
    generate_excel_report(plantclef_species, plantnet_species, 
                         common_species, only_in_plantclef, only_in_plantnet)
    
    # 保存详细结果到文本文件
    with open('analysis_results.txt', 'w', encoding='utf-8') as f:
        f.write("共同物种列表:\n")
        f.write("\n".join(sorted(common_species)))
        f.write("\n\n仅在PlantCLEF2015中的物种:\n")
        f.write("\n".join(sorted(only_in_plantclef)))
        f.write("\n\n仅在PlantNet300K中的物种:\n")
        f.write("\n".join(sorted(only_in_plantnet)))

def generate_excel_report(plantclef_species, plantnet_species, 
                         common_species, only_in_plantclef, only_in_plantnet):
    """生成详细的Excel报告"""
    # 创建时间戳
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # 创建Excel写入器
    with pd.ExcelWriter(f'plant_datasets_analysis_{timestamp}.xlsx') as writer:
        # 1. 概述表格
        summary_data = {
            '统计项': [
                'PlantCLEF2015数据集物种总数',
                'PlantNet300K数据集物种总数',
                '共同物种数量',
                '仅在PlantCLEF2015中的物种数量',
                '仅在PlantNet300K中的物种数量',
                '物种并集总数',
                'PlantCLEF2015独有物种占比',
                'PlantNet300K独有物种占比',
                '共同物种占比(相对于并集)'
            ],
            '数值': [
                len(plantclef_species),
                len(plantnet_species),
                len(common_species),
                len(only_in_plantclef),
                len(only_in_plantnet),
                len(plantclef_species.union(plantnet_species)),
                f"{len(only_in_plantclef)/len(plantclef_species):.2%}",
                f"{len(only_in_plantnet)/len(plantnet_species):.2%}",
                f"{len(common_species)/len(plantclef_species.union(plantnet_species)):.2%}"
            ]
        }
        pd.DataFrame(summary_data).to_excel(writer, sheet_name='总体统计', index=False)
        
        # 2. 共同物种列表
        pd.DataFrame(sorted(common_species), columns=['物种名称']).to_excel(
            writer, sheet_name='共同物种', index=False)
        
        # 3. 仅在PlantCLEF2015中的物种
        pd.DataFrame(sorted(only_in_plantclef), columns=['物种名称']).to_excel(
            writer, sheet_name='PlantCLEF2015独有', index=False)
        
        # 4. 仅在PlantNet300K中的物种
        pd.DataFrame(sorted(only_in_plantnet), columns=['物种名称']).to_excel(
            writer, sheet_name='PlantNet300K独有', index=False)

if __name__ == "__main__":
    plantclef_path = "plantclef2015.json"
    plantnet_path = "plantnet300k.json"
    analyze_datasets(plantclef_path, plantnet_path) 