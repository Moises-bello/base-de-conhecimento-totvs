---
content_hash: 6aea2215c80095df7b7604414630ec52516ce036e1fbbe323d506298c5b347f0
fetched_at: '2026-06-29T00:09:20.967768+00:00'
page_id: '422545750'
product: rm
source: tdn-rm
title: Evento NFC-e (Envio e Consulta)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545750
version: 5
---

Este tipo de evento será utilizado quando ocorrer algum erro de emissão na NFC-e ou no caso de cancelamento.   
Para emitir um cancelamento basta acessar o [TOTVS Gestão de Estoque, Compras e Faturamento](http://tdn.totvs.com/pages/viewpage.action?pageId=198948835). No menu Vendas | Faturamento | SPED NF-e (Estadual) selecione a NFC-e autorizada que irá ser cancelada. No botão Processos escolha a opção Envio de Evento. Escolha o tipo de evento Cancelamento de NF-e/NFC-e. Informe o texto da correção desejada. Este texto é obrigatório e o botão de envio só é habilitado após o mesmo ser digitado com um mínimo de 15 caracteres. Dispare o evento e aguarde o final do processo para verificar se o envio do evento foi bem sucedido ou não.  
 Após o envio, aguarde alguns minutos selecione novamente o registro da NFC-e para a qual foi enviada o cancelamento. No menu Processos selecione Consulta Eventos. Desta forma o cancelamento processado pela SEFAZ será retornado para o [TOTVS Gestão de Estoque, Compras e Faturamento](http://tdn.totvs.com/pages/viewpage.action?pageId=198948835).  
 Após este tipo de evento ser consultado caso seja autorizado a NFC-e terá seu status alterado para Cancelado e o movimento que a originou será automaticamente cancelado. Se o evento de cancelamento for rejeitado pela SEFAZ a NFC-e terá seu status retornado para Autorizada e nada acontecerá com o movimento que a originou.

**Atenção!**: O cancelamento só pode ser feito dentro de um determinado tempo. A SEFAZ deve ser consultada para saber qual o correto período no qual este tipo de evento pode ser enviado.
