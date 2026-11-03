---
article_id: 360012171772
category: Materiais - Compras (SIGACOM)
content_hash: cb2d5a48415310e4a2be4ad67e9e41a819b7ea19c80cb936b88102e02c092e3c
fetched_at: '2026-06-28T22:41:10.410345+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual o conceito para
  se gerar uma Autorização de Entrega na rotina MATA122 ?
type: support-article
updated_at: '2024-06-24T12:24:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012171772-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-o-conceito-para-se-gerar-uma-Autoriza%C3%A7%C3%A3o-de-Entrega-na-rotina-MATA122
---

**Dúvida**

Qual o conceito para se gerar uma **Autorização de Entrega na rotina MATA122** ?

**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Solução**

A rotina **Autorização de Entrega** (**MATA122**) deve ser gerada antes de receber os materiais provenientes de um **Contrato de Parceria** (**MATA125**), para desta forma poder efetuar as baixas dos itens solicitados neste contrato e assim registrar a autorização da compra.

Pode efetuar-se a**Autorização de Entrega** parcial, ficando a quantidade restante em aberto para outras autorizações.

A **Autorização de Entrega** equivale a um **Pedido de Compra** (**MATA121**), porém, é utilizada somente para produtos com **Contrato de Parceria**. Ainda assim, as **Autorizações de Entrega** são gravadas na mesma tabela dos **Pedidos de Compras** (**Tabela - SC7**).

Ao acessar a rotina **Pedidos de Compra**, são apresentados todos os registros efetuados por esta rotina e também os efetuados na **Autorização de Entrega**, apenas para visualização.

Para configurar permissão ou não para a alteração do preço unitário do produto no recebimento da nota fiscal ou na inclusão da **Autorização de Entrega**, mesmo quando os valores já foram informados no **Pedido de Compras**, na **Autorização de Entrega** ou no **Contrato de Parceria**, sugerimos verificar os conteúdos disponíveis na configuração do parâmetro **MV\_ALTPRCC** utilizando o módulo **Configurador**.

***Obs.:***

*A autorização de entrega se dá independente da data inserida no campo "data de entrega" (C7\_DATPRF), não existindo no padrão do sistema validação impeditiva, na inclusão da informação neste campo.*

***Saiba Mais:***

* [MP - SIGACOM - Pontos de entrada rotinas MATA120 - Pedido de Compras e MATA122 - Autorização de Entrega](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006480572-MP-SIGACOM-Pontos-de-entrada-rotinas-MATA120-Pedido-de-Compras-e-MATA122-Autoriza%C3%A7%C3%A3o-de-Entrega?source=search)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
