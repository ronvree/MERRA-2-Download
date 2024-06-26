

"""

    All locations with corresponding coordinates conveniently stored in a python list

"""

LOCATIONS = [
    ('Japan/Abashiri', 44.0177777777778, 144.279722222222),
    ('Japan/Aikawa', 38.0291666666667, 138.24),
    ('Japan/Akita', 39.7175, 140.099166666667),
    ('Japan/Aomori', 40.8216666666667, 140.768888888889),
    ('Japan/Asahikawa', 43.7569444444444, 142.372222222222),
    ('Japan/Choshi', 35.7397222222222, 140.857222222222),
    ('Japan/Esashi', 41.8672222222222, 140.123888888889),
    ('Japan/Fukue', 32.6947222222222, 128.826944444444),
    ('Japan/Fukui', 36.0555555555556, 136.2225),
    ('Japan/Fukuoka', 33.5822222222222, 130.376388888889),
    ('Japan/Fukushima', 37.7594444444444, 140.470833333333),
    ('Japan/Gifu', 35.4002777777778, 136.7625),
    ('Japan/Hachijojima', 33.1216666666667, 139.779166666667),
    ('Japan/Hachinohe', 40.5272222222222, 141.521666666667),
    ('Japan/Hakodate', 41.8166666666667, 140.754166666667),
    ('Japan/Hamada', 34.8966666666667, 132.070555555556),
    ('Japan/Hamamatsu', 34.7538888888889, 137.711666666667),
    ('Japan/Hikone', 35.2761111111111, 136.243888888889),
    ('Japan/Hiroo', 42.2944444444444, 143.316666666667),
    ('Japan/Hiroshima', 34.3986111111111, 132.462777777778),
    ('Japan/Iida', 35.5233333333333, 137.8225),
    ('Japan/Iriomotejima', 24.4277777777778, 123.765555555556),
    ('Japan/Ishigakijima', 24.3366666666667, 124.164444444444),
    ('Japan/Iwamizawa', 43.2116666666667, 141.785833333333),
    ('Japan/Izuhara-1', 34.1977777777778, 129.291944444444),
    ('Japan/Izuhara-2', 34.1533333333333, 129.222777777778),
    ('Japan/Kagoshima', 31.555, 130.548055555556),
    ('Japan/Kanazawa', 36.5897222222222, 136.634722222222),
    ('Japan/Kobe', 34.6969444444444, 135.212777777778),
    ('Japan/Kochi-1', 33.5680555555556, 133.549444444444),
    ('Japan/Kochi-2', 33.5683333333333, 133.549166666667),
    ('Japan/Kofu', 35.6672222222222, 138.553888888889),
    ('Japan/Kumagaya', 36.15, 139.38),
    ('Japan/Kumamoto', 32.8136111111111, 130.706944444444),
    ('Japan/Kumejima', 26.3380555555556, 126.803888888889),
    ('Japan/Kushiro-1', 42.9858333333333, 144.377777777778),
    ('Japan/Kushiro-2', 42.9530555555556, 144.4375),
    ('Japan/Kutchan', 42.9011111111111, 140.758055555556),
    ('Japan/Kyoto-1', 35.0147222222222, 135.732777777778),
    ('Japan/Kyoto-2', 35.0119831, 135.6761135),
    ('Japan/Maebashi', 36.4052777777778, 139.060555555556),
    ('Japan/Maizuru', 35.4502777777778, 135.318055555556),
    ('Japan/Matsue', 35.4572222222222, 133.065555555556),
    ('Japan/Matsumoto', 36.2466666666667, 137.970555555556),
    ('Japan/Matsuyama', 33.8436111111111, 132.7775),
    ('Japan/Minamidaitojima', 25.8288888888889, 131.228611111111),
    ('Japan/Mito', 36.3811111111111, 140.468055555556),
    ('Japan/Miyakejima', 34.1238888888889, 139.521388888889),
    ('Japan/Miyako', 39.6469444444444, 141.965833333333),
    ('Japan/Miyakojima', 24.7944444444444, 125.278333333333),
    ('Japan/Miyazaki', 31.9383333333333, 131.414166666667),
    ('Japan/Mombetsu', 44.345, 143.355277777778),
    ('Japan/Morioka', 39.6983333333333, 141.166111111111),
    ('Japan/Muroran-1', 42.3116666666667, 140.975277777778),
    ('Japan/Muroran-2', 42.3236111111111, 140.97),
    ('Japan/Nagano', 36.6627777777778, 138.1925),
    ('Japan/Nagasaki', 32.7341666666667, 129.868055555556),
    ('Japan/Nago', 26.5941666666667, 127.966388888889),
    ('Japan/Nagoya-1', 35.1677777777778, 136.965555555556),
    ('Japan/Nagoya-2', 35.1683333333333, 136.964722222222),
    ('Japan/Naha', 26.2072222222222, 127.687222222222),
    ('Japan/Nara', 34.6938888888889, 135.827777777778),
    ('Japan/Naze', 28.3797222222222, 129.495555555556),
    ('Japan/Naze,Funchatoge', 28.3941666666667, 129.552777777778),
    ('Japan/Nemuro', 43.3305555555556, 145.585555555556),
    ('Japan/Niigata', 37.8936111111111, 139.018888888889),
    ('Japan/Nobeoka', 32.5819444444444, 131.658055555556),
    ('Japan/Obihiro', 42.9222222222222, 143.211944444444),
    ('Japan/Oita', 33.2361111111111, 131.619166666667),
    ('Japan/Okayama', 34.6858333333333, 133.925277777778),
    ('Japan/Onahama', 36.9475, 140.903333333333),
    ('Japan/Osaka', 34.6822222222222, 135.519166666667),
    ('Japan/Oshima', 34.7494444444444, 139.363055555556),
    ('Japan/Owase', 34.0697222222222, 136.193333333333),
    ('Japan/Rumoi', 43.9461111111111, 141.631944444444),
    ('Japan/Saga', 33.2663888888889, 130.305277777778),
    ('Japan/Saigo', 36.2044444444444, 133.333888888889),
    ('Japan/Sakata', 38.9086111111111, 139.843333333333),
    ('Japan/Sapporo', 43.06, 141.328611111111),
    ('Japan/Sendai-1', 38.2619444444444, 140.896666666667),
    ('Japan/Sendai-2', 38.2622222222222, 140.896666666667),
    ('Japan/Shimonoseki', 33.9486111111111, 130.926111111111),
    ('Japan/Shinjo', 38.7569444444444, 140.312222222222),
    ('Japan/Shionomisaki', 33.4502777777778, 135.757222222222),
    ('Japan/Shirakawa', 37.1316666666667, 140.215),
    ('Japan/Shizuoka', 34.9761111111111, 138.403888888889),
    ('Japan/Sumoto', 34.3383333333333, 134.905),
    ('Japan/Takada', 37.1066666666667, 138.246666666667),
    ('Japan/Takamatsu', 34.3180555555556, 134.054444444444),
    ('Japan/Takayama', 36.1561111111111, 137.253333333333),
    ('Japan/Tanegashima', 30.7202777777778, 130.9825),
    ('Japan/Tateyama', 34.9869444444444, 139.865277777778),
    ('Japan/Tokushima', 34.0677777777778, 134.573333333333),
    ('Japan/Tokyo', 35.6916666666667, 139.751111111111),
    ('Japan/Tottori-1', 35.4877777777778, 134.238333333333),
    ('Japan/Tottori-2', 35.5308333333333, 134.199444444444),
    ('Japan/Toyama', 36.7094444444445, 137.2025),
    ('Japan/Toyooka', 35.5358333333333, 134.822222222222),
    ('Japan/Tsu', 34.7341666666667, 136.519722222222),
    ('Japan/Tsuruga', 35.6533333333333, 136.062222222222),
    ('Japan/Urakawa', 42.1625, 142.776944444444),
    ('Japan/Utsunomiya', 36.5497222222222, 139.868333333333),
    ('Japan/Uwajima', 33.2277777777778, 132.553055555556),
    ('Japan/Wajima', 37.3913888888889, 136.895277777778),
    ('Japan/Wakayama', 34.2288888888889, 135.164166666667),
    ('Japan/Wakkanai', 45.415, 141.678888888889),
    ('Japan/Yakushima-1', 30.3855555555556, 130.659166666667),
    ('Japan/Yakushima-2', 30.3830555555556, 130.659166666667),
    ('Japan/Yamagata', 38.2555555555556, 140.346111111111),
    ('Japan/Yokohama', 35.4397222222222, 139.6525),
    ('Japan/Yonago', 35.4347222222222, 133.338611111111),
    ('Japan/Yonagunijima', 24.4666666666667, 123.010555555556),
    ('South Korea/Boeun', 36.48759, 127.73412),
    ('South Korea/Boryeong', 36.32724, 126.55744),
    ('South Korea/Buan', 35.72954, 126.71655),
    ('South Korea/Busan', 35.10468, 129.03203),
    ('South Korea/Buyeo', 36.27242, 126.92079),
    ('South Korea/Cheonan', 36.7624, 127.2927),
    ('South Korea/Cheongju', 36.63924, 127.44066),
    ('South Korea/Chuncheon', 37.90256, 127.7357),
    ('South Korea/Chungju', 36.97038, 127.95266),
    ('South Korea/Chupungnyeong', 36.22023, 127.99457),
    ('South Korea/Daegu', 35.87797, 128.65295),
    ('South Korea/Daegwallyeong', 37.67713, 128.71833),
    ('South Korea/Daejeon', 36.372, 127.37212),
    ('South Korea/Ganghwa', 37.70739, 126.44634),
    ('South Korea/Gangneung', 37.75147, 128.89098),
    ('South Korea/Geochang', 35.6674, 127.909),
    ('South Korea/Geoje', 34.88818, 128.60453),
    ('South Korea/Geumsan', 36.1027, 127.4817),
    ('South Korea/Goheung', 34.61826, 127.27572),
    ('South Korea/Gumi', 36.13, 128.32),
    ('South Korea/Gunsan', 36.0053, 126.76135),
    ('South Korea/Gwangju', 35.17294, 126.89158),
    ('South Korea/Haenam', 34.55375, 126.56907),
    ('South Korea/Hapcheon', 35.56503, 128.16986),
    ('South Korea/Hongcheon', 37.68358, 127.8804),
    ('South Korea/Icheon', 37.26399, 127.48421),
    ('South Korea/Imsil', 35.61203, 127.28556),
    ('South Korea/Incheon', 37.47772, 126.6249),
    ('South Korea/Inje', 38.05987, 128.16713),
    ('South Korea/Jangheung', 34.68875, 126.91949),
    ('South Korea/Jecheon', 37.15927, 128.19431),
    ('South Korea/Jeju', 33.51411, 126.52968),
    ('South Korea/Jeongeup', 35.56306, 126.83917),
    ('South Korea/Jeonju', 35.8408, 127.119),
    ('South Korea/Jinju', 35.16379, 128.04002),
    ('South Korea/Miryang', 35.49148, 128.7441),
    ('South Korea/Mokpo', 34.81689, 126.38121),
    ('South Korea/Mungyeong', 36.62727, 128.148),
    ('South Korea/Namhae', 34.81662, 127.92641),
    ('South Korea/Pohang', 36.03201, 129.38002),
    ('South Korea/Sancheong', 35.41299, 127.8791),
    ('South Korea/Seogwipo', 33.24613, 126.56534),
    ('South Korea/Seongsan', 33.38677, 126.8802),
    ('South Korea/Seosan', 36.77661, 126.49391),
    ('South Korea/Seoul', 37.57142, 126.9658),
    ('South Korea/Sokcho', 38.25085, 128.56472),
    ('South Korea/Suwon', 37.27226, 126.98533),
    ('South Korea/Tongyeong', 34.84546, 128.4356),
    ('South Korea/Uiseong', 36.35611, 128.688),
    ('South Korea/Uljin', 36.99176, 129.41278),
    ('South Korea/Ulleungdo', 37.48129, 130.89864),
    ('South Korea/Ulsan', 35.5825, 129.3347222),
    ('South Korea/Wando', 34.39587, 126.70184),
    ('South Korea/Wonju', 37.33756, 127.9466),
    ('South Korea/Yangpyeong', 37.48863, 127.49446),
    ('South Korea/Yeongcheon', 35.97743, 128.95141),
    ('South Korea/Yeongdeok', 36.53331, 129.40936),
    ('South Korea/Yeongju', 36.87188, 128.51696),
    ('South Korea/Yeosu', 34.73929, 127.74064),
    ('Switzerland/Adelboden', 46.492022, 7.561067),
    ('Switzerland/Alchenflüh', 47.079619, 7.5848),
    ('Switzerland/Altdorf', 46.872614, 8.658569),
    ('Switzerland/Andeer', 46.600961, 9.422614),
    ('Switzerland/Appenzell', 47.331994, 9.415403),
    ('Switzerland/Aurigeno', 46.236078, 8.725292),
    ('Switzerland/Azmoos', 47.076869, 9.479753),
    ('Switzerland/Ballens', 46.554378, 6.374472),
    ('Switzerland/Basel-Binningen', 47.548594, 7.582372),
    ('Switzerland/Bauma', 47.364822, 8.881672),
    ('Switzerland/Bellelay', 47.265314, 7.165786),
    ('Switzerland/Biel', 47.151194, 7.254139),
    ('Switzerland/Birmensdorf', 47.342472, 8.444342),
    ('Switzerland/Blonay', 46.464014, 6.891869),
    ('Switzerland/BondoGR', 46.337594, 9.555908),
    ('Switzerland/Boudry', 46.949492, 6.834386),
    ('Switzerland/Brusio-Piazzo', 46.265447, 10.115375),
    ('Switzerland/Buchs', 47.158028, 9.469656),
    ('Switzerland/Cartigny', 46.177483, 6.014089),
    ('Switzerland/Cernier', 47.098392, 6.986644),
    ('Switzerland/Cevio-Cavergno', 46.315447, 8.598925),
    ('Switzerland/Changins', 46.395917, 6.229419),
    ('Switzerland/Chardonne', 46.474036, 6.835272),
    ('Switzerland/Chaumont', 47.049108, 6.978031),
    ('Switzerland/Chur', 46.868244, 9.5419),
    ('Switzerland/Comprovasco,Motto', 46.442531, 8.950197),
    ('Switzerland/Couvet', 46.9213, 6.637761),
    ('Switzerland/Davos-Dorf', 46.808986, 9.836586),
    ('Switzerland/Diessenhofen', 47.690281, 8.744),
    ('Switzerland/Disentis', 46.699461, 8.850803),
    ('Switzerland/Domat,Ems', 46.834311, 9.457442),
    ('Switzerland/Dornach', 47.481642, 7.611114),
    ('Switzerland/Döttingen', 47.568867, 8.249947),
    ('Switzerland/Echandens', 46.537211, 6.543094),
    ('Switzerland/Edlibach', 47.179358, 8.573208),
    ('Switzerland/Einsiedeln', 47.131972, 8.748844),
    ('Switzerland/Elm', 46.921942, 9.172731),
    ('Switzerland/Enges', 47.056436, 7.012192),
    ('Switzerland/Entlebuch', 46.987397, 8.068953),
    ('Switzerland/Eschen-Boja', 47.218989, 9.520044),
    ('Switzerland/Escholzmatt', 46.898653, 7.932344),
    ('Switzerland/Estavayer-le-Lac', 46.841619, 6.848706),
    ('Switzerland/Faido', 46.477881, 8.800878),
    ('Switzerland/Fanas', 46.983531, 9.660289),
    ('Switzerland/Fiesch', 46.400261, 8.127792),
    ('Switzerland/Flawil', 47.415283, 9.182167),
    ('Switzerland/Frauenfeld', 47.560647, 8.887883),
    ('Switzerland/Gadmen', 46.736853, 8.351842),
    ('Switzerland/Grellingen', 47.441186, 7.597728),
    ('Switzerland/Grossdietwil', 47.166089, 7.887067),
    ('Switzerland/Gryon', 46.274817, 7.065661),
    ('Switzerland/Grüsch', 46.983786, 9.64715),
    ('Switzerland/Gstaad', 46.438214, 7.269478),
    ('Switzerland/Gundetswil', 47.536489, 8.819919),
    ('Switzerland/Hallau', 47.698183, 8.457489),
    ('Switzerland/Hardb.Weinfelden', 47.567569, 9.125747),
    ('Switzerland/Heiden', 47.442925, 9.533178),
    ('Switzerland/Herzogenbuchsee', 47.18465, 7.702511),
    ('Switzerland/Hochdorf', 47.166514, 8.28935),
    ('Switzerland/Horgen', 47.265269, 8.582169),
    ('Switzerland/Höfen', 46.717125, 7.569428),
    ('Switzerland/JegenstorfII', 47.049108, 7.507072),
    ('Switzerland/Jenaz', 46.928553, 9.710558),
    ("Switzerland/L'Abergement", 46.756178, 6.490211),
    ('Switzerland/LaBrévine', 46.982014, 6.599133),
    ('Switzerland/LaValsainte', 46.648728, 7.182475),
    ('Switzerland/Langnaui.E.', 46.939633, 7.806425),
    ('Switzerland/Lanterswil', 47.514847, 9.098194),
    ('Switzerland/Laufenburg', 47.561031, 8.063136),
    ('Switzerland/LeLocle', 47.047992, 6.754314),
    ('Switzerland/LeSépey', 46.365406, 7.065819),
    ('Switzerland/LesDiablerets', 46.355131, 7.118014),
    ('Switzerland/LesPlans-sur-Bex', 46.256639, 7.092033),
    ('Switzerland/LesPonts-de-Martel', 47.002858, 6.728592),
    ('Switzerland/LesRangiers', 47.381992, 7.215775),
    ('Switzerland/Leysin', 46.340108, 7.009622),
    ('Switzerland/Leytron', 46.18625, 7.21845),
    ('Switzerland/Liddes', 45.988267, 7.180528),
    ('Switzerland/Liestal-1', 47.481403, 7.730519),
    ('Switzerland/Liestal-2', 47.4814, 7.730519),
    ('Switzerland/Linthal', 46.915883, 8.993658),
    ('Switzerland/Locarno', 46.169278, 8.798214),
    ('Switzerland/Locarno-Monti', 46.172556, 8.787417),
    ('Switzerland/Longirod', 46.498772, 6.26595),
    ('Switzerland/Luzern', 47.062769, 8.342442),
    ('Switzerland/Martina', 46.884997, 10.464608),
    ('Switzerland/MeiringenI', 46.75275, 8.137867),
    ('Switzerland/Merishausen', 47.763636, 8.612414),
    ('Switzerland/MorginsVS', 46.2415, 6.850589),
    ('Switzerland/Moudon', 46.646331, 6.777689),
    ('Switzerland/Moutier', 47.279386, 7.385775),
    ('Switzerland/Mugena', 46.046497, 8.888964),
    ('Switzerland/Murg', 47.108222, 9.217372),
    ('Switzerland/Muri,AG', 47.265317, 8.332283),
    ('Switzerland/Möhlin', 47.561983, 7.850547),
    ('Switzerland/Neuchâtel', 47.000444, 6.935714),
    ('Switzerland/Neuhausen', 47.681939, 8.615533),
    ('Switzerland/Näfels', 47.092389, 9.071936),
    ('Switzerland/Oberehrendingen', 47.481914, 8.332208),
    ('Switzerland/Oberlangenegg', 46.808222, 7.716267),
    ('Switzerland/Oeschberg', 47.126578, 7.613264),
    ('Switzerland/Olivone', 46.527333, 8.932936),
    ('Switzerland/Orbe,Bochuz', 46.722633, 6.536061),
    ('Switzerland/Orvin', 47.157753, 7.214464),
    ('Switzerland/Osogna', 46.311967, 8.987064),
    ('Switzerland/Osterfingen', 47.656878, 8.490242),
    ('Switzerland/Payerne', 46.811581, 6.942469),
    ('Switzerland/Posieux', 46.761672, 7.098294),
    ('Switzerland/Prato-Sornico', 46.394025, 8.655608),
    ('Switzerland/Rafz', 47.620414, 8.542733),
    ('Switzerland/Rancate', 45.870208, 8.967242),
    ('Switzerland/Raperswilen,TG', 47.632486, 9.048642),
    ('Switzerland/Reinach,BL', 47.493131, 7.589494),
    ('Switzerland/Ried,Frutigen', 46.570078, 7.619381),
    ('Switzerland/Romanshorn', 47.563608, 9.376172),
    ('Switzerland/Rorschach', 47.472492, 9.494931),
    ('Switzerland/SagnoTI', 45.857811, 9.033789),
    ('Switzerland/SargansII', 47.050589, 9.439256),
    ('Switzerland/Sarnen', 46.894217, 8.252236),
    ('Switzerland/Schiers', 46.965036, 9.685814),
    ('Switzerland/Schönenwerd', 47.365283, 7.999019),
    ('Switzerland/Scuol', 46.794394, 10.296356),
    ('Switzerland/Seewil', 47.048228, 7.409689),
    ('Switzerland/SeewisDorf', 46.965358, 9.632064),
    ('Switzerland/Sent', 46.815436, 10.335078),
    ('Switzerland/Seon', 47.338319, 8.153353),
    ('Switzerland/Sihlbrugg', 47.219356, 8.5767),
    ('Switzerland/Silenen', 46.782531, 8.669625),
    ('Switzerland/Simplon-Dorf', 46.195022, 8.056794),
    ('Switzerland/St.Luc', 46.222336, 7.594153),
    ('Switzerland/Sta.Maria(ValMustair)', 46.603092, 10.421956),
    ('Switzerland/Stampa', 46.34585, 9.595214),
    ('Switzerland/Stein,ARII', 47.381969, 9.348772),
    ('Switzerland/Therwil', 47.499697, 7.558086),
    ('Switzerland/Thusis', 46.709511, 9.44165),
    ('Switzerland/Trient', 46.048003, 6.993797),
    ('Switzerland/Unterseen', 46.684958, 7.854311),
    ('Switzerland/Vallorbe', 46.712292, 6.379286),
    ('Switzerland/Vals', 46.622889, 9.182461),
    ('Switzerland/Vergeletto', 46.225417, 8.605172),
    ('Switzerland/Versoix', 46.290431, 6.137128),
    ('Switzerland/Villnachern', 47.470556, 8.154928),
    ('Switzerland/Vira,Gambarogno', 46.148775, 8.848836),
    ('Switzerland/Visp', 46.293494, 7.892842),
    ('Switzerland/Wald,ZH', 47.277122, 8.916314),
    ('Switzerland/Wattwil,SG', 47.289853, 9.104422),
    ('Switzerland/Wengen', 46.603731, 7.921556),
    ('Switzerland/Wetzikon', 47.320664, 8.814333),
    ('Switzerland/Wil,SG', 47.461458, 9.056733),
    ('Switzerland/Wildhaus', 47.205022, 9.352617),
    ('Switzerland/Wiliberg', 47.279603, 8.027331),
    ('Switzerland/Winterthur', 47.474228, 8.795444),
    ('Switzerland/Wolhusen', 47.064342, 8.071028),
    ('Switzerland/WorbBE', 46.924433, 7.577772),
    ('Switzerland/Wynau', 47.256317, 7.808556),
    ('Switzerland/Wädenswil', 47.223239, 8.679778),
    ('Switzerland/Zizers', 46.931325, 9.566175),
    ('Switzerland/Zofingen', 47.291794, 7.941003),
    ('Switzerland/Zweisimmen', 46.555264, 7.373433),
    ('Switzerland/Zürich-Albisgüetli', 47.350869, 8.510678),
    ('Switzerland/Zürich-MeteoSchweiz', 47.378142, 8.565853),
    ('Switzerland/Zürich-Witikon', 47.3591, 8.590272),
    ('USA/Washington-DC', 38.8853496, -77.0386278),
]
