---
article_id: 360018057152
category: Contabilidade Gerencial - Reprocessamento
content_hash: 74b97dbfef2221f70ad050deb0ad655d3d846d281934320bb4cc731d25cc8c1b
fetched_at: '2026-06-28T22:40:41.899941+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA190 - Período do
  calendário encerrado/bloqueado
type: support-article
updated_at: '2021-08-30T14:33:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018057152-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA190-Per%C3%ADodo-do-calend%C3%A1rio-encerrado-bloqueado
---

**Ocorrência**

Precisamos gerar as tabelas CQs (tabelas de saldos) da contabilidade, para isso é necessário efetuar o Reprocessamento de Saldos Contábil (CTBA190), porém é apresentado a seguinte mensagem:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013570032/mceclip0.png)

**Ambiente**Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 11.80

**Causa**  
A mensagem em questão é demonstrada devido ao **bloqueio** feito através do parâmetro **MV\_CTGBLOQ**, o mesmo foi criado para que o **reprocessamento**(CTBA190) não seja executado caso um ou mais períodos do calendário encontra-se como **Encerrado ou Bloqueado** na data definida na rotina **CTBA190**, verifique a definição deste parâmetro:

|  |  |
| --- | --- |
| **MV\_CTGBLOQ** | Parâmetro que indica quais Status do Calendário serão considerados para o bloqueio do Reprocessamento. Se estiver em branco, nenhum Bloqueio de calendário será considerado. Se quiser bloquear o Status 2 e 3, informe “23” no conteúdo. |

**Saiba mais:**

**[CTBA190- Como realizar o reprocessamento de saldos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007452371-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA190-Como-realizar-o-reprocessamento-de-saldos-no-SIGACTB)**

**[CTBA190- Erro na chamada do processo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115016125428-MP-SIGACTB-CTBA190-Reprocessamento-de-Saldos-Erro-na-Chamado-do-Processo)**
