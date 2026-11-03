---
article_id: 8378753311895
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 89da852f41162e0c0a1848a510a9e7f3eb113042ad773a780a0cc4f12b8a20e4
fetched_at: '2026-06-28T22:42:03.650251+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - SPEDFISCAL -
  Arquivo txt gerado em branco
type: support-article
updated_at: '2025-02-04T19:27:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8378753311895-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPEDFISCAL-Arquivo-txt-gerado-em-branco
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29751622764439) Tempo aproximado para leitura: **00:02:00 min****Dúvida**

O que verificar quando o arquivo txt do **Sped Fiscal** é gerado em branco?  
  
**Ambiente**TOTVS Backoffice (**Linha Protheus**) - A partir da versão **12.1.25**  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
1. Verifique os campos do **parâmetro** da *Wizard* do arquivo, ele deve conter um **período de menor ao maior**.

Exemplo: 01/08/2022 à 31/08/2022  
  
A pergunta **Livro**, deve possuir o conteúdo asterisco ( \* ) para que seja gerado corretamente.  
  
No **diretório do arquivo**, deve possuir uma barra invertida no final.

**Exemplo: C:/Temp/**Segue forma correta de preenchimento na imagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8378540143767)

Umas das possíveis causas deste problema ocorrer é ter informado o registro pretendido dentro do parâmetro **MV\_REGSPED**.

Descrição: Informar os registros que não devem ser gerados no SPED Fiscal    
  
**Solução**Deve-se retirar do parâmetro quaisquer registros que precisam ser gerados no arquivo do Sped Fiscal
