---
content_hash: d6164c3cdd8048b40cd3468aae1cd68d181359280408e5fc0a0e4ff6c61f423f
fetched_at: '2026-07-02T19:24:19.651339+00:00'
page_id: '243638275'
product: protheus
source: tdn-tec
title: Implementação da funcionalidade exclusão de arquivo do componente TFileManagerHook
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243638275
version: 2
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
|  |  |
| Ocorrência | Ao executar o método CpyT2S() e passar o parâmetro lCompress como verdadeiro(.T.) ocorre o erro.  Segue o exemplo de teste:  cOrigem := "C:\temp\myfile.xyz" cDestino := "\test" lCompacta := .T. lSucess:= CpyT2S(cOrigem, cDestino, lCompacta) |
| Implementação | Implementação da mensagem MS\_FILEDELETE do componente TFileManagerHook |
| Informações adicionais | * Referente ao chamado: Não há chamado associado * Referente à ocorrência: SCHTML-446 * Disponível a partir da build: 7.00.131227A - 3.1.7 |
