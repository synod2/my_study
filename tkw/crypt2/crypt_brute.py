from Crypto.Util.number import *


g =1468
h =13176937611470940769675424427237214361327027262801017230328464476187661764921664954701796966426482598685480847329992216474898047298138546932927013411286080877561831522628228420965755215837424657249966873002314137994287169213354516263406270423795978394635388801400699885714033340665899016561199970830561882935631759522528099622669587315882980737349844878337007525538293173251532224267379685239505646821600410765279043812411429818495529092434724758640978876122625789495327928210547087547860489325326144621483366895679471870087870408957451137227143277719799927169623974008653573716761024220674229810095209914374390011024349L
A =22171697832053348372915156043907956018090374461486719823366788630982715459384574553995928805167650346479356982401578161672693725423656918877111472214422442822321625228790031176477006387102261114291881317978365738605597034007565240733234828473235498045060301370063576730214239276663597216959028938702407690674202957249530224200656409763758677312265502252459474165905940522616924153211785956678275565280913390459395819438405830015823251969534345394385537526648860230429494250071276556746938056133344210445379647457181241674557283446678737258648530017213913802458974971453566678233726954727138234790969492546826523537158L
B =21251918005448659289449540367076207273003136102402948519268321486936734267649761131906829634666742021555542747288804916060499331412675118289617172656894696939180508678248554638496093176525353583495353834532364036007392039073993229985968415793651145047522785446635657509992391925580677770086168373498842908951372029092354946478354834120976530860456422386647226785585577733215760931557612319244940761622252983954745116260878050222286503437408510241127875494413228131438716950664031868505118149350877745316461481208779725275726026031260556779604902294937659461052089402100729217965841272238065302532882861094831960922472L
p =36416598149204678746613774367335394418818540686081178949292703167146103769686977098311936910892255381505012076996538695563763728453722792393508239790798417928810924208352785963037070885776153765280985533615624550198273407375650747001758391126814998498088382510133441013074771543464269812056636761840445695357746189203973350947418017496096468209755162029601945293367109584953080901393887040618021500119075628542529750701055865457182596931680189830763274025951607252183893164091069436120579097006203008253591406223666572333518943654621052210438476603030156263623221155480270748529488292790643952121391019941280923396132717L
q =22703614806237330889410083770159223453128766013766321040706174044355426290328539338099711291079959714155244437030261032146984868113293511467274463709974076015468157237127672046781216262952714317506848836418718547505157984648161313592118697709984413028733405554946035544310954827596178187067728654513993575659442761349110567922330434847940441527278779320200714023296202983137830985906413366968841334238825204827013560287441312629166207563391639545363637173286538187147065563647798900324550559230799880457351250762884396716657695545274970206009025313609823106997020670498921913048309409470476279377425822906035488401579L

def exeu(a, b): 
    r = [a, b] 
    s = [1, 0] 
    t = [0, 1] 
    while r[-1] != 0: 
        q = int(r[-2] / r[-1]) 
        r.append(r[-2] - q * r[-1]) 
        s.append(s[-2] - q * s[-1])
        t.append(t[-2] - q * t[-1]) 
    return (r[-2], s[-2], t[-2])
    
print exeu(9,14)