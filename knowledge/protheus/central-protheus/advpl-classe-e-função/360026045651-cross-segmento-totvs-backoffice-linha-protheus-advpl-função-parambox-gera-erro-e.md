---
article_id: 360026045651
category: ADVPL - Classe e Função
content_hash: d08ff999e484c02619476c760d027a9e6cddee2d7db1a0b306f436823c1a7da8
fetched_at: '2026-06-28T22:40:16.829465+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Função parambox
  gera erro em ponto de entrada
type: support-article
updated_at: '2021-10-26T15:32:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026045651-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-parambox-gera-erro-em-ponto-de-entrada
---

**Ocorrência**Ao utilizar a função ParamBox() em alguns pontos de entrada do sistema, está sendo gerado erro na rotina padrão.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Causa**A função ParamBox() ao ser instanciada altera o estado do Pergunte() em memória, fazendo assim com que seja gerado erro em rotinas padrões que esperam por um determinado valor (tipagem ou conteúdo) em um MV\_PAR\*\* e recebam outro.  
  
**Solução**Armazenar o estado atual do Pergunte() em memória e restaurar após a utilização do ParamBox().  
Observação: A Função **Parambox** é uma função interna não recomendamos a utilização em customizações   
  
**Saiba mais**  
[Manipulação de perguntas (salvar estado)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018402211)

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Funções, classes e variáveis de propriedade interna](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016461772)
