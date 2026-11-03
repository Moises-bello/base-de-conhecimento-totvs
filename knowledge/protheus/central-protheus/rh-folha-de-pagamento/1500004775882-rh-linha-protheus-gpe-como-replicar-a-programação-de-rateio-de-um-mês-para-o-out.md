---
article_id: 1500004775882
category: RH - Folha de Pagamento
content_hash: 080885ddbe9e291c31de74723aa4474623a3bec3f41bebd42c9ac8578373864f
fetched_at: '2026-06-28T22:44:14.773914+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como replicar a programação de rateio de um mês
  para o outro durante o fechamento da folha
type: support-article
updated_at: '2024-09-11T11:58:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004775882-RH-Linha-Protheus-GPE-Como-replicar-a-programa%C3%A7%C3%A3o-de-rateio-de-um-m%C3%AAs-para-o-outro-durante-o-fechamento-da-folha
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26292863958167) Tempo aproximado para leitura: 00:02:00 min**  
**Dúvida**Como replicar a programação de rateio de um mês para o outro durante o fechamento da folha?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Foi realizado a criação do parâmetro MV\_REPLRAT (deve ser incluído via configurador para que a implementação tenha efeito) que permitirá a réplica automática da programação de rateio mensal.

Quando o parâmetro estiver habilitado, caso exista uma programação de rateio com inicio e fim no mês/ano do período de cálculo que será fechado, a programação será replicada para o próximo mês.

**Importante:** Se a programação de rateio iniciar em um mês e terminar em outro, a programação não será replicada.

Ao clicar em Manutenção ou em Visualizar o filtro é carregado com o período atual da folha, caso não encontre um período o sistema mostrará todos os registros:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006432402)

Para alterar o filtro basta alterar as informações nos campos "Mês/Ano de" e "Mês/Ano até", clique em "Atualizar Filtro" o grid com as informações será atualizado, filtrando os registros pelo filtro definido:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006432422)

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[RH - Linha Protheus - GPE - Como realizar a programação de rateio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018658931-RH-Linha-Protheus-GPE-Como-realizar-a-programa%C3%A7%C3%A3o-de-rateio)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
