---
content_hash: e75f6d09b7109620c7a3a65a5daf16e8f17a5c0b935638dbc757887ae19856b4
fetched_at: '2026-06-29T00:08:50.932099+00:00'
page_id: '334348063'
product: rm
source: tdn-rm
title: DT Geração de lançamentos - Seleção de alunos por arquivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=334348063
version: 7
---

# GERAÇÃO DE LANÇAMENTOS - SELEÇÃO DE ALUNOS POR ARQUIVO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Gestão Educacional* |
| **Módulo:** | **TOTVS Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Geração de lançamentos* | *Geração de lançamentos* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Seleção de alunos por arquivo** | *Seleção de alunos por arquivo* | |  |  | |
| **Cadastros Iniciais:** | *N/A* |
| **Parâmetro(s):** | **N/A** |
| **Ponto de Entrada:** | **N/A** |
| **Tickets relacionados** | **N/A** |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *DEDUINTEGRACOES-735* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | ***N/A*** |
| **Tabelas Utilizadas:** | ***N/A*** |
| **Sistema(s) Operacional(is):** | ***N/A*** |

## Descrição

No processo de geração de lançamentos (*Financeiro / Contábil | Financeiro*) foi disponibilizada mais uma opção pra seleção dos alunos. Agora é possível selecionar os alunos que terão lançamentos gerados a partir de um arquivo.

Será possível selecionar arquivos do tipo texto (.txt), CSV (.csv) e planilhas Excel (.xls, xlsx).

O único dado obrigatório que deve conter no arquivo é o registro acadêmico do aluno (RA) da tabela SALUNO.

Arquivos do tipo texto e CSV não devem ter cabeçalho e devem trazer o valor do registro acadêmico do aluno (RA) sempre na primeira posição da linha e, caso existam outros valores referentes a outras informações, a separação entre elas devem ser feitas através ';' (ponto e virgula).

Arquivos de planilhas Excel não devem ter cabeçalho e devem trazer o valor acadêmico do aluno (RA) sempre na primeira coluna.

Ao realizar a seleção de alunos através de arquivos Excel, é importante ressaltar que a leitura do arquivo é realizada até o momento em que é encontrada uma célula branco, na primeira coluna. Todos os alunos encontrados até esse ponto serão considerados no processo de seleção de alunos por arquivo.

Após a seleção do arquivo a ser considerado, basta clicar "Adicionar alunos" e será feita uma busca pelos alunos através dos valores informados referente ao registro acadêmico.

A sequência do processo de geração segue como antes.

## Vídeo

##
