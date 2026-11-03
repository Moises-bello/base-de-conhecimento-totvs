---
article_id: 360050718494
category: RH - Dissídio
content_hash: c30fea7f58d0899d04a452a104427057cf4bfb6b1a6d97b7f5a7f80280d5a3c8
fetched_at: '2026-06-28T22:43:43.501668+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de dissídio, geração da mensagem: "Não
  é possível recalcular pois o período selecionado já foi integrado à folha de pagamentos.
  Revise os parâmetros."
type: support-article
updated_at: '2021-04-30T00:09:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050718494-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-diss%C3%ADdio-gera%C3%A7%C3%A3o-da-mensagem-N%C3%A3o-%C3%A9-poss%C3%ADvel-recalcular-pois-o-per%C3%ADodo-selecionado-j%C3%A1-foi-integrado-%C3%A0-folha-de-pagamentos-Revise-os-par%C3%A2metros
---

**Ocorrência**Após confirmar os parâmetros de cálculo da rotina de dissídio retroativo o sistema retorna a seguinte mensagem: "Não é possível recalcular pois o período selecionado já foi integrado à folha de pagamentos. Revise os parâmetros."  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Causa**O sistema retorna essa mensagem ao encontrar os meses informados nos parâmetros de cálculo dentro da tabela RHH com a coluna RHH\_INTEGR igual a S.  
  
**Solução**1. Confirme a existência do cálculo na tabela RHH através da seleção do funcionário/ outras ações/ manutenção/ coluna Integração Folha;  
2. Se for necessário recalcular um período já integrado para folha de pagamento, realize a exclusão do dissídio: [MP - GPE - Exclusão do cálculo de dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037259774-MP-GPE-Exclus%C3%A3o-do-c%C3%A1lculo-de-diss%C3%ADdio-?source=search)**Saiba mais:** <https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio>
