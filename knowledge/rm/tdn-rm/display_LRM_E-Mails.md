---
content_hash: 834fed1eb9d32dc3e3ded5ce86371e4e63edd96f778c9bf43d76cc1726d89fa5
fetched_at: '2026-06-29T00:09:34.002670+00:00'
page_id: '425459109'
product: rm
source: tdn-rm
title: E-Mails
type: documentation
url: https://tdn.totvs.com/display/LRM/E-Mails
version: 10
---

**E-Mails**

---

**Abertura de E-mail**  
   
Caso não possua e-mail personalizado no tipo do atendimento para abertura de atendimentos, o sistema busca deste parâmetro o modelo de e-mail. Se o parâmetro estiver vazio, o modelo de e-mail utilizado será o fixo do sistema.  
   
**Repasse de Atendimento**  
   
Caso não possua e-mail personalizado no tipo do atendimento para repasse de atendimentos, o sistema busca deste parâmetro o modelo de e-mail. Se o parâmetro estiver vazio, o modelo de e-mail utilizado será o fixo do sistema.  
   
**Concluído Respondido**  
   
Caso não possua e-mail personalizado no tipo do atendimento para atendimentos que foram concluídos respondidos, o sistema busca deste parâmetro o modelo de e-mail. Se o parâmetro estiver vazio, o modelo de e-mail utilizado será o fixo do sistema.  
   
**E-mail enviado por dentro do atendimento**  
   
Permite personalizar os e-mails enviados sobre o atendimento através de relatórios globais pré-cadastrados. Caso não possua este parâmetro preenchido, o sistema busca o modelo fixo do sistema.

**Origem do e-mail do atendente**

Neste parâmetro se definido **Pessoa** será enviado e-mail para o e-mail informado no cadastro da pessoa vinculada ao atendente. Se não houver nenhum e-mail informado no cadastro da pessoa, não será enviado o e-mail ao atendente.

Caso seja escolhida a opção **Usuário** será enviado e-mail para o e-mail informado no cadastro do usuário. Se não houver nenhum e-mail informado no cadastro do usuário, não será enviado e-mail ao atendente.

   
**From Name dos E-mails gerados pelo sistema**  
   
**Endereço eletrônico do suporte (E-mail do Suporte)**  
   
Existem alguns serviços do sistema (alarmar atendimentos, entendimento do atendimento, entre outros) que enviam e-mails para atendente(s)/usuário(s)  e estes são enviados não tendo como remetente um atendente(s)/usuário(s) específico(s), as vezes por serem serviços automáticos e outras vezes por regras de manter oculto tais atendentes. Como os serviços de envio de e-mails exigem um remetente para se enviar um e-mail então este parâmetro vem suprir esta necessidade que é utilizado como remetente de envio de e-mails destes serviços. O valor deve ser um endereço de e-mail válido.  
   
**Caixa postal para mensagens enviadas ao cliente**  
   
Para segurança da empresa e até mesmo para auditorias é interessante que os e-mails de conclusão de atendimento e de entendimento, sejam enviados ao cliente (caso seja parametrizado) e que possuam cópias registradas. Este parâmetro é um endereço de e-mail para onde tais e-mails são enviados no esquema de cópia oculta.  
   
   
**Enviar e-mails de notificações no formato texto**   
   
Em vários momentos, de acordo com algumas ações, o sistema monta e dispara e-mails (quando atendimento é concluído, cancelado, repassado (Avançar etapa), alarmado, entre outros) a serem enviados (imediatamente e/ou posteriormente). Por padrão tais e-mails são montados no formato HTML. Este parâmetro tem a função de informar ao sistema para que os e-mails sejam montados como um texto simples (texto) e não mais no formato HTML.  
   
**Enviar email para cliente na conclusão do atendimento**  
   
Na conclusão de atendimentos o sistema possui a opção de enviar um e-mail para o cliente a fim de avisá-lo da conclusão do atendimento. Este e-mail contém algumas informações sobre o atendimento e também é um dos tipos de e-mail que podem ser customizados (através de um relatório e associação deste relatório ao parâmetro adequado) de acordo com a necessidade do cliente. Este parâmetro indica ao sistema se tal e-mail será enviado ou não. Lembrando que este parâmetro trabalha em conjunto com o parâmetro "Caixa Postal para reply do cliente em caso de não concordar com a solução do atendimento" onde este deve estar preenchido com um endereço de e-mail válido e o parâmetro "Enviar email para cliente na conclusão do atendimento" deve estar marcado para que o e-mail ao cliente de conclusão do atendimento seja enviado.   
   
**E-Mail de repasse exibir texto completo da solicitação**  
   
Os e-mails de repasses enviados pelo sistema contêm várias informações e entre elas está o texto com a solicitação do atendimento. Este parâmetro interfere em como o texto será apresentado no sentido de apresentar o texto inteiro ou então somente os primeiros 500 caracteres da solicitação.  
   
   
**E-Mail de repasse exibir texto completo da discussão**  
   
Os e-mails de repasses enviados pelo sistema contêm várias informações e entre elas está o texto com a discussão sobre ponderações, dúvidas, informações sobre a solicitação do atendimento. Normalmente são apresentados somente as últimas 7(sete) discussões que foram inseridas no atendimento. Este parâmetro modifica tal comportamento no sentido de montar o e-mail de repasse com o texto inteiro que consta na discussão do atendimento.
