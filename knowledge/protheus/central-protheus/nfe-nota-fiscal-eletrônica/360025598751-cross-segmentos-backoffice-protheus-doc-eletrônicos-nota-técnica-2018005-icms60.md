---
article_id: 360025598751
category: NFe - Nota Fiscal Eletrônica
content_hash: b2a361400e31065f63f9c066341670e125ddd838ca45fdde9936786f64672ac5
fetched_at: '2026-06-28T22:40:06.960871+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota Técnica 2018.005
  ICMS60 e ICMS500 TAGS  vBCSTRet, pST e vICMSSTRet
type: support-article
updated_at: '2025-07-18T18:24:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025598751-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Nota-T%C3%A9cnica-2018-005-ICMS60-e-ICMS500-TAGS-vBCSTRet-pST-e-vICMSSTRet
---

**Dúvida**Como gerar conteúdo nas TAGS do ICMS60 vBCSTRet, pST e vICMSSTRet ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

Segue o link abaixo com as **configurações para gerar o ICMS60, sem controle de lote:**

<https://suporte.totvs.com/portal/p/10098/download#detail/765125>

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **alterar** **MV\_ULTAQUI = 1** considerar valores somente ***da última aquisição;***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024313492)

Ou

2.  Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **alterar****MV\_ULTAQUI = 2** considera as últimas aquisições até compor a quantidade da venda;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024313612)

Ou

3.  Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **alterar** **MV\_ULTAQUI = 3** considera as últimas aquisições até compor a quantidade da venda, respeitando a média por nota fiscal.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33566750502039)

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
Sit Trib ICMS **(F4\_SITTRIB) =** 500 *Simples Nacional*

Calcula ICMS **(F4\_ICM)** = Não  
LF ICMS-ST **(F4\_LFICMST)** = Não  
L. Fisc. ICMS **(F4\_LFICM)** = Outros ou ISENTO 

* **Exemplo do DANFE:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024314392)**

* **Exemplo do XML:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024332871)

**Importante:**

Essa mensagem é do Estado de SP, cada Estado possui a mensagem de acordo **com a Legislação de sua UF**

![274.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500016645621)

* Conforme o **parecer da consultoria no link abaixo:**

***[Clique Aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=490637567)***

* **Saiba mais:**

As UFs que atualmente geram a mensagem referente ao ICMS60 no XML são **SP, PR, SC, AM, RS, ES e MG**

**Importante:**

Para **emitentes do** **Estado de SP para** que não seja gerada a mensagem referente ao ICMS60 em informações adicionais do fisco para **destinatários que sejam consumidor final:**

1. Configurar ***no TES de Saída:***

Inf ST Ant (F4\_ART274) = **2**

2. Configurar ***cadastro de Cliente:***

Tipo (A1\_TIPO) = **Consumidor Final**

* **Segue vídeos de exemplos abaixo:**
