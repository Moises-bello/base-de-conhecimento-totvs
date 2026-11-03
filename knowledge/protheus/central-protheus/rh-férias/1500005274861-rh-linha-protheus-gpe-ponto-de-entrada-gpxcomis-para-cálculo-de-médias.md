---
article_id: 1500005274861
category: RH - Férias
content_hash: 0dda32a07ea11dfa2c932db417c496e16bfcc0b7b5955c1cf2e6a55a0da77b9a
fetched_at: '2026-06-28T22:43:59.414463+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Ponto de entrada GPXCOMIS para cálculo de médias
type: support-article
updated_at: '2025-09-02T17:07:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005274861-RH-Linha-Protheus-GPE-Ponto-de-entrada-GPXCOMIS-para-c%C3%A1lculo-de-m%C3%A9dias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31465543544471) Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Na rotina de cálculo de médias foi criado o **ponto de entrada GPXCOMIS.**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**A finalidade é possibilitar a **inclusão de outros código de verbas para serem consideradas como verbas de comissão** e desta forma serem **consideradas para o cálculo da média dos maiores valores de comissões.**

**Programa Fonte:**   
GPEXMED.PRX

**Sintaxe**

GPXCOMIS - Verbas de Comissão ( ) --> String

**Retorno**

String(caracter)

* String contendo os códigos das verbas a serem consideradas como comissão para o cálculo da média dos maiores valores.

**Procedimentos para Implementação**

**1.** No Rdmake, defina uma string com os código de verbas a serem consideradas como comissão.

**2.** Faça o tratamento necessário.

**3.** O retorno esperado é uma string contendo o código das verbas, com separador entre elas, a serem consideradas como comissão

**4.** Obtenha o pacote do GPEXMED, que está no pacote acumulado de RH disponível no portal:   
[Como baixar o Pacote Acumulado de RH?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-MP-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-continua-acumulado-do-modulo-Gest%C3%A3o-de-Pessoal)

**Exemplos**  

```
#INCLUDE 'RWMAKE.CH'USER FUNCTION GPXCOMISLocal cCodigo        := '990*991*992'return(cCodigo)
```

**Saiba Mais**  
Acesse o *link* a seguir para o boletim técnico: <https://tdn.totvs.com/pages/viewpage.action?pageId=642866774>
