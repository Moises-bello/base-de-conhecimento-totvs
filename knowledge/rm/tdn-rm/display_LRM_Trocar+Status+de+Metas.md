---
content_hash: af1ffda2f624c45f115172dbfed2a5c30cf5f21ff50944e5cfd92e8a3961003e
fetched_at: '2026-06-29T00:09:59.374542+00:00'
page_id: '452718321'
product: rm
source: tdn-rm
title: Trocar Status de Metas
type: documentation
url: https://tdn.totvs.com/display/LRM/Trocar+Status+de+Metas
version: 2
---

**Trocar Status de Metas**

Este processo tem como objetivo alterar os status das metas. São eles:

**Abrir/Reabrir metas -** Processo responsável em alterar o status da meta para "Aberta" quando selecionar uma meta com o status "Em planejamento", "Suspensa" e/ou "Finalizada".

**Validações**

* Se o processo for disparado com apenas uma meta agrupadora selecionada, deverá ser exibida uma listagem com as metas filhas existentes, onde o usuário poderá escolher mais metas que deseja que sejam alteradas neste momento.
* Se o processo for disparado com mais de um item selecionado, as metas selecionadas deverão ser submetidas ao processo.
* Para metas agrupadoras, será verificada se as metas que estejam definidas em sua composição totalizem 100%. Caso o total não seja 100% será incluído um alerta que não impede a troca de status.
* Verificar se há mais de um responsável definido para uma meta. Nesse caso será incluído um alerta que impede a troca de status.
* Verificar se, para metas do tipo Valor, que utilizam faixas de valores, verificar se há pelo menos uma faixa que define a meta como "Cumprida". Caso não exista será incluído um alerta que não impede a troca de status.

**Suspender/Replanejar metas -** Processo responsável em alterar o status da meta para "Suspensa" quando selecionar uma meta com o status "Aberta".

**Validações**

* Se o processo for disparado com apenas uma meta agrupadora selecionada, deverá ser exibida uma listagem com as metas filhas existentes, onde o usuário poderá escolher mais metas que deseja que sejam alteradas neste momento.
* Se o processo for disparado com mais de um item selecionado, as metas selecionadas deverão ser submetidas ao processo.

**Cancelar metas -** processo responsável em alterar o status da meta para "Cancelada" quando selecionar uma meta com o status "Suspensa".

**Validações**

* Se o processo for disparado com apenas uma meta agrupadora selecionada, deverá ser exibida uma listagem com as metas filhas existentes, onde o usuário poderá escolher mais metas que deseja que sejam alteradas neste momento.
* Se o processo for disparado com mais de um item selecionado, as metas selecionadas deverão ser submetidas ao processo.

**Finalizar metas -** Processo responsável em alterar o status da meta para "Finalizada" quando selecionar uma meta com o status "Aberta".

**Validações**:

* Se o processo for disparado com apenas uma meta agrupadora selecionada, deverá ser exibida uma listagem com as metas filhas existentes, onde o usuário poderá escolher mais metas que deseja que sejam alteradas neste momento.
* Se o processo for disparado com mais de um item selecionado, as metas selecionadas deverão ser submetidas ao processo.
* Para metas agrupadoras, será verificada se as metas que estejam definidas em sua composição totalizem 100%. Caso o total não seja 100% será incluído um alerta que não impede a troca de status.
* Verificar se há mais de um responsável definido para uma meta. Nesse caso será incluído um alerta que impede a troca de status. - Verificar se, para metas do tipo Valor, que utilizam faixas de valores, verificar se há pelo menos uma faixa que define a meta como "Cumprida". Caso não exista será incluído um alerta que não impede a troca de status.
