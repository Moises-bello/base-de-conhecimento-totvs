---
article_id: 360026703531
category: TAF - REINF
content_hash: 36f44f8eab0cc543e7e18c85abc593b607d108f7d6b8fb2ff0a223f9442c9ada
fetched_at: '2026-06-28T22:41:33.590129+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - 0/1 Eventos Transmitidos
  REINF
type: support-article
updated_at: '2023-03-31T17:07:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026703531-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-0-1-Eventos-Transmitidos-REINF
---

**Ocorrência**  
Ao realizar a Transmissão de algum evento do Reinf, é exibida a seguinte mensagem:

![0-1EVENTOS.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360025983131/0-1EVENTOS.PNG)  
  
**Ambiente**

TAF – Reinf – A partir da versão 12.1.33  
  
**Causa**

Este incidente ocorre quando o parâmetro MV\_TAFSURL não está preenchido com a URL do TSS.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Abrir a tabela de parâmetros via Configurador (Ou a SX6 via APSDU). Neste exemplo será efetuado acessando o configurador. Será necessário que um usuário com permissão de acesso ao Configurador e APSDU execute essa etapa.

![sigacfg.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360025983851/sigacfg.PNG)

2. Realizar um filtro na tabela da seguinte maneira:

![filtro.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360025981492/filtro.png)

3. Verificar o conteúdo deste parâmetro, e preencher com a URL do TSS (tanto no registro com a filial preenchida, quanto com a filial em branco):

![prametropt1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360025984191/prametropt1.PNG)

![prametropt2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360025984211/prametropt2.PNG)

 4. Após as alterações, realizar a transmissão novamente.
