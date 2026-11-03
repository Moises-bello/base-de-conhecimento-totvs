---
content_hash: f5cb1e53dc979f30be94005a4af4ff5843d5604c95c0a167d1873db479b3ec88
fetched_at: '2026-06-29T00:10:46.578118+00:00'
page_id: '554655629'
product: rm
source: tdn-rm
title: Fechamento do Condomínio Integral - Processo - Cancelar Lançamentos de Adiantamento
  de Cobrança Direta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=554655629
version: 5
---

**Cancelar****lançamentos****de adiantamento de cobrança direta**

---

Esse processo permite o cancelamento de lançamentos financeiros gerados para **Adiantamento de****Cobrança Direta**.  
   
**Pré-Condições:**

* Adiantamento de Cobrança Direta com status igual à "**Integrado**"
* O adiantamento de cobrança direta integrado não pode ter nenhum lançamento em situação de baixado/boleto gerado que impossibilite seu cancelamento

**Como utilizar:**

1. Selecione um fechamento desejado;
2. Em **Anexos**selecione **Adiantamento de****Cobrança Direta**
3. Na aba de Adiantamento de Cobrança Direta que se abriu selecione um ou mais registros de cobranças diretas complementares
4. Em **Processos** de Adiantamento de Cobrança Direta clique na opção **Cancelar Lançamentos**
5. O processo irá cancelar os lançamentos dos registros selecionados, desde que eles atendam às pré-condições
6. Os registros selecionados que foram processados com sucesso terão seu status alterado para "Calculado".

Importante!

* O agrupamento por cliente/fornecedor é definido pelo usuário no momento da execução do processo de geração de lançamentos. Contudo existe o agrupamento por subunidade que é automático na geração do lançamento. Portanto duas ou mais apurações para uma mesma subunidade serão agrupadas no lançamento gerado.
* No cancelamento do lançamento de adiantamento de cobrança, caso o sistema detecte que uma cobrança está agrupada com uma outra, então esta segunda será cancelada mesmo não tendo sido selecionada no processo.
