---
article_id: 15112232858519
category: ADVPL - Classe e Função
content_hash: 5559c8b3d4c8e6807fdd8f7cbd1690281f227abbb09f80e02751019be39049c8
fetched_at: '2026-06-28T22:40:20.630576+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL -  Como verificar
  se um fonte é customizado no sistema?
type: support-article
updated_at: '2023-06-07T17:53:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15112232858519-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-verificar-se-um-fonte-%C3%A9-customizado-no-sistema
---

Tempo aproximado para leitura: **01:00:00 min** **Dúvida** Como verificar se um fonte é customizado no sistema?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Todas as Versões  
  
**Solução**

Para verificar se o fonte é customizado temos a função GetFuncArray() que tem por objetivo retornar um array com as funções contidas no RPO - Repositório de Objetos, a partir de uma máscara fornecida como parâmetro.

No qual a primeira posição do *array* de retorno é o tipo da função:

* Tipo da função ( USER, FULL , etc.. )
* Nome do arquivo que contém o código fonte onde a função está declarada.
* Número da linha, no código fonte, onde a função foi declarada.
* Data da última modificação do código fonte compilado.
* Hora da última modificação do código fonte compilado

Após o retorno da função GetFuncArray(), é possível validar o resultado utilizando a função GetSrcArray() para saber se o fonte encontrado está no RPO padrão ou no RPO Custom. Evitando que o fonte seja confundido com algum RDMAKE padrão.

**Saiba Mais:**

[GetFuncArray](https://tdn.totvs.com/display/tec/GetFuncArray)

[GetSrcArray](https://tdn.totvs.com/display/tec/GetSrcArray)
