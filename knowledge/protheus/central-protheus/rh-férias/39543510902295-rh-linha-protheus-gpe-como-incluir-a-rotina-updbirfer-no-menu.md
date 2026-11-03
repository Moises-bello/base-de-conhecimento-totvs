---
article_id: 39543510902295
category: RH - Férias
content_hash: 62c21c1a0bb93c9b6756f3570c7538f141bed156b82f9e4f5bd7c3e9ac57c87d
fetched_at: '2026-06-28T22:43:58.159829+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Como incluir a rotina UPDBIRFER  no menu
type: support-article
updated_at: '2026-04-06T16:41:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39543510902295-RH-Linha-Protheus-GPE-Como-incluir-a-rotina-UPDBIRFER-no-menu
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39543510859287) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como incluir a rotina UPDBIRFER  no menu?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para incluir a rotina de UPDBIRFER no menu, realize os seguintes passos:

**1.** Execute o backup do arquivo **sigagpe.xnu** na pasta **system** do Protheus;  
**2.** Acesse o Configurador **SIGACFG** em **Ambiente > Cadastros > Menus (CFGX013)**;  
  
 ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39543510860823)  
  
**3.** Selecione o Ambiente que deseja editar o menu e Clique em **OK**. No exemplo utilizaremos o **SIGAGPE - Gestão de Pessoal**;  
 ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39543510863255)  
  
 **4.** Selecione do lado esquerdo **Menu** já existente e clique em **Adicionar** para copiá-lo para novo layout;  
   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39543512567575)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39543512572055)

**5.** Selecione no lado direito o **Menu** que seja ajustar;

**6.** Para **Adicionar** novo Item, selecione a pasta e clique em **Novo Item**. Nesse exemplo selecionamos a pasta Miscelânea > Esocial > Middleware;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39543512574487)

**7.** Preencha campos de acordo com a rotina que deseja incluir e clique em **Ok**. Nesse exemplo faremos a inclusão da rotina **UPDBIRFER**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39543512576279)

**8.** Clique em **gerar**, informe nome do arquivo, neste exemplo **SIGAGPE** (sem extensão) a ser salvo e clique em **gerar** novamente;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39543510873623)![](https://centraldeatendimento.totvs.com/hc/article_attachments/39543512578455)

Para que a nova rotina seja apresentada no menu do módulo selecionado, saia do sistema e entre novamente.

**Saiba mais:**

[Criação id's 1562, 1722 e 1723](https://tdn.totvs.com/pages/viewpage.action?pageId=394210801)

[RH - Férias](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597291-RH-F%C3%A9rias)
