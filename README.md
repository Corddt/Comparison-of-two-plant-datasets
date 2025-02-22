# Plant Species Dataset Analysis

这个项目用于分析和比较两个植物数据集（PlantCLEF2015和PlantNet300K）的异同。项目包含多种分析工具，可以生成详细的统计报告、Excel表格和可视化图表。

## 功能特点 

1. 计算两个数据集的物种总数和独有物种数量
2. 分析数据集之间的物种重叠情况
3. 生成详细的分析报告（TXT格式）
4. 生成Excel格式的数据统计表
5. 生成交互式可视化图表（HTML格式）

## 项目结构

.
├── README.md
├── compare_datasets.py # Excel报告生成
├── visualize_datasets.py # 可视化图表生成
├── combined_analysis.py # 综合分析报告生成
├── plantclef2015.json # PlantCLEF2015数据集
└── plantnet300k.json # PlantNet300K数据集

## 安装要求

1. 安装Python 3.x

2. 安装所需的Python库

    ```bash
    pip install pandas openpyxl plotly
    ```


## 使用方法

1. 运行Excel报告生成

    ```bash
    python compare_datasets.py
    ```

2. 运行可视化图表生成

    ```bash
    python visualize_datasets.py
    ```

3. 运行综合分析报告生成

    ```bash
    python combined_analysis.py
    ``` 

## 输出文件

- `analysis_report.txt`: 包含基本统计信息的文本报告
- `plant_datasets_analysis_[timestamp].xlsx`: 详细的Excel统计报表
- `visualizations/species_analysis.html`: 交互式可视化图表

## 可视化图表包含

1. 物种总数对比图
2. 物种分布情况饼图
3. 物种数量分布图
4. 物种重叠度热力图
5. 物种数量箱线图
6. 物种数量散点图

## 数据集信息

- **PlantCLEF2015**: 包含约1000种植物物种
- **PlantNet300K**: 包含约1000种植物物种

## 注意事项

- 确保JSON文件使用UTF-8编码
- 运行脚本前请确保已安装所有必要的依赖
- 可视化图表需要现代浏览器才能正确显示

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request来帮助改进项目。

## 作者

[Corddt]

## 更新日志

- 2025-02-22: 初始版本发布


    

