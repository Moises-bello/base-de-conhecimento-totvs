---
content_hash: de2d61974e1e135b2ebf8874e23d8487626b88bc91e2a248474d582bd785cd46
fetched_at: '2026-06-29T00:11:26.389208+00:00'
page_id: '716357943'
product: rm
source: tdn-rm
title: ideContri
type: documentation
url: https://tdn.totvs.com/display/LRM/ideContri
version: 5
---

**Informações de identificação do contribuinte.**

| Registro/Campo | Registro Pai | Ocorr | Tam | Descrição | Origem RM |
| --- | --- | --- | --- | --- | --- |
| ideContri | evtAssocDespRec evtAssocDespRep evtComProd evtCPRB evtEspDesportivo  evtRetPF  evtRetPJ | 1-1 |  | Informações de identificação do contribuinte | Identificação do declarante. |
| tpInsc | ideContri | 1-1 | 1 | Preencher com o código correspondente ao tipo de inscrição  Valores Válidos: 1 - CNPJ 2 - CPF | Gerado pelo sistema.  Verificar pelo tamanho da informação no campo CNPJ da Filial Matriz: CPF (11 carac.) e CNPJ(14 carac.). |
| nrInsc | ideContri | 1-1 | 15 | Informar o número de inscrição do contribuinte conforme o tipo de inscrição indicado no campo {tpInsc}.   Se for um CNPJ deve ser informada apenas a Raiz/Base de oito posições, exceto se natureza jurídica de administração pública federal ([101-5], [104-0], [107-4], [116-3]), situação onde o campo deve ser preenchido com o CNPJ completo com 14 posições.  Validação: Se {tpInsc} for igual a [1], deve ser um número de CNPJ válido. Se {tpInsc} for igual a [2], deve ser um CPF válido. | Preenchido, conforme as regras do campo, com o CNPJ da Filial Matriz.  GFILIAL.CGC |
