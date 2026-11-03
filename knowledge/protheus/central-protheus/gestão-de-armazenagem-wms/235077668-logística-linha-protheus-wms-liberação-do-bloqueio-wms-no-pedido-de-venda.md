---
article_id: 235077668
category: Gestão de Armazenagem (WMS)
content_hash: c5252caeabba03fdfefd04c16b725723745804eb084b607d33435dc93dbeff98
fetched_at: '2026-06-28T22:45:48.054863+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - Liberação do Bloqueio WMS no pedido de venda
type: support-article
updated_at: '2025-10-31T19:59:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/235077668-Log%C3%ADstica-Linha-Protheus-WMS-Libera%C3%A7%C3%A3o-do-Bloqueio-WMS-no-pedido-de-venda
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35446964185879)**Tempo aproximado para leitura: **00:01:40 min  
  
Dúvida**Onde é efetuada a liberação do Bloqueio **WMS** ***- Warehouse Management System** -* para o pedido de venda?  
  
**Ambiente**TOTVS Logística - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (WMS) - Versão 12  
  
**Solução**O processo de liberação do bloqueio **WMS** no pedido, campo **Bloqueio WMS** - **C9\_BLWMS**, pode ocorrer em uma série de etapas distintas de acordo com algumas regras do cadastro **Serviços Vs Tarefas - WMSA070**:

1. Tarefa Separação;
2. Tarefa Conferência;
3. Conferência Expedição;
4. Liberação Manual;
5. Romaneio Embarque - Novo **WMS**;
6. Montagem Volume - Novo **WMS**.

Caso esteja parametrizado para efetuar a liberação na **1 - Tarefa de Separação** ou **2 - Tarefa de Conferência**, somente será liberado nestas situações se não existir montagem de volumes. Havendo montagem de volumes, a liberação será efetuada após a finalização da montagem dos volumes.  
  
A liberação será dependente de existir o respectivo processo, ou seja, só será efetuada a liberação na tarefa de conferência, se existir a tarefa de conferência. Do contrário, será liberado no processo anterior, neste exemplo, ao final da separação. O mesmo princípio se aplica a conferência expedição e a montagem de volumes.  
  
Quando parametrizado para efetuar a liberação manual, deverá ser feita a liberação pela rotina **Conferência de Expedição - WMSA412** de forma manual, após o processo de conferência.  
  
Quando feita montagem de volumes no processo **WMS**, a liberação ocorre automaticamente ao finalizar toda a montagem de volumes do pedido. Se utilizada a opção **5 - Romaneio Embarque**, os volumes montados ficarão bloqueados para faturamento, sendo liberados somente através da rotina de **Romaneio de Embarque - WMSV105**. Ainda no processo de montagem de volumes poderá ser liberado um volume em particular para faturamento, efetuando nesta situação uma liberação parcial do pedido de venda para o faturamento.  
  
**Importante**  
As opções de liberação via **5 - Montagem de Volume** e **6 - Romaneio de Embarque**, somente são aplicadas ao **novo WMS**.  
  
**Saiba mais**  
Assista ao *Webinar* sobre o cadastro **Serviços** **Vs** **Tarefas** e conheça todas as configurações disponíveis: [Webinar TOTVS | Serviços](https://www.youtube.com/watch?v=f1K8WBRCUUc) [Vs Tarefas #TOTVS\_Logística\_Linha\_Protheus](https://www.youtube.com/watch?v=f1K8WBRCUUc)
