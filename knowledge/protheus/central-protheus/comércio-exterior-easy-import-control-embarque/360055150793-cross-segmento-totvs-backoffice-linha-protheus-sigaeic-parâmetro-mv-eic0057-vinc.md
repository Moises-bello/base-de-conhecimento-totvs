---
article_id: 360055150793
category: Comércio Exterior - Easy Import Control - Embarque
content_hash: e65670d190eaed5352ae364f1ded11ce83838684209dfd26157520e43174897c
fetched_at: '2026-06-28T22:39:48.750265+00:00'
product: protheus
section_id: 1500001538381
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Parâmetro MV_EIC0057
  Vincular itens parciais na Invoice
type: support-article
updated_at: '2022-01-20T20:19:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055150793-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Par%C3%A2metro-MV-EIC0057-Vincular-itens-parciais-na-Invoice
---

**Dúvida**Como configurar o parâmetro MV\_EIC0057?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**Foi criado o parâmetro MV\_EIC0057 que permite a gravação de embarques de importação utilizando itens parciais na invoice. Com a utilização desse novo parâmetro, o cliente tem a opção de vincular itens a invoice em momentos diferentes no processo, não sendo obrigatório que todos os itens que fazem parte do processo estejam associados a uma ou mais invoice na fase de embarque para que possa efetuar a gravação do processo.  
Este parâmetro tem funcionalidade apenas para a fase de embarque.

Pré-Requisitos:  
• Habilitar o parâmetro MV\_EIC0057 = .T.  
• Possuir uma Solicitação de Importação e Purchase Order com mais de um item.  
• Possuir um Embarque com Invoice e com itens parcialmente vinculados.  
• Gravar o Desembaraço.

Sequência 01  
1. No Easy Import Control (SIGAEIC), acesse Atualizações / Embarque / Manutenção (EICDI500);  
2. Selecione o processo em Clique em Alterar;  
3. Clique em “Ações Relacionadas / Invoices”, selecione a invoice e clique em “Ações Relacionadas / Alterar”. Desmarque um  
item que está vinculado a invoice e clique em Confirmar;  
4. Na tela de “Manutenção de Invoices”, clique em Confirmar e na tela de “Fechamento de Embarque” clique novamente em  
confirmar para salvar o processo;  
5. Observe que o processo foi salvo sem apresentar a mensagem “Existem itens ou saldo de itens sem Invoice.”.
