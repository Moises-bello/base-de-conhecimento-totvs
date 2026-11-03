---
article_id: 1500002994501
category: SIGAEST - FECHAMENTO DE ESTOQUE (VIRADA DOS SALDOS)
content_hash: f89ce9755f652ccea06202cba7d628edb017457223c4ae2cc81bef49d360aa7a
fetched_at: '2026-06-28T22:38:52.690590+00:00'
product: protheus
section_id: 1500001538921
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -  Quais os possíveis
  impactos da Reabertura de Estoque?
type: support-article
updated_at: '2025-03-12T12:23:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002994501-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Quais-os-poss%C3%ADveis-impactos-da-Reabertura-de-Estoque
---

**Dúvida**Quais os impactos de se fazer a reabertura de estoque?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - **12.1.27** **ou anterior**

**Solução**

Atualmente não existe um programa padrão para reabertura de estoque, porém existem usuários que realizam tal processo eliminando os registros da tabela **SB9** e ajustando o parâmetro **MV\_ULMES** com a data do período anterior.

#### **Não recomendamos a realização deste processo, pois não é um processo padrão do sistema, porém quando não existe alternativa, o cliente deve acionar, via Executivo de Soluções de Negócio TOTVS, a solicitação de alocação de analista de campo especialista em Estoque/Custos para acompanhamento do processo de reabertura de estoque localmente na empresa.**

|  |
| --- |
| **Caso a empresa utilize a Release 12.1.33 e tenha a configuração da nova [Jornada de Fechamento](https://tdn.totvs.com/display/PROT/Acompanha+Custos), é possível reabrir o Estoque. Veja no artigo abaixo os detalhes:**  **[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA038 - Processo de Reabertura de Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6420543172247)** |

Nesta documentação serão abordadas situações de impacto no processo de reabertura de estoque:

* Não se deve reabrir fechamentos de estoque quando em sua base de dados existem ordens de produção (Tabela **SC2**) que possuem movimentação de requisição/devolução de estoque contra OP entre os períodos de fechamento de estoque. Pois esta ação irá prejudicar o controle de custos destes produtos desestabilizando seus valores.

Veja o exemplo:

**Período Janeiro/2015**

**Movimentos de estoque**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Data** | **Movimento** | **Produto** | **Quantidade** | **Custo** |
| 05/01/15 | Abertura de Ordem de Produção 00000101001 | PA | 150 peças | Não tem |
| 06/01/15 | Requisição Contra OP | MP | 100 peças | 100,00 |
| 07/01/15 | Requisição Contra OP | MP | 50 peças | 50,00 |

**Fechamento de Estoque**

**Recalculo** **do** **Custo** **Médio** (**MATA330**)

A rotina de Custo Médio prepara o saldo que está em processo (no exemplo acima 150,00 – duas requisições) da seguinte forma:

* SC2->C2\_VFIM1 = SC2->C2\_VINI1 + Movimentações internas (Requisição/Devolução) contra produção para esta ordem de produção.

No nosso exemplo ficara:

* SC2->C2\_VINI1 = 0 (Pois a OP foi aberta neste mês)

Total de Requisições = 150,00

* Resultado SC2->C2\_VFIM1 = 150,00

 

**Virada de Saldos (MATA280)**

A rotina de virada de saldos prepara o saldo da tabela **SC2** para o próximo período da seguinte forma:

SC2->C2\_VINI1 = Saldo em processo do período anterior

SC2->C2\_VINI1 = SC2->C2\_VFIM1, ou seja SC2->C2\_VINI1 = 150,00 para o próximo período.

**Problema ao reabrir o período já fechado**

Ao realizar o procedimento de reabertura de estoque, o cliente que possui Ordens de Produção que são utilizadas em dois ou mais fechamentos e não se atentam ao controle de saldos da tabela **SC2,** pode-se ocorrer o problema abaixo:

* Nova execução da rotina de **Recalculo do Custo Médio** (**MATA330**);
* A rotina de custo médio prepara o saldo que está em processo (no exemplo acima 150,00 – duas requisições) da seguinte forma:

SC2->C2\_VFIM1 = SC2->C2\_INI1 + Movimentações internas (Requisição/Devolução) contra produção para esta ordem de produção.

No nosso exemplo ficara:

SC2->C2\_VINI1 = 150,00 (***Pois ao reabrir o estoque o cliente não conhece a estrutura de nossas tabelas e não tem o controle do campo C2\_VINI1 do período anterior***)

Total de Requisições = 150,00

Resultado SC2->C2\_VFIM1 = 300,00 (aqui esta o impacto na reabertura de estoque, onde o custo ficará incorreto e será repassado para os apontamentos de produção).

Por este motivo não é recomendado pela TOTVS reabrir períodos nesta situação. É recomendável a solicitação de um analista in loco (localmente) para avaliação do ambiente e acompanhamento do processo de reabertura de períodos quando necessário, o suporte padrão não atua com esse tipo de processo, pois é necessário analise em todo ambiente, incluído a base de dados.

**Saiba mais:**

[*MP - SIGAEST - Roteiro para fechamento dos estoques*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048372754-MP-SIGAEST-Roteiro-para-fechamento-dos-estoques)

*[Clique aqui e veja mais artigos sobre Fechamento de Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012208793-SIGAEST-FECHAMENTO-DE-ESTOQUE-VIRADA-DOS-SALDOS-)*
