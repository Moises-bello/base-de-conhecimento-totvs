---
article_id: 360024937972
category: NFe - Nota Fiscal Eletrônica
content_hash: 29b98439f6b976daa8b0b8714d60c67cf7903e8bdc9db84b9d1c374e3abb4ab8
fetched_at: '2026-06-28T22:40:05.530718+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 938 Rejeição :
  Não informada vBCSTRet, pST, vICMSSubstituto e vICMSSTRet'
type: support-article
updated_at: '2025-08-04T15:16:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024937972-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-938-Rejei%C3%A7%C3%A3o-N%C3%A3o-informada-vBCSTRet-pST-vICMSSubstituto-e-vICMSSTRet
---

**Dúvida**Como solucionar a rejeição 938 Rejeição : Não informada vBCSTRet, pST, vICMSSubstituto e vICMSSTRet?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Ao utilizar o ICMS60 para destinatário diferente de ***consumidor final, sendo a tag* "indFinal=0"** será necessário gerar as TAGS, ***vBCSTRet, pST, vICMSSubstituto e vICMSSTRet*** validação é  a critério da UF.

**​**

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **editar** ***MV\_ULTAQUI  =*** 1 - Considerar valores ***somente da última aquisição***, 2 - Considera as ***últimas aquisições até compor a quantidade da venda*** ou 3- Considera as últimas aquisições até compor a ***quantidade da venda, respeitando a média por nota fiscal.***

***![20220321_104749.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4906031932567)***

    2. Configurar o TES ***conforme os campos abaixo:***

Calcula ICMS **(F4\_ICM)** = Não  
  
Sit Trib ICMS **(F4\_SITTRIB)** = 60  
  
Inf ST Ant **(F4\_ART274)** = 1  
  
LF ICMS-ST **(F4\_LFICMST)** = Não  
  
L. Fisc. ICMS **(F4\_LFICM)** = Outros ou ISENTO 

![20220321_110157.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4906662444439)

* **Saiba Mais**

O correto é o seu XML gerar ao menos com todas as ***TAGS zeradas conforme o exemplo abaixo, para o CST 60 ou 500:*  
  
![](https://totvssuporte.zendesk.com/attachments/token/9FvNcA4pqRMRryBI9giXtWgU9/?name=inline-1787686614.png)**

**1. Atualização do ambiente TSS (repositório e schemas)**

1. Atualizar o **repositório** com o último pacote de **expedição continua do TSS** disponível no link:

[MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981)

    2. Atualizar a pasta **SCHEMAS** presente na estrutura do TSS através do link:

<https://suporte.totvs.com/portal/p/10098/download?e=761857>

**Saiba Mais:** [TSS - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552)

**2. Atualização do ambiente Protheus:**

1. Aplicar o **Pacote Acumulado Documentos eletrônicos:**

[Clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=525010692)

     2. **Compilar RDMAKE NFESEFAZ** (se emitir NF-e) presente no link abaixo:

<https://suporte.totvs.com/portal/p/10098/download?e=1083729>

**​**Ou gerar todas as TAGs com os ***valores do ICMS60 conforme o exemplo abaixo:*  
  
![](https://totvssuporte.zendesk.com/attachments/token/ChnWqLqQ1iBUBuCUpRhSKqUsM/?name=inline816381121.png)**

* Para adquirir ***mais conhecimento*** sobre esse assunto, acesse os links abaixo:

*[Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025598751)*

*[Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025305012)*
