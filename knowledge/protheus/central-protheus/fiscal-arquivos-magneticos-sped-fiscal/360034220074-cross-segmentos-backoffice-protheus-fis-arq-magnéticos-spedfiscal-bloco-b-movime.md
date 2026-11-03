---
article_id: 360034220074
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 9558c32a153610642121a590011270f34038d0865b01d2f5598da78eb6881714
fetched_at: '2026-06-28T22:42:02.510010+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPEDFISCAL
  - Bloco B - Movimentação de Instituição Financeira.
type: support-article
updated_at: '2025-02-11T21:36:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034220074-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPEDFISCAL-Bloco-B-Movimenta%C3%A7%C3%A3o-de-Institui%C3%A7%C3%A3o-Financeira
---

**Dúvida**Como incluir as Movimentações de Instituição Financeira na Rotina FISA300?  
   
 **Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**Ao acessar a rotina **FISA300**, em **Rotinas disponíveis** -> **Apuração ISS** -> **Movimentação de Instituição Financeira**, existe a opção de Incluir, Alterar ou Visualizar as movimentações. Deverão ser incluídas as movimentações relativas às prestações de serviços por instituições financeiras com base no **Plano Contábil das Instituições do Sistema Financeiro Nacional – COSIF**, disponibilizado pelo Banco Central do Brasil.   
  
As receitas inclusas nessa rotina servirão de insumo para a geração do registro **B350 (SERVIÇOS PRESTADOS POR INSTITUIÇÕES FINANCEIRAS)**.   
Esse registro deve demonstrar todas as receitas referentes a serviços (classificação 7.1.7.00.00-9 do COSIF), ainda que não incluídos no anexo da Lei Complementar 116/2003. **Só deverão ser excluídas destas receitas as prestações acobertadas por Notas Fiscais de Serviço**.

Serão exibidas, do lado direto, as movimentações existentes, com opções de inclusão de novos registros, bem como alteração e exclusão de registros já existentes:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045154713/mceclip0.png)

A rotina (**FISA093**) alimenta a tabela **CLL - ISS Instituições Financeiras**, que atualmente já é utilizada no Livro Fiscal Eletrônico (LFE).
