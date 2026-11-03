---
content_hash: 2ddc453a337bd96f1eb437cb68b3298183a2f08e9dae61066b61bcb8441f6ac9
fetched_at: '2026-07-02T19:24:29.460940+00:00'
page_id: '893434313'
product: protheus
source: tdn-tec
title: Correção - Foco na tela errada ao voltar de outra TWorkspace encerrada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=893434313
version: 1
---

Correção - Foco na tela errada ao voltar de outra TWorkspace encerrada

|  |  |
| --- | --- |
| Situação | Quando o usuário está trabalhando em uma TWorkspace com sua TDialog e, em seguida, é aberta uma janela modal, e a partir dessa janela modal é criada uma segunda TWorkspace, ao encerrar essa segunda TWorkspace, o sistema retorna à primeira TWorkspace. No entanto, ocorre um erro de tratamento que faz com que a TDialog seja exibida sem a janela modal, a qual permanece oculta. |
| Ocorrência | Esse comportamento foi detectado em algumas telas do sistema Logix. |
| Correção | Foi aplicado um tratamento para ativar a janela correta após o encerramento de uma TWorkspace. |
| Informações adicionais | * Referente ao chamado: 21660464 * Referente à ocorrência: DTCLIENT01-5209 * Disponível em builds iguais ou superiores a 20.3.2.9 |
