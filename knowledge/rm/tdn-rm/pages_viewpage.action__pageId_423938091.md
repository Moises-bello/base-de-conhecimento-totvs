---
content_hash: 8a34097be9e3e5ba7def10dc85ddacfc5b58518bd2fecac46411c2d086a98733
fetched_at: '2026-06-29T00:09:25.269680+00:00'
page_id: '423938091'
product: rm
source: tdn-rm
title: Enviar Evento MDF-e (Neogrid)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938091
version: 6
---

No processo do envio de evento MDF-e podemos adotar três situações que são elas:

**Cancelamento**: O MDF-e só poderá ser cancelado dentro do prazo de 24 horas após autorizado, ainda não tenha ocorrido o início do transporte e o texto do motivo deverá ter no mínimo 15 caracteres. O processo irá chamar o Client Neogrid, passando os parâmetros específicos para o Cancelamento.

Após a execução o ERP automaticamente irá alterar o status do MDF-e para "Evento Pendente".

**Encerramento**: Entende-se como encerramento do MDF-e o ato de informar ao fisco, esse evento, através de Web Service de registro de eventos o fim de sua vigência, que poderá ocorrer pelo término do trajeto acobertado ou pela alteração das informações do MDF-e através da emissão de um novo.   
O processo irá chamar o método do Client Neogrid de Envio de Evento, passando os parâmetros específicos para o Encerramento da MDF-e.   
Após a execução o ERP automaticamente irá alterar o status do MDF-e para "Evento Pendente".

**Inclusão de Condutor**: Para cada MDF-e deverá ter um condutor já cadastrado no movimento de origem.   
Assim como as informações do veículo, da carga, valor, remetente, destinatário, e outros dados.   
Caso aconteça algo específico e seja necessário alterar este condutor (motorista) o processo servirá para tal ocasião.   
O processo irá chamar o método do Client Neogrid de Envio de Evento, passando os parâmetros específicos para a inclusão do novo condutor.   
Após a execução o ERP automaticamente irá alterar o status do MDF-e para "Evento Pendente".  
Pode se concluir que, após o envio será disponibilizado o XML do evento na pasta "SENT" do WebEDI, caso o Client Neogrid esteja desligado, o XML irá para a pasta "OUT", sendo assim, ao ligar o Client, ele irá enviar para a Neogrid os XMLs que estão nesta pasta e a Neogrid enviará para a SEFAZ validar.

* # [Monitor de Arquivos XML](http://tdn.totvs.com/display/LRM/Monitor+de+Arquivos+XML)
* # [Enviar MDF-e](http://tdn.totvs.com/pages/viewpage.action?pageId=423938105)
