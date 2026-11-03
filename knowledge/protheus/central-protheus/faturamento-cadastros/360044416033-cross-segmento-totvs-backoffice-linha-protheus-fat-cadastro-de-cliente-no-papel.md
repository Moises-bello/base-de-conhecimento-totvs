---
article_id: 360044416033
category: Faturamento - Cadastros
content_hash: 964b1b250a92089aa61e8c242e819772a167ae48bc81b547c8a74906a0f6a367
fetched_at: '2026-06-28T22:38:36.526693+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FAT- Cadastro de Cliente
  no Papel de Trabalho
type: support-article
updated_at: '2023-07-05T13:05:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044416033-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FAT-Cadastro-de-Cliente-no-Papel-de-Trabalho
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Cadastro de Cliente no Papel de Trabalho

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FAT - A partir da versão 12

**Solução**É necessário configurar o Cadastro de Cliente em rotina **MVC (MV\_MVCSA1=.T.)**e informar a rotina **CRMA980** no Papel de Trabalho.

O Papel de Trabalho é configurável somente para rotina em MVC, e na rotina Cadastro de Cliente pode ser utilizada em **MVC** (**CRMA980**) ou não (**MATA030**) e essa configuração se dá através do parâmetro **MV\_MVCSA1**:

Se o parâmetro estiver igual a **.T.**, o cadastro de clientes será executado em MVC, ou seja, será utilizada a rotina **CRMA980**.  
  
Se o parâmetro estiver igual a **.F.**, o cadastro de clientes não será executado em MVC, ou seja, será utilizada a rotina **MATA030**.

**Saiba mais:**

**[Cadastro de Cliente em rotina MVC](https://tdn.totvs.com/pages/releaseview.action?pageId=520673220)**
