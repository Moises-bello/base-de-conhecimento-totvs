---
article_id: 34817817809943
category: eConsignado (Crédito do Trabalhador)
content_hash: 1b2695e633f3a1df412a1abb23e88a4bcda5e7aa052cb758fb84b004b39dba27
fetched_at: '2026-06-28T22:43:07.232438+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Como incluir a rotina Painel de Importação do arquivo
  eConsignado GPEM815A no menu
type: support-article
updated_at: '2025-09-09T20:17:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34817817809943-RH-Linha-Protheus-GPE-Como-incluir-a-rotina-Painel-de-Importa%C3%A7%C3%A3o-do-arquivo-eConsignado-GPEM815A-no-menu
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34817817761047) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como incluir a rotina Painel de Importação do arquivo eConsignado GPEM815A no menu?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para incluir a rotina Painel de Importação do arquivo eConsignado GPEM815A no menu, realize os seguintes passos:

**1.** Execute o backup do arquivo **sigagpe.xnu** na pasta **system** do Protheus;  
**2.** Acesse o Configurador **SIGACFG** em **Ambiente > Cadastros > Menus (CFGX013)**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34817803369623)  
  
**3.** Selecione o Ambiente que deseja editar o menu e Clique em OK. No exemplo utilizaremos o SIGAGPE - Gestão de Pessoal;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34817803374999)

**4.** Selecione do lado esquerdo **Menu** já existente e clique em **Adicionar** para copiá-lo para novo layout;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34817803378839)

**5.** Selecione no lado direito o **Menu** que seja ajustar;

**6.** Para **Adicionar** novo Item, selecione a pasta e clique em **Novo Item**. Nesse exemplo selecionamos a pasta Importação;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34817817767447)

**7.**Preencha campos de acordo com a rotina que deseja incluir e clique em **Ok**. Nesse exemplo faremos a inclusão da rotina Painel de Importação do arquivo eConsignado **GPEM815A** ;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34817803381399)

**8.** Clique em **gerar**, informe nome do arquivo, neste exemplo **SIGAGPE** (sem extensão) a ser salvo e clique em **gerar** novamente;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34817817769367)

Para que a nova rotina seja apresentada no menu do módulo selecionado, saia do sistema e entre novamente. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34817803383575)  
  
Ao acessar a rotina, ela terá esta visualização:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34817817772439)

**Saiba Mais**

[Manual do Crédito Consignado do Trabalhador](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-operacional-do-empregador-programa-credito-do-trabalhador-v2-16-05-25.pdf)

[Orientações Consultoria de Segmentos - Crédito do Trabalhador](https://tdn.totvs.com/pages/releaseview.action?pageId=939253541#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosCr%C3%A9ditodoTrabalhador-3.7.2Ovalordoabonopecuni%C3%A1riodevecomporaremunera%C3%A7%C3%A3odispon%C3%ADvelparadescontodocr%C3%A9ditodotrabalhador?)

[Manual Crédito do Trabalhador Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)

[eConsignado (Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/32292829000215-eConsignado-Cr%C3%A9dito-do-Trabalhador)
