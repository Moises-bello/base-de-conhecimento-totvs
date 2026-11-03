---
content_hash: 4f9375c2519a6b057d30d29b73fa89f36e7a4e21596836650329f04ac917e9ae
fetched_at: '2026-06-29T00:10:30.308036+00:00'
page_id: '519718189'
product: rm
source: tdn-rm
title: FISCAL01-11194  DT Atualização de Campos T015/T015AE - TAF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=519718189
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | TAF |
| Ticket: | FISCAL01-11194 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11194 |

## **02. SITUAÇÃO/REQUISITO**

Atualizar o layout do Registro T015 para contemplar os novos campos:

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem da Informação** |
| 46 | NATUREZA\_RENDIMENTO | Código da natureza de rendimento | Campo novo |
| 47 | IND\_DEC\_TERC | Indicativo de 13º salário, de acordo com as opções: 1=Sim;  2=Não. Obs: Validação: Deve estar de acordo com as regras estabelecidas na Tabela 01, na coluna 13° Salário. Valores. | Incluir este campo no Layout do Registro, mas sem ligação. Necessário somente para compor o tamanho do Registro |
| 48 | ICMS\_ST\_FRETE | Valor do ICMS-ST em relação ao frete | Não temos informações separadas para isto. Sugestão: Não tratar este campo. Incluir no Layout de Integração, mas não ligar. |

Atualizar o layout do Registro T015AE para contemplar os novos campos:

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem da Informação** |
| 31 | VLR\_COMP\_ANO\_CALENDARIO | Compensação Judicial relativa ao ano calendário | Incluir este campo no Layout do Registro, mas sem ligação. Necessário somente para compor o tamanho do Registro |
| 32 | VLR\_COMP\_ANO\_ANT | Compensação Judicial relativa a anos anteriores ao ano calendário. | Incluir este campo no Layout do Registro, mas sem ligação. Necessário somente para compor o tamanho do Registro |

## **03. SOLUÇÃO**

Foi implementado no Layout do TAF, no Registro T015  os campos: 

* Campo 46, Código da Natureza de rendimento
* Campo 47, Indicativo do 13º salário
* Campo 48, Valor do ICMS ST

E no Registro T015AE, os campos:

* Campo 31, Compensação Judicial relativo ao ano calendário
* Campo 32, Compensação Judicial relativo a anos anteriores ao ano calendário

Os campos não possuem ligação com o contexto(será implementado em outra issue).
