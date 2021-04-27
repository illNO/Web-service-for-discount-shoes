import requests
from bs4 import BeautifulSoup
import re
import json
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def remove_tags(text):
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub('', text)


headers = {
        # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
}

url_outlet = 'https://www.asos.com/men/outlet/shoes-trainers/cat/?cid=27437&nlid=mw|outlet|shop+by+product|shoes+%26+trainers' + f'&page=1'


url = 'https://www.asos.com/adidas-originals/' \
      'adidas-originals-nmdr1-trainers-in-off-' \
      'white/prd/22822790?ctaref=we+recommend+car' \
      'ousel_9&featureref1=we+recommend+pers'
urls = ['https://www.asos.com/adidas-originals/adidas-originals-lowertree-trainers-in-green-white-and-red/prd/22002450?colourwayid=60342291&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-nite-jogger-in-silver/prd/22002451?colourwayid=60342276&SearchQuery=&cid=27437', 'https://www.asos.com/adidas/adidas-ultraboost-srdy-trainers-in-white-sky-tint-black/prd/21070605?colourwayid=60138064&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-xplr-trainers-in-core-black-white/prd/21069727?colourwayid=60137988&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-sl-72-trainers-in-white/prd/14686673?colourwayid=16636338&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-rivalry-hi-top-trainers-in-white-and-purple/prd/12906345?colourwayid=16424366&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-yung-1-trainers-in-grey/prd/11425775?colourwayid=16312575&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-lx-con-trainers-in-chalk-with-black-stripes/prd/21378121?colourwayid=60162331&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-superstar-trainers-los-angeles-city-series/prd/13600938?colourwayid=16550591&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-delpala-trainers-in-white/prd/20754081?colourwayid=60085360&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-campus-trainers-in-black/prd/20753473?colourwayid=60085352&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-superstar-trainers-in-navy/prd/20752827?colourwayid=60085310&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-delpala-trainers-in-grey/prd/20754419?colourwayid=60085393&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-campus-80s-trainers-in-green/prd/20752026?colourwayid=60085268&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-performance/adidas-running-ultraboost-20-trainers-in-green/prd/20730475?colourwayid=60083161&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-supercourt-trainers-in-white-team-royal-blue/prd/21070587?colourwayid=60138060&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-campus-trainers-in-dark-blue-white/prd/21046381?colourwayid=60136419&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-continental-80-trainers-in-white-grey-collegiate-navy/prd/21070613?colourwayid=60138068&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-vegan-stan-smith-trainers-in-white-and-green/prd/14685419?colourwayid=16636294&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-team-court-trainers-in-black/prd/21071352?colourwayid=60138093&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-rivalry-low-trainers-in-off-white/prd/14350490?colourwayid=16609832&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-zx-flux-trainers-in-white/prd/13176434?colourwayid=16449813&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-nite-jogger-trainers-in-silver/prd/13600930?colourwayid=16550585&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-rivalry-lo-trainers-in-triple-black/prd/12269530?colourwayid=16427521&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-continental-80-trainers-in-burgundy-with-gum-sole/prd/13659895?colourwayid=16555734&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-u-path-run-trainers-in-off-white/prd/13659914?colourwayid=16555737&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-swift-trainers-in-black/prd/13659919?colourwayid=16555725&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-supercourt-trainers-in-white-team-royal-blue/prd/21070587?colourwayid=60138060&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-continental-80-vulc-trainers/prd/12267761?colourwayid=16419810&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-clean-classics-sustainable-stan-smith-trainers-in-white/prd/14685403?colourwayid=16636292&SearchQuery=&cid=27437']
urls1 = ['https://www.asos.com/ben-sherman/ben-sherman-shoe-shine-set/prd/12905415?colourwayid=16524496&SearchQuery=&cid=27437', 'https://www.asos.com/toms/toms-trvl-lite-lace-up-trainers-in-grey/prd/22900922?colourwayid=60435043&SearchQuery=&cid=27437', 'https://www.asos.com/brave-soul/brave-soul-faux-suede-loafers-in-beige/prd/22896966?colourwayid=60434741&SearchQuery=&cid=27437', 'https://www.asos.com/brave-soul/brave-soul-utility-padded-sliders-in-black/prd/23343811?colourwayid=60473222&SearchQuery=&cid=27437', 'https://www.asos.com/truffle-collection/truffle-collection-flip-flops-in-black/prd/22554043?colourwayid=60407539&SearchQuery=&cid=27437', 'https://www.asos.com/original-penguin/original-penguin-buckle-footbed-sandals-in-black/prd/22127078?colourwayid=60375453&SearchQuery=&cid=27437', 'https://www.asos.com/original-penguin/original-penguin-logo-sliders-in-black/prd/22127081?colourwayid=60375459&SearchQuery=&cid=27437', 'https://www.asos.com/calvin-klein/calvin-klein-antal-plimsolls-in-black/prd/22345635?colourwayid=60391562&SearchQuery=&cid=27437', 'https://www.asos.com/asos-design/asos-design-wide-fit-black-patent-loafer-with-double-silver-chain-detail/prd/21330892?colourwayid=60158081&SearchQuery=&cid=27437', 'https://www.asos.com/asos-design/asos-design-heeled-chelsea-boots-with-pointed-toe-in-stone-suede-with-strap-detail/prd/21030692?colourwayid=60135340&SearchQuery=&cid=27437', 'https://www.asos.com/topman/topman-cuban-boots-in-tan/prd/20758711?colourwayid=60085631&SearchQuery=&cid=27437', 'https://www.asos.com/h-by-hudson/h-by-hudson-battle-boots-in-burgundy-leather/prd/20596737?colourwayid=60067202&SearchQuery=&cid=27437', 'https://www.asos.com/aldo/aldo-mynytho-casual-thong-sandals-in-brown/prd/23002128?colourwayid=60443180&SearchQuery=&cid=27437', 'https://www.asos.com/brave-soul/brave-soul-espadrilles-in-khaki-green/prd/23343810?colourwayid=60473217&SearchQuery=&cid=27437', 'https://www.asos.com/ben-sherman/ben-sherman-suede-snaffle-bar-loafers-in-navy-stripe/prd/22120735?colourwayid=60375069&SearchQuery=&cid=27437', 'https://www.asos.com/brave-soul/brave-soul-slip-on-plimsolls-in-black/prd/23343809?colourwayid=60473215&SearchQuery=&cid=27437', 'https://www.asos.com/original-penguin/original-penguin-buckle-footbed-sandals-in-brown/prd/22127209?colourwayid=60375469&SearchQuery=&cid=27437', 'https://www.asos.com/calvin-klein/calvin-klein-jeans-aurelio-plimsolls-in-navy/prd/22346096?colourwayid=60391567&SearchQuery=&cid=27437', 'https://www.asos.com/original-penguin/original-penguin-wide-fit-chunky-back-tab-trainers-in-white-mix/prd/22131531?colourwayid=60375844&SearchQuery=&cid=27437', 'https://www.asos.com/asos-design/asos-design-cuban-heel-western-chelsea-boots-in-pink-patent-with-metal-hardware/prd/21328683?colourwayid=60157896&SearchQuery=&cid=27437', 'https://www.asos.com/h-by-hudson/h-by-hudson-atol-chunky-lace-up-shoes-in-black-leather/prd/20597037?colourwayid=60067225&SearchQuery=&cid=27437', 'https://www.asos.com/asos-design/asos-design-wide-fit-brogue-loafers-in-black-faux-leather-with-tassel/prd/21330305?colourwayid=60158063&SearchQuery=&cid=27437', 'https://www.asos.com/asos-design/asos-design-wide-fit-loafers-in-brown-faux-leather-with-snake-effect-and-snaffle-detail/prd/21331255?colourwayid=60158134&SearchQuery=&cid=27437', 'https://www.asos.com/original-penguin/original-penguin-wide-fit-logo-sliders-in-black/prd/22127356?colourwayid=60375481&SearchQuery=&cid=27437', 'https://www.asos.com/calvin-klein/calvin-klein-falconi-trainers-in-black/prd/23273214?colourwayid=60466529&SearchQuery=&cid=27437', 'https://www.asos.com/calvin-klein/calvin-klein-antal-plimsolls-in-white/prd/22346102?colourwayid=60391574&SearchQuery=&cid=27437', 'https://www.asos.com/ben-sherman/ben-sherman-suede-snaffle-bar-loafers-in-beige/prd/22120721?colourwayid=60375085&SearchQuery=&cid=27437', 'https://www.asos.com/brave-soul/brave-soul-slidder-in-prince-of-wales-check-print/prd/14670806?colourwayid=16635156&SearchQuery=&cid=27437', 'https://www.asos.com/rule-london/rule-london-faux-leather-trim-mules-in-black/prd/22554873?colourwayid=60407591&SearchQuery=&cid=27437', 'https://www.asos.com/silver-street/silver-street-smart-penny-loafers-in-tan-leather/prd/20409172?colourwayid=60051338&SearchQuery=&cid=27437', 'https://www.asos.com/calvin-klein/calvin-klein-jeans-joele-trainers-in-black/prd/23204229?colourwayid=60459067&SearchQuery=&cid=27437', 'https://www.asos.com/asos-design/asos-design-wide-fit-trainers-with-contrast-tongue-and-heel-in-white/prd/14580016?colourwayid=16627534&SearchQuery=&cid=27437', 'https://www.asos.com/topman/topman-trainers-with-navy-stripe-in-white/prd/20332692?colourwayid=60044541&SearchQuery=&cid=27437', 'https://www.asos.com/asos-design/asos-design-casual-lace-up-brogue-shoes-in-brown-suede-with-contrast-sole/prd/20440725?colourwayid=60054051&SearchQuery=&cid=27437', 'https://www.asos.com/nike/nike-air-max-2090-cl-trainers-in-white-turquoise/prd/14837857?colourwayid=16647985&SearchQuery=&cid=27437']
urls2 = ['https://www.asos.com/topman/topman-chunky-trainers-in-white/prd/20333016?colourwayid=60044551&SearchQuery=&cid=27437', 'https://www.asos.com/brave-soul/brave-soul-chunky-sole-trainers-in-white-with-contrast-grey/prd/22896976?colourwayid=60434760&SearchQuery=&cid=27437', 'https://www.asos.com/brave-soul/brave-soul-side-zip-lace-up-trainers-in-black/prd/22896979?colourwayid=60434754&SearchQuery=&cid=27437', 'https://www.asos.com/truffle-collection/truffle-collection-snaffle-trim-mule-slippers-in-black/prd/21197159?colourwayid=60147322&SearchQuery=&cid=27437', 'https://www.asos.com/brave-soul/brave-soul-ultra-light-sliders-in-khaki/prd/22934532?colourwayid=60437555&SearchQuery=&cid=27437', 'https://www.asos.com/truffle-collection/truffle-collection-wide-fit-chunky-sole-trainers-in-black/prd/21553899?colourwayid=60175907&SearchQuery=&cid=27437', 'https://www.asos.com/silver-street/silver-street-smart-monk-shoes-in-brown/prd/9108366?colourwayid=15265312&SearchQuery=&cid=27437', 'https://www.asos.com/brave-soul/brave-soul-side-zip-lace-up-trainers-in-white/prd/22896973?colourwayid=60434743&SearchQuery=&cid=27437', 'https://www.asos.com/asos-design/asos-design-trainers-in-white-with-gold-detail/prd/14097079?colourwayid=16591163&SearchQuery=&cid=27437', 'https://www.asos.com/asos-design/asos-design-knitted-trainers-with-wrapped-sole/prd/21342541?colourwayid=60159018&SearchQuery=&cid=27437', 'https://www.asos.com/toms/toms-arroyo-runner-trainers-in-black/prd/22900908?colourwayid=60435060&SearchQuery=&cid=27437', 'https://www.asos.com/silver-street/silver-street-brogue-lace-up-shoes-in-burgundy-leather/prd/20409161?colourwayid=60051348&SearchQuery=&cid=27437', 'https://www.asos.com/calvin-klein/calvin-klein-jeans-augusto-hi-top-trainers-in-white/prd/22346104?colourwayid=60391586&SearchQuery=&cid=27437', 'https://www.asos.com/river-island/river-island-smart-oxfords-with-toe-cap-in-brown/prd/20833731?colourwayid=60092697&SearchQuery=&cid=27437', 'https://www.asos.com/asos-design/asos-design-loafers-in-woven-tan-faux-leather/prd/14587235?colourwayid=16628131&SearchQuery=&cid=27437', 'https://www.asos.com/ben-sherman/ben-sherman-chunky-woven-lace-up-shoes-in-black-leather/prd/21089515?colourwayid=60139492&SearchQuery=&cid=27437', 'https://www.asos.com/ben-sherman/ben-sherman-lace-up-ankle-boots-in-tan-leather-suede-mix/prd/21089497?colourwayid=60139501&SearchQuery=&cid=27437', 'https://www.asos.com/brave-soul/brave-soul-faux-suede-chelsea-boots-in-tan/prd/22126890?colourwayid=60375439&SearchQuery=&cid=27437', 'https://www.asos.com/original-penguin/original-penguin-lace-up-plimsolls-in-navy/prd/22127211?colourwayid=60375464&SearchQuery=&cid=27437', 'https://www.asos.com/asos-design/asos-design-mesh-trainers-in-white/prd/14579524?colourwayid=16627448&SearchQuery=&cid=27437', 'https://www.asos.com/toms/toms-trvl-lite-lace-up-trainers-in-black/prd/22900926?colourwayid=60435039&SearchQuery=&cid=27437', 'https://www.asos.com/truffle-collection/truffle-collection-wide-fit-chunky-loafers-in-black-faux-leather/prd/21553922?colourwayid=60175897&SearchQuery=&cid=27437', 'https://www.asos.com/silver-street/silver-street-chunky-sole-trim-loafers-in-black-leather/prd/21198060?colourwayid=60147402&SearchQuery=&cid=27437', 'https://www.asos.com/ben-sherman/ben-sherman-canvas-plimsoll-in-black/prd/21370175?colourwayid=60161547&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-stan-smith-leather-trainers-in-white/prd/12166045?colourwayid=16364792&SearchQuery=&cid=27437', 'https://www.asos.com/truffle-collection/truffle-collection-flip-flops-in-white/prd/22554027?colourwayid=60407516&SearchQuery=&cid=27437', 'https://www.asos.com/asos-design/asos-design-brogue-loafers-in-tan-leather-with-gold-snaffle-and-tassel/prd/13663953?colourwayid=16555996&SearchQuery=&cid=27437', 'https://www.asos.com/truffle-collection/truffle-collection-chunky-dad-trainers-in-grey/prd/21197153?colourwayid=60147311&SearchQuery=&cid=27437', 'https://www.asos.com/new-look/new-look-pu-penny-loafer-in-black/prd/14647413?colourwayid=16633252&SearchQuery=&cid=27437', 'https://www.asos.com/brave-soul/brave-soul-lace-up-trainers-in-white-contrast-red/prd/22896631?colourwayid=60434731&SearchQuery=&cid=27437', 'https://www.asos.com/silver-street/silver-street-suede-shoes-in-tan/prd/21198038?colourwayid=60147397&SearchQuery=&cid=27437', 'https://www.asos.com/brave-soul/brave-soul-lace-up-trainer-in-white/prd/22430639?colourwayid=60397625&SearchQuery=&cid=27437', 'https://www.asos.com/asos-dark-future/asos-dark-future-flip-flops-in-white-with-logo/prd/14582192?colourwayid=16627704&SearchQuery=&cid=27437', 'https://www.asos.com/nike/nike-daybreak-type-se-recycled-canvas-trainers-in-grey/prd/14837264?colourwayid=16647960&SearchQuery=&cid=27437', 'https://www.asos.com/toms/toms-avalon-espadrilles-in-toffee/prd/21641643?colourwayid=60183676&SearchQuery=&cid=27437']
urls3 = ['https://www.asos.com/topman/topman-chunky-trainers-in-white/prd/20333016?colourwayid=60044551&SearchQuery=&cid=27437', 'https://www.asos.com/brave-soul/brave-soul-chunky-sole-trainers-in-white-with-contrast-grey/prd/22896976?colourwayid=60434760&SearchQuery=&cid=27437', 'https://www.asos.com/brave-soul/brave-soul-side-zip-lace-up-trainers-in-black/prd/22896979?colourwayid=60434754&SearchQuery=&cid=27437', 'https://www.asos.com/truffle-collection/truffle-collection-snaffle-trim-mule-slippers-in-black/prd/21197159?colourwayid=60147322&SearchQuery=&cid=27437', 'https://www.asos.com/brave-soul/brave-soul-ultra-light-sliders-in-khaki/prd/22934532?colourwayid=60437555&SearchQuery=&cid=27437', 'https://www.asos.com/truffle-collection/truffle-collection-wide-fit-chunky-sole-trainers-in-black/prd/21553899?colourwayid=60175907&SearchQuery=&cid=27437', 'https://www.asos.com/silver-street/silver-street-smart-monk-shoes-in-brown/prd/9108366?colourwayid=15265312&SearchQuery=&cid=27437', 'https://www.asos.com/brave-soul/brave-soul-side-zip-lace-up-trainers-in-white/prd/22896973?colourwayid=60434743&SearchQuery=&cid=27437', 'https://www.asos.com/asos-design/asos-design-trainers-in-white-with-gold-detail/prd/14097079?colourwayid=16591163&SearchQuery=&cid=27437', 'https://www.asos.com/asos-design/asos-design-knitted-trainers-with-wrapped-sole/prd/21342541?colourwayid=60159018&SearchQuery=&cid=27437', 'https://www.asos.com/toms/toms-arroyo-runner-trainers-in-black/prd/22900908?colourwayid=60435060&SearchQuery=&cid=27437', 'https://www.asos.com/silver-street/silver-street-brogue-lace-up-shoes-in-burgundy-leather/prd/20409161?colourwayid=60051348&SearchQuery=&cid=27437', 'https://www.asos.com/calvin-klein/calvin-klein-jeans-augusto-hi-top-trainers-in-white/prd/22346104?colourwayid=60391586&SearchQuery=&cid=27437', 'https://www.asos.com/river-island/river-island-smart-oxfords-with-toe-cap-in-brown/prd/20833731?colourwayid=60092697&SearchQuery=&cid=27437', 'https://www.asos.com/asos-design/asos-design-loafers-in-woven-tan-faux-leather/prd/14587235?colourwayid=16628131&SearchQuery=&cid=27437', 'https://www.asos.com/ben-sherman/ben-sherman-chunky-woven-lace-up-shoes-in-black-leather/prd/21089515?colourwayid=60139492&SearchQuery=&cid=27437', 'https://www.asos.com/ben-sherman/ben-sherman-lace-up-ankle-boots-in-tan-leather-suede-mix/prd/21089497?colourwayid=60139501&SearchQuery=&cid=27437', 'https://www.asos.com/brave-soul/brave-soul-faux-suede-chelsea-boots-in-tan/prd/22126890?colourwayid=60375439&SearchQuery=&cid=27437', 'https://www.asos.com/original-penguin/original-penguin-lace-up-plimsolls-in-navy/prd/22127211?colourwayid=60375464&SearchQuery=&cid=27437', 'https://www.asos.com/asos-design/asos-design-mesh-trainers-in-white/prd/14579524?colourwayid=16627448&SearchQuery=&cid=27437', 'https://www.asos.com/toms/toms-trvl-lite-lace-up-trainers-in-black/prd/22900926?colourwayid=60435039&SearchQuery=&cid=27437', 'https://www.asos.com/truffle-collection/truffle-collection-wide-fit-chunky-loafers-in-black-faux-leather/prd/21553922?colourwayid=60175897&SearchQuery=&cid=27437', 'https://www.asos.com/silver-street/silver-street-chunky-sole-trim-loafers-in-black-leather/prd/21198060?colourwayid=60147402&SearchQuery=&cid=27437', 'https://www.asos.com/ben-sherman/ben-sherman-canvas-plimsoll-in-black/prd/21370175?colourwayid=60161547&SearchQuery=&cid=27437', 'https://www.asos.com/adidas-originals/adidas-originals-stan-smith-leather-trainers-in-white/prd/12166045?colourwayid=16364792&SearchQuery=&cid=27437', 'https://www.asos.com/truffle-collection/truffle-collection-flip-flops-in-white/prd/22554027?colourwayid=60407516&SearchQuery=&cid=27437', 'https://www.asos.com/asos-design/asos-design-brogue-loafers-in-tan-leather-with-gold-snaffle-and-tassel/prd/13663953?colourwayid=16555996&SearchQuery=&cid=27437', 'https://www.asos.com/truffle-collection/truffle-collection-chunky-dad-trainers-in-grey/prd/21197153?colourwayid=60147311&SearchQuery=&cid=27437', 'https://www.asos.com/new-look/new-look-pu-penny-loafer-in-black/prd/14647413?colourwayid=16633252&SearchQuery=&cid=27437', 'https://www.asos.com/brave-soul/brave-soul-lace-up-trainers-in-white-contrast-red/prd/22896631?colourwayid=60434731&SearchQuery=&cid=27437', 'https://www.asos.com/silver-street/silver-street-suede-shoes-in-tan/prd/21198038?colourwayid=60147397&SearchQuery=&cid=27437', 'https://www.asos.com/brave-soul/brave-soul-lace-up-trainer-in-white/prd/22430639?colourwayid=60397625&SearchQuery=&cid=27437', 'https://www.asos.com/asos-dark-future/asos-dark-future-flip-flops-in-white-with-logo/prd/14582192?colourwayid=16627704&SearchQuery=&cid=27437', 'https://www.asos.com/nike/nike-daybreak-type-se-recycled-canvas-trainers-in-grey/prd/14837264?colourwayid=16647960&SearchQuery=&cid=27437', 'https://www.asos.com/toms/toms-avalon-espadrilles-in-toffee/prd/21641643?colourwayid=60183676&SearchQuery=&cid=27437']
urls4 = ['https://www.asos.com/asos-design/asos-design-black-patent-loafer-with-double-silver-chain-detail/prd/21330889?colourwayid=60158087&SearchQuery=&cid=27437', 'https://www.asos.com/calvin-klein/calvin-klein-demos-chunky-trainers-in-white/prd/23272806?colourwayid=60466499&SearchQuery=&cid=27437', 'https://www.asos.com/truffle-collection/truffle-collection-wide-fit-chunky-chelsea-boots-in-black-faux-leather/prd/21553921?colourwayid=60175898&SearchQuery=&cid=27437', 'https://www.asos.com/dune/dune-side-stripe-trainers-in-white-leather-mix/prd/21747281?colourwayid=60219469&SearchQuery=&cid=27437', 'https://www.asos.com/silver-street/silver-street-tassel-loafers-in-black-leather/prd/20409179?colourwayid=60051370&SearchQuery=&cid=27437', 'https://www.asos.com/silver-street/silver-street-leather-brogues-in-black/prd/14337180?colourwayid=16608845&SearchQuery=&cid=27437', 'https://www.asos.com/truffle-collection/truffle-collection-chunky-dad-trainers-in-white/prd/21197150?colourwayid=60147313&SearchQuery=&cid=27437', 'https://www.asos.com/asos-design/asos-design-trainers-in-mixed-materials/prd/20249610?colourwayid=60020963&SearchQuery=&cid=27437', 'https://www.asos.com/aldo/aldo-balsam-casual-thong-sandals-in-navy/prd/23002119?colourwayid=60443168&SearchQuery=&cid=27437', 'https://www.asos.com/silver-street/silver-street-woven-suede-loafers-in-tan/prd/22695870?colourwayid=60417813&SearchQuery=&cid=27437', 'https://www.asos.com/toms/toms-trvl-flip-flops-in-black/prd/22900915?colourwayid=60435036&SearchQuery=&cid=27437', 'https://www.asos.com/truffle-collection/truffle-collection-wide-fit-casual-chelsea-boots-in-black/prd/21193926?colourwayid=60147087&SearchQuery=&cid=27437', 'https://www.asos.com/brave-soul/brave-soul-faux-suede-chunky-trainer-in-black/prd/22430646?colourwayid=60397621&SearchQuery=&cid=27437', 'https://www.asos.com/tommy-hilfiger/tommy-hilfiger-nautical-print-beach-flip-flops-in-red/prd/23556540?colourwayid=60493514&SearchQuery=&cid=27437', 'https://www.asos.com/asos-design/asos-design-lace-up-boots-in-black-leather-with-borg-lining/prd/21030116?colourwayid=60135308&SearchQuery=&cid=27437', 'https://www.asos.com/silver-street/silver-street-chunky-chelsea-boots-in-black-leather/prd/21196362?colourwayid=60147266&SearchQuery=&cid=27437', 'https://www.asos.com/truffle-collection/truffle-collection-casual-monk-strap-shoes-in-black/prd/21195829?colourwayid=60147239&SearchQuery=&cid=27437', 'https://www.asos.com/asos-design/asos-design-tech-lounge-sliders-in-red-with-black-faux-fur-lining/prd/21008875?colourwayid=60133681&SearchQuery=&cid=27437', 'https://www.asos.com/asos-design/asos-design-oxford-plimsolls-in-white-canvas/prd/9155082?colourwayid=15019272&SearchQuery=&cid=27437', 'https://www.asos.com/nike-sb/nike-sb-zoom-janoski-remastered-64-tokyo-canvas-trainers-in-off-white-multi/prd/14832415?colourwayid=16647609&SearchQuery=&cid=27437', 'https://www.asos.com/walk-london/walk-london-luca-monk-shoes-in-black-high-shine/prd/13900615?colourwayid=16575209&SearchQuery=&cid=27437', 'https://www.asos.com/ellesse/ellesse-varesse-trainers-in-black/prd/21827560?colourwayid=60302549&SearchQuery=&cid=27437', 'https://www.asos.com/asos-design/asos-design-trainer-with-patent-material/prd/21341971?colourwayid=60158971&SearchQuery=&cid=27437', 'https://www.asos.com/new-look/new-look-desert-boot-in-black/prd/21198036?colourwayid=60147364&SearchQuery=&cid=27437', 'https://www.asos.com/gh-bass/gh-bass-co-easy-weejuns-larson-loafers-in-navy-velvet/prd/21494944?colourwayid=60171680&SearchQuery=&cid=27437', 'https://www.asos.com/asos-design/asos-design-trainers-with-chunky-sole-and-all-over-diamante/prd/14580024?colourwayid=16627519&SearchQuery=&cid=27437', 'https://www.asos.com/asos-design/asos-design-cuban-heel-western-chelsea-boots-in-black-leather-with-lightning-detail/prd/8345050?colourwayid=15164865&SearchQuery=&cid=27437', 'https://www.asos.com/asos-design/asos-design-tassel-loafers-in-black-suede-with-natural-sole/prd/12484610?colourwayid=16421507&SearchQuery=&cid=27437', 'https://www.asos.com/reiss/reiss-ashley-pool-sliders-in-black/prd/21626315?colourwayid=60182221&SearchQuery=&cid=27437', 'https://www.asos.com/french-connection/french-connection-faux-leather-lace-up-plimsoll/prd/21475995?colourwayid=60170127&SearchQuery=&cid=27437', 'https://www.asos.com/asos-design/asos-design-cuban-heel-western-chelsea-boots-in-black-faux-suede-with-diamante-and-strap-detail/prd/21007785?colourwayid=60133607&SearchQuery=&cid=27437', 'https://www.asos.com/silver-street/silver-street-wide-fit-chunky-sole-trim-loafers-in-black-leather/prd/21511603?colourwayid=60172754&SearchQuery=&cid=27437']
shoe_dict = {}
for url in urls4:
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')

    title = remove_tags(str(soup.title))
    description = remove_tags(str(soup.find("div", {"class": "brand-description"})))
    description1 = remove_tags(str(soup.find("div", {"class": "product-description"})))
    about = remove_tags(str(soup.find_all("div", {"class": "about-me"})))

    shoe_description = title + description + description1 + about
    shoe_dict[url] = shoe_description

with open('shoes.json', 'a') as outfile:
    json.dump(shoe_dict, outfile, indent=2)








# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.implicitly_wait(10)  # seconds
#
# driver.get(url_outlet)
# # for a in driver.find_elements_by_xpath('//*[@id="plp"]/div/div/div[2]/div/div[1]/section'):
# print(driver.find_element_by_xpath('//*[@id="plp"]/div/div/div[2]/div/div[1]').text)
# # for a in driver.find_elements_by_xpath('//*[@id="plp"]/div/div/div[2]/div/div[1]'):
# #     print(a.get_attribute('href'))
#
# driver.quit()
# print(soup)

# text = soup.find(id='product-details-container').text
# print(text)



