---
content_hash: 358b2df8e766dc5059548e6bc586eb34159d2958ee1345b2f7832808c539af31
fetched_at: '2026-06-29T00:10:41.973189+00:00'
page_id: '546688766'
product: rm
source: tdn-rm
title: Habilitar/Desabilitar Edição de Composições Replanejadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546688766
version: 16
---

O processo "Habilitar/Desabilitar Edição de Composições Replanejadas" permite que o usuário possa habilitar ou desabilitar a edição de Composições que foram replanejadas. 

**Observação:**  
O processo só estará visível se o projeto estiver parametrizado para utilizar Vigência de Recurso e o usuário tiver permissão de acesso para esta funcionalidade.

Para que o processo seja executado é necessário que o usuário selecione pelo menos uma Composição que tenha sido replanejada. Assim ele poderá definir se as Composições selecionadas vão ficar Habilitadas ou Desabilitadas para edição.

* Se o usuário selecionar Composições replanejadas que já estão habilitadas, será permitido apenas a execução de Desabilitar a edição.

Após a execução, os possíveis resultados são:

* Caso seja selecionado Composições que não foram replanejadas e Composições que foram replanejadas, será exibido um Log de avisos, informando as Composições que foram alteradas com sucesso, e aquelas que não podem ser alteradas por não serem replanejadas.

* A Composição foi alterada, porém um alerta de ressalva é exibido.

* Todas as Composições sejam alteradas com sucesso.
