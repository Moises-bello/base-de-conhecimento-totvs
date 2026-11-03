---
content_hash: af408fead52eb79e1831239ac5134386db9617a634367c1e1959a59b27fd8b6a
fetched_at: '2026-06-29T00:09:09.759493+00:00'
page_id: '394201429'
product: rm
source: tdn-rm
title: FINANCEIRO01-8489 DT Cancelamento de baixa sessão caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=394201429
version: 1
---

# Cancelamento de baixa de lançamentos baixados na sessão de caixa

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Cancelamento de Baixa |
| **Situação/Requisito:** | Ao tentar realizar o cancelamento de baixa de um lançamento que foi baixado via sessão de caixa o sistema não apresentava mensagem de erro relatando que a sessão de caixa ainda está aberta. |
| **Solução/Implementação:** | Realizada a validação se a sessão de caixa ainda está aberta, se estiver aberta o sistema deve bloquear o cancelamento da baixa. A baixa só será permitida caso a sessão de caixa esteja fechada. |
| **Requisito:** | FIN000041 |
