---
article_id: 39127555611159
category: ADVPL - Web Service
content_hash: 9d13499d9b06e34153e6af49d98a403cd958f9d3f5b9a8581e91c5fe7080b882
fetched_at: '2026-06-28T22:40:10.548101+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Troca de senha
  no REST 2.0
type: support-article
updated_at: '2026-03-18T17:46:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39127555611159-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Troca-de-senha-no-REST-2-0
---

O REST 2.0, a partir da Lib 20230227, ao tentar login com usuário cuja senha está expirada, retorna HTTP 302 com header Location apontando para a API de troca de senha (/api/framework/v1/changepassworduserservice). Para trocar a senha, deve-se enviar um POST com JSON contendo usuário, senha atual e nova senha.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39127528174871) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**   
Qual é o comportamento do REST 2.0 ao realizar login (via Basic ou JWT) com um usuário que possui a senha expirada?

**Ambiente**   
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - A partir da Lib 20230227

**Solução**   
O REST 2.0 teve seu comportamento alterado para a autenticação de usuários que estão com a senha expirada.

Anteriormente, ao fazer o login via Basic ou gerar o JWT via API, mesmo com a senha expirada, o login era bem-sucedido. A partir da **Lib 20230227**, ao efetuar o login nessas condições, o REST retornará um status HTTP `302`. O header da resposta conterá o parâmetro `Location` apontando para a API oficial de troca de senha: `/api/framework/v1/changepassworduserservice`.

Para realizar a troca, a API de destino deve ser consumida enviando as credenciais necessárias.

**Passos**

1. Configure a requisição para a API de troca de senha utilizando exclusivamente o método **POST** na rota `/api/framework/v1/changepassworduserservice`.
2. No corpo (body) da requisição, envie o usuário, a senha atual e a nova senha respeitando a seguinte estrutura JSON:

**JSON**

```
{
  "user": "string",
  "oldPassword": "string",
  "newPassword": "string"
}
```

**Saiba mais**  
[Troca de senha REST 2.0.](https://tdn.totvs.com/display/public/framework/Troca+de+senha+no+REST+2.0)  
[Conceitos sobre WebServices](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053029654-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Conceitos-sobre-WebServices)  
[Configuração básica REST do protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045401793-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Configura%C3%A7%C3%A3o-b%C3%A1sica-REST-do-protheus)
