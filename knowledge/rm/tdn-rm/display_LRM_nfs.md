---
content_hash: f035472494ab5605dbd1a04c6bfa9f333406690b0f3159d4f45f1ab56148bbc7
fetched_at: '2026-06-29T00:11:26.384901+00:00'
page_id: '716357238'
product: rm
source: tdn-rm
title: nfs
type: documentation
url: https://tdn.totvs.com/display/LRM/nfs
version: 2
---

## Detalhamento das notas fiscais de serviços prestados pela empresa identificada no registro superior.

| Registro/Campo | Registro Pai | Ele | Tipo | Ocorr | Tam | Dec | Descrição | Origem RM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| serie | nfs | E | C | 1-1 | 5 |  | Informar o número de série da nota fiscal/fatura. Preencher com 0 (zero) caso não exista número de série. | DLAF.SERIEDOC |
| numDocto | nfs | E | C | 1-1 | 10 |  | Número da Nota Fiscal/Fatura | DLAF.DOCINI |
| dtEmissaoNF | nfs | E | D | 1-1 |  |  | Data de Emissão da Nota Fiscal/Fatura  Validação: O mês/ano da emissão da nota fiscal deve ser igual ao mês/ano indicado no registro de abertura do arquivo. | DLAF.DATAEMISSAO |
| vlrBruto | nfs | E | N | 1-1 | 14 | 2 | Preencher com o valor bruto da nota fiscal.  Validação: Deve ser maior que 0 | Somatório do valor contábil de todos os itens do lançamento. |
| obs | nfs | E | C | 0-1 | 250 |  | Observações. | DHISTLAF.OBSERVACAO |
