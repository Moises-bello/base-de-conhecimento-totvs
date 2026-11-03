---
article_id: 12717622069783
category: Financeiro - Reinf
content_hash: e44748985b88ee1b99b99ae544b7c1adaedcdfd2ee6f1065302c756950189d1f
fetched_at: '2026-06-28T22:37:51.725447+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: ' Cross Segmentos - Backoffice Linha Protheus - REINF - PCC na emissão (MV_BX10925=2)
  quando será enviado o imposto para o REINF?'
type: support-article
updated_at: '2023-12-15T21:18:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12717622069783--Cross-Segmentos-Backoffice-Linha-Protheus-REINF-PCC-na-emiss%C3%A3o-MV-BX10925-2-quando-ser%C3%A1-enviado-o-imposto-para-o-REINF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17710685194391) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Para os clientes que utilizam o PCC na emissão (MV\_BX10925=2) quando será enviado o imposto para o REINF?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

O fato gerador do PCC é o pagamento e não a emissão, o filtro do extrator fiscal ira enviar o PCC após pagar o titulo principal NF.  
  
Independente da configuração do parâmetro **MV\_BX10925**, que permite que os TX's desses impostos possam ser gerados na **emissão** ou na **baixa**, o **Extrator Fiscal** irá considerar como fato gerador do PIS, COFINS e CSLL o **pagamento do título principal**(exemplo: título do tipo **NF**, **DP**, **BOL**, **etc**.), através do campo ***FK2\_DATA***;

Quando o parâmetro **MV\_BX10925** = 2 (gera **TX's** na inclusão do **título a pagar**), o **Extrator Fiscal** irá verificar se o **título principal** está baixado para enviar os tributos ao **TAF**. Se a **baixa** tiver sido **parcial**, será enviado os valores dos **tributos** proporcionais ao **valor baixado**.  
  
**Exemplo:**  
NF com data de emissão: 01/09/2023 | Vencimento: 20/10/2023  
Titulo imposto TX - PCC emissão: 01/09/2023 | Vencimento: 20/11/2023  
Pagamento da NF: 20/10/2023  
  
Ao executar o extrator fiscal no período do mês **10/2023**, nesse período que será enviado o layout de **pagamento** (**T158**) com as informações do **PCC**. Independente da data que baixar o titulo TX, esse data não será filtrada pelo extrator fiscal, pois filtra o período de pagamento do titulo principal.

**Saiba mais:**  
[FAQ - 0016 - Quais os fatos geradores serão considerados no extrator financeiro?](https://tdn.totvs.com/pages/viewpage.action?pageId=737543501)  
**Legislação:**  
[Retenção de Tributos - PIS/COFINS/CSLL/ISS/INSS - Pagamentos Parciais - Valor Bruto](https://tdn.totvs.com/pages/releaseview.action?pageId=181143263)
