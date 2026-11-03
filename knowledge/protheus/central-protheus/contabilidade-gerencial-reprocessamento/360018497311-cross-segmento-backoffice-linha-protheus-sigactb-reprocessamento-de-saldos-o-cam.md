---
article_id: 360018497311
category: Contabilidade Gerencial - Reprocessamento
content_hash: c1b08905267d82373981bc7d8fd4df8a6b9c89b28ac39faab06bc6677879e6d9
fetched_at: '2026-06-28T22:40:41.996383+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Reprocessamento de saldos
  o  Campo Filial das tabelas CQ não estão sendo alimentadas
type: support-article
updated_at: '2025-08-08T14:40:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018497311-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Reprocessamento-de-saldos-o-Campo-Filial-das-tabelas-CQ-n%C3%A3o-est%C3%A3o-sendo-alimentadas
---

**Ocorrência**

* Tabelas de saldo (CQ) e movimento(CT2) Exclusivas
* Ao realizar o reprocessamento de saldo as Tabelas CQ não são alimentada
* Campo Filial das tabelas CQ não são alimentadas
* CQ1\_FILIAL,CQ2\_FILIAL, CQ3\_FILIAL,CQ4\_FILIAL ,CQ5\_FILIAL,CQ6\_FILIAL, CQ7\_FILIAL ,CQ8\_FILIAL , CQ9\_FILIAL, CQA\_FILIAL
* Saldo não é atualizado no relatório balancete

**Ambiente**  
Protheus – Contabilidade gerencial – A partir da versão P12

**Solução**

Necessário realizar o procedimento abaixo:

* [MP - SIGACTB - Compartilhamento de Tabelas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007377851-MP-SIGACTB-Compartilhamento-de-Tabelas-)
* [MP - SIGACTB - Reprocessamento não atualiza saldos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006689012-MP-SIGACTB-Reprocessamento-n%C3%A3o-atualiza-saldos?source=search)
* [MP - SIGACTB/SIGAATF - Instalação de Procedure](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009382821-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-instalar-as-Stored-Procedures?source=search)
* [MP - SIGACTB - Saldo anterior zerado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115016115388-MP-SIGACTB-Saldo-anterior-zerado)
* [MP - SIGACTB - Saldos não estão sendo atualizados de forma online.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019534772-MP-SIGACTB-Saldos-n%C3%A3o-est%C3%A3o-sendo-atualizados-de-forma-online-?source=search)
* [MP - SIGACTB - CTBA 190 Como realizar o reprocessamento de saldos no SIGACTB?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007452371-MP-SIGACTB-CTBA-190-Como-realizar-o-reprocessamento-de-saldos-no-SIGACTB-?source=search) .

Obs: é imprescindível a realização de todos os procedimento descritos nos link anteriores

* Ao realize o reprocessamento de saldo Informe da filial logada
* Reprocessamento deve ser feito do primeiro lançamento existente na tabela CT2 até a data atual

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013813211)

* Verifique se os campos [X2\_AUTREC](https://tdn.totvs.com/pages/releaseview.action?pageId=271180179), X2\_TAMFIL, X2\_TAMUN, X2\_TAMEMP , das tabelas CT2, CTC, CTF, CQO,CQ1...CQ9 e CQA estão com o tamanho correto em comparação ao seu sigmat
* Exemplo:

   
   
![](https://totvssuporte.zendesk.com/attachments/token/Qq3AIenfEl8nm8sZFld18yR2n/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/PZFEXcoibAbPZtT4AiNU69Hda/?name=image.png)

Caso detecte problema nos campo da X2 , solicito que abra um ticket junto ao time de Framework , pois houve tratamento na Issue DFRM4-9613.

Veja também :

[MP - SIGACTB - Saldos não estão sendo atualizados de forma online.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019534772-MP-SIGACTB-Saldos-n%C3%A3o-est%C3%A3o-sendo-atualizados-de-forma-online-?source=search)

* [MP - SIGACTB - CTBA190 Saldos não são atualizados com Stored Procedure](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021997171-MP-SIGACTB-CTBA190-Saldos-n%C3%A3o-s%C3%A3o-atualizados-com-Stored-Procedure?source=search)
