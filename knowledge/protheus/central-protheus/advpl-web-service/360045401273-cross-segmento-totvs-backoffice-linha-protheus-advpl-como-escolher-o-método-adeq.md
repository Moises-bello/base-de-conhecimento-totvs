---
article_id: 360045401273
category: ADVPL - Web Service
content_hash: 9869df1e188131902c1923af39f4c34762d92bd5ed4a77fc0930be13dc79ac3a
fetched_at: '2026-06-28T22:40:10.142353+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) -  ADVPL - Como escolher
  o método adequado em API's
type: support-article
updated_at: '2025-07-24T17:24:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045401273-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-escolher-o-m%C3%A9todo-adequado-em-API-s
---

**Dúvida**Como escolher o método adequado no uso de **API's**  
  
**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) – ADVPL – A partir da versão 12  
  
**Solução**Abaixo descrevemos algumas situações e o método adequado a ser usado.

***GET***

```
Quero retornar uma lista de usuários;  
Quero retornar o usuário com o id x;  
Quero retornar todas as permissões do usuário x;  
Quero retornar todos os usuário maiores de idade;
```

***PUT***

```
Quero sobrescrever o usuário atual na base de dados usando os dados informados na requisição;  
Quero alterar o estado do usuário para ativo independente de outras regras;
```

*POST*

```
Quero adicionar um novo usuário;  
Quero executar uma ação ou serie de operações no usuário;
```

***DELETE***

```
Quero deletar um usuário;
```

**Saiba Mais**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - O que é REST](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028699492)
