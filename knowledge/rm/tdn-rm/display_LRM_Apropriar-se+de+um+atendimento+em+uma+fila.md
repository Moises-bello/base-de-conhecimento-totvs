---
content_hash: 7d1652a06ff936c8fc4bb84ff9c97b2ae6c5d19acef63ed73e374717f9b91976
fetched_at: '2026-06-29T00:09:37.177630+00:00'
page_id: '425459573'
product: rm
source: tdn-rm
title: Apropriar-se de um atendimento em uma fila
type: documentation
url: https://tdn.totvs.com/display/LRM/Apropriar-se+de+um+atendimento+em+uma+fila
version: 6
---

O processo de pegar um atendimento na fila irá checar se aquele atendimento está na fila, e se aquele atendente tem permissão para se apropriar dele, ou seja, está inserido no grupo de atendentes com tipo de repasse "Para uma fila". Teremos nesses casos as situações:   
Atendimento que não está em nenhuma fila.  
Atendimento que está na fila e atendente não tem permissão para se apropriar dele.  
Atendimento que está na fila e atendente tem permissão para se apropriar dele.  
Para cada caso será exibida uma mensagem informando ao usuário a situação após execução do processo.

Atenção

A partir da versão 12.1.23 o sistema permite a utilização do parâmetro " Atendente destino será o novo responsável pelo contato com o cliente" (Similar ao que já existe no avanço de etapas e repasse de atendimento).

Este parâmetro permite que o usuário que apropria - se de um atendimento que esta na fila possa ser ou não ser o contato direto do atendimento.

Exemplo:

Usuário Mestre criou um atendimento e ele é o contato do atendimento.

Ao avançar o atendimento para fila o sistema permite que outro usuário do grupo de atendentes apropriar- se do atendimento na fila habilitando um parâmetro que define se ele vai ser ou não não o responsável pelo contato.
