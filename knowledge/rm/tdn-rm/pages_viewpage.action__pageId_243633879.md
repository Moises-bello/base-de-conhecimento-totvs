---
content_hash: cd866c80281776f5ecec6f2c7de85e046baeff2b63b0a0ae371b64a82cd1e613
fetched_at: '2026-06-29T00:08:12.033672+00:00'
page_id: '243633879'
product: rm
source: tdn-rm
title: DT_CPMOV001-256_Melhorias_na_Cotação_Prazo_Entrega_Orçamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243633879
version: 116
---

# PRAZO DE ENTREGA NO ORÇAMENTO DA COTAÇÃO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | *Gestão de Estoques, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cotação* | *CmpCotacaoAction* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Orçamento / Negociação* | *CmpCotacaoOrcamentosForm* | |  |  | |
| **Cadastros Iniciais:** | **Solicitação de Compras para ser utilizada na cotação*.* |
| **Parâmetro(s):** | *Não se aplica* |
| **Ponto de Entrada:** | *Não se aplica* |
| **Chamados Relacionados** | *Não se aplica* |
| **Requisito (ISSUE):** | 1. [CPMOV001-244](http://jiraproducao.totvs.com.br/browse/CPMOV001-244 "Melhorias na Cotação - Documentação") |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *Oracle ou SQL Server.* |
| **Tabelas Utilizadas:** | *TCORCAMENTO, TWCORCAMENTO* |
| **Sistema(s) Operacional(is):** | *Windows 7 SP1 ou superior* |

## Descrição

A partir da versão 12.1.12 do TOTVS Gestão de estoques, compras e faturamento os campos **'Data de Entrega'** e **'Prazo de Entrega (dias)'**estão disponíveis na edição do orçamento da cotação para edição tornando possível trabalhar apenas com um data de Entrega fixa ou baseando se em um Prazo de entrega calculado em dias.

Esta alteração torna a cotação mais flexível para a geração da ordem de compras.

## Procedimento para Utilização

Caso o usuário opte por informar a data de entrega do orçamento em vez de o prazo de entrega, o sistema deverá manter o comportamento antes desta alteração e o prazo de entrega do orçamento deverá exibir a informação "-1" no campo. Caso o usuário opte por informar o prazo de entrega em dias, o sistema fará um calculo da previsão da data que será entregue, mas será considerado o prazo informado.

O prazo de entrega sempre prevalece neste caso, sendo que se o mesmo estiver como valor -1, será considerado a data de entrega informada. Este comportamento já existe no itens de orçamento e foi replicado para o orçamento.

Além disso foi criado um botão para que o prazo de entrega e data de entrega do orçamento possa ser replicado para os itens de orçamento.

 

**Geração da Ordem de Compras**

Na geração da ordem de compra a partir da cotação, foi realizado o tratamento para que, se o tipo de movimento estiver parametrizado para usar prazo de entrega o sistema calculará a data de entrega do movimento a partir da data que estiver informada no parâmetro **“Data Prazo de Entrega”** do tipo de movimento somada ao prazo de entrega do orçamento.

Exemplo:

“Data Prazo de Entrega = Data Emissão”: 15/06/16

Prazo Entrega do Orçamento: 5 dias

Data de Entrega Calculada no Movimento: 20/06/16

Na geração da ordem de compra a partir da cotação, se o tipo de movimento está parametrizado para usar data de entrega, o sistema manterá o comportamento já existente.

**Planilha de Importação e Exportação de Orçamento/Negociação**

Esta implementação não afetará a importação de planilhas. Na planilha já existe o campo Prazo de Entrega do orçamento. Caso esse prazo seja alterado na planilha, ao importa-la o prazo informado na planilha é gravado normalmente .

**Orçamento via WEB**

Foi criado um campo para exibir a data da cotação, que não poderá ser alterado, e um campo para o usuário informar o prazo de entrega do orçamento. Este campo tem o mesmo comportamento da tela.

Exemplo:

Data Cotação: 10/06/16

Prazo de Entrega do Orçamento no Portal: 5 dias

Data Entrega Calculada no Portal: 15/06/16

divs
