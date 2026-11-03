---
article_id: 360060890473
category: RH - Relatórios
content_hash: f9a3dd8183dd16abdeec12c32f325d322699a20e20ca03efb6ba3d3192c72b4c
fetched_at: '2026-06-28T22:44:43.519535+00:00'
product: protheus
section_id: 32419371267223
source: central-protheus
title: RH - Linha Protheus - PON - Dias duplicados ao gerar o Espelho de Ponto
type: support-article
updated_at: '2025-10-16T18:33:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060890473-RH-Linha-Protheus-PON-Dias-duplicados-ao-gerar-o-Espelho-de-Ponto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35684775141015) Tempo aproximado para leitura: 00:01:30 min  
  
Ocorrência**Ao gerar o Espelho de Ponto, um dia aparece duplicado, trazendo duas, ou até mais linhas.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**No Espelho de Ponto, será visualizada duas ou mais linhas quando existem mais de uma ocorrência num mesmo dia, exemplos:   
- Um evento de hora extra e um cadastro de abono;  
- Dois abonos diferentes;  
- Uma exceção cadastrada e um abono, entre outros cenários que possuam dois registros ou duas ações para o mesmo dia.  
Nos casos acima, será gerado no espelho de ponto informações duplicadas, lhe demonstrando por padrão em duas linhas, uma com cada informação/ocorrência.  
  
**Solução**Caso queira que não seja gerada essa duplicidade no Espelho de Ponto e queira tratar esse cenário, trazendo de uma outra forma impressa, será necessário customizar o ***RDMake* IMPESP** **(fonte do espelho de ponto).**  
  
**Obs.:** Na pasta ***RDMAKES** existem* todos os *RDMakes* dos módulos de RH disponíveis para *download* ao baixar o pacote de expedição, para o passo a passo de como baixa*r* [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)
