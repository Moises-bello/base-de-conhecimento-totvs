---
content_hash: 4a3128f997124b42a8abb6aa3d2e4a184da5b03c46eac976b5cfa5ab21e9c9ff
fetched_at: '2026-06-29T00:10:38.187308+00:00'
page_id: '544191584'
product: rm
source: tdn-rm
title: FISCAL01-12237 SPED Fiscal - Registro 1922 Informações Adicionais dos Ajustes
  da Sub-apuração do ICMS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=544191584
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | SPED Fiscal |
| Ticket: | FISCAL01-12237 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12237 |

## **02. SITUAÇÃO/REQUISITO**

Adicionar o registro 1922 na geração do SPED Fiscal.

#### **Registro 1922: Informações Adicionais dos Ajustes da Sub-apuração do ICMS**

Esse registro traz detalhes de processos judiciais/administrativos que foram referenciados nos Lançamentos de Outros Débitos/Créditos ou nos Ajustes informados nos Lançamentos Fiscais para o Registro 1921.

Esse registro é filho do 1921 (nível 6).

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem do dado** |
| 01 | REG | Indicador do registro | Valor fixo “1922” |
| 02 | NUM\_DA | Número do documento de arrecadação estadual, se houver | Não será gerado. Atualmente não é possível associar uma guia ao lançamento de outros débitos/créditos |
| 03 | NUM\_PROC | Número do processo ao qual o ajuste está vinculado, se houver | DPROCESSOJUDICIAL.NUMERO |
| 04 | IND\_PROC | Indicador da origem do processo:  0- SEFAZ;  1- Justiça Federal;  2- Justiça Estadual;  9- Outros | Primeiro caracter do campo DPROCESSOJUDICIAL.TIPO |
| 05 | PROC | Descrição resumida do processo que embasou o lançamento | DPROCESSOJUDICIAL.DESCRICAO |
| 06 | TXT\_COMPL | Descrição complementar | Não será gerado. |

## **03. SOLUÇÃO**

Geração do Registro 1922 para lançamentos de Outros Débitos/Créditos, que possuem Processo Judicial.
