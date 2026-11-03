---
content_hash: 17a6ea913263d03cb4813172148328445ba112e4150724acfcf5dfa1ea33326e
fetched_at: '2026-06-29T00:08:04.426903+00:00'
page_id: '235570598'
product: rm
source: tdn-rm
title: TUKEYM_DT_Atividade_Extra_Professor
type: documentation
url: https://tdn.totvs.com/display/LRM/TUKEYM_DT_Atividade_Extra_Professor
version: 118
---

# ATIVIDADE EXTRA DO PROFESSOR

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Atividade Extra do Professor* | *Atividade Extra do Professor* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Atividades Ofertadas* | *Atividades Ofertadas* | |
| **Cadastros Iniciais:** | *1) Professor cadastrado;*  *2) Atividade extra cadastrada;*  *3) Grupo de atividade extra cadastrada com o campo descrição e instituição disponível;*  *4) Atividade ofertada cadastrada.* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *Sql Server e Oracle* |
| **Tabelas Utilizadas:** | *SATIVIDADEPROFESSOR* |
| **Sistema(s) Operacional(is):** | *Windows 7* |

## Descrição

Ajuste no tamanho máximo do campo DESCRICAO da tabela SATIVIDADEPROFESSOR de 100 caracteres para 200 caracteres e do campo INSTITUICAO da tabela SATIVIDADEPROFESSOR de 30 caracteres para 100 caracteres.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(12.1.11)* deste chamado.

## Procedimento para Utilização

Para a rotina Atividade Extra do Professor:

1. Acessar o TOTVS Educacional;
2. Acessar Currículo e Oferta | Professor | Atividade Extra e cadastrar uma nova atividade extra e inserir um grupo de atividades (onde neste grupo deverá estar disponível os campos descrição e instituição);
3. Acessar Currículo e Oferta | Professor | Anexo Atividade Extra e inserir uma nova atividade selecionando a que foi cadastrada (onde ela possui um grupo de atividade que deixa disponível os campos descrição e instituição);
4. Preencher os campos de Descrição e Instituição com o valor máximo de 200 e 100 respectivamente e salvar.

Para a rotina Atividades Ofertadas:

1. Acessar o TOTVS Educacional;
2. Acessar Atividades Acadêmicas | Atividades ofertadas;
3. Selecionar uma atividade ofertada e ir no anexo Professor na atividade | Inserir um novo professor;
4. Preencher os campos de Descrição e Código Instituição com o valor máximo de 200 e 100 respectivamente e salvar.

divs
