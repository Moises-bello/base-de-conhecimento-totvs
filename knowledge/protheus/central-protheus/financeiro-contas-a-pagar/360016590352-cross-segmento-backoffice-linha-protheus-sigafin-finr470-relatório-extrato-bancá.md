---
article_id: 360016590352
category: Financeiro - Contas a Pagar
content_hash: f736b9f9c37bc44d1cb4ad66aac225c11584538cc3f4b20678c2b1e9d8f84257
fetched_at: '2026-06-28T22:38:06.999775+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINR470 - Relatório
  Extrato Bancário não apresenta informações de todas as filiais '
type: support-article
updated_at: '2025-01-31T19:44:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016590352-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINR470-Relat%C3%B3rio-Extrato-Banc%C3%A1rio-n%C3%A3o-apresenta-informa%C3%A7%C3%B5es-de-todas-as-filiais
---

**Dúvida**Como faço para visualizar as movimentações de todas as filiais no relatório de Extrato Bancário?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINR470 - Todas as versões  
  
**Solução**

O extrato bancário permite visualizar as movimentações de todas as filiais com a **tabela SE5** (movimentos bancário) exclusiva por filiais, para que seja possível visualizar os saldos de todas as filiais, a **tabela SA6** (Bancos) precisa estar compartilhada por filiais e o usuário ter acesso pelo **Mod. Configurador as filiais.**

Foi aplicada a melhoria por questão de segurança no código fonte do relatório para que não sejam listados movimentos de outras filiais, pois o usuário poderia ter acesso a informações indevidas/sigilosas. 

Este tratamento hoje é padrão do fonte, caso ainda não consiga visualizar as movimentações por filial seguindo a regra acima, será necessário avaliar se possui o **ponto de entrada** **F470ALLF**. e desabilita-lo pelo Modulo **SIGACFG -> Ambientes -> Cadastros -> Catalogo de Personalização**   
  
**Saiba mais**  
[Extrato Bancário - FINR470 - Financeiro P12](https://tdn.totvs.com/pages/releaseview.action?pageId=496801916)
