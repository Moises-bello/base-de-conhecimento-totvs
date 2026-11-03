---
content_hash: 68bfd6c4ed66f2e57c422e336cc968b5176893b2baebd6b296569f468aeb0348
fetched_at: '2026-06-29T00:09:08.327962+00:00'
page_id: '387288461'
product: rm
source: tdn-rm
title: 3376059 EDUCACIONAL01-5866 Matrícula Processo Seletivo RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=387288461
version: 82
---

# MATRÍCULA PROCESSO SELETIVO RM

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Matrícula Processo Seletivo RM* |
| **Situação/Requisito:** | *Ao realizar a matrícula do aluno proveniente do Processo Seletivo, ocorre a seguinte situação: Mesmo preenchendo a relação de cadastro "Forma de Inscrição x Tipo de Ingresso" no educacional, o tipo de ingresso não está sendo preenchido dentro do curso/habilitação do aluno.* |
| **Solução/Implementação:** | *Ajustado o método que buscava o valor do de-para Forma de Inscrição x Tipo de Ingresso. A consulta estava realizando o filtro utilizando o CODPESSOA da tabela SPSINSCRICAOAREAOFERTADA, que pode ser nulo em determinadas situações, como na inscrição via novo portal. Foi retirado esse campo da seleção, já que a chave primária da tabela já consta no filtro.* |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
