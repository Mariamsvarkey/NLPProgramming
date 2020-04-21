{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package punkt to\n",
      "[nltk_data]     C:\\Users\\Maria\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package punkt is already up-to-date!\n"
     ]
    }
   ],
   "source": [
    "import nltk\n",
    "nltk.download('punkt')\n",
    "from nltk.tokenize import sent_tokenize"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nltk.tokenize import word_tokenize"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting python-docx\n",
      "  Downloading https://files.pythonhosted.org/packages/e4/83/c66a1934ed5ed8ab1dbb9931f1779079f8bca0f6bbc5793c06c4b5e7d671/python-docx-0.8.10.tar.gz (5.5MB)\n",
      "Requirement already satisfied: lxml>=2.3.2 in c:\\users\\maria\\anaconda3\\lib\\site-packages (from python-docx)\n",
      "Building wheels for collected packages: python-docx\n",
      "  Running setup.py bdist_wheel for python-docx: started\n",
      "  Running setup.py bdist_wheel for python-docx: finished with status 'done'\n",
      "  Stored in directory: C:\\Users\\Maria\\AppData\\Local\\pip\\Cache\\wheels\\18\\0b\\a0\\1dd62ff812c857c9e487f27d80d53d2b40531bec1acecfa47b\n",
      "Successfully built python-docx\n",
      "Installing collected packages: python-docx\n",
      "Successfully installed python-docx-0.8.10\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "You are using pip version 9.0.3, however version 19.3.1 is available.\n",
      "You should consider upgrading via the 'python -m pip install --upgrade pip' command.\n"
     ]
    }
   ],
   "source": [
    "pip install --pre python-docx"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "import docx\n",
    "from docx import Document"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "doc = Document('doc.docx')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "text = doc.paragraphs[0].text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Born into an aristocratic\\xa0\\xa0family of\\xa0, Vivekananda was inclined towards spirituality.', 'He was influenced by his\\xa0, Ramakrishna, from whom he learnt that all living beings were an embodiment of the divine self; therefore, service to God could be rendered by service to humankind.', \"After Ramakrishna's death, Vivekananda toured the\\xa0\\xa0extensively and acquired first-hand knowledge of the conditions prevailing in\\xa0.\", \"He later travelled to the United States, representing India at the 1893 Parliament of the World's Religions.\", 'Vivekananda conducted hundreds of public and private lectures and classes, disseminating tenets of\\xa0\\xa0in the United States, England and Europe.', 'In India, Vivekananda is regarded as a\\xa0, and his birthday is celebrated as\\xa0.']\n"
     ]
    }
   ],
   "source": [
    "print(sent_tokenize(text))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Born', 'into', 'an', 'aristocratic', 'family', 'of', ',', 'Vivekananda', 'was', 'inclined', 'towards', 'spirituality', '.', 'He', 'was', 'influenced', 'by', 'his', ',', 'Ramakrishna', ',', 'from', 'whom', 'he', 'learnt', 'that', 'all', 'living', 'beings', 'were', 'an', 'embodiment', 'of', 'the', 'divine', 'self', ';', 'therefore', ',', 'service', 'to', 'God', 'could', 'be', 'rendered', 'by', 'service', 'to', 'humankind', '.', 'After', 'Ramakrishna', \"'s\", 'death', ',', 'Vivekananda', 'toured', 'the', 'extensively', 'and', 'acquired', 'first-hand', 'knowledge', 'of', 'the', 'conditions', 'prevailing', 'in', '.', 'He', 'later', 'travelled', 'to', 'the', 'United', 'States', ',', 'representing', 'India', 'at', 'the', '1893', 'Parliament', 'of', 'the', 'World', \"'s\", 'Religions', '.', 'Vivekananda', 'conducted', 'hundreds', 'of', 'public', 'and', 'private', 'lectures', 'and', 'classes', ',', 'disseminating', 'tenets', 'of', 'in', 'the', 'United', 'States', ',', 'England', 'and', 'Europe', '.', 'In', 'India', ',', 'Vivekananda', 'is', 'regarded', 'as', 'a', ',', 'and', 'his', 'birthday', 'is', 'celebrated', 'as', '.']\n"
     ]
    }
   ],
   "source": [
    "print(word_tokenize(text))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
