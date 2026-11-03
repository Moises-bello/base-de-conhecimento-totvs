---
article_id: 35671454377879
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: c1781d386724ca01e007d23265d5157582ed67f02299f80852a7b8d7f0b8fff7
fetched_at: '2026-06-28T22:39:56.290956+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Anápolis/GO
  (Tomador Estrangeiro)
type: support-article
updated_at: '2025-10-16T08:38:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35671454377879-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-An%C3%A1polis-GO-Tomador-Estrangeiro
---

**Dúvida**  
Como realizar a configuração dentro do Protheus para um tomador estrangeiro na NFS-e de Goiânia/GO?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**  
Conforme exigências da prefeitura, as particularidades dos cadastros precisarão estar da seguinte maneira:  
  
**Cadastro do Cliente**  
A1\_PFISICA = 00000000000 | NIF do Tomador  
A1\_CGC = EM BRANCO | Prefeitura não aceita o envio desse conteúdo no XML (CNPJ ou CPF)  
  
**TES**  
F4\_ISSST = 1 (Dentro do Município)  
  
**Pedido de Vendas**  
C5\_ESTPRES e C5\_MUNPRES = 5201108
