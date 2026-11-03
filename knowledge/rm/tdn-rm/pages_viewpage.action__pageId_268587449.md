---
content_hash: 0c7e88c2a48081394a656423dacb0a1b212b7b7ea4050e01c38817b4d56f168f
fetched_at: '2026-06-29T00:08:20.747132+00:00'
page_id: '268587449'
product: rm
source: tdn-rm
title: DT_CPMOV001-460_Substituição_Marca_Todos_Fornecedores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268587449
version: 115
---

# SUBSTITUIÇÃO DE MARCA PARA TODOS OS FORNECEDORES

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Alterar Marcas do Produto | CmpCotacaoTrocaMarcaPrdCfoAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Cotação | CmpCotacaoAction | |
| **Cadastros Iniciais:** | *Consultar documento:* |
| **Parâmetro(s):** | *Consultar documento:* |
| **Ponto de Entrada:** | Não se aplica. |
| **Chamados Relacionados** | Não se aplica. |
| **Requisito (ISSUE):** | CPMOV001-460. |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle ou SQL Server. |
| **Tabelas Utilizadas:** | TCITMORCAMENTO – Itens de Orçamento. |
| **Sistema(s) Operacional(is):** | Windows 7 SP1 ou superior. |

## Descrição

Permitir que o comprador possa alterar as marcas dos produtos para todos os fornecedores da cotação.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **RM**, acesse **BackOffice/Gestão de Estoque, Compras e Faturamento/Ambiente/Parâmetros/Gestão de Estoque, Compras e Faturamento**. Na janela de **Assistente de Implantação de Processos** acesse **Gestão de Compras/Cotação**selecione uma Filial e na **Etapa 2 – Definições Gerais**marque o parâmetro **Usar Marca de Produto na Cotação**:

**CONFIGURAÇÃO DE SEGURANÇA**

Para que o Comprador possa efetuar a troca de marca dos produtos na cotação para todos os fornecedores, é preciso configurar a segurança. 

1. No RM acesse **Serviços Globais/Segurança/Perfis,** selecione o contexto **Gestão de Estoque, Compras e Faturamento.**Edite o perfil e em **[03] Compras/[03.01] Gestão de Compras/[03.01.02] Cotação** e permitir acesso à **[03.01.02.22] Permite Trocar Marca dos Produtos na Cotação**:

## Procedimento para Utilização

### **Cadastro de Marca e Vinculo de Marcas ao Produto**

1. Consulte o documento técnico: [DT\_CPMOV001-452\_Marca](http://tdn.totvs.com/display/LRM/DT_CPMOV001-452_Marca)

### Solicitações**de Compras com Item de Movimento usando marca.**

1. Consulte o documento técnico: [DT\_CPMOV001-452\_Marca\_Movimento](http://tdn.totvs.com/display/LRM/DT_CPMOV001-452_Marca_Movimento)

### Substituição de Marca na Cotação

**Substituição para Todos Fornecedores**

Quando o sistema for configurado para **Usar Marca de Produto na Cotação**e o comprador possuir permissão para **Permite trocar marca dos produtos na cotação**, na tela de edição da **Cotação \ pasta Orçamentos** será apresentado o botão **Alterar Marca do(s) Produto(s).**Este botão ficará habilitado para os seguintes status da cotação: **Composição, Aguardando Resposta Fornecedores** ou****Negociação da Melhor Oferta******.**

**Substituição de Marca para Todos os Fornecedores - Cotação com status Aguardando Resposta Fornecedores:**

1. Selecionar uma cotação com status igual a **Aguardando Resposta Fornecedores** clique em Editar.  
   O sistema apresenta a janela de edição da Cotação.
2. Na pasta Orçamentos selecione pelo menos um Fornecedor e clique em **Alterar Marca do(s) Produto(s)**  
     
     
   O sistema apresenta a janela de **Alterar Marca do(s) Produto(s).**Serão listados nesta janela somente os produtos que possuem marcas vinculadas ao produto.
3. Na janela de **Alterar Marca do(s) Produto(s)** será permitido informar a nova marca pelo grid de Produtos ou através do campo **Marca**.
   1. Quando for pelo grid editável, serão listados todas as marcas associadas ao produto no campo **Nova Marca Orçada**.
   2. Pelo campo **Marca**, caso tenha algum registro selecionado no grid, serão apresentadas as marcas do produto selecionado. Quando for selecionado mais de um produto será apresentado as marcas iguais para estes produtos. Após a escolha da marca, selecione os produtos e clique em **Alterar.**
4. Confira os dados e clique em **Executar**.

**Substituição de Marca para Todos os Fornecedores - Cotação com status ******Negociação da Melhor Oferta******:**

1. Selecionar uma cotação com status igual a ******Negociação da Melhor Oferta******clique em Editar.  
   O sistema apresenta a janela de edição da Cotação.
2. Na pasta Orçamentos selecione pelo menos um Fornecedor e clique em **Alterar Marca do(s) Produto(s)**  
   O sistema apresenta a janela de Alterar Marca do(s) Produto(s).
3. Na janela de **Alterar Marca do(s) Produto(s)** será permitido informar a nova marca pelo grid de Produtos ou através do campo **Marca**.
4. Confira os dados e clique em **Executar**.

divs
