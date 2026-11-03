---
article_id: 4418849260439
category: SIGAEST - RELATORIOS
content_hash: a64031b60aec9bd71c4c9f4bb9e3f7607d0544b9dd71297174fbfa3935259c31
fetched_at: '2026-06-28T22:39:05.977703+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR430 - Relatório
  de Formação de Preço
type: support-article
updated_at: '2025-11-24T19:30:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418849260439-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR430-Relat%C3%B3rio-de-Forma%C3%A7%C3%A3o-de-Pre%C3%A7o
---

É possível imprimir a parte superior da rotina de Formação de Preço (MATC010) usando o relatório FORMAÇÃO DE PREÇOS (MATR430) a partir do release 12.2510, via CONSULTA SMART VIEW ESTSV001, pois os relatórios TREPORT serão descontinuados no Protheus. O artigo explica o passo a passo para gerar o relatório filtrando por produto e exibindo a estrutura desejada.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36554035711895) Tempo aproximado para leitura: **00:03:30 min**

**Dúvida**

É possível gerar um relatório que imprima a parte superior da rotina de Formação de Preço (MATC010)?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Sim, é possível utilizar o relatório **FORMAÇÃO DE PREÇOS (MATR430).** A partir do release 12.2510 somente é possível utilizando a **CONSULTA SMART VIEW ESTSV001 (**[**link**](https://tdn.totvs.com/x/f4L1Lg)**)**. No respectivo release relatórios TREPORT serão descontinuados no Protheus.

Passo a passo com exemplo de uso do MATR430:  
  
1.  Ao abrir a rotina de Formação de Preços (MATC010), selecionamos um item para ser exibido dessa forma:   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418824682391)  
  
  
2. Supondo que queira imprimir esse grid, pode-se fazer através da rotina MATR430:   
  
- Em acesso ao Smartclient digite MATR430 e pressione F3  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418824891543)  
  
-  Será apresentada a tela inicial da rotina em seguida clique em Outras Ações > Parâmetros    
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418846584727)  
  
**Neste caso em particular, optamos por filtrar por produto e exibir a estrutura, porém pode ser utilizado de outras formas.**  
  
Feito isto, após clicar em "OK" o relatório será exibido:    
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418863340567)

**Saiba mais:**

[Smart View - Estoque (Consultas)](https://tdn.totvs.com/x/M8LrL)

[SIGAEST - Descontinuidade de Relatórios do Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23374418520087-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Descontinuidade-de-Relat%C3%B3rios-do-Estoque)

[Fontes de Relatórios TREPORT Estoque/Custos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058126794-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Fontes-de-relat%C3%B3rios-Estoque-para-altera%C3%A7%C3%A3o-ou-customiza%C3%A7%C3%A3o-fora-do-padr%C3%A3o)

[Clique aqui e veja mais artigos sobre Relatórios no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)
