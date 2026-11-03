---
article_id: 360035616693
category: RH - Contabilização
content_hash: db9738c2c59b54b8facf93cdf3caf600cbd0772e2c534655fefb384c70344354
fetched_at: '2026-06-28T22:43:46.027360+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Pontos de Entrada disponíveis na rotina de contabilização
  (GPEM110)
type: support-article
updated_at: '2025-07-28T20:06:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035616693-RH-Linha-Protheus-GPE-Pontos-de-Entrada-dispon%C3%ADveis-na-rotina-de-contabiliza%C3%A7%C3%A3o-GPEM110
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33775960714391)** Tempo aproximado para leitura:**00:01:30 min**

**Dúvida**Quais são os pontos de entrada na rotina de contabilização?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Abaixo, estão listados os pontos de entrada da rotina de contabilização GPEM110:  
  
**GP110VLD**-  Ponto de entrada para consistência adicionais de usuário antes da execução da contabilização;  
[RH - Linha Protheus - GPE - Ponto de Entrada GP110VLD - Consiste a Execução da Contabilização da Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6141780054423-RH-Linha-Protheus-GPE-Ponto-de-Entrada-GP110VLD-Consiste-a-Execu%C3%A7%C3%A3o-da-Contabiliza%C3%A7%C3%A3o-da-Folha-de-Pagamento)  
**GP110ACT**- Há clientes que, para contabilizar todas as filiais em uma, mesmo com o Modo de Acesso do SRZ igual a Exclusivo, alteram o conteúdo do campo RZ\_FILIAL para branco (Simulando um arquivo compartilhado). Para prever essas situações, e, se o ponto de entrada retornar conteúdo correspondente a filial a ser pesquisada e Contabilizada *Array* com dois Elementos. Obs.: Recomendamos o uso da função SRZFilReplace, caso seja necessário estar dando *replace* no campo RZ\_FILIAL. A função deverá ser chamada da seguinte forma: SRZFilReplace( cFilReplace , [ bCondReplace ] );    
[RH - Linha Protheus - GPE - Como utilizar o ponto de entrada GP110ACT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6113330053911-RH-Linha-Protheus-GPE-Como-utilizar-o-ponto-de-entrada-GP110ACT)  
**GP110ANL**- Ponto Entrada após carregar o Numero do Lote contábil;    
**GP110APL**- Alterar parâmetros da geração de lançamentos para o SRZ;  
[RH - Linha Protheus - GPE - RH - Linha Protheus - GPE - Como utilizar o ponto de entrada GP110APL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6278175781399-RH-Linha-Protheus-GPE-RH-Linha-Protheus-GPE-Como-utilizar-o-ponto-de-entrada-GP110APL)  
**GP110APP**- Alterar parâmetros da geração de lançamentos para o SRZ;  
[RH - Linha Protheus - GPE - Como utilizar o ponto de entrada GP110APP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6140879458455-RH-Linha-Protheus-GPE-Como-utilizar-o-ponto-de-entrada-GP110APP)  
**GP110SRZ**- Ponto de Entrada para devolver o conteúdo dos *arrays aTotFunFer|,* a13Salar e a14Sala rateado. O retorno deve ser um *array* tridimensional onde o 1o nível representa a quantidade de rateios efetuada e os dois últimos níveis tem a mesma estrutura;  
[RH - Linha Protheus - GPE - Como utilizar o ponto de entrada GP110SRZ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6176919381399-RH-Linha-Protheus-GPE-Como-utilizar-o-ponto-de-entrada-GP110SRZ)

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Como configurar Lançamento Padrão para Folha de Pagamento do Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021101152-RH-Linha-Protheus-GPE-Como-configurar-Lan%C3%A7amento-Padr%C3%A3o-para-Folha-de-Pagamento-do-Protheus-)
