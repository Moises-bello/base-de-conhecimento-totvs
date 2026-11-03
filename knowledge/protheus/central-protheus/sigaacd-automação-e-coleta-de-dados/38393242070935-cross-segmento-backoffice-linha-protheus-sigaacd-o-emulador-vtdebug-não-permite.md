---
article_id: 38393242070935
category: SIGAACD - Automação e Coleta de Dados
content_hash: ac1881dddd7a863ebd45a48da0061528efa14dccd2f168a53f0c0068510b058b
fetched_at: '2026-06-28T22:39:12.881135+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - O emulador VTDEBUG
  não permite realizar a leitura das mensagens de erros.
type: support-article
updated_at: '2026-02-20T13:56:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38393242070935-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-O-emulador-VTDEBUG-n%C3%A3o-permite-realizar-a-leitura-das-mensagens-de-erros
---

O VTDebug é uma ferramenta de depuração para simular problemas do VT100, mas possui limitações, como não permitir a leitura de mensagens de erro ou códigos de barras, pois não interpreta entradas contínuas de caracteres, apenas simula eventos de teclado individuais, diferindo do terminal físico VT100.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38393235555735) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
O emulador VTDEBUG não permite realizar a leitura das mensagens de erros, porque?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**

O **VTDebug** é uma ferramenta de depuração que simula o terminal VT100, mas com escopo limitado. Diferente de um terminal real, ele não aceita entrada direta de caracteres em objetos de interface (como o **TGet**).

**Por que certas funções não funcionam?**

* **Baseado em Eventos de Teclado**: O funcionamento depende exclusivamente da simulação do pressionamento individual de cada tecla.
* **Leitura de Código de Barras**: Como leitores enviam strings contínuas e automáticas (sem disparar eventos de tecla individualmente), o VTDebug não consegue interpretar a entrada.
* **VTAlert**: Sofre da mesma limitação por depender desse modelo de eventos manuais.

O **VTDebug** foi projetado para **simular teclas para debug**, e não para reproduzir a entrada contínua de dados de um terminal físico.

**Como aparecer as mensagens no emulador VTDEBUG?**

* Para simulação dos erros no emulador, pode ser usado Software para Compartilhamento de Tela.
* Exemplos **AnyDesk**, **TeamViewer** e **Samsung Flow** ou aplicativo indicado pelo fabricante do coletor que o usuário possua para espelhamento do coletor num Computador/Desktop.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)

[VTDebug - Limitações](https://tdn.totvs.com/pages/releaseview.action?pageId=561064716)
