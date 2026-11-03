---
content_hash: 5b55be515e9631a57239afc74b0659a8cc100003bc90a4f6882282f0ca7ad8a6
fetched_at: '2026-06-29T00:09:20.490584+00:00'
page_id: '422545697'
product: rm
source: tdn-rm
title: Solicitar Exclusão de Toda Operação Contábil (Fiscal)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545697
version: 3
---

Depois que os lançamentos fiscais são integrados ao lote zero do TOTVS Gestão Contábil, esses lançamentos não poderão ser mais alterados. Se por algum motivo for necessário que estes lançamentos não sejam mais considerados na contabilidade, eles deverão ser estornados*.* Através desta ação, serão incluídos no TOTVS Gestão Contábil os lançamentos de estornos, que deverão ser integrados também ao lote zero para que estes cancelem os efeitos contábeis dos lançamentos originais. Desta forma, tanto os lançamentos estornados quanto os de estorno,  ficarão registrados na contabilidade, porém um anulando o efeito contábil do outro.  
 Quando uma operação contábil já tiver sido estornada ela não é considerada mais uma operação Ativa. Desta forma, através deste processo, poderá ser solicitada uma tarefa para excluir toda esta operação contábil. A solicitação desta tarefa será enviada ao TOTVS Gestão Contábil para que seja analisada. Se a solicitação desta tarefa for aceita, ela será executada pelo TOTVS Gestão Contábil, onde os lançamentos provenientes desta operação que já não está mais Ativa serão excluídos da base de dados, tanto os originais que foram estornados quanto os seus respectivos estornos. Se a solicitação não for aceita ela será cancelada e os lançamentos continuarão presentes na base de dados.
