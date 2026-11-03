---
content_hash: 5e0f4e6ba2c56cd0570f12b739bffa30b73697c565b599709027ff2a76214b69
fetched_at: '2026-06-29T00:11:03.304178+00:00'
page_id: '620769796'
product: rm
source: tdn-rm
title: Apuração ISS - Saídas - Por Código Tributação do Município
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=620769796
version: 13
---

**Definição**

Este relatório tem a função de mostrar os valores das saídas sobre o Tributo **ISS** que foi apurado no mês informado por código do Serviço no Município. 

O Resumo de Apuração do ISS foi construído à partir de uma Consulta SQL anexa ao Período de Apuração. Desta forma, podemos tirar proveito de todos os recursos da MDI, como personalização, ordenação e agrupamento de colunas, exportação de dados, etc. Além disso, a consulta pode ser facilmente modificada a critério do usuário.

Arquivo com a consulta SQL

Para a geração do relatório, foi disponibilizado no TOTVS Compartilhamento a seguinte consulta SQL:

***SQL Server***

* FISSQLANEX0016 - Apuração ISS - Saídas - Por Código Trib. Município.TotvsConsSQLAnex

Para obter a consulta via TOTVS Compartilhamento, consulte este link: [TOTVS Compartilhamento](https://tdn.totvs.com/display/LRM/TOTVS+Compartilhamento).

**Passo 1 - Menu de Acesso**

Acesse o Período de Apuração a ser gerado o relatório através de Obrigações Principais > Período de Apuração

**Passo 2 - Importação**

Importar Consulta SQL (FISSQLANEX0016) através do menu Anexos > Consultas SQL > Importar Consulta SQL Anexa

Para maiores informações de consultas anexas, acesse: 

**Passo 3 - Geração**

Após a importação da Consulta SQL Anexa, basta acessar novamente o menu Anexos → Consultas SQL e abrir o Registro de Apuração ICMS.

Ao ser importado a consulta é exibida como uma visão anexa do Período de Apuração. 

Como facilitador, as colunas podem ser livremente organizadas de acordo com a demanda do usuário.

As informações dos registros listados dentro do período podem ser exportados em diversas extensões.
