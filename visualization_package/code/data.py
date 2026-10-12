# Per-study data model, derived from the verified extraction workbook
# fields: cite, year, species, task(M/Q/F), levels, fam, mm(multimodal/non-RGB), avail(P/R/N), tier, acc, altm, flag(headline source conflict), inc(internal inconsistency),
# N, unit, qd = "D1 D2 D3 D4 A1 A2 A3", why = rationale, dec(explicit decay/overripe class), anch(shelf-life/commercial anchor)
S = {}
def add(id, cite, year, species, task, levels, fam, mm, avail, tier, acc, altm, flag, inc, N, unit, qd, why, dec=False, anch=False, model=''):
    S[id] = dict(id=id, cite=cite, year=year, species=species, task=task, levels=levels, fam=fam, mm=mm, avail=avail, tier=tier,
                 acc=acc, altm=altm, flag=flag, inc=inc, N=N, unit=unit, qd=qd.split(), why=why, dec=dec, anch=anch, model=model)
add('P001','Wu et al. (2026)',2026,['avocado'],'F',None,'FM',True,'N','II',None,'MAE 0.94-7.10 (ordinal label); MSE 1.75-82.3',False,True,12000,'images (150 fruit)','U L L L H H L',
 'D1 lab collection, 150 fruit; D2 fruit-ID confined to one partition (test and validation combined); D3 daily labels through spoilage; A1 controlled lab; A2 RGB+spectra',anch=True,model='GPT-4o + GLIP/SAM + BERT spectral encoder; ResNet/ViT/Swin-V2 heads')
add('P005','Ahmad et al. (2026)',2026,['mango'],'F',5,'CNN',False,'P','III',99.2,'Proposed SE-DBIRNet 98.2 (F1 96.1)',True,True,4428,'images','U U U L H L L',
 'D1 public studio dataset not collected by authors; D2 10-fold CV with 70/15/15 inside each fold, fruit grouping not stated; D3 stage labels inherited from source; A1 consistent studio illumination',dec=True,model='SE-DBIRNet (dual-path residual + SE)')
add('P008','Li et al. (2021)',2021,['apple'],'Q',3,'CNN',False,'N','II',95.33,'',False,False,3600,'images (+300 test fruit)','U L H U U L H',
 'D2 independent 300-fruit test (headline); augmentation preceded the random split in development evaluation; D3 grades from appearance, criteria not specified; A1 time/angle/light varied',model='Custom 6-conv CNN; Inception V3; HOG/GLCM+SVM')
add('P009','Kripa & Jeyalakshmi (2026)',2026,['mango'],'M',3,'CNN',True,'R','II',97.86,'RGB-only fusion 91.52',True,True,600,'observations (120 fruit)','U U H H H H L',
 'D2 fruit-identity split but confusion matrices total 490 vs 120 test; D3 classes derived by k-means on biochemical vectors that are also predictors; D4 CGAN/SMOTE expansion (2,018 synthetic pairs, train-only)',model='DenseNet201+Inception-ResNetV2+EfficientNetV2 fusion + biochemical encoder')
add('P010','Zhuang et al. (2019)',2019,['banana'],'M',4,'CL',False,'N','II',100.0,'',False,False,321,'images/fruit','U L H L H L L',
 'D2 one image per fruit, separate 121-image test; D3 maturity stages defined from peel appearance; A1 fixed lab set-up',model='NB / LDA / SVM on colour, LBP, HOG')
add('P011','Liu, Y. et al. (2024)',2024,['tomato'],'M',3,'CNN',True,'N','II',99.4,'RGB-only VGG16 94.2',True,True,856,'images (214 fruit)','U U L L H H L',
 'D2 split proportions inconsistent, fruit grouping not stated, matrix has 169 observations; D3 skin plus cross-section red coverage; A2 RGB+Vis/NIR+haptics',model='VGG16 + 1D-CNN + LSTM fusion')
