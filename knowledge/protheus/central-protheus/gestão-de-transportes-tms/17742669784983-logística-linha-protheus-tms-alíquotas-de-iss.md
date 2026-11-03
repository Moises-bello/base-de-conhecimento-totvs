---
article_id: 17742669784983
category: Gestão de Transportes (TMS)
content_hash: 674e373bd6769e4044ba01fe93fb11493a0d3bf2e9d2baa21df347a26eb9bc03
fetched_at: '2026-06-28T22:45:27.240223+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Alíquotas de ISS
type: support-article
updated_at: '2026-04-23T14:19:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17742669784983-Log%C3%ADstica-Linha-Protheus-TMS-Al%C3%ADquotas-de-ISS
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17742639325719)*** Tempo aproximado para leitura: **00:02:25 min**  
  
**Dúvida**  
Como são definidas as alíquotas do **ISS -** **Imposto sobre Serviço** pelo **TOTVS Logística TMS** ?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**  
O **TMS** obtém as alíquotas de **ISS** a partir dos seguintes cadastros:

1. Alíquota da região de calculo, definida no campo **DUY\_ALQISS**;
2. Alíquota do produto de calculo, definida no campo **B1\_ALIQISS.** Produto de calculo pode ser identificado no campo **D2\_COD**
3. Alíquota do parâmetro **MV\_ALIQISS**

Por exemplo, se o campo **DUY\_ALQISS** está preenchido como 5%, esta será a alíquota utilizada para o calculo e valerá somente para a região de calculo em questão, independente do que for preenchido no produto de calculo ou no parâmetro **MV\_ALIQISS.** Se o **DUY\_ALQISS** estiver vazio, o Sistema acata do **B1\_ALIQISS,** e esta será acatada sempre que utilizado o produto de calculo em questão, e se **B1\_ALIQISS** estiver vazio, acata do **MV\_ALIQISS**, sendo esta a alíquota geral para o Sistema, podendo ser diferenciada por filial diretamente no parâmetro.  
  
O Sistema poderá utilizar outra alíquota de ISS para notas fiscais de serviço caso existam regras distintas em:

* **Exceções Fiscais - MATA540;**
* **Alíquotas do ISS - FISA052;**
* **Uso de pontos de entradas**

Para utilizar **Alíquotas do ISS - FISA052** - tabela **CE1**, no produto de calculo, campo **B1\_MEPLES** **= 2** e parâmetro **MV\_ISSXMUN** **= .T.**. Mais detalhes sobre essa configuração constam na documentação disponível na seção **Saiba mais**.  
  
Todas essas regras serão desconsideradas se estiver configurado o uso de alíquotas de **ISS** via **Configurador de Tributos - FISA170** conforme exemplo contido na documentação disponível na seção **Saiba mais**.  
  
**Saiba mais**  
[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 – Como utilizar uma alíquota de ISS por Município com Configurador de Tributos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28272502990999-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-utilizar-uma-al%C3%ADquota-de-ISS-por-Munic%C3%ADpio-com-Configurador-de-Tributos)  
[Logística - Linha Protheus - TMS - Retenção ISS pelo TMS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9627052434711-Log%C3%ADstica-Linha-Protheus-TMS-Reten%C3%A7%C3%A3o-ISS-pelo-TMS?source=search)  
[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Exceções Fiscais (MATA540) - Todos os campos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047488214-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Exce%C3%A7%C3%B5es-Fiscais-MATA540-Todos-os-campos)  
[CROSS Segmentos - TOTVS BackOffice Linha Protheus - FIS - Rotina FISA052 Para Notas Fiscais de Saída](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045913513-CROSS-Segmentos-TOTVS-BackOffice-Linha-Protheus-FIS-Rotina-FISA052-Para-Notas-Fiscais-de-Sa%C3%ADda)
