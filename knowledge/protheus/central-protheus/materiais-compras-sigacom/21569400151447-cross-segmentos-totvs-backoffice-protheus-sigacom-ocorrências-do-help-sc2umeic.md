---
article_id: 21569400151447
category: Materiais - Compras (SIGACOM)
content_hash: 4270dd6820e2d13cf62b54f5f3e9c5fd28ce976ce1d0ec7d57a3b126a101eca7
fetched_at: '2026-06-28T22:41:22.026392+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Protheus - SIGACOM - Ocorrências do help
  SC2UMEIC.
type: support-article
updated_at: '2024-02-23T17:30:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21569400151447-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGACOM-Ocorr%C3%AAncias-do-help-SC2UMEIC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21569392798999) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao incluir uma solicitação de compras, o sistema gera o help SC2UMEIC

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21569400131351)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - a partir da 12.1.33  
  
**Causa**Quando o parâmetro MV\_EASY (responsável por fazer integração com o módulo SIGAEIC) está habilitado, o sistema verifica se houve o preenchimento no campo C1\_SEGUM e do campo C1\_QTSEGUM. Pois se um deles foi preenchido o outro também deverá ser preenchido. O sistema traz essas informações do cadastro de produto.  
  
**Solução**

1. Validar se os campos C1\_SEGUM e C1\_QTSEGUM estão marcados como "Usado" no configurador.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21569392803351)
2. Valide se o cadastro do produto está com as informações referentes a segunda unidade coerentes.![](https://centraldeatendimento.totvs.com/hc/article_attachments/21569392804503)
3. Verifique se após preencher o código do produto e digitar a quantidade no campo C1\_QUANT o sistema preenche os campos C1\_SEGUM e C1\_QTSEGUM automaticamente.

***Saiba Mais:***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)  
[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-BR/sections/1500001537201-Materiais-Compras-SIGACOM-)
