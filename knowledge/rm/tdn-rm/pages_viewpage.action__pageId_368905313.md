---
content_hash: 9ab8e4022f67ce178c7a0b6c3b09c771a6386627a28082cac9b563692eaa5d05
fetched_at: '2026-06-29T00:09:00.487281+00:00'
page_id: '368905313'
product: rm
source: tdn-rm
title: 2816299 EDUCACIONAL01-4953 DT Certificados/Diplomas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=368905313
version: 1
---

# CERTIFICADOS/DIPLOMAS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Certificados/diplomas |
| **Situação/Requisito:** | Ao entrar na aba "Registro do livro", o campo "Folha" está com o valor '0' sendo que no banco de dados esse campo está com o valor de '100001' |
| **Solução/Implementação:** | O valor máximo aceito no campo "Folha" do registro no livro do certificado/diploma estava limitado até 9999. O valor máximo foi alterado para 2147483647 que é o limite aceito em um campo do tipo int32. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
