---
article_id: 360024716313
category: Portal de Gestão de Capital Humano
content_hash: fb524c1b123f5a31d2ee83b7d24eecfebcb5c4cdf85e414489612db442d90874
fetched_at: '2026-06-28T22:42:59.092071+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH - Ao logar no portal ocorre erro WSCERR064
  - Invalid Content Type
type: support-article
updated_at: '2021-04-07T13:13:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024716313-RH-Linha-Protheus-PORTAL-GCH-Ao-logar-no-portal-ocorre-erro-WSCERR064-Invalid-Content-Type
---

**Ocorrência**No Portal Gestão de Capital Humano, após configurar e acessar, ocorre o erro WSCERR064.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038653793/mceclip0.png)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Portal Gestão do Capital Humano - Todas as versões  
  
**Causa**Esse incidente ocorre por erro da configuração do APPSERVER.INI, em relação ao Web Service.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
**1.** É necessário configurar um **web service** para cada empresa/filial, ou seja, para cada empresa/filial, haverá um WebService e um respectivo Portal.  
  
**Observação:** Para acesso ao Portal existem licenças específicas que necessitam da contratação do cliente.  
Para informação de licença deverá entrar em contato com Executivo de Conta do seu ERP.  
  
**Por exemplo**:  
EMPRESA **T1** FILIAL **D MG 01** = Terá um link de WebService e será amarrado a um link do Portal Gestão do Capital Humano. Conforme imagem abaixo:   
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006443442/mceclip0.png)  
  
Se for utilizar o Portal em outra Empresa/Filial, deverá efetuar nova configuração e apontar os dados, ex: EMPRESA **T1** FILIAL **D MG 02** e gerar novo link conforme imagem acima.  
  
Para informações de configuração do Portal GCH, verifique o link [Como instalar e configurar o Portal Gestão do Capital Humano?](https://tdn.totvs.com/pages/releaseview.action?pageId=267806134)  
Para auxílio na Configuração do Portal GCH, entre em contato com suporte Framework.  
  
**2.** Verifique se o ambiente está atualizado com Pacote Acumulado RH e Arquivos do Portal, conforme links abaixo:   
[Pacote Acumulado RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)  
[Como Atualizar os arquivos do Portal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044250613-MP-PORTAL-GCH-Como-Atualizar-os-arquivos-do-Portal)  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)
