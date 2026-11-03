---
article_id: 360028884371
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 1a50c885e659538a57de42abefcf956ce61d71cae75df3b62473dce47c665403
fetched_at: '2026-06-28T22:42:10.717133+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Declan RJ -
  Como é considerado os valores no quadro D
type: support-article
updated_at: '2022-08-17T20:15:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028884371-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Declan-RJ-Como-%C3%A9-considerado-os-valores-no-quadro-D
---

**Dúvida**Como é considerado os valores do quadro D  
  
**Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução****Sequencial 0005** - Será somado o campo F3\_VALIPI de todos os documentos de saída (independente do CFOP) que estão com o campo F4\_INCIDE diferente de 'S'.  
   
**Sequencial 0029** - Será somado o campo F3\_VALCONT de todos os registros que estão com o campo F4\_INCIDE igual a 'S'

**Sequencial 0037** - Quando o CFOP for 5949,6949 ou 7949, o sistema pega a diferença dos campos F3\_VALCONT e F3\_BASEICM (F3\_VALCONT - F3\_BASEICM).

Quando o CFOP for :  
5210/6210/7210/5414/6414/5415/6415/5657/6657/5904/6904/5601/5602/5605/5606/5663/5664/5665/5666/6663/6664/6665/6666/5901/5902/5903/6901/6902/6903/5905/5906/5907/5908/5909/6905/6906/6907/6908/6909/5912/5913/5914/5915/5916/5917/5918/5919/5920/5921/5922/5923/5924/5925/6912/6913/6914/6915/6916/6917/6918/6919/6920/6921/6922/6923/6924/6925/5926/5929/6929/5933/6933/7930/ (exceto 5949,6949 e 7949) ou estiver no parâmetro MV\_DECIT10 o sistema irá somar o conteúdo do campo F3\_VALCONT.  
  
**Sequencial 0007** - Soma do campo F3\_VALCONT para todos os CFOPs: '1406','2406','1551','2551','3551','1552','2552','1553','2553','3553','1554','2554','1555','2555' mais os que estiverem no parâmetro MV\_DECIT01

**Sequencial 0008** - Soma do campo F3\_VALCONT para os CFOPs: '1407','2407','1556','2556','3556','1557','2557'.

**Sequencial 0010** - Soma do campo F3\_VALIPI para os CFOPs que estão no parâmetro MV\_DECIT04

**Sequencial 0036** - Quando o CFOP for 1949,2949 ou 3949, o sistema pega a diferença dos campos F3\_VALCONT e F3\_BASEICM (F3\_VALCONT - F3\_BASEICM).

Quando o CFOP for :  
1126,2126,3126,1154,2154,1414,2414,1415,2415,1904,2904,1601,1602,1604,1605,1663,1664,2663,2664,1901,1902,1903,2901,2902,2903,1905,1906,1907,1908,1909,2905,2906,2907,2908,2909,1912,1913,1914,1915,1916,1917,1918,1919,1920,1921,1922,1923,1924,1925,2912,2913,2914,2915,2916,2917,2918,2919,2920,2921,2922,2923,2924,2925,1926,1933,2933,3930, ou estiver no parâmetro MV\_DECIT05 o sistema irá somar o conteúdo do campo F3\_VALCONT.
