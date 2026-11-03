---
content_hash: 2406e21defe975b958a54ea20cd530f42af5faa18cc18560de8a21ae77a34979
fetched_at: '2026-06-29T00:09:16.931299+00:00'
page_id: '421388524'
product: rm
source: tdn-rm
title: Parcelamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Parcelamento
version: 8
---

Parcelar Lançamentos é um recurso, que permite dividir um lançamento em vários outros, com valores, vencimentos e número de documento que poderão ser alterados e definidos durante a execução do processo.

O processo de parcelamento de lançamento é irreversível. Uma vez efetuado, não é possível recuperar o lançamento original.  
O lançamento que possuir  não poderá ser parcelado.

Não será permitido o Parcelamento de:

* Lançamento remetido para o banco
* Lançamento baixado
* Lançamento faturado
* Lançamento gerador de IRRF
* Lançamento gerado de IRRF
* Lançamento gerador de INSS
* Lançamento gerado de INSS
* Lançamento com cheque emitido
* Lançamento gerado por acordo
* Lançamento baixado por acordo
* Lançamento vinculado
* Lançamento baixado Parcialmente
* Lançamento negativado ou em processo de negativação.

**Observação:**

* Neste processo o lançamento de origem será excluído da base.
* Só é possível parcelar um lançamento de cada vez.
* A opção "Manter Data de Vencimento" indica se a data carregada do lançamento origem será mantida ou o sistema acrescentará um mês de intervalo entre cada novo vencimento.
* Com a opção "Atualizar Datas Opcionais de acordo com os Parâmetros" marcada será aplicada a regra do default da data opcional definida nos parâmetros do TOTVS Gestão Financeira, com exceção quando esta estiver como "Nula" (mantém a data do lançamento origem).
