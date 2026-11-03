---
content_hash: 82d9dc9e936bfde4aff0be2d9d4c8a4e633bfa304bc80bc44283fcd86ddd77e5
fetched_at: '2026-06-29T00:06:21.649393+00:00'
page_id: '223175333'
product: rm
source: tdn-rm
title: TTFDY8_DT_13o_CodigoFixo_EventoAdicional
type: documentation
url: https://tdn.totvs.com/display/LRM/TTFDY8_DT_13o_CodigoFixo_EventoAdicional
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
| **Chamados   relacionados:** | *TTFDY8* |
| **Versões/Release:** | *12.1.9* |
