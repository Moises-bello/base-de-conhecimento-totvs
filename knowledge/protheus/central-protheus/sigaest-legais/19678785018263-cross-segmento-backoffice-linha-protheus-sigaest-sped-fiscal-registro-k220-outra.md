---
article_id: 19678785018263
category: SIGAEST - LEGAIS
content_hash: 31835b56b10882ef085eef034f3eb6e1e3b9a4b67cd01f6a913da45747557c0a
fetched_at: '2026-06-28T22:38:51.855303+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - SPED FISCAL - Registro
  K220: Outras Movimentações Internas entre Mercadorias'
type: support-article
updated_at: '2023-12-08T20:23:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19678785018263-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-SPED-FISCAL-Registro-K220-Outras-Movimenta%C3%A7%C3%B5es-Internas-entre-Mercadorias
---

**Introdução**

O registro K220 apresenta as movimentações internas entre mercadorias. Este registro é usado para tratar quaisquer outras movimentações que não se enquadrem nos demais tipos de registro.

Importante: Quando falamos em Movimentação interna no bloco K, o conceito é diferente das Movimentações internas do Protheus (Movimentação simples [MATA240] e Movimentação múltipla [MATA241]).

Para a montagem deste registro, são consideradas todas as transferências realizadas através das rotinas Transferência Simples (MATA260) e Transferência Múltipla (MATA261), cujos os produtos de Origem e Destino sejam diferentes.

**Fluxo do processo**

![](https://tdn.totvs.com/download/attachments/259560142/image2018-10-30_18-52-0.png?version=1&modificationDate=1540939924403&api=v2)

**Leiaute no Guia Prático EFD-ICMS/IPI**

Este registro contém as informações de movimentações internas entre mercadorias que não se enquadram nos demais registros.

Neste registro são demonstradas as transferências de produtos com a finalidade de troca entre códigos de produtos.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Tipo** | **Tam** | **Dec** | **Obrig** |
| 01 | REG | Texto fixo contendo "K220" | C | 4 | - | O |
| 02 | DT\_MOV | Data da movimentação interna | N | 8 | - | O |
| 03 | COD\_ITEM\_ORI | Código do item de origem (campo 02 do Registro 0200) | C | 60 | - | O |
| 04 | COD\_ITEM\_DEST | Código do item de destino(campo 02 do Registro 0200) | C | 60 | - | O |
| 05 | QTD\_ORI | Quantidade movimentada do item de Origem | N | - | 6 | O |
| 06 | QTD\_DEST | Quantidade movimentada do item de destino | N | - | 6 | O |

Importante: a quantidade gravada no campo QTD do **Bloco K,** será sempre a quantidade do produto de origem.

#### Tipos de Produtos considerados

00, 01, 02, 03, 04, 05 e 10.

#### Rotinas envolvidas

MATA260 – Transferência de Produtos  
MATA261 – Transferência de Produtos Modelo II

#### Tabelas envolvidas

SD3 – Movimentações Internas

**Exemplo prático do processo utilizando o Protheus**

1. Cadastrar local de estoque
   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Atualizações > Cadastros > Produtos > Locais de estoque
   3. Clique Incluir
   4. Informe os campos obrigatórios  
        
      ![](https://tdn.totvs.com/download/attachments/259560142/image2018-10-30_10-26-2.png?version=1&modificationDate=1540948155653&api=v2)
2. Cadastrar produto
   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Atualizações > Cadastros > Produtos >Produto
   3. Clique Incluir
   4. Informe os campos obrigatórios  
      ![](https://tdn.totvs.com/download/attachments/259560142/image2018-10-30_21-12-43.png?version=1&modificationDate=1540948363210&api=v2)  
        
      ![](https://tdn.totvs.com/download/attachments/259560142/image2018-10-30_21-13-34.png?version=1&modificationDate=1540948415013&api=v2)
3. Cadastrar saldo inicial
   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Atualizações > Saldos > Inicial
   3. Clique Incluir
   4. Informe os campos obrigatórios, Qtd. Inic. Mes e Sld. Ini. Mes  
      ![](https://tdn.totvs.com/download/attachments/259560142/image2018-10-30_21-14-59.png?version=1&modificationDate=1540948499813&api=v2)  
        
      ![](https://tdn.totvs.com/download/attachments/259560142/image2018-10-30_21-15-35.png?version=1&modificationDate=1540948535883&api=v2)
4. Cadastrar Transferência Simples
   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Atualizações > Movimentações> Internas > Transferência Simples
   3. Clique Incluir
   4. Informe os campos obrigatórios, Quantidade Primária  
      ![](https://tdn.totvs.com/download/attachments/259560142/image2018-10-30_21-23-50.png?version=1&modificationDate=1540949030953&api=v2)
5. Emitir relatório relação bloco K
   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Relatórios > Legais > Relação Bloco K
   3. Clique Outras Ações
   4. Clique Parâmetros
   5. Revise os parâmetros
   6. Clique Imprimir  
      Serão apresentados os saldos dos produtos origem e destino no registro K220

      ![](https://tdn.totvs.com/download/attachments/259560142/image2018-10-30_21-27-6.png?version=1&modificationDate=1540949226433&api=v2)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Legais/Fiscais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)
