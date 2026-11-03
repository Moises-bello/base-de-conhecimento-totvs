---
article_id: 15473198697495
category: Escrita Fiscal - Configurador de Tributos
content_hash: e219d4a84889e0618fca744a3730905d027e19de79cc03e4fe58aaa662411b3f
fetched_at: '2026-06-28T22:39:17.344703+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como calcular
  nota fiscal de importação do Paraná com ICMS Diferido?
type: support-article
updated_at: '2026-05-22T19:35:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15473198697495-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-nota-fiscal-de-importa%C3%A7%C3%A3o-do-Paran%C3%A1-com-ICMS-Diferido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15473139362583) Tempo aproximado para leitura: **00:10:00 min** **Dúvida**Como calcular nota fiscal de importação do Paraná com ICMS Diferido?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**MV\_ESTADO = PR  
Fornecedor = EX  
   
![](https://totvssuporte.zendesk.com/attachments/token/DG2JH631DVY6S0VnhnOt1SaCT/?name=image.png)  
   
Cadastro de produtos  
![](https://totvssuporte.zendesk.com/attachments/token/U3M5XTOu3aABIKmMZC5EGGR5z/?name=image.png)  
   
TES  
Calcula ICMS = sim  
Calcula ipi = sim  
CST = em branco  
L fiscal icms = tributado  
L fiscal ipi = tributado  
mat consumo = não

IPI na base = não

Agrega valor = sim

PIS/COF = ambos

Cred pis/cof = não calcula

Perc ICM Dif = 0  
   
Calculo  
 

|  |  |  |
| --- | --- | --- |
| CIF - |  | 10.000,00 |
| II | 9,60% | 960,00 |
| IPI | 3,25% | 356,20 |
| PIS | 2,10% | 210,00 |
| COFINS | 9,65% | 965,00 |
| TX SISC |  | 154,23 |
| DESP ADUANEIRAS |  | 300,00 |
|  |  | 0,00 |
| TOTAL |  | 12.945,43 |
|  |  |  |
| base de calculo do ICMS  12.945,43/0,94 |  | 13.771,73 |

ICMS calculado  = 2.478,91  
**ICMS Diferido (66,67%)  = 1.652,69**  
   
Valor do ICMS destacado = 826,22  
   
**TOTAL NF = 13.771,65**  
   
   
**Configurações no Fisa170**  
   
   
**1A) ID DO TRIBUTO**  
 Criar um imposto ICMPR  
   
![](https://totvssuporte.zendesk.com/attachments/token/nigCEL0iE7XYheSAfoIEYlFd6/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/2cczvPwEgxm1ykkidGvRDAjBJ/?name=image.png)  
 

## **2B) Perfis**

   
Perfil do Produto  
   
Cadastrei um produto na SB1 000030 = Maquinas e Aparelhos  
![](https://totvssuporte.zendesk.com/attachments/token/wYAYmabJ1jUP6J97qPNl7BFJq/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/5AYtHvMqGhNucSQOCXRhJCcaU/?name=image.png)  
   
Perfil da Operação  
000019  
   
![](https://totvssuporte.zendesk.com/attachments/token/uibNCas6sKafMYuxiqkA4dW3G/?name=image.png)Perfil Participante  
000030  
   
![](https://totvssuporte.zendesk.com/attachments/token/27EakALfTnhX0pgSiNrsPcaNi/?name=image.png)  
   
Perfil Origem / Destino  
   
![](https://totvssuporte.zendesk.com/attachments/token/r65gwHNN1kQmUFjBbErI8n0hg/?name=image.png)  
   
3C) Regra de Calculo de Documento Fiscal  
 

## **Regra de Base de Calculo**

   
ICMPR  
   
![](https://totvssuporte.zendesk.com/attachments/token/2KCCy62n8CZK24ysjJ0cmCsPz/?name=image.png)  
Formula  
   
![](https://totvssuporte.zendesk.com/attachments/token/vn8vAERjcSln0O5CUVziFup9J/?name=image.png)  
   
IMPIMP  
   
![](https://totvssuporte.zendesk.com/attachments/token/l41UhnuH408Q671mcC2LUDhys/?name=image.png)  
Formula  
   
![](https://totvssuporte.zendesk.com/attachments/token/1nP9gHMcyqzAv4nc4zRaoELx5/?name=image.png)  
   
IPIIM  
   
![](https://totvssuporte.zendesk.com/attachments/token/fJcM2x2FGFmodGjrAlKlkO0JH/?name=image.png)  
Formula  
   
![](https://totvssuporte.zendesk.com/attachments/token/GjDHd4OIWEBFvMkGWwneWuT02/?name=image.png)  
   
PSCFIM  
   
![](https://totvssuporte.zendesk.com/attachments/token/iTGvXyOI9Gbf1jyt6pYPFGi0k/?name=image.png)  
   
Formula  
   
![](https://totvssuporte.zendesk.com/attachments/token/JZpr7wQMHU4wEJ7NGyDZtUWrx/?name=image.png)  
 

## **Regra de Alíquota**

   
ICMS EFETIVO  
ICMPRE  
   
![](https://totvssuporte.zendesk.com/attachments/token/oqzCRqY9jVcbHFmMP8f7j8fg8/?name=image.png)  
   
ICMS DESEMBARAÇO INTERNO  
ICMPRI  
   
![](https://totvssuporte.zendesk.com/attachments/token/TiKBCgNlsdYtLkJwhFRvHJp28/?name=image.png)  
   
IMPOSTO IMPORTAÇÃO  
IMPIMP  
   
![](https://totvssuporte.zendesk.com/attachments/token/ulcI6b9FS5hWQLnPdPxX16w29/?name=image.png)  
   
IPI IMPORTAÇÃO  
IPIIM  
   
![](https://totvssuporte.zendesk.com/attachments/token/lPxGhfaHYZbILubGj3dVAEsDw/?name=image.png)  
   
PIS IMPORTAÇÃO  
PISIM  
   
![](https://totvssuporte.zendesk.com/attachments/token/5FIcb5J7HKJNcYdFjhxg3jvq1/?name=image.png)  
   
COFINS DE IMPORTAÇÃO  
COFIM  
   
![](https://totvssuporte.zendesk.com/attachments/token/ktJ8Bcd65A2FePJYYip8jSH3J/?name=image.png)  
 

## **Regra de Escrituração**

   
ICMS IMPORTAÇÃO PARANA  
000030  
   
![](https://totvssuporte.zendesk.com/attachments/token/jFr8T9dpD3RSjDI87oizIQxTo/?name=image.png)  
   
PIS IMPORTAÇÃO  
000031  
![](https://totvssuporte.zendesk.com/attachments/token/YZ6fdrIVvnh7ScRDJbQl3KrBJ/?name=image.png)  
   
COFINS IMPORTAÇÃO  
000032  
   
![](https://totvssuporte.zendesk.com/attachments/token/2X9LOUOTQYWk6zyJQJZv9eYyM/?name=image.png)  
   
IMPOSTO DE IMPORTAÇÃO  
000033  
   
![](https://totvssuporte.zendesk.com/attachments/token/WDdSiYTXBZ3NzqS8reLpkApFG/?name=image.png)  
 

## **Regra de Calculo Documento Fiscal**

   
ICMS IMPORTAÇÃO PARANA  
ICMPR1  
   
![](https://totvssuporte.zendesk.com/attachments/token/34WX0P7AbEBVIK37jHaDDEcea/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/ftJB0YRhrnBbarPAmLyRNBw0y/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/5p5GYzWrwmQZLsY0oAFBjBKZK/?name=image.png)  
   
Detalhamento da Formula  
   
![](https://totvssuporte.zendesk.com/attachments/token/3yOx2r2ww4yrhfYoRrfhQzPBg/?name=image.png)  
   
Aba isento e outras em branco  
   
II IMPORTAÇÃO  
IMPIMP  
   
![](https://totvssuporte.zendesk.com/attachments/token/uYiV1DaKlw9G11f9MlUUm05ub/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/ZU0fGohEhnR0b9wY73Vruv6hY/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/tXnRSARJnazc9Zvkz4zn0pXHI/?name=image.png)  
   
IPI IMPORTAÇÃO  
IPIIM  
   
![](https://totvssuporte.zendesk.com/attachments/token/Z0tYiGBZf1NQX2ZPDeg75XYxy/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/TBBEHZp7hdub9CvxLHWUNStgW/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/6757nybAsNQn7vTfiAFZzvyuy/?name=image.png)  
Para o IPI não criei regra de escrituração pois o MATXFIS soma de forma automática no valor total da nota fiscal  
Na TES configure a situação tributária do IPI  
   
PIS IMPORTAÇÃO  
PISIM  
   
![](https://totvssuporte.zendesk.com/attachments/token/aNTAwdy5sCXB4FDjDZ23lna80/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/6A7aug8fWh3dAvUZplUkRBr8e/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/78BzJF6flPywUv9nRU4dFvspV/?name=image.png)  
COFINS IMPORTAÇÃO  
COFIM  
   
![](https://totvssuporte.zendesk.com/attachments/token/xEEvEWA2ZTweKXK9gW0wOSzdi/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/iV3KMA4DNPBuSpHg4iBLneTMJ/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/P3sAEjQ9XJY29bIcAotT0yunS/?name=image.png)  
Lançamento da nota fiscal no mata103  
   
Após cadastrar as regras de base de calculo deve ser configurado as formulas do ICMS e IPI  
 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15472850974103)  
Livros Fiscais

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15472923520407) Duplicata

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15472918610967)  
  
Detalhamento da Formula de ICMS (ICMPR ) , IPI ( IPIIM ) segue em vídeo   
   
ICMPR  
( O:VAL\_MERCADORIA - O:DESCONTO + O:FRETE + O:SEGURO + O:DESPESAS + VAL:IMPIMP + VAL:IPIIM + VAL:PISIM + VAL:COFIM ) / ( 1 - ( A:ICMPRE ) / 100 )  
   
IPIIM  
( O:VAL\_MERCADORIA - O:DESCONTO + VAL:IMPIMP )
