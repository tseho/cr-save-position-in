# -*- coding: utf-8 -*-

import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
from System.Windows.Forms import *
from System.Drawing import *

class askForm(Form):
    def __init__(self, selectedBooks):
        self._selectedBooks = selectedBooks
        #
        # label1
        #
        self.label1 = Label()
        self.label1.AutoSize = True
        self.label1.Location = Point(13, 13)
        self.label1.Name = "label1"
        self.label1.Size = Size(149, 13)
        self.label1.TabIndex = 0
        self.label1.Text = "Name of the custom property :"
        #
        # textBox1
        #
        self.textBox1 = TextBox()
        self.textBox1.Location = Point(16, 39)
        self.textBox1.Name = "textBox1"
        self.textBox1.Size = Size(256, 20)
        self.textBox1.TabIndex = 1
        self.textBox1.Text = "Saved Position"
        self.textBox1.KeyDown += self.textBox1_KeyDown
        #
        # button1
        #
        self.button1 = Button()
        self.button1.Location = Point(196, 72)
        self.button1.Name = "button1"
        self.button1.Size = Size(75, 34)
        self.button1.TabIndex = 2
        self.button1.Text = "Apply"
        self.button1.UseVisualStyleBackColor = True
        self.button1.Click += self.button1_Click
        #
        # button2
        #
        self.button2 = Button()
        self.button2.Location = Point(115, 72)
        self.button2.Name = "button2"
        self.button2.Size = Size(75, 34)
        self.button2.TabIndex = 3
        self.button2.Text = "Cancel"
        self.button2.UseVisualStyleBackColor = True
        self.button2.Click += self.button2_Click
        #
        # Form1
        #
        AutoScaleDimensions = SizeF(6, 13)
        self.ClientSize = Size(284, 118)
        self.StartPosition = FormStartPosition.CenterParent
        self.Controls.Add(self.button2)
        self.Controls.Add(self.button1)
        self.Controls.Add(self.textBox1)
        self.Controls.Add(self.label1)
        self.Name = "Form1"
        self.Text = "Save Position In"

    def textBox1_KeyDown(self, sender, e):
        if e.KeyCode == Keys.Enter:
            self.process()

    def button1_Click(self, sender, e):
        self.process()

    def button2_Click(self, sender, e):
        self.Close()

    def process(self):
        selectedBooks = self._selectedBooks
        propertyName = self.textBox1.Text

        if propertyName == '':
            pass

        position = 0
        for book in selectedBooks:
            position += 1
            book.SetCustomValue(propertyName, str(position))
        MessageBox.Show("Saved the current order into the property \"{}\" for the {} selected issues".format(propertyName, position), 'Save Position In')
        self.Close()

#@Name Save Position In
#@Key SavePositionIn
#@Hook Books
#@Description Save the position of each book from the selection into a custom field
def SavePositionIn(selectedBooks):
    form = askForm(selectedBooks)
    form.ShowDialog(ComicRack.MainWindow)
