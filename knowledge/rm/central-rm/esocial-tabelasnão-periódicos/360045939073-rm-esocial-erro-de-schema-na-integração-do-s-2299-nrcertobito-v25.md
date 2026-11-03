---
article_id: 360045939073
category: eSocial - Tabelas/Não Periódicos
content_hash: e69d4b65284381ef8edf86e4bf2b7fe80e54f7017f1f908c214d0ae129f538b1
fetched_at: '2026-06-28T22:47:10.583657+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RM - eSocial -  Erro de Schema na integração do S-2299: ''nrCertObito'' (v.2.5)'
type: support-article
updated_at: '2021-05-24T13:26:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045939073-RM-eSocial-Erro-de-Schema-na-integra%C3%A7%C3%A3o-do-S-2299-nrCertObito-v-2-5
---

**Ocorrência**Ao realizar a integração do evento S-2299 por falecimento, é apresentado o erro **'nrCertObito':[facet'pattern'] The value 'xxxx' is not accepted by the pattern '\{32}'**. **Ambiente**RM - eSocial - Todas as Versões  
  
 **Causa**O erro é apresentado pois o número de caracteres informados na tag **nrCertObito** dentro do XML S-2299 está incorreto de acordo com o layout do eSocial.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063314534/mceclip0.png)

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
 1. Encontre a tag **nrCertObito** no XML S-2299 e compare se os caracteres informados são iguais aos cadastrados na rescisão;  
 2. Valide se o campo **Nro. Atestado de Óbito** dentro da rescisão do funcionário está preenchido corretamente;  
 3. Caso a rescisão esteja incorreta, cancele-a e gere novamente. Feito isso, regere também o XML S-2299.  
  
**Importante**  
Documentação válida somente para leiaute anterior à versão S-1.0 pois nesta versão não existirá a tag nrCertObito
