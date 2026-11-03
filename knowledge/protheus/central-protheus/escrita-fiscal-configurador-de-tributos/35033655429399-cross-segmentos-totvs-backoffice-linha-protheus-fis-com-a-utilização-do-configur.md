---
article_id: 35033655429399
category: Escrita Fiscal - Configurador de Tributos
content_hash: 7496c46ec394260d099b1c74dfe1e7b1dc81fddf627b4a99801524bab55bb99c
fetched_at: '2026-06-28T22:39:17.690069+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – Com a utilização
  do Configurador de Tributos, os campos C5_RECISS e A1_RECISS são utilizados?
type: support-article
updated_at: '2025-10-06T13:41:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35033655429399-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Com-a-utiliza%C3%A7%C3%A3o-do-Configurador-de-Tributos-os-campos-C5-RECISS-e-A1-RECISS-s%C3%A3o-utilizados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35033655400599) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Com a utilização do Configurador de Tributos, os campos C5\_RECISS e A1\_RECISS são utilizados?  
  
**Ambiente**  
  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Fis - Todas as versões  
  
**Solução**

No **Protheus ERP da TOTVS**, a definição de quem é o responsável pelo recolhimento do **ISS (Imposto Sobre Serviços)** pode ser configurada por meio do **Configurador de Tributos**. Este processo envolve a utilização e integração de campos específicos nos cadastros de pedidos e clientes, conforme detalhado abaixo:

#### **1. Campos Utilizados**

* **C5\_RECISS** – Campo localizado no módulo de **Vendas (SC5)**, que indica, no pedido de venda, quem é o responsável pela retenção do ISS: o **emitente da nota fiscal** ou o **tomador do serviço**.
* **A1\_RECISS** – Campo localizado no cadastro de **Clientes (SA1)**, que também permite configurar previamente essa responsabilidade por cliente.

#### **2. Integração e Gravação dos Dados**

Durante o processo de emissão do RPS (Recibo Provisório de Serviços), o sistema utiliza os dados configurados nos campos mencionados (C5\_RECISS e A1\_RECISS) para gravar a informação final no campo:

* **F3\_RECISS** – Campo localizado no arquivo **SF3 (Cabeçalho de Notas Fiscais)**, que armazena o valor consolidado da responsabilidade de retenção do ISS. Esse valor será utilizado posteriormente tanto para a geração do XML do RPS quanto para os processos fiscais.

#### **3. Utilização do Campo F3\_RECISS**

O valor armazenado no campo **F3\_RECISS** é utilizado em dois pontos principais:

* **Geração do XML do RPS** – O campo é incluído no XML gerado para a prefeitura, indicando de forma correta quem é o responsável pelo recolhimento do ISS.
* **Apuração do ISS (Programa MATA954)** – Durante o processo de apuração do imposto, o sistema considera o valor do campo F3\_RECISS para classificar corretamente os valores de ISS a recolher ou reter.
