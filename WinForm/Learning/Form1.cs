using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinFormLearn
{
    public partial class Form1 : Form
    {
        string calendar_msg;

        public Form1()
        {
            InitializeComponent();
        }

        private void label1_MouseClick(object sender, MouseEventArgs e)
        {
            (label1.Text, label2.Text) = (label2.Text, label1.Text);
        }

        private void label2_MouseClick(object sender, MouseEventArgs e)
        {
            System.Diagnostics.Process.Start("http://www.baidu.com");
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            label2.Text = textBox1.Text;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofd = new OpenFileDialog();
            DialogResult dr = ofd.ShowDialog();
            string filename = ofd.FileName;
            if (dr == DialogResult.OK && !string.IsNullOrEmpty(filename))
            {
                richTextBox1.LoadFile(filename, RichTextBoxStreamType.PlainText);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofd = new OpenFileDialog();
            DialogResult dr = ofd.ShowDialog();
            string filename = ofd.FileName;
            if (dr == DialogResult.OK && !string.IsNullOrEmpty(filename))
            {
                richTextBox1.SaveFile(filename, RichTextBoxStreamType.PlainText);
            }

        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            string name = textBox3.Text;
            string pwd = textBox2.Text;
            string repwd = textBox4.Text;
            string sex = "";
            string hobby = "";

            if (string.IsNullOrEmpty(name))
            {
                MessageBox.Show("用户名不能为空");
                return;
            }
            if (string.IsNullOrEmpty(pwd))
            {
                MessageBox.Show("密码不能为空");
                return;
            }
            if (string.IsNullOrEmpty(repwd))
            {
                MessageBox.Show("两次输入的密码不一致");
                return;
            }

            if (radioButton1.Checked)
            {
                sex = radioButton1.Text;
            }
            else if (radioButton2.Checked)
            {
                sex = radioButton2.Text;
            }

            foreach (Control c in Controls)
            {
                if (c is CheckBox)
                {
                    if (((CheckBox)c).Checked)
                    {
                        hobby = hobby + " " + ((CheckBox)c).Text;
                    }
                }
            }

            if (hobby != "")
            {
                MessageBox.Show("您选择的爱好是：" + hobby, "提示");
            }
            else
            {
                MessageBox.Show("您没有选择爱好", "提示");
            }

            TestForm loginForm = new TestForm(name, pwd, sex);
            loginForm.Show();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            string msg = "";
            for (int i = 0; i < checkedListBox1.CheckedItems.Count; i++)
            {
                msg = msg + " " + checkedListBox1.CheckedItems[i].ToString();
            }
            if (msg != "")
            {
                MessageBox.Show("您购买的商品有：" + msg, "提示");
            }
            else
            {
                MessageBox.Show("您没有选择商品", "提示");
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            string msg = "";
            for (int i = 0; i < listBox1.SelectedItems.Count; i++)
            {
                msg = msg + " " + listBox1.SelectedItems[i].ToString();
            }
            if (msg != "")
            {
                MessageBox.Show("您购买的商品有：" + msg, "提示");
            }
            else
            {
                MessageBox.Show("您没有选择商品", "提示");
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            string msg = "";
            for (int i = 0; i < listBox2.SelectedItems.Count; i++)
            {
                msg = msg + " " + listBox2.SelectedItems[i].ToString();
            }
            if (msg != "")
            {
                MessageBox.Show("您购买的商品有：" + msg, "提示");
            }
            else
            {
                MessageBox.Show("您没有选择商品", "提示");
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            if (textBox5.Text != "")
            {
                listBox2.Items.Add(textBox5.Text);
            }
            else
            {
                MessageBox.Show("请添加商品", "提示");
            }
        }

        private void button8_MouseClick(object sender, EventArgs e)
        {
            int count = listBox2.SelectedItems.Count;
            List<string> itemValues = new List<string>();

            if (count != 0)
            {
                for (int i = 0; i < count; i++)
                {
                    itemValues.Add(listBox2.SelectedItems[i].ToString());
                }
                foreach (string item in itemValues)
                {
                    listBox2.Items.Remove(item);
                }
            }
            else
            {
                MessageBox.Show("请选择要删除的商品");
            }
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            MessageBox.Show("您选择的专业是：" + comboBox1.Text, "提示");
        }

        private void button10_Click(object sender, EventArgs e)
        {
            if (!string.IsNullOrEmpty(textBox6.Text))
            {
                if (comboBox1.Items.Contains(textBox6.Text))
                {
                    MessageBox.Show("该专业已存在");
                }
                else
                {
                    comboBox1.Items.Add(textBox6.Text);
                }
            }
            else
            {
                MessageBox.Show("请输入专业", "提示");
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            if (!string.IsNullOrEmpty(textBox6.Text))
            {
                if (comboBox1.Items.Contains((string)textBox6.Text))
                {
                    comboBox1.Items.Remove((string)textBox6.Text);
                }
                else
                {
                    MessageBox.Show("输入专业不存在", "提示");
                }
            }
            else
            {
                MessageBox.Show("输入要删除的专业", "提示");
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
            (pictureBox1.Image, pictureBox2.Image) = (pictureBox2.Image, pictureBox1.Image);
        }

        private void button13_Click(object sender, EventArgs e)
        {
            timer1.Start();
        }

        private void button14_Click(object sender, EventArgs e)
        {
            timer1.Stop();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            (pictureBox1.Image, pictureBox2.Image) = (pictureBox2.Image, pictureBox1.Image);
        }

        private void monthCalendar1_DateChanged(object sender, DateRangeEventArgs e)
        {
            textBox7.Text = monthCalendar1.SelectionStart.ToShortDateString();
            calendar_msg = monthCalendar1.SelectionEnd.ToLongDateString();
        }

        private void button15_Click(object sender, EventArgs e)
        {
            MessageBox.Show(calendar_msg, "提示");
        }

        private void 测试ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MessageBox.Show("你打开了窗口", "提示");
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            Point p = e.Location;
            //toolStripStatusLabel1.Text = "行 " + p.X.ToString() + ",列 " + p.Y.ToString();
            toolStripStatusLabel1.Text = string.Format("行 {0}, 列 {1}", e.X, e.Y);
        }

        private void 帮助HToolStripMenuItem_Click(object sender, EventArgs e)
        {
            AboutBox1 about = new AboutBox1();
            about.ShowDialog();
        }

        private void button16_Click(object sender, EventArgs e)
        {
            DialogResult dr = cd1.ShowDialog();
            if (dr == DialogResult.OK)
            {
                richTextBox1.ForeColor = cd1.Color;
            }
        }

        private void button17_Click(object sender, EventArgs e)
        {
            DialogResult dr = fontDialog1.ShowDialog();
            if (dr == DialogResult.OK)
            {
                richTextBox1.Font = fontDialog1.Font;
            }
        }

        private void button18_Click(object sender, EventArgs e)
        {
            DialogResult dr = openFileDialog1.ShowDialog();
            string filename = openFileDialog1.FileName;
            if (dr == DialogResult.OK && !string.IsNullOrEmpty(filename))
            {
                StreamReader sr = new StreamReader(filename);
                richTextBox2.Text = sr.ReadToEnd();
                sr.Close();
            }
        }

        private void button19_Click(object sender, EventArgs e)
        {
            DialogResult dr = saveFileDialog1.ShowDialog();
            string filename = saveFileDialog1.FileName;
            if (dr == DialogResult.OK && !string.IsNullOrEmpty(filename))
            {
                StreamWriter sr = new StreamWriter(filename);
                sr.Write(richTextBox2.Text);
                sr.Close();
            }
        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            textBox8.Text = numericUpDown1.Value.ToString();
        }
    }
}
