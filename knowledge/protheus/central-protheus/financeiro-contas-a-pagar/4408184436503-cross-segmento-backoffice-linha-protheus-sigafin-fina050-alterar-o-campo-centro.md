---
article_id: 4408184436503
category: Financeiro - Contas a Pagar
content_hash: c2d8268005c809c8a4e2aab3a8677b78138afa4ad2eec2a6da17c2044cd05242
fetched_at: '2026-06-28T22:38:07.283988+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA050 - Alterar o
  campo centro de custo de uma parcela de desdobramento quando houve rateio
type: support-article
updated_at: '2022-09-23T21:39:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408184436503-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Alterar-o-campo-centro-de-custo-de-uma-parcela-de-desdobramento-quando-houve-rateio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**É possível alterar o campo centro de custo de uma parcela de desdobramento quando houve rateio?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões  
  
**Solução**Não é possível realizar a alteração do centro de custo de uma parcela do desdobramento no qual houve rateio de CC, neste caso é necessário cancelar o desdobramento e inclui-lo novamente com a alteração ou utilizar o ponto de entrada **F050MCP**para permitir a alteração do campo **E2\_CCUSTO**das parcelas já criadas. 

**F050MCP -**Permite incluir novos campos na opção **Alterar** da rotina **FINA050**.  
Documentação:<http://tdn.totvs.com/display/PROT/DT_F050MCP_Adiciona_campos_na_alteracao_do_Contas_a_pagar>

Saiba mais:   
**[MP - SIGAFIN - FINA050 - Cancelamento de Desdobramento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018602371-MP-SIGAFIN-FINA050-Cancelamento-de-Desdobramento)**
