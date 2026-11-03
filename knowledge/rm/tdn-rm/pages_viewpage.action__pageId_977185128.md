---
content_hash: 4f48f03b77d9378a17d1b110b30aa6daf0ac720b4b62499a7b42246a76b967af
fetched_at: '2026-06-29T00:12:15.374676+00:00'
page_id: '977185128'
product: rm
source: tdn-rm
title: Consolidar Saldo da Conta/Caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=977185128
version: 7
---

# **Visão Geral**

Neste contexto, os saldos "Instantâneo", "Não Compensado" (e consequentemente a coluna calculada "Saldo Total") do [cadastro da Conta/Caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=421388837) não são atualizados automaticamente ao realizar operações que afetam os saldos da conta/caixa (baixa, cancelamento de baixa, compensação e cancelamento da compensação do extrato de caixa). Tais movimentações são armazenadas previamente em uma tabela auxiliar, a FSALDOCXAAUX. 

O recurso 'Consolidar Saldo' tem como objetivo atualizar os saldos "Instantâneo", "Não Compensado" (e consequentemente a coluna calculada "Saldo Total") do cadastro da Conta/Caixa de acordo com os valores dos registros contidos na tabela FSALDOCXAAUX, sendo possível agendar a execução do processo, configurar recorrência e fracionar os jobs a fim de obter uma melhor performance do processo.

# **Permissão**

No cadastro do Perfil do usuário foi liberada a etapa [03.01.02.03] Consolidar Saldo.

Ao permitir acesso a esta etapa, a opção 'Consolidar Saldo' estará disponível para uso no menu Movimentações Bancárias | Contas/Caixa.

# **Agendamento e fracionamento de job**

Este processo permite agendamento (quando o ambiente está em [N camadas](https://tdn.totvs.com/pages/viewpage.action?pageId=236432384)) e também o [fracionamento de job](https://tdn.totvs.com/pages/viewpage.action?pageId=547231277). Neste caso, ao seguir o procedimento indicado na documentação específica de agendamento, basta incluir o ID FinCxaConsolidarSaldoProcess e definir os parâmetros conforme a necessidade. Exemplo:

# **Demonstração do processo**
