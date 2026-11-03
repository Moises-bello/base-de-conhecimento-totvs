---
article_id: 360025305012
category: NFe - Nota Fiscal Eletrônica
content_hash: c3e2553b4a9e12849d24e280b322d59b3eb923e49e1144baf3cad13281fa83df
fetched_at: '2026-06-28T22:40:06.951798+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota Técnica 2018.005
  ICMS60 e ICMS500 TAG  vICMSSubstituto
type: support-article
updated_at: '2024-07-25T21:31:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025305012-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Nota-T%C3%A9cnica-2018-005-ICMS60-e-ICMS500-TAG-vICMSSubstituto
---

**Dúvida**

Como gerar a TAG ICMS60 e ICMS500 TAG  vICMSSubstituto ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* Segue o link abaixo com as **configurações para gerar o ICMS60, sem controle de lote:**

<https://suporte.totvs.com/portal/p/10098/download#detail/765125>

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **alterar** **MV\_ULTAQUI = 1** considerar valores somente ***da última aquisição;***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25175153980695)

Ou

2.  Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **alterar****MV\_ULTAQUI = 2** considera as últimas aquisições até compor a quantidade da venda;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25175153993495)

Ou

3.  Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **alterar** **MV\_ULTAQUI = 3** considera as últimas aquisições até compor a quantidade da venda, respeitando a média por nota fiscal.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074600593)

* Esse parâmetro altera a fórmula de cálculo para gravação dos campos ***FT\_BSTANT , FT\_PSTANT, FT\_VSTANT, FT\_PFCANTS e FT\_VFCANTS e FT\_VICPRST.***

Em ambos os casos os cálculos serão realizados considerando a média ponderada e proporcionalizando conforme a quantidade vendida.

**Para a gravação dos campos da SFT da saída serão consideradas as últimas notas de entradas desse produto. Sendo necessário que um dos grupos de campos abaixo estejam preenchidos:**

* ICMS ST Destacado (campos D1\_ICMSRET, D1\_BRICMS e D1\_ALIQSOL)

* ICMS ST Recolhido Anteriormente (digitado manualmente no item da nota de entrada por meio dos campos D1\_ICMNDES, D1\_BASNDES e D1\_ALQNDES)

* Antecipação Tributária (campos D1\_VALANTI, D1\_BRICMS e D1\_ALIQSOL).

4. Configuração ***TES de Entrada:***

Sit Trib ICMS (F4\_SITTRIB) = 10

Calcular ICMS próprio e ICMS-ST

5. Configuração ***TES de Saída:***

Inf ST Ant **(F4\_ART274)** = 1  
Sit Trib ICMS **(F4\_SITTRIB) =** 60  *Regime Normal*   
Cod Sit SN **(F4\_CSOSN) =** 500 *Simples Nacional*

Calcula ICMS **(F4\_ICM)** = Não  
LF ICMS-ST **(F4\_LFICMST)** = Não  
L. Fisc. ICMS **(F4\_LFICM)** = Outros ou ISENTO 

* **Saiba mais:**

**O ICMS60 e ICMS500 são** recolhidos anteriormente, sendo assim não **são somados ao total da nota.**

Verificar se na nota de saída foram gravados os campos ***FT\_BSTANT , FT\_PSTANT e FT\_VSTANT.*** Sem a gravação dos campos as tags no xml não serão geradas.

[MP - FIS - Como preencher automaticamente o campo FT\_VICPRST para geração da tag vICMSSubstituto?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027856832)

**Exemplo de XML:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024318832)**

* **Segue vídeo de exemplo abaixo:**

* **Saiba Mais:**

**Importante:**

Essa mensagem é do Estado de SP, cada Estado possui a mensagem de acordo **com a Legislação de sua UF**

![274.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/25175130652311)

* Conforme o **parecer da consultoria no link abaixo:**

***[Clique Aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=490637567)***
