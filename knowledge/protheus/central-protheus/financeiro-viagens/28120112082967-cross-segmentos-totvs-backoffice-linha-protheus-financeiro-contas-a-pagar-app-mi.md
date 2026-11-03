---
article_id: 28120112082967
category: Financeiro - Viagens
content_hash: e2a78794c30ddbd036f2adae80befae50ec1f22d76f78661ce88aac099f9ab34
fetched_at: '2026-06-28T22:38:21.320547+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Contas a
  Pagar - App Minha Prestação de Contas não aparece as filiais pós login
type: support-article
updated_at: '2024-11-28T11:29:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28120112082967-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Financeiro-Contas-a-Pagar-App-Minha-Presta%C3%A7%C3%A3o-de-Contas-n%C3%A3o-aparece-as-filiais-p%C3%B3s-login
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28120095515415) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No App Minha Prestação de Contas, ao realizar login, não apresenta as filiais de acesso.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/28120095516183)**

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre, pois a parametrização do sistema pode estar incorreta para uso do **App Minha Prestação de Contas**  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Verifique inicialmente no **SIGACFG >> Usuários >> Usuários**, se o participante possui acesso ao grupo/filial

2. No ini do **REST**, verifique se está passando corretamente as chaves de validação de **Grupo/Filiais de acesso**

**Acesse a documentação: [Configuração do REST Protheus para uso com os aplicativos Mobile](https://tdn.totvs.com/pages/releaseview.action?pageId=519719292)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28120112068119)

3. Verifique se a chave **AllowOrigin** está com **\* (Asterisco)** e os ip´s abaixo estão liberados no servidor

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28120112068759)  
  
A chave **AllowOrigin** indica de quais ip's o **REST** pode responder. Quando o valor é **\* (asterisco),** indica que o Protheus pode responder para qualquer ip.  
  
Para utilização dos Apps, é possível limitar o acesso apenas para os ranges de ip's do Mingle listados abaixo:  
  
**34.66.1.67**  
**34.66.27.255**  
**34.121.152.77**  
**34.122.88.30**  
**146.148.50.219**  
**104.155.181.56**  
**34.28.132.209**  
**35.225.171.255**  
**34.69.186.150**

**Saiba mais**[Guia de uso - Minha Prestação de Contas](https://tdn.totvs.com/pages/releaseview.action?pageId=287057777)  
[Viagens - Financeiro - P12](https://tdn.totvs.com/display/public/PROT/Viagens+-+Financeiro+-+P12)

[Configuração do REST Protheus para uso com os aplicativos Mobile](https://tdn.totvs.com/pages/releaseview.action?pageId=519719292)
