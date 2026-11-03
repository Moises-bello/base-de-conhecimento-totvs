---
article_id: 23797376479895
category: Financeiro
content_hash: 1c1c6911fc1acf572194ec3877cee0d82dc5b090e5256bb25d03d7165c643348
fetched_at: '2026-06-28T22:38:04.198293+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: SIGAFIN – FINR150 – Qual motivo de algumas colunas do relatório ter delimitação
  de caracteres?
type: support-article
updated_at: '2024-06-07T10:35:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23797376479895-SIGAFIN-FINR150-Qual-motivo-de-algumas-colunas-do-relat%C3%B3rio-ter-delimita%C3%A7%C3%A3o-de-caracteres
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23797386895511) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**O relatório FINA150 impresso no padrão do sistema com suas colunas sem personalização, possui uma delimitação de caracter limite para que as informações não sejam impressas fora da folha ou truncadas.  
E por esse motivo algumas colunas padrões do relatório possuem delimitação máxima de caracter  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**

Essa limitação de conteúdo nas colunas são definida diretamente no fonte

Exemplo: A coluna "Histórico" referente ao campo E2\_HIST. No Padrão do sistema essa coluna possui um tamanho máximo de 25 caracteres para que o seu conteúdo não seja impresso fora da folha.

**Solução**Caso haja a necessidade de aumento de uma coluna, sugerimos baixar o fonte de relatório que temos no portal do cliente e efetuar a alterações conforme a necessidade no endereço abaixo:   
<https://suporte.totvs.com/portal/p/10098/download?e=1120373>
