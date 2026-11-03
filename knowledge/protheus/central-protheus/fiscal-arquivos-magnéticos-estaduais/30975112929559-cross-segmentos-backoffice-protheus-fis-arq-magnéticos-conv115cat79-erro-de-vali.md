---
article_id: 30975112929559
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 41d57e5ec27f7a9dd659c3340da8ae4b31a72ae48fb0bee48890e0f870ee6253
fetched_at: '2026-06-28T22:42:09.151106+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - CONV115/CAT79
  - Erro de validação "DEST 314"
type: support-article
updated_at: '2025-03-27T18:39:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30975112929559-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-CONV115-CAT79-Erro-de-valida%C3%A7%C3%A3o-DEST-314
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30975112904855) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao importar os arquivos magnéticos **CONV115** ou **CAT79**, ocorre o erro de validação:  
**DEST 314 - Código Autenticação Digital do registro do arquivo Cadastro inválido**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30975112906391)

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões

**Causa**Esse erro ocorre, pois o código **MD5** (**campo 21** **- Código de Autenticação Digital do registro**) do arquivo **tipo D** - **DADOS CADASTRAIS DO DESTINATÁRIO DO DOCUMENTO FISCAL** está errado.  
  
**Solução**

**1 -** Identifique a **Nota Fiscal** que está com erro no arquivo:

Você pode identificar essa nota fiscal através do log dos erros de validação do arquivo.

**2 -** Verifique os campos de cadastro usados nesta **NF** , pois o **campo 21 - Código de Autenticação Digital do registro** é formado por um código **MD5** gerado com base nas informações do **campo 10 à 20 do leiaute** conforme citado no mesmo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30975141784215)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30975112908439)

Observação: Esses campos são referente ao **Cadastro do Cliente (tabela SA1) e a Nota fiscal (tabela SFT)**. É necessário que os campos estejam preenchidos corretamente e com o tamanho de caracteres igual indica o leiaute.
