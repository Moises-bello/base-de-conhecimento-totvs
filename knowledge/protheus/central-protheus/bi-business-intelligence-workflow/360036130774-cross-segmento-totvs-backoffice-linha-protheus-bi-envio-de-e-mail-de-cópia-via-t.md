---
article_id: 360036130774
category: BI - Business- Intelligence - Workflow
content_hash: bd095a78e90ba9a9cce5247ec11e57b3e81098f3e42ca419d4898cf598453472
fetched_at: '2026-06-28T22:37:03.028856+00:00'
product: protheus
section_id: 1500001550762
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Envio de e-mail de
  cópia via TWFPROCESS() '
type: support-article
updated_at: '2022-02-15T19:02:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036130774-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Envio-de-e-mail-de-c%C3%B3pia-via-TWFPROCESS
---

**Dúvida**É possível enviar um e-mail de cópia no Workflow?  
 **Ambiente**Protheus – Workflow – A partir da versão 12.1.17  
  
**Solução**

Para definir o destinatário do email, copia , você pode utilizar as propriedades   
**:cTo,  :cCC** da classe **TWFPROCESS()**

Estas propriedades definem o endereço dos destinatários. Poderá ser informado mais que um destinatário ao mesmo tempo. Basta incluir um ponto-e-vírgula “;” entre eles.

```
Exemplo:  
oP:cTo := "aluno1@microsiga.com.br;aluno2@microsiga.com.br"  
oP:cCC := "aluno3@microsiga.com.br;Aluno"
```

**Saiba mais:**  
**[TWFProcess](https://tdn.totvs.com/display/public/PROT/TWFProcess)**
