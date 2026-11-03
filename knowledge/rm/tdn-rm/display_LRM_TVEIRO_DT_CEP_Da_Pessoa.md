---
content_hash: 8dea91d5ae8d9ea3e2eae020666cb5a5385d0e92208bd0a956f7d383ab70480e
fetched_at: '2026-06-29T00:08:12.183606+00:00'
page_id: '243637804'
product: rm
source: tdn-rm
title: TVEIRO_DT_CEP_Da_Pessoa
type: documentation
url: https://tdn.totvs.com/display/LRM/TVEIRO_DT_CEP_Da_Pessoa
version: 115
---

# CEP DA PESSOA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Pessoas |
| **Função:** | CEP da Pessoa |
| **Situação/Requisito:** | Sistema grava a informação do CEP com a máscara aplicada, porém se a máscara é alterada nos parâmetros do sistema, ao carregar os dados da pessoa o CEP não está sendo exibido. |
| **Solução/Implementação:** | Realizada tratativa na carga do dos dados da pessoa para que sejam removidos os caracteres não numéricos. |
| **Conversores e Parâmetros:** | Realizado ajuste da carga de funções no processo de alteração de dados da requisição. |
| **Chamados relacionados:** | TVEIRO |
| **Requisito (ISSUE):** |  |

divs
