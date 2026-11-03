---
article_id: 360061920094
category: Materiais - Compras (SIGACOM)
content_hash: 13c7047f5435fb8c56d71e8cf2e734f74ff464136e15e1bafcec9890732f9136
fetched_at: '2026-06-28T22:41:25.296010+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Rotina CTBANFE exibe
  HELPs quando existem campos vazios
type: support-article
updated_at: '2022-05-18T21:22:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061920094-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Rotina-CTBANFE-exibe-HELPs-quando-existem-campos-vazios
---

**Ocorrência**

No módulo Compras, ao tentar realizar contabilização de um Documento de Entrada (MATA103) com campos obrigatórios vazio ou incorreto (exemplo, Cta Debito / Credito), não ocorre o HELP informativo, passando a impressão que a rotina está travada.

**Ambiente**

Protheus – Compras – A partir da versão 12  
  
**Causa**Esse incidente ocorre devido a configuração do parâmetro **MV\_CT105MS** estar vazio ou **N** (Não).  
  
**Solução**Deve ajustar o valor do parârametro para **S** (Sim).

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
