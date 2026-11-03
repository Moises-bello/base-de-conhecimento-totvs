---
article_id: 31633014918039
category: SIGAEST - CUSTOS
content_hash: e79531b75b5f52c6896a1bbcc097df5d620189183028bb581e80a16f9d799ef5
fetched_at: '2026-06-28T22:39:00.749599+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como é possível apontar
  perdas com Custo Zerado para produto que sera descartado (Sucata)?
type: support-article
updated_at: '2025-10-01T14:13:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31633014918039-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-%C3%A9-poss%C3%ADvel-apontar-perdas-com-Custo-Zerado-para-produto-que-sera-descartado-Sucata
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31633000737047) Tempo aproximado para leitura: **00:03:15 min** **Dúvida**

Ao efetuar um apontamento de Perda e informar o produto Destino, precisamos que o produto Destino **não seja custeado**, pois o mesmo será apenas um descarte sem Custos. Como é possível apontar perdas com Custo Zerado para produto descartado (Sucata)?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Todas as versões  
  
**Solução**

Para melhor compreensão do funcionamento padrão, toda Movimentação Interna (SD3) não valorizada apropria o Custo Médio do produto Destino.

No cenário abordado, precisa que o produto Destino ***não tenha Custo na Movimentação e não afete o custo da produção*, pois será um produto descartado, por exemplo uma sucata sem Custo**.

Nesse caso, no padrão não tem essa funcionalidade específica, **mas é possível**, veja um exemplo no passo a passo abaixo:

 - Utilizar o **parâmetro (SX6)** [**MV\_PERDINF = .F. (Falso)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7093136901527-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Apropria%C3%A7%C3%A3o-do-custo-em-Apontamento-de-Perda)

 - **Opcional:** Utilizar o parâmetro [**MV\_DIGIPER habilitado**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034904634-Manufatura-Linha-Protheus-SIGAPCP-Funcionamento-da-perda-durante-o-apontamento-de-produ%C3%A7%C3%A3o) para informar a perda no momento do Apontamento;

- Na rotina **Apontamento de Perda (MATA685)**, pressionar a **tecla F12** e manter o parâmetro "**Requisita Produto Origem"** igual a "**Não"**.

![F12 MATA685.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/31634718875415)

 - Criar um produto Novo SUCATA SEM CUSTO;

![produto sucata.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/31635024665367)

 - Na rotinas Saldos Iniciais (MATA220) incluir o Saldo Inicial Quantidade 0 e Valor 0;

![saldo inicial sucata.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/31635372746519)

 - Pronto, ao efetuar os Apontamento de Perdas e informar como Destino esse produto, não **utiliza Custo para o mesmo**. Dessa forma permite que seja descartado conforme regra de negócio específica.

![resultado sucata sem custo.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/31635372750743)

Veja também o vídeo abaixo com um passo a passo:

Saiba Mais:

[Clique aqui e veja mais artigos sobre CUSTOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[SIGAEST - Apropriação do custo em Apontamento de Perda](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7093136901527-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Apropria%C3%A7%C3%A3o-do-custo-em-Apontamento-de-Perda)

[SIGAPCP - Funcionamento da perda durante o apontamento de produção](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034904634-Manufatura-Linha-Protheus-SIGAPCP-Funcionamento-da-perda-durante-o-apontamento-de-produ%C3%A7%C3%A3o)
