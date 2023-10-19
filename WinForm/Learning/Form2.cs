using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinFormLearn
{
    public partial class TestForm : Form
    {
        public TestForm(string name, string pwd, string sex)
        {
            InitializeComponent();
            label1.Text = "欢迎用户 " + name + " 性别 " + sex;
            label2.Text = "密码为 " + pwd;
        }

        private void TestForm_MouseClick(object sender, MouseEventArgs e)
        {
            this.CenterToScreen();
        }

        private void TestForm_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            this.Close();
        }
    }
}
