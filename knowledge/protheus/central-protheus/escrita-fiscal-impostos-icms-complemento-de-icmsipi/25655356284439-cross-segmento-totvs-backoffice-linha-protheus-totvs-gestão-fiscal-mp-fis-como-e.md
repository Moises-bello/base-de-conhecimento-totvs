---
article_id: 25655356284439
category: Escrita Fiscal - Impostos - ICMS - Complemento de ICMS/IPI
content_hash: 6fc011b389ad529c60d21403b97e98ac0b507bb0afe4dc0c7ef3e7b2bacf5949
fetched_at: '2026-06-28T22:39:21.283311+00:00'
product: protheus
section_id: 1500001538701
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal -
  MP FIS Como Emitir o Complemento de FECP ST para RJ?
type: support-article
updated_at: '2024-08-15T11:38:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25655356284439-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-MP-FIS-Como-Emitir-o-Complemento-de-FECP-ST-para-RJ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25655372362647) Tempo aproximado para leitura: 05:00**min** **Dúvida**Como Emitir o Complemento de FECP ST para RJ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A nota fiscal precisa ser feita pela rotina mata920 em livros fiscais, para colocar a base de calculo do FECP ST

MV\_ESTADO = RJ  
   
Cliente = RJ  
   
Cadastro de Produtos  
![](https://totvssuporte.zendesk.com/attachments/token/dPfMK8ZmGKajIvhcywGBTQWZA/?name=image.png)  
   
UF x UF  
Rj x Rj  
 ![](https://centraldeatendimento.totvs.com/hc/article_attachments/25655356260119)  
  
![](https://totvssuporte.zendesk.com/attachments/token/HzfvMcrOdBtt4IT6C2zcxasX8/?name=image.png)  
   
No meu teste dados da NF original  
Valor da base de calculo do ICMS ST = 1300,00

Valor da base de calculo do FECP ST = 300,00 

MVA = 30%  
  
   
Complemento do FECP ST  
   
TES  
Calcula icms = não  
L fiscal icms = zerado  
Formula = preenchida  
Agrega valor = sim  
Agrega solid = não  
Sit trib icm = 10

MKP icm comp = não

Marg solid = em branco ou configuração  
   
![](https://totvssuporte.zendesk.com/attachments/token/RhudYbr7Jo67Tqb8rhOYCULOZ/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/FqJxqQgorZaDT0WETPT8sqpGx/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/kIHaIJnyIwBKaobuOtOymFyHv/?name=image.png)  
   
Documento manual de saidas  
   
![](https://totvssuporte.zendesk.com/attachments/token/ed8RkV3Y4DRZ0bIO60xuojlvg/?name=image.png)  
   
CD2  
![](https://totvssuporte.zendesk.com/attachments/token/rHwOVBBstcWYyhyOnBZplcmTN/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/Q2qrEuDKkTwpDuAFTKql1uVuW/?name=image.png)  
 

Na CD2 precisa gravar o MVA para não causar rejeição 932
