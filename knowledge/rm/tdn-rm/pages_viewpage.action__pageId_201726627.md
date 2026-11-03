---
content_hash: 8353748bcb8b77f973efbf28bbcebec8a20db39f2fac83c2d3264191a219aa42
fetched_at: '2026-06-29T00:06:05.715790+00:00'
page_id: '201726627'
product: rm
source: tdn-rm
title: DT_Tolerância_no_Faturamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201726627
version: 8
---

# TOLERÂNCIA NO FATURAMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Tolerância no Faturamento |  |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Faturamento.* |  | |  |  | |
| **Cadastros Iniciais:** | Perfil do Usuário, |
| **Parâmetro(s):** | Aprovação |
| **Ponto de Entrada:** |  |
| **Chamados relacionados** |  |
| **Requisito (ISSUE):** | PCREQ-5374 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas utilizadas:** |  |
| **Sistema(s) operacional(is):** | Windows 7 SP1 ou superior. |
| **Versões/Release:** | 12.1.7. |

## Descrição

O processo de Tolerância no Faturamento consiste os limites superior e inferior informados no Cadastro de Produto, impedindo que ao realizar um faturamento de movimento que utilize tolerância os mesmos não sejam realizados.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

**1.****Parâmetros**

 Acessar: BackOffice | Gestão de Estoque, Compras e Faturamento | Aba: Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento

* Movimento de Origem
  + Processos: 04.09 – Outras Movimentações
  + Selecionar o tipo de movimento
  + [Mov – Outros Dados] Aprovação: Usa
* Movimento de Destino
  + Processos: 04.09 – Outras Movimentações
  + Selecionar o tipo de movimento
  + [Mov – Outros Dados] Tolerância: Usar Para Quantidade ou Usar Para Preço ou Usar Para Quantidade e Preço

**2.****Tolerância no produto**

 Acessar: BackOffice | Gestão de Estoque, Compras e Faturamento | Aba: Cadastros | Produto

* + Editar (ou incluir novo) um produto
  + Aba: Preço
  + Preencher “Tolerância Preço” e/ou “Tolerância Quantidade”.

**CONFIGURAÇÃO DE MENUS**

 Não há.

## Procedimento para Utilização

**Processos**

Acessar: BackOffice | Gestão de Estoque, Compras e Faturamento | Aba: Outras Movimentações | Outras Movimentações;

* + Selecionar o tipo de movimento de origem;
  + Selecionar a filial;
  + Faturar/Receber um movimento;
  + Alterar a quantidade e/ou preço do(s) item(s) e faturar

Neste momento ocorrerá a consistência da tolerância no faturamento, conforme parametrização do tipo de movimento de destino.

## Vídeo

 Não há.

## Ponto de Entrada

 Não há.
