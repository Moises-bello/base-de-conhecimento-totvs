---
content_hash: 608fb5ece980f53e9013819a40af1c1eb1573ca01c14e2e6896be0dcf5649949
fetched_at: '2026-06-29T00:05:54.272267+00:00'
page_id: '1077772795'
product: rm
source: tdn-rm
title: PI - Integração - RD Station - Status do Lead
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1077772795
version: 2
---

### **Motivo de desistência, alterando o Status do Lead no rd station:**

---

É possível que o SDR informe o motivo de desistência de uma proposta (no menu de interesse) e neste momento o RD Station irá atualizar o status deste Lead.

Estágio do Funil: **Cliente**

Observe que foi informado um interesse que possui uma situação de desistência (Perdido). Neste momento o sistema irá atualizar o estágio do funil deste cliente no RD STATION.

Estágio do Funil atualizado para Lead, e foi desmarcada a opção **Marcar oportunidade.**

Observação

Caso este Lead já possua uma proposta gerada para o Backoffice, o mesmo terá seu status alterado para **Cliente** (como visualizamos acima).  
Nesta condição, ao acessar a GUIA interesses (não será possível alterar uma **situação de Interesse para o Status PERDIDO.**Caso o usuário teste realizar esta ação o sistema retornará a seguinte mensagem:

**Interesse do cliente fica como "Perdido" no PI (Modelo Novo)**

Quando um cliente (Lead) é atendido no PI, pode acontecer de ele não seguir com a compra naquele momento. Nesses casos, o interesse dele pode ser marcado como "Perdido", e o Lead vai para o Banco de Leads.  
Mas se esse cliente voltar a demonstrar interesse e for marcado novamente como Oportunidade no RD Station, é importante entender o que deve ser feito no PI para retomar o atendimento.

Comportamento no sistema, na prática:

 1. O Lead entra no sistema PI

* O cliente é captado no RD Station.
* Quando é marcado como Oportunidade, ele entra automaticamente no fluxo de atendimento do PI.

2. Interesse é marcado como Perdido

* No PI, você acessa o cadastro do cliente.
* Vai na aba Interesse e preenche:

  + Situação: Perdido
  + Motivo: por exemplo, Preço Alto

* O sistema entende que aquele cliente não quer mais comprar.
* Resultado: o cliente é movido para o Banco de Leads, saindo do atendimento ativo.

 3. Cliente volta a demonstrar interesse no RD

* No RD Station, o cliente é marcado novamente como Oportunidade.

Importante: O que acontece nesse momento?

* O cliente sai do Banco de Leads e vai para em atendimento:
* Ele volta sozinho para o atendimento no PI.
* Toda vez que um lead já **existente em banco** manifesta novo interesse, é registrada uma anotação (timeline) com o nome do empreendimento e da mídia de origem.
