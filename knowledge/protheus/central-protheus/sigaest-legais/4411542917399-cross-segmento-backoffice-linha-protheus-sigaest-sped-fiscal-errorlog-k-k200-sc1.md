---
article_id: 4411542917399
category: SIGAEST - LEGAIS
content_hash: 7d9b9670c66ab5982fcb2f511e618b535fbd6378f709eccd2d2953e935d75c9b
fetched_at: '2026-06-28T22:38:51.830619+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - SPED Fiscal - Error.log
  - K_K200_SC192070: Error : grupo de arquivos  inválido especificado.'
type: support-article
updated_at: '2021-10-27T14:34:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411542917399-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-SPED-Fiscal-Error-log-K-K200-SC192070-Error-grupo-de-arquivos-inv%C3%A1lido-especificado
---

**Ocorrência**

Ao processar o SPED Fiscal ocorre o erro: K\_K200\_SC192070: Error : 1921 (37000) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]grupo de arquivos 'TOTVS12' inválido especificado.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**  
Esse incidente ocorre, normalmente quando existe alguma restrição dentro do banco de dados.  
  
**Solução**

**Importante:**Esse processo deve ser realizado pelo DBA responsável da organização, pois se trata de uma configuração dentro do Banco de Dados.

Dentro do banco de dados em questão, clicar com botão direito do mouse > propriedade:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411539796887/mceclip1.png)

E acessar a opção de Arquivos e Grupo de Arquivos:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411545221399/mceclip3.png)

Em Arquivos e Grupo de Arquivos é necessário criar os campos "INDEX" e "DATA" nas propriedades do banco de dados, conforme os prints abaixo:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411545257111/mceclip4.png)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411540145431/mceclip5.png)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)*
