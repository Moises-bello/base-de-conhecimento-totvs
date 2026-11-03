---
article_id: 360014074932
category: RH - Cadastros
content_hash: 87731af8af0a456d3c135e32e5095736c3418c93303d7bdadf53dd35143d51b3
fetched_at: '2026-06-28T22:44:52.706984+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: 'RH - Linha Protheus - PON -  O que verificar quando gerada a mensagem: Este
  evento não se encontra cadastrado no sistema - Tabela 20'
type: support-article
updated_at: '2025-12-17T17:54:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014074932-RH-Linha-Protheus-PON-O-que-verificar-quando-gerada-a-mensagem-Este-evento-n%C3%A3o-se-encontra-cadastrado-no-sistema-Tabela-20
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35218768075287) Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
O que verificar quando gerar a mensagem: Este evento não se encontra cadastrado no sistema - Tabela 20?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (linha Protheus) – Ponto Eletrônico – Todas as versões  
  
**Solução**  
Isso pode ocorrer por não existir nenhum registro na SX5 - Tabela 20, ou se existirem ID's não vinculados a um cadastro de Evento na tabela SP9.  
  
Para ajuste, validar em seu ambiente conforme abaixo:

- Verifique o compartilhamento das tabelas **SX5** e **SP9** (Eventos), se as mesmas estiverem como CCC - Compartilhada, o campo X5\_FILIAL da tabela 20 da SX5 e P9\_FILIAL da tabela SP9 não devem possuir filial. Se estiverem como EEE - Exclusiva, ambas devem possuir filial informada e devem possuir todos os Identificadores para todas as filiais;

- Se certifique que a tabela **SP4** (Tipos Horas Extras) esteja com o mesmo compartilhamento da **SP9** (Eventos), pois ambas são correlatas e devem estar com o mesmo modo de compartilhamento;

- Verifique através do modulo Configurador em **Ambiente> Cadastros> Tabelas> Tabela 20** se existem todos os Identificadores abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37095826791063)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37095818236439)

- Caso esteja faltando algum identificador, será necessário rodar o UPDDISTR para atualizar a tabela 20 com todos os ID do ponto disponíveis, ou incluir de forma manual clicando abaixo do ultimo ID para liberar a linha e realizar o cadastro.

- Se constar todos os Identificadores de Ponto cadastrados, verifique no Ponto Eletrônico em **Atualizações> Cadastro do Ponto> Eventos**, se todos os identificadores estão atrelados a algum evento, caso algum não esteja, crie um evento ou altere um já existente e vincule o identificador faltante.

**Saiba Mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Como utilizar o cadastro de evento do ponto eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407450836887-RH-Linha-Protheus-PON-Como-utilizar-o-cadastro-de-evento-do-ponto-eletr%C3%B4nico)  
[RH - Linha Protheus - PON - Como cadastrar os eventos para Folha de Pagamento ou Banco de Horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013459532-RH-Linha-Protheus-PON-Como-cadastrar-os-eventos-para-Folha-de-Pagamento-ou-Banco-de-Horas)
