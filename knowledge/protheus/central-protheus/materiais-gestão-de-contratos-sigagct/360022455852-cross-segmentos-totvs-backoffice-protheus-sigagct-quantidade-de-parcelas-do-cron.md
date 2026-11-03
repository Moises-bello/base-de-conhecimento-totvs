---
article_id: 360022455852
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: c3fb2567c705a76a1d38ba9ceeee0c4e8e166965a2dd59bd642986354b1de997
fetched_at: '2026-06-28T22:37:20.156157+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quantidade de parcelas
  do Cronograma Financeiro por Condição Pagamento
type: support-article
updated_at: '2024-11-11T12:09:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022455852-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Quantidade-de-parcelas-do-Cronograma-Financeiro-por-Condi%C3%A7%C3%A3o-Pagamento
---

**Dúvida**Cálculo de quantidade de competências do cronograma financeiro por Condição Pagamento  
  
**Ambiente**Microsiga Protheus - Gestão de contratos - à partir da versão 12  
  
**Solução**A geração do cronograma com Periodicidade como "Condição de Pagamento", passa a considerar o parâmetro/pergunte (***CN300CRG03***) de Quantidade de Parcelas, Condição de Pagamento informada e data final do contrato.

Exemplo:  
Para contrato com vigência de 12 meses, data de início= 08/03/2018 e data final= 08/03/2019.

* Periodicidade = Cond Pgto
* Data prevista da 1º medição= 12/03/2018
* Quantidade de parcelas= 4
* Condição de pagamento= 3x

Neste exemplo o cronograma será gerado com 12 parcelas.

Cálculo realizado pelo sistema:  
*(Quantidade de parcelas (4) x Quantidade de parcelas da condição de pagamento(3))*

***Obs.1:***

Caso se deseje que as parcelas do cronograma sejam conforme apenas a condição de pagamento "pura", deve-se deixar o parâmetro "Quantidade de Parcelas" (***CN300CRG06***) igual a "0" ou "1".

O Parâmetro referente a "Dia(s)" (***CN300CRG02***) na elaboração do cronograma, quando utilizar a periodicidade Condição Pagamento não é considerado e ao informar dias no campo é apresentando alerta.

***Obs.2***:

O uso da Condição de Pagamento no opção "Periodicidade = Cond Pgto" serve apenas para se montar as parcelas no momento da criação do Cronograma Financeiro a ser criado, e não para uso posterior no Contrato.

***Obs.3:***  
**MV\_CNFVIGE** -> permitir a inclusão de cronograma financeiro contendo parcelas com previsão superior a data de vencimento do contrato.

***Obs.4:***

No uso desta Periodicidade = Cond Pagto pra montagem das parcelas do cronograma financeiro, a informação do parâmentro "Data prevista da 1º medição" (***CN300CRG05***) tem a funcionaldiade de ser a "data de referência" para geração das parcelas conforme a Condição de Pagamento indicada, e assim não necessariamente a primeira medição terá a data prevista conforme a data informada neste parâmetro.

Por exemplo: Se for escolhida uma condição de pagamento "30 dias" a primeira medição terá data de vencimento com 30 dias após a data informada no parâmetro "Data prevista da 1º medição" (***CN300CRG05***) e conforme o artigo abaixo, a data prevista da primeira medição será a mesma do vencimento da parcela:

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Na inclusão do Cronograma Financeiro do Contrato os campos de Vencimento (CNF\_DTVENC) e Data Prevista Medição (CNF\_PRUMED) ficam iguais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4474997200407-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Na-inclus%C3%A3o-do-Cronograma-Financeiro-do-Contrato-os-campos-de-Vencimento-CNF-DTVENC-e-Data-Prevista-Medi%C3%A7%C3%A3o-CNF-PRUMED-ficam-iguais)

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
