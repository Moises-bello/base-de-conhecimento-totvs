---
article_id: 1500004315022
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 49b6c6373353aad3fa6e11d54e0b092d5ae967c07da94df79dcce3337679268f
fetched_at: '2026-06-28T22:38:39.852109+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - SIGAFAT - Help: A100VALOR'
type: support-article
updated_at: '2024-09-23T20:49:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004315022-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Help-A100VALOR
---

**Ocorrência**O que fazer quando gera o Help **A100VALOR** no Faturamento?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 11.80.  
  
**Solução**

Verifique se os campos de **quantidade** e **valor** das tabelas **SC6**, **SD1** e **SB6** estão com a quantidade de **decimais iguais**, conforme a documentação:

* [Aumento de Casas Decimais no ambiente Faturamento (SIGAFAT)](https://tdn.totvs.com/x/twEmDg)

Caso não estejam, realize o ajuste através dos "**[Grupos de Campos Numéricos](https://youtu.be/BXPL4BPr668?si=ZcVvWgMGujYV1ap5)**"

Todos os campos de **quantidade** devem ficar **iguais entre eles**, assim como todos os campo de **valor** também devem ter o **mesmo tamanho** entre eles.

**Help A100VALOR na Devolução de Poder de Terceiros no Faturamento:**

Além de validar o tamanho dos campos de quantidade e valor, verificar os parâmetros **MV\_BLOQSB6** e **MV\_LIBESB6**: **[TUBUQK\_DT\_Retorno de Poder de Terceiro](https://tdn.totvs.com/x/aWBNDQ)**

* **MV\_LIBESB6:** Indica se deve permitir a inclusão de NFE (**F4\_PODER3=D**) com quantidade total da remessa e saldo financeiro a menor.
* **MV\_BLOQSB6:** A finalidade desse parâmetro é impedir que seja informado um valor unitário diferente do valor unitário do campo **B6\_PRUNIT**.

Para maiores informações sobre **Devolução de Terceiros**:

* [Emissão de Nota de Devolução controlando Poder De/Em Terceiros (Retorno)](https://tdn.totvs.com/x/nKkXDg)

**Após** **ajustar** os campos, verifique a possibilidade de **executar**algumas rotinas de recálculos disponibilizados pelo sistema, que podem ajustar os campos que possuem dados incorretos:

* FATURAMENTO > Miscelanea > Ajustes > **Refazer Acumulados** (**MATA215**)
* FATURAMENTO > Miscelanea > Ajustes > **Refazer Poder de Terceiros** (**MATA216**)
* FINANCEIRO > Miscelanea > Recalculos > **Refaz Dados Clientes e Fornecedores** (**FINA410**)
* ESTOQUE/CUSTOS > Miscelanea > Processamentos > **Refaz Saldos** (**MATA300**)

Saiba mais sobre outros Helps no pedido de venda:

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Help: A410TOTAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007798262-MP-FAT-Help-A410TOTAL)**

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Help: A410UNIDIF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028613392-MP-FAT-Help-A410UNIDIF-na-devolu%C3%A7%C3%A3o-de-Compras)**
