from statistics import mean, pstdev
import random


def sd_extreme_ex (a,b,c,d,e):

	normal_sd = pstdev([a,b,c,d,e])
	min_sd = 1000000000
	max_sd = 0
	val1 = 0
	val2 = 0
	val3 = 0
	val4 = 0
	val5 = 0
	for i in list(range(0,11)):#31
		for j in list(range(0,11)):
			for k in list(range(0,11)):
				for p in list(range(0,11)):
					for q in list(range(0,11)):
						val1 = a - i*0.1
						val2 = b - j*0.1
						val3 = c - k*0.1
						val4 = d - p*0.1
						val5 = e - q*0.1
				

						sd = pstdev([val1,val2,val3,val4,val5])
						if (sd>=max_sd):
							max_sd = sd
						if (sd<=min_sd):
							min_sd = sd
						#print('.',end="",flush=True)

	print(max_sd-normal_sd)					
	print(min_sd-normal_sd)
	

for i in list(range(0,1)):
	a = random.randrange(0, 101, 2)
	b = random.randrange(0, 101, 2)
	c = random.randrange(0, 101, 2)
	d = random.randrange(0, 101, 2)
	e = random.randrange(0, 101, 2)
	print((a,b,c,d,e))
	sd_extreme_ex(a,b,c,d,e)

