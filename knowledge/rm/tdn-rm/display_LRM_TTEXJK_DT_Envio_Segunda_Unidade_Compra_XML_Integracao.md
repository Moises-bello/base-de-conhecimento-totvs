---
content_hash: 4799206d47682aaafce3b238b2df6de64490d8e48bd2978fd7d63901c22dc7dd
fetched_at: '2026-06-29T00:06:07.921995+00:00'
page_id: '201740172'
product: rm
source: tdn-rm
title: TTEXJK_DT_Envio_Segunda_Unidade_Compra_XML_Integracao
type: documentation
url: https://tdn.totvs.com/display/LRM/TTEXJK_DT_Envio_Segunda_Unidade_Compra_XML_Integracao
version: 1
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Estoque, Compras e Faturamento.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | INT.002 | INT - CONFIGURADOR | |
| **Cadastros Iniciais:** | *Necessário que as cargas referentes as unidades a serem enviadas já estarem cadastradas no RM e integradas no PROTHEUS.* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados relacionados** | *N/A* |
| **Requisito (ISSUE):** | EST000001 - Produto |
| **País(es):** | *N/A* |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas utilizadas:** | *TPRODUTO, TPRODUTODEF* |
| **Sistema(s) operacional(is):** |  |
| **Versões/Release:** | *12.1.8* |

## Descrição

Ao enviar um produto do RM para o PROTHEUS na integração entre SigaMnt x BackOffice atualmente o valor do campo CODUNDCOMPRA não está sendo enviado na mensagem única de integração. Após a implementação o sistema deverá enviar na tag <SecurityInternalId> o valor referente ao campo CODUNDCOMPRA que é preenchido no cadastro do produto.

## Procedimento para Implantação

1 - O sistema é atualizado logo após a aplicação do pacote de atualizações *(Patch)* deste chamado, condicionado a NÃO ter executado o configurador.

2 - Caso o configurador já tenha sido utilizado, deverá ser utilizado o script referente à este chamado.

## Procedimento para Configuração

*1 - Necessário que a integração com o SIGAMNT esteja ativa.*

*2 - Necessário que a fórmula visual referente à entidade ITEM esteja ativa.*

## Procedimento para Utilização

1 - Acessar o cadastro de Produtos.

2 - Na aba controle de Estoque estarão visíveis a Unidade de Controle e também a Unidade de Compra.

3 - Editando o item e salvando devem ser enviadas na mensagem única os dois campos supracitados.

## Ponto de Entrada

|  |  |
| --- | --- |
| **Descrição:** | *Estoque -> Produtos* |
| **Localização:** | *Editar -> Aba Controle de Estoque* |
| **Eventos:** | *envio de campos no xml* |
| **Programa Fonte:** | *N/A* |
| **Função:** | *N/A* |
|  |  |
