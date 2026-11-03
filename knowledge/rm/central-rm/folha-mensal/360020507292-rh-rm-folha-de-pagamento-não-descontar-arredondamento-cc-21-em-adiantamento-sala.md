---
article_id: 360020507292
category: Folha Mensal
content_hash: 796756f2a73feaeb9fd4c8e12827d52400dcde58f667907176185af0f313ac79
fetched_at: '2026-06-28T22:46:59.550700+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - Folha de pagamento - Não descontar arredondamento (CC 21) em adiantamento
  salarial (CC 34)
type: support-article
updated_at: '2024-10-18T15:51:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020507292-RH-RM-Folha-de-pagamento-N%C3%A3o-descontar-arredondamento-CC-21-em-adiantamento-salarial-CC-34
---

**Dúvida**Existe parametrizações para que não ocorra desconto de insuficiência de saldo de competências anteriores no período de pagamento de adiantamento?    
   
 **Ambiente**RM – Folha de pagamento – A partir da versão 12.1.18  
   
**Solução**  
Por padrão o sistema irá lançar o valor do evento com o código de cálculo 20 na movimentação posterior caso o funcionário tenha o líquido positivo, não validado nenhum código de cálculo para este processo.

Para que o sistema não realize o lançamento do desconto de insuficiência de saldo no adiantamento, será necessária a criação e vínculo de fórmulas nos eventos com código de cálculo 20 e 21.
