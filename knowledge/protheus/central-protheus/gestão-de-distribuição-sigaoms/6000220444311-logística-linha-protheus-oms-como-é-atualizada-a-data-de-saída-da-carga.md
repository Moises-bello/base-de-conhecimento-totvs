---
article_id: 6000220444311
category: Gestão de Distribuição (SIGAOMS)
content_hash: 3597602eed1012e9b58787d4b6182806d98d97b774c6634100dfbb2040341923
fetched_at: '2026-06-28T22:45:49.667064+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: 'Logística - Linha Protheus - OMS - Como é atualizada a Data de Saída da Carga '
type: support-article
updated_at: '2022-12-01T11:05:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6000220444311-Log%C3%ADstica-Linha-Protheus-OMS-Como-%C3%A9-atualizada-a-Data-de-Sa%C3%ADda-da-Carga
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:24 min****Dúvida**Como é atualizada a **Data de Saída** da Carga na rotina **Montagem de Carga - OMSA200**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**  
Na rotina **OMSA200 - Montagem de Carga**, temos o campo **DAI\_DTSAID - Data Saída**, que por padrão  vem preenchido com a **data** de **Montagem da Carga.** É utilizado esse tratamento devido uma carga conter vários **Pedidos de Venda** com **data de entregas diferentes.** Por conta desse canário, o módulo **TOTVS OMS - Order Management System** não tem como definir qual a melhor **data de entrega** no momento da **Montagem da Carga.**  
  
Após a criação da carga, é possível alterar a data de entrega:  
  
Acesse **OMSA200 - Montagem de Carga/Manutenção/Outras Ações/Seq. Ent/Outras Ações/Hora Inicial**, conforme exemplo abaixo:

![data1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/6377517901591/data1.JPG)

![22.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6377589575959/22.png)

![4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6377597509399/4.png)

Caso desejar um tratamento diferente do descrito acima, indicamos os seguintes Pontos de Entrada:

1. **OM200FIM** - Esse ponto de entrada é acionado no momento da gravação da Carga, sendo assim, é possível criar um tratamento para que seja preenchido a data de entrega da carga no campo **DAI\_DTSAID - Data Saída**, ou em algum campo customizado. *Link* da documentação técnica: [DT PE OM200FIM - Final do carregamento](https://tdn.totvs.com/display/PROT/DT+PE+OM200FIM+-+Final+do+carregamento)
2. **OS200VSB** - Esse ponto de entrada permite que seja incluído **um novo botão na tela de Outras Ações**, após acionar o **botão Seq Ent.** Dessa forma poderá criar uma função totalmente customizada para preencher a **Data de Entrega,** seja no campo padrão **DAI\_DTSAID - Data Saída** ou em um **campo customizado**. *Link* da documentação técnica: [DT PE OS200VSB - Inclusão de botões](https://tdn.totvs.com/pages/viewpage.action?pageId=612259295)
3. **OM200ADC** - Esse ponto de entrada permite incluir campos na validação padrão do preenchimento da **Data de Saída da carga** pelo processo padrão, citado inicialmente. Poderá ser incluído um **tratamento customizado** para que seja preenchido um campo customizado com a regra que o desejar. *Link* da documentação técnica: [DT PE OM200ADC - Inclusão de campos na sequência de entrega](https://tdn.totvs.com/pages/releaseview.action?pageId=611311189)

**Saiba mais**  
A relação dos **Pontos de Entrada** disponíveis na rotina **OMSA200-Montagem de Carga**, poderão ser acessados no *link*: [Logística - Linha Protheus - OMS - Pontos de Entrada disponíveis na rotina Montagem de Carga - OMSA200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000900021-Log%C3%ADstica-Linha-Protheus-OMS-Pontos-de-Entrada-dispon%C3%ADveis-na-rotina-Montagem-de-Carga-OMSA200)
