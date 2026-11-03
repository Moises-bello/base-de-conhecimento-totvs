---
content_hash: 41195dc25ed4f381841b6beb959ac16a1adb3ebfadebe49b7bc0a9044a0fe4cd
fetched_at: '2026-06-28T21:35:31.864043+00:00'
page_id: '993701480'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Eventos de processos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=993701480
version: 24
---

Consulte a documentação correta:

Esta documentação refere-se ao Editor de processo atual da plataforma. Caso esteja utilizando o Editor de processo clássico, acesse ,  e .

5.\*ndice

# Falando de eventos de processos...

---

Os eventos de processo representam algo que acontece – em contraste a algo que é feito, como uma tarefa, por exemplo. Eles podem ter diferentes significados e comportamentos, dependendo do seu tipo e do momento em que ocorrem no processo. Aqui são listados diversos eventos, desde os iniciais, os que ocorrem ao longo do processo até os finais.

Clique em cada evento para obter informações mais detalhadas sobre eles.

## Eventos iniciais

---

#ebecf05%

 

95%

Representa a etapa inicial do processo, onde o fluxo começa e a solicitação é iniciada.

#ebecf05%95%

**Temporizador (evento inicial)1**Abre solicitações do processo de forma recorrente considerando um período de tempo definido.

#ebecf05%

 

95%

**Sinal (evento inicial)1**  
Recebe um sinal emitido por atividades de envio de sinal e abre uma solicitação do processo.

#ebecf05%

 

95%

**Múltiplo (evento inicial)1**Monitora periodicamente condições e *scripts* condicionais e abre uma solicitação sempre que um sinal é recebido ou uma condição é atendida.

#ebecf05%

 

95%

**Condicional (evento inicial)1**Abre uma solicitação do processo sempre que um *script* condicional é atendido dentro de um período de tempo definido.

## Eventos intermediários

---

#ebecf05%95%

Permite tratar exceções que podem ocorrer na execução de uma atividade de serviço automatizada.

#ebecf05%95%

Permite pausar o fluxo do processo até que uma condição de tempo seja atingida.

#ebecf05%95%

**Intermediário1**Evento que ocorre entre o início e o fim do processo e funciona como uma atividade comum.

#ebecf05%95%

**Sinal (evento intermediário de recebimento)1**Mantém a solicitação parada nesse ponto até receber um sinal emitido por outra atividade de envio de sinal.

#ebecf05%95%

**Sinal (evento intermediário de envio)1**Emite um sinal assim que a solicitação chega nesse ponto e movimenta a solicitação imediatamente para a próxima etapa.

#ebecf05%95%

**Múltiplo (evento intermediário)1**Emite múltiplos sinais e executa múltiplos *scripts* condicionais quando a solicitação chega nesse ponto do processo.

#ebecf05%95%

**Condicional (evento intermediário)1**Cria uma atividade que será responsável por executar um *script* condicional periodicamente.

## Eventos finais

---

#ebecf05%

 

95%

Representa o cancelamento da solicitação.

#ebecf05%

 

95%

Representa o fim do processo, onde o fluxo em questão termina e a solicitação é finalizada.

#ebecf05%

 

95%

Representa o fim abrupto de todos os possíveis caminhos que o fluxo do processo pode seguir.

#ebecf05%95%

**Captura de erro (evento final)1**Identifica e indica que a solicitação foi finalizada com um erro do ponto de vista de negócio.

#ebecf05%

 

95%

**Sinal (evento final)1**  
Emite um sinal que pode ser captado por atividades de recepção de sinal em outros processos quando a solicitação é finalizada.

#ebecf05%

 

95%

**Múltiplo (evento final)1**Emite múltiplos sinais e executa múltiplos *scripts* condicionais depois que a solicitação é finalizada, funcionando como um pós processamento.

**1** → Esse evento somente é exibido em processos que o utilizam criados e exportados do Fluig Studio. No Editor de processo, ele está disponível apenas para visualização, por isso não é exibido na paleta de componentes. Não é permitido editá-lo, apenas movê-lo ou excluí-lo. A exclusão pode ser desfeita, mas criar outro evento não é possível.

Fique atento!

Esta documentação é válida a partir da atualização **Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.

]]>
