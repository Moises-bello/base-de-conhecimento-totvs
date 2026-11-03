---
article_id: 360036665554
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 0001301f2b37b0042c09277cc2d5aa8290a0e3753ff5250ce633be735aa66439
fetched_at: '2026-06-28T22:37:19.774117+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como alterar o Prefixo
  dos Títulos Gerados pela Medição no Gestão de Contratos ?
type: support-article
updated_at: '2025-03-19T19:34:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036665554-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-alterar-o-Prefixo-dos-T%C3%ADtulos-Gerados-pela-Medi%C3%A7%C3%A3o-no-Gest%C3%A3o-de-Contratos
---

**Dúvida**Como alterar o Prefixo dos Títulos Gerados pela Medição no Gestão de Contratos ?  
  
**Ambiente**Protheus – SIGAGCT – A partir da versão 12.1.17

**Solução**Quando são faturamos Títulos no financeiro ao encerrar a Medição pelas rotinas *CNTA120/CNTA121*, por padrão do sistema o **Prefixo** é preenchido com o conteúdo **"MED",** a informação consta no parâmetro **MV\_CNPREMD****:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048998614)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048999234)

Para alterar a nomenclatura do Prefixo do título, acesse o cadastro de parâmetros via SIGACFG (Configurador), realize a alteração desejada no conteúdo do parâmetro conforme imagem abaixo.

Cadastro Padrão do Parâmetro **MV\_CNPREMD** no Configurador:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047984054)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047984094)

Após a alteração, realize a Medição.

Veja no exemplo abaixo a alteração para o Prefixo **ALE:**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048859173)**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048999434)

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como Alterar o Tipo dos Títulos gerados pela Medição dos Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036668334-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-Alterar-o-Tipo-dos-T%C3%ADtulos-gerados-pela-Medi%C3%A7%C3%A3o-dos-Contratos)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Parâmetro MV\_NMEDTIT - Como é gerada a Numeração do Título gerado na Medição ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048576874-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Par%C3%A2metro-MV-NMEDTIT-Como-%C3%A9-gerada-a-Numera%C3%A7%C3%A3o-do-T%C3%ADtulo-gerado-na-Medi%C3%A7%C3%A3o)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como alterar o Número dos Títulos Gerados pela Medição no Gestão de Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30768368684567-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-alterar-o-N%C3%BAmero-dos-T%C3%ADtulos-Gerados-pela-Medi%C3%A7%C3%A3o-no-Gest%C3%A3o-de-Contratos)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
