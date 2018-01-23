#-*- coding:utf-8 -*-
import fresh_tomatoes
import media

new_movie0 = media.Movie('太空救援',
                        '位于外太空的“礼炮7号”空间站意外与地球失去联系，工程师维克托·阿约金和退役宇航员弗拉基米尔·费奥多罗夫临危受命，搭乘联盟号T-13寻找“礼炮7号”的踪迹，当经历宇宙空间对接、太空舱寒流、空间站失火、太阳能充电系统失灵等一系列危机准备返航之时，却被告知空间站即将被击落，一场更大的太空灾难正在袭来。。。。。。',
                        'http://vs5.bdstatic.com/browse_static/v3/detail2/page/layout/default_poster_06aabfbf1.jpg',
                        'https://www.youtube.com/watch?v=_YFRUdMPmL8')

new_movie1 = media.Movie('野蛮游戏：疯狂森林',
                        '野蛮游戏：疯狂森林 story line',
                        'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1438323953,654962572&fm=27&gp=0.jpg',
                        'https://www.youtube.com/watch?v=m6S4phxKEM8')

new_movie2 = media.Movie('侏罗纪世界：陨落国度',
                        '侏罗纪世界：陨落国度 story line',
                        'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1516443268556&di=ad0e5f7c90c1a49e9b643278d5119323&imgtype=0&src=http%3A%2F%2Ff.hiphotos.baidu.com%2Fnews%2Fcrop%3D78%2C1%2C426%2C256%3Bw%3D638%2Fsign%3D4abeadf10f55b31988b6d8357e9eba0a%2Fc8177f3e6709c93d95b2ef079a3df8dcd00054fa.jpg',
                        'https://www.youtube.com/watch?v=jXmPkWDeAcE')

new_movie3 = media.Movie('环太平洋2: 起义时刻',
                        '环太平洋2: 起义时刻 story line',
                        'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1516443289477&di=35366bdb59ef2af5e2b4f14b87708d18&imgtype=0&src=http%3A%2F%2Fwww.qlmoney.com%2Fuploadfile%2F2016%2F1011%2F20161011105201764.jpg',
                        'https://www.youtube.com/watch?v=apqzsgdl-gk')

new_movie4 = media.Movie('X战警',
                        'X战警 story line',
                        'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1516443308335&di=dbb296e879b74616ed126908b55fb642&imgtype=0&src=http%3A%2F%2Fcs.vmoiver.com%2FUploads%2Fpost%2F2016-03-18%2F56ebcb6fce094.jpg',
                        'https://www.youtube.com/watch?v=Qnb2ZdoxbbU')

#new_movie.showTrailer()

movies = [new_movie0,new_movie1,new_movie2,new_movie3,new_movie4]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)















