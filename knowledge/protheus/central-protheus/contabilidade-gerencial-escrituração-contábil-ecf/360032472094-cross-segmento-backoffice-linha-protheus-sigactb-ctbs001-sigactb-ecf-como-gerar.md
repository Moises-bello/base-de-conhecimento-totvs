---
article_id: 360032472094
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: f046dc94a0e8c1ce21860e048e232cae5c3877c139714474e79f3493df1c20c4
fetched_at: '2026-06-28T22:40:48.856033+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 - SIGACTB- ECF
  Como gerar o registro Y540
type: support-article
updated_at: '2025-04-25T11:39:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360032472094-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-SIGACTB-ECF-Como-gerar-o-registro-Y540
---

**Dúvida**Como gerar o registro Y540  
  
**Ambiente**

Cross Segmento - Backoffice Linha Protheus - – Contabilidade Gerencial – A partir da versão 11.80  
  
**Solução**

O registro y540 é gerado a partir da SD2.  
  
![](https://totvssuporte.zendesk.com/attachments/token/0HlmtigjeW9t8D2KzindYNMqK/?name=inline1637359327.png)​  
<http://tdn.totvs.com/pages/releaseview.action?pageId=243650896>

**[Registro Y540 - Discriminação da Receita de Vendas dos Estabelecimentos por Atividade Econômica](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512#Obriga%C3%A7%C3%A3oECFEscritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoY-Informa%C3%A7%C3%B5esGerais)**

* Tabelas - CGH (Receita de Vendas Estab. Ativi) / CZS (CNAE-Fisca)
* Registro do Layout TOTVS - T105
* Rotina - TAFA341 (Receita de Vendas dos Estab. por Atividade Economica

* Necessário gerar a ECF com base no regime tributário de  empresa
  + [Como gerar o Regime tributário Lucro Real /Apuração anual?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004875431-MP-SIGACTB-ECF-Como-gerar-o-Regime-tribut%C3%A1rio-Lucro-Real-Apura%C3%A7%C3%A3o-anual-?source=search)
  + [Como realizar a exportação no Regime tributário Lucro Real com Apuração trimestral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006950711-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Real-com-Apura%C3%A7%C3%A3o-trimestral-?source=search)
  + [Como realizar a exportação no Regime tributário Lucro Presumido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004838052-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Presumido?source=search)
  + [IMUNE OU ISENTA COMO GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047581974-MP-SIGACTB-ECF-IMUNE-OU-ISENTA-COMO-GERAR?source=search)

* Na wizard da ECF (rotina CTBS001)  o sistema irá apresentar

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043123373)

![](https://totvssuporte.zendesk.com/attachments/token/OhSsV6EIkY56k19XifTvkx8ox/?name=inline832906092.png)​

* Tabela SD2, exporta todos os registros do período selecionado na revisão da ECF:

![](https://totvssuporte.zendesk.com/attachments/token/Gtl17w7Bd5LDroK5gxrf7D2r2/?name=inline1168380191.png)​

* O CNAE é preenchido conforme cadastro no SIGAMAT:

![](https://totvssuporte.zendesk.com/attachments/token/LFIUsVqL7kqbCeU8MpZ81zq5t/?name=inline-696663630.png)​

* Integração TAFTICKET :

![](https://totvssuporte.zendesk.com/attachments/token/eI0kWYzeNcyDP4LIjTWFDggc4/?name=inline798121289.png)​

Rotina TAFA341

![](https://totvssuporte.zendesk.com/attachments/token/H7sLSZXiYY1uGtQJxUgHdMgtR/?name=inline47592162.png)

Apartir do Leiaute 7 , registro Y540  foi excluido pela receita 

Com isso a pergunta fica inativa

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24657098725015)

Vendas a Comercial Exportadora com Fim Específico de Exportação

<http://sped.rfb.gov.br/estatico/2E/B756440254D95A88E90837EF8166BFF4968846/Manual_de_Orienta%c3%a7%c3%a3o_da_ECF_Dezembro_2020.pdf>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24657098740247)

<https://tdn.totvs.com/pages/releaseview.action?pageId=599877579>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24657084344855)

​

[MP - SIGACTB - ECF - Como realizar a geração dos blocos X e Y?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006827952-MP-SIGACTB-ECF-Como-realizar-a-gera%C3%A7%C3%A3o-dos-blocos-X-e-Y-?source=search)