add('P013','Liu, X. et al. (2025)',2025,['plum'],'Q',3,'CNN',True,'R','II',100.0,'RGB-only VGG16 85.71',True,True,2340,'images (780 fruit)','U H H H H H H',
 'D2/D4 minority-class augmentation not limited to training; D3 grade score includes red ratio and circularity, which are model inputs; A2 RGB+Vis/NIR',model='VGG16 + 1D-CNN + handcrafted features (Bi-Mod Hybrid Net)')
add('P015','Olisah et al. (2024)',2024,['blackberry'],'M',2,'CNN',True,'R','I',95.1,'Synthetic perturbation 92.7 / 90.2',False,True,201,'images (301 fruit)','L U U U L H L',
 'D1 two commercial UK farms; D2 grouping not stated, no farm hold-out; D3 subjective ripeness (trained assessor on one farm, non-expert on the other); D4 blur/reference failures excluded; A2 two-band 700/770 nm imaging',model='VGG16 twin-input bootstrap ensemble + stacking')
add('P017','Ismail & Malik (2022)',2022,['apple','banana'],'Q',2,'CNN',False,'N','I',99.5,'Banana 98.9; run-time 96.7 / 93.8',True,True,8939,'images (8,639 apple + 300 banana)','U U H U L L U',
 'D1 secondary datasets, run-time test only 30 and 32 fruit; D3 labels from appearance; D4 apple N 8,791 vs 8,639; A3 apple defect task has no decay class',dec=True,model='EfficientNet B0-B2 stack; EfficientNet-B2 embedded')
add('P018','Wei et al. (2022)',2022,['grape'],'M',4,'CL',False,'R','I',88.0,'',True,True,295,'bunches/samples','L H L U L L L',
 'D2 hidden neurons selected on test accuracy; D3 maturity coefficient from SSC, acid and berry traits; A1 greenhouse imaging',model='BPNN on colour features')
add('P019','Zhou et al. (2021)',2021,['strawberry'],'M',7,'DET',False,'N','I',None,'mAP 0.73-0.89',False,False,4859,'images','L H H U L L L',
 'D2 80/20 train/validation only, overlapping UAV views; D3 manual appearance labels; A1 field imaging',dec=True,model='YOLOv3')
add('P020','Wakchaure et al. (2024)',2024,['custard apple'],'M',5,'CL',False,'R','I',100.0,'',False,False,455,'images','H U H U L L L',
 'D1 only 455 of 2,275 images (defect-free, ideal colour transition) retained; D2 random split, no grouping; D3 areole-opening appearance',model='K-means segmentation + SVM')
add('P022','Jaramillo-Acevedo et al. (2020)',2020,['avocado'],'M',3,'CL',False,'N','II',88.0,'Mean of class rates 100/80/85',True,True,130,'fruit','U U U U U L L',
 'D2 no train/validation/test counts, 65 evaluation samples; D3 label assignment criterion unclear; A1 illumination varied with flash',model='MLP on RGB means + GLCM')
add('P024','Mousse et al. (2024)',2024,['tomato'],'M',5,'DET',False,'N','III',97.06,'Validation set (2,912/3,000)',True,False,None,'not reported','H H H H U L L',
 'D1 internet images; D2 train/validation only, augmented; D4 augmentation-expanded; draft version of the paper',model='Superpixel+CNN detector; attention RNN/LSTM classifier')
add('P025','Chuquimarca et al. (2023)',2023,['banana'],'M',4,'CNN',False,'N','II',91.7,'Real-only 87.2',True,True,3495,'real images (+161,280 synthetic)','U U L H H L L',
 'D2 daily images of the same fruit, grouping not reported; D3 storage-day bands; D4 rotting images discarded, synthetic expansion',anch=True,model='CIDIS CNN, synthetic pre-training')
add('P026','Wang, L. (2022)',2022,['kiwifruit'],'Q',5,'CL',False,'N','II',97.5,'',False,True,326,'images','U U U U H L H',
 'D2 all 326 images described as test, training split not reported; D3 professional grading; A1 closed box',model='Deep extreme learning machine')
