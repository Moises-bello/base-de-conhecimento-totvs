---
article_id: 4409709183383
category: esocial - Periódicos
content_hash: bbea4fcee0ab645b5b6b93c7a9d32e10e3517d8c945fcb84ab0f85f335f8a75e
fetched_at: '2026-06-28T22:47:09.235431+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Diferença entre o evento S-1200 e S-1210
type: support-article
updated_at: '2024-06-27T18:26:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409709183383-RH-RM-FOP-eSocial-Diferen%C3%A7a-entre-o-evento-S-1200-e-S-1210
---

**Dúvida**Qual a diferença entre o evento **S-1200** e **S-1210?****Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**Tanto os eventos S-1200 quanto S-1210 tem suas informações montadas a partir dos valores lançados no envelope de pagamento (ficha financeira/PFFINANC).

**S-1200** – **Remuneração de trabalhador vinculado ao Regime Geral de Previdência Social**São as informações da remuneração de cada trabalhador conforme mês de apuração (Competência).  
O sistema irá buscar os valores lançados do envelope de pagamento (ficha financeira/PFFINANC) conforme incidência dos eventos. Para assistência de saúde dos dependentes, irá buscar os valores do histórico de assistência saúde do dependente.

**S-1210 – Pagamentos de Rendimentos do Trabalho**São as informações prestadas relativas aos pagamentos dos rendimentos do trabalho (Imposto sobre a Renda Retido na Fonte – IRRF) verificando data de pagamento do evento e mês de apuração (Caixa).  
O sistema irá buscar os valores lançados no envelope de pagamento (ficha financeira/PFFINANC), recibo de férias e autônomos do Fluxus (será calculado através do total do lançamento financeiro menos o total de INSS e IRRF).

**Atenção**Quando a empresa utiliza Tomador de Serviço, serão considerados os valores da distribuição do [SEFIP](https://tdn.totvs.com/display/LRM/Distribuir+SEFIP) (PFMOVTOMADOR).  
  
**Importante:**  
Em casos de rescisão, as verbas rescisórias são lançadas no S-2299. Os valores referente a IRRF de verbas rescisórias são lançados no S-1210. Já os valores referentes as férias (afastamento temporário S-2230) são retornados do recibo de férias.
