---
content_hash: ea10dbaac70f2950e54104da5b461e947fcc8524448d25dcbeb6255cad0847f5
fetched_at: '2026-06-29T00:09:15.448944+00:00'
page_id: '421385383'
product: rm
source: tdn-rm
title: Conciliar Apontamentos
type: documentation
url: https://tdn.totvs.com/display/LRM/Conciliar+Apontamentos
version: 5
---

---

A conciliação de apontamentos é um processo do anexo "Apontamentos dos Coletores".

Através deste processo o sistema efetua a conciliação de registros de carga (início) e descarga (fim) do Ciclo de Transporte, que estão dispostos linha a linha separadamente, e os transforma em um único registro no anexo de "Apontamentos conciliados".

O inicio do processo é manual, mas a conciliação dos apontamentos é realizada automaticamente após o usuário informar, na interface do processo, o período para filtrar os apontamentos que serão considerados no processo. Uma vez efetuada esta conciliação os registros originais ficarão marcados como "Conciliado" e não poderão ser considerados nos próximos processos de conciliação dos apontamentos e tampouco sofrer alterações.

**Observação:**

Apesar da possibilidade de serem selecionados apontamentos de vários equipamentos distintos o sistema irá efetuar tal consolidação por conjuntos de apontamentos de mesmos equipamentos e apontamentos de um equipamento não serão processados junto ao conjunto de apontamentos de outro equipamento.

O total de registros deve ser um número par, uma vez que um apontamento consolidado é a união de dois apontamentos.

O total de registros de saída é igual ao total de registros de entrada.

Com isso poderemos garantir que todos terão pares, mas isto não garante que é o par correto, apenas que poderemos conciliar todos os apontamentos de coletores.

**IMPORTANTE:** Os apontamentos realizados através da leitura do QR code pelo aplicativo, após sincronizados, já aparcerão no sistema como conciliados, e por isso esse processo não será necessário nesse cenário.
