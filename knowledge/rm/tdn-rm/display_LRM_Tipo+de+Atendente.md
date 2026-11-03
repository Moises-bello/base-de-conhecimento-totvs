---
content_hash: ee2ff98406f79de6bea0ce6951af2b0209498c65c81f4d2d0a57bf7a04a73796
fetched_at: '2026-06-29T00:09:33.428478+00:00'
page_id: '425459023'
product: rm
source: tdn-rm
title: Tipo de Atendente
type: documentation
url: https://tdn.totvs.com/display/LRM/Tipo+de+Atendente
version: 1
---

**Tipo de Atendente**   
Nesta opção cadastra-se a tabela de tipo de atendente.   
   
Através do cadastro é possível controlar:  
   
**Identificação**   
Nesta pasta, serão informados os dados que identificarão o tipo de atendente cadastrado.  
Descrição do tipo de atendente:  
Preencha neste campo a identificação/ nome do tipo de atendente.   
Peso de alarme:  
Preencha neste campo o número correspondente ao peso do alarme para o tipo de atendente que está sendo cadastrado.  
Ao calcular o disparo do alarme de uma ocorrência, o sistema verifica várias situações, inclusive o peso de alarme do tipo de atendente. Este campo é um multiplicador que define o prazo que o atendente possui para resolver um atendimento sem que o mesmo alarme. Você pode definir um peso que prolongue o prazo ou um que diminua de acordo com o tipo de atendente.   
Código da Setença SQL: Preencha este campo com a setença sql desejada para personalização da tela de visão de atendimentos. Através desse vínculo, os campos desejados na tela serão apresentados conforme a real necessidade. Lembrando que este procedimento pode ser realizado através dos parâmetros do sistema e caso as opções não estejam definidas a visão de atendimentos será apresentada de forma padrão.   
Exemplo  
O atendente Antônio Braga está vinculado ao tipo de atendente "Técnicos".   
Como este tipo de atendente precisa de mais tempo para analisar as solicitações das ocorrências, foi definido que o tipo de atendente "Técnicos" possui peso de alarme 2.   
A atendente Beatriz Menga está vinculada ao tipo de atendente "Administração".   
Como este tipo de atendente não precisa de muito tempo para analisar as solicitações das ocorrências, foi definido que o tipo de atendente "Administração" possui peso de alarme 1.  
Nos parâmetros de alarme do RM Agilis está definido o seguinte:  
Status: Em Andamento   
Classificação: ERRO  
Prioridade: Urgente  
Condição 1: Número máximo de horas/ minutos em aberto com o responsável atual: 8  
Condição 2: Tempo máximo de resposta (em horas/ minutos desde a data de abertura): 16  
Ou seja, os atendimentos que possuem as características acima, vão alarmar dentro de um prazo máximo de 8 ou 16 horas, dependendo da condição que se encontram.   
Tanto a atendente Beatriz quanto o atendente Antônio possuem atendimentos pendentes em sua responsabilidade. Alguns destes atendimentos possuem as seguintes características:  
Status: Em Andamento   
Classificação: ERRO  
Prioridade: Urgente  
Neste caso, observando o parâmetro de alarme, os atendimentos que se encontram com os atendentes citados acima, vão alarmar dentro de um período de tempo.   
Para o atendente Antônio, como o mesmo pertence a um tipo que está definido com o peso de alarme = 2, o sistema realiza o seguinte cálculo para disparar o alarme:  
Condição 1 => 2 x 8 = 16 horas   
Condição 2 => 2 x 16 = 32 horas  
Ou seja, o Antônio possui 16 ou 32 horas (dependendo da condição) para resolver o atendimento antes que o mesmo alarme.   
Para a atendente Beatriz, como a mesma pertence a um tipo que está definido com o peso de alarme = 1, o sistema realiza o seguinte cálculo para disparar o alarme:  
Condição 1 => 1 x 8 = 8 horas   
Condição 2 => 1 x 16 = 16 horas  
Ou seja, a Beatriz possui 8 ou 16 horas (dependendo da condição) para resolver o atendimento antes que o mesmo alarme.  
   
**Observação**  
Caso não seja definido um peso de alarme para o tipo de atendente ou um atendente não estiver vinculado a um tipo, o sistema calcula o prazo para disparo de alarme das ocorrências de acordo com os parâmetros de alarme definidos em: Opções | Parâmetros | RM Agilis | Alarmes.   
Dica  
Para vincular um atendente a um tipo, acesse: Cadastros | Atendentes | Atendentes | Identificação e selecione o tipo correspondente ao atendente em questão.   
**Atenção**  
O peso de alarme quando é definido com um valor abaixo de 0, o sistema diminui o prazo limite para disparo do alarme, pois o mesmo é um multiplicador.
