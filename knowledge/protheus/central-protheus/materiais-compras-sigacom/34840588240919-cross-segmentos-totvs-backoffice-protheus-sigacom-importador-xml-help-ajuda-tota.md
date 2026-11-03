---
article_id: 34840588240919
category: Materiais - Compras (SIGACOM)
content_hash: a45df46fa4b805aeebc874b6c7c286f6c9c0d954f8bd6aedf85503ddce22cd7a
fetched_at: '2026-06-28T22:41:19.934022+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML - Help
  AJUDA TOTAL Valor total inválido
type: support-article
updated_at: '2025-09-10T16:16:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34840588240919-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML-Help-AJUDA-TOTAL-Valor-total-inv%C3%A1lido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34840666448407) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**

Ao Gerar Documento na rotina do Monitor, sistema gera ocorrência  Help AJUDA TOTAL Valor total inválido, conforme print abaixo.

***Obs.: Este erro pode ocorrer quando a inconsistência estiver no valor total, no valor unitário ou na quantidade.***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34840666449175)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34840666449943)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - versão 12Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - versão 12  
  
**Causa**  
O erro em questão ocorre quando a configuração de **TAMANHO** e/ou **DECIMAIS** dos campos das tabelas **SDS** e/ou **SDT** está divergente da configuração dos campos das tabelas **SF1** e **SD1** que são suas correspondentes.  
  
**Solução**  
Para solucionar esta ocorrência, abra o módulo SIGACFG e verifique como estão configurados os campos abaixo. **Os campos correspondentes precisam ter mesmo tamanho e decimais.** Por exemplo, se o campo DS\_QUANT tiver tamanho 15 e decimais 4 o campo D1\_QUANT também deverá ter. Seguem abaixo os campos correspondentes que devem ser validados.

***Quantidade***

DT\_QUANT e D1\_QUANT

***Valor unitário***

DT\_VUNIT e D1\_VUNIT

***Valor total***

DT\_TOTAL e D1\_TOTAL

Sendo assim, busque a configuração desses campos e ajuste-os conforme o necessário para que fiquem corretos conforme indicado acima.

Após realizar os ajustes, é necessário que efetue o procedimento abaixo para reprocessar a nota

1. Abra a rotina do Monitor, localize e selecione a nota com essa ocorrência, clique em Outras ações, clicar em Excluir
2. Abra o Reprocessar, vá na aba Excluídos, localize a nota e selecione-a, clicar em Excluir
3. Com a nota excluída, agora será necessário importá-la manualmente.
4. Agora vamos importá-la do zero  
                              1.Coloque o XML na pasta INN  
                              2. Execute as rotinas COLAUTOREAD e depois SCHEDCOMCOL  
                              3. A nota irá aparecer no Monitor  
                              4. Selecione a nota, e gere documento novamente

O aumento de casas decimais no Protheus é uma questão delicada. Quando realizado sem os devidos critérios, ou não recebe a devida manutenção, pode causar diversas inconsistências.

Por esse motivo a TOTVS Criou os [**Grupos de Campos Numéricos**](https://youtu.be/BXPL4BPr668?si=Q_-ZXQtei4JMYyGe).

**IMPORTANTE**: Qualquer tratamento relacionado a casas decimais é considerado um desvio do Nativo do Protheus (no qual é padrão o uso de dois dígitos, apenas, para o ambiente Faturamento).  
Portanto, é indicado que qualquer alteração neste sentido seja realizado e documentado por um analista in loco (Consultar diretamente seu ESN) para análise pontual de sua base/ seu cenário, e sempre utilizando os [**Grupos de Campos Numéricos**](https://youtu.be/BXPL4BPr668?si=Q_-ZXQtei4JMYyGe).

***Saiba Mais:***

* [Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-MP-SIGACOM-Importador-XML#:~:text=No%20Importador%20de%20XML%20%C3%A9%20necess%C3%A1rio%20criar%20agendamentos,op%C3%A7%C3%B5es%20do%20menu%20Ambiente%20-%3E%20Schedule%20-%3E%20Schedule%3A)
* [Agendamento (Schedule) - Importador XML](https://tdn.totvs.com/display/public/PROT/Agendamento+%28Schedule%29+-+Importador+XML)
* <https://tdn.totvs.com/pages/viewpage.action?pageId=237371831>
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
