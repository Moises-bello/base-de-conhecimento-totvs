---
content_hash: 3e08ef32c339102cf8f190a36b7950d3bfce63076e1a1fac08e1fed13356d8cd
fetched_at: '2026-06-29T00:09:30.339514+00:00'
page_id: '425458432'
product: rm
source: tdn-rm
title: Expediente
type: documentation
url: https://tdn.totvs.com/display/LRM/Expediente
version: 1
---

**Expediente**

---

**Horário de expediente**   
   
Estes parâmetros indicam o horário fixo em que os atendentes da empresa trabalham. É possível criar horários personalizados por atendente e também efetuar uma integração com o sistema de ponto eletrônico para identificar se o atendente se encontra na empresa, e disponível para o trabalho, ou não.  
   
Este horário de expediente (ou por atendente ou on-line) é o que será utilizado para identificar se o atendente está no período de trabalho para receber um repasse de atendimento e para calcular o tempo útil que um atendimento permaneceu com um atendente.  
   
   
**Horário de atendimento eletrônico**  
   
Como o sistema se trata de um módulo de gestão de relacionamento com o cliente e nestes casos pode haver um sistema eletrônico de atendimento integrado com URA's, este conjunto de parâmetros é utilizado para delimitar os horários de funcionamento de tal sistema eletrônico, isto é, que os atendentes estão disponíveis para atender os clientes por telefone.  
   
No caso destas integrações a URA deve ser capaz de ler tais parâmetros e validá-los informando uma mensagem característica, geralmente uma gravação de voz, informando o horário de funcionamento do serviço. Também há uma série de WebServices que já realiza tal validação do horário de funcionamento observando tais parâmetros retornando apenas verdadeiro ou falso com relação a "está dentro do horário de atendimento?".
