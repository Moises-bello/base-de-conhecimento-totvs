---
article_id: 18179064655383
category: TAF - REINF
content_hash: 81d83615bdb2e406de0e630b646c262e85f4b65f28b49df1a6a89972aaaf9a72
fetched_at: '2026-06-28T22:41:34.907247+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus -TAF - REINF - Como considerar o IR na
  data de contabilização na apuração do Reinf?
type: support-article
updated_at: '2025-05-29T17:28:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18179064655383-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-considerar-o-IR-na-data-de-contabiliza%C3%A7%C3%A3o-na-apura%C3%A7%C3%A3o-do-Reinf
---

**[Remover as instruções entre colchetes e altere o tempo aproximado para leitura]**  
![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18179059964439) Tempo aproximado para leitura: **00:04:00 min****Dúvida**Como considerar a retenção de IR  pela data de contabilização na apuração dos eventos R-4010 e R-4020?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TAF - REINF - Todas as versões  
  
**Solução**

**Painel Reinf**

Este tratamento aplica-se apenas para o IR na emissão (**Tributo 12 no TAF**), os títulos com IR pagamento (tributo 28) devem permanecer considerando apenas a data de pagamento do título.

**MV\_TAFDT40 :** Criação do parâmetro que controla se considera a data de contabilização para apuração dos eventos Reinf do bloco 40 **1=Sim**; **2=Não**.

Por padrão, o parâmetro **MV\_TAFDT40** existirá com seu conteúdo igual a '2', caso seja alterado com o valor '1',  a apuração do evento R-4020 irá se comportar da seguinte forma:

* **NF campo de emissão**

![](https://tdn.totvs.com.br/download/attachments/790632041/image2023-9-19_12-29-56.png?version=1&modificationDate=1695137396430&api=v2)

* **NF campo de Contabilização**

![](https://tdn.totvs.com.br/download/attachments/790632041/image2023-9-19_11-27-53.png?version=1&modificationDate=1695134712817&api=v2)

* **Fatura campo de Contabilização**

![dtcontabil.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32455986017303)

* **Painel Reinf**

![](https://tdn.totvs.com.br/download/attachments/790632041/image2023-9-19_12-29-33.png?version=1&modificationDate=1695137373827&api=v2)

**Obs: Os dados de data contábil precisam vir no arquivo TXT da integração. Caso o parâmetro seja habilitado mas os campos de data contábil estiverem vazios, o painel não irá habilitar os documentos pela contabilização, sendo necessário acionar o time Protheus Financeiro para trazer os campos preenchidos na integração.**

**Validação do Extrator fiscal para geração das datas de contabilização:**

**MV\_VCTIRPF = C**  
**MV\_VENCIRF = C**

Para mais informações:

<https://tdn.totvs.com.br/pages/releaseview.action?pageId=790632041>
