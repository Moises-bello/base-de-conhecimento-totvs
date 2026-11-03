---
content_hash: 5df4f86252d076c2ba088ea5832ac5e4d8fde60d3bcd60fdb801de4d28b24c2e
fetched_at: '2026-06-29T00:08:12.062657+00:00'
page_id: '243634478'
product: rm
source: tdn-rm
title: DT_CPMOV001-357_Interferência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243634478
version: 120
---

# INTERFERÊNCIA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | **Construção e Projetos*.* |
| **Módulo:** | **Gestão de Compras*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Interferência por Fornecedor.* | *Não se aplica.* | | *Interferência por Produto* | *Não se aplica.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Cotação* | *CmpCotacaoAction.* | |
| **Cadastros Iniciais:** | ***Cotação** deve estar com **status Negociação da Melhor Oferta** e usuário possuir permissão para **Realizar Interferência*** |
| **Parâmetro(s):** | *Não se aplica.* |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Chamados Relacionados** | *Não se aplica.* |
| **Requisito (ISSUE):** | *PCREQ-9558 e CPMOV001-357* |
| **País(es):** | *Brasil.* |
| **Banco(s) de Dados:** | *Oracle ou SQL Server.* |
| **Tabelas Utilizadas:** | *TCITMORCAMENTO - Itens de Orçamento.* |
| **Sistema(s) Operacional(is):** | *Windows 7 SP1 ou superior.* |

## Descrição

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação** e editar uma cotação para visualizar e/ou Calcular o Quadro Comparativo alterado a interferência por Produto para que seja possível ser aplicada a todos os produtos. A entrada de menu do processo será realizada no menu existente separando os Processos Por Fornecedor e Por Produto. A entrada de dados será realizada de acordo com a intenção do comprador.

### **Interferência por Produto via Quadro Comparativo:**

Para a interferência realizada através de um duplo clique no **Quadro comparativo** o Fornecedor virá preenchido e não será permitido a edição. A grid de produtos terá o filtro de acordo com o produto selecionado e não permitirá alteração dos campos **Código e Descrição do Produto, Unidade Solicitada, Quantidade Solicitada e Preço**, exceto pelo campo **Qtde a ser Gerada** ou **Qtde Efetivada**, de acordo com a parametrização, que poderá ser o seu valor preenchido e por fim informar o **Motivo** e se necessário o **Detalhe do Motivo**.

**Interferência por Produto via Menu:**

Para a interferência realizada através do menu, o usuário poderá selecionar o Fornecedor e todos os produtos que terão o campo **Qtde a ser Gerada**ou **Qtde Efetivada** alterada e por fim informar o **Motivo** e se necessário o **Detalhe do Motivo**. Serão alterados os valores dos produtos que estão exibidos na grid de acordo com o Fornecedor selecionado, portanto, não será possível editar múltiplos produtos para múltiplos fornecedores.

**Interferência por Fornecedor via Menu:**

Para a interferência realizada através do menu o usuário poderá selecionar o Fornecedor e todos os produtos estarão disponíveis apenas para a visualização e por fim informar o **Motivo** e se necessário o **Detalhe do Motivo**.

## Procedimento para Utilização

## 

### **Interferência por Produto via Quadro Comparativo:**

       1. No Gestão de Estoque, Compras e Faturamento, acesse **Compras / Cotação**.

O sistema apresenta a janela de **Filtros - Cotação - Composição.**

       2. Selecione uma opção de filtro e clique em Executar.

       3. Na visão de Cotação selecione uma Cotação com **Status Negociação da Melhor Oferta** e clique em **Editar**.

O sistema apresenta a janela **Cotação:...**

       4. Clique no botão **Quadro Comparativo**

O sistema apresenta a pasta **Quadro Comparativo**

       5. Clique duas vezes sobre um produto na grid.

O sistema apresenta a janela **Interferência.** Se necessário informe o **Motivo** e **Detalhe do Motivo** e confirme.

**Interferência por Produto via Menu:**

1. No Gestão de Estoque, Compras e Faturamento, acesse **Compras / Cotação**.

O sistema apresenta a janela de **Filtros - Cotação - Composição.**

2. Selecione uma opção de filtro e clique em Executar.

3. Na visão de Cotação selecione uma Cotação com **Status Negociação da Melhor Oferta** e clique em **Editar**.

O sistema apresenta a janela **Cotação:...**

4. Clique no botão **Quadro Comparativo**

O sistema apresenta a pasta **Quadro Comparativo**

5. Clique no botão **Interferência/Produto**

O sistema apresenta a janela **Interferência.**

6. Informe o **Cliente/Fornecedor**

O sistema apresenta na janela de **Interferência** todos os produtos da cotação. Informe a **Qtde A Ser Gerada** e se necessário informe o **Motivo** e **Detalhe do Motivo** e confirme.

**Interferência por Fornecedor via Menu:**

1. No Gestão de Estoque, Compras e Faturamento, acesse **Compras / Cotação**.

O sistema apresenta a janela de **Filtros - Cotação - Composição.**

2. Selecione uma opção de filtro e clique em Executar.

3. Na visão de Cotação selecione uma Cotação com **Status Negociação da Melhor Oferta** e clique em **Editar**.

O sistema apresenta a janela **Cotação:...**

4. Clique no botão **Quadro Comparativo**

O sistema apresenta a pasta **Quadro Comparativo**

5. Clique no botão **Interferência/Fornecedor**

O sistema apresenta a janela **Interferência.**

6. Informe o **Cliente/Fornecedor**

O sistema apresenta na janela de **Interferência** todos os produtos da cotação. Se necessário informe o **Motivo** e **Detalhe do Motivo** e confirme.

divs
