---
content_hash: 06372403be6763186fe0feec112096c8f6a1b033e4a74723943303f1acf0dc44
fetched_at: '2026-06-29T00:09:54.242637+00:00'
page_id: '444597260'
product: rm
source: tdn-rm
title: 4609782 FOPCALCULO01-5651 Transferência - Funcionário tipo D
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=444597260
version: 1
---

# Transferência

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Plataforma RH |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Transferência |
| **Situação/Requisito:** | Ao fazer a transferência de filiais (mesma coligada) de um diretor e nesta coligada, está parametrizado para não cadastrar número de ficha de registro para Diretores, quando o cliente está fazendo a transferência deste diretor, o sistema não deixa avançar enquanto ele não preenche a ficha de registro. |
| **Solução/Implementação:** | Adicionado condição que ao verificar se o tipo de funcionário é diretor e o parâmetro de numero de registros para diretores habilita ou não o campo Numero de Registro |
| **Tickets relacionados:** | 4609782 |
