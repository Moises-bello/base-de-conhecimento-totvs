---
content_hash: afc86c0511f1b889f38c80e3c4eb9120532ed0925a26ba59f288f36e29f96b5b
fetched_at: '2026-06-29T00:08:38.515598+00:00'
page_id: '285661448'
product: rm
source: tdn-rm
title: 1147856 EDUCACIONAL01-1865 Geração Arquivo ENADE Aluno Irregular
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285661448
version: 100
---

# GERAÇÃO DE ARQUIVO ENADE

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Geração de arquivo ENADE |
| **Situação/Requisito:** | Foi identificado que ao gerar o arquivo para o ENADE pois o sistema está tratando como "Irregulares" os casos de alunos "Ingressantes", com situação da prova "Nenhum". |
| **Solução/Implementação:** | Foi identificado uma inconsistência nas validações do aluno, assim foi feito o ajuste para que o sistema desconsidere somente alunos que compareceram ou são irregulares de fato e gere o arquivo, independente de quantas vezes for executado o processo, carregando corretamente os alunos. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
