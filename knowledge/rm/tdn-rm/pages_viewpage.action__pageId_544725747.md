---
content_hash: 09b16c5a3043cf43a79d8f4795eeb9684b6141ad45cc6cdd0b99187934c7ca3e
fetched_at: '2026-06-29T00:10:38.761935+00:00'
page_id: '544725747'
product: rm
source: tdn-rm
title: Registro de Entradas\Saídas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=544725747
version: 44
---

**Definição**

Os registros são feitos individualmente, para cada nota emitida, em linhas individuais e a escrituração é encerrada no último dia útil de cada período de apuração de impostos. Para efeitos legais e organizacionais, é preciso que a empresa arquive as notas na mesma ordem dos lançamentos no livro de registros.

O Registro de Entradas\Saídas foi construído à partir de uma Consulta SQL anexa ao Período de Apuração. Desta forma, podemos tirar proveito de todos os recursos da MDI, como personalização, ordenação e agrupamento de colunas, exportação de dados, etc. Além disso, a consulta pode ser facilmente modificada a critério do usuário.

Arquivo com a consulta SQL

Para a geração do relatório, foi disponibilizado no TOTVS Compartilhamento a seguinte consulta SQL:

***SQL Server***

* FISSQLANEX0001 - Registro ES - SQL.TotvsConsSQLAnex

**Oracle**

* FISSQLANEX0012 - Apuração - Registro\_ES - ORA.TotvsConsSQLAnex

Para obter a consulta via TOTVS Compartilhamento, consulte este link: [TOTVS Compartilhamento](https://tdn.totvs.com/display/LRM/TOTVS+Compartilhamento).

**Passo 1 - Menu de Acesso**

Acesse o Período de Apuração a ser gerado o relatório através de Obrigações Principais > Período de Apuração

**Passo 2 - Importação**

Importar Consulta SQL (FISSQLANEX0001) através do menu Anexos > Consultas SQL > Importar Consulta SQL Anexa

Para maiores informações de consultas anexas, acesse: 

**Passo 3 - Geração**

Após a importação da Consulta SQL Anexa, basta acessar novamente o menu Anexos → Consultas SQL e abrir o Registro de Entrada\Saída.

Ao ser importado a consulta é exibida como uma visão anexa do Período de Apuração. 

Como facilitador, as colunas podem ser livremente organizadas de acordo com a demanda do usuário.

As informações dos registros listados dentro do período podem ser exportados em diversas extensões.

**Gráficos**

Foram disponibilizados também 2 Gráficos no TOTVS Compartilhamento, ambos representando visualmente as informações do Registro de Entradas\Saídas

Disponibilização dos Gráficos

Os dois gráficos foram disponibilizados via TOTVS Compartilhamento.

**SQL Server**

* FISGRA0008 - Entradas e Saídas do Período - Valor de ICMS - SQL.TotvsGraf
* FISGRA0009 - Entradas e Saídas do Período - Valor Contábil - SQL.TotvsGraf

**Oracle**

* FISGRA0011 - Entradas e Saídas do Período - Valor de ICMS - ORA.TotvsGraf
* FISGRA0012 - Entradas e Saídas do Período - Valor Contábil - ORA.TotvsGraf

No caso de dúvida em como obter os objetos gerencias, consulte este link: [TOTVS Compartilhamento](https://tdn.totvs.com/display/LRM/TOTVS+Compartilhamento).

Estes Gráficos devem ser importados no cadastro de Gráficos e posteriormente associados na visão de Período de Apuração.

Para efetuar a importação dos gráficos, acesse o cadastro .

Apos a importação acesse os Anexos do Período de Apuração > Selecione a opção Gráficos > Inserir Gráfico para anexar esse gráfico como Anexo do Período de Apuração

Associe os parâmetros da consulta aos campos da visão do Período de Apuração

Após anexar os gráficos os mesmos podem ser exibidos através do menu Anexos → Gráficos.

noneWebinar dos relatórios Registro de Entradas\Saídas e Resumo de Apuração

648432
