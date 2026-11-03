---
content_hash: 58d8aab8f03582396834d360ee11441e205df99b25bb95dd785924ae845a126e
fetched_at: '2026-06-29T00:08:04.062573+00:00'
page_id: '235334879'
product: rm
source: tdn-rm
title: TUMRRA_DT_Bloquear_Lancamento_Financeiro_Semelhante
type: documentation
url: https://tdn.totvs.com/display/LRM/TUMRRA_DT_Bloquear_Lancamento_Financeiro_Semelhante
version: 116
---

# LANÇAMENTO FINANCEIRO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Lançamento Financeiro* |
| **Situação/Requisito:** | Implementação de um parâmetro para que o usuário master defina se um lançamento financeiro já gerado com os mesmos dados deverá ou não ser gerado novamente. Esta validação será efetuada da mesma forma como é hoje: o sistema valida os campos, Coligada, Filial, Data Emissão, Valor e Histórico. Quando estes dados forem os mesmos, se o novo parâmetro estiver marcado, o lançamento não será gerado. |
| **Solução/Implementação:** | Criado parâmetro 'Bloquear Lançamento Financeiro com mesmo valor' nos parâmetros do TOTVS Folha de Pagamento - aba Geral. Marcando este parâmetro, os lançamentos que tiverem o mesmo valor, data de emissão, histórico, coligada e filial, não serão lançados. |
| **Chamados relacionados:** | *TUMRRA* |

divs
