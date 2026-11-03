---
article_id: 360019091791
category: Escrita Fiscal - Impostos - ICMS - Complemento de ICMS/IPI
content_hash: da29d825809f421e8ee0d096eb0e897fe69e12aded676a870893fca528be203b
fetched_at: '2026-06-28T22:39:21.312072+00:00'
product: protheus
section_id: 1500001538701
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - NF Complemento de
  Difal
type: support-article
updated_at: '2024-08-26T12:15:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019091791-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-NF-Complemento-de-Difal
---

**Dúvida**Como efetuar o lançamento de nota para o complemento do Difal?  
  
**Ambiente**Protheus Fiscal - Todas as versões  
  
  
**Solução**

**Procedimento de Utilização**

Devido à quantidade de informações que devem ser inseridas, os complementos de DIFAL não serão gerados a partir de pedidos de venda. Estes documentos serão emitidos através da rotina **MATA920** (Nota Fiscal Manual de Saída).

1) Acessar a rotina de inclusão de notas fiscais manuais de saída:**Módulo Livros Fiscais -> Atualizações -> Movimentos -> NF Manual Saída.**

2) Selecionar o tipo **"Compl. ICMS"** no combobox de seleção de tipo de documento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18703128544535)

3) Preencher as demais informações do cabeçalho do documento normalmente.

4) Informar o produto da NF original (que está sendo complementada), o TES a ser utilizado na operação e os demais dados pertinentes ao item.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18703128553495)

Agrega valor = não

Sit trib icm = 00 ou 20

Calc difal = sim

MKP ICM COMP = sim

Marg solid = nunca

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18703144895127)

5) Para vincular o complemento ao documento de origem: Ao editar o campo **"N.F. Original"**, pressione a tecla **<F4>** para que sejam listadas as notas que podem ser complementadas.

6) Após selecionar a nota que será complementada os campos **"N.F. Original"**, **"Serie Orig."** e **"It.Doc. Orig"**. serão preenchidos automaticamente. Estes campos também podem ser informados manualmente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18703128561303)

7) Preencher os valores a serem complementados nos campos:

* + **Base Dest** (D2\_BASEDES): Base de ICMS interestadual para a UF de destino. Utilizado p/ geração da tag **vBCUFDest**. Obrigatório caso haja cálculo de FCP (Fundo de Combate à Pobreza ) no estado de destino.
  + **ICMS Comple.** (D2\_ICMSCOM): Valor do ICMS partilhado correspondente à UF de ORIGEM. Utilizado p/ geração da tag **vICMSUFRemet**.
  + **ICMS Difal** (D2\_DIFAL): Valor do ICMS partilhado correspondente à UF de DESTINO. Utilizado p/ geração da tag **vICMSUFDest**.
  + ![](https://centraldeatendimento.totvs.com/hc/article_attachments/18703128567959)
  + Conforme parametro MV\_PPDIFAL para o ano de 2023 100% destino, dessa forma configura somente o campo ICMS DIFAL, nesse exemplo que não tem FECP
  + - **FECP Comp.** (D2\_ALFCCMP) - **Se aplicável**: Percentual do FCP (Fundo de Combate à Pobreza) do estado de destino. Utilizado p/ geração da tag **pFCPUFDest**.
    - **Valor FECP** (D2\_VFCPDIF) - **Se aplicável**: Valor do FCP (Fundo de Combate à Pobreza) do estado de destino. Utilizado p/ geração da tag **vFCPUFDest**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18703128573847)

Importante na CD2 gravar o valor do imposto e percentual

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18703144909591)

8) Confirmar a inclusão do documento e efetuar os procedimentos de transmissão à SEFAZ normalmente.

Importante

Se forem informados valores nos campos "FECP Comp." e "Valor FECP" é obrigatório informar a "Base Dest." utilizada no cálculo correspondente ao valor do fundo. Caso contrário será apresentada a rejeição 793 no momento da transmissão do documento:

**"Valor do ICMS relativo ao Fundo de Combate à Pobreza na UF de destino difere do calculado".**

Para a impressão do Difal ec/87 no danfe deve ser usado os CSTs 00 ou 20

Não usar o CST90 causa a rejeição 508

---

**Recebendo um complemento:**

Caso a empresa seja não contribuinte do ICMS e venha a receber uma nota complementar com cálculo de DIFAL o procedimento deve ser realizado através da rotina **MATA103** (Documento de Entrada).

1) Acessar a rotina de inclusão de documentos de entrada:**Módulo Compras -> Atualizações -> Movimentos -> Documento Entrada**

2) Selecionar o tipo **"Compl. ICMS"** no combobox de seleção de tipo de documento.

3) Preencher as demais informações do cabeçalho do documento normalmente.

4) Informar o produto da NF original (que está sendo complementada), o TES a ser utilizado na operação e os demais dados pertinentes ao item. É necessário que o TES utilizado possua os cálculos do DIFAL e/ou ICMS (se aplicável) devidamente configurados.

5) Para vincular o complemento ao documento de origem: Após o preenchimento das informações do item **4**, pressione a tecla **<F7>** para que sejam listadas as notas que podem ser complementadas.

6) Após selecionar a nota que será complementada os campos **"Docto. Orig."**, **"Serie Orig."** e **"It.Doc. Orig"**. serão preenchidos automaticamente. Estes campos também podem ser informados manualmente.

7) Preencher os valores a serem complementados nos campos:

* + **Base Dest** (D1\_BASEDES): Base de ICMS interestadual para a UF de destino.
  + **ICMS Comple.** (D1\_ICMSCOM): Valor do ICMS partilhado correspondente à UF de DESTINO.
  + **ICMS Difal** (D1\_DIFAL): Valor do ICMS partilhado correspondente à UF de ORIGEM.
  + **FECP Comp.** (D1\_ALFCCMP) - **Se aplicável**: Percentual do FCP (Fundo de Combate à Pobreza) do estado de destino.
  + **Valor FECP** (D1\_VFCPDIF) - **Se aplicável**: Valor do FCP (Fundo de Combate à Pobreza) do estado de destino.

8) Confirmar a inclusão do documento.
