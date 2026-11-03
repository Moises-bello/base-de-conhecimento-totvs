---
article_id: 1500001746381
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: d723076798f0872e74ea46478cf4278f1784814d41232b1b3e80946b7dffb739
fetched_at: '2026-06-28T22:39:49.979782+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - As Taxas Foram
  Atualizadas Recalcule as Adições.
type: support-article
updated_at: '2022-04-27T21:03:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001746381-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-As-Taxas-Foram-Atualizadas-Recalcule-as-Adi%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Ao  Gerar a Declaraçao de Importação Eletrônica DI, apresenta a mensagem: As taxas foram atualizadas recalcule as adições, como ajustar?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – A partir da versão 12.  
  
**Solução**No cenário onde o parâmetro **MV\_TEM\_DI** está habilitado, ao transmitir para integração (ainda que para análise) o processo de desembaraço, o sistema atualizará a data de referência para a taxa do *US$* do processo; caso a data/taxa sejam diferente da que encontra-se informada no processo, deverá regerar as adições, reapurando os valores dos impostos, ou seja, a data de referência para as taxas é a data de registro da Declaração de Importação.

A data/ taxa usada na geração das adições deve ser a mesma em que o processo será transmitido ao Siscomex, caso contrário, será necessária a sua regeração.

Outro ponto importante a observar é que após a geração das adições, caso seja realizada alguma alteração na adição, não é necessário regerar para que ocorra a gravação das informações;  após a alteração, caso sejam regeradas as adições, as informações dos campos que não são calculados automaticamente serão perdidos, requerendo que sejam reinformados para o processo.
