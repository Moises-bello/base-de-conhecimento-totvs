---
article_id: 36268148515351
category: Reforma Tributária
content_hash: f449e16b6bbe0a24d9a65729e8847eb21dfde01eac66dc61b8196ac8ef60a04b
fetched_at: '2026-06-28T22:39:53.798831+00:00'
product: protheus
section_id: 34900856700439
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributária
  – Rejeição 1037 Alíquota da CBS inválida [nItem: 999]'
type: support-article
updated_at: '2025-11-11T22:31:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36268148515351-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tribut%C3%A1ria-Rejei%C3%A7%C3%A3o-1037-Al%C3%ADquota-da-CBS-inv%C3%A1lida-nItem-999
---

**Dúvida**  
Como corrigir a Rejeição 1037 Alíquota da CBS inválida [nItem: 999] ?  
  
**Ambiente**   
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**

Alíquota da CBS (tag: pCBS) deve ser igual a 0,9% para documento com data de emissão no ano de 2025 e 2026. Art. 346 da LC 214/2025. Exceção: Se o cClassTrib possuir indicador de Tributação Regular, o pCBS deve ser igual a zero.  
Observação: Alíquota de referência a ser publicada para anos posteriores a 2026.

Verifique a documentação abaixo, nela demonstra como configurar a alíquota do CBS:

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar o cálculo do CBS/IBS no Configurador de Tributos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33325130340887-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-c%C3%A1lculo-do-CBS-IBS-no-Configurador-de-Tributos)

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 - Como calcular IBS e CBS com redução de alíquota?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35813572745111-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-IBS-e-CBS-com-redu%C3%A7%C3%A3o-de-al%C3%ADquota)

Para informações sobre a tabela do cClassTrib acesse o link abaixo:

[Tabela cClassTrib](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=dRTFFnw8z08=)

Obs: Caso tenha duvidas com a documentação acima entrar em contato com a equipe Fiscal.
