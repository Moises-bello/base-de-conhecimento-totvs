---
content_hash: a0e3129f17583c725654eb75f265b25a1fc30c174e9370f6caa133d985e8ed61
fetched_at: '2026-06-29T00:11:38.869657+00:00'
page_id: '785618693'
product: rm
source: tdn-rm
title: Regras de preenchimento do Centro de Custo
type: documentation
url: https://tdn.totvs.com/display/LRM/Regras+de+preenchimento+do+Centro+de+Custo
version: 4
---

**Paciente interno**

* Centro de custo, será do leito

+ Se o paciente estiver ocupando o leito
+ Local de uso for leito ou berçário

* Centro de custo, será do local de uso

+ Local de uso for Centro Cirúrgico ou Uti

* Não encaixou nas regras acima, irá tentar recuperar o centro do custo:
  + Do leito, se ele existir.
  + Senão do Local de uso

**Paciente Externo**

* Materiais e medicamentos

+ Centro de custo do

* Não encaixou na regra acima, irá tentar recuperar o centro do custo do local de uso.

Informações

Ao final, tanto para paciente externo ou interno, se o centro custo permanecer vazio, será recuperado o centro de custo da unidade de atendimento
