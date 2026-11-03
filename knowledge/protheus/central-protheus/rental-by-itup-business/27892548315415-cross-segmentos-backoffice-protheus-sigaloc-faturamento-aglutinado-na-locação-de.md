---
article_id: 27892548315415
category: Rental by ItUp Business
content_hash: 56174552a42ae56ac0558ba41851a8e99795857bb65ae08b3dcff00aa55415aa
fetched_at: '2026-06-28T22:36:20.472999+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC -  Faturamento Aglutinado na
  Locação de Equipamentos (SIGALOC)
type: support-article
updated_at: '2026-04-09T12:49:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27892548315415-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Faturamento-Aglutinado-na-Loca%C3%A7%C3%A3o-de-Equipamentos-SIGALOC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27892572982295) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como realizar o Faturamento Aglutinado no SIGALOC?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Este documento descreve a funcionalidade de **faturamento aglutinado** no módulo Rental, que permite consolidar itens de locação, mão de obra e outros serviços durante o processo de faturamento automático. O sistema utiliza as configurações feitas na capa do projeto para determinar os produtos que serão utilizados no faturamento aglutinado, garantindo uma gestão mais eficiente dos contratos de locação.

#### **Funcionamento**

1. **Configuração na Capa do Projeto:**

   * Na capa do projeto, é essencial configurar corretamente o produto que será utilizado no processo de aglutinação. O campo específico permite selecionar o produto de acordo com o tipo de serviço:
     + **Locação**
     + **Mão de Obra**
     + **Outros (Cobranças Adicionais)**

   Além disso, há um **campo combo** (Sim/Não) que define se o faturamento dos itens deve ser aglutinado. Essa configuração é o ponto de partida para que o sistema processe o faturamento aglutinado de forma correta.

   ![image2023-3-31_16-58-51.png](https://tdn.totvs.com/download/attachments/606426382/image2023-3-31_16-58-51.png?version=1&modificationDate=1680292731483&api=v2)
2. **Processo de Faturamento Aglutinado:**
   * Uma vez ativada a opção de aglutinação na capa do projeto, o sistema agrupa os itens de locação, mão de obra e outros serviços no Pedido de Venda.
   * A unificação dos itens é baseada nas categorias de serviço, sendo que o produto selecionado na capa será utilizado para todos os itens relacionados.
3. **Exemplo Prático:**

   * Considere um contrato com **5 itens de locação**:
     + **Configuração na Capa:** O produto específico para locação foi informado, e o campo de aglutinação foi marcado como "Sim".
     + **Pedido de Venda (SC6):** O sistema consolidará os 5 itens de locação em uma única entrada no pedido de venda, com os valores e quantidades aglutinados.
     + **Tabela FPZ:** Os detalhes de cada um dos 5 itens serão registrados individualmente na tabela FPZ para permitir um controle mais granular das locações.

   Esse processo garante que, embora o Pedido de Venda seja simplificado, o controle detalhado dos itens locados permanece disponível na tabela FPZ.

**Saiba mais:**[***Faturamento automático***](https://tdn.totvs.com/pages/releaseview.action?pageId=606426382)
