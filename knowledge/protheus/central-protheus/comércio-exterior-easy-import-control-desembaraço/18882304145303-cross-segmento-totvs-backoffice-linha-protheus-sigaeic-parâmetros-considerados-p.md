---
article_id: 18882304145303
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 74722090ebd5e8d705a007f969289919ec46cbd48a8fa7eee5a96dc7268af5ec
fetched_at: '2026-06-28T22:39:51.349165+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Parâmetros considerados
  para a Data de Emissão do Câmbio no Financeiro.
type: support-article
updated_at: '2023-11-07T14:16:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18882304145303-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Par%C3%A2metros-considerados-para-a-Data-de-Emiss%C3%A3o-do-C%C3%A2mbio-no-Financeiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18882261666071)Tempo aproximado para leitura: **03:00 min** **Dúvida**Quais Parâmetros o Sistema considera para a Data de Emissão do Câmbio no Financeiro?  
  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – A partir da versão 12.1.33  
   
**Solução**Sobre a Data de Emissão, o sistema irá levar em consideração a configuração dos parâmetros: "**MV\_DTB\_APD"** e "**MV\_DTEMIS".**   
Na tela do Contas a Pagar existe o campo "**Dt. Emissão (E2\_EMISSAO)"**. Dentro do Padrão, o conteúdo desse campo é a Data de Emissão da Invoice **(W9\_DT\_EMIS)**. Porém, existe um parâmetro, o "**MV\_DTEMIS"**, que define qual campo o sistema utilizará para preenchê-lo (desde que a data não seja maior do que a data de vencimento, se for, o sistema preencherá o "**E2\_EMISSAO"** com a própria data de vencimento).  
   
As parcelas principais da Invoice (**Evento 101**) serão criadas conforme as Condições de Pagamentos registradas nas mesmas. As datas de vencimentos serão apuradas a partir de uma data base. Por padrão o sistema utiliza a Data de Embarque do processo (da mesma forma que é realizado no Siscomex), mas é possível modificar este critério através do parâmetro "**MV\_DTB\_APD"**, que armazena o campo de referencia para a data base, devendo ser este campo pertencente à tabela da declaração de importação **(SW6)** ou à tabela de Invoices **(SW9)**.

**Saiba mais:**[Títulos no SIGAEIC](https://tdn.totvs.com/pages/releaseview.action?pageId=185745467&preview=%2F185745467%2F185668046%2FFAQ+-+Como+Gerar+T%C3%ADtulos+no+SIGAEIC.docx)
