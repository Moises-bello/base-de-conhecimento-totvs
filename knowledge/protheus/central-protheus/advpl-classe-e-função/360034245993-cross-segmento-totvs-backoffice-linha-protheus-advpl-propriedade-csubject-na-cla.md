---
article_id: 360034245993
category: ADVPL - Classe e Função
content_hash: cd774e647b45a05ab03417fba4a75344f291618039bf2ff8b71451e0a8a87c94
fetched_at: '2026-06-28T22:40:17.088251+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Propriedade cSubject
  na classe Tmailmanager '
type: support-article
updated_at: '2022-06-13T17:28:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034245993-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Propriedade-cSubject-na-classe-Tmailmanager
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**Ao ler e-mail do nosso servidor de e-mail, o assunto do e-mail vem com caracteres especiais quando o assunto tem acentuação: **oMessage:cSubject**.

Assunto do E-mail : Favor Realizar Confirmação 

```
oMessage:cSubject : =?UTF-8?Q?Favor_Realizar_Confirma=c3=a7=c3=a3o?=
```

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**A propriedade cSubject da Classe Tmailmanager, não é realizado tratamento ou conversão desse conteúdo/texto que vem do servidor de email, que no caso alguns caracteres não são da tabela ASC (Vide Documentação [RFC 6532](https://tools.ietf.org/html/rfc6532) ) Uma possibilidade é tratar retirando esse caracteres e tratar os demais.
