---
article_id: 6734260990359
category: Administração de Pessoal
content_hash: e7230ba139afc07cb3c6fcde4e56418652a857a5731cdf1733a09b8dc0c6cfa5
fetched_at: '2026-06-28T22:47:01.339926+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Registro Preliminar
type: support-article
updated_at: '2025-03-12T13:42:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6734260990359-RH-RM-FOP-Registro-Preliminar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:15 min** **Dúvida**Como faço o Registro Preliminar de funcionários?**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Em **Administração de** **Pessoal | Registro Preliminar**, o cadastro de Registro Preliminar permite que o usuário possua um cadastro para informar dados básicos de um funcionário que será admitido, utilizando um registro de **Pessoa** existente. Na inclusão de um Registro Preliminar, estarão disponíveis campos como Pessoa, Data de Admissão prevista e CPF. **Importante ressaltar que o campo CPF serve para conferência dos dados da Pessoa, não sendo possível modificá-lo.** Ele aparecerá na tela quando um **Cód. Pessoa** for inserido:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6733881540887/mceclip0.png)  
  
Quando houver integração entre os módulos **Folha de Pagamento** x **Gestão de Pessoas** e a obrigatoriedade de requisição para admissão, ao incluir um funcionário em **Administração de Pessoal | Funcionários | Incluir** é exibida a tela de pré-cadastro que faz a busca por todas as pessoas que já estão associadas a uma requisição. Nesta mesma tela existe o ícone **Exibir somente pessoas com registro preliminar**que irá filtrar as pessoas que já possuem cadastro no Registro Preliminar. No caso da não existência da integração **Folha de Pagamento**x **Gestão de Pessoas**, e a não utilização de requisição para admissão, ao incluir um novo funcionário, dentro do cadastro existe um ícone que permite localizar uma pessoa já cadastrada na base de dados e que também possui um Registro Preliminar.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6734046483479/mceclip1.png)  
  
**Importante**  
- Os campos do Registro Preliminar são de preenchimento obrigatório;  
- As informações contidas neste cadastro serão utilizadas pelo eSocial;  
- Os dados deste cadastro serão enviados para o eSocial através do evento [S-2190 - Admissão de Trabalhador-Registro Preliminar](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719051). Para incluir um novo registro de Pessoa para sua utilização no Registro Preliminar, é necessário ao usuário ter a permissão de Incluir **Pessoa** no sistema **TOTVS Gestão de Pessoas**;  
- Uma vez que realizou o cadastro de um Registro Preliminar, **a fim de evitar que o funcionário fique com a matrícula do eSocial duplicada**, deve-se utilizar a opção **Localizar Pessoa / Registro Preliminar** ao cadastrar o **Funcionário**.
