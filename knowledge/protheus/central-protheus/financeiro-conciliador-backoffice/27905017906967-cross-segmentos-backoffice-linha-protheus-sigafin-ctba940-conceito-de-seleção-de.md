---
article_id: 27905017906967
category: Financeiro - Conciliador Backoffice
content_hash: 288ad8c52400cbedb16589d48ac1152c594635e598ca9079802c2da88bd97795
fetched_at: '2026-06-28T22:37:47.183095+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Conceito
  de seleção de filiais
type: support-article
updated_at: '2025-04-03T13:29:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27905017906967-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Conceito-de-sele%C3%A7%C3%A3o-de-filiais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27905017889943) Tempo aproximado para leitura: **00****:05:00 min** **Dúvida**Qual o conceito de seleção de filiais?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.2210  
  
**Solução**

Está tela a seguir apenas exibirá as filiais que o usuário tem permissão.

Na tabela exibida é possível marcar/desmarcar as filiais que serão utilizadas.

![smartclient_zkinup0jWj.gif](https://tdn.totvs.com/download/attachments/654959947/smartclient_zkinup0jWj.gif?version=1&modificationDate=1717444024327&api=v2)

**Importante**

O compartilhamento de tabelas de conciliação **(QLC - Cabeçalho de conciliação e QLD - Itens da conciliação)** devem ser iguais e compatíveis com a maneira em que se deseja trabalhar as conciliações.

Para conciliar e consultar conciliações de mais de uma **filial** por vez, as tabelas **QLC** e **QLD** deverão estar em **modo compartilhado,** caso as tabelas estejam em **modo exclusivo**, será apresentada apenas a filial logada.

Outro aspecto crucial é a necessidade de ajustar o compartilhamento antes de começar a usar a rotina, uma vez que as tabelas são alimentadas, não é recomendado modificar o compartilhamento, pois os campos relacionado a filial, QLC\_CODCON e QLD\_CODCON, perderão seu controle, perdendo integridade dos dados e podendo ocasionar erros não mensuráveis.

**Saiba mais**

[Selecão de filiais (Conciliador - SIGACTB)](https://tdn.totvs.com/pages/releaseview.action?pageId=654959947)

[How To | SIGAFIN - CTBA940 - Selecionar Filiais](https://www.youtube.com/watch?v=DkRBuoJ96TM)
