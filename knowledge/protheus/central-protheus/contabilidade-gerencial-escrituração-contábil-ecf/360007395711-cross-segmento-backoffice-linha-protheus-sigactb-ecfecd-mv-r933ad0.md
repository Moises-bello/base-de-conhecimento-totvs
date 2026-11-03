---
article_id: 360007395711
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: b37a6ebdbe72ab8b868102e282a2695ac6ef5787fa6a5940f88f8780be09f37f
fetched_at: '2026-06-28T22:40:47.629440+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus  - SIGACTB - ECF/ECD - MV_R933AD0
type: support-article
updated_at: '2022-06-03T22:10:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007395711-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-ECD-MV-R933AD0
---

**Ocorrência**

Ao gerar o Sped ECD ou ECF é apresentado mensagem referente o parâmetro MV\_R933AD0.

Ao informar o parâmetro "DIPJ =SIM" o sistema apresenta mensagem

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406603597719/mceclip0.png)

Ao gerar o  ECF  com DIPJ é apresentado mensagem referente o parâmetro MV\_R933AD0.

![Erro_parametro.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360007673192/Erro_parametro.jpg)  
  
**Ambiente**Protheus - Contabilidade Gerencial  - A partir da versão 11.80  
  
**Causa**

Este incidente ocorre devido a necessidade do preenchimento do parâmetro MV\_R933AD0 com a informação do campo da tabela **Itens das NF de Entrada (SD1)** que guarda a informação do valor do imposto de importação.

**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse o Configurador (SIGACFG).

2. Acesse Base de Dados > Dicionário > Base de Dados.

3. Localize o parâmetro MV\_R933AD0

4. O Conteúdo do parâmetro deve ser o campo da tabela **Itens das NF de Entrada (SD1) - D1\_II**

![img.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360007673252/img.png)

**Para maiores informações:**

# [MP - SIGACTB - ECF - Como realizar a geração dos blocos X e Y?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006827952-MP-SIGACTB-ECF-Como-realizar-a-gera%C3%A7%C3%A3o-dos-blocos-X-e-Y-)
