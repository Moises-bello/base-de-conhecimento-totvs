---
article_id: 20885080721687
category: Gestão de Transportes (TMS)
content_hash: 1c004c46b39e0e295801eab26cc16da6025b661e7088a3d12ce1c0db6fa45325
fetched_at: '2026-06-28T22:45:27.407637+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Como configurar o ICMS de Pauta
type: support-article
updated_at: '2025-01-13T19:26:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20885080721687-Log%C3%ADstica-Linha-Protheus-TMS-Como-configurar-o-ICMS-de-Pauta
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20885100592407) Tempo aproximado para leitura: **00:01:45 min** **Dúvida**Como funciona e quais as principais parametrizações para o calculo do **ICMS - Imposto sobre Circulação de Mercadorias e Serviços** de Pauta?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**

Conforme **Art.112 § 19 do RICMS/RN**, a base de cálculo do **ICMS** deverá corresponder, no mínimo, à soma dos valores individuais de referência, conhecido como pauta do produto e do frete. Isso significa que, caso a soma do valor do produto e do frete informados seja inferior à soma de referência, o que será considerado para a base de cálculo do **ICMS** é a soma de referência, ou seja, a maior soma. O cálculo da base de cálculo do **ICMS** é realizado baseando-se no valor de referência do produto e no valor de referência do frete.  
  
As configurações necessárias são:

* Configurar o parâmetro **MV\_ICPAUTA** = 2
* Efetuar os seguintes cadastros:
  + **Produto - MATA010**
    - Preencha os campos **Icms Pauta - B1\_VLR\_ICM** = 0,01, **P.ICMS Prop - B1\_INT\_ICM** = 0,01 e **Tipo Carga - B1\_TIPCAR** = conforme citado na documentação em **Saiba mais**.
  + **TES - Tipos de Entrada e Saída - MATA080**
    - Preencha os campos **Paut.ICMS PP - F4\_PAUTICM** = **1 - Sim** e **Red.Car.ICMS - F4\_RDBSICM** = **2 - Sim**.

Após realizar estes e os demais cadastrados citados na documentação disponível em **Saiba mais**, então, na rotina **Entrada Docto Cliente - TMSA050,** preencher obrigatoriamente o campo **KM - DTC\_KM,** e esta informação deve estar em **Dist.Entrega - DV9\_KM**, e no campo **Cod. Produto - DTC\_CODPRO,** deve ser informado o produto cadastrado conforme citado acima.  
  
**Saiba mais**[Exemplo de Cálculo de Impostos ICMS de Pauta (TMSA200 - SIGATMS)](https://tdn.totvs.com/pages/releaseview.action?pageId=489759699)
