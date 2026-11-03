---
content_hash: b4d5a24206c8958768cd19c8b648874ab927bffbab409853c6be56dbbcafdfd4
fetched_at: '2026-06-29T00:09:02.915997+00:00'
page_id: '381028800'
product: rm
source: tdn-rm
title: Acerto de Jornadas
type: documentation
url: https://tdn.totvs.com/display/LRM/Acerto+de+Jornadas
version: 12
---

**Atenção!**

Este processo ficará visível somente quando na coligada existir um horário na condição abaixo:

O horário possui duas jornadas com mesmo índice.

O sistema gerou na fila de eventos um gatilho para o evento S-1050 contendo 4 índices, sendo o correto 5 índices. Portanto, deverá ser realizado o processo de acerto de jornadas.

### Alerta sobre a condição do horário

Na fila de eventos após selecionar o evento S-1050 e Gerar o XML, será demonstrada uma mensagem de Aviso para o usuário conforme segue:

### Procedimentos para geração do Acerto de Jornadas

Para geração selecione: eSocial | Outros processos| Acerto de Jornadas.

Selecione Sim ou Não para a mensagem apresentada: "Este processo irá realizar o acerto de jornadas para o evento S-1050 na geração de XML. Deseja prosseguir com a execução?"

No final do processo será demonstrada a mensagem: "A execução do processo foi concluída com sucesso".

Na fila de eventos será visualizado os gatilhos conforme a jornada do horário.

### Reforçamos que após execução do processo, a opção "eSocial | Outros Processos | Acerto de Jornadas" não será mais exibida.

**Dicas Importantes:**

* Após realizar o acerto da Jornada e o status do XML S-1050 estiver acima de 3, o sistema irá gerar um gatilho do evento S-2206

O processo “Acerto de Jornadas”  irá gerar gatilho na fila de eventos  para os eventos S-1050 e S-2206 .  
  
  
**Exemplo dos gatilhos gerados:**

**a) Evento S-1050 com status 3-Enviado para TAF:**

* Serão gerados (02) dois gatilhos na fila de eventos (um com tipo da operação "Alteração" e o outro "Inclusão").
* Para os funcionários vinculados ao horário será gerado gatilho na fila de eventos para o evento S-2206 com tipo da operação "Alteração".

**b) Evento S-1050 com Status 1-Gerado :**

* O sistema irá re-gerar os gatilhos na fila de eventos e os índices a serem ajustados serão visualizados com status "Pendente".
