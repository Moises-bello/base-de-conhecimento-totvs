---
content_hash: c6fb5ba78a2ee58e25e2b45a61e0c1baad6a88e89e15b14796944faaff77a369
fetched_at: '2026-06-29T00:10:25.171376+00:00'
page_id: '501476328'
product: rm
source: tdn-rm
title: Como visualizar o S-3000 de um registro na fila de eventos?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=501476328
version: 3
---

false

**A partir das Versões:**

* **12.1.23**
* **12.1.24**
* **12.1.25**

# Objetivo:

---

       O objetivo deste documento é trazer informações de como visualizar o identificador do evento S-3000 na fila de eventos, relacionando-o ao evento que o originou.

---

#### **Atenção: Nas versões iguais ou inferiores à 12.1.25, é necessário executar o RM.Atualizador para que o campo IDEVENTOEXCLUSAO fique disponível na fila de eventos.**

Quando for necessário excluir algum registro já enviado ao governo, o usuário pode gerar um evento S-3000, ou será gerado um gatilho automaticamente caso ele exclua o cadastro/registro de origem.

Após transmitir um S-3000 ao governo, ao realizar a atualização de status do mesmo e ele tiver seu status atualizado para 10 - Aceito RET, o evento que deu origem à exclusão terá seu status alterado para 11 - Excluído RET. Quando essa situação ocorre, tanto para eventos periódicos quanto para não periódicos que permitam a exclusão através do S-3000, será disponibilizado na fila de eventos a coluna "Id evento de exclusão":

Ao editar o registro do evento de origem, será possível ver o vínculo com o evento S-3000:
