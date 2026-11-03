---
article_id: 23796298541335
category: Materiais - Compras (SIGACOM)
content_hash: 626c0f9848a415c1330ec7233a59c492308b9fda0c2aa4984a5ce7cdc29a4188
fetched_at: '2026-06-28T22:41:18.938248+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help na Classificação
  da Nota - O cliente/Fornecedor não possui CNPJ/CPF cadastrado!!!
type: support-article
updated_at: '2026-01-23T14:21:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23796298541335-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-na-Classifica%C3%A7%C3%A3o-da-Nota-O-cliente-Fornecedor-n%C3%A3o-possui-CNPJ-CPF-cadastrado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23796298506263) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Help na Classificação da Nota - O cliente/Fornecedor não possui CNPJ/CPF cadastrado!!!  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Compras - Todas as versões  
  
**Solução**  
O Help é apresentado quando utiliza uma Tes que está com o Campo de Transferência entre filiais habilitado **F4\_TRANFIL = 1**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23796298507671)

1-Verifique se a Nota é para inclusão pela rotina de **Transferência de Filiais (MATA310/MATA311)** do módulo de Estoque.

     1.1-Se a nota **Não** for incluída pela rotina de Transferência de Filiais (MATA310/MATA311) do modulo de estoque, mas sim pela rotina de Documento de Entrada (MATA103) do Compras, utilize uma TES com o campo **F4\_TRANFIL = 2 - Não.**

2-Se a nota For de **Transferência de filiais** siga as orientações abaixo:

     2.2-Verifique o Conteúdo do Parâmetro **MV\_FILTRF** igual a **T** revise todas as configurações do artigo abaixo:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310/MATA311 - Transferência entre Filiais utilizando o parâmetro MV\_FILTRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011717052-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Transfer%C3%AAncia-entre-Filiais-utilizando-o-par%C3%A2metro-MV-FILTRF?source=search)

     2.3-Se o Conteúdo **MV\_FILTRF** igual a **F** revise todas as configurações do artigo abaixo:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310 / MATA311 - Como configurar a Transferência entre Filiais (MATA310 / MATA311) no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418209855639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Como-configurar-a-Transfer%C3%AAncia-entre-Filiais-MATA310-MATA311-no-Protheus?source=search)

Para dúvidas no uso da rotina de Transferência entre Filiais (MATA310/MATA311) orienta-se o contato junto ao suporte ao módulo de estoque/Custos.

***Saiba Mais :***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
