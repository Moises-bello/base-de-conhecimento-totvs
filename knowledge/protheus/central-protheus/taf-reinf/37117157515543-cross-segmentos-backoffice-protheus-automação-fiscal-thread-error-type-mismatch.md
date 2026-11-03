---
article_id: 37117157515543
category: TAF - REINF
content_hash: 032ec6c919dc6ebe114622f011d765a735a3332e118dd2bab50a2bab91889f1f
fetched_at: '2026-06-28T22:41:33.434872+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Automação Fiscal - THREAD ERROR type
  mismatch on compare  on MONITORUPD(AUTONFEBUSINESS.PRW)
type: support-article
updated_at: '2025-12-18T18:01:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37117157515543-Cross-Segmentos-Backoffice-Protheus-Automa%C3%A7%C3%A3o-Fiscal-THREAD-ERROR-type-mismatch-on-compare-on-MONITORUPD-AUTONFEBUSINESS-PRW
---

**Ocorrência:**  
No módulo **Faturamento**, ao tentar realizar o monitoramento na rotina **Monitor/Faixa** é retornado *errolog*.

**THREAD ERROR: type mismatch on compare  on MONITORUPD(AUTONFEBUSINESS.PRW) 25/11/2025 00:00:50 line : 481**

**Ambiente:**  
Cross Segmento - TOTVS BackOffice (Linha Protheus) - A partir da versão **12.1.2310**  
  
**Causa:**  
O incidente ocorre devido ao conteúdo do campo "**TIPO**" está divergente no parâmetro **MV\_TAFISCH** no ambiente, este parâmetro deve ser do tipo **caractere** "**C**" o erro ocorre quando está como **Lógico** "**L**".

**Solução:**

 1° Aplique atualização completa do **Módulo 84** (**TAF**).  
   
**12.1.2310:** <https://suporte.totvs.com/portal/p/10098/download#detail/1126399> (Somente ambiente com garantia estendida).  
**12.1.2410:** <https://suporte.totvs.com/portal/p/10098/download?e=1174332>

**12.1.2510**: <https://suporte.totvs.com/portal/p/10098/download?e=1228187>  
   
  2° Execute o **UPDTAF** e **UPDDISTR**,

[Cross Segmentos - Backoffice Protheus - Automação Fiscal - Como executar o UPDTAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37119711558039-Cross-Segmentos-Backoffice-Protheus-Automa%C3%A7%C3%A3o-Fiscal-Como-executar-o-UPDTAF)

IMPORTANTE: O conteúdo do campo **TIPO** do parâmetro **MV\_TAFISCH**, somente vai ser corrigido para **caractere (C)** após execução do **UPDTAF**.

Realize o teste no ambiente de homologação e após correção replique na sua produção.
