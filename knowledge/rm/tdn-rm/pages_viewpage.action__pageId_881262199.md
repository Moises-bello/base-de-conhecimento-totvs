---
content_hash: 9b0ca5549696e6978bd08978ca15460f0318b4ca4812e6384e07815e1ea0e696
fetched_at: '2026-06-29T00:12:00.149235+00:00'
page_id: '881262199'
product: rm
source: tdn-rm
title: Meu Imóvel - Atendimentos - Anexos em Repositório de Arquivos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=881262199
version: 3
---

A partir do Release 12.1.2502 é possível armazenar os arquivos em anexo nos atendimentos do *Meu Imóvel* no repositório de arquivos *[FileRepo](https://tdn.totvs.com/pages/viewpage.action?pageId=792426187)* e não mais na tabela de arquivos anexos ao atendimento do RM.

Essa implementação foi concebida para atender a necessidade de armazenamento destes diversos tipos de arquivos e seus respectivos tamanhos, sem onerar a base de dados RM.

Para utilizar esta solução altere o parâmetro de ***[armazenamento dos arquivos anexos](https://tdn.totvs.com/pages/viewpage.action?pageId=425458436)*** do *Totvs Aprovações e Atendimento*, para utilizar o *Repositório de Arquivos (FileRepo)*,

**Importa reforçar que o envio de [anexo no Atendimento](https://tdn.totvs.com/display/LRM/Arquivos+Anexos+do+Atendimento), pelo Atendente e no [*Meu Imóvel* pelo cliente do contrato](https://tdn.totvs.com/pages/viewpage.action?pageId=715158089), não mudou em nada, ficando transparente a estes usuários.**
