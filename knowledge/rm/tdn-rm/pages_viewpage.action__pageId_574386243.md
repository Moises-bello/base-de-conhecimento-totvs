---
content_hash: cf8bd667021b609bc1ed3d32db1f6b1185a027294c3f7ff4cca28645aa62d2ac
fetched_at: '2026-06-29T00:10:53.035913+00:00'
page_id: '574386243'
product: rm
source: tdn-rm
title: Remove Vínculo Patrimônio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=574386243
version: 11
---

Este processo permite desvincular funcionários/responsáveis de patrimônios. Se o parâmetro de sistema "Usar funcionários RM Labore como responsáveis" estiver marcado serão desvinculados funcionários, caso contrário responsáveis.

Processo

**Regras para execução da ocorrência**

Caso preencha apenas os patrimônios e data, o último funcionário/responsável por estes patrimônios será desvinculado.

Caso preencha apenas os responsáveis e data, serão desvinculados todos os patrimônios relacionados a estes funcionário/responsáveis.

Caso preencha todos os campos, serão desvinculados apenas os responsáveis dos patrimônios informados.

A data da remoção do vínculo deve ser maior do que a da última transferência realizada para o(s) mesmo(s) patrimônio(s), ou seja, deve-se conferir se o patrimônio já possui uma transferência e se a data é posterior a informada no processo a ser realizado.

Após a execução do processo será gerada uma transferência de controle para todos os patrimônios envolvidos, porém o campo de funcionário/responsável irá ficar vazio.

**OBS.:** Caso o parâmetro de sistema "Tornar responsável obrigatório" esteja marcado o processo não será realizado.

Veja Também

* [Transferência de Controle](https://tdn.totvs.com/pages/viewpage.action?pageId=423938031)
* [Consulta de Transferências de Controle](https://tdn.totvs.com/pages/viewpage.action?pageId=423938341)
