---
article_id: 34664608748951
category: Gestão de Transportes (TMS)
content_hash: c0c7cd9bb110aac152ee3229b3750c944b4d181fc791f063a13fe0cd2381afd7
fetched_at: '2026-06-28T22:45:32.542820+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Regras de tributação por cliente no Configurador
  de Tributos
type: support-article
updated_at: '2026-03-24T11:34:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34664608748951-Log%C3%ADstica-Linha-Protheus-TMS-Regras-de-tributa%C3%A7%C3%A3o-por-cliente-no-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34664582422679) Tempo aproximado para leitura: **00:01:55 min**  
  
**Dúvida**  
Como utilizar as **Regras de Tributação por Cliente - TMSA600** no **Configurador de Tributos - FISA170**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**  
No **TMS**, existem ocasiões que necessitamos utilizar uma determinada classificação tributária na geração do documento de transporte. Para estas situações especificas, utilizamos o cadastro de **Regras de tributação por cliente - TMSA600** preenchendo os campos **Tipo da NFC - DV1\_TIPNFC** ou **Cod. Prod. - DV1\_CODPRO**, e, a partir dos dados que foram digitados na rotina de **Entrada Documentos de Clientes - TMSA050**, o Sistema realiza a combinação entre **Cod. Produto - DTC\_CODPRO** igual a **Cod. Prod. - DV1\_CODPRO** ou **Tipo Nf Cli. - DTC\_TIPNFC** igual a **Tipo da NFC - DV1\_TIPNFC** para encontrar a **Regra de Tributação** associada ao **TES - Tipos de Entrada e Saída** configurado com a classificação tributaria desejada.  
  
No **Configurador de Tributos - FISA170**, o Sistema não utiliza o **TES** como variável para obter as **Regras de Cálculos**, logo, para atender a esta necessidade, temos os novos campos **TP. Operação - DV1\_OPER** e **TP. Operação - DUG\_OPER** disponíveis nos cadastros de **Regras de tributação por cliente - TMSA600** e **Regras de Tributação - TMSA410.**  
   
Campo **TP. Operação - DV1\_OPER** - **Regras de tributação por cliente - TMSA600:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34672371368343)

Campo **TP. Operação - DUG\_OPER - Regras de Tributação - TMSA410.** Com este campo, temos a possibilidade de criar operações especificas por componentes de fretes ou para determinada TES:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37962987138199)

O campo **TP. Operação** deve ser preenchido conforme o **Tipo de Operação** desejada, e, se necessário, podem ser incluídas novas operações na tabela **SX5**. A operação utilizada neste campo deverá ser informada no cadastro de **Perfil de Operação no Configurador de Tributos - FISA170**, pasta **Tipo de Operação**, campo **Tp. Operação - F26\_TPOPER:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37962987138967)

Caso já existam regras cadastradas no **Configurador de Tributos**, para evitar que o sistema aplique múltiplas regras de cálculo simultaneamente, o que resultaria na duplicidade do imposto, é necessário ajustar o cadastro de **Regras de Tributação por Cliente - TMSA600** ou em **Regras de Tributação - TMSA410**. Para isso, deve-se preencher o campo **Tp. Operação** com uma regra genérica, por exemplo **T1 - ICMS Normal**, e associá-la ao **Perfil de Operação** no **Configurador de Tributos**. Em resumo, para garantir o Sistema não acate diferentes **Regras de Cálculo - Documentos Fiscais** ao mesmo tempo na geração do documento, duplicando o imposto, o Sistema deve estar configurado com **DV1\_OPER ou DUG\_OPER = F26\_TPOPER**.  
  
**Saiba mais**  
Guia para o uso do **Configurador de tributos - FISA170** no **Protheus TMS -** [Logística - Linha Protheus - TMS - Exemplo de uso do Configurador de Tributos no TMS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32213798486167-Log%C3%ADstica-Linha-Protheus-TMS-Exemplo-de-uso-do-Configurador-de-Tributos-no-TMS)
