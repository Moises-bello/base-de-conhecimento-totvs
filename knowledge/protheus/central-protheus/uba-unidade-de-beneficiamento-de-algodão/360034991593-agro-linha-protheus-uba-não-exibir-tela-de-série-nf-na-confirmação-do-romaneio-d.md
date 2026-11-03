---
article_id: 360034991593
category: UBA - Unidade de Beneficiamento de Algodão
content_hash: 93ea3b7c2f341dbea599b2ed4f2256a468cd9dfec23fc39ee3c19be62275a6a6
fetched_at: '2026-06-28T22:45:35.627918+00:00'
product: protheus
section_id: 360005717853
source: central-protheus
title: Agro - Linha Protheus - UBA - Não exibir tela de série NF na confirmação do
  romaneio de transferência
type: support-article
updated_at: '2024-03-15T14:13:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034991593-Agro-Linha-Protheus-UBA-N%C3%A3o-exibir-tela-de-s%C3%A9rie-NF-na-confirma%C3%A7%C3%A3o-do-romaneio-de-transfer%C3%AAncia
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22096996130071)**Tempo aproximado para leitura: **00:00:30 min**  
 **Dúvida**Como faço para que não seja exibida a tela referente à série da **Nota Fiscal** ao confirmar um romaneio de transferência na rotina **AGRA500 - Romaneio Unificado**?  
  
 **Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - UBA - Unidade de Beneficiamento de Algodão - A partir da versão 12.1.17  
  
**Solução**Para que a tela correspondente à série da **Nota Fiscal** não seja exibida ao confirmar um romaneio de transferência é necessário acessar o parâmetro **MV\_AGRORI - Utiliza Módulo de Originação**e inserir **.T.** em seu conteúdo.É necessário também acessar o parâmetro **MV\_OGASERS - Define a série padrão a ser utilizada na geração dos documentos de saída** e informar a série utilizada para documentos de saída.
