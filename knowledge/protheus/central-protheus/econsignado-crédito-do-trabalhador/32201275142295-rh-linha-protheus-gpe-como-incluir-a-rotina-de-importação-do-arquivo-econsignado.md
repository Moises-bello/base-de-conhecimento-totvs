---
article_id: 32201275142295
category: eConsignado (Crédito do Trabalhador)
content_hash: 103f423c2586b0e1fe0e72bdef3c7f827d5dae91bf695451260c47756e5d484c
fetched_at: '2026-06-28T22:43:07.413901+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Como incluir a rotina de Importação do arquivo
  eConsignado GPEM944 no menu
type: support-article
updated_at: '2025-09-02T10:45:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32201275142295-RH-Linha-Protheus-GPE-Como-incluir-a-rotina-de-Importa%C3%A7%C3%A3o-do-arquivo-eConsignado-GPEM944-no-menu
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32201275136151) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como incluir a rotina de Importação eConsignado GPEM944 no menu?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - Todas as versões  
  
**Solução**Para incluir a rotina Importação do arquivo do eConsignado (GPEM944) no menu, realize os seguintes passos:

**1.** Execute o backup do arquivo **sigagpe.xnu** na pasta **system** do Protheus;  
**2.** Acesse o Configurador **SIGACFG** em **Ambiente > Cadastros > Menus (CFGX013)**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32202522765079)  
  
**3.** Selecione o Ambiente que deseja editar o menu e Clique em OK. No exemplo utilizaremos o SIGAGPE - Gestão de Pessoal;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32202522768151)

**4.** Selecione do lado esquerdo **Menu** já existente e clique em **Adicionar** para copiá-lo para novo layout;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32202532136471)

**5.** Selecione no lado direito o **Menu** que seja ajustar;

**6.** Para **Adicionar** novo Item, selecione a pasta e clique em **Novo Item**. Nesse exemplo selecionamos a pasta Importação;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32202532137623)

**7.** Preencha campos de acordo com a rotina que deseja incluir e clique em **Ok**. Nesse exemplo faremos a inclusão da rotina **GPEM944** Importação do arquivo eConsignado;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32202532138391)

**8.** Clique em **gerar**, informe nome do arquivo, neste exemplo **SIGAGPE** (sem extensão) a ser salvo e clique em **gerar** novamente;

![](https://i.imgur.com/7OMRxem.png)

Para que a nova rotina seja apresentada no menu do módulo selecionado, saia do sistema e entre novamente. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32202522771607)

**Saiba mais:**

[Crédito do Trabalhador - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)

[Artigos Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
