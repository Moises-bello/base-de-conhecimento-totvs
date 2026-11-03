---
content_hash: 94def94550a933586602b7ba7e368dc8f159033f70b3651f99662aaae36c96ce
fetched_at: '2026-06-29T00:10:32.537524+00:00'
page_id: '527005639'
product: rm
source: tdn-rm
title: FISCAL01-11746 DT Sentença SQL para conferência dos valores gerados na Reinf
  - 2030/2040
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=527005639
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Consulta SQL Anexa |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11746 |

## **02. SITUAÇÃO/REQUISITO**

Criação de sentença SQL a ser publicada como Objeto Gerencial para os clientes e facilitar a conferência dos valores gerados nos eventos da REINF.

Essa sentença deve retornar as origens dos eventos, contendo todos os campos necessários para elaboração de relatórios como: código do Evento, Filial, Cliente/Fornecedor, número do movimento, Base de cálculo do Tributos, valores da retenção, etc.

## **03. SOLUÇÃO**

Criação de Consulta SQL Anexa para conferência dos eventos R-2030, R-2040 da Reinf.

Os mesmos estão disponíveis em Objetos Gerenciais:

Oracle:

* LI\_ORA\_REINF\_R2030\_R2040.TotvsConsSQLAnex

SQL Server:

* LI\_SQL\_REINF\_R2030\_R2040.TotvsConsSQLAnex

A importação ocorre pela visão de Eventos Periódicos (R-5011) por meio de Anexos/Consultas SQL/Importar Consulta SQL Anexa:

Assim, adiciona-se o objeto compartilhado em objetos gerenciais (diretório SQL) e seleciona-se o grupo de usuários que terá acesso:

Após executar o processo, acessa-se a consulta anexa em Anexos/Consultas SQL/Eventos R-2030 e R2040 Relacionados ao Período (SQL):

O sistema abrirá uma visão anexa, com todas as colunas contidas na consulta,   
em que é possível utilizar das funcionalidades comuns a cada visão, como:

* Agrupar os registros por coluna
* Exportar como planilha excel

Para maiores informações de consultas anexas, acesse:
