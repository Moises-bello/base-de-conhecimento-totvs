---
article_id: 4429819665815
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 79d5119cc13942ba3239c46abc00e0d36c7b003eb40725f60a7ede1f03b580bb
fetched_at: '2026-06-28T22:39:51.324716+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Dedução automática
  do frete nacional para os incoterms CPT, CIP, DDU ou DAP
type: support-article
updated_at: '2025-11-28T17:43:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4429819665815-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Dedu%C3%A7%C3%A3o-autom%C3%A1tica-do-frete-nacional-para-os-incoterms-CPT-CIP-DDU-ou-DAP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36644589555223)Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Como realizar a dedução automática do Frete Nacional em processos com incoterm CPT, CIF, DDU ou DAP?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Import Control* – Todas versões  
  
**Solução**  
Para realizar a dedução automática do frete nacional, primeiramente deve-se ativar o parâmetro **MV\_DEFRENA**.  
No embarque/desembaraço, informe o valor do frete total no campo Vl. Frete PP ou Vl. Frete CC e o valor do frete nacional no campo Vl. Frete TN na pasta Transporte.  
No momento em que entrar na rotina Recebimento de Importação(EICDI154) e clicar em Primeira, Única ou Mãe, será exibida a mensagem perguntando se deseja realizar a dedução automática do frete nacional.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4429790176919)

Clicando em sim, o valor do frete nacional entrará como dedução no total da NF.  
  
**Saiba mais**  
[Recebimento de Importação - Conta e Ordem - Nota Complementar](https://tdn.totvs.com/pages/releaseview.action?pageId=555859396)
