from flask import Flask, render_template

app  = Flask(__name__)

frettaListi =  [
        {
            "id": 0,
            "flokkur": "almennt",
            "hofundur": "dsg",
            "fyrirsogn": "FlÃ³rens veldur usla Ã¡ FlÃ³rÃ­da",
            "meginmal": "ÃžaÃ° er bara helv... vesen Ã¡ fellibylnum og allt Ã­ klessu Ã­ FlÃ³rÃ­da.  MilljÃ³nir manna Ã¾urftu aÃ° yfirgefa heimili sin vegna yfirvofandi eyÃ°ileggingar FlÃ³rensar...",
            "mynd": "mynd0.jpg",
        },
        {
            "id": 1,
            "flokkur": "veidi",
            "hofundur": "gjg",
            "fyrirsogn": "VeiÃ°in er drÃ¦m Ã¾etta haustiÃ°",
            "meginmal": "VeiÃ°in hefur heldur veriÃ° dÃ¶pur Ã¾etta haustiÃ° Ã¾rÃ¡tt fyrir Ã¡gÃ¦tis rigninar upp Ã¡ sÃ­Ã°kastiÃ°...",
            "mynd": "mynd1.jpg",
        },
        {
            "id": 2,
            "flokkur": "sport",
            "hofundur": "gus",
            "fyrirsogn": "Ã“lafÃ­a stendur sig vel",
            "meginmal": "Ã“lafÃ­a er komin Ã­ 65 sÃ¦ti peningalistans og hefur Ã¾vÃ­ tryggt sÃ©r keppnisrÃ©tt Ã¡ LPG mÃ³tarÃ¶Ã°inni Ã¡ komandi keppnistimabili...",
            "mynd": "mynd2.jpg",
        },
        {
            "id": 3,
            "flokkur": "sport",
            "hofundur": "gus",
            "fyrirsogn": "Ãsland dottiÃ° Ãºr leik",
            "meginmal": "Ãslenska karlalandsliÃ°iÃ° Ã­ kÃ¶rfubolta er dottiÃ° Ãºr leik a Eurobasket Ã¾rÃ¡tt fyrir Ã¡gÃ¦tis spretti inn a milli.  Ãsland spilaÃ°i lokaleik sinn Ã¡ mÃ³tinu fyrir troÃ°fullri hÃ¶ll gegn heimamÃ¶nnum Finnum..",
            "mynd": "mynd3.jpg",
        },
        {
            "id": 4,
            "flokkur": "almennt",
            "hofundur": "dsg",
            "fyrirsogn": "Allt aÃ° 21 stigs hiti Ã­ dag",
            "meginmal": "LitlÂ­ar breytÂ­ingÂ­ar verÃ°a Ã­ veÃ°rinu Ã­ dag, samÂ­kvÃ¦mt hugÂ­leiÃ°ingÂ­um veÃ°urÂ­frÃ¦Ã°ings VeÃ°urÂ­stofu Ãslands.SuÃ°vestanÃ¡tt rÃ­kÂ­ir Ã¡ landÂ­inu, yfÂ­irÂ­leitt Ã¡ bilÂ­inu 5-13 m/â€‹s. VÃ­Ã°a er lÃ©ttÂ­skÃ½jaÃ° Ã¡ austÂ­urÂ­hluta landsÂ­ins en Ã¾ungÂ­bÃºiÃ° og dÃ¡Â­lÃ­tÂ­il rignÂ­ing eÃ°a sÃºld meÃ° kÃ¶flÂ­um sunnÂ­an- og vestÂ­anÂ­til. Hiti verÃ°ur Ã¡ bilÂ­inu 11 til 21 stig, hlÃ½jÂ­ast austÂ­ast Ã¡ landÂ­inu.LitlÂ­ar breytÂ­ingÂ­ar verÃ°a Ã­ veÃ°rinu nÃ¦stu daga en ÃºtÂ­lit er fyrÂ­ir aÃ° Ã¾aÃ° dragi Ãºr suÃ°vestanÃ¡ttÂ­inni Ã­ lok vikÂ­unnÂ­ar.",
            "mynd": "mynd4.jpg",
        },
                {
            "id": 5,
            "flokkur": "veidi",
            "hofundur": "gjg",
            "fyrirsogn": "LifnaÃ°i yfir KjÃ³sinni eftir rigningu",
            "meginmal": "MargÂ­ar Ã¡r eru bÃºnÂ­ar aÃ° vera afar vatnsÂ­litlÂ­ar Ã­ sumÂ­ar og eiga inni hvaÃ° varÃ°ar veiÃ°ina. LaxÃ¡ Ã­ DÃ¶lÂ­um er til dÃ¦mÂ­is Ã¾ekkt fyrÂ­ir gÃ³Ã°an endaÂ­sprett og er Ã¾Ã¡ bundÂ­in viÃ° haustrignÂ­ingÂ­ar. Ãžar hefÂ­ur ekki enn rignt en Ã¾aÃ° er svipaÃ° og aÃ° spila Ã­ lottÃ³Â­inu aÃ° kaupa leyfi Ã­ DÃ¶lÂ­unÂ­um sÃ­Ã°sumÂ­ars eÃ°a Ã¡ haustÂ­dÃ¶gÂ­um. Ãžar er hÃ¦gt aÃ° vinna stÃ³ra vinnÂ­inga ef menn hitta Ã¡ rignÂ­ingu sem gerÂ­ir Ã¾aÃ° aÃ° verkÂ­um aÃ° laxÂ­inn lÃ¦tÂ­ur sig loksÂ­ins vaÃ°a upp Ã­ Ã¡na og Ã¾eir sem eru fyrÂ­ir fÃ¡ sÃºrÂ­efni.",
            "mynd": "mynd5.jpg",
        }
    ]

@app.route('/')
def index():
    return render_template('index.html', f1 = frettaListi)

    
@app.route('/frett/<int:id>')
def frett(id):
    frett = frettaListi[id]
    return render_template('drett.html', frett=frett)

@app.route('/frettalokkur/<flokkur>')
def frettaflokkur(flokkur):
    return render_template('frettaflokkur.html', flokku=flokkur,f1 = frettaListi)

@app.errorhandler(404)
def villa(error):
    return render_template('villusida.html')

if __name__ == '__main__':
    app.run(debug=True)
