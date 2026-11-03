---
article_id: 360058695713
category: Manutenção de Ativos (SIGAMNT)
content_hash: 953c76d1c289226d2d9917c019f761f4e9d3a70808028c4925db3bfc63ea5e20
fetched_at: '2026-06-28T22:42:34.406632+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Retirar permissão para finalizar ordem
  de serviço
type: support-article
updated_at: '2024-04-22T11:22:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058695713-Manufatura-Linha-Protheus-MNT-Retirar-permiss%C3%A3o-para-finalizar-ordem-de-servi%C3%A7o
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:01:30 min**  
**Dúvida**Como retirar a permissão de um **usuário** para finalizar uma **OS - Ordem de Serviço**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Versão 12  
  
**Solução**A permissão para finalizar uma **OS** deve ser realizada no cadastro de **Privilégios - CFGA530**no **SIGACFG**.   
  
1) Para a rotina **Fechamento em lote - MNTA510**, é necessário incluir essa rotina como acesso **NEGADO**;  
  
2) Para a rotina **Retorno - MNTA400**, apenas o botão **Final** deve ter o acesso **NEGADO**;  
  
3) Para a rotina **Retorno Mod. 2 - MNTA435**, o botão que efetua a finalização é o **Finalizar Ordem de Serviço**. Para bloqueio, sugerem-se: 

* Incluir essa rotina como acesso **NEGADO**nos **Privilégios**;
* Utilizar o **PE - Ponto de entrada** **MNTA435J**. Conforme *link* abaixo, no exemplo da documentação será retirado o botão **Finalizar Ordem de Serviço** para todos os usuários e deve ser substituído o conteúdo **oBtSpl** por **oBtFOS**. E é necessário criar a regra para que somente determinados usuários tenham esse botão visível;
* Utilizar o **PE** **MNT40011**. Caso seja configurado esse **PE**, refletirá também na rotina **Retorno - MNTA400**.

4) Para a rotina **Simplificado - MNTA415**, o botão que efetua a finalização é o **Finalizar O.S.**. Para o bloqueio, sugerem-se: 

* Incluir essa rotina como acesso **NEGADO**nos **Privilégios**;
* Utilizar o **PE** **MNT41502**.

5) Para a rotina **Retorno em lote - MNTA401**, é necessário incluir essa rotina como acesso **NEGADO**nos **Privilégios**;  
  
6) Para a rotina**Rateio de insumos - MNTA402**, a opção que efetua a finalização é a **Finalizar**. Para o bloqueio, sugerem-se: 

* Incluir essa rotina como acesso **NEGADO** nos **Privilégios**;
* ou utilizar o ponto de entrada **MNTA4021**.

7) Para a rotina de **Árvore lógica - MNTA902**, a permissão é realizada na rotina **Restrição Acesso - MNTA904**por meio da opção **Retornar ordem de serviço**, que quando desmarcada, inibe o botão **Retornar Ordem de Serviço**, e não permite com que o usuário finalize a **OS.**  
No caso do botão **Retornar Ordem de Serviço**da **Árvore lógica** precisar ser apresentado para o **usuário**, e restrinja somente a finalização de **OS**, verifique o **passo 3** acima, pois esse botão aciona a rotina **Retorno Mod. 2 - MNTA435**.  
  
**Saiba mais**  
Para informações complementares dos **PE** citados, verifique os *links*:  
[DT PE MNTA435J Seleciona os botoes que nao serao apresentados na EnchoiceBar](https://tdn.totvs.com/display/PROT/DT+PE+MNTA435J+Seleciona+os+botoes+que+nao+serao+apresentados+na+EnchoiceBar)  
[MNT40011 - Validação de Ordem de Serviço](https://tdn.totvs.com/pages/viewpage.action?pageId=6793526)  
[MNT41502 - Finalização de Ordem de Serviço](https://tdn.totvs.com/pages/viewpage.action?pageId=6793533)  
[DT PE MNTA4021 - Oculta o botão Finalizar do Rateio de Insumos (MNTA402)](https://tdn.totvs.com/pages/viewpage.action?pageId=526987610)
