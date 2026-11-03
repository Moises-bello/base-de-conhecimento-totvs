---
content_hash: 21fd2e7bab8e46634036c4166b4dd7dec2a9f834e842ee768c30bfd03b19416b
fetched_at: '2026-06-28T21:35:19.251292+00:00'
page_id: '200906235'
product: fluig
source: tdn-fluig
title: Eventos de Notificação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=200906235
version: 17
---

# Índice

true.\*ndicenone

# Objetivo

---

Neste guia será apresentada a configuração de um *widget* desenvolvido sobre a plataforma e um evento de notificação.

# Pré-requisitos

---

Conhecimento prévio em determinados pontos, sendo estes:

* Visão geral sobre a plataforma fluig

# Eventos

---

No repositório [samples](http://git.fluig.com/projects/SAMPLES) está disponível o [sample-notification-event](https://git.fluig.com/projects/SAMPLES/repos/projetos/browse/event-notification) que contém o projeto [poster-custom-priority](https://git.fluig.com/projects/SAMPLES/repos/projetos/browse/event-notification/poster-custom-priority).

Esse projeto disponibiliza um *widget* desenvolvido sobre a plataforma para postagem, definindo a notificação, um *dataset* personalizado que é utilizado no *widget* e um evento *beforeSendNotification* que considera o campo metadata da notificação para definir a nova prioridade da notificação.

Vale observar que a notificação não tem sua prioridade alterada automaticamente apenas enviando um parâmetro no *customData*, é preciso personalizar o evento *beforeSendNotification* para isso.

## Passos de implementação

---

A seguir são apresentados os passos para implementar essa customização:

0.5falsesamplesfadetrue1Passo 1

* Faça o *download* do projeto [poster-custom-priority](https://git.fluig.com/projects/SAMPLES/repos/projetos/browse/event-notification/poster-custom-priority).

**Figura 1 - *Download* do projeto**

2Passo 2

* Importe o projeto para o TDS.

**Figura 2 - Importação do projeto**

3Passo 3

* Exporte o evento *beforeSendNotification*.

**Figura 3 - Exportação do evento**

4Passo 4

* Exporte o *dataset* comunidadesPoster.  
  Obs.: o nome do *dataset* na exportação deve ser **comunidadesPoster**.

**Figura 4 - Exportação do *dataset***

5Passo 5

* Exporte o *widget* **custom\_poster**.   
  Obs.: o **custom\_poster** não é uma extensão da *socialposter*.

**Figura 5 - Exportação do *widget***

6Passo 6

* Edite a página de uma comunidade e adicione o **custom\_poster** nela, removendo o *widget* de publicação antiga.

**Figura 6 - Inclusão do *widget* na página**

7Passo 7

* Realize uma publicação selecionando a prioridade **Não enviar**.   
  Obs.: nesse caso não deve ser gerada nenhuma notificação, caso a prioridade escolhida seja alta, é possível verificar pela [API pública](http://api.fluig.com/resource_AlertServiceRest.html#path__alert_service_findAll.html) se a prioridade foi alterada.

**Figura 7 - Nova publicação**
