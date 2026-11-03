---
article_id: 15537475392791
category: Folha Mensal
content_hash: a7e70c349a5a3f1eae53890ba3f9524b35f0f9daa7f2576de95601b331926081
fetched_at: '2026-06-28T22:46:58.193817+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Diferença de Vale Transporte
type: support-article
updated_at: '2024-09-16T18:31:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15537475392791-RH-RM-FOP-Diferen%C3%A7a-de-Vale-Transporte
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15537459579671) Tempo aproximado para leitura: **00:03:20 min****Ocorrência**Ao realizar a rotina de diferença salarial, ao analisar o log de cálculo, o evento de diferença de vale transporte aparece como evento desconsiderado.  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**O evento com **código de cálculo 6**não entra para o cálculo na diferença. Pelo seguinte motivo:  
  
O sistema não grava o valor creditado para o funcionário no vale transporte, por exemplo:  
  
**-**Salário do Funcionário: R$ 3.000,00  
**-** Valor do desconto de vale transporte (Código de cálculo 6): R$ 180,00 que é 3000 X 6%  
**-** Valor de vale transporte comprado para esse funcionário no mês: R$ 150,00  
  
Dessa forma, o valor descontado seria maior que valor creditado, ou seja, maior que o valor comprado de vale transporte, assim o desconto deixa de ser R$ 180,00 e passar a ser R$ 150,00.  
  
Quando se tem aumento salarial, e assim gerado uma diferença salarial, o sistema não recalcula o valor do vale transporte, justamente por não saber se valor a ser descontado na diferença irá ultrapassar o valor creditado, no caso o valor da compra de vale transporte.  
  
**Solução**  
Para solucionar essa ocorrência, caso tenha que realizar essa diferença, a mesma só pode ser realizada por fórmula, pois o código de cálculo irá bloquear o recalculo para que impeça uma possibilidade do funcionário ser levado no desconto.
