---
article_id: 24239467101719
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: cc29af63a995c02a1e78b6971959052e997e23351fbc90b348812c8b0bcf5c48
fetched_at: '2026-06-28T22:42:01.143424+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Como gerar o Bloco B zerado para contribuintes do ICMS do DF no Sped Fiscal?
type: support-article
updated_at: '2024-06-18T12:32:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24239467101719-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-o-Bloco-B-zerado-para-contribuintes-do-ICMS-do-DF-no-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24239504899607) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como gerar **Bloco B zerado** no **Sped Fiscal** para cenários de contribuinte do **ICMS** no **Distrito Federal**?  
  
**Ambiente:**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**

**Descrição**:  
Contribuinte de ICMS e de ISS necessita gerar a **EFD ICMS/IPI** **(SPEDFISCAL)** para o Distrito Federal, porém encontra problemas relacionados ao registro **B470**. Com a implementação e adoção da NFS-e nacional por parte do Distrito Federal, não tenho mais a necessidade de gerar o **Bloco B**, porém como contribuinte de ICMS, precisa gerar o **Bloco B** com o registro **B470** com todos os seus campos zerados.

**Solução:**

Realizados ajustes nas rotinas **SPEDFISCAL** e **SPEDXFUN**, para tratar o **A****rt. 34** do decreto **43.982/2022**, com a implementação da NFS-e no Distrito Federal, contribuintes do ISS estão dispensados da escrituração do **Bloco B**.

Criado a opção **3-Gera B470 Zerado**, para a geração do arquivo com o **Bloco B**, zerado:

![](https://tdn.totvs.com/download/attachments/836070300/image-2024-4-8_9-53-19.png?version=1&modificationDate=1712580800047&api=v2)

Arquivo do **SPEDFISCAL**, gerado com o **Bloco B**, zerado.

![](https://tdn.totvs.com/download/attachments/836070300/image-2024-4-8_9-59-55.png?version=1&modificationDate=1712581196157&api=v2)

Para essa questão, segue doc oficial:

<https://tdn.totvs.com/display/public/PROT/18210839+DSERFIS1-33950+DT+-+SPEDFISCAL+-++Bloco+B+Gerar+Zerado+quando+a+Empresa+Contribuinte+do+ICMS+no+Distrito+Federal>

Após isso, realize novos testes.
