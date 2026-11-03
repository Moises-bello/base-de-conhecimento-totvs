---
article_id: 360025465372
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: db92e3b13ddee269f4e3979cfb1a501a72d16bbdde6e9044aa8e451f714274d0
fetched_at: '2026-06-28T22:37:19.722673+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT  - Ao realizar o desconto
  na medição os campos de % de Desconto do Contrato (CNE_PDESC) e Valor de desconto
  do Contrato (CNE_VLDESC) ficam bloqueados para preenchimento em contratos Fixo e
  Semi-Fixo.
type: support-article
updated_at: '2025-05-16T18:44:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025465372-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Ao-realizar-o-desconto-na-medi%C3%A7%C3%A3o-os-campos-de-de-Desconto-do-Contrato-CNE-PDESC-e-Valor-de-desconto-do-Contrato-CNE-VLDESC-ficam-bloqueados-para-preenchimento-em-contratos-Fixo-e-Semi-Fixo
---

**Dúvida** Ao realizar o desconto na medição os campos de % de Desconto do Contrato (CNE\_PDESC) e Valor de desconto do Contrato (CNE\_VLDESC) ficam bloqueados para preenchimento.

**Ambiente**Microsiga Protheus – Gestão de Contratos– A partir da versão 11.8  
  
**Solução**

No gestão de Contratos, os campos de **%**de Desconto do Contrato**(CNE\_PDESC)**e Valor de desconto do Contrato**(CNE\_VLDESC)**ficam bloqueados para preenchimento para contratos do tipo **Fixo** e **Semi-fixo por produto.**

Caso seja necessário aplicar um desconto no momento da medição, na rotina Nova Medição (CNTA121) é necessário utilizar a Aba **"Descontos".**

Nova Medição (CNTA121):

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099394294)

Cadastre um tipo de Desconto e caso queira que o desconto seja aplicado no Pedido preencha o campo  **Interf. Ped = Sim**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32075821523351)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32075829772439)

No campo Valor na Aba descontos aplique o Valor do desconto.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32075821529623)

**Obs1**: O valor aplicado será aplicado no valor Total na soma de todos os itens da Medição.

**Obs2:** Os campos **%**de Desconto do Contrato**(CNE\_PDESC)**e Valor de desconto do Contrato **(CNE\_VLDESC)** foram bloqueados para preenchimento para contratos do tipo **Fixo** e **Semi-fixo por produto** devido inconsistência no sistema, de  acordo com a documentação  [DT Inconsistência no processo de desconto da medição](https://tdn.totvs.com/pages/releaseview.action?pageId=729236468)

***Saiba Mais:***

[DT Inconsistência no processo de desconto da medição](https://tdn.totvs.com/pages/releaseview.action?pageId=729236468)

[GCT0034\_Como\_configurar\_o\_tipo\_de\_desconto\_na\_medição?](https://tdn.totvs.com/pages/releaseview.action?pageId=239037294)

[Pontos de entrada rotinas de medição](https://tdn.totvs.com/pages/releaseview.action?pageId=274840426)

[GCT0117 - Processo de desconto](http://tdn.totvs.com/display/PROT/GCT0117+-+Processo+de+desconto)

[MP - SIGAGCT - Como são considerados os descontos no financeiro em títulos gerados pelo encerramento da medição ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025642971-MP-SIGAGCT-Como-s%C3%A3o-considerados-os-descontos-no-financeiro-em-t%C3%ADtulos-gerados-pelo-encerramento-da-medi%C3%A7%C3%A3o)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
