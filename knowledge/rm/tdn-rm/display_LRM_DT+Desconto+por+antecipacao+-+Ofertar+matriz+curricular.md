---
content_hash: 5d64a89511b4cd1a339d83257a92ebd4a5917c592d1daf30e4cba7a168e7e7f7
fetched_at: '2026-06-29T00:08:48.903321+00:00'
page_id: '329029110'
product: rm
source: tdn-rm
title: DT Desconto por antecipacao - Ofertar matriz curricular
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Desconto+por+antecipacao+-+Ofertar+matriz+curricular
version: 3
---

# DESCONTO POR ANTECIPAÇÃO - OFERTAR MATRIZ CURRICULAR

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Gestão Educacional* |
| **Módulo:** | *TOTVS Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Desconto por antecipação* | *Desconto por antecipação.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Ofertar Matriz Curricular*.* | *Ofertar Matriz Curricular* | |  |  | |
| **Cadastros Iniciais:** | *Cadastro de Matrizes Curriculares* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *DEDUINTEGRACOES-1407* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *N/A* |
| **Tabelas Utilizadas:** | *SHABILITACAOFILIALDESCPONTUAL* |
| **Sistema(s) Operacional(is):** | *N/A* |

## Descrição

No processo "Ofertar Matriz Curricular", disponível na visão de Matrizes Curricular,  foi disponibilizada a opção de selecionar os descontos de antecipação que serão automaticamente associados as matrizes aplicadas criadas durante o processo.

## **Ofertar Matriz Curricular**

No módulo Educacional o processo 'Ofertar Matriz Curricular' é acessado através dos processos de matrizes curriculares (Currículo e Oferta → Matrizes Curriculares → Processos → Ofertar Matriz Curricular).

O processo foi alterado e inserido mais um passo para a sua execução. Após selecionar os turnos para a oferta e avançar o processo, será exibido a visão contendo os descontos de antecipação já cadastrados no sistema.

É possível a realização de filtros para a seleção. O usuário deve selecionar os descontos que ele deseja cadastrar para nas matrizes aplicadas que serão criadas e executar o processo.

Importante:

A associação de desconto por antecipação a matriz aplicada validará a vigência do desconto por antecipação que está sendo associado. Não serão permitidas inclusões de descontos por antecipações com vigências sobrepostas. Os descontos que tiverem vigência sobrepostas não serão inseridos durante a execução do processo.

Importante:

Para o usuário vincular descontos por antecipação a matriz aplicada através deste assistente ele precisa ter permissão em descontos por antecipação no módulo financeiro.
