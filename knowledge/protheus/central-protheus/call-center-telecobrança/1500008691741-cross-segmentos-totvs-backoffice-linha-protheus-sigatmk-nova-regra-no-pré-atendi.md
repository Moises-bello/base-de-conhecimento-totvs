---
article_id: 1500008691741
category: Call Center - Telecobrança
content_hash: 1865ff019261817980fa99a6c9c75aca7190a4f1bf81cc5402951ea71db6829d
fetched_at: '2026-06-28T22:41:28.666310+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- Nova Regra no Pré-atendimento
type: support-article
updated_at: '2022-06-22T17:31:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008691741-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Nova-Regra-no-Pr%C3%A9-atendimento
---

**Dúvida**

Configuração para Nova Regra no Pré-Atendimento.

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- a partir da versão 12.  
  
**Solução**

Criada uma nova forma de busca e seleção dos Clientes para a realização da renegociação da cobrança dos seus títulos.

Com essa nova forma de tratar a renegociação dos títulos, o ambiente poderá ser configurado para que seja tratado o período (em horas) em que um operador poderá ligar para o Cliente e realizar a cobrança/renegociação dos seus Títulos. 

Para que essa nova regra de cobrança seja considerada no ambiente, realize os seguintes passos:

1. Valide se as rotinas :

**TMKA274** - **TMKA280** - **TMKA280X** estão atualizadas com a data de **08/03/2021**, caso não esteja, efetue o download do pacote : **<https://suporte.totvs.com/portal/p/10098/download?e=1010905>**

2. Criação dos Parâmetros :

**MV\_NEWTCOB :** Habilita/Desabilita Nova Regra de Telecobrança.

**MV\_TSITCOB :** Situação dos Títulos para serem Utilizados na Nova Regra de Telecobrança.

3. Criação dos Campos :

**CAMPOS** : **K1\_DTFRENE e K1\_HRFRENE, U0\_TEMPCOB**

Detalhes desse assunto em : **<https://tdn.totvs.com/x/KBU0Iw>**
