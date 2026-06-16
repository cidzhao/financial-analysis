import json

def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def safe_float(v):
    try:
        if v is None: return 0.0
        return float(v)
    except:
        return 0.0

def calc_qoq(curr, prev):
    if prev == 0:
        return "-"
    growth = (curr - prev) / abs(prev) * 100
    color = "positive" if growth > 0 else "negative" if growth < 0 else ""
    sign = "+" if growth > 0 else ""
    return f'<span class="qoq {color}">({sign}{growth:.1f}%)</span>'

def generate_report():
    data = load_data('c:/Users/zhaoxiaoyu/Documents/finical/finical-report/sea/extracted_data.json')
    quarters = data['quarters'][1:5] # 2026 Q1, 2025 Q4, 2025 Q3, 2025 Q2
    quarters_reverse = quarters[::-1] # chronological: 2025 Q2 to 2026 Q1

    # Segments configuration
    segments = {
        'Shopee': {
            'name': 'Shopee (电商及商品销售)',
            'rev_keys': ['Shopee', 'sales of goods'],
            'cost_keys': ['Cost of Shopee', 'cost of sales of goods'],
            'sm_key': 'Sales and marketing expenses of Shopee',
            'op_key': 'Operating income of Shopee'
        },
        'Monee': {
            'name': 'Monee (数字金融服务)',
            'rev_keys': ['Monee'],
            'cost_keys': ['Cost of Monee'],
            'sm_key': 'Sales and marketing expenses of Monee',
            'op_key': 'Operating income of Monee'
        },
        'Garena': {
            'name': 'Garena (数字娱乐)',
            'rev_keys': ['Garena'],
            'cost_keys': ['Cost of Garena'],
            'sm_key': 'Sales and marketing expenses of Garena',
            'op_key': 'Operating income of Garena'
        },
        'Other': {
            'name': 'Other (其他服务)',
            'rev_keys': ['Other Services'],
            'cost_keys': ['Cost of Other Service'],
            'sm_key': 'Sales and marketing expenses of Other',
            'op_key': 'Operating income of Other'
        }
    }

    # Extract metrics per segment
    metrics = {}
    for seg_id, seg_info in segments.items():
        metrics[seg_id] = {
            'Revenue': [],
            'Cost': [],
            'GrossProfit': [],
            'GrossMargin': [],
            'S&M': [],
            'OpIncome': []
        }
        for i in range(4):
            idx = 4 - i
            
            rev = sum(safe_float(data[k][idx]) for k in seg_info['rev_keys'] if k in data)
            cost = sum(safe_float(data[k][idx]) for k in seg_info['cost_keys'] if k in data)
            sm = safe_float(data[seg_info['sm_key']][idx]) if seg_info['sm_key'] in data else 0.0
            op = safe_float(data[seg_info['op_key']][idx]) if seg_info['op_key'] in data else 0.0
            
            gp = rev - cost
            gm = (gp / rev) if rev else 0.0
            
            metrics[seg_id]['Revenue'].append(rev)
            metrics[seg_id]['Cost'].append(cost)
            metrics[seg_id]['GrossProfit'].append(gp)
            metrics[seg_id]['GrossMargin'].append(gm)
            metrics[seg_id]['S&M'].append(sm)
            metrics[seg_id]['OpIncome'].append(op)

    # HTML Generation
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Sea Limited 业务板块财务分析报告 (2025 Q2 - 2026 Q1)</title>
    <!-- 引入 ECharts -->
    <script src="https://cdn.jsdelivr.net/npm/echarts@5.5.0/dist/echarts.min.js"></script>
    <style>
        :root {{
            --bg-color: #f8fafc;
            --card-bg: #ffffff;
            --text-main: #1e293b;
            --text-light: #64748b;
            --border: #e2e8f0;
            --primary: #3b82f6;
            --shopee: #f97316;
            --monee: #10b981;
            --garena: #ef4444;
            --other: #8b5cf6;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            margin: 0;
            padding: 40px 20px;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        .header {{
            text-align: center;
            margin-bottom: 50px;
        }}
        .header h1 {{
            font-size: 2.5rem;
            margin-bottom: 10px;
            color: var(--text-main);
        }}
        .header p {{
            font-size: 1.1rem;
            color: var(--text-light);
        }}
        .charts-container {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
            gap: 30px;
            margin-bottom: 40px;
        }}
        .chart-box {{
            background: var(--card-bg);
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            height: 400px;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(550px, 1fr));
            gap: 30px;
        }}
        .card {{
            background: var(--card-bg);
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }}
        .card h2 {{
            margin-top: 0;
            padding-bottom: 12px;
            border-bottom: 2px solid var(--border);
            font-size: 1.5rem;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }}
        th, td {{
            padding: 12px 6px;
            text-align: right;
            border-bottom: 1px solid var(--border);
            white-space: nowrap;
        }}
        th:first-child, td:first-child {{
            text-align: left;
            font-weight: 600;
        }}
        th {{
            color: var(--text-light);
            font-size: 0.9rem;
            text-transform: uppercase;
        }}
        .qoq {{
            font-size: 0.8rem;
            margin-left: 4px;
        }}
        .positive {{ color: #10b981; }}
        .negative {{ color: #ef4444; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Sea Limited 业务板块财务分析</h1>
            <p>包含 Shopee, Monee, Garena 和 其他业务的季度环比 (单位: 亿美元)</p>
            <p style="font-size: 0.9rem; color: #94a3b8;">注: Shopee 业务数据已包含商品销售对应的营收及成本。</p>
        </div>
        
        <!-- 图表区 -->
        <div class="charts-container">
            <div class="chart-box" id="revenueChart"></div>
            <div class="chart-box" id="opIncomeChart"></div>
            <div class="chart-box" id="grossMarginChart" style="grid-column: 1 / -1;"></div>
        </div>

        <!-- 数据表格区 -->
        <div class="grid">
"""

    for seg_id, seg_info in segments.items():
        color_var = f"--{seg_id.lower()}"
        m = metrics[seg_id]
        
        # Helper to format value + qoq
        def format_val_qoq(arr, is_percent=False):
            res = [f"<td>{arr[0]*100:.1f}%</td>" if is_percent else f"<td>{arr[0]:.2f}</td>"]
            for i in range(1, 4):
                val = arr[i]
                prev = arr[i-1]
                val_str = f"{val*100:.1f}%" if is_percent else f"{val:.2f}"
                if is_percent:
                    # For margins, calculate bps or just absolute difference? Let's just do simple difference for percentage
                    diff = (val - prev) * 100
                    color = "positive" if diff > 0 else "negative" if diff < 0 else ""
                    sign = "+" if diff > 0 else ""
                    qoq_str = f'<span class="qoq {color}">({sign}{diff:.1f}pts)</span>'
                else:
                    qoq_str = calc_qoq(val, prev)
                
                res.append(f"<td>{val_str}<br>{qoq_str}</td>")
            return res

        html += f"""
            <div class="card">
                <h2 style="color: var({color_var})">{seg_info['name']}</h2>
                <table>
                    <thead>
                        <tr>
                            <th>指标</th>
                            <th>{quarters_reverse[0]}</th>
                            <th>{quarters_reverse[1]}</th>
                            <th>{quarters_reverse[2]}</th>
                            <th>{quarters_reverse[3]}</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>总营收</td>
                            {''.join(format_val_qoq(m['Revenue']))}
                        </tr>
                        <tr>
                            <td>成本</td>
                            {''.join(format_val_qoq(m['Cost']))}
                        </tr>
                        <tr>
                            <td>毛利润</td>
                            {''.join(format_val_qoq(m['GrossProfit']))}
                        </tr>
                        <tr>
                            <td>毛利率</td>
                            {''.join(format_val_qoq(m['GrossMargin'], is_percent=True))}
                        </tr>
                        <tr>
                            <td>销售营销费用</td>
                            {''.join(format_val_qoq(m['S&M']))}
                        </tr>
                        <tr>
                            <td>营业利润</td>
                            {''.join(format_val_qoq(m['OpIncome']))}
                        </tr>
                    </tbody>
                </table>
                <p style="font-size: 0.8rem; color: #94a3b8; margin-top: 10px; text-align: right;">注: 表格内带有颜色的百分比表示该项指标的环比增速 (QoQ)。</p>
            </div>
        """

    html += """
        </div>
    </div>
    
    <script>
        const quarters = """ + json.dumps(quarters_reverse) + """;
        const metrics = """ + json.dumps(metrics) + """;
        
        // 1. Revenue Chart
        const revChart = echarts.init(document.getElementById('revenueChart'));
        revChart.setOption({
            title: { text: '各板块总营收 (亿美元)', left: 'center' },
            tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
            legend: { bottom: 0 },
            grid: { left: '3%', right: '4%', bottom: '15%', containLabel: true },
            xAxis: { type: 'category', data: quarters },
            yAxis: { type: 'value' },
            series: [
                { name: 'Shopee', type: 'bar', stack: 'total', itemStyle: { color: '#f97316' }, data: metrics.Shopee.Revenue },
                { name: 'Monee', type: 'bar', stack: 'total', itemStyle: { color: '#10b981' }, data: metrics.Monee.Revenue },
                { name: 'Garena', type: 'bar', stack: 'total', itemStyle: { color: '#ef4444' }, data: metrics.Garena.Revenue },
                { name: 'Other', type: 'bar', stack: 'total', itemStyle: { color: '#8b5cf6' }, data: metrics.Other.Revenue }
            ]
        });

        // 2. Operating Income Chart
        const opChart = echarts.init(document.getElementById('opIncomeChart'));
        opChart.setOption({
            title: { text: '各板块营业利润 (亿美元)', left: 'center' },
            tooltip: { trigger: 'axis' },
            legend: { bottom: 0 },
            grid: { left: '3%', right: '4%', bottom: '15%', containLabel: true },
            xAxis: { type: 'category', data: quarters },
            yAxis: { type: 'value' },
            series: [
                { name: 'Shopee', type: 'line', marker: 'circle', itemStyle: { color: '#f97316' }, data: metrics.Shopee.OpIncome },
                { name: 'Monee', type: 'line', marker: 'circle', itemStyle: { color: '#10b981' }, data: metrics.Monee.OpIncome },
                { name: 'Garena', type: 'line', marker: 'circle', itemStyle: { color: '#ef4444' }, data: metrics.Garena.OpIncome },
                { name: 'Other', type: 'line', marker: 'circle', itemStyle: { color: '#8b5cf6' }, data: metrics.Other.OpIncome }
            ]
        });

        // 3. Gross Margin Chart
        const gmChart = echarts.init(document.getElementById('grossMarginChart'));
        gmChart.setOption({
            title: { text: '各板块毛利率变化', left: 'center' },
            tooltip: { 
                trigger: 'axis',
                valueFormatter: (value) => (value * 100).toFixed(1) + '%'
            },
            legend: { bottom: 0 },
            grid: { left: '3%', right: '4%', bottom: '15%', containLabel: true },
            xAxis: { type: 'category', data: quarters },
            yAxis: { 
                type: 'value',
                axisLabel: { formatter: (val) => (val * 100).toFixed(0) + '%' }
            },
            series: [
                { name: 'Shopee', type: 'line', marker: 'circle', itemStyle: { color: '#f97316' }, data: metrics.Shopee.GrossMargin },
                { name: 'Monee', type: 'line', marker: 'circle', itemStyle: { color: '#10b981' }, data: metrics.Monee.GrossMargin },
                { name: 'Garena', type: 'line', marker: 'circle', itemStyle: { color: '#ef4444' }, data: metrics.Garena.GrossMargin }
            ]
        });

        window.addEventListener('resize', function() {
            revChart.resize();
            opChart.resize();
            gmChart.resize();
        });
    </script>
</body>
</html>
"""

    with open('c:/Users/zhaoxiaoyu/Documents/finical/finical-report/sea/sea-anaylisis.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("HTML report generated at c:/Users/zhaoxiaoyu/Documents/finical/finical-report/sea/sea-anaylisis.html")

if __name__ == "__main__":
    generate_report()
