---
article_id: 23772789056023
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: e6b76ca6044ff78870e4d89e6b1f97c89f4437e1a08baa38ba35b604d92e1841
fetched_at: '2026-06-28T22:42:08.892447+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - CAT207 - Como
  gerar informação na tabela CFF "Complemento de crédito Acumulado de ICMS"?
type: support-article
updated_at: '2024-06-05T23:36:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23772789056023-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-CAT207-Como-gerar-informa%C3%A7%C3%A3o-na-tabela-CFF-Complemento-de-cr%C3%A9dito-Acumulado-de-ICMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23772789050135) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar informação na tabela **CFF** **"Complemento de crédito acumulado de ICMS"** ?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Para gerar a tabela **CFF (Complemento de crédito Acumulado de ICMS)**, configure os códigos de **Enquadramento Legal** na **TES (tabela SF4)** além dos cadastros na tabela **CFE (Enquadramento Legal - Credito Acumulado de ICMS)**.  
  
O sistema gera a informação do **Enquadramento** de duas formas:  
Através do parâmetro **MV\_ENQLEG** ou   
Pelo **Cadastro de** **TES** campo **F4\_ENQLEG**.  
  
Ou seja:  
Se o parâmetro **MV\_ENQLEG** estiver preenchido, o sistema busca o conteúdo desse parâmetro;  
Se não, busca do campo **F4\_ENQLEG**, configurado no **Cadastro de TES.**  
1. Se o parâmetro **MV\_ENQLEG** estiver preenchido, o sistema vai buscar o **código** do campo **CFE\_CODIGO** indicado no parâmetro **MV\_ENQLEG**.  
Usando a tabela **CFE**, como exemplo:

*Print*:

![](https://totvssuporte.zendesk.com/attachments/token/XfDXFxMOAYD913uFRwOm5rmxA/?name=image.png)  
  
E o exemplo do parâmetro:  
  
*Print:*

![](https://totvssuporte.zendesk.com/attachments/token/b3bmlPA7GCJ4ed0Zp6z4eEYlH/?name=image.png)  
Se a **Nota Fiscal** for emitida para **SP** levará o **Código 01**.  
Se for emitida para **MG** ou **RJ**, levará o **Código 02**.  
  
2. Se o parâmetro **MV\_ENQLEG** estiver vazio, o sistema buscará do campo **F4\_ENQLEG** do **Cadastro de TES.**  
Se utilizar o **Cadastro da TES**, realize o reprocessamento na **FISA118**, assim o sistema irá gerar as informações na **CFF**.  
  
**Importante:**Verifique se o parâmetro atende a sua necessidade, para tratar a questão das operações **Estaduais** e **Interestaduais**, senão, deverá ser configurado um **Cadastro de TES** para cada **Enquadramento**.

Segue Boletins completos da rotina **CAT207:**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=631856241>

Relatório **FISR026**:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=625453930>
