---
content_hash: 7e2edc4e3ed454da35bc83f9a720e337fbe705d2e7ece4ed16ce0407984e3e86
fetched_at: '2026-06-29T00:10:10.484549+00:00'
page_id: '452719850'
product: rm
source: tdn-rm
title: Fila de Eventos
type: documentation
url: https://tdn.totvs.com/display/LRM/Fila+de+Eventos
version: 7
---

Através da fila de eventos será possível monitorar os registros dos Eventos gerados pelos gatilhos, bem como seus status. Após a geração do XML ao editar os registros, poderá identificar informações como: o Tipo de Evento, o Status, o Tipo de Operação, e o cadastro a que ele se refere, além de erros de geração e informações da integração com TAF/TSS.

**Observações:**

* Caso o gatilho seja incluído de forma manual na fila de eventos, a informação "Evento inserido manualmente" ficará destacada na tela do cadastro.
* Para os eventos **rejeitados pelo Governo**, o detalhamento da possível inconsistência poderá ser verificada na aba "Erros de integração" ao editar o registro na Fila de Eventos.
* A partir do registro da fila de eventos é possível
  + Integrar com TAF, Gerar XML,
  + Atualizar Status Integração TAF,
  + Gerar Retificação Arquivo eSocial,
  + Evento de Exclusão (S-3000),
  + Excluir Evento da Fila (Esse processo é IRREVERSÍVEL) e
  + Validar S-1200 com Envelope dos registros selecionados.
* Para a atualização do status de uma grande quantidade de registros, não é recomendável utilizar a Fila de Eventos, deverá utilizar o processo "Atualizar Status Integração TAF" que encontra-se disponível no menu  "eSocial".
* Ao integrar com o TAF o registro S-2230 onde a coluna *Afastamento de Férias =SIM*o sistema irá preencher a coluna *Fora do prazo de envio* conforme parametrização feita no campo abaixo:
* O campo competência ficará habilitado para os eventos de *tabela* que estiverem com os Status **0**- Pendente,**1-** Gerado, **2**Gerado erro, 5-Erro integração com o TAF,6-Rejeitado TAF e 9 Rejeitado RET ,podendo ser alterado caso necessário. Ao alterar o campo mês ou ano o status do evento passa para pendente.
* É possível realizar a atualização do campo “Competência” (início de validade) dos eventos S-1010 de forma automatizada. O objetivo de facilitar a manutenção das informações cadastrais, permitindo alterar simultaneamente o início de validade de múltiplos eventos S-1010.
* Ao migrar para o novo leiaute S-1.0 os eventos que foram excluídos (S-1030, S-1040, S-1050, S-1060, S-1080, S-1250, S-1295, S-1300, S-2221, S-2245, S-2250, S-2260) no leiaute 2.5.00 NT 19/2020 não terão mais disponibilidade de seleção, sendo vistos apenas na opção "Exibir todos".

**Quantidade de dias anterior ao período de gozo de férias para envio do S-2230 (Máx. 60 dias)**
