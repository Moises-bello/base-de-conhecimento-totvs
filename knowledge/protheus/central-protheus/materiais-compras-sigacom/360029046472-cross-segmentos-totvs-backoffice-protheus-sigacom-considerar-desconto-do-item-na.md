---
article_id: 360029046472
category: Materiais - Compras (SIGACOM)
content_hash: a27f1238b975caf2246c104f809bada8f9e6520b945478760f39976aa20b9640
fetched_at: '2026-06-28T22:41:16.160270+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Considerar Desconto
  do Item na Tolerância de Recebimento - MV_DESCTOL
type: support-article
updated_at: '2022-05-16T21:27:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029046472-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Considerar-Desconto-do-Item-na-Toler%C3%A2ncia-de-Recebimento-MV-DESCTOL
---

**Dúvida**

Considerar Desconto do Item na Tolerância de Recebimento - MV\_DESCTOL

**Ambiente**

Protheus – Compras – A partir da versão 11.80  
  
**Solução**

Através do processo de bloqueio do Documento de Entrada (MATA103) foi criado parâmetro

MV\_DESCTOL - que indica se o desconto do item deve ser considera do no cálculo da tolerância de recebimento.

1. No Configurador (SIGACFG) acesse para configuração:

Ambientes / Cadastros / Parâmetros (CFGX017):

![mv_desctol.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360030597412/mv_desctol.PNG)

1. No módulo de Compras acesse sequencialmente as seguintes opções de Menu:

2. Atualizações / Adm. Compras / Tolerância Recebto (COMA020). Clique em Incluir para realizar o cadastro de tolerância de recebimento.

3. Atualizações / Pedidos / Pedidos de Compra (MATA120) para incluir um Pedido de Compras.

4. Atualizações / Movimentos / Documento de Entrada (MATA103) para incluir um documento de entrada vinculado ao Pedido de Compras.

5. Se o parâmetro MV\_DESCTOL estiver com o valor igual a .T., o documento de entrada será bloqueado somente se o valor do item, menos seu desconto, ultrapassar a porcentagem estabelecida no cadastro da tolerância de recebimento

***Saiba Mais :***

[MP - SIGACOM - Como utilizar a Tolerância de Recebimento no módulo de Compras ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006558892)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
