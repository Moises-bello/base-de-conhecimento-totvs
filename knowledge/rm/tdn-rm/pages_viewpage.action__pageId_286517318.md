---
content_hash: 572e51af670d1262d848e15ef7e118c6d5a413795ca32be92f9b75ecaee7f2ca
fetched_at: '2026-06-29T00:08:40.921858+00:00'
page_id: '286517318'
product: rm
source: tdn-rm
title: 1203056 EDUCACIONAL01-2138 DT Digitação de notas de aluno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286517318
version: 104
---

# DIGITAÇÃO DE NOTAS DE ALUNO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Totvs Educacional |
| **Função:** | Digitação de notas de alunos |
| **Situação/Requisito:** | Ao salvar as notas digitadas dos alunos, o sistema apresenta uma mensagem de validação de violação chave. |
| **Solução/Implementação:** | - Ao realizar a manutenção nas notas dos alunos, o sistema realiza a gravação dessas alterações em uma tabela de log para histórico.  Na realização do registro desse histórico, o desempenho de alguns processadores faziam com que mais de um registro fossem registrado ao mesmo tempo, praticamente, gerando uma inconsistência na base dados.  Com isso, foi realizado um ajuste na gravação de dados, a fim de evitar que o registro de logs causem uma violação de chave no banco de dados. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 1203056 |

divs
