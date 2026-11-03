---
content_hash: 96865790cf4484a3fbe6f8a3aa97e6124e650777d88fd5dd4376106d594f1091
fetched_at: '2026-06-29T00:09:33.783613+00:00'
page_id: '425459052'
product: rm
source: tdn-rm
title: Serviços TAA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459052
version: 10
---

**Serviços**

---

**Gerar atendimento por grupos de e-mail**

* **Servidor**

O sistema disponibiliza um serviço no qual acessa as caixas postais previamente cadastradas em Grupos de E-mails e, para cada e-mail encontrado cria um atendimento de acordo com as características definidas nesse cadastro. Para que seja possível executar este serviço com sucesso é necessário acessar e ler a caixa postal que fica em um servidor de e-mail. Normalmente servidores de e-mail disponibilizam um protocolo chamado POP3 ou IMAP para que seja possível acessar e ler tais caixas postais. Este parâmetro informa qual é o servidor de e-mail que será utilizado para a o processamento deste serviço. Ele pode ser preenchido com o valor de um IP ou então o nome do servidor. A principal diferença entre os protocolos POP e IMAP é que ao usar o protocolo POP, os e-mails são deletados após serem transformados em atendimento, já o protocolo IMAP não permite que aplicativos deletem e-mail, por isso são transformados em atendimentos todos os e-mails não lidos e em seguidas eles são marcados como lidos. Se em algum momento alguém marcar algum e-mail já transformado em atendimento como não lido e o processo for executado de novo, ele será transformado em atendimento novamente.

* **Porta**

Para garantir a máxima segurança e integridade dos seus dados, nosso serviço **exige** uma conexão direta e criptografada do tipo SSL/TLS.

Isso significa que, ao configurar seu leitor de e-mail, você **deve** utilizar as portas padrão designadas para este tipo de conexão segura, de acordo com o protocolo escolhido:

**Para protocolo POP3:** Use a porta **`995`**

**Para protocolo IMAP:** Use a porta **`993`**

**Atenção:** É importante **não** utilizar as portas de conexão padrão não seguras (`110` para POP3 e `143` para IMAP). Tentativas de conexão nessas portas resultarão em erro, pois nosso sistema, por motivos de segurança, não suporta o mecanismo de criptografia tardia (`STARTTLS`) associado a elas.

**Nota sobre as portas:** As portas `995` e `993` são padrões globais definidos pela IANA (Autoridade para Atribuição de Números da Internet). O uso de uma porta diferente só será necessário caso seu servidor de e-mail tenha uma configuração privada e customizada, conforme orientado pelo seu administrador de TI.

**Importante:**

O Microsoft Exchange não suporta mais a autenticação básica (usuário e senha), então, usuários desse serviço devem configurar a autenticação OAuth 2.0 no cadastro de grupo de e-mails, vide link abaixo para mais detalhes:

   
**Despertar atendimentos**

* **Conclusão Automática de Atendimento**

O processo normal de conclusão de um atendimento seria:

1. Atendimento é encaminhado a outro atendente para avisar ao cliente da solução, processo de "Concluir" (fica com o status de concluído a responder);
2. Atendente entra em contato com o cliente para lhe informar a solução, processo "Concluído respondido" (fica com o status de concluído respondido);
3. O cliente entra em contato com o atendente (ou então o contrário) avisando que a solução informada resolveu o problema, processo "Concluído confirmado" (fica com o status de concluído confirmado).

Pode ocorrer de o atendimento estar concluído respondido e o cliente ultrapassar ao prazo de dias estipulado pela empresa para entrar em contato confirmando a resolução do problema. Neste caso entra em ação o serviço de concluir automático que busca estes atendimentos que foram colocados em concluídos respondidos a X dias e os conclui automaticamente. Este parâmetro significa a quantidade de dias, isto é,  quantos dias os atendimentos podem ficar como "Concluídos Respondidos" antes de serem concluídos automaticamente pelo sistema.

* **Utilizar Data/Hora do Momento da Execução do Serviço**

Utilizado para especificar o horário que o serviço de despertar será executado (recomendável para organizações que trabalham com turnos de funcionários).  
   
**Exemplo 1:**   
Dessa forma quando o serviço de despertar estiver sendo executado, caso o parâmetro esteja marcado ele irá verificar se a data de despertar é menor igual (<=)do que a data corrente ( Data/hora no momento da execução do serviço).  
Data Despertar: 01/04/2011 10:00:00  
Data Corrente: 01/04/2011 09:00:00  <-- Momento em que o serviço foi executado.  
**Exemplo 2:**   
Caso o parâmetro esteja desmarcado o sistema irá verificar se a data de despertar é menor do que a maior data possível de um dia.  
Data Despertar: 01/04/2011 10:00:00  
Data Corrente: 01/04/2011 23:59:59 <- Maior data possível do dia da execução do processo.  
   
**Agendados a responder**

* **Agendados a responder**

No decorrer dos trabalhos com os atendimentos é normal você informar um prazo, que deve ser passado ao cliente, para a resolução do problema/solicitação. Quando isto é realizado o atendimento é encaminhado a outro atendente para que este possa entrar em contato com o cliente, passar o prazo e buscar o aceite deste prazo.  
   
Novamente pode ocorrer do cliente ultrapassar o prazo para enviar o retorno ou então no caso do representante que não informar ao cliente o prazo e por isso o aceite ainda não foi dado. Para evitar esta situação existe um serviço que varre os atendimentos nesta situação, "Agendado a Responder", identifica aqueles que estão a mais de X dias assim e o alteram para "Agendado Respondido", isto é, como se o prazo dado tivesse sido aceito. Este parâmetro é exatamente a quantidade de dias que o sistema deve considerar no momento de avaliar os atendimentos nesta situação e passá-los para agendado respondido.
