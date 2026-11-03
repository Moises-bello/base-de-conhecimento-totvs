---
article_id: 10408284195351
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 9299c7a36a0941e15834b16532961eb65c68348e2cdb992e4f4528d2eeaf29b0
fetched_at: '2026-06-28T22:37:22.859299+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help "Atenção - Valor
  Total da Planilha não Previsto no Cronograma. O mesmo deve ser reestruturado" na
  rotina de medição
type: support-article
updated_at: '2024-02-07T12:20:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10408284195351-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-Aten%C3%A7%C3%A3o-Valor-Total-da-Planilha-n%C3%A3o-Previsto-no-Cronograma-O-mesmo-deve-ser-reestruturado-na-rotina-de-medi%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Ao encerrar uma medição ocorre o Help: "Atenção - Valor Total da Planilha não Previsto no Cronograma. O mesmo deve ser reestruturado" na rotina de medição

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10407256944663)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões  
  
**Solução**Esta mensagem normalmente ocorre quando o valor liquido previsto da Planilha da medição (***CXN\_VLLIQD***) estiver maior que o valor previsto do cronograma (considerando o limite informado no tipo de contrato) menos o valor realizado do Cronograma [ **CNF\_VLPREV(considerando o limite) - CNF\_VLREAL** ]  
  
Ou também quando há alguma divergência entre o montante/valor total do contrato e o montante do Cronograma Financeiro/Físico existentes no contrato.  
  
  
Quando há essas divergências, pode-se excluir a medição e incluir um nova, verificando se a questão ainda persiste, ou no caso havendo divergência ente valores da planilha e cronograma a forma de se reestruturar é a realização de uma revisão de renovação por exemplo no contrato realizando os devidos ajustes para os montantes do(s) cronograma(s) fiquem de acordo com o valor total do contrato.  
  
  
Dessa forma, é orientado a realização em ambiente de homologação da exclusão da medição e do processamento da rotina de recálculo do saldo ([Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar o Reajuste de Saldo em contratos, planilhas e cronograma financeiro ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020124591-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-o-Reajuste-de-Saldo-em-contratos-planilhas-e-cronograma-financeiro-?source=search)) para verificar se ocorre alguma mudança nas informações do contrato, de forma que sane a questão, ou modifique os valores para então estes poderem ser ajustados através de uma revisão de contrato, como reportado anteriormente.  
  
  
Caso necessário, para uma analise da base e identificação da causa para o contrato em específico pode-se entrar em contato com o ESN Totvs para a analise por um analista especialista em Loco.

***Saiba Mais:***

* [Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Revisão de Renovação de Contrato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025659713-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Revis%C3%A3o-de-Renova%C3%A7%C3%A3o-de-Contrato?source=search)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quais são os tipos de Revisão disponíveis, para revisar contratos no Gestão de Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034587334-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Quais-s%C3%A3o-os-tipos-de-Revis%C3%A3o-dispon%C3%ADveis-para-revisar-contratos-no-Gest%C3%A3o-de-Contratos-?source=search)
