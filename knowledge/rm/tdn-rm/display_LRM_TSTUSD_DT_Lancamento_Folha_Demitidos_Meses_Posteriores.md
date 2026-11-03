---
content_hash: e3434d2cd61c385724e6aa4ae2ac477259e9ef9dd3438c6c26ddcd159b38fb82
fetched_at: '2026-06-29T00:06:09.839229+00:00'
page_id: '203757630'
product: rm
source: tdn-rm
title: TSTUSD_DT_Lancamento_Folha_Demitidos_Meses_Posteriores
type: documentation
url: https://tdn.totvs.com/display/LRM/TSTUSD_DT_Lancamento_Folha_Demitidos_Meses_Posteriores
version: 2
---

# LANÇAMENTO DA FOLHA PARA DEMITIDOS EM MESES POSTERIORES

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cadastro de Rescisão* |
| **Situação/Requisito:** | *Ao efetuar um cadastro de rescisão posterior com 2 meses à frente da competência atual, não está sendo permitido realizar lançamentos na folha da competência atual.*  *Quando o cadastro da rescisão é na competência seguinte, os lançamentos não são bloqueados.* |
| **Solução/Implementação:** | *Ajuste no cadastro de Rescisão para não marcar o flag de rescisão calculada, no caso de data de demissão com 2 meses ou mais à frente da competência atual.*  *Para assim, permitir que haja lançamentos na folha do mês corrente.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSTUSD* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
