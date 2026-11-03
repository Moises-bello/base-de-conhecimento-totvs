---
article_id: 360028703594
category: esocial - Processos
content_hash: 113d446b6156b9dd94c0f8a06dec64202aa0c4974272d6d489c064046796b72c
fetched_at: '2026-06-28T22:47:08.337327+00:00'
product: rm
section_id: 1500000834441
source: central-rm
title: RH - RM - FOP - eSocial - Distribuição de SEFIP de meses anteriores para tomadores
  de serviços em retificação
type: support-article
updated_at: '2024-06-04T18:59:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028703594-RH-RM-FOP-eSocial-Distribui%C3%A7%C3%A3o-de-SEFIP-de-meses-anteriores-para-tomadores-de-servi%C3%A7os-em-retifica%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21731606664343)**Tempo aproximado para leitura: **00:03:40 min**

**Dúvida**Como realizar a distribuição do SEFIP de meses anteriores para tomadores de serviços em retificação?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**O parâmetro **Distribuição de Retificação**será habilitado apenas para competências anteriores à atual, devendo ser informado o período de retificação para distribuição da movimentação por tomador. As opções disponíveis no grupo **Período**definirão para qual período do envelope será distribuída SEFIP e as opções disponíveis no grupo **Rateio tomador por**,definirão como será realizada a distribuição.

Para distribuição de meses anteriores, siga os passos abaixo:

1. Acesse **Encargos** | **SEFIP** | **Distribuir Sefip** e selecione a competência a ser distribuída;  
2. Informe se a distribuição retroativa será relacionada à retificação marcando o parâmetro **Distribuição de Retificação**;2.1. Com o parâmetro **Distribuição de Retificação**marcado, a distribuição será processada para o período que foi lançado a retificação no envelope e habilitará no grupo **Rateio tomador por** as opções **Histórico de Tomador**, **Tomadores da Competência Atual** ou **Rateio de eventos**;2.2. Com o parâmetro **Distribuição de Retificação** desmarcado, o sistema habilitará no grupo **Período** os parâmetros **Todos** e **Período**, permitindo distribuir SEFIP para todos os períodos ou um período específico do envelope. Será habilitado no grupo **Rateio tomador por,**as opções **Histórico de Tomador**e **Tomadores da Competência Atual**;3.  Selecione no grupo **Rateio tomador por** de qual forma será a distribuição de SEFIP, tendo como opções **Histórico de Tomador**, **Tomadores da Competência Atual** ou **Rateio de** **eventos.** 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21731606670999)

3.1. Selecionando **Tomadores da Competência Atual**, o rateio de tomador que a distribuição seguirá será o mesmo que estiver cadastrado no anexo **Rateio Tomador** do funcionário;  
3.2. Selecionando **Rateio de eventos**, deverá ser cadastrado em **Administração de Pessoal | Eventos | Rateio de Eventos** a composição do rateio que o sistema utilizará como base para realizar a distribuição;  
3.3. Selecionando **Histórico de Tomador** o rateio de tomador que a distribuição do período da retificação seguirá será o mesmo que estiver cadastrado no anexo **Histórico de Rateio por Tomador** do funcionário.

**Importante**Com o parâmetro **Sobrepor dados existentes** marcado o sistema substituirá o rateio existente no mês selecionado, pelo novo rateio que está sendo realizado. Com o parâmetro desmarcado, o sistema fará o rateio apenas para os eventos que não possuem distribuição no mês selecionado.  
  
**Saiba mais**   
Para mais informações acesse: 

* [Retificação de Rescisão](http://tdn.totvs.com/pages/releaseview.action?pageId=435110514#1-2)
* [Retificação da Folha de Pagamento](http://tdn.totvs.com/pages/releaseview.action?pageId=435110514#1-3)
