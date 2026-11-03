---
article_id: 360051275494
category: RH - Leitura e Apontamento
content_hash: 7738a103fc3c201149c91d1213edaf3bb0bbf8dbdb99a9d359d47ab820eb4382
fetched_at: '2026-06-28T22:44:46.035028+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON - Utilização de ExecAuto para realizar Leitura/Apontamento
type: support-article
updated_at: '2025-11-27T13:09:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051275494-RH-Linha-Protheus-PON-Utiliza%C3%A7%C3%A3o-de-ExecAuto-para-realizar-Leitura-Apontamento
---

**Dúvida**  
É possível utilizar ***ExecAuto*** PONM010 para realizar Leitura/Apontamento de Marcações?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
É possível utilizar ***ExecAuto*** da rotina **PONM010** **apenas para geração ou exclusão** de marcações na tabela SP8, porém, não é possível executar o apontamento desta forma.  
Os fontes que tratam do **Apontamento** no Ponto Eletrônico, que são: PONM010, PONA280, PONA040, PONXAPO, PONXFUN e PONCLAPO, **não possuem** ***ExecAuto*** para esta funcionalidade, portanto, recomendamos que seja utilizado um [Schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052033373) para execução automática do Apontamento.  
  
Para utilização do *ExecAuto* na geração ou exclusão de marcações, basta seguir o exemplo [desta documentação.](https://tdn.totvs.com/pages/releaseview.action?pageId=492705908)  
  
  
  
**Saiba mais**  
[ExecAuto - PONM010](https://tdn.totvs.com/pages/releaseview.action?pageId=492705908)  
[RH - Linha Protheus - PON - Como configurar o Schedule de Leitura/Apontamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052033373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)
