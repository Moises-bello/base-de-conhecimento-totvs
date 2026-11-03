---
article_id: 360026830373
category: Escrita Fiscal - Impostos - ICMS
content_hash: a10055f28087768b8f8b8455645d43f2fd314459d54c85d0127dc1129b4921c6
fetched_at: '2026-06-28T22:39:25.580022+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Configuração do cálculo
  para o ICMS DIFERIDO Resolução SEFAZ 13/2019 RJ
type: support-article
updated_at: '2022-11-16T12:47:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026830373-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Configura%C3%A7%C3%A3o-do-c%C3%A1lculo-para-o-ICMS-DIFERIDO-Resolu%C3%A7%C3%A3o-SEFAZ-13-2019-RJ
---

**Dúvida**

Configuração do calculo para o ICMS DIFERIDO Resolução SEFAZ 13/2019 RJ

**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Solução**

Configuração de Diferimento

**F4\_ICM:**Definido como SIM.

**F4\_ICMSDIF:**Definido como 7 Ded. ICMS BC. Composta 

Utilizando esta opção sera utilizado a formula abaixo para calcular diferimento de ICMS:

ICMS diferido = Preço na Nota Fiscal / (1 - Alíquota) \* Alíquota

**F4\_PICMDIF:**Informar o Percentual de Diferimento

**Manual de configurações de Diferimento**

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418030442775-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-C%C3%A1lculo-de-Diferimento-de-ICMS?source=search>

Configuração de reflexo:

CE0\_NFBASE: Informe qual base de cálculo será utilizada na lançamento deste reflexo:

Z) Base Zerada.

CE0\_NFALIQ: Informe qual alíquota será utilizada no lançamento deste reflexo:

Z) Alíquota Zerada.

CE0\_NFVALO: Informe qual valor será utilizado no lançamento deste reflexo:

8) Valor do ICMS Diferido.

CE0\_VL197: Define se o valor dos registros C197 ou D197 será gravado no campo 07-VL\_ICMS ou 08-VL\_OUTROS.

2) Valor Outras

![ICMS_DIFERIDO_SEFAZ_RJ.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360041730274/ICMS_DIFERIDO_SEFAZ_RJ.JPG)

**Atenção:** Caso seja utilizado um percentual igual a 100 o valor de ICMS ficará zerado, pois ao definir como 100% significa que ocorreu um diferimento do Valor Total.

![Capturar1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360042572633/Capturar1.JPG)

Informações Adicionais:

INCENTIVOS E BENEFÍCIOS FISCAIS

<http://tdn.totvs.com/pages/releaseview.action?pageId=469449117>
