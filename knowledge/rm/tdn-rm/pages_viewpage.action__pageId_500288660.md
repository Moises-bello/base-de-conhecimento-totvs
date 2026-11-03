---
content_hash: c3cda87b9e9d86fc96964c4e533dbb1166f3939f4c8ab75d842594baee6862cf
fetched_at: '2026-06-29T00:10:23.236003+00:00'
page_id: '500288660'
product: rm
source: tdn-rm
title: MATESTCNTFTOF01-5915 DT Controle de Casas Decimais no Preço Faturamento, Valor
  Parcela, Valor e Valor Total de Medição do Item de Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=500288660
version: 17
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM. |
| Segmento: | BackOffice. |
| Módulo: | TOTVS Gestão de Estoque, Compras e Faturamento. |
| Função: | Número de Decimais do Preço. |
| Ticket: | Não se aplica. |
| Requisito/Story/Issue (informe o requisito relacionado) : | MATESTCNTFTOF01-5915. |

## **02. SITUAÇÃO/REQUISITO**

Ao configurar o parâmetro de *"Alterar edição do preço"* no cadastro de produto e definir o *"Número de Decimais do Preço",* esta parametrização é aplicada somente ao **Preço Unitário** do Item de Movimento.

## **03. SOLUÇÃO**

Foi realizado uma melhoria para que o campo **Preço Faturamento, Valor Parcela, Valor e Valor Total da Medição** do Item de Contrato siga a parametrização do *"Número de Decimais do Preço"* definida no Cadastro do Produto, respeitando as seguintes regras:

Se em "Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Parâmetros Gerais | Tabelas | Produtos | Definições Gerais | Definições de Produto 3/3 | Subgrupo Cadastrar", estiver marcada a opção “*Casas Decimais Preço*”, no cadastro do produto, aba Preço, será exibida a opção “*Alterar edição do Preço*”, que ao ser marcada habilita o campo “*Número de Decimais do Preço”,* onde deverá ser informada a quantidade de casas decimais que se deseja utilizar para o produto.

Na tela de Item de Contrato, o campo **Preço Faturamento** e **Valor Parcela** apresentarão a quantidade de casas decimais que estiver informada no cadastro do produto:

**Observação:** o campo Valor Total vai **sempre** seguir a parametrizacao geral das casas decimais definido em "Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Parâmetros Gerais | Definições Gerais 2/3 | Casas Decimais | Valores".

Na tela de **Medições**, os campos **Valor** e **Valor Total** apresentarão a quantidade de casas decimais conforme parametrização do controle de casas decimais no **Preço Faturamento**:

## **04. DEMAIS INFORMAÇÕES**

Se em "Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Parâmetros Gerais | Tabelas | Produtos | Definições Gerais | Definições de Produto 3/3 | Subgrupo Cadastrar" **não**estiver marcada a opção “*Casas Decimais Preço*”, na tela de Item de Contrato o campo **Preço Faturamento**apresentará a quantidade de casas decimais que estiver informada em "Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Parâmetros Gerais | Definições Gerais 2/3 | Casas Decimais | Valores".

Se no cadastro do produto, aba Preço, não estiver marcado o parâmetro “*Alterar edição do preço*”, quando esse produto for utilizado na tela de Item de Contrato, o campo **Preço Faturamento** apresentará a quantidade de casas decimais que estiver informada em "Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Parâmetros Gerais | Definições Gerais 2/3 | Casas Decimais | Valores":

Todos os demais campos de valor do contrato continuarão sendo apresentados com no máximo 04(quatro) casas decimais, conforme parametrização do sistema.

Todos os cálculos que envolvem o **Preço de Faturamento**serão feitos com no máximo 04(quatro) casas decimais, conforme parametrização do sistema.

**Observação:**

Para complementar a melhoria realizada foi criado também o campo **Seleção de Preço,** disponível na tela do Item de Contrato, na Base de Dados. O campo criado é o **TITMCNT.PRECOFATURAMENTOSELEC**.

Agora, a Seleção de Preço selecionada será salva no banco de dados, não tendo a necessidade de selecionar o preço novamente ao editar o item de contrato.

**Atenção:**

* Entre em contato com a equipe de suporte para obter o script de criação do campo no Banco de Dados.

## **05. ASSUNTOS RELACIONADOS**

* .
* [Parâmetros do Contrato](http://tdn.totvs.com/pages/viewpage.action?pageId=423938209).
* [Produtos/Serviços](http://tdn.totvs.com/pages/viewpage.action?pageId=423938817).
