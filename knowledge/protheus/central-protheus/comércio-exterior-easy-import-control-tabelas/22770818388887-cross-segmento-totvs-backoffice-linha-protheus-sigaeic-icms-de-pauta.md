---
article_id: 22770818388887
category: Comércio Exterior - Easy Import Control - Tabelas
content_hash: 1d13dabb8d98b091c623b6eaa95405100b9444158072e11301506c36e2c89c47
fetched_at: '2026-06-28T22:39:47.760418+00:00'
product: protheus
section_id: 1500001549562
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - ICMS de Pauta
type: support-article
updated_at: '2024-04-16T12:08:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22770818388887-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-ICMS-de-Pauta
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22770818365975) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como faço para montar um processo onde tem ICMS de pauta no SIGAEIC?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Import Control* – Todas versões  
  
  
**Solução**

Serão necessários os seguintes procedimentos:  
1. Acessar a rotina CFO (Atualizações > Tabelas > CFO - **EICOP100**), incluir/ configurar ou incluir uma operação através do campo "**Tp.Paut.ICMS**" (WZ\_TPPICMS) para efetuar o cálculo do ICMS pelo peso (opção 1- Peso) ou pela quantidade do item (opção 2-Quantidade).

![ICMS PAUTA 1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22770818367895)   
2. Acessar o cadastro de produtos (Atualizações > Cadastros > Produtos - **MATA010**) selecione o produto importado em modo de alteração e na pasta "Impostos" informe o valor do ICMS de pauta do produto em questão no campo "**ICMS Pauta**" (B1\_VLR\_ICM).

![ICMS PAUTA 2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22770791377431)   
3. Depois que o processo estiver com Purchase Order, Embarque/Desembraço criados é só acessar a rotina Apropriação de CFO (**EICOP110**), selecione o embarque e informar a operação cadastrada do ICMS de pauta.  
4. Para pesquisar se o valor está correto é só acessar a rotina de Recebimento de importação (**EICDI154**) na opção itens na coluna ICMS a Recolher, o(s) valor(es) será(ão) exibido(s).
