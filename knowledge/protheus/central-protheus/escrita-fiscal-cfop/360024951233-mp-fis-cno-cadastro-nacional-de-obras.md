---
article_id: 360024951233
category: Escrita Fiscal - CFOP
content_hash: 8de6edcf4df4fdc8990b99da83c2f97beec790ff8be98001e0483c83a86aca28
fetched_at: '2026-06-28T22:39:35.946353+00:00'
product: protheus
section_id: 1500001538541
source: central-protheus
title: 'MP - FIS -  CNO - Cadastro Nacional de Obras '
type: support-article
updated_at: '2021-10-01T16:48:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024951233-MP-FIS-CNO-Cadastro-Nacional-de-Obras
---

**Dúvida**Qual o formato da composição numérica para exibição do CNO ( Cadastro Nacional de Obras) ?  
   
 **Ambiente**Microsiga Protheus - a partir da versão 12.1.17  
  
**Solução**

O Cadastro Nacional de Obras (CNO) refere-se ao registro perante a Receita Federal do Brasil das informações específicas de obras de construção civil, seja por pessoas físicas ou para pessoa jurídica. O CNO foi criado para substituir o cadastro especifico de INSS de Obras, conhecido como matriculas CEI de Obras.

No manual do usuário do CNO (<http://receita.economia.gov.br/orientacao/tributaria/cadastros/cadastros-nacional-de-obras-cno/manual-cno-ecac.pdf>) no item 5.1.5.1 informações sobre a Obra, o campo número da obra está com seguinte formato:

02.043.11375/74 - (dois números seguidos de ponto)+(três números seguidos de ponto)+(5 números seguidos de barra)+(dois números).

Diante do exposto acima, a composição numérica do CNO permanecerá com o mesmo formato do CEI ou seja, com 12 caracteres.

Para gerar essa informação para o REINF via documento de entrada é necessário realizar o Cadastro do CNO pela rotina MATA322 e preencher o campo D1\_CNO.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038221414/mceclip0.png)

*Boletim - Cadastro Nacional de Obras*

*<http://tdn.totvs.com/display/public/PROT/DT+Cadastro+Nacional+de+Obras>*

*<http://tdn.totvs.com/pages/releaseview.action?pageId=490983116>*
