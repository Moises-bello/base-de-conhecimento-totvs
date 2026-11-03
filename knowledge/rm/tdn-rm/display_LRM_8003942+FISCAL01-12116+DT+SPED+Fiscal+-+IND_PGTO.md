---
content_hash: 9ac29d0165c08c90628ba01e8fc9fde814d78b7df7b772f8e653e0ab4fe73bdf
fetched_at: '2026-06-29T00:10:38.836422+00:00'
page_id: '545247897'
product: rm
source: tdn-rm
title: 8003942 FISCAL01-12116 DT SPED Fiscal - IND_PGTO
type: documentation
url: https://tdn.totvs.com/display/LRM/8003942+FISCAL01-12116+DT+SPED+Fiscal+-+IND_PGTO
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPED Fiscal |
| Ticket: | 8003942 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12116 |

## **02. SITUAÇÃO/REQUISITO**

Possibilitar na rotina SPED Fiscal, registro C100, a geração do campo 13 IND\_PGTO (Indicador de Pagamento), com o código igual a 2 "Outros", quando relacionado a notas fiscais de Devolução, que geraram financeiro.

## **03. SOLUÇÃO**

Ao Gerar o SPED Fiscal, O Registro C100, campo 13 IND\_PGTO (Indicador de Pagamento) será preenchido com o valor:

* Dado que um lançamento fiscal é proveniente de movimento:  
  + E, no movimento existe pelo menos uma parcela com o meio de pagamento “Sem Pagamento”:
    - 2 (“Outros”)\*
  + Se não existe nenhuma parcela com meio de pagamento "Sem Pagamento":
    - Se a forma de pagamento for igual a "Outros": 2 (“Outros”)\*
    - Se a forma de pagamento for igual à Vista: 0 ("À Vista")
    - Se a forma de pagamento for igual à Prazo: 1 ("À prazo")
* Se não for proveniente de movimento:
  + Se não houver data de vencimento: 2 (“Outros”)\*
  + Se a data de vencimento for maior que a data de emissão: 1 ("À prazo")
  + Senão: 0 ("À Vista")

Observação

Para o caso de geração referente à período igual ou anterior à "01/07/2012, será gerado com código 9 ("Sem Pagamento") ao invés de 2 ("Outros").
