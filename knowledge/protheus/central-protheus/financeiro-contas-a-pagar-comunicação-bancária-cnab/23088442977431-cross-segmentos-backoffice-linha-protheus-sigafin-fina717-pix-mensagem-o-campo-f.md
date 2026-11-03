---
article_id: 23088442977431
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 62e6a9bd2023b80cbcdc6f57a06acd1b35386cd683492e6d8a53510be6a6bf60
fetched_at: '2026-06-28T22:37:56.373339+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA717 - PIX - Mensagem:
  "O campo Forma de identificação não é válido"'
type: support-article
updated_at: '2024-04-29T18:36:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23088442977431-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA717-PIX-Mensagem-O-campo-Forma-de-identifica%C3%A7%C3%A3o-n%C3%A3o-%C3%A9-v%C3%A1lido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23088470817687) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar a transmissão de título em "PIX" na rotina de pagamentos online via API, ocorre a mensagem **"Não foi possível recuperar as informações do usuário. O campo Forma de identificação não é válido"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23088470820119)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210  
  
**Causa**Esse incidente ocorre, pois na rotin**a** de Cadastro de fornecedores (MATA020), o fornecedor informado não possui chave PIX

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23088470823703)

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acessar o **cadastro de fornecedores (MATA020)**  
2. Posicionar sobre o **Fornecedor** informado na transmissão de pagamentos   
3. Clicar em **"Outras Ações" >> "Chaves PIX"**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23088442947095)  
  
4. Informar o tipo e chave **PIX do fornecedor**, definir como **"Principal"**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23088470830359)

5. Retransmitir o título, pela opção de **"Transmitir Rejeitados"** no **Monitor de pendências** do **FINA710**, ou cancelar e gerar novamente o **Borderô de pagamentos (FINA240)**  
  
**Saiba mais**  
[Comunicação bancária online - FINA710](https://tdn.totvs.com/pages/releaseview.action?pageId=734394374)  
[Pagamentos instantâneos - PIX](https://tdn.totvs.com/pages/releaseview.action?pageId=569478747)
