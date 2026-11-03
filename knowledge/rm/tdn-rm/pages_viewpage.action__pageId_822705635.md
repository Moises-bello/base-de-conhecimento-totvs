---
content_hash: ed88e47c6e61091fd31d6b1354e7331fdfc21b0f2c339622e62a5e64c4470197
fetched_at: '2026-06-29T00:11:46.590534+00:00'
page_id: '822705635'
product: rm
source: tdn-rm
title: Gestão - Funções de Fórmulas - Cobrança Direta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822705635
version: 7
---

As funções de fórmulas do módulo Cobrança Direta, são utilizadas para realizar cálculos e manipulações de dados quando associadas a alguns campos que possibilitam utilização de fórmulas. Essas funções são essenciais para automatizar operações, realizar análises e gerar resultados com base em dados fornecidos. Aqui estão algumas finalidades comuns das funções de fórmulas.

---

\*Funções

CODPESSEMPR

COMPETENCIA

Exemplo de utilização de fórmulas

Os exemplos abaixo fornecem orientações sobre o uso de algumas funções de fórmulas para auxílio quanto a utilização destas.  
  
**Modelo para Código do empreendimento:**

***PARMQRY('CODPESSEMPR').value***

A expressão PARMQRY('CODPESSEMPR').value indica que a fórmula PARMQRY está sendo utilizada para recuperar o valor associado a um campo específico, onde 'CODPESSEMPR' seria o identificador desse campo. Portanto, o resultado retornado por essa expressão seria o valor correspondente ao campo referente ao código do empreendimento.

---

**Modelo para Competência:  
  
*SE  
PARMQRY('COMPETENCIA').value = ("01/2022")   
ENTAO 5   
SENAO 100***

* `SE PARMQRY('COMPETENCIA').value = ("01/2022")`: Esta parte verifica se o valor retornado pela função PARMQRY para o campo 'COMPETENCIA' é igual a "01/2022".
* Se a condição acima for verdadeira (`ENTAO 5`): Isso significa que, se a competência for "01/2022", o resultado da expressão será 5.
* Se a condição não for atendida (`SENAO 100`): Caso a competência não seja "01/2022", o resultado da expressão será 100.  
  Em resumo, o resultado da consulta retorna 5 se a competência for janeiro de 2022,  e 100 em qualquer outra situação.

Para mais informações sobre utilização de fórmulas e suas funções acesse:
