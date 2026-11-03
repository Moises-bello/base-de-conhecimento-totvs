---
content_hash: c8a629b63ed0e0b5edb316ca31920b43a23db69200160b9abf684114f9dce964
fetched_at: '2026-06-29T00:11:16.195945+00:00'
page_id: '664191966'
product: rm
source: tdn-rm
title: Cálculo Distância Total (Km)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=664191966
version: 4
---

Para se chegar na distância do ciclo de transporte do tipo distância percorrida, é necessário realizar alguns cálculos.

O total de marcadores de distância percorrida no trajeto será igual ao número registrado no campo Ponto de Carga subtraído do número registrados no campo Ponto de Descarga.

**Total Marcadores (Estacas)** = Nº do Ponto da Descarga – Nº do Ponto de Carga

Caso o resultado do cálculo acima seja negativo, será considerado o valor absoluto do resultado.

Após o cálculo do Total de Marcadores, a distância entre os marcadores (estacas) de carga e descarga será obtida multiplicando o total de marcadores pela distância fixa entre os mesmos, conforme valor informado em km no parâmetro do projeto, ou no cadastro do ciclo, caso o valor tenha sido alterado.

Abaixo, mostramos as telas do parâmetro, e a do ciclo onde a distância pode ser alterada caso o ciclo possua uma distância diferente do valor default cadastrado para o projeto, respectivamente:

**Distância entre os marcadores de carga e descarga =** Total Marcadores \* Distância fixa entre Marcadores (definida no parâmetro ou ciclo conforme falado acima)

A Distância entre Marcadores será, então, somada à distância registrada pelo apontador no campo Acréscimo do apontamento de descarga, chegando-se, assim, à Distância Percorrida no percurso.

**Distância Total (Km)** = Distância entre Marcadores de carga e descarga + Acréscimo
