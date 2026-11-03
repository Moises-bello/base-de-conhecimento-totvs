---
content_hash: 2299961c1e21aef89ae6856cf0d5b2f2486f9cd17229519cabc99a3159169919
fetched_at: '2026-07-02T19:24:19.702442+00:00'
page_id: '243656824'
product: protheus
source: tdn-tec
title: Problema na geração do ProtheusDoc (11.2)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243656824
version: 1
---

Foi identificado uma falha na geração do ProtheusDOC, quando o arquivo não havia sido salvo ainda.

|  |  |
| --- | --- |
| Situação | Ao modificar ou adicionar um bloco de ProtheusDOC, não efetua a exportação corretamente. |
| Ocorrência | Ao modificar ou adicionar um bloco ProtheusDOC e solicitado a execução da exportação sem salvar o arquivo, o conteúdo usado na geração era o conteúdo do arquivo original (sem a alteração). |
| Correção | Ao acionar o processo de exportação é efetuada uma verificação de arquivos editados e não salvos, solicitando confirmação ao usuário quando necessário. |
| Informações adicionais | * Referente ao chamado: TVMCL9 * Referente à ocorrência: SSIM-1132 (e relacionados). * Disponível em builds superiores a 11.2.45 |
