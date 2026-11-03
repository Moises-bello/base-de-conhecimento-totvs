---
article_id: 7145000680727
category: Financeiro - Contas a Pagar
content_hash: 7191db5f4e42932cd7305f20175264f2a93ee41a0338df3043de74aa44457ed9
fetched_at: '2026-06-28T22:38:07.136163+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINR855 - Não aparece
  imposto com retenção na Baixa
type: support-article
updated_at: '2025-06-18T11:42:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7145000680727-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINR855-N%C3%A3o-aparece-imposto-com-reten%C3%A7%C3%A3o-na-Baixa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32892109001495) Tempo aproximado para leitura: **00:05 min** **Dúvida**Não apresenta imposto com retenção na Baixa com o conteúdo do parâmetro (MV\_BX10925 = 1)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

O imposto está configurado para ser retido no momento da baixa, conforme o parâmetro **MV\_BX10925 = 1**. Dessa forma, os impostos foram apenas calculados (provisionados), mas ainda não foram efetivamente retidos, ou seja, não houve a geração dos títulos do tipo TX. Por esse motivo, eles não serão exibidos no relatório **FINR855 - Relação - Título Principal x Impostos**, que contempla apenas os impostos já retidos (gerados pelo título TX).

Após a realização da baixa e consequente geração dos títulos TX, todos os impostos passarão a ser apresentados normalmente no relatório.

Como alternativa, recomenda-se a utilização do relatório **FINR865 - Relação de Títulos a Pagar com Retenção de Impostos**, que contempla os impostos provisionados e retidos.
