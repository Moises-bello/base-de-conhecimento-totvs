---
article_id: 1500004099822
category: Faturamento - Cadastros
content_hash: 2010dec74f9e411ea538d3720f2ccc66d29c0ec5b7a4ab4c73b200cc5c405b00
fetched_at: '2026-06-28T22:38:35.539680+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Histórico de
  Cliente
type: support-article
updated_at: '2021-09-30T16:38:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004099822-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Hist%C3%B3rico-de-Cliente
---

**Dúvida**

Existe alguma forma de manter o histórico de vendas de um cliente, caso seja necessário efetuar um cadastro novo?

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT- todas as versões

**Solução**

Dentro do sistema, o que pode ser efetuado é inativar o cadastro anterior, através do campo **a1\_msblql** (**bloqueio**), onde este registro só não poderá ser incluído em novos pedidos, orçamentos ou oportunidades, mas ficará no sistema para consulta e com isso, pode ser criado um registro novo para ele por conta do novo estado ou qualquer outra informação importante, podendo fazer até uma variação de loja por exemplo:

* O cliente tinha o código 000001, loja 01 e  estado SP e  passa a ser cliente código 000001, loja  02  e estado DF, mantendo o mesmo cnpj, porém, só será utilizado a loja 02 para os processos do sistema, enquanto a loja 01 fica bloqueada para uso, assim, não é excluído o registro e mantido o histórico de vendas.

Não tem como carregar o histórico de vendas do registro anterior para o cadastro novo.

**Importante**: No cadastro do cliente não há função que trate **histórico de compras**.  O cadastro de cliente possui o campo "**Maior compra**" (**a1\_mcompra**) na aba Financeira que indica o valor da maior compra do cliente na empresa. Este campo é calculado com base nas notas fiscais de vendas ou títulos implantados, armazenado na moeda forte definido pelo parâmetro **MV\_MCUSTO**.
