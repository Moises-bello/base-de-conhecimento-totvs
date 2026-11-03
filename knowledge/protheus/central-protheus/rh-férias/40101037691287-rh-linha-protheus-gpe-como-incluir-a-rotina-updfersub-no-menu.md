---
article_id: 40101037691287
category: RH - Férias
content_hash: 534085154ec54a6294c6442d6abf46d9d33ca273605c1d0a2b5030c780944ec8
fetched_at: '2026-06-28T22:43:58.164561+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Como incluir a rotina UPDFERSUB no menu
type: support-article
updated_at: '2026-04-29T18:16:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40101037691287-RH-Linha-Protheus-GPE-Como-incluir-a-rotina-UPDFERSUB-no-menu
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40101037673495) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como incluir a rotina UPDFERSUB no menu?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para incluir a rotina UPDFERSUB no menu, realize os seguintes passos:

**1.** Execute o backup do arquivo **sigagpe.xnu** na pasta **system** do Protheus;  
**2.** Acesse o Configurador **SIGACFG** em **Ambiente > Cadastros > Menus (CFGX013)**;  
  
 ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40101037674647)  
  
**3.** Selecione o Ambiente que deseja editar o menu e Clique em **OK**. No exemplo utilizaremos o **SIGAGPE - Gestão de Pessoal**;  
 ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40100998607639)  
  
 **4.** Selecione do lado esquerdo **Menu** já existente e clique em **Adicionar** para copiá-lo para novo layout;  
   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40101037678487)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40101037678871)

**5.** Selecione no lado direito o **Menu** que seja ajustar;

**6.** Para **Adicionar** novo Item, selecione a pasta e clique em **Novo Item**. Nesse exemplo selecionamos a pasta **Miscelânea > Esocial > Middleware**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40101037679767)

**7.** Preencha campos de acordo com a rotina que deseja incluir e clique em **Ok**. Nesse exemplo faremos a inclusão da rotina **UPDFERSUB**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40101037681175)

**8.** Clique em **gerar**, informe nome do arquivo, neste exemplo **SIGAGPE** (sem extensão) a ser salvo e clique em **gerar** novamente;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40100998610455)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40101037682071)

Para que a nova rotina seja apresentada no menu do módulo selecionado, saia do sistema e entre novamente.

**Saiba Mais**  
[RH - Linha Protheus - GPE - Rdmake UPDFERSUB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/40095257246743-RH-Linha-Protheus-GPE-Rdmake-UPDFERSUB)  
[Substituição verbas Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=1014630057#body-body2)  
[RH - Férias](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597291-RH-F%C3%A9rias)
