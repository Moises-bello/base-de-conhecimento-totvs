---
article_id: 360025899434
category: Financeiro - Contas a Receber
content_hash: 7f2133eee2e4b85e7b43efe6086f4ba56d0528d40e68e8e59f5b0c061474d49c
fetched_at: '2026-06-28T22:38:15.036051+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: 'MP - SIGAFIN - FINA070 - HELP FA070MOTINV na baixa '
type: support-article
updated_at: '2021-04-28T15:17:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025899434-MP-SIGAFIN-FINA070-HELP-FA070MOTINV-na-baixa
---

**Ocorrência**No módulo Financeiro, ao acessar a rotina de baixa apresenta a mensagem Help: FA070MOTINV Motivo da Baixa inválido para este título, pois o mesmo se encontra em Banco. Para efetuar uma Devolução, transfira o título para o caixa e então faça a Devolução**![FINA070.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360041286973/FINA070.PNG)**

**Ambiente**Microsiga Protheus - Financeiro - FINA070 - A partir da versão 12

**Causa**O título está vinculado a algum banco (portador definido) e na tentativa de baixar o título com motivo de baixa que  "NÃO" utiliza banco o sistema está buscando retornar que não é possível utilizar este motivo.

**Solução**A solução seria baixar por motivo **DAÇÃO**, ou baixar com motivo diferente de **NORMAL**, ou ainda na rotina transferência **FINA060**, em transferência, mude o tipo de carteira para F ou G.  
Para evitar problemas futuros atualize seu sistema de Help, pressione F1 e siga o manual de atualização do mesmo no sistema.
