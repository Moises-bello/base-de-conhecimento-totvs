---
article_id: 1500001869541
category: Materiais - Compras (SIGACOM)
content_hash: 5b1034ee8809b9cb3ecf8e64c3ce5bb3af5b6fe255855ff3b76c42938c3f90ad
fetched_at: '2026-06-28T22:41:17.142333+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Diferença entre " Aprovador
  Especial " x " Aprovador Padrão " na rotina Tipo de Compras (COMA200)
type: support-article
updated_at: '2023-09-06T20:30:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001869541-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Diferen%C3%A7a-entre-Aprovador-Especial-x-Aprovador-Padr%C3%A3o-na-rotina-Tipo-de-Compras-COMA200
---

**Dúvida**Diferença entre " Apv Especial " x " Aprov Padrão " na rotina Tipo de compras (COMA200).  
  
**Ambiente**  
Protheus – Compras – A partir da versão 11.80  
  
**Solução**

Conheça o processo em nosso canal How To no YouTube clicando nos links abaixo:

[How To | SIGACOM  -  Tipo de Compras (COMA200): Aprovador Padrão](https://www.youtube.com/watch?v=WiTxsyeqUKE)

[How To | SIGACOM  -  Tipo de Compras (COMA200): Aprovador Especial](https://www.youtube.com/watch?v=imQf541k9X8)

Na rotina Tipo de Compras (COMA200), existem os flags "Apv Especial" e "Aprov Padrão", seu objetivo é direcionar o PC/SC para os aprovadores através da amarração Tp.Compras x Aprovadores existente na rotina de Grupo de Aprovação. Para mais detalhes sobre essa amarração, [clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=506993520)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100685354)

Abaixo, detalho o funcionamento de cada um destes:

**Aprovação Padrão (Aprov Padrão):**

- Se algum produto do PC/SC entrar na regra do tipo de compras:

Esse produto deverá ser aprovado pelo **grupo padrão**, ou seja, será aprovado por todos demais aprovadores do grupo, exceto o aprovador que tenha amarração do tipo de compra no Grupo de Aprovação (Em outras palavras, esse aprovador será uma excessão).

**Exemplo:**

**Aprovadores (Grupo de aprovação):**

APROV 1: - (Contem amarração com a regra de tipo de compras / REGRA: CC = 01)

APROV 2:

APROV 3:

Neste caso, se o produto do PC/SC possuir centro de custo 01 (CC = 01), esse pedido será direcionado para os aprovadores 'APROV 2' e 'APROV 3' (Que são aprovadores padrões do grupo), ou seja, o aprovador 'APROV 1' não receberá essa demanda;

**Aprovação Especial (Apv Especial):**

- Se algum produto do PC/SC entrar na regra do tipo de compras:

Esse produto deverá ser aprovado **SOMENTE** pelo aprovador que contem a regra do tipo de compras (Apv Especial), NÃO cairá para aprovação dos demais aprovadores do grupo de aprovação.

**Exemplo:**

**Aprovadores (Grupo de aprovação):**

APROV 1: - (Contem amarração com a regra de tipo de compras / REGRA: CC = 01)

APROV 2:

APROV 3:

Neste caso, se o produto do PC/SC possuir centro de custo 01 (CC = 01), esse pedido será direcionado SOMENTE para o aprovador 'APROV 1', que possui uma regra especial para esse centro de custo definido no tipo de compras, ou seja, os demais aprovadores NÃO receberam essa demanda.

***Obs:***

Quando a regra não for aplicada na inclusão do PC/SC, a alçada é gerada para todos os aprovadores do grupo de forma normal.

***Saiba Mais :***

[MP - SIGACOM - Como configurar Controle de Alçadas utilizando Tipo de Compras ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020735492-MP-SIGACOM-Como-configurar-Controle-de-Al%C3%A7adas-utilizando-Tipo-de-Compras-)

[8 - Tipo de Compra](https://tdn.totvs.com/display/PROT/8+-+Tipo+de+Compra)

[PCOM09006 - Tipos de Compra (COMA200)](https://tdn.totvs.com/pages/viewpage.action?pageId=267795014)

[7 - Grupo de Aprovação](https://tdn.totvs.com/pages/viewpage.action?pageId=506993520)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
