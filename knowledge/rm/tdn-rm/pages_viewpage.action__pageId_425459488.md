---
content_hash: 127004d0265d1531c134785039c6837b3023ee8d30adb2bf4c4ff9e4c791b8bc
fetched_at: '2026-06-29T00:09:36.258317+00:00'
page_id: '425459488'
product: rm
source: tdn-rm
title: Enterprise Service Bus (ESB)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459488
version: 2
---

**Enterprise Service Bus (ESB)**

---

Alguns pacotes de integração utilizam o ESB na sua arquitetura, ficando nestes casos obrigatória a instalação do ByYou ESB.  
 A Integração TOTVS prevê que os módulos integrados não sejam alterados, sendo que o TOTVS Business Conector integra de forma nativa os módulos RM (Data Servers).

* **Comunicação Síncrona com ESB:**

A Aplicação Origem irá disponibilizar uma mensagem XML via Adapter de Envio para o Web Service (WS) no ByYou ESB. O ByYou ESB tem a responsabilidade de receber a mensagem (XML), transformar (XSL) no formato esperado pelo destinatário e enviá-la a um Web Service no destinatário, aguardando retorno que deve ser devolvido à origem.

* **Comunicação Assíncrona com ESB:**

A Aplicação Origem irá disponibilizar uma mensagem XML via Adapter Envio para uma Fila (Banco de Dados). A Fila será lida por um Agente que enviará a mensagem para o Web Service (WS) no ByYou ESB. O ByYou ESB irá receber a mensagem (XML), transformar (XSL) no formato esperado pelo destinatário e enviá-la a um Web Service no destinatário.   
    
 A mensagem será armazenada em uma Fila (Banco de Dados) no Destino. A Fila será lida por um Agente Recebimento que enviará a mensagem para o Adapter Recebimento (Destino).O Adapter Recebimento será responsável por ler e interpretar as mensagens e processar os dados na Aplicação Destino.
