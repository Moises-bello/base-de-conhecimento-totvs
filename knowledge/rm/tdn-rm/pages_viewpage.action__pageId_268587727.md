---
content_hash: 26dcf12b3613010d7bbdf54e2e8da74a6c3fdaff92606a66500471bb3adbe957
fetched_at: '2026-06-29T00:08:20.764201+00:00'
page_id: '268587727'
product: rm
source: tdn-rm
title: DT_CPMOV001-667_Agrupamento de Itens da Cotação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268587727
version: 113
---

# Agrupamento de Itens da Cotação

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cotação* | CmpCotacaoAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Informe a(s) rotina(s) envolvidas*.* | *Informe o nome técnico da(s) rotina(s) envolvidas.* | |  |  | |
| **Cadastros Iniciais:** | *Consultar documento: [DT\_CPMOV001-452\_Marca\_Cotacao](http://tdn.totvs.com/display/LRM/DT_CPMOV001-452_Marca_Cotacao)* |
| **Parâmetro(s):** | *Consultar documento: [DT\_CPMOV001-452\_Marca\_Cotacao](http://tdn.totvs.com/display/LRM/DT_CPMOV001-452_Marca_Cotacao)* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *N/A* |
| **Requisito (ISSUE):** | CPMOV001-667 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server ou Oracle* |
| **Tabelas Utilizadas:** | TCITMORCAMENTO – Itens de Orçamento. |
| **Sistema(s) Operacional(is):** | Windows 7 SP1 ou superior. |

## Descrição

Permitir que o comprador possa agrupar as marcas dos produtos para todos os produtos similares nos itens de orçamento\negociação da cotação.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **RM**, acesse **BackOffice/Gestão de Estoque, Compras e Faturamento/Ambiente/Parâmetros/Gestão de Estoque, Compras e Faturamento**. Na janela de **Assistente de Implantação de Processos** acesse **Gestão de Compras/Cotação**selecione uma Filial e na **Etapa 2 – Definições Gerais**marque o parâmetro **Usar Marca de Produto na Cotação**:

2. No **RM**, acesse **BackOffice/Gestão de Estoque, Compras e Faturamento/Ambiente/Parâmetros/Gestão de Estoque, Compras e Faturamento**. Na janela de **Assistente de Implantação de Processos** acesse **Gestão de Compras/Cotação**selecione uma Filial e na **Etapa 6 – Movimentos 1/2** desmarque o parâmetro **Não agrupar itens iguais na Cotação**:

**CONFIGURAÇÃO DE SEGURANÇA**

Para que o Comprador possa efetuar a troca de marca dos produtos na cotação para todos os fornecedores, é preciso configurar a segurança. 

1. No RM acesse **Serviços Globais/Segurança/Perfis,** selecione o contexto **Gestão de Estoque, Compras e Faturamento.**Edite o perfil e em **[03] Compras/[03.01] Gestão de Compras/[03.01.02] Cotação** e permitir acesso à **[03.01.02.22] Permite Trocar Marca dos Produtos na Cotação**:

## Procedimento para Utilização

Quando o sistema for configurado para **Usar Marca de Produto na Cotação, **agrupar itens iguais na Cotação****e o comprador possuir permissão para **Permite trocar marca dos produtos na cotação**, na tela de edição da**Cotação \ pasta Itens de Movimento****.**

1. Na pasta Itens de Movimento apresenta todos os produtos que estão participando da Cotação.  
     
     
     
   Neste momento é possível verificar que temos 2 produtos iguais na Cotação de Solicitações de compras distintas.

2. Selecionar um fornecedor que deseja realizar o orçamento\negociação na **pasta** **Orçamentos** clique em Editar. O sistema apresenta a janela de edição.

Quando utilizar agrupamento de itens não será possível realizar a alteração da Marca através da Grid, sendo necessário, utilizar o lookup de Marca e aplicar para os itens de orçamento selecionados através do botão "Aplicar em Selecionados".

3. Selecione o Item de Orçamento que deseja alterar a Marca para que seja possível realizar o agrupamento.

4. Informe a Marca no Lookup, onde serão apresentadas as marcas cadastradas no Anexo de Produto.

Caso seja selecionado mais de um produto distinto, as marcas apresentadas serão uma combinação de marcas iguais entre os produtos selecionados.

5. Após selecionar a Marca no Lookup, utilizar o botão "Aplicar em Selecionados" para realizar a troca da marca.

6. Salvar o registro do Orçamento para que a alteração seja efetivada.

divs
