import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image

def calWordFreqencies():
    excludes = {"将军","却说","丞相"}
    txt = open("三国演义.txt", "r", encoding='utf-8').read()
    words = jieba.lcut(txt)
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    for word in excludes:
        del (counts[word])

    return counts

def drawWordcloudPlot(counts):
    coloring = np.array(Image.open("E:/baidupic/alice_color.png"))
    wc = WordCloud(background_color="white",
                             max_words=2000,
                             mask=coloring,
                             max_font_size=60,
                             random_state=42,
                             scale=2,
                             font_path="c:/Windows/Fonts/SimHei.ttf")
    wc.generate_from_frequencies(counts)
    image_colors = ImageColorGenerator(coloring)

    plt.imshow(wc)
    plt.axis("off")
    plt.show()
def main():
    counts = calWordFreqencies()
    drawWordcloudPlot(counts)

main()