---
article_id: 1500007798262
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: b1dbfb70a68d440f818d32d92aca67dca670f7f3fb2fe78cf86c9c5a0ed15699
fetched_at: '2026-06-28T22:38:41.066966+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento)
  - Helps A410TOTAL e A410TOTDPRC no Faturamento
type: support-article
updated_at: '2023-09-13T10:41:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007798262-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Helps-A410TOTAL-e-A410TOTDPRC-no-Faturamento
---

**Ocorrência**

O que fazer quando gera o Help **A410TOTAL** e **A410TOTDPRC** no Faturamento?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - A partir da release 11.80.

**Causa**

Esse incidente ocorre, devido a inconsistência nas configurações da Base de Dados. A soma dos produtos não bate com o valor total.

**Solução****Help: A410TOTAL SEM Poder de/em terceiros:**

Verifique se os campos de **quantidade** e **valor** das tabelas **SC5,** **SC6**, **SF1,** **SD1** e **SB6** estão com a quantidade de **decimais iguais**, conforme a documentação: **[FAT0068\_Aumento\_de\_Casas\_Decimais\_no\_ambiente\_Faturamento\_SIGAFAT](https://tdn.totvs.com/x/twEmDg)**

Todos os campos de **quantidade** devem ficar **iguais entre eles**, assim como todos os campos de **valor** também devem ter o **mesmo tamanho** entre eles.

**Help: A410TOTAL na Devolução COM Poder de/em terceiros (C5\_TIPO == D):**

Além de validar o tamanho dos campos de quantidade e valor, verificar os parâmetros **MV\_BLOQSB6** e **MV\_LIBESB6**:**[TUBUQK\_DT\_Retorno de Poder de Terceiro](https://tdn.totvs.com/x/aWBNDQ)**

* **MV\_LIBESB6:** Indica se deve permitir a inclusão de NFE (**F4\_PODER3=D**) com quantidade total da remessa e saldo financeiro a menor.
* **MV\_BLOQSB6:** A finalidade desse parâmetro é impedir que seja informado um valor unitário diferente do valor unitário do campo **B6\_PRUNIT**.  
  Para maiores informações sobre **Devolução de Terceiros**:  **[FAT0057\_Emissão\_de\_Nota\_de\_Devolução\_de\_Terceiros\_Retorno](https://tdn.totvs.com/x/nKkXDg)**

**Após** **ajustar** os campos, verifique a possibilidade de **executar**algumas rotinas de recálculos disponibilizados pelo sistema, que podem ajustar os campos que possuem dados incorretos:

* FATURAMENTO (SIGAFAT) > Miscelanea > Ajustes > **Refazer Acumulados** (**MATA215**)
* FATURAMENTO (SIGAFAT) > Miscelanea > Ajustes > **Refazer Poder de Terceiros** (**MATA216**)
* FINANCEIRO (SIGAFIN) > Miscelanea > Recalculos > **Refaz Dados Clientes e Fornecedores** (**FINA410**)
* ESTOQUE/CUSTOS (SIGAEST) > Miscelanea > Processamentos > **Refaz Saldos** (**MATA300**)

**Help: A410TOTDPRC**Essa mensagem ocorre quando multiplicação da quantidade e preço unitário não condiz com o valor total.Procure validar as casas decimais das tabelas SD1, SC6, SC9, SD2 (e SB6 se possuir poder de terceiros) com a documentação: **[FAT0068\_Aumento\_de\_Casas\_Decimais\_no\_ambiente\_Faturamento\_SIGAFAT](https://tdn.totvs.com/x/twEmDg)**

**Saiba mais:**

Outros HELPs do pedido de venda (MATA410):

* **[Cross Segmento - Backoffice (Linha Protheus) - SIGAFAT - Help: A100VALOR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004315022-MP-FAT-Help-A100VALOR)**
* **[Cross Segmento - TOTVS Backoffice (Linha Protheus)- SIGAFAT - Help : A410UNIDIF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028613392-MP-FAT-Help-A410UNIDIF-na-devolu%C3%A7%C3%A3o-de-Compras)**
