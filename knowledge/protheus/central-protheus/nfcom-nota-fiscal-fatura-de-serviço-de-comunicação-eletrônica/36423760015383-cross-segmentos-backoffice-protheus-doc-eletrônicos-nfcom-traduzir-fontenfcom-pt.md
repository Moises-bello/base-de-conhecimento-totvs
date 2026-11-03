---
article_id: 36423760015383
category: NFCOM - Nota Fiscal Fatura de Serviço de Comunicação Eletrônica
content_hash: 4d9696c04550cc916042644909b45ff2a0d72d7d4dc9c47b49bf2baa467b1df4
fetched_at: '2026-06-28T22:39:55.195213+00:00'
product: protheus
section_id: 33828030194199
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFCOM - Traduzir
  fonteNFCOM_pt-br.TRes não disponivel!
type: support-article
updated_at: '2025-12-03T12:43:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36423760015383-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFCOM-Traduzir-fonteNFCOM-pt-br-TRes-n%C3%A3o-disponivel
---

**Ocorrência**  
Ao tentar acessar a rotina SPEDNFE - Opção 8 (NFCOM) é apresentada a mensagem: "**Traduzir fonteNFCOM\_pt-br.TRes não disponivel!".**  
   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Causa**  
Para correção, ambos os pacotes devem ser aplicados abaixo no **Protheus**:  
  
**1.** Acumulado: [clique aqui para download](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1171486) (12.1.2410).  
**2.** Pontual: [clique aqui para download](https://r.totvs.io/p/1211710) (12.1.2410) - Principal, o qual **contém o fonteNFCOM\_pt-br.TRes incluso dentro do patch.**  
  
Lembrando que o arquivo .TRES está contido dentro dos pacotes, ou seja, não será listado nos contents dentro do VSCODE.  
Após isso, basta reiniciar os serviços por completo, acessar a rotina novamente e realizar novos testes.
