---
article_id: 360025521491
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 0100beec4d0798896d20a6e6e86c3b680a909658409962455165cfde065cdb90
fetched_at: '2026-06-28T22:37:55.022572+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB - A Contabilidade
  está em modo exclusivo e foi solicitado o processamento de todas as filiais
type: support-article
updated_at: '2025-10-13T22:01:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025521491-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-A-Contabilidade-est%C3%A1-em-modo-exclusivo-e-foi-solicitado-o-processamento-de-todas-as-filiais
---

**Ocorrência**No módulo Financeiro, ao tentar realizar a contabilização online no **Retorno de Cobrança (FINA200)** com a pergunta:**Processa Filial=Todas Filial** quando a tabela: **CT2** é **Exclusivo** apresenta mensagem **A Contabilidade está em modo exclusivo e foi solicitado o processamento de todas as filiais**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**O aviso apresentando através da mensagem é uma validação padrão da rotina retorno.  
Será apresentada quando é contabilizado de forma online o Retorno de Cobrança e quando preenchido a pergunta: **Processa Filial=Todas Filial** e o compartilhamento da tabela: CT2 é Exclusivo.  
  
**Solução**Neste caso não é realizado a contabilização Online, deverá contabilizar de forma off line através da rotina **CTBAFIN**.
