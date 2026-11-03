---
article_id: 8731050004759
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: e43e1c4f5a1d44d96be161033a5dd7922935b3d279c7694742b89f0c73bc1c7a
fetched_at: '2026-06-28T22:42:02.239360+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Sped Fiscal
  - Como gerar os registros 1200 e 1210 via Documento Fiscal?
type: support-article
updated_at: '2022-09-08T18:01:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8731050004759-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-Como-gerar-os-registros-1200-e-1210-via-Documento-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar os registros **1200** e **1210** no **Sped Fiscal** via **Documento Fiscal?**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão**12.1.25**  
  
**Solução**Os registros **1200/1210** são gerados com base nos valores gerados pela **Apuração de ICMS (MATA953)** na aba**Créditos Extra Apuração**.  
  
Esses valores podem ser gerados na **Apuração do ICMS** com base na escrituração do **documento fiscal** atrelado ao **Código de Ajuste** utilizado.  
  
O processo para geração dos registros via documento fiscal é o seguinte:  
  
**1.** Acesse a rotina **Cadastro de Lançamentos Manuais da Apuração do ICMS (MATA964)** e  escolha o código de ajuste a ser informado na aba **Apuração do ICMS.**  
  
**2.** Pressione o botão **Alterar** e na aba **Código** **Extra Apuração** do **Código de Ajuste**, localize o campo **Cod. Aj. Cre - CDO\_CODCRE**e o preencha com o código que deve ser apresentado no registro **1200.**

**3.** Na **Aba Cadastrais** amarre um **Código de Reflexo** contendo a regra de cálculo a ser efetuada e caso seja necessário levar os lançamentos de forma individualizada, por documento, ao registro **1210** deixe o campo **Agrup. Apr - CDO\_AGRUPA  = 2.**

No exemplo didático abaixo temos o código de ajuste **SP000202** que será demonstrado na **Apuração do ICMS** e que também vai gerar dados na aba **Extra Apuração** devido ao campo **Cod. Aj. Cre - CDO\_CODCRE** conter o **Código de Ajuste SP099999**

**Aba Cadastrais**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8737122267287/mceclip1.png)

**Aba Crédito Extra Apuração**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8737204152599/mceclip2.png)

**4.** No cadastro de **TES** que será utilizado para escriturar o documento fiscal, informe o **Código de Ajuste**  alterado rotina **MATA964** (no caso, **SP000202**)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8737299062807/mceclip3.png)

**5.** Escriture o documento fiscal utilizando o cadastro de **TES** e verifique se na Aba **Lançamentos da Apuração** foi realizado o cálculo:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8737324090391/mceclip4.png)

**6.** Através da rotina **MATA953**, gere a **Apuração do ICMS.** Na aba **Apuração do ICMS,** será demonstrado o código de ajuste **SP000202**

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8737352899223/mceclip5.png)

Na aba **Créditos Extra Apuração** será demonstrado os valores referente ao código de ajuste **SP099999**

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8737477462039/mceclip7.png)

Ao dar um duplo clique sobre o código de ajuste será demonstrado o detalhamento dos valores por documento fiscal.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8737427295511/mceclip6.png)

**7.** Confirme a **Apuração do ICMS** e gere o **Sped Fiscal** com a pergunta abaixo = SIM

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8660128072855/mceclip12.png)

**Importante:**

O registro **1210** só será gerado quando da **Utilização do Crédito**. No **Recebimento** ou **Transferência do Crédito** será gerado apenas o registro **1200.**
