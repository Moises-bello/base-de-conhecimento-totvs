---
article_id: 28623881406871
category: RH - Cadastros
content_hash: 343b9dabdb697b662150fc222fb9df74c62484f36a143aa0f617e57173b129ff
fetched_at: '2026-06-28T22:44:53.069403+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - PONA300 - Configuração para Faixa de Hora Extra
  Autorizada em Lote
type: support-article
updated_at: '2026-02-03T16:42:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28623881406871-RH-Linha-Protheus-PON-PONA300-Configura%C3%A7%C3%A3o-para-Faixa-de-Hora-Extra-Autorizada-em-Lote
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28623866663191) Tempo aproximado para leitura: **01:00:00 min**  
  
**Dúvida**  
Como configurar Faixa de Hora Extra em Lote?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
A funcionalidade da rotina Faixas de He Autorizadas é criarmos um intervalo de horas extras que será autorizado ao funcionário e em apontamento ser gerado o evento autorizado.  
  
Para isso, será necessário alterar o campo PA\_FAIXAHE (Faixa de Hora Extra) na regra de apontamento para SIM.  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/35943672685847)**  
  
Na rotina **PONA300**, em **Atualizações > Cadastro de Funcionários > Faixas de He Autorizadas.**  
Em caso de cadastros por funcionários, siga a documentação:  
[**RH - Linha Protheus - PON - PONA300 - Funcionalidade da rotina Faixa de Hora Extra Autorizada**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014909032-RH-Linha-Protheus-PON-PONA300-Funcionalidade-da-rotina-Faixa-de-Hora-Extra-Autorizada)  
  
Para efetuar os cadastros de **Faixas de He Autorizadas** de forma coletiva, siga a instrução abaixo:  
->Faixas de Horas Extras Autorizadas,em **outras** **ações > coletivas:**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/28625624863767)**  
  
-> Selecionar a opção **Gerar Horários** e após **Salvar:**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/28625624870935)**  
  
-> Preencher os parâmetros conforme a necessidade:  
No exemplo abaixo, foi preenchido a filial 01:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28625624878231)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28625578133399)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28625624885271)  
  
-> Selecionado todos os funcionários, com inclusão no dia 01/12 das 20hs ás 22hs:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28625624890135)  
  
-> Após salvar, gera o Log de ocorrência:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28625624893207)  
  
-> Informação na rotina:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28625578152599)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28625578156311)

**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
