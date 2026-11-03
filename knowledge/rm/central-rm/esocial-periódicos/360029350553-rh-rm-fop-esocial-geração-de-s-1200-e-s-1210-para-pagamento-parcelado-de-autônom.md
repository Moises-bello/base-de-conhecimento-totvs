---
article_id: 360029350553
category: esocial - Periódicos
content_hash: 875bd1ba05f6ddbf36f6c9277297bb675f3959426c75a1567d553e3677c2e1d4
fetched_at: '2026-06-28T22:47:09.387947+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Geração de S-1200 e S-1210 para pagamento parcelado
  de autônomo do Fluxus
type: support-article
updated_at: '2026-02-02T14:37:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029350553-RH-RM-FOP-eSocial-Gera%C3%A7%C3%A3o-de-S-1200-e-S-1210-para-pagamento-parcelado-de-aut%C3%B4nomo-do-Fluxus
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15833106722711)**Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como enviar os eventos **S-1200** e **S-1210** para transportador autônomo cadastrados no **TOTVS Gestão Financeira** quando é feito pagamento de forma parcelada?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
Para realizar corretamente a geração dos eventos, siga os passos abaixo:  
1. No TOTVS Folha de Pagamento, acesse **Administração de Pessoal | Cliente e Fornecedor;**  
2. Na aba **Identificação**preencha os campos **Data de Nascimento** e **Categoria**, além dos demais campos obrigatórios;

![](http://tdn.totvs.com/download/attachments/499105902/image2018-12-5_18-13-21.png?version=1&modificationDate=1562268000590&api=v2)

3. Na aba **Tributos**, preencha os campos **Número do Contribuinte**, **CBO Autônomo**, **Código da Receita** e **NIT**, além dos demais obrigatórios;

![](http://tdn.totvs.com/download/attachments/499105902/image2018-12-5_17-36-35.png?version=1&modificationDate=1562268000490&api=v2)

4. Na aba **eSocial**preencha o campo **Código da categoria eSocial**;

![](http://tdn.totvs.com/download/attachments/499105902/image2018-12-5_17-37-50.png?version=1&modificationDate=1562268000627&api=v2)

No lançamento do cliente fornecedor deve existir uma baixa parcial para que no **S-1210** a tag <indPgtoTt> e os demais campos do grupo <infoPagtoParc> sejam considerados no XML.  
  
**Importante**  
A partir da versão 12.1.25.00, será disponibilizado o anexo do **eSocial**, que irá substituir o item **Integrações | eSocial**

**![](http://tdn.totvs.com/download/attachments/499105902/image2019-6-21_13-50-6.png?version=1&modificationDate=1562268000657&api=v2)**

**![](http://tdn.totvs.com/download/attachments/499105902/image2019-6-21_13-52-39.png?version=1&modificationDate=1562268000693&api=v2)**

**Saiba mais**   
Acesse as páginas abaixo para mais detalhes e exemplos do processo supracitado:

* [S-1200 e S-1210 - Autônomos cadastrados no Financeiro - Pagamento Parcelado](http://tdn.totvs.com/pages/releaseview.action?pageId=499105902)
* [Baixa Parcial de Lançamento Financeiro](http://tdn.totvs.com/display/public/LRM/Baixa+Parcial)
