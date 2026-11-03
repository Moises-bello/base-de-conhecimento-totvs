---
article_id: 13266931373335
category: Portal
content_hash: 30f3b418317df395aeccce3454a420ecd6dd025ec6ef48d1ff58c4555aa94494
fetched_at: '2026-06-28T22:46:47.475898+00:00'
product: rm
section_id: 1500000861182
source: central-rm
title: RH - RM - Portal RH - Envio de e-mails automáticos em solicitação de férias
type: support-article
updated_at: '2025-01-21T19:29:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13266931373335-RH-RM-Portal-RH-Envio-de-e-mails-autom%C3%A1ticos-em-solicita%C3%A7%C3%A3o-de-f%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:05:56 min** **Dúvida**

Como realizar envio de e-mails automáticos em solicitação de férias?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**Para solucionar essa dúvida, realize os seguintes passos:

1.  Configurar o envio de E-mail do RM conforme material:

[RM - Frame - Configurar Envio de E-mail](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360001046067-RM-Frame-Configurar-Envio-de-E-mail?source=search)  
  
2.  Acessar o grupo de quiosque do colaborador, ir em Folha de pagamento | Configurações | Parametrizador | RM Portal | E-mail de férias e marcar a flag  Enviar e-mail na sugestão e aprovação de férias.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500015808222/mceclip0.png)

* Atualmente, o envio de e-mails pode ser disparado quando ocorrem as seguintes ações:

1. * **Funcionário cadastra sugestão de férias no RM Portal:** quando o funcionário incluir nova sugestão de férias, será disparado o envio de e-mail confirmando a inclusão da sugestão para o funcionário e um e-mail solicitação aprovação para o gestor.
   * **Gestor aprova no RM Portal sugestão de férias cadastrada pelo funcionário:** quando o gestor aprovar a sugestão de férias do funcionário, será enviado e-mail informando o fato ao funcionário.
   * **Departamento Pessoal aprova sugestão de férias através do processo "Aprovação de Alt. Cadastrais":** quando o departamento pessoal aprovar a sugestão de férias, será enviado e-mail ao funcionário informando do fato.
   * **Gestor/Departamento Pessoal reprova a sugestão de férias do funcionário:** quando o gestor reprovar a sugestão do funcionário ou o Departamento Pessoal reprovar através do processo de "Aprovação de Alt. Cadastrais", será enviado e-mail para o funcionário informando do ocorrido.

3. Existe a opção para customizar o corpo dos e-mails da solicitação de férias: deve cadastrar mensagens customizadas em Folha de Pagamento | Configurações | Mensagens Customizadas.

É possível utilizar algumas variáveis no corpo do e-mail customizado :

Abaixo as variáveis aceitas:

1. **[NomeGestor]:** Nome do Gestor do Funcionário;
2. **[NomeFuncionario]:** Nome do Funcionário;
3. **[LinkAcesso]:** Link para acesso à página de aprovação de férias (é necessário efetuar o login);
4. **[DataInicioGozoFerias]:** Data início do gozo de férias;
5. **[DataFimGozoFerias]:** Data fim do gozo de férias;
6. **[TotalDiasFerias]:** Número total de dias;
7. **[DiasAbonoFerias]:** Dias de abono pecuniário;
8. **[AntecipacaoPrimeiraParc13]:** Pode assumir os valore "Sim" ou "Não", informando se o funcionário solicitou ou não a antecipação da 1ª parcela do 13º salário.  
     
   Após o cadastro da mensagem customizada, acesse novamente o grupo de quiosque do colaborador | E-mail de férias  e informe a mensagem customizada criada no passo anterior.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500015808242/mceclip1.png)

Material [RH - RM - FOP - Customização da Mensagem para envio de e-mail na solicitação de Férias no Portal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412849694743-RH-RM-FOP-Customiza%C3%A7%C3%A3o-da-Mensagem-para-envio-de-e-mail-na-solicita%C3%A7%C3%A3o-de-F%C3%A9rias-no-Portal?source=search)

**Importante:**

* O sistema já contém mensagens de e-mail padrões a serem enviadas somente marcando a flag "Enviar e-mail na sugestão e aprovação de férias". Caso queira que o e-mail seja customizado siga o Passo 3.
* O envio de e-mail é disparado obedecendo a hierarquia de chefe/supervisor, segue material do funcionamento de chefe/supervisor: [RH - RM - FOP - Chefes e Supervisores: Cadastro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019444691-RH-RM-FOP-Chefes-e-Supervisores-Cadastro?source=search)
