---
article_id: 15310825405719
category: SIGAACD - Automação e Coleta de Dados
content_hash: 4573e9ab5c4dffec734c1c3f97dcb73fe5bda4fcee387a42d859af30f63c5eae
fetched_at: '2026-06-28T22:39:11.247468+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDV060 - Como criar
  o campo CB5_PRINTR?
type: support-article
updated_at: '2023-07-04T16:42:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15310825405719-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDV060-Como-criar-o-campo-CB5-PRINTR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15310792376343) Tempo aproximado para leitura: **00:02:30 min****Dúvida**Como criar o campo CB5\_PRINTR, para utilização da impressora local (via USB)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - 12.1.33 e superiores.  
  
**Solução**

Para realizar criação do campo CB5\_PRINTR e Consulta Padrão CB5SO manualmente, seguir os passos abaixo:

**Criar Consulta Padrão CB5SO**

Configurador\* Base de Dados>Dicionário>Base de Dados. No menu Consultas Padrão, incluir nova consulta e seguir orientações abaixo:

**Tipo de Consulta: Consulta Específica**

| Consulta | CB5SO |
| --- | --- |

| Descrição | Impressora SO |
| Tabela | CB5 - Tipos de Impressão |
| Expressão | SelectPrinter()[2] |
| Retorno | M->CB5\_PRINTR |

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15310753926423)

Após a criação da Consulta Padrão, conforme orientado acima, **Criar Campo CB5\_PRINTR:**

| Campo | CB5\_PRINTR |
| --- | --- |

| Tipo | 1-Caracter |
| Tamanho | 30 |
| Formato | @! |
| Contexto | 1-Real |
| Propriedade | 1-Alterar |
| Tít. Português | Impressora |
| Desc. Português | Impressora |
| Modo Edição | M->CB5\_DRVWIN == "1" |
| Cons. Padrão | CB5SO |

**Obs.:** O campo CB5\_PRINTR foi criado com tamanho de 30 caracteres, porém, pode ocorrer de que a descrição da impressora seja maior do que 30 caracteres, com isso, a alteração do tamanho do campo é passível de alteração, podendo aumentar o tamanho do mesmo.

Para mais detalhes:

<https://tdn.totvs.com/display/public/PROT/ACDA060+-+Criar+campo+CB5_PRINTR>

<https://tdn.totvs.com/pages/releaseview.action?pageId=731890309>

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)*
