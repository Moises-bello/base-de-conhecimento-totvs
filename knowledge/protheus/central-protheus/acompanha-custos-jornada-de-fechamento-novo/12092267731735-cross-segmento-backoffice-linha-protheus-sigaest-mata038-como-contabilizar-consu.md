---
article_id: 12092267731735
category: ACOMPANHA CUSTOS - JORNADA DE FECHAMENTO (NOVO)
content_hash: 8c52eab27c2ed7db354a85e00609076275db64c8fa88ea7f26c237b9f37b4677
fetched_at: '2026-06-28T22:38:48.181859+00:00'
product: protheus
section_id: 5367899706647
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA038 - Como contabilizar
  consumo e produção no acompanha custos?
type: support-article
updated_at: '2025-03-12T12:23:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12092267731735-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-Como-contabilizar-consumo-e-produ%C3%A7%C3%A3o-no-acompanha-custos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21985089671191) Tempo aproximado para leitura: **00:03:29 min** **Dúvida**Como efetuar a contabilização, dentro da rotina de acompanha custos, da forma antiga por ambas, ou então por consumo e produção?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - 12.1.33;

**Solução**

Pré-Condição

Para que a jornada de fechamento possua a etapa de contabilização, é necessário que o parâmetro de Gerar Lançamento Contábil esteja configurado como "Sim", e o ambiente precisa estar configurado como custo off-line (M) através do parâmetro MV\_CUSMED.

![](https://tdn.totvs.com/download/attachments/572501579/image2021-1-19_9-27-33.png?version=1&modificationDate=1611059253317&api=v2)

Após a configuração do parâmetro, a rotina de contabilização (MATA331) será incluída na jornada de fechamento.

Após a etapa de Análise e Revisão referente o recálculo das movimentações do período, ao clicar para a próxima etapa, será iniciado a Contabilização através da rotina de **Contabilização do Custo Médio - MATA331**, sendo atualizado em tempo real a situação da rotina que ocorre no sistema. Após a execução da Contabilização, caso haja necessidade, é possível refazer o processamento da rotina, através do botão "Refazer contabilização".

![](https://tdn.totvs.com/download/attachments/572501579/contabilizao.gif?version=1&modificationDate=1643224652067&api=v2)

**Contabilização por consumo e produção**

Pré-Condição

Para que a jornada de fechamento possua a etapa de contabilização por consumo e produção , é necessário que o parâmetro de Gerar Lançamento Contábil esteja configurado como "Sim" e que o parâmetro de Forma de Contabilização esteja configurado como "Contabilização por consumo e produção" , e o ambiente precisa estar configurado como custo off-line (M) através do parâmetro MV\_CUSMED.

![](https://tdn.totvs.com/download/attachments/572501579/image2021-1-19_9-27-33.png?version=1&modificationDate=1611059253317&api=v2)

![](https://tdn.totvs.com/download/attachments/572501579/image2021-5-13_13-58-7.png?version=1&modificationDate=1620925087920&api=v2)

Após a configuração dos parâmetros, a rotina de contabilização (MATA331) será incluída na jornada de fechamento e após a finalização do cálculo do custo e contabilização por consumo, será executado o fluxo de cálculo e contabilização por produção.

![](https://tdn.totvs.com/download/attachments/572501579/consumo_e_producao.gif?version=1&modificationDate=1643225910543&api=v2)

Após a etapa de Análise e Revisão referente o recálculo das movimentações do período, ao clicar para a próxima etapa, será iniciado a Contabilização através da rotina de **Contabilização do Custo Médio - MATA331**, sendo atualizado em tempo real a situação da rotina que ocorre no sistema. Após a execução da Contabilização, caso haja necessidade, é possível refazer o processamento da rotina, através do botão "Refazer contabilização".

![](https://tdn.totvs.com/download/attachments/572501579/refazer_contabilizacao.gif?version=1&modificationDate=1643226342137&api=v2)

* [Como fica a questão dos lançamentos contábeis que apresentem alguma pendência de conta contábil, por exemplo? Uma vez, que a tela de contabilização não é mais exibida.](https://tdn.totvs.com/pages/viewpage.action?pageId=684982280)

**Saiba Mais**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Validação para inicia a rotina Acompanha Custos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5240908654999)*
