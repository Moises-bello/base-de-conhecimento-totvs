---
article_id: 8618487176727
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 7e60f75c216a2f23c84fe5cda5e4975fa23bbb3fb485908724d371982047fced
fetched_at: '2026-06-28T22:42:00.883360+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS -   Arq. Magnéticos - Sped Fiscal
  - Como gerar os registros 1200 e 1210 via Apuração do ICMS?
type: support-article
updated_at: '2022-09-05T14:57:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8618487176727-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-Como-gerar-os-registros-1200-e-1210-via-Apura%C3%A7%C3%A3o-do-ICMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar os registros **1200** e **1210** no **Sped Fiscal** via **Apuração do ICMS**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Solução**

Os registros **1200/1210** são gerados com base nos valores gerados pela **Apuração de ICMS(MATA953)** na aba**Créditos Extra Apuração**.  
  
Assim, existem duas formas de gerar os registros via **Apuração do ICMS:**

**1. Manualmente, incluindo um código de ajuste diretamente na aba Créditos Extra Apuração:**

Acesse a **Apuração do ICMS (MATA953)** e na **Aba Créditos Extra Apuração**, em **Outras Ações,** inclua uma nova linha na qual deve ser informada **Código de Lançamento** correspondente a **UF** do **MV\_ESTADO** e que o quarto dígito deste código seja igual a  **9,** conforme exemplo didático abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8615226315799/mceclip0.png)

Uma vez informado código válido, será possível acessar **Apuração** detalhada através de **duplo clique nesta nova linha**.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8615237883159/mceclip1.png)

Na tela detalhada, também é possível incluir linhas nas seções de **Recebimento**, **Recebimento por Transferência** e **Utilização**, através do botão **Inc. Lin** disponível em **Outras Ações.**

Quando uma nova linha é adicionada manualmente nesta tela, o tipo de lançamento será identificado com a descrição **M - MANUAL**, e deverá ser informado **Descrição**, o **Código do Tipo** de **Utilização do Crédito** e o **Valor**, e automaticamente os saldos serão atualizados.  
  
**2. Manualmente, incluindo um código de ajuste nas demais abas da Apuração do ICMS:**

Outra maneira de incluir informações manuais na **Apuração do ICMS** de forma que alimente a aba **Extra Apuração** é preenchendo o código manualmente nas abas **Apuração-ICMS, Apuração-ST, DIFAL/FECP ou  Débitos Especiais.**

Nesse caso, acesse a rotina **Cadastro de Lançamentos Manuais da Apuração do ICMS (MATA964)** e  escolha o código de ajuste a ser informado em uma das quatro abas da **Apuração do ICMS**.

Em seguida, pressione o botão **Alterar** e na aba **Código** **Extra Apuração** do **Código de Ajuste**, localize o campo **Cod. Aj. Cre - CDO\_CODCRE** e o preencha com o código que deve ser apresentado na aba **Extra Apuração do ICMS** na **Apuração do ICMS.** Os demais campos da aba devem ser preenchidos, conforme necessidade.

No exemplo didático abaixo temos o código de ajuste **SP000202** que será utilizado na **Apuração do ICMS** e que também vai gerar dados na aba **Extra Apuração** devido ao campo **Cod. Aj. Cre - CDO\_CODCRE** conter o **Código de Ajuste SP099999**

**Aba cadastrais**

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8618408616983/mceclip5.png)

**Aba Créditos Extra Apuração**

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8618410952215/mceclip6.png)

**Apuração do ICMS**

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8659980728599/mceclip10.png)

**Aba Créditos Extra Apuração**

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8660024057111/mceclip11.png)

Resumidamente, quando houver **Código de Lançamento** vinculado a um **Código de Ajuste de Crédito,** as inclusões, edições e exclusões de linhas também terão efeito na aba **Créditos Extra Apuração.**

Para ambos os processos, confirme a apuração e em seguida gere o **Sped Fiscal** com a pergunta abaixo = **SIM**

**![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8660128072855/mceclip12.png)**
