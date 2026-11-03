---
article_id: 360014707532
category: SIGAEST - LEGAIS
content_hash: fc887389f224db4ea06a3a1fba4b9459c66243f8e754f53d26459e8a0c0290a1
fetched_at: '2026-06-28T22:38:51.582284+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: MP - SIGAEST - Bloco K - Rotinas e Fontes envolvidos
type: support-article
updated_at: '2021-04-28T15:12:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014707532-MP-SIGAEST-Bloco-K-Rotinas-e-Fontes-envolvidos
---

**Dúvida**Quais as Rotinas e Fontes envolvidos na geração do Bloco K do SPED?  
  
**Ambiente**Protheus – Estoque/Custos – A partir da versão 11.80  
  
**Solução**

|  |  |
| --- | --- |
| **Rotina** | **Descrição** |
| MATXSPED.PRW | Contém as funções para geração dos registros 0210, K200, K220, K230, K235, K250 e K255. |
| SPEDFISCAL.PRW,  SPEDXFUN.PRW | Rotina responsável pela geração de todos os blocos utilizados para entrega do SPEDFISCAL.  No caso do Bloco K, esta rotina é responsável pela geração dos registros K001, K100 e K990. |
| MATR241 | O relatório de Relação do Bloco K. |
| SPEDFISCAL | Rotina para geração do arquivo SPED. Nele, a pergunta "Gera Bloco K" influencia na geração ou não do bloco. |

**Saiba mais:**

*[MP - SIGAEST - Como o Protheus gera no SPED o Registro K200: Estoque Escriturado?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019502091-MP-SIGAEST-Como-o-Protheus-gera-no-SPED-o-Registro-K200-Estoque-Escriturado-)*

*[MP - SIGAEST- Quais os tipos de produtos e como definir um tipo que não seja padrão para que seja considerado no Bloco K200?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033136554)*

*[MP - SIGAEST - BLOCO K Escopo Reduzido K200/K280](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023095891-MP-SIGAEST-BLOCO-K-Escopo-Reduzido-K200-K280)*

*[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)*