add('P027','Xie et al. (2024)',2024,['sugar apple'],'M',3,'SEG',False,'R','II',None,'mIoU 89.95; pixel acc. 96.6',False,False,1000,'images (30 fruit)','H U H L U L L',
 'D1 only 30 sugar apples; D2 random image split from 30 fruit; D3 expert-checked annotation of appearance',dec=True,model='ECD-DeepLabv3+')
add('P028','Abdullah (2025)',2025,['apple','banana','mango','orange','strawberry'],'F',2,'CNN',False,'P','III',100.0,'',True,True,5997,'images','H U U H U L L',
 'D1/D4 public and web sources mixed; D2 metrics described as validation and as test; D3 inherited labels',dec=True,model='ResNet50, MobileNetV2, VGG16, EfficientNetB0')
add('P029','Ji et al. (2023)',2023,['apple'],'Q',3,'TR',False,'R','I',94.0,'Offline precision/accuracy 94.46',False,True,1244,'images (300 online fruit)','L U L L L L H',
 'D2 image-level split, independence of 300 online fruit not stated; D3 national grading standard GB/T 10651-2008; A1 conveyor line',model='YOLOv5s + Swin Transformer')
add('P030','Villasenor-Aguilar et al. (2024)',2024,['orange'],'M',4,'CL',False,'P','II',None,'R2 0.95-0.98; MSE reported',True,True,75,'fruit','H H H L H L L',
 'D1 75 fruit; D2 no held-out set; D3 colour-category labels from the input colour index',model='Takagi-Sugeno fuzzy / ANFIS')
add('P031','Liu, C. et al. (2023)',2023,['passion fruit'],'Q',4,'DET',False,'R','II',None,'mAP50 95.36; F1 89.3',False,False,1114,'images','U U L L U L H',
 'D2 original-image split, no fruit grouping or validation set; D3 modified Codex STAN 316-2014; Bad grade mixes unripe, rotten and other defects',model='ATC-YOLOv5')
add('P033','Yang et al. (2024)',2024,['banana'],'F',3,'CNN',False,'R','II',98.8,'Recalculated 98.33 (118/120)',True,True,600,'images','U U U U H L L',
 'D1/D4 600 of 1,500 images retained; D2 Figure 9 vs Table 1 test counts conflict, daily repeated imaging; D3 peel grades mapped to commercial periods',anch=True,model='ResNet-101')
add('P034','Kosasih et al. (2023)',2023,['banana'],'M',6,'CL',False,'N','II',86.67,'SVM 80.0',True,True,45,'images','H H H U U L L',
 'D1 45 images; D2 15-image test; D3 appearance; identical training/test vector',model='Naive Bayes / SVM on grayscale histogram statistics')
add('P035','Yin et al. (2022)',2022,['apple'],'Q',5,'CNN',False,'R','II',95.64,'',True,True,11020,'images','U U H L H L U',
 'D2 random 6:2:2 image split, evaluation described as validation and test; D3 defect appearance labels; A3 defect classes include rot',dec=True,model='OB-Net (double-branch ResNet-18)')
add('P036','Reka et al. (2024)',2024,['apple','banana','orange','papaya','guava'],'F',2,'CNN',False,'N','III',95.0,'Banana storage-day RF 88.0',True,True,None,'not reported','H U H H U L L',
 'D1/D4 multi-source dataset, counts and split not given; D2 evaluation subset unclear; D3 visual labels (banana day classes anchored to storage days)',dec=True,anch=True,model='Basic CNN, VGG16, InceptionV3; RF/GNB on hue')
add('P038','Song et al. (2023)',2023,['cherry'],'F',4,'TR',False,'R','I',98.5,'Recalculated 98.45 (828/841)',True,True,4669,'images','L H H H L L L',
 'D2/D4 broken class augmented before split (260 augmented images in test); D3 peel appearance; A1 orchard imaging',dec=True,model='Swin-T features + MLP')
