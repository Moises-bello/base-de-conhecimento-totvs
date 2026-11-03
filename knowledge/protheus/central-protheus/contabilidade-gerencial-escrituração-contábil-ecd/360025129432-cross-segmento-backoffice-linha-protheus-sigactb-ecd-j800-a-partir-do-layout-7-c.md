---
article_id: 360025129432
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: e538f13fa354b0b37dcf6882908262e579744f00fda5512827f1478a6f687db9
fetched_at: '2026-06-28T22:40:44.686326+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECD - J800 A PARTIR
  DO LAYOUT 7 COMO GERAR NOTA EXPLICATIVA
type: support-article
updated_at: '2024-04-22T19:34:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025129432-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-J800-A-PARTIR-DO-LAYOUT-7-COMO-GERAR-NOTA-EXPLICATIVA
---

**Dúvida** ECD LAYOUT 7 COMO GERAR NOTA EXPLICATIVA REGISTRO J800?  
   
 **Ambiente**Protheus – Contabilidade gerencial– A partir da versão 12.1.17

**Causa**

No campo NOTA\_EXP\_REF referente as notas explicativas informadas no registros J100,J150 e J210/ J215. Cada nota explicativa é identificada por um código/número (escolha/controle do contador), e poderá constar em qualquer linha das demonstrações.

Será necessário o envio de um arquivo com extensão rtf. (J800) fazendo referência a numeração das notas explicativas relativas às demonstrações contábeis.

TIPO\_DOC (Campo 02) do registro J800, igual a :

“010 – Notas Explicativas”,

“011 – Relatório da Administração”,

“012 – Parecer dos Auditores” ou

“999 – Outros”

**Solução**

* Em um editor de texto, digite a nota explicativa e salve no formato RTF

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068783774)

* Em um editor de texto, digite a nota explicativa e salve no formato RTF

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068783894)

* Após a preenchimento da wizard e criação de uma revisão, antes de gerar o TXT, posicione na revisão e selecione a opção NOTAS EXPLICATIVAS.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22981405808535)

* O campo  CSE\_NOTARF possui Tamanho 12/ Decimais 0/ Uso Livre.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023994791)

* Ainda posicionado na revisão, selecione a opção "Outras informações"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22981405825431)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22981405837463)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023970372)

Leia também:

<https://totvssuporte.zendesk.com/knowledge/articles/360025419031/pt-br?brand_id=1509248>

Saiba mais:

<http://tdn.totvs.com/display/PROT/ECD_SPED_CONTABIL_Alteracoes_para_Leiaute_7_00>
