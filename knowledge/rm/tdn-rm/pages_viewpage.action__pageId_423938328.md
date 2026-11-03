---
content_hash: 9f6da9f10712254a65b6b1af9a90f9a6da11f53f5d1d3b011b9d819415f956cb
fetched_at: '2026-06-29T00:09:26.595611+00:00'
page_id: '423938328'
product: rm
source: tdn-rm
title: Associação Dinâmica do Centro de Custo/Conta Gerencial ao Plano Paralelo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938328
version: 3
---

Para a geração do SPED Contábil, quando a Sociedade Empresária estiver sujeita à regulamentação, seja do Banco Central ou da SRF, é necessário que seja feita a associação das contas contábeis do Plano de Contas Contábil utilizado pela empresa às contas paralelas correspondentes do Plano de Contas da Receita-Plano Referencial. Se a empresa utilizar em suas movimentações Centros de Custos ou Contas Gerenciais, é necessário fazer também a associação destes às contas contábeis.

A associação dos Centros de Custos / Contas Gerenciais pode ser feita manualmente, um(a) a um(a) às contas contábeis que já estiverem associadas às contas do plano paralelo, ou dinamicamente através deste processo.

Uma vez que as contas contábeis já estiverem todas associadas às contas paralelas correspondentes, execute este processo e indique as datas para o período inicial e período final. O sistema identificará todos os Centros de Custos / Contas Gerenciais utilizados nas movimentações dentro do período informado e os associará dinamicamente às respectivas contas contábeis.

**Observações**

* Na execução deste processo, o sistema primeiramente removerá todas as associações de Centros de Custos / Contas Gerenciais que porventura existirem no plano paralelo informado para em seguida fazer dinamicamente as novas associações.
* A associação dinâmica somente será feita às contas contábeis que estiverem associadas às contas paralelas e somente para os Centros de Custos / Contas Gerenciais cujo campo Enviar para o Sped esteja marcado e que tiverem sido movimentados no período informado.
* No final do processo será gerado um LOG com as informações processadas.

**Pré-Requisto**

Nos Parâmetros do Sistema/Rotinas Legais deve ser devidamente indicado que informação a sua empresa irá considerar para o SPED Contábil, marcando uma das duas opções: 'O próprio Centro de Custo' ou 'Conta Gerencial'.