add('P039','Cai et al. (2022)',2022,['orange'],'F',2,'CL',True,'R','II',98.8,'All 280 fruit 96.4',False,False,280,'fruit','U L L L H H L',
 'D1 inoculated fruit, lesion facing camera; D2 fruit-level hold-out (79/80); D3 Penicillium inoculation, tissue cutting; A2 680-nm structured illumination, monochrome',dec=True,model='PLS-DA, SVM, LS-SVM, KNN on GLCM')
add('P040','Dao et al. (2023)',2023,['tomato'],'Q',2,'DET',False,'N','I',94.4,'Offline mAP 99.5 (validation)',False,False,370,'images (250 trial fruit)','L H H H L L H',
 'D2/D4 augmentation before split; D3 visual good/bad labels; A1 conveyor prototype trial; A3 NG class mixes cracks, rot, pests',model='CNN-YOLOv8')
add('P041','Sugumar et al. (2019)',2019,['citrus'],'M',2,'CL',False,'N','II',100.0,'PKM rotten false negatives 13%',False,False,650,'images (claimed)','U H H U H L L',
 'D2 25 test images per variety, no validation; D3 colour/size reference derived from inputs',dec=True,model='KNN on colour and geometry')
add('P042','Trieu & Thinh (2023)',2023,['mango'],'Q',3,'CL',True,'N','II',98.3,'Cross-validation curve',True,False,732,'fruit','L L H L H H H',
 'D2 459/136/137 fruit-level split; D3 grade rules reuse the input features; A2 image + load cell',model='Random forest')
add('P043','Wang, J. et al. (2022)',2022,['apple'],'Q',4,'CL',True,'P','II',96.67,'',False,False,120,'fruit (integrated trial)','U H L U H H H',
 'D2 rule thresholds tested on the samples used to design them; D3 adapted national grading rules and Brix; A2 RGB + NIR',model='Rule-based thresholds + CARS-PLS')
add('P044','Khatun et al. (2024)',2024,['dragon fruit'],'M',2,'CNN',False,'P','I',98.0,'Maturity 90.0',False,True,3780,'images','L U H U L L L',
 'D1 three farms; D2 random image split, augmentation order unclear; D3 expert guidance, no laboratory validation',model='ResNet-50')
add('P046','Nguyen et al. (2024)',2024,['apple','pear'],'Q',5,'SEG',False,'N','II',None,'Pearson r 0.78-0.96',False,False,1553,'fruit (scald)','U H H U U L H',
 'D2 starch thresholds calibrated and evaluated on the same 72 fruit; D3 technician ratings, no gold standard; A3 scald severity, not decay',model='Mask R-CNN + image analysis')
add('P047','Liang et al. (2022)',2022,['apple'],'Q',3,'DET',False,'R','I',92.42,'Recalculated 94.33 (183/194)',True,True,3000,'images (194 test fruit)','U L L L L L H',
 'D2 separate 194 supermarket fruit tested online; D3 local grading rule and defect area; A3 defect-area grades',model='BiSeNetV2 + pruned YOLOv4')
add('P050','Chen, M.-C. et al. (2022)',2022,['apple','orange','lemon'],'Q',2,'DET',False,'N','II',None,'Avg P/R/F1 88-89',True,True,6381,'images','U U U U U L H',
 'D1/D2/D4 totals and split ratios conflict across tables; D3 defect definitions not reported',model='Tiny-YOLOv3 + CNN / autoencoder')
add('P051','Trinh & Nguyen (2023)',2023,['pineapple'],'M',None,'DET',False,'P','I',None,'mAP 96.8 / 98.76',True,True,50000,'images (claimed)','U H H H L L L',
 'D2 split and support not reported; D3 colour annotation; D4 stage definitions (2/3/4/9) and pre-training data inconsistent',model='YOLOv5')
