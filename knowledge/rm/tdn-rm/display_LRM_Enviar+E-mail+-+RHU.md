---
content_hash: ad0575a2b3761fc330731d61a1f8dbe857037a1f4bbc76a279f74b51a7ae3436
fetched_at: '2026-06-29T00:10:09.932166+00:00'
page_id: '452719740'
product: rm
source: tdn-rm
title: Enviar E-mail - RHU
type: documentation
url: https://tdn.totvs.com/display/LRM/Enviar+E-mail+-+RHU
version: 2
---

**Enviar E-mail**

O processo de "Enviar e-mail" executado a partir de um assistente, tem a finalidade de enviar emails para as pessoas envolvidas.

**Observações:**

* Para emails onde for utilizado um relatório do sistema, o usuário deverá utilizar os recursos do gerador de relatórios.
* Para que estes relatórios sejam apresentados para serem utilizados no envio de mensagens, ao criar o relatório a ser utilizado, este deverá ser informando no campo tipo de relatório o tipo de mensagem a ser enviada (Ex.: EMAIL PESSOA, EMAIL EXAME) e tipo de saída "texto" e ainda conter no texto do relatório um campo obrigatório, mesmo que seja invisível (Ex.: no relatório de Pessoa, deve conter obrigatoriamente o campo CODIGO da tabela PPESSOA).
* É possível definir outro e-mail para que seja enviada uma cópia da mensagem/relatório do sistema.
* O campo "Assunto" será preenchido com o nome do relatório do sistema, caso a opção de envio seja "relatório do sistema". - O campo "Dados do Remetente" é desabilitado caso a opção de envio seja "relatório do sistema".

**Atenção:**

O processo de envio de e-mails para candidatos irá registrar um contato realizado por e-mail. Para isso, existe um parâmetro no sistema que define qual o Tipo de Contato que será utilizado nesse processo.

Esse parâmetro irá preencher com o registro de contato referente ao E-mail, que será cadastrado pelo administrador do sistema.

O registro de contato só será gerado neste processo se o parâmetro citado estiver preenchido com um Tipo de Contato Ativo. Caso contrário, o processo de envio de e-mail será executado normalmente mas sem registrar o contato.

O registro de contato irá preencher com as informações do candidato, a data e hora do momento do envio e o tipo definido no parâmetro descrito acima.

O campo "Contato com sucesso" será preenchido com a opção "Não aplicável". Se por qualquer motivo no sistema não conseguir realizar o envio do e-mail, o registro de contato não será gerado.
