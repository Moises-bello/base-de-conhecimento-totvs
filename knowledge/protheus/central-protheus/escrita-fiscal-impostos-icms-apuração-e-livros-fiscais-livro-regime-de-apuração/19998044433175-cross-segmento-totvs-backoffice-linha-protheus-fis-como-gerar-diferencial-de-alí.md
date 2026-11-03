---
article_id: 19998044433175
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: 3a8db970fd864bde12593c4285b2b02452f8a4d4bcbd8e1ab3cc4b7f08870047
fetched_at: '2026-06-28T22:39:22.084006+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS -  Como gerar Diferencial
  de alíquotas na Apuração do RJ por reflexo?
type: support-article
updated_at: '2024-12-09T18:02:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19998044433175-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-gerar-Diferencial-de-al%C3%ADquotas-na-Apura%C3%A7%C3%A3o-do-RJ-por-reflexo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19998060407447) Tempo aproximado para leitura: 05:00**min** **Dúvida**Como gerar Diferencial de alíquotas na Apuração do RJ por reflexo?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**MV\_ESTADO = RJ  
MV\_P9AUTO = F  
MV\_P9SPED = .F.  
MV\_USASPED = .T.  
MV\_BASDENT= RJ  
   
Fornecedor = SP  
   
UF x UF  
Sp para RJ  
![](https://totvssuporte.zendesk.com/attachments/token/lVx0tjRywy4xXLsLazFiYmWhD/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/fzEIfNV730KOQw6zESd55Jca8/?name=image.png)  
   
   
TES  
Calcula ICMS = sim  
L. fiscal ICMS = outros  
Sit. trib. icm. = 90  
Mat. consumo = sim  
Calc. dif. icm. = sim  
Calc. difal = não ou em branco  
   
![](https://totvssuporte.zendesk.com/attachments/token/xxziiFp2JdVt0a98b4P8fkCvD/?name=image.png)  
    
Reflexo 0000150  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23631713669015)  
   
Reflexo 0000190  
![](https://totvssuporte.zendesk.com/attachments/token/3MOUx7idGagRtjUqERnPJL20W/?name=image.png)  
Exemplo do calculo  
Valor da mercadoria = 250,00  
   
Base de calculo do ICMS = 250,00\*12% = 30,00  
Base dupla do Difal = 250,00-30,00 = 220,00  
220,00/0,80 = 275,00  
275,00\*20% = 55,00-30,00= 25,00  
275,00 \*2% = 5,50  
   
lançamento da nota fiscal de entradas  
   
![](https://totvssuporte.zendesk.com/attachments/token/5JqSe4PogTkMDMIU05aLafua6/?name=image.png)  
   
Lançamento da apuração  
![](https://totvssuporte.zendesk.com/attachments/token/LbLGNBm58QlMJsqPdvosQrbTV/?name=image.png)  
   
Apuração do ICMS  
   
![](https://totvssuporte.zendesk.com/attachments/token/m6jqziFBHJ4slY8JgSBf4UTmg/?name=image.png)  
   
Debitos especiais  
![](https://totvssuporte.zendesk.com/attachments/token/O5hdsYCuRdhM6cZRoIahqYwMm/?name=image.png)  
 

Boletim do Reflexo

<https://tdn.totvs.com/pages/releaseview.action?pageId=640907320>

Boletim da apuração do ICMS

<https://tdn.totvs.com/pages/releaseview.action?pageId=270894388>
