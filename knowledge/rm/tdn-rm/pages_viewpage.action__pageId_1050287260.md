---
content_hash: 32b67c932e8f907ea707ac281466c0ed00ed9d7581b5b76714f0f44803056b3e
fetched_at: '2026-06-29T00:05:51.238259+00:00'
page_id: '1050287260'
product: rm
source: tdn-rm
title: Substituição da NFCom
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1050287260
version: 5
---

Antes de substituir uma NFCom por este processo certifique-se que o parâmetro:  **Mov - Edita Movimento Relacionado** no tipo de movimento está marcado.

Preencha o campo Nome Mov. Relacionado com a expressão :"NFS-e Substituída".

Na visão de movimentos filtre o movimento referente a NFCom que será substituída e selecione-o. Dispare o Processo de Cópia de Movimento a partir de outro Movimento. Ao ser apresentado o novo Movimento para edição preencha o campo com o número do movimento referente à NFCom que será substituída. Em seguida faça as outras alterações no movimento que levaram ao processo de substituição da NFCom anteriormente emitida e salve o movimento. Proceda normalmente com o Processo de Geração/Transmissão da NFCom.

O registro da  NFCom enviada ficará com o  status Pendente e o da NFCom substituída será alterado para Cancelamento Pendente. Espere o tempo de processamento da NFCom substituta e consulte-a. Se a prefeitura acatar o pedido esta NFCom terá seu status alterado para Autorizada, a NFCom substituída terá seu status alterado para Cancelada e o movimento referente a ela será automaticamente cancelado.

Caso o pedido de substituição não seja acatado a NFCom Substituta terá seu status alterado para Rejeitado e a NFCom substituída terá seu status retornado para Autorizada. Nada acontecerá com o movimento a ela relacionado.

***Atenção!* Este processo só pode ser executado para NFCom que estejam Autorizadas.**
