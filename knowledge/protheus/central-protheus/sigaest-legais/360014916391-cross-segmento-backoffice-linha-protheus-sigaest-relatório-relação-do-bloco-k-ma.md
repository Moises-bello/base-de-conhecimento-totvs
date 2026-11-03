---
article_id: 360014916391
category: SIGAEST - LEGAIS
content_hash: b14ac402be03fc747eb4117e02ce057fe4025e29df8562ebf232338ee9eeec3f
fetched_at: '2026-06-28T22:38:51.403800+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST  - Relatório Relação
  do Bloco K - MATR241
type: support-article
updated_at: '2025-12-17T14:33:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014916391-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Relat%C3%B3rio-Rela%C3%A7%C3%A3o-do-Bloco-K-MATR241
---

O relatório Relação do Bloco K (MATR241) lista os dados processados para os registros do Bloco K do SPED Fiscal, usando o mesmo componente do SPEDFISCAL, facilitando a análise dos dados de Materiais e Fiscal. Inclui parâmetros de período, geração do registro 0210 por movimento e detalhamento dos registros K250/K255, apresentando informações de forma amigável ao usuário.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37089617655575) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**  
Relatório Relação do Bloco K - MATR241  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
  
Relatório Relação do Bloco K - MATR241

O relatório de Relação do **Bloco K** (**MATR241**) lista todos os dados processados e que serão gravados nos Registros do Bloco K do SPED Fiscal, utilizam o mesmo componente responsável pelo processamento do Bloco K presente na rotina SPEDFISCAL.  Assim, os dados resultantes entre ambas as rotinas são os mesmos. Ele tem como objetivo facilitar a análise dos dados gerados pelo Bloco K, isolando os pontos processados pela equipe de Materiais e Fiscal e apresentar as informações ao usuário de forma amigável. Os componentes responsáveis pela geração do Bloco K, geram os registros K001, K100 e K990, porém, quando o processamento é realizado através da rotina SPEDFISCAL, eles são ignorados e gerados dentro do próprio SPEDFISCAL. Dentro do relatório eles são apenas informativos.

O relatório possui os seguintes parâmetros:

* **Do período:**Período inicial do processamento.
* **Até o período**: Período final do processamento.
* **Reg. 0210 por movimento**: Indica se gera o registro 0210 por movimentação. Caso marcado como NÃO, o registro 0210 é gerado **Por Estrutura**.
* **Detalhar K250/K255**: Indica se detalha ou não os Registros K250/K255. Por padrão os registros são gerados no SPEDFISCAL sem detalhamento.

**Saiba mais:**

[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)
