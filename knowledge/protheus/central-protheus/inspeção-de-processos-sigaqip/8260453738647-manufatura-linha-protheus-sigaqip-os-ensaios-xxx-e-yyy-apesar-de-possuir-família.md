---
article_id: 8260453738647
category: Inspeção de Processos (SIGAQIP)
content_hash: a8e93f084f095d95517acb5cc94b41d8a390e12c27c5d79b3e154b973db4af64
fetched_at: '2026-06-28T22:42:25.877918+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - O(s) ensaio(s) xxx e yyy apesar de
  possuir família de instrumento na especificação do produto possuem medições onde
  o instrumento não foi informado
type: support-article
updated_at: '2022-08-18T13:07:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8260453738647-Manufatura-Linha-Protheus-SIGAQIP-O-s-ensaio-s-xxx-e-yyy-apesar-de-possuir-fam%C3%ADlia-de-instrumento-na-especifica%C3%A7%C3%A3o-do-produto-possuem-medi%C3%A7%C3%B5es-onde-o-instrumento-n%C3%A3o-foi-informado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:50:00 min****Ocorrência**No módulo **SIGAQIP - Inspeção de Processos**, ao confirmar a inspeção na rotina **QIPA215 - Resultados** é exibida a mensagem **O(s) ensaio(s) xxx e yyy apesar de possuir família de instrumento na especificação do produto possuem medições onde o instrumento não foi informado**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Causa**Esta mensagem é exibida quando os ensaios descritos na mensagem possuem relacionamento com família de instrumento no **QIPA010 - Especificação de Produto**, e o instrumento não foi informado no **QIPA215** na aba **Instrumento** para cada medição informada durante a inspeção.  
  
**Solução**Para solucionar essa mensagem, deve ser informado o instrumento para o ensaio especificado, na aba **Instrumento** da rotina **QIPA215**.
