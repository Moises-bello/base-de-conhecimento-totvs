---
content_hash: 755ceff8fc3af5e0e49de1e7411b788c8b29607e85a0dad3f9e29e8bb9dda926
fetched_at: '2026-06-29T00:08:52.529563+00:00'
page_id: '341217757'
product: rm
source: tdn-rm
title: DT Reestruturação do Censo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=341217757
version: 97
---

# REESTRUTURAÇÃO DO CENSO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **Totvs Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Censo* | **Censo** |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Relação de deficiências do Censo** | *****Relação de deficiências do Censo***** | | **Importação de dados do Censo da Educação Básica** | ****Importação de dados do Censo da Educação Básica**** | | ****Importação de dados do Censo da Educação Superior**** | ****Importação de dados do Censo da Educação Superior**** | | ****Preparação de dados do Censo da Educação Básica**** | ******Preparação de dados do Censo da Educação Básica****** | | ********Preparação de dados do Censo da Educação Superior******** | ************Preparação de dados do Censo da Educação Superior************ | | **********Arquivamento de dados do Censo da Educação Básica********** | ************Arquivamento de dados do Censo da Educação Básica************ | | ************Arquivamento gerais do Censo************ | ************Arquivamento gerais do Censo************ | | ************Exportar consultas do Censo************ | ************Exportar consultas do Censo************ | | ************Parâmetros do Censo************ | ************Parâmetros do Censo************ | |
| **Cadastros Iniciais:** | *N/A* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *[EDUCACIONAL01-2643](http://jiraproducao.totvs.com.br/browse/EDUCACIONAL01-2643)*  *[EDUCACIONAL01-2659](http://jiraproducao.totvs.com.br/browse/EDUCACIONAL01-2659)*  *[EDUCACIONAL01-2660](http://jiraproducao.totvs.com.br/browse/EDUCACIONAL01-2660)* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *Sql Server e Oracle* |
| **Tabelas Utilizadas:** | *N/A* |
| **Sistema(s) Operacional(is):** | *Windows 7, 8 e 10* |

## Descrição

* Foi criado um menu para o Censo em **Atividades Acadêmicas | Acadêmico**. As telas do Censo que ficavam no menu **Atividades Acadêmicas | Assistentes** foram transferidas para o novo menu, tais como, Importação de dados do Censo da Educação Básica e da Educação Superior; Preparação de dados do Censo da Educação Básica e da Educação Superior; Arquivamento de dados do Censo da Educação Básica e além disso a Relação de Cadastro de Deficiências localizado em **Currículo e Oferta | Auxiliares | Relação de Cadastro**;
* As rotinas do Censo (Básico e Superior) foram alteradas para buscar as consultas do código quando não houver configuração de consulta nos parâmetros do Censo;
* Foi incluída uma observação na tela de parâmetros, informando que quando não existir consulta parametrizada, a rotina do Censo irá utiliza a consulta padrão do sistema;
* Foi criada uma tela para fazer a exportação das consultas do Censo para um arquivo ou direto para as consultas do RM;
* A tela de Parâmetros do Censo foi retirada de dentro da tela de Parâmetros do Educacional e incluída no menu Censo.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da release 12.1.20.

## Procedimento para Utilização

O procedimento de utilização toma por base o seguinte documento de referência: <http://tdn.totvs.com/x/p41WF>.

* O novo menu criado para o **Ensino Básico** ou **Ensino Superior** que **usa Educacenso.**

* O novo menu criado para o **Ensino Superior** que **não usa Educacenso**

divs