add('P052','Cheng et al. (2022)',2022,['tomato'],'Q',4,'DET',False,'N','I',None,'mAP 99.7-100',False,False,2000,'video frames','L U H U L L U',
 'D2 video-derived frames, no grouping; D3 expert appearance annotation; A1 orchard video',model='YOLOv4')
add('P053','Fahad et al. (2022)',2022,['apple','banana','guava','orange','lemon','tomato'],'F',3,'DET',False,'P','III',82.2,'mAP50 0.840',True,True,60059,'images','H U H H U L L',
 'D1/D4 mobile and internet sources mixed; D3 manual appearance labels; includes medium-fresh class',dec=True,model='VGG16; YOLOv5m')
add('P054','Kazi & Panda (2022)',2022,['apple','banana','orange'],'F',2,'CNN',False,'P','III',99.7,'',True,True,13599,'images','H H H U U L L',
 'D1 Kaggle images; D2 best architecture chosen on test scores, split percentages inconsistent; D3 appearance folders',dec=True,model='AlexNet, VGG16, ResNet-50 (not pretrained)')
add('P055','Mukhiddinov et al. (2022)',2022,['apple','banana','orange','strawberry','mango'],'F',2,'DET',False,'P','III',None,'AP50 73.5 (detector)',True,True,12000,'images','H U H H U L L',
 'D1/D4 phone and web images mixed; D2 split ratios and 2,000-image matrix subset do not reconcile; D3 manual boxes',dec=True,model='Improved YOLOv4')
add('P056','Sofian et al. (2024)',2024,['apple','banana','orange'],'F',2,'CNN',False,'P','III',97.61,'',True,True,30357,'images','H H U H U L L',
 'D1 pre-augmented Kaggle data; D2 re-split without grouping (augmented siblings); D4 pre-augmented dataset',dec=True,model='EfficientNetV2-S, MobileNetV2, VGG19')

# Excluded at full-text assessment
X = {
'P002':('Xuan et al. (2022)','a','Hyperspectral-only input; continuous SSC, firmness and size regression'),
'P003':('Zhu et al. (2025)','a','Hyperspectral-only input; colour, SSC and firmness regression'),
'P006':('Skolik et al. (2019)','a','ATR-FTIR spectroscopy; no image predictor'),
'P007':('Ibba et al. (2021)','a','Bioimpedance; no image predictor'),
'P014':('Lee et al. (2024)','a','Destructive GC-MS metabolomics; no image predictor'),
'P016':('Ktenioudaki et al. (2022)','a','Hyperspectral-only input; continuous quality and shelf-life regression'),
'P021':('Chen, Y. J. et al. (2022)','a','Acoustic signals; no image predictor'),
'P032':('Worasawate et al. (2022)','a','Point colour sensor, weight and capacitance; not camera images'),
'P045':('Tan et al. (2025)','a','Raman spectroscopy of excised peel'),
'P048':('Brilliantina et al. (2026)','a','Gas, thermal and acoustic sensors; not image-based'),
'P057':('Masuduzzaman et al. (2026)','a','Temperature/humidity sensor model; no learned image classifier'),
'P004':('Singh et al. (2026)','b','Nutritional-quality regression; grades derived from destructive nutrient thresholds'),
'P012':('Nouri et al. (2025)','b','Continuous firmness regression from active vibration video'),
'P049':('Ibrahim et al. (2016)','b','Shape and mass sorting only'),
'P058':('Sonwani et al. (2022)','b','Produce-type identification plus sensor alerts; no validated freshness endpoint'),
'P023':('Osman et al. (2022)','c','Descriptive clustering and photogrammetry; no held-out classification metric'),
'P037':('Ratprakhon et al. (2020)','c','Calibrated colour measurement; no trained classifier or accuracy'),
'P059':('Haidar et al. (2012)','d','Published 2012 (outside 2016-2026 window); date-variety identification'),
'P060':('Kavdir & Guyer (2004)','d','Published 2004 (outside window); monochrome NIR defect classification, not RGB'),
}
