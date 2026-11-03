---
content_hash: 79f376637dc0b65a45aa275816d7332f4fca0e3353444a46dd1b36bbbb338e56
fetched_at: '2026-07-02T19:24:24.946187+00:00'
page_id: '491456345'
product: protheus
source: tdn-tec
title: Logix - Campos tipo Data não estão gavando as informações corretamente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=491456345
version: 1
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Ocorrência | Cliente está com problema de validação da data informada na tela, no programa CON10186 opção "Geração arquivo para ECD".  A situação ocorre apenas se acessar o Logix via Web, se usar via smartclient ele funciona normalmente.  Pelo web ele consegue gerar se colocar as datas de 01/01/2018 a 30/12/2018, porém, quando colocar 31/12/2018 a tela retorna que os anos estão diferentes. |
| Correção | Corrigido o componente TGet para respeitar o que foi digitado no campo. |
| Informações adicionais | * Referente ao ticket: 5769929 * Referente à ocorrência: MTEC-2638 * Disponível a partir da build 7.00.131227A - 4.3.0 |
