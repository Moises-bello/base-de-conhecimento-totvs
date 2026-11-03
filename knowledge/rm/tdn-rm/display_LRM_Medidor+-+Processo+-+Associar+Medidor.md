---
content_hash: 13bcff5556429ac851b483e0336125b6668824e87b2c1dc3dae5db2d76d36897
fetched_at: '2026-06-29T00:09:49.432464+00:00'
page_id: '435105293'
product: rm
source: tdn-rm
title: Medidor - Processo - Associar Medidor
type: documentation
url: https://tdn.totvs.com/display/LRM/Medidor+-+Processo+-+Associar+Medidor
version: 2
---

Processo tem como objetivo associar um ou mais medidores à um empreendimento.

**(Figura 1 - Tela de associação de medidores)**

Campos:

**Cód. Empreendimento** - Campo para selecionar o empreendimento que será associado o(s) medidor(es).

* Este campo é de preenchimento obrigatório.
* Se caso esse processo for chamado na visão de medidores, esse campo estará desbloqueado para alteração.
* Se caso esse processo for chamado na visão de empreendimento, esse campo estará bloqueado e já preenchido pelo empreendimento selecionado.

**Associar por** - Campo para selecionar ao que o medidor vai ser associado.

* Em caso de processo chamado na visão de medidores, esses campos serão devidamente bloqueados conforme:
* Caso o medidor selecionado seja Tipo Geral, ele só poderá ser associado ao empreendimento.    2.1.2 Caso o medidor selecionado seja Por Grupo, ele poderá ser associando por unidades ou subunidades.
* Caso o medidor selecionado seja Individual, ele só poderá ser associado a uma subunidade.
* Se caso esse processo for chamado na visão de empreendimento, esses campos serão desbloqueados.
* Caso ele seja associado por empreendimento, será possível associar somente medidores do Tipo Geral.
* Caso ele seja associado por unidade, será possível associar somente medidores Por Grupo.
* Caso ele seja associado por subunidades, será possível associar somente medidores Individual e Por Grupo.

**Medidores** - Campo para selecionar o(s) medidor(es) a ser(em) associado(s) à algum empreendimento, unidade(s)ou subunidade(s).

* Os medidores a serem exibidos, estarão de acordo com o tipo de associação selecionado.

**Data inicial da associação** - Campo para selecionar a data inicial da associação, se vai ser a mesma data de ligação do medidor ou alguma data customizada.  
  
**Empreendimento** - Campo para selecionar a(s) unidade(s) ou subunidade(s).

* Se o cadastro for associado por um empreendimento, esse campo será preenchido automaticamente.
* As unidades ou subunidades a serem exibidos, estarão de acordo com o empreendimento selecionado.
* Observações.:
  + Na visão de empreendimento é possível selecionar somente um empreendimento por vez.
  + Na visão do medidor é possível selecionar um ou mais medidores, desde que, tenham o mesmo Tipo de medidor.
