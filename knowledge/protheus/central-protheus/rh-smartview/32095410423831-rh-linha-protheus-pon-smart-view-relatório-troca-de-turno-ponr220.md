---
article_id: 32095410423831
category: RH - Smartview
content_hash: 28ef05f0ba42761284fd26e082a27fae2552b6224718a6c88c038afd924d0ad0
fetched_at: '2026-06-28T22:44:42.036231+00:00'
product: protheus
section_id: 32419360907799
source: central-protheus
title: RH - Linha Protheus - PON - Smart View - Relatório Troca de Turno (PONR220)
type: support-article
updated_at: '2025-06-02T17:37:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32095410423831-RH-Linha-Protheus-PON-Smart-View-Relat%C3%B3rio-Troca-de-Turno-PONR220
---

**Dúvida**Como gerar o relatório **Smart View da troca de turno**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**Utilização do relatório de troca de turno via Smart View.  
  
**Solução**Para efetuar as configurações e liberação de *MENU* do relatório **Troca de turno via *Smart view*** a premissa é de que o ambiente esteja configurado o *SMART VIEW*, siga a documentação: <https://tdn.totvs.com/pages/releaseview.action?pageId=834823409>  
  
Após garantir a configuração e estando funcional o *Smart view* siga para configuração e utilização do relatório troca de turno no *Smart View.* Primeiramente se tem por necessidade a liberação do *MENU* no PROTHEUS. Sendo assim, no Configurador(**SIGACFG**) acesse em **Ambiente-Cadastros-Menus**, selecione o **Ponto Eletrônico** e cilque em **ok**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32095410396823)  
  
Clique em adicionar todos os MENUS:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32095410396951)  
  
Recomendamos que crie o MENU abaixo de 'Relatórios'. Ao selecionar '&Relatorios' clique em 'Novo Item':  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32095376014743)  
  
Preencha as informações de acordo com o exemplo a seguir:  
  
**Dica:** A descrição do relatório fica a seu critério. Ao informar a descrição esta será apresentada no *Smart View*. Portanto, procure deixar a descrição mais clara possível.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32095376014999)  
  
Após isto, clique em ok e 'Gerar' preencha com o SIGAPON e clique em 'Gerar', veja:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32095410400663)  
  
Confirma a geração do MENU e clique em **Sim** para efetuar o *backup* dos MENUS anteriores. Após isto, clique em fechar e abra o *Smartclient.*  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32095376016919)  
  
Ao abrir o *Smartclient*, acesse o caminho do relatório, exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32095410402711)  
  
Após abrir o relatório via *Smartclient*, será possível acessa-lo via *Smart View:*![](https://centraldeatendimento.totvs.com/hc/article_attachments/32095410403095)  
  
Acesse o *Smart View* com *login* e senha configurado e busque por relatórios:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32095410404119)  
Clique em Visualizar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32095410404759)  
Preencha os parâmetros de acordo com sua necessidade:  
Importante:  
Para listar o relatório o turno e regra de/para tem que estar preenchido com base na troca de turno do funcionário.

Veja exemplo abaixo:  
Funcionário teve a seguinte troca de turno:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32095376020375)  
  
No relatório tem que passar no parâmetro 'Turno De?' o turno anterior e 'Turno Para?' o turno atual:  
Importante: O mesmo se aplica na 'Regra de?' e 'Regra Para?'  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32095376020887)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32095410407319)

Veja que foi listado de acordo com a troca de turno: **![](https://centraldeatendimento.totvs.com/hc/article_attachments/32095376022295)****Saiba Mais:**[DT Smart View - Relatório Troca de Turno (PONR220)](https://tdn.totvs.com/pages/viewpage.action?pageId=800581574)  
[RH - Linha Protheus - PON - Como funciona a Troca de Turno dos funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015528671-RH-Linha-Protheus-PON-Como-funciona-a-Troca-de-Turno-dos-funcion%C3%A1rios)  
[RH - Linha Protheus - PON - Como cadastrar um Turno de Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410322419095-RH-Linha-Protheus-PON-Como-cadastrar-um-Turno-de-Trabalho)[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download?e=1080347)  
  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
