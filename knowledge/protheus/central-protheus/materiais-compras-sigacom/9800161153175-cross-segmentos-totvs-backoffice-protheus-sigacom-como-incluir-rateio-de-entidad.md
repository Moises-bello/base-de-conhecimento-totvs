---
article_id: 9800161153175
category: Materiais - Compras (SIGACOM)
content_hash: f8a2ba29a23bfc2314a2674a7f4290f3a27759c9fd827c866de2e9132a46cb00
fetched_at: '2026-06-28T22:41:15.955764+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como incluir Rateio
  de Entidades Contábeis na Solicitação de Compras ?
type: support-article
updated_at: '2026-06-22T14:30:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9800161153175-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-incluir-Rateio-de-Entidades-Cont%C3%A1beis-na-Solicita%C3%A7%C3%A3o-de-Compras
---

Na rotina MATA110 de Solicitação de Compras do TOTVS Protheus, é possível incluir rateio de Centro de Custos e outras Entidades Contábeis por item, via "Outras Ações - Rateio", com percentuais que somem 100%. O rateio acompanha o item no Pedido de Compras, apaga campos contábeis da linha e é preenchido manualmente, sem automatização ou uso de valores, apenas percentuais.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38137681227543) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**  
Como incluir Rateio de Entidades Contábeis na Solicitação de Compras  ?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as versões

**Solução**

Na rotina de Solicitação de Compras  MATA110, é possível a inclusão de rateio de Centro de Custos e demais Entidades Contábeis através da opção "Outras Ações - Rateio" da imagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9800060099735)

Escolher os centros de custos e demais entidades contábeis desejadas e os percentuais de rateio que devem somar 100%:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9800064436247)

***Obs.1:***

Este rateio de Entidades Contábeis, tem sua funcionalidade por item da Solicitação de Compras, e não para a SC como um todo.

***Obs.2:***

Quando o item da SC que possui rateio é vinculado na inclusão de um Pedido de Compras, este rateio da SC é levado também para o Rateio de Entidades Contábeis do Pedido de Compras.

***Obs.3:***

Quando incluído o Rateio de Entidades Contábeis ao item, os campos C1\_CC (Centro de Custo), C1\_CONTA (Conta Contábil), C1\_ITEMCTA (Item Conta) e C1\_CLVL (Classe Valor) são apagados da linha do item.

***Obs4:***

No uso desta opção de Rateio de Entidades Contabeis, a rotina não possui uma funcionalidade ou parametrização de preenchimento automático, para que o campo de Conta Contábil ou de alguma das outras Entidades Contabeis da tela da Rateio, ja venha preenchido com alguma informação (trazida por exemplo do cadastro de produtos), sendo que no padrão, a possibilidade é apenas através do preenchimento manual das Entidades Contabeis nesta opção de Rateio.

Caso deseje pode-se avaliar a possibilidade através de uma customização conforme a necessidade.

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Quais são os Pontos de Entrada disponíveis na rotina MATA110 - Solicitação de Compras ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028916371-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Quais-s%C3%A3o-os-Pontos-de-Entrada-dispon%C3%ADveis-na-rotina-MATA110-Solicita%C3%A7%C3%A3o-de-Compras)

***Obs5:***

No uso desta opção de Rateio de Entidades Contabeis da rotina de SCs, por padrão a opção não possui uma funcionalidade ou paramentrização para informação do rateio utilizando valor, havendo apenas a possibilidade de informação de percentuais de rateio pra cada linha de entidades contábeis.

***Saiba Mais :***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
