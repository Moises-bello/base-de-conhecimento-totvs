---
article_id: 4407434868247
category: TAF - eSocial - Relatório
content_hash: 1dd59d4466875cb2f57044f3bd894908e438301c317b173192eeeeb6d514c6b5
fetched_at: '2026-06-28T22:45:19.959854+00:00'
product: protheus
section_id: 1500001536821
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial  - Totalizador-  S-5002 - Totalizador -
  Valor zerado IRRF (S-1210) Retorno Totalizador
type: support-article
updated_at: '2024-06-17T16:45:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407434868247-RH-Linha-Protheus-TAF-eSocial-Totalizador-S-5002-Totalizador-Valor-zerado-IRRF-S-1210-Retorno-Totalizador
---

**Dúvida**Valor zerado ao consultar o IR do evento S-5002  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial- Totalizador- S-5002 - Remuneração de trabalhador vinculado ao Regime Geral de Previdência Social (TAFA250)- Todas as versões  
  
**Solução**1 - Ao consultar o evento S-5002 no retorno do Totalizador do IR, o valor está zerado. Extraia o XML RET para validar se existe o retorno do evento S-5002, se o mesmo encontra-se no arquivo .xml. Caso não esteja,  deverá validar se o evento S-1210 foi enviado com as informações necessárias para que o governo retorne com o totalizador no sistema.

[RH - Linha Protheus - TAF - eSocial - Configuração - Como gerar XML de retorno dos eventos no TAF, e o XML do TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046869313)

2 - Caso o XML RET esteja com o valor no arquivo, verifique se o TAF está atualizado com as últimas atualizações:

[RH - Linha Protheus - TAF - ATUALIZAÇÃO - Como atualizar o TAF E-social (Expedição Contínua)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18972648169239)

3 - Se estiver dentro dos requisitos, sugerimos que abra um chamado no suporte da TOTVS para validação da ocorrência.

4. Documentações relacionadas:

[RH - Linha Protheus - TAF - eSocial - Totalizadores - Como acessar as rotinas de Totalizadores no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412246151319)
