---
article_id: 360059174994
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: f239311583222092d4fef5165d4bb7a1655155eb3ebda715c6df3a2bad0e46b1
fetched_at: '2026-06-28T22:38:31.153006+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-Ajuste de casas decimais e tamanho de campo para campos de percentual
  de comissão
type: support-article
updated_at: '2021-04-28T15:52:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059174994-MP-FAT-Ajuste-de-casas-decimais-e-tamanho-de-campo-para-campos-de-percentual-de-comiss%C3%A3o
---

**Dúvida**Ajuste de casas decimais e tamanho de campo para campos de percentual de comissão.  
  
**Ambiente**Microsiga Protheus - todas as versões.  
  
**Solução**

Quais os campos são relacionados a E3\_COMIS para que se possa ajustar o tamanho sem gerar conflitos no sistema?

Abaixo, segue a lista de campos relacionados a percentual de comissão do faturamento e financeiro que a principio é importante que tenham o mesmo tamanho, decimal e formato:  
  
**ada\_comis**(1 a 5)- comissão proveniente do contrato de parceria para o pedido de venda;  
**a1\_comis** - comissão proveniente do cadastro do cliente e gera a informação no campo **c5\_comis**;  
**a3\_comis** - comissão proveniente do cadastro do vendedor e gera a informação no campo **c5\_comis;**  
**b1\_comis** - comissão proveniente do produto e gera a informação no campo **c6\_comis**;  
**ck\_comis1**- comissão de produto proveniente do orçamento e gera a informação no campo **c6\_comis**;  
**c5\_comis**( 1 a 5)- comissão do vendedor no cabeçalho do pedido;  
**c6\_comis**(1 a 5) - comissão do produto na linha de item do pedido;  
**d2\_comis**(1 a 5)- comissão do produto proveniente da tabela **sc6** (itens do pedido de venda);  
**e1\_comis**(1 a 5)- percentual de comissão proveniente do pedido de venda (**MATA410**);  
**e3\_comis** - comissão gerada após a emissão da nota ou baixa do título.  
  
A alteração deve ser efetuada via configurador, base de dados, alterando a tabela correspondente, onde alterando o tamanho e decimal, o sistema automaticamente já ajusta o formato.  
  
**Obs: Não há grupo de campos para o ajuste automático desses campos, devendo alterar um a um.**

**Saiba mais sobre o assunto casas decimais:**

**[MP-FAT- Casas decimais no Faturamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115001427308-MP-FAT-Casas-decimais-no-Faturamento)**

**[MP - FAT - Limite de casas decimais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026073693-MP-FAT-Limite-de-casas-decimais)**
