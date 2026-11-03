---
article_id: 33071442613271
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 6d2571b31703ad84bec7d55f7e81ee5b5e89614254806e6174675296de341989
fetched_at: '2026-06-28T22:40:52.742669+00:00'
product: protheus
section_id: 1500001537561
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 - ECD - ESTRUTURA
  NIVEL VISÃO GERENCIAL J100 E J150
type: support-article
updated_at: '2025-06-26T14:44:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33071442613271-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-ESTRUTURA-NIVEL-VIS%C3%83O-GERENCIAL-J100-E-J150
---

**Dúvida**

Considerando a  regra de [NIVEL (NIVEL\_AGL) definida pela receita , como deve ser extruturada a visão gerencial de Balanço (J100) e DRE (J150) , para entrega da ECD?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028148692-MP-SIGACTB-ECD-I050-5-NIVEL-O-plano-de-contas-com-todas-as-suas-contas-sint%C3%A9ticas-e-anal%C3%ADticas-deve-conter-no-m%C3%ADnimo-4-n%C3%ADveis-Resolu%C3%A7%C3%A3o-CFC-1299-2010-?source=search)

**Ambiente**

Cross Segmento - TOTVS Backoffice Linha Protheus - Contabilidade gerencial - Todas as versões  
  
**Solução**   
Para solucionar essa dúvida, realize os seguintes passos:

O nível de aglutinação criada na Visão segue "(mesmo conceito do plano de contas – Registro I050)"

* [NIVEL O plano de contas com todas as suas contas sintéticas e analíticas deve conter no mínimo 4 níveis , sendo 3 níveis sintéticas (Resolução CFC 1299/2010).](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028148692-MP-SIGACTB-ECD-I050-5-NIVEL-O-plano-de-contas-com-todas-as-suas-contas-sint%C3%A9ticas-e-anal%C3%ADticas-deve-conter-no-m%C3%ADnimo-4-n%C3%ADveis-Resolu%C3%A7%C3%A3o-CFC-1299-2010-?source=search)
* Veja o que o manual da receita descreve sobre o  Campo 05  NIVEL\_AGL , para o J100 e o J150

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33071435783703)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33071435784599)

* Com isso a configuração adequada da visão gerencial :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33071435785495)

* Exemplo de montagem da DRE :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33071442583575)

* É preciso que os campo "Entid.gerenc", "Entid.Super"  e o "Ordem" estejam devidamente preenchidos , pois com base nesses campo que o sistema irá aglutinar no J150

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33071435788183)

* Veja como os campos "Entid.gerenc", "Entid.Super" e " Ordem", foram devidamente preenchidos

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33071442586647)

* Exemplo de montagem do Balanço:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33071435790743)

* É preciso que os campo "Entid.gerenc", "Entid.Super"  e o "Ordem" estejam devidamente preenchidos , pois com base nesses campo que o sistema irá aglutinar no J100

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33071442588951)

* Veja como os campos "Entid.gerenc", "Entid.Super" e " Ordem", foram devidamente preenchidos

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33071442590743)

* Dependendo da configuração do [parâmetro MV\_GRVISOR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023832631-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA161-ORDENA%C3%87%C3%83O-RELAT%C3%93RIO-DRE-e-BALAN%C3%87O-X-ECD-J00-e-J150)  o sistema irá considerar para ordenar o J100 e o J150   "Entid.gerenc", "Entid.Super" , ou com base " Ordem"
