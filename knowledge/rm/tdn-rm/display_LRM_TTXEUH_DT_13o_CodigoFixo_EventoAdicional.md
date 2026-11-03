---
content_hash: dbd81aa7d9f0f469a85c131ad22154543c82dcd897822a07d68e125aedc70eb6
fetched_at: '2026-06-29T00:06:21.652749+00:00'
page_id: '223175346'
product: rm
source: tdn-rm
title: TTXEUH_DT_13o_CodigoFixo_EventoAdicional
type: documentation
url: https://tdn.totvs.com/display/LRM/TTXEUH_DT_13o_CodigoFixo_EventoAdicional
version: 1
---

# 13o. COM MESMO EVENTO COMO CÓDIGO FIXO E EVENTO ADICIONAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *13o.Salário* |
| **Situação/Requisito:** | *No cálculo da 2a.Parcela de 13o.Salário, quando está cadastrado o mesmo evento como Código Fixo e como Evento Adicional de 13o., está sendo considerado somente o valor do Evento Adicional.*  *Mas ao cancelar o envelope, o número de vezes no cadastro do Código Fixo está sendo incrementado.* |
| **Solução/Implementação:** | *Ajuste no lançamento da 2a.Parcela de 13o.Salário para somar os valores, quando o mesmo evento está cadastrado como Código Fixo e como Evento Adicional de 13o., e consequentemente decrementar o número de vezes no cadastro do Código Fixo.* |
| **Chamados   relacionados:** | *TTXEUH* |
| **Versões/Release:** | *11.82.43* |
