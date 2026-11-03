---
content_hash: 675bc283131bd2ce35614b918d0da9ecb01c810a86a406efb25baf500df9b743
fetched_at: '2026-06-29T00:08:49.360740+00:00'
page_id: '330137885'
product: rm
source: tdn-rm
title: 1783004 EDUCACIONAL01-3679 DT Importação de Arquivo no Urânia
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=330137885
version: 1
---

# IMPORTAÇÃO DE ARQUIVO NO URÂNIA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Processo para importação de dados para integração com o Urânia |
| **Situação/Requisito:** | Ao realizar a importação do arquivo do urânia, utilizando um ambiente N Camadas (Client, AppServer, JobServer) o sistema apresenta a seguinte mensagem: "Um erro aconteceu ao tentar carregar o arquivo .xml. Detalhes: O arquivo xml informado não existe." |
| **Solução/Implementação:** | Foi feito um ajuste na importação do arquivo xml para 3 camadas. Ao trabalhar com três camadas, o server não consegue localizar o caminho do arquivo passado pelo client. Então, foi necessário importar o arquivo para o server. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
