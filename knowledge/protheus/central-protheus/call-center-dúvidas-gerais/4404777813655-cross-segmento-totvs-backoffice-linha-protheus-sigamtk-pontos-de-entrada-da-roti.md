---
article_id: 4404777813655
category: Call Center - Dúvidas Gerais
content_hash: 37665089093d95997facd88257557a7e5b2ea16cadf5e2b849daf3ff812ffb6d
fetched_at: '2026-06-28T22:41:26.576577+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAMTK - Pontos de entrada
  da rotina de Suspects
type: support-article
updated_at: '2023-06-15T12:25:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404777813655-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAMTK-Pontos-de-entrada-da-rotina-de-Suspects
---

**Dúvida**Quais são os pontos de entradas existentes na rotina Cadastro de Suspects (**TMKA341**)?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAMTK - Todas as versões.  
  
**Solução**

**- CRMBRWVIEW** - Substituição das Visões Padrão do CRM - **<https://tdn.totvs.com/x/NT6WDg>**

**- TKDELACH** - Exclusão de ponto de entrada, executado antes da gravação da exclusão do ponto de entrada. O retorno do ponto de entrada, fará com que o processo de gravação continue (caso seja .T.) ou pare (caso seja .F.) - **<https://tdn.totvs.com/x/spJn>**

**- TKALTACH** - Alteração do ponto de entrada, executado antes da gravação da alteração do ponto de entrada. O retorno do ponto de entrada, fará com que o processo de gravação continue (caso seja .T.) ou pare (caso seja .F.) - **<https://tdn.totvs.com/x/sJJn>**

**- TK341LEG** - Alteração de cores da legenda - **<https://tdn.totvs.com/x/ppJn>**

**- TK341GPROS** - Conversão de Suspect em Prospect, executado antes da gravação da conversão do Suspect para o Prospect. O objetivo é permitir a gravação de campos adicionais - **<https://tdn.totvs.com/x/pJJn>**

**- TK341OPG** - Permite o Controle Sobre a Geração de Oportunidade Rápida, utilizado para implementação de validações sobre a geração de oportunidade na qualificação de um **Suspect** -**<https://tdn.totvs.com/x/NQqOIQ>**

**- TK341OPT** - Permite a Manipulação do Modelo de Dados que Compõe a Oportunidade Rápida, deve ser utilizado para manipulação dos dados a serem gravados  na oportunidade quando esta for gerada na qualificação de um **Suspect** - **<https://tdn.totvs.com/x/QQ_OIQ>**

**- TK341GRV** - Gravação do suspect - **<https://tdn.totvs.com/x/pZJn>**

**- TK341BUT** - Inclusão de botões na enchoice do cadastro de suspects - **<https://tdn.totvs.com/x/o5Jn>**

**- TK341ROT** - Inclusão de novas rotinas no menu - **<https://tdn.totvs.com/x/3dfSKQ>**

**- TK341FIL** - Filtra o browse do Cadastro de Suspects - **<https://tdn.totvs.com/x/_t-SKQ>**

**- TMKGRSP** - Execução de comandos - **<https://tdn.totvs.com/x/yJJn>**

**- TK341MEMO** - Ponto de Entrada para capturar os campos memo do usuário para serem atualizados no cadastro de suspects **-** (não localizada documentação no TDN)

**- TMKINCACH** - Ponto de Entrada depois da inclusão do contato - (não localizada documentação no TDN)

**- TMKSUSP** - Ponto de Entrada antes da gravação de Suspect para Prospect - (não localizada documentação no TDN)

**Saiba Mais**

**[Pontos de Entrada - Call Center - P12](https://tdn.totvs.com/x/r52pHg)**
