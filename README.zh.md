# 虚拟示波器

这个仓库包含了一个使用 PyQt6 和 Arduino Nano 实现的简易虚拟示波器。该示波器可以实时显示5V范围内的电压波形。该项目采用 GPlv3 协议进行许可。

## 功能特点

- 实时显示电压波形：通过连接 Arduino Nano 和计算机，可以将电压波形实时传输到计算机，并在图形界面中显示。
- 简易界面：使用 PyQt6 开发的用户友好界面，简单易用。
- 支持5V电压范围：该虚拟示波器适用于5V以内的电压测量。

## 如何使用

以下是使用该虚拟示波器的基本步骤：

1. 确保你已经连接了 Arduino Nano 板到计算机，并正确地设置了串口的权限。

2. **使用 Python 代码的方式：**

   - 在计算机上安装 Python 3.11，并安装 PyQt6 库。
   - 克隆该仓库到本地：

     ```
     git clone git@github.com:Elonisme/Virtual-Simple-Oscilloscope.git
     ```

   - 进入项目目录：

     ```
     cd Virtual-Simple-Oscilloscope
     ```

   - 运行主程序：

     ```
     python main.py
     ```

3. **使用已发布的可执行文件的方式：**

   - 在计算机上下载最新的可执行文件：[Releases](https://github.com/Elonisme/Virtual-Simple-Oscilloscope/releases)。
   - 解压缩下载的文件。
   - 双击运行可执行文件。

4. 在图形界面上，你将看到实时的电压波形显示。

## 许可

该项目基于 GPlv3 协议进行许可。详细信息请参阅 [LICENSE](LICENSE) 文件。

## 贡献

如果你对该项目有任何改进或建议，欢迎贡献你的代码。请提出问题或提交请求。

## 免责声明

该虚拟示波器仅用于教育和学习目的。请小心操作，遵循适当的安全措施。作者对使用该示波器可能产生的任何损失或损害不承担任何责任。

## 联系方式

如有任何问题或疑问，请通过以下方式联系作者：

- 电子邮件：elonisme@163.com
- GitHub 项目页面:[Elonisme/Virtual-Simple-Oscilloscope](https://github.com/Elonisme/Virtual-Simple-Oscilloscope)
