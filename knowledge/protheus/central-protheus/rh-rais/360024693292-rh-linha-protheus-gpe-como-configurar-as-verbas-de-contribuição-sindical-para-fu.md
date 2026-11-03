---
article_id: 360024693292
category: RH - RAIS
content_hash: b0d2878395aad9fc8925b11819e4d48bdfa4d7486af87465a255b5a76d087ee5
fetched_at: '2026-06-28T22:44:05.668489+00:00'
product: protheus
section_id: 360000030327
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar as verbas de contribuição sindical
  para funcionários e profissionais liberais
type: support-article
updated_at: '2025-08-21T17:26:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024693292-RH-Linha-Protheus-GPE-Como-configurar-as-verbas-de-contribui%C3%A7%C3%A3o-sindical-para-funcion%C3%A1rios-e-profissionais-liberais
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34349968247575)**Tempo aproximado para leitura**: 00:01:00 min**

**Dúvida**Como configurar as verbas de contribuição sindical para funcionários e Profissionais Liberais?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões

**Solução**Conforme estabelece o **artigo 583** da CLT, os agentes ou trabalhadores autônomos e profissionais liberais (não organizados em empresas) poderão optar pelo recolhimento da contribuição sindical anual aos respectivos sindicatos da categoria.Para solucionar essa dúvida, realize os seguintes passos:  
  
As contribuições descontadas dos funcionários constam em verbas, nos acumulados anuais (tabela SRD) e devem possuir configuração de incidência para RAIS verificadas (**L/M/O/P/Q**).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023358712)  
  
  
O sistema busca nos acumulados anuais (SRD) e direciona para a **RAIS,** os valores descontados nas verbas com os identificadores de cálculo abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023397511)

**Configuração da verba:**

Em Atualizações> Cadastros> Verbas de identificador 0068:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023397591)

Na aba Anuais, informar a letra conforme o id de cálculo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023358812)  
  
**Observação**:

O identificador de cálculo **0246** trata-se de uma verba de base, e somente constará na movimentação anual dos funcionários que contribuem para o sindicato de sua categoria.

Para determinar se um funcionário é sindicalizado ou não, e para que tal informação seja considerada para o GDRAIS, o Sistema deve localizar a verba de Contribuição Associativa, que estará configurada com a incidência **L** ou **M**para RAIS.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023358872)  
  
  
**Saiba Mais**<http://tdn.totvs.com/x/DpjHEw>
