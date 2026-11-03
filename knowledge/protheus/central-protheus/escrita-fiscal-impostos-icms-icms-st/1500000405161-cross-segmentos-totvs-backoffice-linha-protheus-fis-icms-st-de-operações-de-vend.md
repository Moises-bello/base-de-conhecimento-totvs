---
article_id: 1500000405161
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: e43315ac973e7a8c78d13bfa74fff164838ef5ed9fae80fb33fdf4fbfadc9f0b
fetched_at: '2026-06-28T22:39:20.492523+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - ICMS ST de operações
  de venda na coluna observações do Livro Fiscal - MATR930 '
type: support-article
updated_at: '2021-07-13T17:24:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000405161-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-ICMS-ST-de-opera%C3%A7%C3%B5es-de-venda-na-coluna-observa%C3%A7%C3%B5es-do-Livro-Fiscal-MATR930
---

**Dúvida**  
Como o contribuinte substituído faz para escriturar o valor do ICMS ST na coluna "Observações" do Livro de Saídas, em operações de devolução de venda?  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
  
Para que o valor do ICMS ST referente operações de venda possa ser gravado na coluna Observações do Livro Fiscal MATR930, será necessário efetuar as configurações conforme abaixo:   
  
Cadastro de TES (SF4)  
  
**Aba ADM/FIN/CUSTO**  
Cred. ICMS ST (F4\_CREDST) = 4  
  
**Aba Impostos**Solid Obs. F4\_OBSSOL = Não   
  
**Configurador**Parâmetro MV\_P1ICMSST = T
