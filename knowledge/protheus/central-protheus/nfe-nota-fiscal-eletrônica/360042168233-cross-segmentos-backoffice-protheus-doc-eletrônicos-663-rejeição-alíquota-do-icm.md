---
article_id: 360042168233
category: NFe - Nota Fiscal Eletrônica
content_hash: 085f71999dcaefd60a2bea9f30bc2878b98a8a5270de92e2a347f51bfd96b6ea
fetched_at: '2026-06-28T22:40:05.226210+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 663 Rejeição :
  Alíquota do ICMS com valor superior a 4 por cento na operação de saída interestadual
  com produtos importados'
type: support-article
updated_at: '2025-07-09T12:27:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042168233-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-663-Rejei%C3%A7%C3%A3o-Al%C3%ADquota-do-ICMS-com-valor-superior-a-4-por-cento-na-opera%C3%A7%C3%A3o-de-sa%C3%ADda-interestadual-com-produtos-importados
---

**Dúvida**Como solucionar a rejeição abaixo ?

663 Rejeição : Alíquota do ICMS com valor superior a 4 por cento na operação de saída interestadual com produtos importados   
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe -Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A Sefaz verifica alíquota do ICMS da nota conteúdo da TAG ***<pICMS> de acordo com as validações abaixo:***

​

Se a nota for de operação fora do Estado **Interestadual e de Saída,** **origem da nota for 1, 2, 3 ou** **situação tributária da nota for 00, 10, 20, 70 ou 90.** Alíquota do ICMS não pode ser **superior a 4 por cento.**

1- Preencher o campo  **Origem** **B1\_ORIGEM no cadastro de produto :**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33347776323607)

2- Caso a situação tributária não seja  00, 10, 20, 70 ou 90 altere no **TES** no campo **Sit. trib. ICMS** **F4\_SITTRIB.**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33347776326551)

3- Preencher o CFOP no TES da nota no campo **Cod. Fiscal "F4\_CF":** Há **Exceção 2**: A regra de validação acima não se aplica para as operações com CFOP de Retorno de Mercadorias ou Anulação de Valor **(Anexos XIII.04 e XIII.05).**  CFOPS constam no link abaixo na página 22:  
  
[Nota Técnica 2015.003 - v 1.94](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=DRiCiO978HY=)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33347776327703)

4- Se correto a **origem do Produto, CFOP e situação tributária** será necessário ajustar no sistema alíquota.

**Saiba mais:**

**Exceção 3:**A regra de validação acima não se aplica na venda de veículos novos (grupo “veicProd”) se existir ao menos um item de Venda direta para grandes consumidores (tpOp=3), ou de Faturamento direto para consumidor final (tpOp=2).

Para essa exceção há documentação **do link abaixo:**

[MP - NFE - Como gerar Detalhamento Específico de Veículos novos no XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026946731)

1- Verifique se está correto o campo C6\_CLASFIS "**Sit. trib"** este campo deve estar como **exemplo 000**, O primeiro número é referente a **origem do produto e os outros dois referente a situação tributária do ICMS.**  
  
  
2- Exclua essa nota no pedido de **vendas ou compra digite novamente o TES** e verifique se irá atualizar o campo Sit. trib. com **exemplo 000** conforme abaixo:  
  
  
​![C6_CLASFIS.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019579902)  
  
  
3- Se não estiver atualizando é possível **alterar manualmente.**

4- Após isso, gere o **documento e transmita.**
