---
content_hash: e2f2c6ab44592def7e6233773438adc39b63703dc20213a2f68a9db2e7c44379
fetched_at: '2026-07-02T19:24:26.626968+00:00'
page_id: '553330377'
product: protheus
source: tdn-tec
title: 3 - Funções de Usuário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553330377
version: 15
---

O REST permite que o usuário possa customizar o comportamento padrão conforme lhe convenha.

Veja onde é possível customizar:

true

* **CONTROLE DE THREADS**

  + **OnStart**   
    Permite realizar operações na Inicialização da Thread REST
  + Permite realizar operações na Parada da Thread REST
  + Permite a captura de erros (exception) das Threads
true

* **ATENDIMENTO DE REQUISIÇÕES**

  + Permite bloquear ou ocultar APIs em determinado ambiente REST
  + Permite autorizar ou ocultar APIs em determinado ambiente REST, a demais APIs serão bloqueadas
  + Permite escolher qual Pool Thread irá atender a requisição
  + Permite customizar a autenticação da requisição ao serviço REST
  + **[OnSend](https://tdn.totvs.com/display/tec/onSend)**  
    Permite a centralização do tratamento de todas as mensagens de resposta do REST
