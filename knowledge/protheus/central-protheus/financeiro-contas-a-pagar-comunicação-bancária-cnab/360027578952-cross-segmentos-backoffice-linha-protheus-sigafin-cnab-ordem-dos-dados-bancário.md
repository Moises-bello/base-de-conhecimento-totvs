---
article_id: 360027578952
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: b69ae6ef25bf73e489aa737caeec772ea40d11cead048fa530f71da4e9cad3f0
fetched_at: '2026-06-28T22:37:55.299819+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN -  CNAB - Ordem dos dados
  bancário no retorno de cobrança
type: support-article
updated_at: '2022-11-22T23:24:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027578952-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-Ordem-dos-dados-banc%C3%A1rio-no-retorno-de-cobran%C3%A7a
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:05:00min**

**Dúvida**Qual banco, agência e conta o sistema considera para retorno de arquivo CNAB?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - CNAB - Todas as versões  
  
**Solução**No padrão, os dados bancários para o retorno de cobrança seguem na seguinte ordem:

**1)** **Parâmetros de Bancos (FINA130)** na aba: **Outros**.

**EE\_CODOFI = Banco Oficial**

**EE\_AGEOFI = Agência Oficial**

**EE\_CTAOFI = Conta Oficial  
  
![kcscontaoficial.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360027617851/kcscontaoficial.PNG)**

**2)**Do **Portador do Título**:  
  
**1-****E1\_PORTADO** = Banco  
2- **E1\_AGEDEP** = Agencia  
3- **E1\_CONTA** = Conta  
  
**3)** Dos parâmetros da rotina **Retorno de Cobrança(FINA200)**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027619671/mceclip0.png)

Caso o ponto de entrada **F200PORT** seja utilizado, segue abaixo como o sistema considera o banco:

**A)** Na utilização do ponto de entrada: F200PORT retorne **.T.** – Sistema se comporta exatamente como o padrão descrito acima.

**B)** Na utilização do ponto de entrada F200PORT retorno **.F.** – O sistema desconsidera o  Banco, Agencia e Conta informado nos campos: **Banco Oficial, Agência Oficial, e Conta Oficial** no cadastro Parâmetros Bancos e o **Portador** do título.  
Nesta configuração são **considerados unicamente** os **parâmetros da rotina.**

**Saiba mais**[F200PORT - Definição de banco na baixa](http://tdn.totvs.com.br/pages/releaseview.action?pageId=6070980)
