---
article_id: 4415145086487
category: RH - Provisão
content_hash: db0e3ebb5ed36b74ab3f20f8eae1ac23eaf1f7fb3b439f7f7a650854d85c8aa6
fetched_at: '2026-06-28T22:43:56.904672+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como funciona o cálculo de provisão quando há reintegração
  de funcionário
type: support-article
updated_at: '2024-12-23T16:41:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415145086487-RH-Linha-Protheus-GPE-Como-funciona-o-c%C3%A1lculo-de-provis%C3%A3o-quando-h%C3%A1-reintegra%C3%A7%C3%A3o-de-funcion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27338421812375) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como funciona o cálculo da provisão quando há reintegração de funcionário?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**No Sistema temos duas formas de reintegração: **Retroativa a admissão** e outra com **nova data de admissão**, e em ambas o sistema não trata os valores quitados em rescisão.  
  
Quando ocorre reintegração retroativa a data de admissão, temos dois cenários para cálculo de provisão:  
  
**Reintegração no mesmo mês da rescisão**  
Após reintegração, é necessário excluir o cálculo da provisão (caso já tenha sido efetuado) e calcular novamente a provisão, dessa forma o cálculo será feito de forma normal, sem considerar a rescisão:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415151281687)  
  
**Reintegração em meses posteriores a rescisão**

Excluir o cálculo da provisão do mês da rescisão e calcular a provisão do mês referente a reintegração do funcionário. O sistema irá calcular a provisão do zero, desta forma não terá saldo anterior no cálculo da provisão pós reintegração:![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415139504791)

**Reintegração com nova data de admissão**  
Quando a reintegração é com nova data de admissão, o cálculo da provisão é efetuado considerando a nova data de admissão, então não existirá saldo anterior no primeiro cálculo de provisão.  
  
**Saiba mais**

[Manual Provisão](https://tdn.totvs.com/pages/releaseview.action?pageId=754967312)

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)

[RH - Linha Protheus - GPE - Como reintegrar um Funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050788953)

[RH - Linha Protheus - GPE - Quais são as opções de reintegração de funcionários disponíveis](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36002736467)
