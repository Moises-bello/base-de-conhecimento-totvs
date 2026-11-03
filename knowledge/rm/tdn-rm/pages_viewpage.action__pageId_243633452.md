---
content_hash: aecd14600f726499093e862a026e13967c4cbc5fd2398a7d757857e7abba8284
fetched_at: '2026-06-29T00:08:12.005776+00:00'
page_id: '243633452'
product: rm
source: tdn-rm
title: DT_CPMOV001-256_Melhorias_na_Cotação_Produto_Indisponível
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243633452
version: 119
---

# PRODUTO INDISPONÍVEL NO ORÇAMENTO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | *Gestão de Estoques, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cotação* | *CmpCotacaoAction* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Orçamento / Negociação* | *CmpCotacaoOrcamentosForm* | |  |  | |
| **Cadastros Iniciais:** | *Solicitação de Compras para ser utilizada na cotação* |
| **Parâmetro(s):** | *Não se aplica* |
| **Ponto de Entrada:** | *Não se aplica* |
| **Chamados Relacionados** | *Não se aplica* |
| **Requisito (ISSUE):** | 1. [CPMOV001-244](http://jiraproducao.totvs.com.br/browse/CPMOV001-244 "Melhorias na Cotação - Documentação") |
| **País(es):** | *Brasil.* |
| **Banco(s) de Dados:** | *Oracle ou SQL Server.* |
| **Tabelas Utilizadas:** | *TCORCAMENTO, TCITMORCAMENTO, TWCITMORCAMENTO, TWCORCAMENTO* |
| **Sistema(s) Operacional(is):** | *Windows 7 SP1 ou superior* |

## Descrição

Foi criado um novo status com a descrição **Indisponível** para os produtos orçados. A informação do produto indisponível deve ser registrado no item de orçamento para que os produtos ainda não cotados sejam confundidos com os produtos indisponíveis pelo fornecedor da cotação.

## Procedimento para Utilização

O status indisponível está disponível para ser utilizado na tela de edição de Itens de Orçamento.

**Observações:**

Ao alterar o status do produto cotação para **Indisponível**, este não será considerado no calculo do quadro comparativo, e sendo apresentado apenas como **Indisponível.**

Quando o produto tiver seu status alterado para **Indisponível**o valor cotado será zerado assim como  é feito para com o status **Não Cotado**. 

 O campo status só pode ser alterado durante a edição de um orçamento. Durante a negociação, este não poderá editado, e caso tenha a necessidade de alterar o status para **Indisponível** deverá editar o mesmo como **Orçamento** ao invés de **Negociação**

**Geração do Quadro Comparativo de Preços**

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação**, ao abrir uma cotação e **Calcular o quadro comparativo**, os itens que possuírem status do item igual a**Indisponível** no momento do registro de orçamento e/ou negociação, serão apresentados com a informação: **Indisponível**.

**Relatório de Quadro Comparativo em Excel**

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação**, ao abrir uma cotação e **Calcular o quadro comparativo**, na opção **Gerar Dados do QCP para Planilha,** o modelo completo terá a informação do **Status do Item**, que estará localizado a frente do **Status de Qualificação do Produto**, conforme imagem abaixo.

divs
