---
content_hash: 8b13ea5ef2d0b990795c39b894cbc2519073eb2b28c585a84d452f63433a22c8
fetched_at: '2026-07-02T19:24:21.594723+00:00'
page_id: '268799141'
product: protheus
source: tdn-tec
title: Correção - Possibilitar fechar uma aba de um workspacefolder pelo "X"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268799141
version: 1
---

|  |  |
| --- | --- |
| Situação | Utilizando o exemplo do TDN do TWorkspaceFolder, após abrir a tela não é possível fechar as abas. |
| Ocorrência | O bloco bClose do TWorkspace não estava sendo emitido ao tentar fechar a aba. |
| Correção | Alterado para emitir o evento bClose, porém todo o controle de fechamento de aba deverá ser feito via AdvPL. |
| Informações adicionais | * Referente ao chamado: TWJXDA * Referente à ocorrência: SSIM-1280 * Disponível em builds superiores a 7.00.131227A-20161107 2.3.0 |
