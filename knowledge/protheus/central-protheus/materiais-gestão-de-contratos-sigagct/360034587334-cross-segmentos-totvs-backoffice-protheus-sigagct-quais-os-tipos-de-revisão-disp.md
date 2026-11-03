---
article_id: 360034587334
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 02bcfdf8a95bfa2448419731c04e51382b3c3a8e4c901ad13874e32d5232b156
fetched_at: '2026-06-28T22:37:24.067613+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quais os tipos de Revisão
  disponíveis no Gestão de Contratos ?
type: support-article
updated_at: '2026-05-11T20:02:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034587334-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Quais-os-tipos-de-Revis%C3%A3o-dispon%C3%ADveis-no-Gest%C3%A3o-de-Contratos
---

**Dúvida**

Quais são os tipos de Revisão disponíveis, para revisar contratos no Gestão de Contratos ?  
  
**Ambiente**  
  
Protheus – Gestão de Contrato – A partir da versão 11.80  
  
**Solução**

O tipo de revisão de contratos é o cadastro que servirá de base para o sistema identificar qual a revisão que está sendo processada para o contrato e quais tratamentos deverão ser aplicados durante o processo de revisão.

Estão disponíveis em *Gestão de Contratos (69) > Atualizações > Cadastros > Tipos > Revisões* (***CNTA010***) os seguintes tipos de revisão:

![a2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360102460473)

Abaixo segue descritivo com os principais tipo e demais no link da documentação disponível ao final:

**»** **Aditivo**: revisão para edição das planilhas do contrato através da adição/subtração de quantidades ou até mesmo itens. Também pode ser utilizada para ajustes no plano de execução do contrato através da adição/remoção de parcelas nos cronogramas. Após o ajuste das planilhas, os cronogramas do contrato deverão ser reajustados de acordo com os novos valores da planilha.

**»** **Reajuste**: revisão do contrato para reajuste dos valores dos itens das planilhas conforme variação do índice econômico associado ao contrato.

**»** **Realinhamento**: revisão do contrato para ajuste nos preços dos itens da planilha, conforme algum acordo realizado entre as partes do contrato. Após o ajuste das planilhas, os cronogramas do contrato deverão ser reajustados manualmente de acordo com os novos valores da planilha.

**»** **Readequação**: revisão do contrato para ajuste nas quantidades dos itens da planilha, desde que o montante total do contrato em valor não seja alterado.

**» Paralisação**: revisão para pausa na execução do contrato, evitando assim que o contrato seja movimentado indevidamente no período de paralisação.

**» Reinício**: revisão para reinício da execução de um contrato em paralisação. No reinício será possível editar os cronogramas para ajustes dos prazos conforme nova programação de execução.

**» Alteração de cláusulas:** revisão para ajuste nas cláusulas de um contrato.

**» Contábil**: revisão para edição dos cronogramas contábeis de um contrato, permitindo a manutenção completa destas entidades.

**»** **Índice:**revisão para troca do índice econômico associado a um contrato.

**»** **Troca de Fornecedor**: revisão para troca (substituição) de um fornecedor participante de um contrato. Este tipo de revisão é específico para contratos de compra.  
Cada tipo de revisão atende a uma determinada necessidade de revisão de contratos e não permitirá a realização de outras ações que não sejam as previstas pelo tipo de revisão. Exemplo: em uma revisão de aditivo não poderão ser alterados preços de itens da planilha.

**» Grupo de Aprovação:**Essa funcionalidade permite que as aprovações das revisões de contrato, que antes não eram submetidas ao controle por alçadas, sejam verificadas pelos grupos de aprovadores designados seguindo o fluxo de aprovação definido pelo cliente, tornando o processo mais seguro e confiável.

Ao gerar um contrato é possível informar individualmente o Grupo de Aprovação responsável por ele de acordo com cada necessidade. Desta forma, ele pode ser aprovado por completo e seus documentos gerados ficam disponíveis na rotina de Liberação de Documentos para o novo grupo.

