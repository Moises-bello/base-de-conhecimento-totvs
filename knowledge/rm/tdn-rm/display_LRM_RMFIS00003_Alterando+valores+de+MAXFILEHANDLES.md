---
content_hash: 71320ec69cd20e7923a5966b88c926ac5476478c02acd426297aae9358e9f7d6
fetched_at: '2026-06-29T00:08:43.046362+00:00'
page_id: '301187403'
product: rm
source: tdn-rm
title: RMFIS00003_Alterando valores de MAXFILEHANDLES
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00003_Alterando+valores+de+MAXFILEHANDLES
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1.x |
| **Ocorrência:** | Alterando valores de 'MAXFILEHANDLES' e 'MAXBUFSIZES' |
| **Ambiente:** |  |
| **Passo a passo:** | Para tratativa da mensagem "Erro de banco de dados: MAXFILEHANDLES", que pode ser apresentada ao logar no sistema e/ou tentar escriturar movimentos do TOTVS Gestão de Estoque, Compras e Faturamento, efetue este procedimento:        Saia do sistema e localize o aplicativo BDE Administrator, em seu painel de controle.        Altere os seguintes campos para os seus valores:       * + **MAXFILEHANDLES = 2048**   + **MAXBUFSIZE = 4096** |
| **Observações:** |  |
