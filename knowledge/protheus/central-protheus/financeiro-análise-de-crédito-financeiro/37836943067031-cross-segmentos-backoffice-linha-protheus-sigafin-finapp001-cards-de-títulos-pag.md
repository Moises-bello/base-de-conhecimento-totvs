---
article_id: 37836943067031
category: Financeiro - Análise de Crédito Financeiro
content_hash: 4deeda72c1e97222371b59651af0e3113413edbbe6269a779e5541d86ac7c5e8
fetched_at: '2026-06-28T22:37:25.540876+00:00'
product: protheus
section_id: 36607745462423
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINAPP001 - Cards de
  títulos pagos em atraso e inadimplência não atualizam automaticamente
type: support-article
updated_at: '2026-01-22T12:09:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37836943067031-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINAPP001-Cards-de-t%C3%ADtulos-pagos-em-atraso-e-inadimpl%C3%AAncia-n%C3%A3o-atualizam-automaticamente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37836943044247) Tempo aproximado para leitura: **00:05 min**

**Dúvida**  
Por que os valores de títulos pagos em atraso e inadimplência permanecem incorretos mesmo após a atualização dos títulos na FINAPP001?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release  12.1.2210.  
  
**Solução**

A inconsistência nos valores apresentados no **card de títulos vencidos**, bem como a **não atualização da margem de inadimplência**, ocorre porque o sistema utiliza a **Data Base** (data do sistema no momento do login) como **parâmetro de referência** para o cálculo dos cards "inadimplência" e "títulos pagos com atraso".

Quando a **Data Base** está configurada de forma **retroativa ou futura** em relação à data real do pagamento, o sistema deixa de considerar determinados títulos no processo de atualização. Esse comportamento impacta diretamente os valores exibidos nos cards.

**Exemplo prático:**  
Um título com vencimento em **19/01/2025**, pago em **20/01/2026**, somente será considerado corretamente na composição do card. 'títulos pagos com atraso", caso o usuário esteja **logado com Data Base posterior à data do pagamento**. Caso contrário, o sistema não irá incluir esse título no cálculo apresentado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37836914287767)

Dessa forma, para garantir a atualização correta dos cards e da margem de inadimplência, é fundamental que a **Data Base utilizada no login esteja compatível com a data real dos pagamentos realizados**.

**Saiba Mais**

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINAPP001 - Cálculo de Inadimplência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36320697108631-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINAPP001-C%C3%A1lculo-de-Inadimpl%C3%AAncia)
