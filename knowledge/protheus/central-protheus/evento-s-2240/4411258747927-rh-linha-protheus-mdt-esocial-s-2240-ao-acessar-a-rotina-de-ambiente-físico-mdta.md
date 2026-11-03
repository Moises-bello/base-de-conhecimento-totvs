---
article_id: 4411258747927
category: Evento S-2240
content_hash: 516946bf9478b2e023e4e9662ab02e05df86acb53ce48e666349f405cc667462
fetched_at: '2026-06-28T22:45:23.535112+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2240 - Ao acessar a rotina de Ambiente
  Físico (MDTA165), os campos Tp. Inscr. (TNE_TPINS), Nr. Inscr. (TNE_NRINS) ou Cod.
  Lot. (TNE_CODLOT) estão bloqueados
type: support-article
updated_at: '2025-03-03T18:05:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411258747927-RH-Linha-Protheus-MDT-eSocial-S-2240-Ao-acessar-a-rotina-de-Ambiente-F%C3%ADsico-MDTA165-os-campos-Tp-Inscr-TNE-TPINS-Nr-Inscr-TNE-NRINS-ou-Cod-Lot-TNE-CODLOT-est%C3%A3o-bloqueados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372461650583) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao acessar a rotina de Ambiente Físico (MDTA165), o sistema exige que os campos Tipos de Inscrição (TNE\_TPINS), Número Inscrição. (TNE\_NRINS) ou Cod. Lot. (TNE\_CODLOT) sejam preenchidos para envio do evento S-2240 ao eSocial, porém os campos estão apenas em modo de visualização (bloqueados), como preenche-los?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**De acordo com a documentação do migrador **UPDDISTR** referente a tabela **SX3** ([Regras para atualização do dicionário SX3 - UPDDISTR e migrador de versão](https://tdn.totvs.com/pages/viewpage.action?pageId=181965333)) a alteração do **X3\_TITULO, X3\_PICTURE** e **X3\_WHEN** dos campos é realizada apenas em alguns cenários específicos para cada ambiente e, caso não tenha sido realizada, é necessário o ajuste manual conforme abaixo: **1**- Acessar o módulo do Configurador (**SIGACFG**) e selecionar as opções do menu: B**ase de dados/Dicionário/Base de Dados**.  
**2**- Pesquisar pela Tabela **TNE**:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411241759895)  
  
**3**- Clicar na opção de **Editar** para editar a tabela:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411250183063)  
  
**4**- Selecionar o campo **TNE\_TPINS**, selecionar a opção de Editar, selecionar a pasta "**Opções**" e limpar o conteúdo do campo "**Modo Edição**":  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411258579351)  
  
**5**- Selecionar o campo **TNE\_NRINS**, selecionar a opção de Editar, selecionar a pasta "**Campo**" e caso o conteúdo do campo "**Formato**" estiver diferente de "**@!**" definir esse valor:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411250245527)  
  
**6**- Selecionar a pasta "**Opções"** e limpar o conteúdo do campo "**Modo Edição**":  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411258614935)  
  
**7**- Selecionar o campo **TNE\_CODLOT**, selecionar a opção de Editar, selecionar a pasta "**Informaçõe**s" e alterar o conteúdo do campo "**Título**" de "Cod. Lot." para "**Centro Custo**":  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411250275863)  
  
**8**- Selecionar a pasta "**Opções**" e limpar o conteúdo do campo "**Modo Edição**":  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411258682647)  
  
**9**- Após, salvar e confirmar a tela:  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411250315415)  
  
**10**- E por fim, clicar no **disquete** para que as alterações sejam salvas:  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411250334615)  
  
**Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
