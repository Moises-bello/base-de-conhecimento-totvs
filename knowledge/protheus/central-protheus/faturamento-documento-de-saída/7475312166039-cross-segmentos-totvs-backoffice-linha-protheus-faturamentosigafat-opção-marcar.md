---
article_id: 7475312166039
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: a3c6b59faf707d4b0e12632f6e5d064e1bab62caee627539ccef5ac35b60d992
fetched_at: '2026-06-28T22:38:44.204081+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento(SIGAFAT)
  - Opção Marcar todos com filtro na Exclusão - MATA521A
type: support-article
updated_at: '2025-01-10T20:21:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7475312166039-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Op%C3%A7%C3%A3o-Marcar-todos-com-filtro-na-Exclus%C3%A3o-MATA521A
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Na utilização da opção marcar todos, quando realizou um filtro dos documentos, ao excluir o sistema esta excluindo todos os documentos de saída, não somente o marcado.   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - Todas as versões;  
  
**Solução**

Ao realizar a seleção do documento através do **"Marcar Todos"**, o componente em questão é apresentado apenas para a pesquisa, apesar de apenas um elemento ser apresentado em tela os demais continuam na seleção, pois logo ao inverter a marcação ele seleciona os demais junto, se retirar a busca verá que as linhas omitidas retornam marcadas.

Se desejar filtrar deve usar a opção Filtrar ao lado da pesquisa para a inclusão do filtro, se fizer o mesmo processo de desabilita-lo após a marcação verá que apenas o registro do filtro foi marcado.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7475251313943/mceclip1.png)

Segue documentação sobre a opção de pesquisa nos componentes de tela <https://tdn.totvs.com/display/framework/Browse+-+Criar+nova+Pesquisa>, este comportamento é geral para o componente como pode ser observado em demais rotinas.

Caso ainda tenha dúvida sobre o comportamento deste entre em contato com nosso atendimento de framework.
