---
article_id: 360006892612
category: Materiais - Compras (SIGACOM)
content_hash: 2ffe11bfa8badca0b3959d4b9a6fce37aa7d3dae00e1238942942e9b2b9ea005
fetched_at: '2026-06-28T22:41:07.530958+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como aglutinar produtos
  na cotação com Entidades Contábeis Diferentes ( MV_COTRATP )?
type: support-article
updated_at: '2026-02-24T19:52:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006892612-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-aglutinar-produtos-na-cota%C3%A7%C3%A3o-com-Entidades-Cont%C3%A1beis-Diferentes-MV-COTRATP
---

**Dúvida**

Como aglutinar produtos na cotação com Entidades Contábeis Diferentes (MV\_COTRATP)?

**Ambiente**

Protheus – Compras – A partir da versão 11.80

**Solução**

Com o objetivo de propiciar maior ganho de escala e assim reduzir os custos de compras das empresas, garantindo melhor margem de lucro, o programa Gera Cotação **(MATA131)** foi alterado e passa a processar a aglutinação de produtos solicitados em diferentes itens de Solicitação de Compra e de Entidades Contábeis em um único item de cotação.

Passa a valer este tratamento ao configurar o parâmetro **MV\_COTRATP** habilitado com o conteúdo (T).

Isto feito os itens de Pedido de Compra gerados a partir de Processos de Cotação que aglutinaram itens de diferentes Entidades Contábeis passa a gerar, de forma automática, Rateio Contábil (tabela SCH) com percentuais conforme as quantidades determinadas nas Solicitações de Compra de origem.

**MV\_COTRATP** = Indica se aglutina itens com entidades contábeis diferentes na cotação e gera rateio contábil no item do pedido de compra. (T=Sim; F=Não).

**Detalhes sobre a aglutinação da Cotação**

Campos que diferenciam os itens de uma Solicitação de Compras para mesmo código de produto, para que não aglutinem quando é efetuado a geração da Cotação:

**C1\_FILIAL+C1\_GRADE+C1\_FORNECE+C1\_LOJA+C1\_PRODUTO+C1\_DESCRI+DTOS(C1\_DATPRF)+C1\_CC+C1\_CONTA+C1\_ITEMCTA+C1\_CLVL+C1\_FILENT**

Caso necessário algum tratamento via ponto de entrada para atender algo específico da empresa, abaixo constam os Pontos de Entrada disponíveis no processo:

***PEs disponiveis do processo:***

**MA131KEY**   
<https://tdn.totvs.com/display/public/PROT/TTYQWE_DT_PONTO_DE_ENTRADA_MA131KEY>

**MA131QSC**   
<https://tdn.totvs.com/display/public/PROT/TUCB70_DT_PONTO_DE_ENTRADA_MA131QSC>

***Obs*****:**

No Novo Fluxo de Compras NFC atualmente não existe nenhuma possibilidade de não aglutinar os itens da solicitação ao gerar a cotação. Sendo assim, quando houver mais de uma solicitação possuindo produtos iguais, com a mesma Data de necessidade, conta contábil, entre outras similaridades, haverá um agrupamento de solicitações. Surgindo então na tela um campo chamado **Solicitações agrupadas**. Nele o usuário conseguirá visualizar através de um disclaimer azul, o número da Solicitação e o número do item, apresentada nesse mesma ordem **Solicitação-Item**, somando as quantidades solicitadas à quantidade total.

![](https://tdn.totvs.com.br/download/attachments/680260500/SC%20agrupada.png?version=1&modificationDate=1712772084363&api=v2)

***Saiba Mais :***

[MP - SIGACOM - MATA161 Auditoria da Cotação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022836692-MP-SIGACOM-MATA161-Auditoria-da-Cota%C3%A7%C3%A3o?source=search)

[MP - SIGACOM - Análise de Cotação por fator](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023025352-MP-SIGACOM-An%C3%A1lise-de-Cota%C3%A7%C3%A3o-por-fator?source=search)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
