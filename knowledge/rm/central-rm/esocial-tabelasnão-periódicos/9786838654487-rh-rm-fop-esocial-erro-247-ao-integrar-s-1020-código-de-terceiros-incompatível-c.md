---
article_id: 9786838654487
category: eSocial - Tabelas/Não Periódicos
content_hash: 3db7de7943f0e1b130150a403da4cd63e994db54d79277d6f2339355583d298a
fetched_at: '2026-06-28T22:47:10.328572+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 247 ao integrar S-1020: Código de Terceiros
  incompatível com o FPAS informado'
type: support-article
updated_at: '2024-12-30T14:35:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9786838654487-RH-RM-FOP-eSocial-Erro-247-ao-integrar-S-1020-C%C3%B3digo-de-Terceiros-incompat%C3%ADvel-com-o-FPAS-informado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24266709210135) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao transmitir o evento S-1020, o governo retorna a mensagem **Erro código 247: Código de Terceiros incompatível com o FPAS informado. Ação Sugerida: Para classificação tributária igual a (01, 02, 03, 04), informar 0000. Nos demais casos, o valor informado no campo deverá ser compatível com o código FPAS que consta na Tabela 4 (Códigos e Alíquotas de FPAS/Teceiros).**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9786100879511)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Esse incidente geralmente ocorre quando o XML está informando um código FPAS que não corresponde ao código de terceiros.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique a informação gerada na *tag* **fpas** do XML em questão;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9786424290967)

2. Acesse o **Anexo I do Leiaute do eSocial - Tabelas** e verifique os **Código de Terceiros** disponíveis conforme o **FPAS** da empresa conforme **Tabela 4 - Códigos e Alíquotas de FPAS/Terceiros;**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9786529303447)

3. Sendo necessário ajustar o FPAS ou o Código de Terceiros, acesse o menu **Administração de Pessoal | Seções** e ajuste os campos **F.P.A.S.** e/ou **Cód. Terceiros (INSS)**. Caso utilize tomador de serviços, também poderá ser alterado através do menu eSocial | Lotação Tributária, ajustando os campos **FPAS** e/ou **Código de Terceiros**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9805323823127)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9812304494359)  
  
**Importante**  
Conforme o leiaute do eSocial, o Código de Terceiros deve ser preenchido já considerando a existência de eventuais convênios para  recolhimento direto. Ex.: Se o contribuinte está enquadrado com **FPAS 507**, cujo código cheio de  terceiros é **0079**, se possuir convênio com SENAI deve informar o código **0075**.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9812446106391)

**Saiba mais**Para mais informações, acesse:  
     - [Documentação Técnica eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)
