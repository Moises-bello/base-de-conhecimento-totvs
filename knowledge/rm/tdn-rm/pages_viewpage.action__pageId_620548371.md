---
content_hash: 823edc351d94f2c7b179e34678df318b8af617519a26d5fb912d7af6a335969b
fetched_at: '2026-06-29T00:11:03.278181+00:00'
page_id: '620548371'
product: rm
source: tdn-rm
title: Registro de Apuração ICMS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=620548371
version: 13
---

**Definição**

O Registro de Apuração de ICMS tem por finalidade demonstrar os valores fiscais relativos ao ICMS das entradas e saídas , agrupados por CFOP, no mês informado.

O Registro de Apuração do ICMS foi construído à partir de uma Consulta SQL anexa ao Período de Apuração. Desta forma, podemos tirar proveito de todos os recursos da MDI, como personalização, ordenação e agrupamento de colunas, exportação de dados, etc. Além disso, a consulta pode ser facilmente modificada a critério do usuário.

Arquivo com a consulta SQL

Para a geração do relatório, foi disponibilizado no TOTVS Compartilhamento a seguinte consulta SQL:

***SQL Server***

* FISSQLANEX0013 - Apuração - ICMS - SQL.TotvsConsSQLAnex

Para obter a consulta via TOTVS Compartilhamento, consulte este link: [TOTVS Compartilhamento](https://tdn.totvs.com/display/LRM/TOTVS+Compartilhamento).

**Passo 1 - Menu de Acesso**

Acesse o Período de Apuração a ser gerado o relatório através de Obrigações Principais > Período de Apuração

**Passo 2 - Importação**

Importar Consulta SQL (FISSQLANEX00013) através do menu Anexos > Consultas SQL > Importar Consulta SQL Anexa

Para maiores informações de consultas anexas, acesse: 

**Passo 3 - Geração**

Após a importação da Consulta SQL Anexa, basta acessar novamente o menu Anexos → Consultas SQL e abrir o Registro de Apuração ICMS.

Ao ser importado a consulta é exibida como uma visão anexa do Período de Apuração. 

Como facilitador, as colunas podem ser livremente organizadas de acordo com a demanda do usuário.

As informações dos registros listados dentro do período podem ser exportados em diversas extensões.