'''

(54, 2, 4, 62, 96)
0.4512268077025823
-0.45020393032895356
(94, 82, 26, 22, 36)
0.4803676593990538
-0.4800542733107207
(84, 28, 94, 46, 42)
0.4727744296385694
-0.47211758585675767
(8, 8, 2, 58, 80)
0.4769624528995031
-0.4765620675976727
(18, 30, 32, 26, 68)
0.384632879491555
-0.3839191876098411
(100, 14, 94, 20, 10)
0.4878677451454081
-0.4878181396113561
(74, 30, 22, 32, 10)
0.3740267278068714
-0.3730809264149606
(46, 44, 28, 74, 74)
0.46061322465676113
-0.45903464851213016
(34, 4, 24, 26, 12)
0.452025454285538
-0.44853086109920604
(52, 46, 66, 42, 20)
0.381840536382164
-0.37539747905741017
(32, 8, 18, 76, 74)
0.4719914845207711
-0.47137307506912407
(12, 70, 86, 82, 58)
0.4005123361535148
-0.39748222687093815
(80, 60, 48, 14, 36)
0.40860367242063944
-0.40525408540934293
(52, 76, 74, 24, 94)
0.4338105777791448
-0.4316153628841626
(96, 98, 16, 0, 18)
0.48457879454718267
-0.48445523168422966
(72, 100, 36, 72, 8)
0.4448250256666384
-0.4434924414408066
(16, 16, 62, 36, 34)
0.39989742976626275
-0.39504602050119786
(84, 90, 34, 70, 84)
0.4039845424470947
-0.4001238290521876
(50, 32, 22, 76, 18)
0.4406341323055898
-0.43843598076392354
(76, 72, 46, 80, 62)
0.43583476621723705
-0.4315711466110148
(50, 26, 24, 78, 28)
0.44264214986987227
-0.44046184048471915
(26, 10, 54, 34, 70)
0.44140149673814477
-0.43921273183899956
(100, 28, 86, 6, 84)
0.4756560236535279
-0.47527795197390077
(80, 78, 56, 74, 78)
0.39052847255762835
-0.3896400717372508
(70, 54, 100, 36, 36)
0.430775185535726
-0.42846777199888564
(6, 40, 38, 36, 48)
0.38406365121154984
-0.38317147887468295
(60, 90, 90, 42, 74)
0.4403821617290973
-0.43781750454583346
(46, 48, 22, 86, 98)
0.45860970126430445
-0.4575299328584741
(96, 46, 88, 78, 54)
0.46429004285259623
-0.4629945221261309
(86, 90, 74, 70, 48)
0.39807676471479425
-0.39240584029747083
(68, 100, 20, 60, 74)
0.3781905128671248
-0.3743964717997734
(48, 34, 12, 54, 82)
0.4002987593935252
-0.39678257248683124
(0, 96, 66, 14, 70)
0.4661637536249543
-0.46552936656512145
(30, 100, 26, 98, 86)
0.48443997286596385
-0.48427659090297226
(6, 70, 58, 98, 76)
0.3873487415037289
-0.38437944213793784
(24, 32, 60, 2, 30)
0.36063337009811036
-0.35459479325160714
(6, 4, 50, 92, 38)
0.40887410080016195
-0.4072215954721763
(26, 10, 20, 14, 76)
0.38984241022388844
-0.38950289321679676
(24, 16, 22, 34, 54)
0.4225167946716262
-0.41775334868220426
(28, 6, 88, 92, 100)
0.4793018909453792
-0.4790298733948788
(34, 22, 36, 90, 68)
0.4619522723661227
-0.4608743938557609
(0, 60, 14, 22, 62)
0.47030985657664104
-0.4695438722396048
(8, 66, 62, 90, 2)
0.47021110262276977
-0.46965660820966093
(72, 6, 10, 22, 34)
0.4096447138412529
-0.40654774126430127
(78, 6, 68, 16, 18)
0.48258383269700644
-0.4823402296901129
(18, 12, 54, 28, 68)
0.4655810763886379
-0.464476705527165
(94, 60, 56, 52, 54)
0.39436752790094154
-0.39407377597187043
(98, 84, 88, 10, 38)
0.46849166692059185
-0.46787677223797886
(12, 38, 62, 78, 18)
0.45067482669012193
-0.4491870965731444
(0, 68, 96, 12, 0)
0.47449090218306367
-0.4741098610045995
(16, 0, 4, 42, 6)
0.4090722030948566
-0.4041429878234979
(18, 44, 78, 48, 24)
0.4066215370375481
-0.4030215211505599
(82, 80, 86, 76, 76)
0.42900922418651977
-0.4183445889752284
(76, 56, 80, 54, 64)
0.4614751950278446
-0.45876315846991034
(22, 20, 80, 54, 74)
0.4608081403975781
-0.45969041249751896
(18, 18, 8, 72, 88)
0.4809786566415468
-0.48070912739721194
(50, 78, 44, 54, 70)
0.46524086893805183
-0.4633239176812456
(24, 4, 90, 68, 8)
0.4702661087752418
-0.469707488335537
(42, 86, 90, 64, 88)
0.45381561143038596
-0.45193373296337214
(42, 78, 100, 44, 94)
0.46845594059520224
-0.46759882233789085
(68, 70, 4, 98, 52)
0.3940269061566113
-0.3912553354478625
(82, 74, 32, 92, 20)
0.4758661192129239
-0.47538417178388315
(0, 30, 90, 44, 52)
0.38580441172467417
-0.38265804719586427
(16, 56, 56, 80, 60)
0.36223050625807574
-0.3608219343340515
(38, 82, 16, 90, 18)
0.47360719811611673
-0.473100241363845
(14, 22, 4, 100, 86)
0.48182251634273143
-0.48162238254110434
(74, 44, 94, 26, 46)
0.45182674831038483
-0.4503119759603571
(74, 32, 8, 12, 100)
0.4643249988649032
-0.46363899301752554
(10, 46, 22, 18, 0)
0.38813574314606747
-0.3821720138954845
(94, 84, 26, 44, 34)
0.47606743303011
-0.47557132639714084
(24, 74, 58, 2, 16)
0.4642195270678471
-0.4632931185331266
(48, 54, 34, 34, 30)
0.47417976255804994
-0.47246203085268945
(6, 72, 52, 32, 96)
0.4196628345980713
-0.41758398668123675
(12, 50, 36, 22, 12)
0.452329420431024
-0.44984840898970546
(36, 2, 70, 10, 68)
0.4501110724008157
-0.448768249802324
(32, 2, 10, 2, 58)
0.4490362601180351
-0.447222404610784
(24, 26, 84, 32, 56)
0.4489311261672384
-0.44721446892904027
(42, 8, 2, 32, 36)
0.4768857288033477
-0.4760727227937487
(18, 82, 10, 88, 10)
0.48757994810253535
-0.48751543084006244
(30, 50, 94, 12, 22)
0.42009591918895595
-0.41787514575781515
(0, 58, 2, 54, 90)
0.4576980656955669
-0.4568100122626717
(94, 96, 92, 40, 38)
0.48923654979213893
-0.4892121049704308
(22, 94, 52, 94, 94)
0.46427394005512923
-0.46343165527655117
(14, 4, 22, 0, 62)
0.3915392538662985
-0.38756012106282256
(82, 92, 30, 98, 50)
0.46598609982855876
-0.4650951358046278
(46, 52, 32, 88, 48)
0.37355754188754986
-0.3724389424450223
(2, 8, 74, 0, 54)
0.4775750597493911
-0.47717795496581417
(18, 12, 96, 58, 90)
0.4550380729728616
-0.4540851505645449
(92, 90, 66, 54, 68)
0.46353646989871145
-0.4617707372796733
(14, 22, 2, 54, 44)
0.455798457120153
-0.4540750559917939
(98, 8, 2, 2, 54)
0.45539313682186844
-0.4545239524359843
(82, 96, 100, 48, 80)
0.37833736031436516
-0.3729373623440928
(46, 76, 84, 48, 36)
0.4737823298723569
-0.47292510556638234
(0, 66, 100, 42, 6)
0.4305840950729163
-0.4291076204347348
(44, 48, 48, 56, 36)
0.4000446005553675
-0.38694800773431837
(86, 28, 90, 16, 58)
0.4514613152772533
-0.4502289024123378
(66, 100, 86, 82, 0)
0.38632899888258976
-0.3837158746632383
(34, 30, 86, 28, 26)
0.39733356025582367
-0.3972384653532366
(38, 18, 88, 6, 86)
0.4675480126232401
-0.4669112486738314
(86, 0, 68, 90, 74)
0.3882350440842117
-0.3879487129989343
(100, 76, 16, 52, 4)
0.4416072070927086
-0.44033932598837566
(46, 52, 64, 10, 20)
0.4636452113112881
-0.4623778293870231
(48, 56, 28, 68, 26)
0.4510944718645753
-0.4487730511367989
(98, 70, 76, 64, 80)
0.39827213447680343
-0.3909781199119564
(30, 18, 88, 26, 92)
0.4860501039175773
-0.4859319307836003
(66, 94, 32, 32, 82)
0.4596253609710317
-0.45847485367438523
(44, 46, 80, 2, 44)
0.33401747914458113
-0.33203326687961265
(100, 50, 90, 14, 80)
0.44600648937721843
-0.4446732582109725
(48, 68, 0, 6, 22)
0.45522597960949795
-0.4539276197427107
(38, 40, 42, 66, 68)
0.48722002209784776
-0.48701584377207574
'''