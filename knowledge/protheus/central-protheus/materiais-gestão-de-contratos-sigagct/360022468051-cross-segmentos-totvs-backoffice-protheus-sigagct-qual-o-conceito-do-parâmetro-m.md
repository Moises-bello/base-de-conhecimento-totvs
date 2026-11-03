---
article_id: 360022468051
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 15d794dc4aee3d72c8f1341a705a8894d2ae0ca1de0c87d7eee1335191493d3b
fetched_at: '2026-06-28T22:37:20.149962+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Qual o conceito do
  parâmetro MV_CNREVMD - Criação de Registro de Revisão para Medições Existentes ?
type: support-article
updated_at: '2026-06-03T17:07:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022468051-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Qual-o-conceito-do-par%C3%A2metro-MV-CNREVMD-Cria%C3%A7%C3%A3o-de-Registro-de-Revis%C3%A3o-para-Medi%C3%A7%C3%B5es-Existentes
---

**Dúvida**  
Qual o conceito do parâmetro **MV\_CNREVMD** - Revisão para Medições ?  
  
**Ambiente**  
Gestão de Contratos – Compras – A partir da versão 11.80  
  
**Solução**  
**MV\_CNREVMD** - Indica se devem ser geradas revisões para as medições já encerradas quando um contrato sofrer revisão. (T=Sim; F=Não)

Quando este parâmetro estiver ativado serão gerados registros das medições existentes anteriormente para a Revisão que esta sendo criada, sendo mantido o campo ***CND\_REVGER*** com a revisão em que esta medição foi gerada originalmente, ou seja, é criado automaticamente registro de revisão para as medições ja existentes.

***Obs1:***

Caso o parâmetro ***MV\_CNREVMD*** esteja ativado e ao realizar uma revisão seja gerado um novo registro de uma medição da revisão anterior para esta nova revisão, esta medição para o contrato feita originalmente na revisão anterior pode ser estornada desde que, ao utilizar a opção "Estornar",  seja posicionado no registro novo criado para a revisão atual do contrato (campo ***CND\_REVISA = Revisão atual do Contrato***). E assim será estornado o status deste registro de medição da revisão atual do contrato.

***Obs2:***

Caso o parâmetro ***MV\_CNREVMD*** esteja desativado no momento da revisão do contrato, não são gerados registros de revisão de medições feitas anteriormente ao se fazer a revisão do contrato, o sistema apenas migra as medições já encerradas para a nova revisão, gerada pelo processo de revisão de contrato. E assim para se estornar essa medição, a possibilidade é somente se forem estornadas as revisões realizadas no contrato até chegar na revisão em que a medição foi feita, e assim fazer o estorno da medição com o contrato estando nessa mesma revisão da medição.

***Saiba Mais:***

[Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
