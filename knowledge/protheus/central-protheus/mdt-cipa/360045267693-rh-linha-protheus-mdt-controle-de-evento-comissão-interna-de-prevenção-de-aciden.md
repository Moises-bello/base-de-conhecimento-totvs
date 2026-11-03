---
article_id: 360045267693
category: MDT - CIPA
content_hash: 027ed2bd767ea96e54935e09925ac4e29c401328f837454f8a63862205dfd893
fetched_at: '2026-06-28T22:44:23.302596+00:00'
product: protheus
section_id: 360012070553
source: central-protheus
title: RH - Linha Protheus - MDT - Controle de Evento  Comissão Interna de Prevenção
  de Acidentes (CIPA) como configurar o  usuário para acessar a rotina MDTA111
type: support-article
updated_at: '2025-10-03T17:11:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045267693-RH-Linha-Protheus-MDT-Controle-de-Evento-Comiss%C3%A3o-Interna-de-Preven%C3%A7%C3%A3o-de-Acidentes-CIPA-como-configurar-o-usu%C3%A1rio-para-acessar-a-rotina-MDTA111
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372801143063)**Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**Ao acessar a rotina de controle de eventos cipa (MDTA111), apresenta a mensagem "Este usuário não está configurado para acessar os eventos da CIPA."  
Como realizar a liberação aos usuários?

![](https://tdn.totvs.com/download/attachments/281259227/image2017-6-21%2013%3A55%3A52.png?version=1&modificationDate=1498070973000&api=v2)

**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho  – Todas as versões  
  
**Solução**O administrador do sistema deverá configurar o parâmetro **MV\_CIPAUSR** para liberar este acesso.

Para correção efetue o processo abaixo:  
Acessar o Configurador **(SIGACFG)** no caminho: **Ambiente - Cadastro - Parâmetro**:  Localize o parâmetro **MV\_CIPAUSR**  e edite com o nome dos usuários que terão acesso.

OBS: Se tiver mais de um usuário, o conteúdo do campo deverá ser separado por virgula, conforme exemplo **MV\_CIPAUSR** =ADMINISTRADOR,JULIANA  
  
Deve conter exatamente o nome do usuário conforme o cadastro de usuários.

![image2017-6-21 14:5:27.png](https://tdn.totvs.com/download/attachments/281259227/image2017-6-21%2014%3A5%3A27.png?version=1&modificationDate=1498070973000&api=v2)

Consulta Cadastro de usuários via Configurador

![image2017-6-21 15:14:25.png](https://tdn.totvs.com/download/attachments/281259227/image2017-6-21%2015%3A14%3A25.png?version=1&modificationDate=1498070973000&api=v2)

Acesse a rotina normalmente observe que será aberta sem restrições:

Observação neste exemplo utilizei o administrador, porém a empresa deve apontar o usuário responsável por este processo no módulo.

![](https://tdn.totvs.com/download/attachments/281259227/image2017-6-21%2015%3A49%3A7.png?version=1&modificationDate=1498070973000&api=v2)

**Saiba Mais**[Artigos MDT CIPA](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012070553-MDT-CIPA)  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
