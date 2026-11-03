---
article_id: 360036878453
category: Escrita Fiscal - Impostos - ICMS
content_hash: 6d2a43ecb995190f0f9cb2c7675d454ed1fb93bce7d6d2c629f2e873d58dc0c2
fetched_at: '2026-06-28T22:39:26.020188+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Venda interestadual
  para consumidor final com CFOP 6107
type: support-article
updated_at: '2022-01-28T18:39:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036878453-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Venda-interestadual-para-consumidor-final-com-CFOP-6107
---

**Dúvida**

Cliente precisa realizar uma venda interestadual para consumidor final, TES esta saindo com CFOP 6101 e o correto seria sair com CFOP 6107.  
   
 **Ambiente**

Protheus – Fiscal – A partir da versão 11.80]  
  
**Solução**

Cliente não pode ter a inscrição estadual preenchida, tem que esta como ISENTO ou em branco, e não pode ser contribuinte, campo deve está em branco ou igual a não.

O sistema faz a conversão de CFOP de acordo com o MV\_ESTADO e UF destino.

Para CFOP 5101 converte 6101 se houver inscrição estadual  
Para CFOP 5101 converte 6107 se não houver inscrição estadual.

Para cada tipo de operação se faz necessário uma TES.

Industrialização - 5101  
Comercialização - 5102

Produtos importados é usado a mesma TES a conversão da alíquota faz de acordo com a origem do produto.
