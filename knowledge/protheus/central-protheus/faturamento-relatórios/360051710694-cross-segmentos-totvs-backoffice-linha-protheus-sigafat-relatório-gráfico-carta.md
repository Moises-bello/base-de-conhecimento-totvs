---
article_id: 360051710694
category: FATURAMENTO - RELATÓRIOS
content_hash: 9025a7284aebae39464777e38f0d86e63acaab04c76b115d2237127d0570945c
fetched_at: '2026-06-28T22:38:22.974038+00:00'
product: protheus
section_id: 1500001539381
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Relatório Gráfico
  Carta de Correção Eletrônica de Nota Fiscal
type: support-article
updated_at: '2022-06-27T14:05:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051710694-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Relat%C3%B3rio-Gr%C3%A1fico-Carta-de-Corre%C3%A7%C3%A3o-Eletr%C3%B4nica-de-Nota-Fiscal
---

**Dúvida**

O sistema dispõe do relatório gráfico de carta de correção eletrônica semelhante ao Danfe das Notas fiscais?  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGAFAT- todas as versões.

**Solução**

No módulo de faturamento não há nenhum relatório que trate **CCe - Carta de Correção Eletrônica**.  
  
A CCe é um evento apenas informativo de correção, ou seja não altera a nota original e não grava nenhuma informação referente a isso nas tabelas do ERP.  
  
Hoje de forma padrão, não há nenhum relatório para saber as CCes transmitidas para as NFes e também não há gravação de nenhuma informação na tabela **SF3** (*Livros Fiscais*) sobre a CCe.  
  
A gravação ocorre apenas nas tabelas do **TSS SPED150** e **SPED154,** nos campos ***TPEVENTO = 110110***.  
  
Caso seja necessário a criação de um relatório, para criar um relatório via **Totvs relatório**, precisaria pegar as informações dessas tabelas de Sped, precisando de  apoio para extrair os dados dessas tabelas, contate a equipe **Sped TSS**.

Com relação a Carta de Correção por carga, hoje não é disponibilizado pelo Protheus a funcionalidade, com isso  não é passível de tratamento nas tabelas de SPED para uma  possível criação relatório de CCe. Em caso de dúvida do assunto contate a equipe d eSPED.

**Saiba mais sobre Carta de Correção Eletrônica:**

**[MP-NFE-Como-transmitir-CC-e-no-Protheus-](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025879314-MP-NFE-Como-transmitir-CC-e-no-Protheus-)**

**[MP - NFE - Impressão de Carta de Correção Eletrônica ( CCe / CC-e)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019180652-MP-NFE-Impress%C3%A3o-de-Carta-de-Corre%C3%A7%C3%A3o-Eletr%C3%B4nica-CCe-CC-e-)**

**[MP - NFE - Como corrigir a rejeição 215 ou 493 na CCE: Rejeição Evento não atende o Schema XML específico?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019481192-MP-NFE-Como-corrigir-a-rejei%C3%A7%C3%A3o-215-ou-493-na-CCE-Rejei%C3%A7%C3%A3o-Evento-n%C3%A3o-atende-o-Schema-XML-espec%C3%ADfico-)**
