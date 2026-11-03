---
article_id: 360026549773
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 3ad55728b08884e5194ec2613a9eb389a02231d8063143273fef50190a831905
fetched_at: '2026-06-28T22:38:43.934415+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT -Nota complemento
  de despesas acessórias (frete, seguro,despesa) da nota de devolução de compra
type: support-article
updated_at: '2023-10-16T20:10:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026549773-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Nota-complemento-de-despesas-acess%C3%B3rias-frete-seguro-despesa-da-nota-de-devolu%C3%A7%C3%A3o-de-compra
---

**Dúvida**

Nota complemento de despesas acessórias (frete, seguro,despesa) da nota de devolução de compra.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

 

**Solução**

Para solucionar realize os seguintes passos:

 1º Cadastrar o Fornecedor no cadastro de Clientes (**MATA030**) (Para que esta entidade seja considerada no Pedido do Tipo Complemento);

2º Incluir Pedido de Venda do **Tipo = C** - **Complemento de Preço** para este Cliente ;

3º Cadastrar um Produto para menção na Nota (Exemplo: "Produto Frete") e registrar no Pedido de Vendas;

4º Utilizar um TES (**MATA080**) que não movimenta estoque, porém, gera título no Financeiro;

5º Deixar o campo de Quantidade em branco, e preencher os campos **C6\_PRCVEN** e **C6\_VALOR** com o mesmo Valor (O valor da despesa / do frete / do seguro)

6º Digitar manualmente nos campos **C6\_NFORI** e **C6\_SERIORI** os números de Nota e Série Originais (A nota de Devolução);

7º Finallizar, liberar e faturar a nota de saída (**MATA461**).

OBS: O procedimento apresentado é uma forma paliativa pois se não desejar cancelar e excluir a nota fiscal para emitir corretamente.

**Saiba mais:****[Emitir uma Nota de Complemento para uma Nota de Devolução de compra](http://tdn.totvs.com/pages/releaseview.action?pageId=268585909)**
