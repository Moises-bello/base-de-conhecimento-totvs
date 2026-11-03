---
content_hash: 8ae4e995c6c8cc0c3b33054bf48ce1f10412f43a206994a386b17a10bba95213
fetched_at: '2026-06-29T00:08:53.351827+00:00'
page_id: '344470453'
product: rm
source: tdn-rm
title: DT Exclusão de Alunos no Saída Inteligente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=344470453
version: 4
---

# EXCLUSÃO DE ALUNOS NO SAÍDA INTELIGENTE

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Excluir aluno da aplicação Saída Inteligente. | Excluir aluno da aplicação Saída Inteligente. |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Informe a(s) rotina(s) envolvidas. | Informe o nome técnico da(s) rotina(s) envolvidas. | |  |  | |
| **Cadastros Iniciais:** | Exportar aluno/responsável para a aplicação Saída Inteligente. |
| **Parâmetro(s):** | N/A |
| **Ponto de Entrada:** | N/A |
| **Tickets relacionados** | N/A |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | N/A |
| **País(es):** | Todos |
| **Banco(s) de Dados:** | *Sql Server e Oracle*. |
| **Tabelas Utilizadas:** | N/A |
| **Sistema(s) Operacional(is):** | *Windows 7, 8 e 10* |

## Descrição

Foi disponibilizada a opção de excluir alunos da aplicação Saída Inteligente. Deve-se filtrar quais alunos deverão ser excluídos e executar o envio dessas informações para a aplicação Saída Inteligente. A partir daí, deverão ser excluídos os alunos enviados e seus responsáveis da aplicação.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da release 12.1.20.

## Procedimento para Utilização

1. Acessar Integrações > Saída Inteligente > Excluir aluno da aplicação Saída Inteligente
2. Filtrar alunos no grid
3. Clicar em Executar

Obs. 1: A rotina enviará os alunos para serem excluídos na aplicação Saída Inteligente, porém, cabe à aplicação verificar se o aluno existe para ser excluído, assim como seus responsáveis.
