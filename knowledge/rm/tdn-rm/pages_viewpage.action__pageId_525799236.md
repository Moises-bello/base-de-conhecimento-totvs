---
content_hash: 1f727bbeb31b381761fdcacc130e75ce26b251dc836d05939ebd8d12a41b25af
fetched_at: '2026-06-29T00:10:32.077778+00:00'
page_id: '525799236'
product: rm
source: tdn-rm
title: FISCAL01-11745 DT Sentença SQL para conferência dos valores gerados na Reinf
  - 2010/2020/2050/2060
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=525799236
version: 8
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Consulta SQL Anexa |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11745, FISCAL01-11747, FISCAL01-11857, FISCAL01-12163 |

## **02. SITUAÇÃO/REQUISITO**

Criação de sentença SQL a ser publicada como Objeto Gerencial para os clientes e facilitar a conferência dos valores gerados nos eventos da REINF.

Essa sentença deve retornar as origens dos eventos, contendo todos os campos necessários para elaboração de relatórios como: código do Evento, Filial, Cliente/Fornecedor, número do Lançamento Fiscal, Base de cálculo do Tributos, valores da retenção, etc.

## **03. SOLUÇÃO**

Criação de Consulta SQL Anexa para conferência dos eventos R-2010, R-2020, R-2050 e R-2060  da Reinf.

Os mesmos estão disponíveis em Objetos Gerenciais:

Oracle:

* LI\_ORA\_REINF\_R2010\_R2020.TotvsConsSQLAnex
* LI\_ORA\_REINF\_R2030\_R2040.TotvsConsSQLAnex
* LI\_ORA\_REINF\_R2050.TotvsConsSQLAnex
* LI\_ORA\_REINF\_R2060.TotvsConsSQLAnex

SQL Server:

* LI\_SQL\_REINF\_R2010\_R2020.TotvsConsSQLAnex
* LI\_SQL\_REINF\_R2030\_R2040.TotvsConsSQLAnex
* LI\_ORA\_REINF\_R2050.TotvsConsSQLAnex
* LI\_SQL\_REINF\_R2060.TotvsConsSQLAnex

A importação ocorre pela visão de Eventos Periódicos (R-5011) por meio de Anexos/Consultas SQL/Importar Consulta SQL Anexa:

Assim, adiciona-se o objeto compartilhado em objetos gerenciais (diretório SQL) e seleciona-se o grupo de usuários que terá acesso:

Após executar o processo, acessa-se a consulta anexa em Anexos/Consultas SQL/Eventos R-2010 e R2020 Relacionados ao Período (SQL):

O sistema abrirá uma visão anexa, com todas as colunas contidas na consulta,   
em que é possível utilizar das funcionalidades comuns a cada visão, como:

* Agrupar os registros por coluna
* Exportar como planilha excel

**Observação: as consultas serão importadas como coligada global.**

Para maiores informações de consultas anexas, acesse:
