---
article_id: 360014704792
category: SIGAEST - LEGAIS
content_hash: 20d9d4f4e66b5eb12cabdadc7329e47ce2c0a0d48033f0b7862d05c4a6e44282
fetched_at: '2026-06-28T22:38:51.566074+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: 'MP - SIGAEST - Bloco K - Registro K260: Reprocessamento/Reparo de Produto/Insumo'
type: support-article
updated_at: '2021-04-28T15:12:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014704792-MP-SIGAEST-Bloco-K-Registro-K260-Reprocessamento-Reparo-de-Produto-Insumo
---

**Dúvida**O que é o Registro K260: Reprocessamento/Reparo de Produto/Insumo?  
  
**Ambiente**Protheus – Estoque/Custos – A partir da versão 11.80  
  
**Solução**

Este registro tem o objetivo de informar o produto que será reprocessado ou que foi reprocessado e o insumo que será reparado ou que foi reparado no período de apuração do Registro K100.

Na prática, este registro é utilizado para informar um produto que será retrabalhado. Como no Protheus não possuímos um processo automatizado e padrão para execução de retrabalho de produtos, este registro não é gerado automaticamente para o **Bloco K**. Caso o cliente possua um processo automatizado/customizado ou deseje informar manualmente este registro, disponibilizamos o ponto de entrada **REGK26X,** onde é possível realizar a gravação do arquivo de trabalho do Registro K260 durante o processamento do **Bloco K**. Devido ao ponto de entrada dar acesso direto ao arquivo de trabalho, não são realizadas validações das informações gravadas.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Tipo** | **Tam** | **Dec** | **Obrig** |
| 01 | REG | Texto fixo contendo "K260" | C | 4 | - | O |
| 02 | COD\_OP\_OS | Código de identificação da ordem de produção, no reprocessamento, ou da ordem de serviço, no reparo | C | 30 | - | OC |
| 03 | COD\_ITEM | Código do produto/insumo a ser reprocessado/reparado ou já reprocessado/reparado (campo 02 do Registro 0200) | C | 60 | - | O |
| 04 | DT\_SAIDA | Data de saída do estoque | N | 8 | - | O |
| 05 | QTD\_SAIDA | Quantidade de saída do estoque | N | - | 3 | O |
| 06 | DT\_RET | Data de retorno ao estoque (entrada) | N | 8 |  | OC |
| 07 | QTD\_RET | Quantidade de retorno ao estoque (entrada) | N | - | 3 | OC |

**Tipos de Produtos considerados**

03 (Produto em Processo) e 04 (Produto Acabado).

**Saiba mais:**

*[Documentação do Ponto de Entrada REGK26X](http://tdn.totvs.com/display/PROT/PEST07668_REGK26X_Registros_K260_K265_Bloco_K)*

*[Clique aqui e veja mais artigos sobre Legais/Fiscais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)*
