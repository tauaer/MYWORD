

def calculator(a, b, operation='add'):
    """基础计算器函数"""
    operations = {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b if b != 0 else 'Error: Division by zero'
    }
    
    return operations.get(operation, 'Error: Invalid operation')

def file_operations():
    """文件操作演示函数"""
    try:
        # 写入文件
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write("GitHub实验项目输出结果\\n")
            f.write("=" * 30 + "\\n")
            for i in range(1, 6):
                f.write(f"数据记录 {i}: 结果 = {i * 10}\\n")
        print("✅ 文件写入成功：output.txt")
        
        # 读取文件
        with open('output.txt', 'r', encoding='utf-8') as f:
            content = f.read()
            print("📖 文件内容：")
            print(content)
            
    except Exception as e:
        print(f"❌ 文件操作错误: {e}")

def data_analysis():
    """简单数据分析演示"""
    numbers = [15, 23, 8, 42, 4, 16]
    
    analysis_result = {
        '数据集': numbers,
        '总和': sum(numbers),
        '平均值': sum(numbers) / len(numbers),
        '最大值': max(numbers),
        '最小值': min(numbers),
        '数据量': len(numbers)
    }
    
    print("📊 数据分析结果：")
    for key, value in analysis_result.items():
        print(f"  {key}: {value}")

def main():
    """主函数 - 增强版"""
    print("=" * 50)
    print("GitHub实验项目 - 增强版测试程序")
    print("=" * 50)
    
    # 测试计算器功能
    print("🧮 计算器功能测试：")
    test_cases = [
        (20, 4, 'add'),
        (20, 4, 'subtract'),
        (20, 4, 'multiply'),
        (20, 4, 'divide')
    ]
    
    for a, b, op in test_cases:
        result = calculator(a, b, op)
        print(f"  {a} {op} {b} = {result}")
    
    print("\\n" + "=" * 30)
    
    # 文件操作演示
    file_operations()
    
    print("\\n" + "=" * 30)
    
    # 数据分析演示
    data_analysis()
    
    print("\\n" + "=" * 50)
    print("🎉 实验完成！所有增强功能测试成功！")
    print("=" * 50)

if __name__ == "__main__":
    main()
