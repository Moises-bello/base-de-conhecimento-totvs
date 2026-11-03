---
article_id: 360007483711
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: e41cc257e1e1374832138c434a88b457000fa371d9bf84c8371c451d2b4b8046
fetched_at: '2026-06-28T22:41:48.267154+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - CENTRO DE CUSTO NO ATIVO
  FIXO - N3_CUSTBEM
type: support-article
updated_at: '2023-07-17T14:39:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007483711-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-CENTRO-DE-CUSTO-NO-ATIVO-FIXO-N3-CUSTBEM
---

**Dúvida**Utilização de centro de custo no ativo fixo  
  
**Ambiente**PROTHEUS – Ativo Fixo – A partir da versão 11.80  
  
**Solução**

A utilização de centro de custo possibilita uma forma de gerenciamento do movimento das contas através de relatórios, sendo utilizado como filtro nos parâmetros.  
Os campos não contem a função de gerar cálculos de custos para informações contábeis

Ao incluir um ativo na rotina de Cadastro de Ativos - **ATFA012**, deve-se utilizar os respectivos campos, abaixo indicados, para o Centro de Custos referente ao bem

**Centro de Custo do bem cadastrado** = N3\_CUSTBEM   
**Centro de Custo de despesa de Depreciação** = N3\_CCDESP (caso o parâmetro **MV\_ATFCCDP**esteja habilitado (.T.), o campo N3\_CCUSTO poderá ser preenchido, replicando seu conteúdo para o campo N3\_CCDESP, do qual será utilizado para depreciação como PADRÃO)  
**Centro de Custo de Depreciação Acumulada** = N3\_CCCDEP   
**Centro de Custo de Correção da Depreciação** = N3\_CCCDES   
**Centro de Custo de Correção Monetária do bem** = N3\_CCCORR

Link com informações de centro custo no ativo

No link cita a rotina ATFA010, porem o procedimento se mantem para a versão 12

<http://tdn.totvs.com/pages/releaseview.action?pageId=185741799>
