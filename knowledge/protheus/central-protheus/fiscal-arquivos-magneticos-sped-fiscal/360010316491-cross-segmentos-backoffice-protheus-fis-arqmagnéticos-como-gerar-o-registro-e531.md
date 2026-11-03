---
article_id: 360010316491
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 8ae61126054290f01432a6e4b93aaf703ebb2fc9d0f88477eab1e5c12d5cc951
fetched_at: '2026-06-28T22:42:02.666229+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como gerar o
  registro E531 no Sped Fiscal?
type: support-article
updated_at: '2023-04-24T12:18:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010316491-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-registro-E531-no-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **02:00 min****Dúvida:**Como gerar o registro **E531** no **Sped Fiscal**?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões

**Solução**

**REGISTRO E531: INFORMAÇÕES ADICIONAIS DOS AJUSTES DA APURAÇÃO DO IPI – IDENTIFICAÇÃO DOS DOCUMENTOS FISCAIS (01 e 55).**

Segundo o **Guia Prático** do **Sped Fiscal**, este registro tem por objetivo identificar os documentos fiscais relacionados ao ajuste. Este registro somente deverá ser informado quando o campo **IND\_DOC** do Registro **E530** for igual a **3**.

**REGISTRO E530: AJUSTES DA APURAÇÃO DO IPI.**

![](http://tdn.totvs.com/download/attachments/346490718/image2018-3-19_10-14-28.png?version=1&modificationDate=1521466619000&api=v2)

PACOTE DE ATUALIZAÇÃO PARA A GERAÇÃO DO REGISTRO **E531:**

<https://suporte.totvs.com/portal/p/10098/download?e=663833>

Após aplicação do *patch* é necessário atualizar os dois dicionários que estão no pacote.

Com a atualização de dicionários, será criado o campo **CC7\_CODIPI** na **TES** e habilitada a opção “**Documento Fiscal**” na linha de ajuste da apuração do **IPI**.

Passo a passo para a geração do registro **E531**:

1. Cadastre a **TES.**Preencha o campo **CC7\_CODREF** (**Código Reflexo do lançamento**) e **CC7\_CODIPI** (**Código de ajusta da apuração do IPI**).

Caso não exista o Código de Reflexo do lançamento do **IPI**, o mesmo deverá ser cadastrado conforme abaixo:

![](http://tdn.totvs.com/download/attachments/346490718/image2018-3-19_10-16-28.png?version=1&modificationDate=1521466619000&api=v2)

![](http://tdn.totvs.com/download/attachments/346490718/image2018-3-19_10-17-1.png?version=1&modificationDate=1521466619000&api=v2)

2. Lance a **Nota Fiscal** via **documento de entrada:**

![](http://tdn.totvs.com/download/attachments/346490718/image2018-3-19_10-17-46.png?version=1&modificationDate=1521466619000&api=v2)

3. Processe a **Apuração do IPI** na rotina **MATA952:**

Será gerada automaticamente na apuração uma linha correspondente ao ajuste do **IPI** realizado através do **Documento fiscal**.

![](http://tdn.totvs.com/download/attachments/346490718/image2018-3-19_10-18-46.png?version=1&modificationDate=1521466619000&api=v2)

Clique duas vezes sobre a **linha do ajuste**, verifique se o campo “**Origem Documento**” foi preenchido com a opção **3- Documento Fiscal**.

![](http://tdn.totvs.com/download/attachments/346490718/image2018-3-19_10-22-57.png?version=1&modificationDate=1521466619000&api=v2)

4. Confirme a **Apuração** e gere o arquivo do **Sped Fiscal:**

![](http://tdn.totvs.com/download/attachments/346490718/image2018-3-19_10-23-43.png?version=1&modificationDate=1521466619000&api=v2)

Anexo, vídeo com exemplo didático do processo de geração do registro **E531**.
