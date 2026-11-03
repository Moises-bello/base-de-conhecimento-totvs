---
article_id: 10160525423127
category: Comércio Exterior - Easy Export Control - Tabelas
content_hash: 512110245abcf9197bfc7d5b4d028c19ebfab2d6509f1f5c79330bde4386aff5
fetched_at: '2026-06-28T22:37:01.455433+00:00'
product: protheus
section_id: 1500001549222
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Alteração do campo
  país (Y9_PAIS) no cadastro de portos/aeroportos
type: support-article
updated_at: '2022-11-11T12:59:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10160525423127-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Altera%C3%A7%C3%A3o-do-campo-pa%C3%ADs-Y9-PAIS-no-cadastro-de-portos-aeroportos
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura**: 00:03:00 min****Dúvida**No cadastro de Portos/Aeroportos, é possível realizar a alteração do campo "PAÍS" quando o mesmo é estrangeiro (EX), pois o mesmo apresenta com o campo Y9\_PAIS bloqueado? Sendo possível em casos nacionais.**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Export Control* – Todas versões  
  
**Causa**Informado a necessidade no EEC, no cadastro de Portos/Aeroportos de alteração do campo "PAÍS" quando o mesmo é estrangeiro (EX) não é possível alterá-lo, sendo possível somente em casos nacionais.   
  
**Solução**O cadastro de Portos/Aeroportos não possui tratamento específico para país estrangeiro. O que ocorre, é que quando o cadastro já está em uso, como por exemplo quando o cadastro do Porto/Aeroporto está em uso em uma Via de Transporte, o sistema não permite mais que as informações sejam alteradas. Este tratamento é válido tanto para qualquer tipo de país. Isto é válido para Portos/Aeroportos cadastrados tanto como Origem como Destino.  
Caso seja possível excluir a origem e destino da via de transporte (caso não tenha sido utilizada), o sistema passará a permitir a alteração do País.
