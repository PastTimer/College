using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;
using System.Xml.Linq;

namespace form_college
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        public void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        public void label1_Click(object sender, EventArgs e)
        {

        }

        public void label3_Click(object sender, EventArgs e)
        {

        }

        public void label4_Click(object sender, EventArgs e)
        {

        }

        public void label10_Click(object sender, EventArgs e)
        {

        }

        public void checkBox2_CheckedChanged(object sender, EventArgs e)
        {

        }

        public void label13_Click(object sender, EventArgs e)
        {
            
        }

        public void label5_Click(object sender, EventArgs e)
        {
            
        }

        public void textBox1_Enter(object sender, EventArgs e)
        {

        }

        private void textBox2_Enter(object sender, EventArgs e)
        {
            if (textBox2.Text == "First Name")
            {
                textBox2.Text = "";
                textBox2.ForeColor = Color.Black;
            }
        }

        private void textBox2_Leave(object sender, EventArgs e)
        {
            if (textBox2.Text == "")
            {
                textBox2.Text = "First Name";
                textBox2.ForeColor = Color.LightGray;
            }

        }

        private void textBox3_Enter(object sender, EventArgs e)
        {
            if (textBox3.Text == "M.I.")
            {
                textBox3.Text = "";
                textBox3.ForeColor = Color.Black;
            }

        }

        private void textBox3_Leave(object sender, EventArgs e)
        {
            if (textBox3.Text == "")
            {
                textBox3.Text = "M.I.";
                textBox3.ForeColor = Color.LightGray;
            }
        }

        private void lastname_Enter(object sender, EventArgs e)
        {
            if (lastname.Text == "Last Name")
            {
                lastname.Text = "";
                lastname.ForeColor = Color.Black;
            }

        }

        private void lastname_Leave(object sender, EventArgs e)
        {
            if (lastname.Text == "")
            {
                lastname.Text = "Last Name";
                lastname.ForeColor = Color.LightGray;
            }

        }

        private void txt1_Enter(object sender, EventArgs e)
        {
            if (txt1.Text == "Ethnicity")
            {
                txt1.Text = "";
                txt1.ForeColor = Color.Black;
            }
        }

        private void txt1_Leave(object sender, EventArgs e)
        {
            if (txt1.Text == "")
            {
                txt1.Text = "Ethnicity";
                txt1.ForeColor = Color.LightGray;
            }
        }

        private void current1_Enter(object sender, EventArgs e)
        {
            if (current1.Text == "Block and Lot number, Village, Street Address, Barangay")
            {
                current1.Text = "";
                current1.ForeColor = Color.Black;
            }
        }

        private void current1_Leave(object sender, EventArgs e)
        {
            if (current1.Text == "")
            {
                current1.Text = "Block and Lot number, Village, Street Address, Barangay";
                current1.ForeColor = Color.LightGray;
            }
        }

        private void current2_Enter(object sender, EventArgs e)
        {
            if (current2.Text == "City, Province")
            {
                current2.Text = "";
                current2.ForeColor = Color.Black;
            }
        }

        private void current2_Leave(object sender, EventArgs e)
        {
            if (current2.Text == "")
            {
                current2.Text = "City, Province";
                current2.ForeColor = Color.LightGray;
            }
        }

        private void current3_Enter(object sender, EventArgs e)
        {
            if (current3.Text == "Zip Code")
            {
                current3.Text = "";
                current3.ForeColor = Color.Black;
            }
        }

        private void current3_Leave(object sender, EventArgs e)
        {
            if (current3.Text == "")
            {
                current3.Text = "Zip Code";
                current3.ForeColor = Color.LightGray;
            }
        }

        private void textBox6_Enter(object sender, EventArgs e)
        {
            if (textBox6.Text == "Block and Lot number, Village, Street Address, Barangay")
            {
                textBox6.Text = "";
                textBox6.ForeColor = Color.Black;
            }
        }

        private void textBox6_Leave(object sender, EventArgs e)
        {
            if (textBox6.Text == "")
            {
                textBox6.Text = "Block and Lot number, Village, Street Address, Barangay";
                textBox6.ForeColor = Color.LightGray;
            }
        }

        private void textBox20_Enter(object sender, EventArgs e)
        {
            if (textBox20.Text == "City, Province")
            {
                textBox20.Text = "";
                textBox20.ForeColor = Color.Black;
            }
        }

        private void textBox20_Leave(object sender, EventArgs e)
        {
            if (textBox20.Text == "")
            {
                textBox20.Text = "City, Province";
                textBox20.ForeColor = Color.LightGray;
            }
        }

        private void textBox21_Enter(object sender, EventArgs e)
        {
            if (textBox21.Text == "Zip Code")
            {
                textBox21.Text = "";
                textBox21.ForeColor = Color.Black;
            }
        }

        private void textBox21_Leave(object sender, EventArgs e)
        {
            if (textBox21.Text == "")
            {
                textBox21.Text = "Zip Code";
                textBox21.ForeColor = Color.LightGray;
            }
        }

        private void textBox17_Enter(object sender, EventArgs e)
        {
            if (textBox17.Text == "Full Name")
            {
                textBox17.Text = "";
                textBox17.ForeColor = Color.Black;
            }
        }

        private void textBox17_Leave(object sender, EventArgs e)
        {   
            if (textBox17.Text == "")
            {
                textBox17.Text = "Full Name";
                textBox17.ForeColor = Color.LightGray;
            }
        }

        private void num_Enter(object sender, EventArgs e)
        {
            if (num.Text == "Contact No.")
            {
                num.Text = "";
                num.ForeColor = Color.Black;
            }
        }

        private void num_Leave(object sender, EventArgs e)
        {
            if (num.Text == "")
            {
                num.Text = "Contact No.";
                num.ForeColor = Color.LightGray;
            }
        }

        private void textBox4_Enter(object sender, EventArgs e)
        {
            if (textBox4.Text == "+63 9XXX-XXX-XXX")
            {
                textBox4.Text = "";
                textBox4.ForeColor = Color.Black;
            }
        }

        private void textBox4_Leave(object sender, EventArgs e)
        {
            if (textBox4.Text == "")
            {
                textBox4.Text = "+63 9XXX-XXX-XXX";
                textBox4.ForeColor = Color.LightGray;
            }
        }

        private void textBox5_Enter(object sender, EventArgs e)
        {
            if (textBox5.Text == "someone@email.com")
            {
                textBox5.Text = "";
                textBox5.ForeColor = Color.Black;
            }
        }

        private void textBox5_Leave(object sender, EventArgs e)
        {
            if (textBox5.Text == "")
            {
                textBox5.Text = "someone@email.com";
                textBox5.ForeColor = Color.LightGray;
            }
        }

        private void fnamem_Enter(object sender, EventArgs e)
        {
            if (fnamem.Text == "First Name")
            {
                fnamem.Text = "";
                fnamem.ForeColor = Color.Black;
            }
        }

        private void fnamem_Leave(object sender, EventArgs e)
        {
            if (fnamem.Text == "")
            {
                fnamem.Text = "First Name";
                fnamem.ForeColor = Color.LightGray;
            }
        }

        private void lnamem_Enter(object sender, EventArgs e)
        {
            if (lnamem.Text == "Last Name")
            {
                lnamem.Text = "";
                lnamem.ForeColor = Color.Black;
            }
        }

        private void lnamem_Leave(object sender, EventArgs e)
        {
            if (lnamem.Text == "")
            {
                lnamem.Text = "Last Name";
                lnamem.ForeColor = Color.LightGray;
            }
        }

        private void mim_Enter(object sender, EventArgs e)
        {
            if (mim.Text == "M.I.")
            {
                mim.Text = "";
                mim.ForeColor = Color.Black;
            }
        }

        private void mim_Leave(object sender, EventArgs e)
        {
            if (mim.Text == "")
            {
                mim.Text = "M.I.";
                mim.ForeColor = Color.LightGray;
            }
        }

        private void fnamef_Enter(object sender, EventArgs e)
        {
            if (fnamef.Text == "First Name")
            {
                fnamef.Text = "";
                fnamef.ForeColor = Color.Black;
            }
        }

        private void fnamef_Leave(object sender, EventArgs e)
        {
            if (fnamef.Text == "")
            {
                fnamef.Text = "First Name";
                fnamef.ForeColor = Color.LightGray;
            }
        }

        private void lnamef_Enter(object sender, EventArgs e)
        {
            if (lnamef.Text == "Last Name")
            {
                lnamef.Text = "";
                lnamef.ForeColor = Color.Black;
            }
        }

        private void lnamef_Leave(object sender, EventArgs e)
        {
            if (lnamef.Text == "")
            {
                lnamef.Text = "Last Name";
                lnamef.ForeColor = Color.LightGray;
            }
        }

        private void mif_Enter(object sender, EventArgs e)
        {
            if (mif.Text == "M.I.")
            {
                mif.Text = "";
                mif.ForeColor = Color.Black;
            }
        }

        private void mif_Leave(object sender, EventArgs e)
        {
            if (mif.Text == "")
            {
                mif.Text = "M.I.";
                mif.ForeColor = Color.LightGray;
            }
        }
        private void next_Click(object sender, EventArgs e)
        {
            mif.Text = String.Empty;
            mif.ForeColor = Color.Black;
            textBox2.Text = "";
            textBox2.ForeColor = Color.Black;
            textBox3.Text = "";
            textBox3.ForeColor = Color.Black;
            lastname.Text = "";
            lastname.ForeColor = Color.Black;
            txt1.Text = "";
            txt1.ForeColor = Color.Black;
            current1.Text = "";
            current1.ForeColor = Color.Black;
            current2.Text = "";
            current2.ForeColor = Color.Black;
            current3.Text = "";
            current3.ForeColor = Color.Black;
            textBox6.Text = "";
            textBox6.ForeColor = Color.Black;
            textBox20.Text = "";
            textBox20.ForeColor = Color.Black;
            textBox21.Text = "";
            textBox21.ForeColor = Color.Black;
            textBox17.Text = "";
            textBox17.ForeColor = Color.Black;
            num.Text = "";
            num.ForeColor = Color.Black;
            textBox4.Text = "";
            textBox4.ForeColor = Color.Black;
            textBox5.Text = "";
            textBox5.ForeColor = Color.Black;
            fnamem.Text = "";
            fnamem.ForeColor = Color.Black;
            lnamem.Text = "";
            lnamem.ForeColor = Color.Black;
            mim.Text = "";
            mim.ForeColor = Color.Black;
            fnamef.Text = "";
            fnamef.ForeColor = Color.Black;
            lnamef.Text = "";
            fnamef.ForeColor = Color.Black;
        }
    }
}