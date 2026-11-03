---
article_id: 360029387531
category: CRM - Dúvidas Gerais
content_hash: 41f5ffcd46c5f7c4638413afb63e3018172c5c167d7e1f2aa4a589988df66d5b
fetched_at: '2026-06-28T22:40:27.530569+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: MP-CRM -array out of bounds -0 of 13 -  on TK61ENTGET
type: support-article
updated_at: '2021-04-28T14:50:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029387531-MP-CRM-array-out-of-bounds-0-of-13-on-TK61ENTGET
---

**Ocorrência**Ao tentar incluir um membro a lista de marketing no Sigacrm, ocorre o erro:

**array out of bounds ( 0 of 13 ) on TK61ENTGET(TMKA061.PRW) 07/05/2018 09:27:43 line : 2138**

**Ambiente**

Microsiga Protheus - a partir da versão 12.  
   
 **Causa**

Quando o error.log é referente array out of bounds ( 0 of 13 ), significa que algum campo não esta como **Usado** ou o nível esta diferente de **1**. 

Neste caso, o sistema não está encontrando o campo da tabela **SU6**, **U6\_DENTIDA**, que pode estar sem marcação de uso ou ter o seu nível diferente de 1.

Este array contempla os campos:

***"U6\_CODENT" } ) // Codigo Entidade***  
***"U6\_DESCENT" } ) // Nome Entidade***  
***"U6\_CODIGO" } ) // Codigo do Item***  
***"U6\_DATA" } ) // Data***  
***"U6\_ENTIDA" } ) // Entidade Selecionada***  
***"U6\_HRFIM" } ) // Hora Final***  
***"U6\_HRINI" } ) // Hora Inicio***  
***"U6\_CONTATO" } ) // Codigo Contato***  
***"U6\_NCONTAT" } ) // Nome Contato***   
***"U6\_DENTIDA" } ) // Descrição da Entidade***

Qualquer e ero relacionado a array out of bounds na função **TK61ENTGET**, deverá ser validado se os campos acima estão como usado e com o nível.  
  
 **Solução**

Via SIGACFG , e busque a tabela **SU6** e deixe o campo **U6\_DENTIDA** como Usado e Nível como 1.  
Após isso, reinicie o Smartclient e realize um novo teste.
