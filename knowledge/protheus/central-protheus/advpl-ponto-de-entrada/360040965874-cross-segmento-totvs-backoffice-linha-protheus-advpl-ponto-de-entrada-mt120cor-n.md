---
article_id: 360040965874
category: ADVPL - Ponto de Entrada
content_hash: 79903e6e45e93f78220593eb71b5c93667829fd6c39b25def38610ef1afeb433
fetched_at: '2026-06-28T22:40:12.645686+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  Mt120cor não aceita funções de usuário
type: support-article
updated_at: '2022-06-21T17:52:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040965874-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-Mt120cor-n%C3%A3o-aceita-fun%C3%A7%C3%B5es-de-usu%C3%A1rio
---

**Dúvida**O PE MT120COR, não mais aceita funções de usuário dentro do Array?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.25  
  
**Solução**A condição  não está mais sendo executada pois o **MATA120** mudou a maneira de tratar o retorno deste ponto de entrada. Antes ele mantinha a ordem do *array* da mesma maneira que o usuário havia passado. Agora ele verifica se existe uma *user function* e acaba colocando o valor do usuário como último no *array*.  
A legenda do *browse* não varre todos os elementos do *array*. Para cada linha ele varre o resultado do *array* até conseguir um resultado válido. Desta maneira se todas as condições forem satisfeitas pelas elementos inicias do *array* a de usuário não será realizada.  
Mesmo com a alteração do **MATA120** caso nenhuma condição das legendas acima inicias(ou seja, as do padrão) seja satisfeita ele **chamará a função do usuário.****Saiba Mais**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Ponto de entrada MT120COR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020817691)
