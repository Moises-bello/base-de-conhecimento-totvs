---
content_hash: f041e951b0bd744982b0f9d469bf5fded27e90575d15021923b4eca61ea6cfe8
fetched_at: '2026-07-02T19:24:24.965337+00:00'
page_id: '493622215'
product: protheus
source: tdn-tec
title: Correção - Rotina de atualização automática do SmartClient
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=493622215
version: 1
---

Correção - Rotina de atualização automática do SmartClient

|  |  |
| --- | --- |
| Situação | Ao executar a rotina de atualização automática do SmartClient no Windows (através da seção [UPDATE] do arquivo de configuração do Application Server), uma mensagem de erro é exibida após falha na cópia de um arquivo com extensão DLL. |
| Ocorrência | Durante a atualização automática o binário SmartClient pode estar usando as bibliotecas DLL que seriam atualizadas, isto causa o erro reportado pois um arquivo em uso não pode ser alterado. |
| Correção | Correção na rotina de atualização automática do SmartClient para que as bibliotecas DLL em uso pelo binário também seja atualizadas. |
| Informações adicionais | * Referente ao chamado: 5345201 * Referente à ocorrência: MTEC-2485 * Disponível em builds iguais ou superiores a 7.00.170117A - 17.3.0.8 |
