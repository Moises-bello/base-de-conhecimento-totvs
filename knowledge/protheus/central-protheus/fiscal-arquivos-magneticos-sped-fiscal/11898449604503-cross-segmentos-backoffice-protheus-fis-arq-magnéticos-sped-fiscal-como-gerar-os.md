---
article_id: 11898449604503
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: eff48b3274441a9ab75ecb7b2fb7202c816b90347be2eaad1d046208d0aef62b
fetched_at: '2026-06-28T22:42:02.255763+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Como gerar os registros C500/ C700 e filhos para NF3-e, a partir do Layout 017
  do arquivo txt do Sped Fiscal?
type: support-article
updated_at: '2023-01-24T13:19:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11898449604503-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-os-registros-C500-C700-e-filhos-para-NF3-e-a-partir-do-Layout-017-do-arquivo-txt-do-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar o registro **C500 Nota de Energia Elétrica e C700 - Consolidação dos documentos de Energia Elétrica** e filhos para **NF3 - Nota Fiscal de Energia Elétrica Eletrônica**  no **Layout 017** do Sped Fiscal?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**Conforme estabelecido pelo **ATO COTEPE/ICMS Nº 117, DE 1º DE DEZEMBRO DE 2022**, foi publicada a versão **3.1.2** do Guia Prático da **EFD ICMS IPI** e da **Nota Técnica 2022.001 v1.2** com vigência **a partir de janeiro/2023**, com as seguintes alterações:  
  
**1. Inclusão do modelo 66 na informação dos registros C700, C790 e C791.**  
**2. Alteração da obrigatoriedade dos campos 08 e 09 do registro C700 de O para OC.**  
**3. Alteração da orientação de preenchimento dos campos 06, 07, 08 e 09 do registro C700**

As notas do **modelo 66**, podem ser geradas nos registros **C500 e C700** de acordo com a concessão da unidade federativa.   
Esclarecimentos sobre a geração de um ou outro registro, no *link*  
[https://tdn.totvs.com/pages/releaseview.action?pageId=728656278.](https://tdn.totvs.com/pages/releaseview.action?pageId=728656278)  
  
A definição do registro que deve ser enviado será de acordo com a **[SEFAZ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11887321686423)** do Estado do Contribuinte. De acordo com o leiaute **Guia Prático EFD-ICMS/IPI** – **Versão 3.1.2**, "Para a escrituração de documentos fiscais do **modelo 66**, este registro consolida o total das notas, por data de emissão e série, que não utilizarem ajustes da **tabela 5.3**", portanto mesmo selecionando a opção **3 - Consolidado** caso a nota contenha código de ajuste da **tabela 5.3** será gerado o registro **C500** e os respectivos registros complementares.

Dessa forma, no Protheus, foi implementada a geração dos registros **C700, C790 e C791** para as notas fiscais do modelo **66 (NF3e).**  
  
Para geração dos registros, na primeira aba da tela de parâmetros do **SPED FISCAL** foi implementado uma nova opção para a geração do **C500 e/ou C700.**

Para as notas fiscais **modelo 66** temos as seguintes opções:

**1 - Ambos (será gerado C500 e C700)**

**2 - Analítico (será gerado C500)**

**3 - Consolidado (será gerado C700**)

![](https://tdn.totvs.com/download/thumbnails/729245578/image2022-12-29_11-19-43.png?version=1&modificationDate=1672325338810&api=v2)

**Importante:**

A geração dos registros **C500 e C700** continuam dependentes do preenchimento dos complementos fiscais como anteriormente, pois, neste ponto não houve alteração.

![](https://tdn.totvs.com/download/attachments/729245578/image2022-12-29_11-45-45.png?version=1&modificationDate=1672325338667&api=v2)
