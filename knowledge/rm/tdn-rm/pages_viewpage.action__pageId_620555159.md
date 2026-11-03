---
content_hash: ce8f27bd52763f1dbab2ed5e40e475c1cdee12705622f7f06a178804c0104923
fetched_at: '2026-06-29T00:11:03.282386+00:00'
page_id: '620555159'
product: rm
source: tdn-rm
title: Registro de Lançamentos de ISS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=620555159
version: 13
---

**Definição**

Registro de ISS é destinado ao registro dos documentos fiscais relativos aos serviços prestados e tomados sujeitos ao ISS.

O Registro de ISS foi construído à partir de uma Consulta SQL anexa ao Período de Apuração. Desta forma, podemos tirar proveito de todos os recursos da MDI, como personalização, ordenação e agrupamento de colunas, exportação de dados, etc. Além disso, a consulta pode ser facilmente modificada a critério do usuário.

Arquivo com a consulta SQL

Para a geração do relatório, foi disponibilizado no TOTVS Compartilhamento a seguinte consulta SQL:

***SQL Server***

* FISSQLANEX0014 - Registro de Lançamentos - ISS - SQL.TotvsConsSQLAnex

Para obter a consulta via TOTVS Compartilhamento, consulte este link: [TOTVS Compartilhamento](https://tdn.totvs.com/display/LRM/TOTVS+Compartilhamento).

**Passo 1 - Menu de Acesso**

Acesse o Período de Apuração a ser gerado o relatório através de Obrigações Principais > Período de Apuração

**Passo 2 - Importação**

Importar Consulta SQL (FISSQLANEX0014) através do menu Anexos > Consultas SQL > Importar Consulta SQL Anexa

Para maiores informações de consultas anexas, acesse: 

**Passo 3 - Geração**

Após a importação da Consulta SQL Anexa, basta acessar novamente o menu Anexos → Consultas SQL e abrir o Registro de Apuração ICMS.

Ao ser importado a consulta é exibida como uma visão anexa do Período de Apuração. 

Como facilitador, as colunas podem ser livremente organizadas de acordo com a demanda do usuário.

As informações dos registros listados dentro do período podem ser exportados em diversas extensões.
