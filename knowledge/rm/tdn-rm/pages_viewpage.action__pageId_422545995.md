---
content_hash: 5f40857989ada23ac0e79b16866ddd09a75e956dcdaf44c9bd4956837e23ab24
fetched_at: '2026-06-29T00:09:22.540935+00:00'
page_id: '422545995'
product: rm
source: tdn-rm
title: Gerar Lançamento Financeiro (Fiscal)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545995
version: 4
---

Através deste processo o usuário poderá integrar os Lançamentos Fiscais ao TOTVS Gestão Financeira. O TOTVS Gestão Fiscal irá gerar somente lançamentos do Tipo Nota Fiscal, independente do Modelo do Documento Fiscal, no TOTVS Gestão Financeira. As faturas vinculadas aos lançamentos, deverão ser criadas através do TOTVS Gestão Financeira.   
Caso o campo "Default para série do Documento" no cadastro do Tipo de Documento estiver em branco e no TOTVS Gestão Fiscal o Lançamento Fiscal estiver com Série Nula, durante a integração o sistema preencherá o campo Serie do Lançamento Financeiro com '@@@', conforme determinado pelo TOTVS Gestão Financeira.  
*****Observações*:****O sistema não permite a Integração de lançamentos para o TOTVS Gestão Financeira se o Lançamento Fiscal foi originado do TOTVS Gestão de Estoque e Faturamento.  
Ao Integrar Lançamentos Fiscais o número do documento sempre será preenchido com o número do documento do Lançamento Fiscal, independente dos parâmetros "Gerar Número do Documento Sequencialmente" e "Copiar Ref. para N° do documento" no TOTVS Gestão Financeira.
