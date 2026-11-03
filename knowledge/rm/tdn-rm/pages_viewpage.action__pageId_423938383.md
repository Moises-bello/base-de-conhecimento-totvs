---
content_hash: ba0ea64ee1205b270ce3ff6f54f5dd44bc7dc38d82c2854f79384de43c27a4aa
fetched_at: '2026-06-29T00:09:26.718787+00:00'
page_id: '423938383'
product: rm
source: tdn-rm
title: Parâmetros de Lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938383
version: 3
---

**Barrar Lançamento com centro de custo inativo**

Com este parâmetro habilitado não será permitido a visualização ou seleção de centro de custo inativos na tela de contabilização (Saldus ou outro módulo) no lookup de centro de custo, entretanto, dependendo do parâmetro "Permitir Lançamento com Centro de Custo inativo por módulo " o centro de custo poderá ser visualizado.

**Permitir Lançamento com Centro de Custo inativo por módulo**

O parâmetro "Permitir Lançamento com Centro de Custo inativo por módulo" habilitará um controle para que o usuário possa selecionar o módulo no qual vai permitir contabilizações com centro de custo inativo. Esta opção somente estará disponível quando o parâmetro "Barrar Lançamento com Centro de Custo inativo por módulo" estiver habilitado.

Exemplo

Marco o parâmetro "Barrar Lançamento com centro de custo inativo" e o "Permitir Lançamento com Centro de Custo inativo por módulo ", e seleciono o módulo Patrimônio, neste caso se eu entrar na tela de contabilização do patrimônio vou poder visualizar e selecionar centro de custo inativo. Será habilitado somente se o parâmetro "Barrar Lançamento com centro de custo inativo" estiver marcado.

**"FCONT – Processar o saldo das contas de resultado antes do encerramento conforme o período informado e não conforme o encerramento realizado pela Transferência de grupos contábeis"**

Com este parâmetro habilitado o sistema irá calcular o saldo das Contas de Resultado conforme o período de apuração informado no FCONT e não pela Transferência de Grupos Contábeis e seus Históricos de Fechamento. Desta forma, somente será considerado os lançamentos com históricos normais ou sem preenchimento de histórico, ou seja, os lançamentos com histórico de fechamento serão desconsiderados.
