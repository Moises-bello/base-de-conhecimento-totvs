---
article_id: 5240908654999
category: ACOMPANHA CUSTOS - JORNADA DE FECHAMENTO (NOVO)
content_hash: 9734e3813be79e8eb241ad38f1ebc69585b00da37c06ea951bff0b4c1408990e
fetched_at: '2026-06-28T22:38:48.242502+00:00'
product: protheus
section_id: 5367899706647
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA038 - Validação
  para iniciar a rotina Acompanha Custos
type: support-article
updated_at: '2025-03-12T12:23:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5240908654999-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-Valida%C3%A7%C3%A3o-para-iniciar-a-rotina-Acompanha-Custos
---

Para iniciar o projeto Acompanha Custo, temos que seguir os seguintes requisitos:

Já ter efetuado as configurações iniciais de acordo boletim abaixo:

[**Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - O que é a rotina Acompanha Custos?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5065773526039)

* No dicionário de dados do cliente, deve existir as  tabelas: **D3X, D3Y**e**D3W**.
* Nos parâmetros do sistema, configurar o parâmetro "MV\_CUSTEXC" para o valor de não exclusivo.
* Atualizar o fonte ACJOURNEY.LOG, contido no pacote da expedição contínua igual ou superior a data **04/02/2022**.

No pacote da [expedição continua](https://tdn.totvs.com/pages/releaseview.action?pageId=522000602), ira conter as pastas: **sdf > bra**

* Dentro da pasta **bra**, contem os arquivos para atualização do dicionário(D3X,D3Y,D3W), que deve ser realizada após cópia dos arquivos, para dentro da pasta **SystemLoad**, e posteriormente realizar o UPDDISTR? [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042296533-MP-FIS-Procedimento-UPDDISTR)

**Aviso**

* Devido a necessidade da jornada de fechamento não poder utilizar a execução exclusiva através do parâmetro **MV\_CUSTEXC**, foi implementado o recurso de [Controle automático de bloqueio de movimentação - **MV\_CMDBLQV**](https://tdn.totvs.com/x/4zrjIg)para impedir movimentações no sistema que interfiram no cálculo do fechamento.
* Se o [Controle automático de bloqueio de movimentação - **MV\_CMDBLQV**](https://tdn.totvs.com/x/4zrjIg) for configurado como compartilhado, as alterações feitas no parâmetro serão refletidas em todas as filiais. Caso esse não seja o comportamento esperado, será preciso criar o parâmetro para cada filial de forma exclusiva.

Caso apresente algum erro ao iniciar o Acompanha Custos, será necessário aplicar o pacote de atualização do Acompanha Custos.

**Avalie também, se a sua apropriação é ONLINE ou OFFLINE antes de iniciar a jornada.**

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007482371-MP-SIGAEST-MATA330-Recalculo-do-custo-M%C3%A9dio-On-Line-MATA330-e-Saldo-Atual-para-Final-MATA350->

Se ONLINE > MV\_CUSMED = O

![](https://totvssuporte.zendesk.com/attachments/token/jfpOYmzAMRhs4JKAWgCzpCu8g/?name=image.png)

Se OFFLINE -> MV\_CUSMED = M

![](https://totvssuporte.zendesk.com/attachments/token/5AwvmPRyr8LumljROr6YJ9zcH/?name=image.png)

**Saiba mais**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - O que é a rotina Acompanha Custos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5065773526039)*

*[Clique aqui e veja mais artigos sobre o Acompanha Custos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/5367899706647-MONITOR-DE-CUSTOS)*
