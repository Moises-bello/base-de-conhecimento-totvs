---
content_hash: 7b3ddb0ca48dd217a85e48d2d307be193d70544bdcc0aa0c335dcc5cbaacb81c
fetched_at: '2026-06-29T00:09:21.189119+00:00'
page_id: '422545857'
product: rm
source: tdn-rm
title: Consulta NFC-e
type: documentation
url: https://tdn.totvs.com/display/LRM/Consulta+NFC-e
version: 2
---

O processo de consulta da NFC-e valerá apenas para notas geradas em Contingência.  
 Ao executar o processo, será enviada para o TSS onde receberá o retorno do resultado do processamento da nota junta a SEFAZ.  
 O processo retornará os seguintes resultados:

* A NFC-e poderá permanecer em Contingência quando o serviço do TSS não retornar a autorização da SEFAZ. Neste caso o sistema não irá alterar o status da NFC-e, apenas será gravado no histórico da nota a mensagem retornada. O log poderá ser visualizado através do menu Anexos | Histórico.
* A autorização da NFC-e, caso o retorno seja resultado em uma autorização o registro terá seu status alterado para Autorizada. Neste caso o movimento que originou a NFC-e será bloqueado para edição.

A NFC-e ainda poderá ser Rejeitada ou Denegada. Na rejeição será retornado ao usuário o motivo. Neste caso de Rejeição o movimento poderá ser alterado e posteriormente enviado.

Status da NFC-e

[Imagens dos Status da NF-e / NFC-e](http://tdn.totvs.com.br/display/LRM/Imagens+dos+Status+da+NF-e)
