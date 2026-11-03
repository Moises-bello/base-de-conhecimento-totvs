---
content_hash: 046c5aee958626a5d546278f2af8329588c94298cd5bacc4f20d687360a8cfcf
fetched_at: '2026-06-29T00:08:50.117846+00:00'
page_id: '331866322'
product: rm
source: tdn-rm
title: 2060943 PORTALMOBILE01-3238 DT Validação de Matrícula Online
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=331866322
version: 2
---

# Validação de Matrícula Online

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Matrícula Online |
| **Situação/Requisito:** | Ao selecionar o curso/habilitação durante o processo de matrícula, o botão "Continuar matrícula" não aparece, impossibilitando a continuação do processo de matrícula.  Isso acontecia devido a um erro de execução dos javascripts que eram executados após as validações da matrícula, onde uma string possuía apóstrofo em seu conteúdo, causando erros na execução do javascript. |
| **Solução/Implementação:** | Foi realizado um ajuste no javascript em questão, onde é executado após as validações do Curso/Habilitação selecionado pelo aluno, para que os parâmetros passados para a função javascript possa receber strings que contenham apóstrofos em seu conteúdo. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
