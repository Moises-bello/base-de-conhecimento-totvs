---
article_id: 5372248562839
category: Configurações
content_hash: ea35fc180cd995f131eb49a4d276f934241dec23ca5467e7b94291ccb23062a3
fetched_at: '2026-06-28T22:46:49.526503+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: RH - RM - FOP - Conversão do Rateio por Tomador
type: support-article
updated_at: '2024-09-04T13:55:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5372248562839-RH-RM-FOP-Convers%C3%A3o-do-Rateio-por-Tomador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26125617257239)Tempo aproximado para leitura: **00:03:20 min  
  
Dúvida**  
Como realizar a conversão do Rateio por Tomador?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para solucionar essa dúvida, acesse: **Configurações | Conversor Histórico Rateio Tomador.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5372096078743)**Este processo tem o objetivo de preencher o histórico de tomador de serviço conforme opções abaixo:  
  
Nessa tela é possível realizar a seleção dos funcionários e a forma de conversão.

* **Considerar apenas rateio atual:** O sistema irá verificar o cadastro do rateio de tomador atual e preencherá o histórico.
* **Considerar movimento distribuído de competências anteriores:** O usuário deverá informar a **Competência Inicial** e o **Evento base para Rateio**, com isso o sistema irá alimentar o histórico a partir da competência informada até a competência anterior a atual com os tomadores encontrados no Movimento Distribuído por Tomador para o evento selecionado. Para a competência atual o sistema alimenta o histórico com o rateio atual de tomador.
* **Regerar histórico:** Está opção deleta todos os históricos existentes, conforme filtro cadastrado e refaz o processo de conversão conforme opções acima.

**Importante**Para preenchimento do campo **Competência Inicial** no histórico o sistema verifica a opção selecionada, conforme abaixo:

* Ao selecionar a opção **Considerar apenas rateio atual** preencherá com o mês e ano da competência atual.
* Ao selecionar a opção **Considerar movimento distribuído de competências anteriores** preencherá com o mês e ano competência existente no movimento do tomador, para a competência atual o sistema alimenta com o mês e ano competência atual.

Caso seja necessária alguma alteração poderá ser feita manualmente pelo histórico ou pela importação de dados.  
  
**Saiba Mais**  
[Conversor Histórico Rateio Tomador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=454831887)  
[RH - RM - FOP - Histórico de Rateio de Tomadores](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028619192-RH-RM-FOP-Hist%C3%B3rico-de-Rateio-de-Tomadores)
