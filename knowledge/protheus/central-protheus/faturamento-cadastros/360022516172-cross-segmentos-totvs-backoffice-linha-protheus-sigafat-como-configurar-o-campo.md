---
article_id: 360022516172
category: Faturamento - Cadastros
content_hash: edf6ea6979ad544607dea97fd78f186fc11e02f2a033001762b8d3cace7012c8
fetched_at: '2026-06-28T22:38:35.510963+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como configurar
  o campo placa para atender o formato "Mercosul"
type: support-article
updated_at: '2023-07-05T12:55:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022516172-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-configurar-o-campo-placa-para-atender-o-formato-Mercosul
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15789595237655) Tempo aproximado para leitura: **00:04:00 min****

**Dúvida**Como configurar a *picture* do campo placa para atender o formato **Mercosul**?

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) -  Todas as versões

**Causa**

Alteração da máscara "**@R XXX-9999"** da rotina **Cadastro de Veículos** campo **"Placa" (DA3\_PLACA)** e rotina **"Pedido de Vendas"** os campos "**Carreta" (C5\_PLACA2) e "Truck/Cavalo" (C5\_PLACA1)** para atender o novo sistema de placas de identificação de veículos (**MERCOSUL**).

**Solução**

Para alteração do campo "**Placa"** (**DA3\_PLACA)**, acesse o **Configurador** (**SIGACFG)** >> **Base de Dados** >> **Dicionário** >> **Bases de Dados;**

Em Dicionário de Dados, abra a tabela **DA3** e localiza o campo **DA3\_PLACA**, altere o formato **@!** para atender o "MercoSul."

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15788877198487)

Para alteração dos campos "**Carreta"** (**C5\_PLACA2) e "Truck/Cavalo" (C5\_PLACA1)**, acesse o **Configurador** (**SIGACFG)** >> **Base de Dados** >> **Dicionário** >> **Bases de Dados;**

Em Dicionário de Dados, abra a tabela **SC5** e localiza o campo **C5\_PLACA2**, altere tamanho **8** e o  formato **@!** para atender o "MercoSul."

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15789002732567)

Em Dicionário de Dados, abra a tabela **SC5** e localiza o campo **C5\_PLACA1**, altere tamanho **8** e o  formato **@!** para atender o "MercoSul."

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15789063107735)

Conclusão do ajuste;

Cadastro de Veículos;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15789230694039)

Pedidos de Venda;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15789291836183)
