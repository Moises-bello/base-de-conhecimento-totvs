---
article_id: 360025333971
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 0aae8cfb0f6c85e09da30960202fdbf382cb3a51e757a59be786a035af904275
fetched_at: '2026-06-28T22:42:10.286135+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - CAT207 Como
  gerar o Registro 5325
type: support-article
updated_at: '2022-08-17T19:43:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025333971-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-CAT207-Como-gerar-o-Registro-5325
---

**Dúvida**Como gerar o **Registro 5325** (Operações Geradoras de Crédito Acumulado) na **CAT207** ?**Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
O **Registro 5325** são operações geradoras de **Crédito Acumulado**, será informado em todas as saídas em que haja geração de **Crédito Acumulado** na operação.Para esse registro o campo **Op Cred Acum (F4\_CRDACUM)** deve ser configurado como Sim.

O campo **PER\_MED\_ICMS** do **Registro 5325** é preenchido de acordo com o campo **F4\_PERCMED**, caso o mesmo esteja preenchido. Caso esteja como ZERO, o Percentual médio será calculado pelo sistema, utilizando a formula citada no Anexo III - Relação dos Códigos Fiscais de Operações ou Prestações – **CFOP** e Fórmulas.

Neste caso para obter os valores de "Saída" e "Entrada" aplicadas nas fórmulas de obtenção do **Percentual Médio de Crédito** deverá obedecer a regra determinada no item **7, 2o, art. 30 da DDTT do RICMS SP** conforme descrito a seguir.

Para a geração do **Crédito Acumulado** do imposto, deverão ser consideradas as operações de:

- Se o pedido de apropriação do crédito for solicitado no ano posterior, de Janeiro a Dezembro do ano da apropriação.  
- Se o pedido de apropriação do crédito for solicitado ate junho, de Janeiro a Dezembro do ano anterior.  
- Se o pedido de apropriação do crédito for solicitado apos junho, de Janeiro ao mês anterior do ano da apropriação.

Validação do Fonte para descobrir o valor do **Crédito Presumido**:  
  
//-- Credito Estimado  
**If** AllTrim((**cAlias**)->F4\_CRDACUM) == "1"  
nCredICM := (((**cAlias**)->FT\_VALCONT / (1 + (**cAlias**)->F4\_IVAUTIL)) \* (nMedio / 100))  
  
OU seja,

O campo **F4\_CRDACUM** deve estar = 1  
Segue a fórmula para encontrar o Valor do **Crédito Acumulado**  
(**FT\_VALCONT** / (1 + **F4\_IVAUTIL**) \* (**F4\_PERCMED** / 100)  
  
  
Importante:

Este Registro somente será gerado, se houver **Crédito Presumido** no período, ou seja, se o valor do Crédito Presumido for maior que o valor do **ICMS** da Nota Fiscal de Saída
