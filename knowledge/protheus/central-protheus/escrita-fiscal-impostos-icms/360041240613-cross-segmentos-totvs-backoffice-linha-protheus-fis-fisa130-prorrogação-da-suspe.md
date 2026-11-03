---
article_id: 360041240613
category: Escrita Fiscal - Impostos - ICMS
content_hash: c7be94a65a689037c372fa65386e01230df1a7d70ca443162995ccb3fe45835b
fetched_at: '2026-06-28T22:39:25.859773+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- FISA130 - Prorrogação
  da Suspensão do ICMS
type: support-article
updated_at: '2021-07-28T14:10:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041240613-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA130-Prorroga%C3%A7%C3%A3o-da-Suspens%C3%A3o-do-ICMS
---

**Dúvida**  
Foi identificado um documento de saída que não está sendo apresentado na rotina FISA130 - Prorrogação da Suspensão do ICMS.

**Ambiente**  
Protheus – Livros Fiscias – A partir da versão 11.80  
  
**Solução**  
Primeiramente, será necessário avaliar se o modelo do documento fiscal é igual a (SPED), campo Poder de Terceiros (F4\_PODER3) no cadastro de TES esta igual a R - Remessa e se foi gerado informações na tabela SB6 (Saldo em Poder de Terceiros).

Em seguida, verifique se foi efetuada alguma alteração no cadastro de TES, se sim, verificar com o departamento fiscal se esta nota pode ser reprocessada e seguir com o procedimento. 

Se por algum motivo, o reprocessamento não surtir efeito positivo, será necessário refazer a rotina de reprocessamento de saldo (MATA216) para que a tabela SB6 seja alimentada corretamente e consequentemente gerar informações na rotina FISA130.
