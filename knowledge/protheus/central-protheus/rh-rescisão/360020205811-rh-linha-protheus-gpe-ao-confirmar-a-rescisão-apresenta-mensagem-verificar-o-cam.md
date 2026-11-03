---
article_id: 360020205811
category: RH - Rescisão
content_hash: c06efd310913629db8dee580b0ee533fefe0c90f0c3c69185322c6cccc3a76e7
fetched_at: '2026-06-28T22:43:48.468226+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao confirmar a rescisão apresenta mensagem: Verificar
  o campo quantidade de lançamentos no cadastro da(s) verba(s) abaixo'
type: support-article
updated_at: '2026-06-25T12:30:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020205811-RH-Linha-Protheus-GPE-Ao-confirmar-a-rescis%C3%A3o-apresenta-mensagem-Verificar-o-campo-quantidade-de-lan%C3%A7amentos-no-cadastro-da-s-verba-s-abaixo
---

**Ocorrência**Ao calcular uma rescisão complementar por dissídio onde foi executada a rotina Dissídio Retroativo e gerada as verbas para a rescisão, ao tentar confirmar a rescisão é apresentada a mensagem "Verificar o campo quantidade de lançamentos no cadastro da(s) verba(s) abaixo":

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360015920592)

**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Causa**  
Quantidade de lançamentos da verba menor que a quantidade de lançamentos no cálculo.  
  
**Solução**Essa mensagem é apresentada quando no cadastro da Verba o campo **QTDE. LANCTO** esta com **1**, então entre na rotina de **Verbas** pelo caminho **>Atualizações >Definições de Cálculos >Verbas,** e **altere** o campo para **9**, Fazendo o ajuste, o sistema permitirá que a rescisão seja salva com a verba calculada mais de uma vez (sendo uma integrada da rotina de Dissídio Retroativo e outra calculada na rotina de Rescisão):

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360015963931)  
  
  
**Saiba Mais**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
