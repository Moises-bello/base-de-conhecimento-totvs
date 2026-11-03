---
article_id: 360033604534
category: Materiais - Compras (SIGACOM)
content_hash: 6329e84bff8f76a4dedd1c57c10ad1580b847faf9fc7c828f354ad86d4a24dac
fetched_at: '2026-06-28T22:41:18.862675+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help A12003 referente
  a Segunda Unidade de Medida na Nota de Entrada
type: support-article
updated_at: '2022-05-18T20:57:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033604534-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-A12003-referente-a-Segunda-Unidade-de-Medida-na-Nota-de-Entrada
---

**Ocorrência**

Help A12003 referente a Segunda Unidade de Medida na Nota de Entrada  
  
**Ambiente**

Microsiga Protheus – Compras – A partir da versão 11.80  
  
**Causas**

* Validação do parâmetro **MV\_CALC2UM** como .T. (*True*) e a quantidade na segunda unidade de medida não está preenchida, pois não há fator de conversão para a segunda unidade de medida informada no cadastro do produto que está sendo utilizado.
* Resultado da multiplicação entre a quantidade do item e o valor unitário é superior a 0.09 centavos.

**Solução**

* Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesso o módulo de compras;  
2. Acesse a rotina Cadastro de produto (MATA010);  
3. Informe o fator de conversão no campo **B1\_CONV**;  
4. Poderá também configurar o parâmetro **MV\_CALC2UM** como .F. (*False*), porém o campo de Valor Total ficará bloqueado para edição;  
5. Outra alternativa para que a mensagem não ocorra é informar a quantidade na segunda unidade de medida manualmente.

* É necessário que o total do item tenha no máximo 0.09 centavos de diferença entre a quantidade x valor unitário. Não é possível remover a validação via configuração ou ponto de entrada.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
