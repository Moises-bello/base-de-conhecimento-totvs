---
article_id: 20611589990167
category: Materiais - Compras (SIGACOM)
content_hash: 35be6bed1b1add09af54679ae386bbe87af4b9c295509718e3195566e34e122f
fetched_at: '2026-06-28T22:41:15.904055+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como gravar origem
  e cst quando documento é gerado pelo monitor do Importador XML?
type: support-article
updated_at: '2024-05-17T17:41:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20611589990167-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-gravar-origem-e-cst-quando-documento-%C3%A9-gerado-pelo-monitor-do-Importador-XML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20611597124247) Tempo aproximado para leitura: **00:05:00min**

**Dúvida**  
Como gravar origem e cst quando documento é gerado pelo monitor do Importador XML / Totvs Colaboração (COMXCOL)?

**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - versão 12

**Solução**

Gravação de **origem + cst** quando documento é originado via Totvs Colaboração nos campos **DT\_CLASFIS** e posteriormente no **D1\_CLASFIS**.

***Obs:***

O parâmetro ainda pode ser utilizado vazio, com isto o sistema irá utilizar a tag do **ICMS** concatenando com a origem para preencher o campo de classificação fiscal automaticamente.

| Parâmetro | MV\_COLCFIS |
| --- | --- |

| Tipo | Caracter |
| Default | Em branco |
| Regra | Ao informar o de/para deve ser feito da seguinte forma:  Separador por**|**  de/para por **=**  **Ex: 0=0|1=2|2=1|5=5** |

| Campo | DT\_CLASFIS |
| --- | --- |

| Obs | Mesmas características do campo D1\_CLASFIS (Sem os valids) |

***Saiba Mais :***

* [14773144 DMANMAT02-39036 DT Campo D1\_CLASFIS altera conteúdo quando a nota tem DT\_CLASFIS](https://tdn.totvs.com/pages/releaseview.action?pageId=699814909)
* [DMANMAT02-18083 DT TOTVS COLABORACAO CLASFIS ORIGEM CST](https://tdn.totvs.com/display/public/PROT/DMANMAT02-18083+DT+TOTVS+COLABORACAO+CLASFIS+ORIGEM+CST)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
