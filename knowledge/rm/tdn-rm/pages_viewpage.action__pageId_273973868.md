---
content_hash: 12bda4d9b420c3322e30ee8f5ff360d71e17ae5386f15f5fa137b9b00d028795
fetched_at: '2026-06-29T00:08:31.899316+00:00'
page_id: '273973868'
product: rm
source: tdn-rm
title: 375884 MRH-5145 GPS ELETRÔNICA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273973868
version: 109
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | CONSTRUÇÃO E PROJETOS |
| **Módulo:** | FOLHA DE PAGAMENTO |
| **Função:** | GPS ELETRÔNICA |
| **Situação/Requisito:** | Quando é solicitada Geração de GPS Eletrônica, o arquivo está sendo gerado antes da geração dos dados. Dessa forma, o arquivo está sendo gerado sempre com dados da geração anterior, sendo necessário executar  o processo de geração da GPS eletrônica duas vezes, para que o arquivo seja gerado corretamente. |
| **Solução/Implementação:** | Foi modificado o processo de geração de GPS Eletrônica, para que o arquivo seja gerado após o calculo dos dados.  Não sendo necessário a execução duas vezes para que o arquivo seja gerado corretamente. |
| **Requisito:** | 375884 |

divs
