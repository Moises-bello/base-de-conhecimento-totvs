---
content_hash: 6d376d83b7d18e5257baaa3e224113bf8940edec11e29128e15d1a0e67f8dd1a
fetched_at: '2026-06-29T00:06:00.129231+00:00'
page_id: '192105591'
product: rm
source: tdn-rm
title: RMFIS00001_03.001 - "DE-PARA" entre ECD e ECF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=192105591
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão: todas** |
| **Processo** | **:** | ECF - Escrituração Contábil Fiscal |
| **Subprocesso** | **:** | ECF - Escrituração Contábil Fiscal |
| **Data da publicação** | **:** | 21/07/2015 |

Para auxiliar no entendimento da ECF, elaboramos o "de-para" abaixo para compreensão das informações que são comuns à ECD e ECF e sua respectiva origem dentro do sistema:

| De entre ECD e ECF | | | | |
| --- | --- | --- | --- | --- |
| **ECD (SPED Contábil)** | | **ECF** | | **Origem** |
| PLANO DE CONTAS | I050 | J050 | Plano de Contas do Contribuinte | Cadastro do Plano de Contas.  Serão enviadas somente as contas que tenham o campo “natureza da conta para emissão do SPED” preenchido. |
| PLANO DE CONTAS REFERENCIAL | I051 | J051 | Plano de Contas Referencial | Cadastro do Plano de Contas Paralelo |
| SUBCONTAS CORRELATAS | I053 | J053 | Subcontas Correlatas | Cadastro de SubContas Correlatas (anexo Plano de Contas) |
| CENTRO DE CUSTOS | I100 | J100 | Centro de Custos | Serão enviados somente os Centros de Custo que tenham a opção “Enviar p/ SPED” marcadas. |
| SALDOS PERIÓDICOS – IDENTIFICAÇÃO DO PERÍODO | I150 | K030 | Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL | No caso da ECF esta informação corresponde ao período de apuração do Tributo no TOTVS Gestão Fiscal |
| DETALHES DOS SALDOS PERIÓDICOS | I155 | K155 | Detalhes dos Saldos Contábeis (Depois do Encerramento do Resultado do Período) | Registro calculado a partir dos lançamentos contábeis para as contas patrimoniais no período. |
| DETALHES DOS SALDOS DAS CONTAS DE RESULTADO ANTES DO ENCERRAMENTO | I355 | K355 | Saldos Finais das Contas Contábeis de Resultado Antes do Encerramento | Na ECD este registro é calculado através dos lançamentos que contenha o histórico de fechamento utilizado na transferência de grupos contábeis.  Na ECF este registro  pode ser calculado conforme na ECD, ou optando por ser calculado desconsiderando todo o lançamento que contenha um histórico que seja de fechamento no período. |
| BALANÇO PATRIMONIAL | J100 | L100  P100  U100 | Balanço Patrimonial | Estes registros serão gerados automaticamente pelo PVA da ECF através do mapeamento do Plano de Contábil com o Plano de Contas Referencial. |
| DEMONSTRAÇÃO DO RESULTADO DO EXERCÍCIO | J150 | L150  P150  U150 | DEMONSTRAÇÃO DO RESULTADO DO EXERCÍCIO |
