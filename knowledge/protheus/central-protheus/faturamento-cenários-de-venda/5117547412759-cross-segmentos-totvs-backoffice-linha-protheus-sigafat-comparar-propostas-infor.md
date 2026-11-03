---
article_id: 5117547412759
category: Faturamento - Cenários de Venda
content_hash: e4e4e879191c9f1ad6c330f9c64c929eb7e89ac27b9666a64e3792cbe0d9886e
fetched_at: '2026-06-28T22:38:34.062363+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Comparar Propostas
  informa que não possui Revisões
type: support-article
updated_at: '2022-03-30T11:38:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5117547412759-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Comparar-Propostas-informa-que-n%C3%A3o-possui-Revis%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao acessar a opção "Comparar Propostas" na rotina de Oportunidade de Vendas (FATA300), o sistema exibe a mensagem "Atenção! Proposta selecionada não possui revisões!".  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Causa**A Comparação de Propostas avalia quais dados foram modificados em uma proposta comercial, supondo que tenha criado uma Proposta comercial ele será gravada como Revisão 01, caso altere qualquer, dado após gravar a proposta, o sistema irá registrar como revisão 02. Essa funcionalidade compara os dados da revisão 01 e 02, indicando o que foi alterado.  
  
**Solução**Realize alterações na proposta comercial e salve essas alterações para que o sistema registre uma nova revisão, após isso execute a comparação para que o sistema demonstre a tela com o comparativo.

**Exemplo de uso**: [Comparar Propostas.mkv](https://totvssuporte.zendesk.com/hc/article_attachments/5117562886423/Comparar_Propostas.mkv)
