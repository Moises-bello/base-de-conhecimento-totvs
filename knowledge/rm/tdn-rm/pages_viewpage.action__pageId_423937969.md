---
content_hash: 5adc42e3d33325975dffa6e2af6d8e9e95500c611bc7661356d556e67380b4b0
fetched_at: '2026-06-29T00:09:24.604326+00:00'
page_id: '423937969'
product: rm
source: tdn-rm
title: Item de Aprovação Fluig
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937969
version: 26
---

O anexo relacionado ao Fluig é sempre criado no contrato, independentemente de haver ou não integração ativa.

Para identificar se o registro exibido é oriundo do Fluig, utilize o campo **ID Fluig**:

* **Em branco** – Indica que não está integrado ao workflow do Fluig.
* **Com valor** – Indica que está integrado ao workflow do Fluig.

Quando está sendo utilizada a [integração com o Fluig pra geração de workflows de Contrato](http://tdn.totvs.com/pages/viewpage.action?pageId=423938705), são exibidos os workflows gerados para o Contrato, é possível verificar o Identificador do workflow no Fluig e Status de Aprovação (Aprovado, Não Aprovado ou  Eliminado no FLUIG), além de demais dados do Item de Contrato ou Medição.

---

Após executar o processo **Geração de Workflow Fluig para Contrato** e acessar o Fluig e **Finalizar**, **Cancelar** ou **Excluir** a solicitação utilizando o processo nativo **Eliminar Solicitações**.

No RM, o processo **Remover solicitação de aprovação eliminada no Fluig** permite excluir do sistema a solicitação que já foi eliminada no Fluig.

* A solicitação de aprovação só pode ser removida no RM quando não houver vínculo ativo com o Fluig.
* Caso o item ainda esteja vinculado a uma solicitação existente no Fluig, a remoção não será executada.  
  Exceção: se o Fluig estiver desativado e o RM não conseguir validar o vínculo, a remoção poderá ocorrer.
* Após remover o relacionamento, é possível excluir a medição.
* Mesmo após a exclusão da linha associada à medição, o registro ainda é exibido, porém o campo ID Fluig passa a ser apresentado com o valor 0.
