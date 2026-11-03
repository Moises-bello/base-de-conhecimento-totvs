---
article_id: 35699782630295
category: Financeiro
content_hash: b0699fdc74c69e8bdefe07c52087f2548b6e9c4516f1e762e3dc6fa9e88e8102
fetched_at: '2026-06-28T22:38:03.445238+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - SIGAFIN - FINA050 -
  Como é gravado a base de cálculo de um imposto, quando sua base de cálculo foi alterada.
  E2_BASEIRF
type: support-article
updated_at: '2025-10-17T13:05:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35699782630295-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-SIGAFIN-FINA050-Como-%C3%A9-gravado-a-base-de-c%C3%A1lculo-de-um-imposto-quando-sua-base-de-c%C3%A1lculo-foi-alterada-E2-BASEIRF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35699811183639) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA050 - Como é gravado a base de cálculo de um imposto, quando sua base de cálculo foi alterada. E2\_BASEIRF  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução:**

A base de cálculo do imposto sempre será gravada referente ao valor **original do título**, mesmo que a base de cálculo tenha sido alterada.

Exemplo do campo E2\_BASEIRF.

Hoje é possível alterar a base de um determinado imposto através de pontos de entradas ou parametrizações do sistema.  
Temos  o ponto de entrada "[F50CIRFF - Ponto de entrada para manipulação da base de cálculo do IRRF](https://tdn.totvs.com/pages/releaseview.action?pageId=689057140)" que altera a base de cálculo do imposto IRPF

E também temos parametrizações no sistema para alterar a base de cálculo de um imposto. Exemplo: "MV\_INSIRF - Define se o valor do INSS deve ser abatido da base de cálculo do IRRF no Financeiro. 1=Abate o valor  2=Não abate"

Neste KCS iremos dar alguns exemplo de como seria o cálculo do imposto após alteração de base, e como iria ser gravação e gerado o imposto no campo E2\_IRRF, e suas gravação da base no campo E2\_BASEIRF e etc..

**1.** Inclusão de um título no contas a pagar no valor de R$ 5.500,00 (valor original do título)

Cenário: Parametrizado para gerar o IRPF (pessoa física) na emissão (sem utilização do ponto de entrada e sem parametrização de alteração de base de cálculo)

Utilizando a tabela de IRPF progressiva do ano de 2025, o valor do imposto será gravado no campo

E2\_IRRF =  R$ 603,77 (será gerado um título do tipo TX)

E2\_BASEIRF= R$ 5.500,00 

Cálculo do IRPF

Segue um trecho da informações da tabela progressiva 2025 a ser utilizada no cálculo

|  |  |  |
| --- | --- | --- |
| Valor da Tabela Progressiva | Alíquota | Valor a Deduzir |
| R$ 999.999.999,99 | 27,5% | R$ 908,73 |

 R$ 5.500,00 \*  27,5%  =  R$ 1.512,50

 R$ 1.512,50  - R$ 908,73 =  **R$ 603,77  E2\_IRRF**

**2**. Inclusão de um título no contas a pagar no valor de R$ 5.500,00  (valor original do título)

Cenário: Parametrizado para gerar o IRPF (pessoa física) na emissão

Parametrizado para gerar INSS na emissão com 11% de alíquota

MV\_INSIRF = 1 Abate da base de cálculo do IRRF no Financeiro

Utilizando a tabela de IRPF progressiva do ano de 2025, o valor do imposto será gravado no campo

E2\_IRRF =  R$ 437,40  (será gerado um título do tipo TX)

E2\_INSS = R$ 605,00 (será gerado um título do tipo INS)  
**E2\_BASEIRF= R$ 5.500,00  (Observação:** A base do imposto sempre será gravada referente ao valor original do título**)**

E2\_BASEINS = R$ 5.500,00

Cálculo do INSS

R$ 5.500,00 \*  11%  =   **R$ 605,00  E2\_INSS**

Cálculo do IRPF

R$ 5.500,00 - R$ 605,00 =  R$ 4.895,00

 R$ 4.895,00  \*  27,5%  =   R$ 1.346,13

R$ 1.346,13  - R$ 908,73 =   **R$ 437,40  E2\_IRRF**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/35699782604951)**

A base de cálculo apresentada em tela referente ao campo **E2\_BASEIRF,** não será R$ 4.895,00 , e sim do valor original do título que foi de R$ 5.500,00 .

**3.** Inclusão de um título no contas a pagar no valor de R$ 5.500,00  (valor original do título)

Cenário: Parametrizado para gerar o IRPF (pessoa física) na emissão

Utilizando o ponto de entrada "[F50CIRFF - Ponto de entrada para manipulação da base de cálculo do IRRF](https://tdn.totvs.com/pages/releaseview.action?pageId=689057140)" para alterar a base para R$ 6.000,00

E2\_IRRF =   R$ 741,27   (será gerado um título do tipo TX)  
**E2\_BASEIRF= R$ 5.500,00  (Observação:** A base do imposto sempre será gravada referente ao valor original do título**)**

Cálculo do IRPF

 R$ 6.000,00  \*  27,5%  =    R$ 1.650,00

 R$ 1.650,00   - R$ 908,73 =    **R$ 741,27   E2\_IRRF**

A base de cálculo apresentada em tela referente ao campo **E2\_BASEIRF,** não será R$ 6.000,00, e sim do valor original do título que foi de R$ 5.500,00   
  
  
Saiba mais:

[F50CIRFF - Ponto de entrada para manipulação da base de cálculo do IRRF](https://tdn.totvs.com/pages/releaseview.action?pageId=689057140)

[FIS - Configuração para cálculo de INSS (retenção)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018978571-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Configura%C3%A7%C3%A3o-para-c%C3%A1lculo-de-INSS-reten%C3%A7%C3%A3o)  
[IRRF - Retenção de Imposto de Renda Pessoa Jurídica ou Física](https://tdn.totvs.com/pages/releaseview.action?pageId=531009057)
