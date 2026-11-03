---
content_hash: 2bf593009b823ac104f3b33d9adf3e48219cebe036273b491b6d094ee80ef82e
fetched_at: '2026-06-29T00:06:30.006970+00:00'
page_id: '234618567'
product: rm
source: tdn-rm
title: TUIM24_DT_MsgLog_CC2_Com_Dias_Ja_lancados
type: documentation
url: https://tdn.totvs.com/display/LRM/TUIM24_DT_MsgLog_CC2_Com_Dias_Ja_lancados
version: 2
---

# MSG LOG QUANDO CC 2 POSSUI DIAS JÁ LANÇADOS NO ENVELOPE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Dias Trabalhados* |
| **Situação/Requisito:** | *Quando o evento de CC 2, Dias Trabalhados, é calculado com férias cadastradas no mês, os dias de ferias são abatidos do total de dias trabalhados da competência.*  *Mas se estas férias são canceladas, e o evento de CC 2 é recalculado, o total de dias não é alterado.*  *No log de cálculo é exibida a mensagem "Dias lançadas pelo usuário".* |
| **Solução/Implementação:** | *Os CC's 1 e 2 tem uma regra considerada em qualquer situação de cálculo, que é nunca sobrepor o numero de dias ou horas já gravado no envelope, se o valor existente for menor que os dias de direito.*  *É assim, para possibilitar ao usuário efetuar pagamentos semanais, ou quinzenais.*  *Durante o recálculo dos CC's 1 e 2, se já existe um numero de dias ou horas gravado no envelope, não tem como identificar se este conteúdo foi informado pelo usuario, para efetuar um lançamento semanal por exemplo, ou se foi o caso de uma férias canceladas.*  *Será feito um ajuste apenas para alterar a mensagem exibida no log, já que nem sempre o valor lançado foi informado pelo usuário. A nova mensagem será "Dias já lançados no envelope".* |
| **Chamados   relacionados:** | *TUIM24, TUNNDT* |
| **Versões/Release:** | *11.82.43, 12.1.11* |
