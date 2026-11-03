---
content_hash: 9fbaf6cc3e527d17a851339a4906cf243467c9e2ee7e9130bc1e8c506e5dcb21
fetched_at: '2026-07-02T19:24:19.696583+00:00'
page_id: '243655331'
product: protheus
source: tdn-tec
title: Ao executar o método CpyT2S() ocorre o erro "Invalid file signature".
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243655331
version: 1
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Situação | Ao executar o método CpyT2S() e passar o parâmetro lCompress como verdadeiro(.T.) ocorre um erro. |
| Ocorrência | Ao executar uma rotina de teste do método (CpyT2S), passando o parâmetro de para compactar arquivo ocorre o erro: Invalid file signature! |
| Correção | Correção na mensagem MS\_FILEOPEN do componente TFileManagerHook |
| Informações adicionais | * Referente ao chamado: Não há chamado relacionado * Referente à ocorrência: SCHTML-447 * Disponível a partir da build: 7.00.131227A - 3.1.7 |
