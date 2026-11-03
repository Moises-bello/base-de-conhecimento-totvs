---
content_hash: bf6c000fd3ec94bf8e8c19409c1e33271620fb0c1581df420c44f2d402f2ebfc
fetched_at: '2026-06-29T00:08:45.289772+00:00'
page_id: '309414412'
product: rm
source: tdn-rm
title: 1486126 EDUCACIONAL01-2947 DT Matrícula de candidatos aprovados no Educacional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=309414412
version: 96
---

# MATRÍCULA DE CANDIDATOS APROVADOS EM PROCESSO SELETIVO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Matrícula de candidatos aprovados no Processo Seletivo* |
| **Situação/Requisito:** | *Ao tentar realizar a matrícula no Educacional de um candidato que foi aprovado em um Processo Seletivo e já tinha sido aluno, o sistema apresenta uma mensagem de validação informando que já existe uma pessoa cadastrada com as informações do candidato.* |
| **Solução/Implementação:** | *Foi realizado um ajuste no sistema para sejam utilizadas todas as informações de unicidade cadastrada no candidato para localizar um aluno com as mesmas informações.*  *Esse processo sempre utilizava as 4 informações de unicidade como, Nome, Data de nascimento, Estado natal e Naturalidade e quando o candidato não possuía todas essas preenchidas o aluno não era encontrado.*  *Agora, a busca será realizadas com as informações que estão preenchidas.* |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
