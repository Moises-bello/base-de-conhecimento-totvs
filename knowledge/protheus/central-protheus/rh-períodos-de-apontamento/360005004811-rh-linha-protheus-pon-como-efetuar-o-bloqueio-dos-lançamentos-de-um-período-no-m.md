---
article_id: 360005004811
category: RH - Períodos de Apontamento
content_hash: 36da053f8499db226462092ffd14192dcfc8bd62a56fb03c18993539644c0e01
fetched_at: '2026-06-28T22:44:45.111396+00:00'
product: protheus
section_id: 32419304439959
source: central-protheus
title: RH - Linha Protheus - PON - Como efetuar o bloqueio dos lançamentos de um período
  no modulo do Ponto Eletrônico
type: support-article
updated_at: '2025-10-13T17:21:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005004811-RH-Linha-Protheus-PON-Como-efetuar-o-bloqueio-dos-lan%C3%A7amentos-de-um-per%C3%ADodo-no-modulo-do-Ponto-Eletr%C3%B4nico
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35600459896471) Tempo aproximado para leitura: 00:02:00 min**Dúvida**Como efetuar o bloqueio dos lançamentos de um período no modulo do ponto eletrônico?  
 **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
 **Solução**Foi efetuada uma implementação no módulo **SIGAPON** - Ponto Eletrônico, que permite ao responsável pelo apontamento e manutenção de marcações informar quais as datas de início e término do bloqueio e quais usuários terão acesso durante esse período de datas.  
  
Para efetuar as configurações segue os passos abaixo:  
- Antes de executar os passos vamos verificar primeiramente o período aberto. Caso necessite de apoio para consulta, acesse a documentação de orientação da rotina de período:  
[RH - Linha Protheus - PON - Rotina Período de Apontamento - PONA290](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059188733-RH-Linha-Protheus-PON-Rotina-Per%C3%ADodo-de-Apontamento-PONA290)  
  
- Em nosso exemplo estamos trabalhando com dois períodos abertos, configurado nos parâmetros: **MV\_PAPONTA = 21/20** e o **MV\_PONMES** = **21/02/2025 a 20/03/2025;**  
- Vale ressaltar que o Bloqueio de Período servirá para informar as datas de inicio e término do bloqueio e quais usuários terão acesso durante esse período de data e não do período de apontamento.

A rotina está disponível no módulo SIGAPON → Atualizações → Cadastro do Ponto → Períodos de Apontamento. No botão **“Bloq. de Períodos”**, ao clicar na opção **Bloqueio de Períodos**, será apresentada uma tela para selecionar a filial desejada. Os registros serão filtrados conforme a filial posicionada no registro de período fechado, na tela inicial (tabela: SPO). Exemplo:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31594981485719)**

- Na rotina é necessário informar o período que terá o bloqueio, os usuários que terão acesso durante o bloqueio, e a data inicial e final do bloqueio;  
- O período será o mês e o ano da data inicial do período de apontamento;  
- O Usuário Liberado 1 e Usuário Liberado 2 são os usuários do Protheus que terão acesso as rotinas durante o bloqueio, todos os demais usuários serão bloqueados;  
- A Data Inicial e a Data Final definem os dias que serão bloqueados. Essas datas serão comparadas com a data do servidor, por isso cadastrar datas passadas não irá bloquear o período. ![](https://centraldeatendimento.totvs.com/hc/article_attachments/31594981486743)

Quando algum usuário que não for o cadastrado na rotina de bloqueios, tentar utilizar alguma rotina referente a manutenção das marcações, será exibido o aviso do bloqueio, conforme imagem abaixo.  
É importante ressaltar que **indiferente da data base utilizada, o sistema bloqueará os dois períodos abertos**, no meu exemplo bloqueou tanto o período 21/03 a 20/04, quanto o período de 21/04 a 20/05, pois o sistema valida as datas do período lançadas no bloqueio e dentre aquele período será bloqueado aos usuários exceto para aqueles dois usuários liberados que estão configurados na rotina de bloqueio.![](https://centraldeatendimento.totvs.com/hc/article_attachments/31594967699863)

**Saiba mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[Bloqueio de Períodos de Apontamento](https://tdn.totvs.com/pages/releaseview.action?pageId=677023774)
