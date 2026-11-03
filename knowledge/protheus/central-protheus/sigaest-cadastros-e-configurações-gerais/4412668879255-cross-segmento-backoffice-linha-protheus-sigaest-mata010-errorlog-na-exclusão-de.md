---
article_id: 4412668879255
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 0eb7d8fec9bc97208ce97f95724144252a2a73ce52e0fd456ef2d4c42cb6bca7
fetched_at: '2026-06-28T22:39:08.296611+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 -  Error.log
  na exclusão de um produto Invalid column name 'S5_CODITE'.
type: support-article
updated_at: '2021-11-19T11:25:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412668879255-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Error-log-na-exclus%C3%A3o-de-um-produto-Invalid-column-name-S5-CODITE
---

**Ocorrência**No momento da exclusão de algum produto é apresentado o error.log Invalid column name 'S5\_CODITE'.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**  
Esse incidente ocorre, pois o campo S5\_CODITE é um campo virtual, e está referenciado em um relacionamento (SX9).  
  
**Solução**

- Via APSDU acessar o arquivo SX9;  
- Realizar filtro pela coluna **X9\_EXPCDOM igual a S5\_CODITE.**  
- Excluir o registro da SX9.  
  
Imagem de exemplo:  
![](https://totvssuporte.zendesk.com/attachments/token/BZNPz0brsU7v1Lf1rrcfQ9WJt/?name=inline-1318652549.png)​  
  
**Observações:**

- Recomendamos que o procedimento seja executado primeiramente em ambiente de homologação e que realizem os devidos testes antes de aplicar na base de produção.  
  
- Sempre efetuar um backup do RPO antes da aplicação e realizar testes em ambiente padrão de homologação.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
