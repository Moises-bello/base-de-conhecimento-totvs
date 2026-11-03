---
article_id: 360017458472
category: NFe - Nota Fiscal Eletrônica
content_hash: cbc4023cff1ea26bc5f8e492775e2b5cc641d6caee57c86115dbd969116c3755
fetched_at: '2026-06-28T22:40:06.789988+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como realizar Inutilização
  de uma nota fiscal eletrônica ?
type: support-article
updated_at: '2025-10-01T13:48:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017458472-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-realizar-Inutiliza%C3%A7%C3%A3o-de-uma-nota-fiscal-eletr%C3%B4nica
---

**Dúvida**

Como realizar Inutilização (Inutilizar) de uma nota fiscal eletrônica ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* **Opção 1: Quando a numeração da nota for pulada**

1 - Habilite **o parâmetro:**

* **MV\_INUTILI= .T.** (com os dois pontos)

![MV_INUTILI.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360102917733)

2- Preencher o parâmetro:

* **MV\_INUTCLI=** Código de um cliente qualquer (que exista na base)

![MV_INUTCLI.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001858222)

3- Preencher o parâmetro:

* **MV\_INUTPRO=** Código de um produto qualquer (que exista na base)

![MV_INUTPRO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001858302)

4- Preencher o parâmetro:

* **MV\_INUTTES =** Código de um TES qualquer (que exista na base).

![MV_INUTTES.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360102917853)

* **Importante:**

Se **o TES** utilizado no parâmetro **MV\_INUTTES**  estiver com os campos **L. Fiscal ICM = Não, L. Fiscal IPI = Não** , não serão gerados os registros nas tabelas **SF3 / SFT.** Além disso, é necessário que seja uma **TES de saída.**

**No momento da transmissão da Inutilização,**será apresentada a mensagem abaixo:

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10220828148375)**

Lembrando que a geração das tabelas é importante para geração dos **arquivos acessórios** que verifica o STATUS da nota no campo **F3\_CODRSEF.**

5 - Após isso, ir na rotina de transmissão de notas  **outras ações -> Inutilização**

![menu_de_inutilizacao.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360102917993)

**Opção 2: Quando a nota foi gerada no Protheus**

Para **inutilização** de uma nota **gerada no sistema que não foi transmitida** ou que **retornou rejeição** na transmissão da nota.

1- Ir em **Faturamento -> Exclusão de Documento -> Selecionar o documento -> Outras ações -> Excluir:**

![excluir.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360100755234)

3-  Na próxima transmissão de notas a inutilização e transmitida automática ou **se não houver transmissão de uma nova nota, transmita a numeração da nota que foi excluída;**

![Transmissao.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360102918153)

4- Após isso consulte em **monitor -> faixa se a Inutilização da nota foi autorizada.**

![monitor_faiza.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360100755394)
