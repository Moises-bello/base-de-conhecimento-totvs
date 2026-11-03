---
article_id: 360021352271
category: RH – DIRF
content_hash: f8dc276ebb33ac4c9b64b10d62ba91928d4c1e02b117e98df950d909098c9f5c
fetched_at: '2026-06-28T22:44:07.891149+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Configuração das verbas de PLR Participação nos
  Lucros da DIRF
type: support-article
updated_at: '2025-08-19T17:23:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021352271-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-das-verbas-de-PLR-Participa%C3%A7%C3%A3o-nos-Lucros-da-DIRF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34295696424983)**Tempo aproximado para leitura:**00:01:00 min**

**Dúvida**Como realizar a configuração das verbas de PLR (Participação nos Lucros) para a DIRF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**O valor recebido como participação nos lucros possui tributação exclusiva, portanto através do cadastro de verbas, localize o Id para cálculo indicado abaixo, e então na pasta **Anuais,** informe a incidência conforme abaixo no campo **DIRF**:

ID 0151 configurar com incidência **O1**:

ID 1279 configurar com incidência **O1**:

ID 0152 configurar com incidência**Q1**:

Verifique, através do cadastro de beneficiários a verba para PLR, então localize o código da verba no cadastro de verbas e configure a incidência **C3.**

Esses valores serão informados sob o código de retenção **3562 – Participação nos Lucros ou Resultados (PLR) após a geração da Dirf (Manutenção do arquivo).  
  
Exemplo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6936797242647)**No informe de rendimento, o PLR será apresentado no quadro 5 linha 03-Outros, sendo o valor liquido a ser impresso**:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6936910646167)**E no quadro 7: **![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6936952092439)**

**Saiba mais**  
[RH - Linha Protheus - GPE - Passo a Passo para geração do Arquivo magnético da DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022076092)

[Página centralizadora Protheus - DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
