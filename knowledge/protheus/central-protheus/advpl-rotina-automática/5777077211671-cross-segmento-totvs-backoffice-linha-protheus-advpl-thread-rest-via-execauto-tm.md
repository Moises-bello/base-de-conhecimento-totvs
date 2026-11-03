---
article_id: 5777077211671
category: ADVPL - Rotina Automática
content_hash: 5063fac0a2eee7ca77eed285419e1841fc1f936f6cf892ace09c223ffbac1a5e
fetched_at: '2026-06-28T22:40:25.133542+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Thread rest via
  execauto Tmka271 mostrando help TMKPROMDI
type: support-article
updated_at: '2022-05-02T16:48:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5777077211671-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Thread-rest-via-execauto-Tmka271-mostrando-help-TMKPROMDI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Dúvida**Ao realizar a chamada da Agenda de Operador após a ExecAuto TMKA271 via Rest é mostrado o help **TMKPROMDI**, como executar sem ativar o help?  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5777906985495/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – REST - A partir do 12.1.33.  
  
**Solução**Para correto funcionamento do *Rest via**ExecAuto  TMKA271*, seguir os passos de atenção abaixo:  
1° - Não são boas práticas utilizar variáveis públicas em tratamentos para API customizada ou para qualquer outra customização.  
O uso de variáveis públicas como a "\_\_cUserId" é tratada diretamente e isto não seria o indicado.  
O correto seria utilizar a chave **Security=1** dentro do HTTPREST e passar um usuário e senha para que assuma o usuário desejado.  
2°- Por se tratar de uma API customizada via REST, a única maneira de atender a solicitação seria a criação de um usuário específico para requisição Rest, não utilizando o mesmo usuário do Protheus.  
Caso contrário, não atenderá a necessidade exposta.   
Quando a requisição é enviada com um usuário, o mesmo fica atrelado a thread do Rest e este não é liberado imediatamente.

Para solucionar a ocorrência, siga os passos abaixo:  
1. Crie um usuário para chamada da ExecAuto TMKA271 via Rest;  
2. Finalizando a execução, ao acessar o Protheus no módulo TMK utilize um usuário diferente do utilizado na ExecAuto.
