---
content_hash: 938df22af70baafd817da204d18ef9d0b2ff1bce1b7be251a1156ba52e05e22d
fetched_at: '2026-06-29T00:09:25.260597+00:00'
page_id: '423938086'
product: rm
source: tdn-rm
title: Enviar Evento MDF-e
type: documentation
url: https://tdn.totvs.com/display/LRM/Enviar+Evento+MDF-e
version: 5
---

Opção existente para armazenar informações sobre o histórico de envio de eventos de um MDF-e existente. No processo de envio do MDF-e, podemos adotar três situações sendo elas:

**Cancelamento**: O MDF-e só poderá ser cancelado dentro do prazo de 24 horas após autorizado, ainda não tenha ocorrido o início do transporte e o texto do motivo deverá ter no mínimo 15 caracteres.   
O processo irá chamar o TSS, passando os parâmetros específicos para o Cancelamento.   
Após a execução o ERP automaticamente irá alterar o status do MDF-e para "Evento Pendente".

**Encerramento**: Entende-se como encerramento do MDF-e o ato de informar ao fisco, esse evento, através de Web Service de registro de eventos o fim de sua vigência, que poderá ocorrer pelo término do trajeto acobertado ou pela alteração das informações do MDF-e através da emissão de um novo.   
O processo irá chamar o método do TSS de Envio de Evento, passando os parâmetros específicos para o Encerramento da MDF-e.   
Após a execução o ERP automaticamente irá alterar o status do MDF-e para "Evento Pendente".

**Inclusão de Condutor**: Para cada MDF-e deverá ter um condutor já cadastrado no movimento de origem.   
Assim como as informações do veículo, da carga, valor, remetente, destinatário, e outros dados.   
Caso aconteça algo específico e seja necessário alterar este condutor (motorista) o processo servirá para tal ocasião.   
O processo irá chamar o método do TSS de Envio de Evento, passando os parâmetros específicos para a inclusão do novo condutor.  
Após a execução o ERP automaticamente irá alterar o status do MDF-e para "Evento Pendente".
