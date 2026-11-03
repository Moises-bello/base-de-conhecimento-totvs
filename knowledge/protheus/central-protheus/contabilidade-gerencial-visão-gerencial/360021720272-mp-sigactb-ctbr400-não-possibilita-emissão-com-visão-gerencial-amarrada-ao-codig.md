---
article_id: 360021720272
category: Contabilidade Gerencial - Visão Gerencial
content_hash: cae545d15674c983413555726a4dd12fd6b967aab8c571775205524bfa826cce
fetched_at: '2026-06-28T22:40:50.698707+00:00'
product: protheus
section_id: 1500001548642
source: central-protheus
title: 'MP - SIGACTB : CTBR400 Não possibilita emissão com Visão gerencial amarrada
  ao codigo de livro'
type: support-article
updated_at: '2021-04-28T15:23:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021720272-MP-SIGACTB-CTBR400-N%C3%A3o-possibilita-emiss%C3%A3o-com-Vis%C3%A3o-gerencial-amarrada-ao-codigo-de-livro
---

**Dúvida**

O plano gerencial não está disponível neste relatório

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018637411/mceclip4.png)  
   
 **Ambiente**  
Protheus  – Contabilidade – A partir da versão 11.80

**Causa**

Situação é apresentada devido o a **visão gerencial** amarrada ao  **Código de Livro**

Determine qual a configuração de Livro será utilizada neste relatório . Se não desejar nenhuma configuração especifica deixe este campo em branco

Neste relatório a  **Código de Livro**  não poderá  ter uma **visão gerencial** amarrada. Somente as mascaras das entidades serão herdadas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018637371/mceclip1.png)  
  
   
**Solução**

Através da rotina CTBA130 verifique a amarração do livro

* O livro que será utilizado na emissão do relatório CTBR400 não deve ser informada a "Visão gerenc."

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018637391/mceclip2.png)

* Deve ser informado os campos abaixo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018762632/mceclip3.png)

Veja mais:

[MP - SIGACTB - CTBA161 /CTBA130 - Amarração Visão Gerencial ao Livro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006908012-MP-SIGACTB-CTBA161-CTBA130-Amarra%C3%A7%C3%A3o-Vis%C3%A3o-Gerencial-ao-Livro?source=search)

[MP - SIGACTB - CTBA130 Máscara Contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015545571-MP-SIGACTB-CTBA130-M%C3%A1scara-Cont%C3%A1bil?source=search)
