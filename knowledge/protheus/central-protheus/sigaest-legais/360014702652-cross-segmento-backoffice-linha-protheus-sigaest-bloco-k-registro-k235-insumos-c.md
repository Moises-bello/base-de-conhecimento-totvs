---
article_id: 360014702652
category: SIGAEST - LEGAIS
content_hash: 4b8fba6c18049f94df23c06f8e13aabd277e8dee47808e8c06bf65bb32aa4051
fetched_at: '2026-06-28T22:38:51.423222+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -  Bloco K - Registro
  K235: Insumos Consumidos (Produção)'
type: support-article
updated_at: '2025-12-22T14:46:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014702652-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Bloco-K-Registro-K235-Insumos-Consumidos-Produ%C3%A7%C3%A3o
---

O Registro K235 do SPED Fiscal apresenta o consumo de insumos no processo produtivo, vinculado ao produto final do Registro K230. Considera movimentos internos de requisições e devoluções com Ordem de Produção no período processado. Recomenda-se controlar o consumo conforme a demanda para ordens trabalhadas em vários períodos, evitando saldo negativo. São considerados produtos dos tipos 00 a 05 e 10.

**Dúvida**  
O que é o Registro K235: Insumos Consumidos (Produção)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

O Registro K235, do Bloco K do SPED FISCAL, apresenta o consumo das mercadorias no processo produtivo, vinculado ao produto resultante (produto final/produto acabado) informado no Registro K230.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Tipo** | **Tam** | **Dec** | **Obrig** |
| 01 | REG | Texto fixo contendo "K235" | C | 4 | - | O |
| 02 | DT\_INI\_OP | Data de saída do estoque para alocação ao produto | N | 8 | - | O |
| 03 | COD\_ITEM | Código do item componente/insumo (campo 02 do Registro 0200) | C | 60 | - | O |
| 04 | QTD | Quantidade consumida do item | N | - | 3 | O |
| 05 | COD\_INS\_SUBST | Código do insumo que foi substituído, caso ocorra a substituição (campo 02 do Registro 0210) | C | 60 | - | OC |

Para a montagem deste registro, são considerados os movimentos internos (SD3) de requisições e devoluções que possuam uma Ordem de Produção informada no campo D3\_OP preenchido, e que tenham sido geradas dentro do período que será processado pelo **Bloco K**. Os dados gravados neste registro referem-se aos componentes consumidos no processo produtivo.

No sistema, o consumo de componentes é realizado através de requisições via movimentos internos. Como o sistema possui o conceito de devolução de consumo, o processamento do registro K235 leva em consideração uma composição entre requisições e devoluções para obter o consumo do período.

## **Como ter um controle do Registro K235 quando a minha empresa trabalha com Ordem de Produção durante vários períodos?**

Existem situações onde o cliente possui uma Ordem de Produção em que é trabalhada durante vários períodos (meses), por exemplo:

Período A - requisição para produção (Exemplo: 100 unidades)

Período B - devolução (Exemplo: 30 unidades)

O registro K235 apresentara uma quantidade negativa devido a composição "requisições - devoluções". Quando o registro K235 apresentar quantidade negativa (O registro será direcionado ao [Registro K275: Correção de Apontamento e Retorno de Insumos](http://tdn.totvs.com/pages/viewpage.action?pageId=259560530) **com** **o saldo negativo** para correção da quantidade consumida do insumo durante o processo produtivo).  **Desta forma, recomendamos que, em processos produtivos com Ordens de Produções que são trabalhadas durante vários períodos (meses), o consumo seja realizado conforme a demanda.** Ordens de Produção geradas pelo módulo de Manutenção de Ativos (SIGAMNT) não são consideradas neste registro.

**Tipos de Produtos considerados:**

00, 01, 02, 03, 04, 05 e 10 ([Veja neste artigo a tabela dos Tipos de Produtos considerados no Bloco K)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033136554-MP-SIGAEST-Como-definir-um-tipo-de-produto-que-n%C3%A3o-seja-padr%C3%A3o-do-sistema-para-que-seja-considerado-no-Bloco-K200-)

**Rotinas envolvidas:**

MATA240 – Movimentos Internos  
MATA241 – Movimentos Internos Modelo II  
MATA250 – Apontamento de Produção

**Tabelas envolvidas:**

SD3 – Movimentações Internas  
SGI – Produtos Alternativos

**Saiba mais:**

[*MP - SIGAEST - Como o Protheus gera no SPED o Registro K200: Estoque Escriturado?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019502091-MP-SIGAEST-Como-o-Protheus-gera-no-SPED-o-Registro-K200-Estoque-Escriturado-)

[*MP - SIGAEST - Processo para geração do registro K270*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022630231-MP-SIGAEST-Processo-para-gera%C3%A7%C3%A3o-do-registro-K270)

[*Clique aqui e veja outros artigos sobre Legais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)
