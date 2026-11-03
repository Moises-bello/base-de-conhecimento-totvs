---
article_id: 15532627655959
category: Call Center - Telecobrança
content_hash: 061b3ef1b7b2c68ea71040d73f9af84ac89da5657bcee9b46fbe3fba707b28b4
fetched_at: '2026-06-28T22:41:28.731003+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGATMK - Como apresentar
  títulos a vencer no Tele cobranças? (MV_TMKTLCT)
type: support-article
updated_at: '2023-06-26T16:58:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15532627655959-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Como-apresentar-t%C3%ADtulos-a-vencer-no-Tele-cobran%C3%A7as-MV-TMKTLCT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15532665726359) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como apresentar títulos a vencer no Tele cobranças? (MV\_TMKTLCT)

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGATMK - A partir da versão 11.  
  
**Solução**

Os títulos serão apresentados nas rotinas de atendimento do Call Center conforme o conteúdo do parâmetro MV\_TMKTLCT, onde existe a opção de configuração do tipo **Lógico** (.T.) ou (.F.):

* Se o parâmetro for definido com (**.F.**), serão apresentados todos os títulos em aberto do cliente, vencidos e a vencer, independentemente do tipo de atendimento (ativo ou receptivo).
* Se o conteúdo for definido como (**.T.**), os títulos serão apresentados conforme o tipo de atendimento. No caso do atendimento**Ativo** serão apresentados somente os títulos vencidos. Caso contrário, quando for **Receptivo** serão apresentados todos os títulos em aberto.

Os títulos apresentados serão diferenciados através dos seguintes status:

* Status vermelho: Títulos vencidos
* Status verde: Títulos a vencer.

OBS: A "**Seleção de Títulos**" (**TMKA180**) não é influenciada por esse parâmetro, sendo que independente da configuração lógica atribuída (.T.) ou (.F.) o processo de seleção de títulos da rotina não é alterado. A configuração do parâmetro só é aplicada para os atendimentos ativos ou receptivos.
