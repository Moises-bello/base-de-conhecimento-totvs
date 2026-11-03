---
article_id: 12917217142423
category: SIGAEST - LEGAIS
content_hash: 79a8ddd0b9d9ca2fe30f1f06ff60dc7922d5773ba3e30687415bdefab29c9c89
fetched_at: '2026-06-28T22:38:51.881995+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - SPEDFISCAL - Não é
  permitido mesmo tipo de produto em parâmetro MV_BLKTP(*) diferentes
type: support-article
updated_at: '2023-03-13T17:46:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12917217142423-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-SPEDFISCAL-N%C3%A3o-%C3%A9-permitido-mesmo-tipo-de-produto-em-par%C3%A2metro-MV-BLKTP-diferentes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**Ao gerar o SPED Fiscal é gerada a mensagem "Não é permitido mesmo tipo de produto em parâmetro MV\_BLKTP(\*) diferentes"  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**Este problema acontece a partir de uma validação recente do SPED Fiscal.

**Solução**

Para melhor compreensão de como resolver este problema, vamos mostrar abaixo qual é o padrão de Tipagem de Produtos no SPED Fiscal.

**Definições de Tipo de Produto para o Bloco K**

No **Bloco K** são tratados os tipos de produto 00, 01, 02, 03, 04, 05, 06 e 10. Conforme definição da Receita Federal, temos os seguintes conceitos para estes tipos de produtos:

|  |  |  |
| --- | --- | --- |
| **Tipo** | **Descrição** | **Definição** |
| 00 | Mercadoria para Revenda | Produto adquirido para comercialização. |
| 01 | Matéria-Prima | A mercadoria que componha, física e/ou quimicamente, um produto em processo ou produto acabado e que não seja oriunda do processo produtivo. A mercadoria recebida para industrialização é classificada como Tipo 01, pois não decorre do processo produtivo, mesmo que no processo de produção se produza mercadoria similar classificada como Tipo 03. |
| 02 | Embalagem | - |
| 03 | Produto em Processo | O produto que possua as seguintes características, cumulativamente: oriundo do processo produtivo; e, preponderantemente, consumido no processo produtivo. Dentre os produtos em processo está incluído o produto resultante caracterizado como retorno de produção. Um produto em processo é caracterizado como retorno de produção quando é resultante de uma fase de produção e é destinado, rotineira e exclusivamente, a uma fase de produção anterior à qual o mesmo foi gerado. No "retorno de produção", o produto retorna (é consumido) a uma fase de produção anterior à qual ele foi gerado. Isso é uma excepcionalidade, pois o normal é o produto em processo ser consumido em uma fase de produção posterior à qual ele foi gerado, e acontece, portanto, em poucos processos produtivos. |
| 04 | Produto Acabado | O produto que possua as seguintes características, cumulativamente:   * Oriundo do processo produtivo; * Produto final resultante do objeto da atividade econômica do contribuinte; * Pronto para ser comercializado. |
| 05 | Subproduto | O produto que possua as seguintes características, cumulativamente: oriundo do processo produtivo e não é objeto da produção principal do estabelecimento; tem aproveitamento econômico; não se enquadre no conceito de produto em processo (Tipo 03) ou de produto acabado (Tipo 04). |
| 06 | Produto Intermediário | Aquele que, embora não se integrando ao novo produto, for consumido no processo de industrialização. |
| 10 | Outros Insumos | - |

**Tratamento do Tipo de Produto para o Bloco K no Protheus via Parâmetros (SX6)**

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Tipo de produto** | **Tipo Padrão** |
| MV\_BLKTP00 | Mercadoria para Revenda | 'ME' |
| MV\_BLKTP01 | Matéria-Prima | 'MP' |
| MV\_BLKTP02 | Embalagem | 'EM' |
| MV\_BLKTP03 | Produto em Processo | 'PP' |
| MV\_BLKTP04 | Produto Acabado | 'PA' |
| MV\_BLKTP05 | Subproduto | 'SP' |
| MV\_BLKTP06 | Produto Intermediário | 'PI' |
| MV\_BLKTP10 | Outros Insumos | 'OI' |

OBS: No padrão, todos estes parâmetros vem vazios. Mas **quando está vazio**, o *Protheus*assume o tipo definido na coluna **Tipo Padrão**.

**Cenário de Exemplo em que Gera o erro**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/12917163575063)

Neste caso, o erro acontece pois:

- O parâmetro MV\_BLKTP03 é reservado ao Produto em Processo (PP), porém quando o usuário delega o tipo Produto Intermediário (PI) neste parâmetro faz com que conflite com o parâmetro MV\_BLKTP06 (reservado ao PI)

**Possíveis Soluções**

**1° Proposta de solução**

- No parâmetro padrão do tipo PI (MV\_BLKTP06), delegar um outro tipo que não seja default de nenhum dos outros (00 ao 10). Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/12917601843991)

Desta forma, o MV\_BLKTP06 será reservado apenas ao **SV** e os produtos do tipo **PI**serão assumidos como tipo 03 (MV\_BLKTP03)

**2° Proposta de solução**

- No parâmetro que o tipo PI foi passado (MV\_BLKTP03), remover o tipo **PI**. Exemplo:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/12917725583511)**

Desta forma, o MV\_BLKTP03 reservará apenas ao tipo PP e o parâmetro MV\_BLKTP06 vazio ou = 'PI' reservará aos produtos do Tipo **PI**

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Legais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)
