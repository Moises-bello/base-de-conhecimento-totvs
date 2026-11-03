---
content_hash: de203006cd4fbd91076f619df7cc53dcaf140f9364fb19c606aa54fc751a47e6
fetched_at: '2026-06-29T00:06:07.131208+00:00'
page_id: '201735393'
product: rm
source: tdn-rm
title: TSOVLX_DT_Horário_Emissão_Movimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201735393
version: 2
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Função:** | Edição de Movimento |
| **Situação/Requisito:** | Um dado movimento é criado por exemplo no dia 13/07 as 18:00, no dia seguinte antes de enviar a nota o movimento é editado e a data é alterada. Contudo o horário permanece como 18:00. Ao enviar a nota a mesma é rejeitada devido ao horário de envio. |
| **Solução/Implementação:** | Foi criado uma nova parametrização no sistema em MOV - Datas 2/2, onde é possível utilizar a opção "Data e Hora de Emissão do Movimento". Desta forma o sistema verificará se a Data de Emissão é diferente do Horário de Emissão ao salvar o movimento, e caso seja verdadeiro, irá atualizar o Horário de Emissão. |
| **Conversores e Parâmetros:** | NA |
| **Chamados relacionados:** | NA |
| **Requisito (ISSUE):** | NA |
| **Versões/Release:** | 11.82.41 |
