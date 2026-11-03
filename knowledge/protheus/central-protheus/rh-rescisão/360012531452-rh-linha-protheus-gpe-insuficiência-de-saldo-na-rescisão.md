---
article_id: 360012531452
category: RH - Rescisão
content_hash: 429d71cc59e076f97a4c0e0b8c7d485634a6de24e1f03f837791646eb9b78172
fetched_at: '2026-06-28T22:43:52.205791+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Insuficiência de Saldo na rescisão
type: support-article
updated_at: '2025-06-16T17:55:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012531452-RH-Linha-Protheus-GPE-Insufici%C3%AAncia-de-Saldo-na-rescis%C3%A3o
---

**Dúvida**Por que é gerado Insuficiência de Saldo na rescisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Desenvolvida melhoria para que na rescisão, quando o líquido for negativo, ou seja, existir mais descontos do que os proventos, é gerado uma verba de insuficiência de saldo com identificador 0045, essa verba é gerada no intuito da empresa contabilizar (integrar para contabilidade) a perda desse valor, deixando transparente o prejuízo com a rescisão contratual em questão.  
  
**Observação**: Para conferencia, filtre todas as verbas geradas na rescisão via Consulta Genérica, a tabela SRV e some todos os proventos - todos os descontos. Caso alguma verba esteja com o tipo incorreto ou esteja com o campo 'pagamento obrigatório' igual a 'sim' terá influência no resultado, pois as verbas de pagamento obrigatório não são consideradas nos proventos - descontos.
