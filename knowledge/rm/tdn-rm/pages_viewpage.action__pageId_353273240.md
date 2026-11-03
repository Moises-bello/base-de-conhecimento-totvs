---
content_hash: 6cee31ba0ea1b823b8bbaf2d2524dc48a1152954d3590f68142a9eac7dcdd5de
fetched_at: '2026-06-29T00:08:57.104504+00:00'
page_id: '353273240'
product: rm
source: tdn-rm
title: RMPAT00009_Exclusão de Índices
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=353273240
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Totvs Gestão Patrimonial |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | Exclusão de Índices |
| **Ambiente:** |  |
| **Passo a passo:** | O processo permite excluir índices utilizados nos cenários de cálculo.  Os valores em índices estão presente nos cadastros de patrimônio, movimentações e relatórios do sistema. Após exclusão, o cenário de cálculo não mais utilizará índices para correções monetárias.    **Regras para Exclusão de Índices:** Para que ocorra a exclusão de índices deve- se primeiramente informar um cenário de cálculo. Ao executar o sistema irá realizar as validações abaixo: • O fechamento de período até o mês anterior ao período de cálculo atual, deve ter sido realizado; • Não poderá existir contabilizações de qualquer operação do sistema (Ocorrências, Depreciação, Transferências de Controle).    **Realizando a Exclusão de Índices:** Acessar: Utilitários | Exclusão de Índices.        Na tela de execução da rotina é apresentada uma mensagem com informações importantes do processo que devem ser lidas e avaliadas.        Selecione o respectivo cenário.        Verifique o cenário na tela do processo e selecione Executar.            Após ser executado com sucesso é possível observar em Cadastros| Cenários, que o cenário informado no processo não possui mais índice; Ao emitir os Relatórios é possível verificar os valores em índices zerados (0,00); Ao acessar o cadastro de patrimônio é possível verificar os valores em índices igual a zero (0,00); Ao realizar uma ocorrência não será apresentado o valor em índices.                        Vale lembrar que os índices serão excluídos somente para os cenários ao qual o processo será realizado, novos cadastros de cenários o índice poderá ser inserido se desejado. Este processo é irreversível. |
| **Observações:** |  |