***Obs:*** Ao alterar um Grupo de Aprovação do contrato, a alçada ficará pendente para o aprovador **antigo, a partir desta aprovação, as próximas alçadas serão consideradas para o novo aprovador.**

**» Caução:**Para que no cadastro do tipo de revisão (***CN0\_TIPO***), apresente o tipo caução somente se o parâmetro **MV\_CNRVCAU** estiver ativo.

**» Aberta:**Visando simplificar o processo de revisões, foi criada a revisão Aberta. Nela pode-se fazer todas as operações que as outras revisões fazem em uma única revisão.

**Obs1:** Os tipos: **Grupo de aprovação** e **Caução** são válidos para a versão P12.

**Obs2:**

Caso ocorra o Help **CNTA300ND** ao Deletar Itens(Não medidos) do contrato em Revisões consulte o artigo a seguir [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help CNTA300ND ao Deletar Itens(Não medidos) do contrato em Revisões?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28442693078807-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-CNTA300ND-ao-Deletar-Itens-N%C3%A3o-medidos-do-contrato-em-Revis%C3%B5es)

**Obs3:**

Existe a possibilidade de alterar o fornecedor de um contrato?

**R:**Sim através da Revisão "**Tipo A**", , poderá ser utilizado tanto para troca/inclusão de fornecedor quanto para cliente. Veja as orientações de configuração no artigo a seguir:[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar a Revisão de troca ou inclusão de um novo Cliente ou Fornecedor ao contrato ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020510472-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-a-Revis%C3%A3o-de-troca-ou-inclus%C3%A3o-de-um-novo-Cliente-ou-Fornecedor-ao-contrato)

Verificar as documentações complementares as reviões em ***"Saiba Mais"***.

***Saiba Mais:***

[Tipos de Revisões de Contrato - CNTA010 - Gestão de Contratos - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=224447795)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help CNTA300ND ao Deletar Itens(Não medidos) do contrato em Revisões?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28442693078807-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-CNTA300ND-ao-Deletar-Itens-N%C3%A3o-medidos-do-contrato-em-Revis%C3%B5es)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Revisão de Renovação de Contrato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025659713-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Revis%C3%A3o-de-Renova%C3%A7%C3%A3o-de-Contrato)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar a Revisão de Índices de um Contrato ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035192133-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-a-Revis%C3%A3o-de-%C3%8Dndices-de-um-Contrato)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar uma Revisão Contábil em contratos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028517152-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-uma-Revis%C3%A3o-Cont%C3%A1bil-em-contratos)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como Realizar a Revisão para Troca do Grupo de Aprovação em um Contrato?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13050849291799-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-Realizar-a-Revis%C3%A3o-para-Troca-do-Grupo-de-Aprova%C3%A7%C3%A3o-em-um-Contrato)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Revisão de Realinhamento para alterar os Valores Unitários dos itens do Contrato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021218171-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Revis%C3%A3o-de-Realinhamento-para-alterar-os-Valores-Unit%C3%A1rios-dos-itens-do-Contrato)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como aumentar ou reduzir os meses e redistribuição das parcelas de um contrato na Revisão de Aditivo ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028039532-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-aumentar-ou-reduzir-os-meses-e-redistribui%C3%A7%C3%A3o-das-parcelas-de-um-contrato-na-Revis%C3%A3o-de-Aditivo)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quais as funções das opções de Arrasto e Redistribuição de Saldos na Aba Parâmetros/Revisão na realização de uma Revisão ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036469613-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Quais-as-fun%C3%A7%C3%B5es-das-op%C3%A7%C3%B5es-de-Arrasto-e-Redistribui%C3%A7%C3%A3o-de-Saldos-na-Aba-Par%C3%A2metros-Revis%C3%A3o-na-realiza%C3%A7%C3%A3o-de-uma-Revis%C3%A3o)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar a Revisão de troca ou inclusão de um novo Cliente ou Fornecedor ao contrato ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020510472-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-a-Revis%C3%A3o-de-troca-ou-inclus%C3%A3o-de-um-novo-Cliente-ou-Fornecedor-ao-contrato)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
