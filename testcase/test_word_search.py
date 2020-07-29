import sys
sys.path.append("..")
import pytest
import allure
from base.browser import Browser
from po.googletranspage import TranHomePage
from po.googleimagepage import ImageHomePage
from po.googlevideopage import VideoHomePage
from po.enlargepage import EnlargeHomePage


@allure.feature("单词学习")
class TestWordLearn:
    @classmethod
    def setup_class(cls):
        browse = Browser(cls)
        cls.driver = browse.get_driver()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    wordlist_RE1 = ['climate', 'complete', 'fairly', 'giant', 'heavy', 'hunter', 'in reality', 'museum', 'physical',
     'relative', 'appearance', 'dig up', 'estimate', 'examine', 'extend', 'length', 'mystery',
     'opinion', 'seek', 'terrible', 'although', 'appropriate', 'collect', 'magical', 'memorize', 'primarily',
     'publish', 'reflect', 'scary', 'text', 'accidental', 'affect', 'deep',
     'determined', 'hide', 'immediate', 'recognize','shock', 'sudden', 'youth', 'illegal', 'law',
     'locate', 'preserve', 'valuable', 'rare', 'weigh', 'treasure', 'collector', 'in demand destroy',
     'middle', 'race', 'equipment', 'limit', 'majority', 'height', 'employed', 'capable', 'occupation',
     'accomplish', 'construction', 'network', 'currency', 'protect', 'expose', 'technique', 'reveal', 'apply',
     'vivid', 'timeless', 'confirm', 'ordinary', 'according to','involve', 'task', 'role', 'block', 'compete',
     'proud', 'average', 'freedom', 'equality', 'divide', 'income', 'steal', 'purchase', 'bury', 'factor', 'disease',
     'pretend', 'sail', 'shoot', 'avoid', 'terrorize', 'transfer', 'fearless', 'target', 'fail', 'respect', 'approach',
     'bright', 'shine', 'response', 'effort', 'flight', 'headed', 'crash', 'investigate', 'disappearance']

    wordlist_RE2_Unit3 = [('analyze', 'to study (something) closely and carefully'),
                          ('attach', 'to be or become joined or connected'),
                          ('conduct', 'to plan and do (something, such as an activity)'),
                          ('effective', 'producing a result that is wanted'),
                          ('injury', 'harm or damage'),
                          ('luxurious', 'very comfortable and expensive'),
                          ('murder', 'the crime of deliberately killing a person'),
                          ('offer', 'to present or put forward'),
                          ('rule out', 'exclude'),
                          ('vulnerable', 'easily hurt or harmed'),
                          ('beneath', ' in a lower position'),
                          ('cruelly', ' in a manner that willingly or knowingly causing pain or distress'),
                          ('debatable', ' open to question'),
                          ('deduce', 'to use logic or reason to decide something'),
                          ('enable', 'to make (something) possible'),
                          ('frozen', ' turned into ice'),
                          ('implies', 'to express (something) in an indirect way'),
                          ('indicate', 'show'),
                          ('laborer', 'a person who does hard physical work for money'),
                          ('gruesome', 'unpleasant and shocking'),
                          ('carbon dating', 'a scientific method of finding out exactly how old an object is'),
                          ('copper', 'is a soft reddish brown metal'),
                          ('shepherd', 'is a person whose job is to take care of sheep'),
                          ('flee', 'escape'),
                          ('exposure', 'is the harmful effect on your body from very cold weather')
                          ]
    wordlist_RE2_Unit4B = [('face', 'impression from people situation'),
                          ('series', 'a group of events or actions that are planned to happen one after the other'),
                          ('basis', 'major'),
                          ('self-defence', 'to protect yourself'),
                          ('ensure', 'make sure'),
                          ('publicity', 'advertisement'),
                          ('accept', 'to agree'),
                          ('violence', 'behaviour that is to hurt someone'),
                          ('entertain', 'to make feel happy or funny'),
                          ('discipline', 'train (someone) to obey rules'),
                          ('endure', 'suffer (something painful or difficult) patiently'),
                          ('take turn doing', 'one by one'),
                          ('jealous', 'someone wants something the other person has'),
                           ('reserved', 'something is kept for a particular purpose'),
                           ('reunite', 'meet again after being separated'),
                           ('ceremony', 'formal event, such as a wedding'),
                           ('demonstrate', 'make it clear to other people, let other people to understand it'),
                           ('approve', 'think it good'),
                          ]

    frenchword = [("ne… que", "seulement", "Je ne bois que de l'eau."),
                  # ("Antiquité", "Les plus anciennes civilisations à écritures."),
                  # ("avoir lieu", "se passer, exister (à un endroit, à un moment)."),
                  # ("compétition", "Épreuve sportive disputée entre plusieurs concurrents."),
                  # ("course", "Action de courir"),("dédié", "Consacrer, vouer."),
                  # ("vainqueur", "Gagnant."),
                  # ("épreuve", "Compétition"),
                  # ("gagnant", "Qui gagne ou qui remporte une épreuve."),
                  # ("discipline", "domaine, activités sportives, épreuves"),
                  # ("récompense", "Bien matériel ou moral donné ou reçu pour une bonne action, un service rendu, des mérites."),
                  # ("couronne", "Cercle que l'on met autour de la tête comme parure ou marque d'honneur."),
                  # ("laurier", "Arbre à feuilles allongées")
                  ]

    wordlist4 = ['fairly', 'in reality', 'physical', 'relative', 'extend', 'although', 'memorize', 'primarily',
                 'determined', 'immediate', 'locate', 'in demand', 'technique', 'purchase', 'terrorize', 'disappearance']

    @allure.story("搜索单词解释并发音,放大拼写,查找单词图片,查找单词视频")
    @pytest.mark.parametrize("search_char, meaning ", wordlist_RE2_Unit4B)
    def test_words_search(self, search_char, meaning):
        READ = 1
        LOOK = 1
        WATCH = 20

        #放大拼写
        enlargepage = EnlargeHomePage(self.driver)
        enlargepage.open_homepage()
        enlargepage.search(search_char, LOOK)
        #搜索单词解释并发音
        googletranspage = TranHomePage(self.driver)
        googletranspage.open_homepage()
        googletranspage.search(search_char, READ)
        googletranspage.listen()
        googletranspage.listen_tran(1)
        #翻译
        googletranspage.search(meaning, READ)
        googletranspage.listen(period=READ)
        #例句
        # googletranspage.search(example, READ)
        # googletranspage.listen(period=READ)
        #同义词
        #syn_word = googletranspage.get_syn_word()
        #googletranspage.read_syn_word(syn_word)
        #放大拼写
        # enlargepage = EnlargeHomePage(self.driver)
        # enlargepage.open_homepage()
        # enlargepage.search(search_char, LOOK)
        #查找单词图片
        googleimagepage = ImageHomePage(self.driver)
        googleimagepage.open_homepage()
        googleimagepage.search(search_char, LOOK)
        googleimagepage.clickfirstimage(READ)
        #搜索结果截图
        googleimagepage.screenshot(search_char)
        #查找单词视频
        # googlevideopage = VideoHomePage(self.driver)
        # googlevideopage.open_homepage()
        # googlevideopage.search(search_char, LOOK)
        # googlevideopage.play(WATCH)


if __name__ == '__main__':
    pytest.main()