---
content_hash: 75d0fbcb8e5afd0111796c083c9e08eb55a45e4d9072207609982a863c0e1fd8
fetched_at: '2026-06-29T00:10:01.960838+00:00'
page_id: '452718815'
product: rm
source: tdn-rm
title: Filiais - SMT
type: documentation
url: https://tdn.totvs.com/display/LRM/Filiais+-+SMT
version: 2
---

**Filiais**

Por esta opção serão cadastradas as Filiais. Defaults Contábeis Serão informadas as contas contábeis default para débito e crédito para a contabilização dos lançamentos da filial, as contas contábeis defaults informadas nesta pasta poderão ser utilizadas em Cadastros | Contabilidade | Eventos Contábeis.

Ramo de Atividade O campo Ramo de Atividade possui os seguintes itens: "Comércio, Indústria, Serviços, Associação, Produtor Rural". Podem ser checados múltiplos registros, mas os campos Associação e Produtor rural são exclusivos, isto é, só podem ser chegados separadamente.

Validação da Inscrição Estadual Se o campo "Ramo de Atividade" for diferente de "Produtor Rural" e o campo "Estado" estiver informado, é feita a validação do campo "Inscrição Estadual".

**Observação:**

O campo Código do Calendário poderá ser utilizado no preenchimento do campo Data de Vencimento dos períodos de IRRF ou IRRF PJ.

Primeiro o sistema verifica o parâmetro do RM Fluxus - Pasta Datas - que define o calendário vigente. Se o parâmetro do RM Fluxus não está setado ou o cliente não possui o RM Fluxus o sistema considera o calendário informado nesse campo.

Os campos da pasta Endereço deverão se encontrar preenchidos, pois serão utilizados nas Rotinas Legais. O campo Ramo Atividade é utilizado nas rotinas GIA- MT e DAPI-MG. Os campos C.A.E Código da Atividade Econômica Principal e C.N.A.E: Classificação Nacional de Atividades Econômicas devem estar preenchidos corretamente pois serão utilizados nas Rotinas Legais.
