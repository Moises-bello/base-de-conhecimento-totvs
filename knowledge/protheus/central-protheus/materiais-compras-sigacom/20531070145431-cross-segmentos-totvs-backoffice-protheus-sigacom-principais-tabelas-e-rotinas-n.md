---
article_id: 20531070145431
category: Materiais - Compras (SIGACOM)
content_hash: b69b66ed2f0a32b2d50e78d409f6d5f4fa57c1fc8a0f899a1b35fc6f0a1412c2
fetched_at: '2026-06-28T22:41:24.082906+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Principais tabelas
  e Rotinas na Integração do Importador XML x TOTVS Transmite
type: support-article
updated_at: '2024-12-04T12:26:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20531070145431-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Principais-tabelas-e-Rotinas-na-Integra%C3%A7%C3%A3o-do-Importador-XML-x-TOTVS-Transmite
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20531070123031) Tempo aproximado para leitura: **00h05 min****Dúvida**Quais são as principais Tabelas e Rotinas na Integração do Importador XML x TOTVS Transmite?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - versão 12

**Solução**

* **Tabelas:**

|  |  |
| --- | --- |
| **Tabela** | **Descrição** |
| DHW | Configuração Grupo/Empresa que integra com o Totvs Transmite |
| DHY | Grava os Ids para consulta dos XML importados do Totvs Transmite |
| DHZ | Histórico de Ids com erros e já importados no Importador XML |
| CKOCOL | Registros do XMLs importados |
| SDS | Cabeçalho do documento no monitor |
| SDT | Itens do documento no monitor |

* **Fontes envolvidos:**

|  |  |
| --- | --- |
| **Fontes** | **Descrição** |
| COLXCFG | Wizard de configuração TOTVS Colaboração / Importador XML |
| COLAUTOREAD | Rotina para importar XMLs na CKOCOL |
| COMTRANSMITE | Classe/Objeto para importação dos XML originados via TOTVS Transmite |
| COMXCOL | Monitor |
| MATA140I | Importa NFE/NFS do TOTVS Colaboração / Importador XML |
| MATA116I | Importa CTE/CTEOS do TOTVS Colaboração / Importador XML |
| WIZIMP | Wizard Integração Importador XML x TOTVS Transmite |
| IMPTRATOOL | Ferramenta de Analise Integração Importador XML x TOTVS Transmite |
| SCHEDIMPTRA | Agendamento requisição e leitura dos recibos |
| SCHEDUPDTRA | Agendamento atualização status no TOTVS Transmite |

***Saiba Mais :***

* [Tabelas e rotinas](https://tdn.totvs.com/pages/viewpage.action?pageId=678583195#tudo-sobre-Tabelas)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
