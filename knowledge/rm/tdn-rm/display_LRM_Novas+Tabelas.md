---
content_hash: a065b4c45660156e7f67e3410072ac103802a4d1cc513464f2286f4b3f048ba6
fetched_at: '2026-06-29T00:12:14.124540+00:00'
page_id: '965460414'
product: rm
source: tdn-rm
title: Novas Tabelas
type: documentation
url: https://tdn.totvs.com/display/LRM/Novas+Tabelas
version: 4
---

Exemplo de select detalhado.

| Novas Tabelas | Antigas Tabelas | Descrição |
| --- | --- | --- |
| XCOMISSOES | XVENDA | Nova tabela de agrupador de comissão |
| XCOMISSOESITEM | XVENDEDOR, XCOMISSAO | item da comissão ou os comissionados/vendedores |
| XCOMISSOESITEMPARCELA | XCOMISSAOPARCELAMENTO | parcela da comissão |
| XCOMISSOESITEMPARCELAREC | XCOMISSAOPARCELAMENTOREC | parcela da comissão associada a baixa do lançamento que gerou a parcela |

| Novas tabelas de apoio a geração  da comissão | Descrição |
| --- | --- |
| XCOMISSOESMODCALCULO | Regra de Pagamento da Comissão |
| XCOMISSOESMODCALCULOCOMPN | Componentes da Regra de Pagamento da Comissão que são permitidas descontar comissão na mesa |
| XCOMISSOESREGRA | Regras da comissão como percentual, formula, quem recebe, quem paga e condição de pagamento |
| XCONDFUNCAO | Função de quem recebe na regra de comissão |
| XCOMISSOESMODALIDADE | Modalidade de como gerar a comissão atrelado ao empreendimento |
| XCOMISSOESMODALIDADEREGRA | Regras associadas a modalidade para pagar os comissionados |
| XCOMISSOESMODALIDADEEMPR | empreendimento associado a modalidade, podendo ser global |
| XCOMISSOESMODALIDADEPARAM | parâmetros para gerar a integração das parcelas do comissionado na modalidade |
| XCOMISSOESMETA | Parâmetros da meta da comissão |
| XCOMISSOESMETAITEM | Parâmetros da regra da meta da comissão |
