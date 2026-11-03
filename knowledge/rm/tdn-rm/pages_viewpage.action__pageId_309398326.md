---
content_hash: 90c05d810c4d3f3d6ac8f78a7bec802b4bec518d288b8025eb5fecdb4eba9e9f
fetched_at: '2026-06-29T00:08:44.608317+00:00'
page_id: '309398326'
product: rm
source: tdn-rm
title: 1566239 EDUCACIONAL01-2977 DT Lançamento de faltas na frequência diária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=309398326
version: 96
---

# LANÇAMENTO DE FREQUÊNCIA DIÁRIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Frequência diária* |
| **Situação/Requisito:** | Ao carregar a tela de frequência diária da turma onde haja um registro em que o campo JUSTIFICADA da tabela SFREQUENCIA esteja com um valor não numérico,  o sistema apresenta um erro de conversão de dados e não abre as informações para lançamento das faltas. |
| **Solução/Implementação:** | Foi realizado um ajuste no sistema a fim de que o valor do campo seja tratado da mesma forma que o banco de dados trata. Dessa forma, a inclusão de um valor não inteiro não irá gerar erro ao carregar a tela. |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.19* |
| **Versão Corrigida:** | *12.1.17* |
| **Versão Expedida:** | *12.1.17* |

divs
