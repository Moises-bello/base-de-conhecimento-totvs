---
article_id: 25359813543447
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 4294df3738478b4bc9449811c4038572f5dbbf1d48fcdaa00e7ffcc3f9c9522e
fetched_at: '2026-06-28T22:38:39.786858+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Faturamento com endereço
  bloqueado (BE_MSBLQL)
type: support-article
updated_at: '2024-08-02T23:57:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25359813543447-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Faturamento-com-endere%C3%A7o-bloqueado-BE-MSBLQL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25359797367703) Tempo aproximado para leitura: **00:04:00 min****Ocorrência:**Ao tentar faturar um Pedido de Venda onde os itens do pedido controlam endereço, e entre esses itens, um deles esteja com o endereço bloqueado pelo campo **BE\_MSBLQL**, caso não seja informado o endereço no campo **C6\_LOCALIZ**, o sistema permite que seja utilizado o saldo do endereço bloqueado.  
**Ambiente:**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Causa:**

Sobre os campos **\_MSBLQL e \_MSBLQD:**

* Somente serão tratadas tabelas de cadastro e que sejam tabelas pai. Exemplo: Tabela SB1 pode ser validada mas não as tabelas SB5 e SBZ que são suas filhas;
* Tabelas de movimento não serão tratadas;
* A validação será realizada somente em tela, através da validação de campo (X3\_VALID) com a função ExistCPO();
* Rotinas de processamento que utilizarem tabelas de cadastro não realizarão a validação do bloqueio do registro;
* Telas que não estiverem executando a validação de bloqueio do registro, serão tratadas como melhoria no produto.
* O processo de definição do endereço, quando não informado diretamente no campo (o qual possui o valid para preenchimento na SC6) é disparado e definido para modulo de estoque.

**Solução:**

O Ponto de Entrada [MTSLDLOT](https://tdn.totvs.com/pages/releaseview.action?pageId=268803104)  pode ser utilizado para não permitir a utilização do lote, seu retorno é lógico e iria barrar o consumo deste determinado lote.

Caso necessite utilizar outros pontos de entrada, abaixo indicamos alguns para uso:

* [Pontos de entrada - Documentos de Saída (MATA460A, MATA461)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7224837938327-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Lista-dos-pontos-de-entrada-nas-rotinas-de-Documentos-de-Sa%C3%ADda-MATA460A-MATA461)
* [Pontos de entrada - Pedidos de Venda (MATA410)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7381576110871-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Pontos-de-Entrada-na-rotina-Pedidos-de-Venda-MATA410)

**Saiba mais:**

[Uso e comportamento dos campos \_MSBLQL e \_MSBLQD](https://tdn.totvs.com/pages/releaseview.action?pageId=518484314)

[MTSLDLOT - Ponto que permite consultar os dados do produto com saldo por lote ou saldo por endereço](https://tdn.totvs.com/pages/releaseview.action?pageId=268803104)
