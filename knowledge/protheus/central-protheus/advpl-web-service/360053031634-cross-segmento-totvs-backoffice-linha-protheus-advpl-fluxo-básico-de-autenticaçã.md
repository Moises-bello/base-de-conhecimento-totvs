---
article_id: 360053031634
category: ADVPL - Web Service
content_hash: 42bc1965a1dc8343a04567c451021a5531110c900e03923109ef84c96a9b31f5
fetched_at: '2026-06-28T22:40:10.471091+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Fluxo básico de
  autenticação Rest no protheus
type: support-article
updated_at: '2021-12-29T14:02:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053031634-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fluxo-b%C3%A1sico-de-autentica%C3%A7%C3%A3o-Rest-no-protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como funciona a autenticação nas requisições REST no protheus ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 12  
  
**Solução**Quando inciamos um serviço REST em nosso ambiente, ao acessarmos a URL definida para o serviço , vão estar listadas todas as **API's** disponíveis no RPO, porém se o **SECURITY** não estiver ativo, qualquer pessoal pode acessar a lista de **API's** e fazer qualquer requisições.

Para evitar isso ativamos a chave SECURITY, exigindo que qualquer pessoa que queira usar nossas API's, precisam ter credencias para tal ação.

Para a ativar a segurança em sua API, para que só tenha acesso requisições autorizadas , você precisa ativar o **SECURITY=1** no seu .ini

```
[HTTPREST]  
Port=8040  
URIs=HTTPURI  
SECURITY=1  
  
Obs.: A partir da LIB Label 20201019, a ser liberada em Outubro de 2020, o comportamento padrão de autenticação de WebServices SOAP e REST será alterado. A partir desta versão, caso a chave Security não seja informada no arquivo appserver.ini, os serviços serão iniciados exigindo autenticação de usuário. Caso seja necessário trabalhar sem autenticação, a chave deverá ser configurada com o valor 0 (Exemplo: Security=0).
```

Com isso as requisições vão começar retornar um erro ***HTTP 401* Unauthorized.**  
Depois de ativar o**SECURITY**se você fizer uma requisição no **postman**, você vai receber o erro mencionado acima, porém se você informar na autenticação básica do postman o **Usuario**e **Senha**do protheus (não precisa ser exclusivamente o admin), você vai perceber que sua requisição vai voltar a funcionar corretamente.  
  
![Screenshot_62.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087669314/Screenshot_62.png)  
  
Temos também a autenticação com token JWT (**saiba mais**).  
Com isso, você deve fazer primeiro a requisição do token, e depois de que tem o token em "mãos", fazer a requisição GET (exemplo) , informando no postman o Bearer: 'seu token'.  
  
![Screenshot_63.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087673174/Screenshot_63.png)  
  
**Saiba Mais:  
[JSON Web Token (JWT)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044840733)   
[Requisição para token JWT (Rest Protheus)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044883213)  
[Requisição para refresh do Token JWT (Rest Protheus)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044356974)**
