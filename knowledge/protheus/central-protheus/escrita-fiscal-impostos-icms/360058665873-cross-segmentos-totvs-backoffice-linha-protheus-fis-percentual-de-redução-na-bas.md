---
article_id: 360058665873
category: Escrita Fiscal - Impostos - ICMS
content_hash: da4f0b25a683637a3686e5d7c46a1b0bfb55d44525ff9b32e86a8d0a961bab84
fetched_at: '2026-06-28T22:39:25.987507+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Percentual de redução
  na base de cálculo conforme decreto RICMS-MG nº 43.080/2002
type: support-article
updated_at: '2021-07-28T17:17:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058665873-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Percentual-de-redu%C3%A7%C3%A3o-na-base-de-c%C3%A1lculo-conforme-decreto-RICMS-MG-n%C2%BA-43-080-2002
---

**Dúvida**

Como Configurar o Percentual de redução na base de cálculo conforme decreto RICMS-MG nº 43.080/2002 ?  
  
**Ambiente**

Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Para atender a Redução da base do ICMS, conforme Decreto nº 43.080/2002 RICMS-MG.O sistema irá utilizar os campos criados para receber o percentual de redução da base de cálculo do ICMS, o valor do ICMS sem débito de imposto e o valor do desconto, para o cálculo do valor da nota fiscal.

Configurar o campo: B1\_PR43080 com a % necessária.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096371294/mceclip0.png)

Configuração dos parâmetros:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096371334/mceclip1.png)

Procedimentos de utilização:

1. No módulo **Livros Fiscais (SIGAFIS**), acesse **Atualizações/Cadastro/Tipo de Entrada e Saída (MATA080)**, informe uma TES com a seguinte configuração.

* + Na pasta Impostos o campo **Calcula ICMS** (F4\_ICM), opção **Sim**.
  + Na pasta Impostos o campo **L. Fisc. ICMS**(F4\_LFICM), opção **T=Tributado**.

2. No**Cadastro de Produtos**, na pasta Impostosobserve o conteúdo do campo **%Red.430080** (B1\_PR43080) indique o percentual de redução na base de cálculo no cadastro de um produto.

3. No **Cadastro de Fornecedores**, cadastrar um fornecedor de Minas Gerais.

4. No **Cadastro de Clientes,** cadastrar um cliente de Minas Gerais.

5. No módulo **Compras (SIGACOM**), acesse **Atualizações/Movimentos/Documentos de Entrada (MATA103)**, incluir uma Nota Fiscal de Entrada. Na pasta Impostos, observe a base do imposto já reduzido, a alíquota e o valor do imposto. Na pasta Totais está indicado o valor da mercadoria e o total da nota que são diferentes devido ao cálculo do desconto.

6. No módulo **Faturamento (SIGAFAT**), acesse **Atualizações/Faturamento/Documentos de Saída (MATA460)**, incluir uma Nota Fiscal de Saída. Na pasta Impostos, observe a base do imposto já reduzido, a alíquota e o valor do imposto. Na pasta Totais está indicado o valor da mercadoria e o total da nota que são diferentes devido ao cálculo do desconto.

Exemplo de cálculo:

Uma nota de saída onde o valor total dos produtos seja de R$ 1.000,00, onde o produto tenha 30% de redução da base de cálculo.

Desta forma, os cálculos ficariam desta forma:

* Base ICMS = R$ 1.000,00 – (R$ 1.000,00 \* 30%) = R$ 700,00
* Valor ICMS = R$ 700,00 \* 18% = R$ 126,00

* O valor do desconto corresponde à diferença entre o valor do ICMS sem desconto e ICMS com desconto:

Sem desconto o ICMS seria R$ 1.000,00 \* 18% = R$ 180,00

Valor do desconto = R$ 180,00 – R$ 126,00 = R$ 54,00

* Deve ser tirado do total da nota esse valor:

R$ 1.000,00 – R$ 54,00 = R$ 946,00

O total do valor da nota nesse exemplo será de R$ 946,00.
