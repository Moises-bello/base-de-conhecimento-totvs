---
article_id: 6442944537495
category: Escrita Fiscal - Impostos - IPI
content_hash: 74d4ab294cfb22dd7c733270f3ea941327b63485027889016ba87509344c5860
fetched_at: '2026-06-28T22:39:28.943980+00:00'
product: protheus
section_id: 1500001538641
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal -
  Como configurar o IPI e ICMS ST na coluna de Outros do icms ?
type: support-article
updated_at: '2022-05-31T14:58:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6442944537495-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-Como-configurar-o-IPI-e-ICMS-ST-na-coluna-de-Outros-do-icms
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **HH:MM:SS min** **Dúvida**Como configurar o IPI e ICMS ST na coluna de Outros do icms ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões]  
  
**Solução**

configuração da TES para que o IPI e o ICMS ST entre na coluna de outros do ICMS  
  
TES  
Calcula icms = sim  
L fiscal icms = outros  
LF icms st = outros

Calcula ipi = sim

L fiscal ipi = outros

IPI s/n trib = sim  
MKP icm comp = não  
marg solid = nunca  
CST = 10  
  
Dessa forma ao lançar a nota fiscal de entradas o valor do ICMS ST e IPI serão Lançados na coluna de outros do ICMS  
  
![](https://totvssuporte.zendesk.com/attachments/token/qdtX9kRMleL1i3Ijlp4Ww1nRN/?name=inline-1727115700.png)​  
  
livros fiscais  
![](https://totvssuporte.zendesk.com/attachments/token/k7VZylnpLf0ConUQBTmxNilPB/?name=inline1672345528.png)​  
  
matr930  
![](https://totvssuporte.zendesk.com/attachments/token/WtSMNYZf6GY083g7dF7xjRL1n/?name=inline-781299802.png)
