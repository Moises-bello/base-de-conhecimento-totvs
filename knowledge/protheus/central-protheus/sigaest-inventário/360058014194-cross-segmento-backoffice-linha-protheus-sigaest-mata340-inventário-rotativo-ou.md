---
article_id: 360058014194
category: SIGAEST - INVENTÁRIO
content_hash: c2ad6383326ffbe21756bfd3cee0348ce801c71ac064b98f34dce7b8f3f05fa2
fetched_at: '2026-06-28T22:38:50.369321+00:00'
product: protheus
section_id: 1500001538961
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA340 - Inventário
  rotativo ou cíclico no Protheus
type: support-article
updated_at: '2025-12-10T13:45:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058014194-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA340-Invent%C3%A1rio-rotativo-ou-c%C3%ADclico-no-Protheus
---

No Protheus, o inventário rotativo é feito informando o campo "Per. Invent. (B1\_PERINV)" para definir a periodicidade em dias da contagem dos itens. O processo padrão de inventário deve ser seguido para correção. Não há processo automatizado para inventário rotativo, mas pode-se usar a rotina de bloqueio por data para controlar movimentações.

**Dúvida**  
Como efetuar inventário rotativo ou cíclico no Protheus?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Para efetuar inventário rotativo no Protheus é necessário informar o campo **Per. Invent. - (B1\_PERINV)** que define, em dias, a periodicidade em que se deve contar um determinado item do Estoque.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100620953)

**Exemplo:** o produto **A** deve ser inventariado de 30 em 30 dias. A partir deste instante, a data do inventário (B2\_DTINV) passa a ser de extrema importância, pois, o sistema assumirá como saldo a ser inventariado o saldo do final do dia do Inventário (B7\_DATA).

Para corrigir o inventário, é necessário efetuar todo o processo padrão de inventário, desde a digitação até o processamento do inventário. Veja o artigo sobre o padrão para processar o inventário. ([Ver artigo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049739614-MP-SIGAEST-MATA340-Processo-padr%C3%A3o-para-Inventariar-produtos-no-Estoque?source=search))

**Obs.: No Protheus o Inventário rotativo dos produtos é efetuado da forma descrita acima. Salientamos que não temos um** **processo automatizado** **de inventario rotativo no sistema.**

Dica: utilizar a rotina BLOQUEIO DE INVENTÁRIO por data calculada, [conforme instruções do artigo,](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021321072-MP-SIGAEST-MATA271-Bloqueio-de-produtos-para-invent%C3%A1rio-por-data-calculada?source=search) dessa forma é possível bloquear as movimentações que estão em período de inventário.

**Os principais campos envolvidos no processo, são B1\_PERINV, B2\_DINVENT e B7\_DATA.**

Pode-se também [personalizar o relatório](https://tdn.totvs.com/pages/viewpage.action?pageId=338377994) Lista de Produtos (MATR280) de forma que apresente os dados da tabela SB1 e SB2 para ter uma visão dos campos envolvidos e facilitar as análises. Caso desejar, a TOTVS também disponibiliza no portal do cliente os fontes de relatórios caso desejar customizar fora do padrão.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100691733)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100691933)

|  |
| --- |
| Observações importantes: |
| **O Protheus possui o inventario rotativo por curva ABC?**  Atualmente, no sistema nativo do Protheus, não é possível realizar o inventário rotativo por curva ABC. Contudo, é possível executar a curva ABC por meio do Mestre de Inventário, utilizando o módulo SIGAACD.  **Para maiores informações:**  [Inventário por Produto (ACDV035-SIGAACD)](https://tdn.totvs.com/pages/releaseview.action?pageId=780791398) |

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Inventário no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033402-SIGAEST-INVENT%C3%81RIO)
