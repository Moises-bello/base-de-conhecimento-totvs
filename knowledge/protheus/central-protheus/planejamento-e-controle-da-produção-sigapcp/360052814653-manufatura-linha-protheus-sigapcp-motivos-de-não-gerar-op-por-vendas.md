---
article_id: 360052814653
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: c807ae7b554e73b652bbd9693b1c418684856087aa90b8898634eba79d2d53c6
fetched_at: '2026-06-28T22:42:44.560733+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Motivos de não gerar OP por Vendas
type: support-article
updated_at: '2023-12-19T18:06:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052814653-Manufatura-Linha-Protheus-SIGAPCP-Motivos-de-n%C3%A3o-gerar-OP-por-Vendas
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:55 min**  
**Dúvida**Quais as situações em que a **OP - Ordem de Produção** não é gerada pela opção de **Vendas**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**A **OP** não é gerada por **Vendas** quando:

* A **TES - Tipo de entrada e saída** não está configurado para atualizar estoque.
* O parâmetro **MV\_CONSEST - Considera Estoque na Geracao de Ordem de Producao?** está como **S** e o Sistema identifica a existência de estoque em quantidade suficiente para atender a necessidade, neste caso o campo **C6\_OP - OP Gerada**fica preenchido com **05.**
* O parâmetro **Considera Qtd Liberada PV?** está com o conteúdo **Sim** e não há quantidade liberada na tabela **SC9 - Pedidos Liberados.**

**Saiba mais**  
Para mais informações referente as opções que o campo **C6\_OP** pode ter, acesse a documentação [MP-FAT-Quais conteúdos o campo C6\_OP pode ter](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115013175268-MP-FAT-Quais-conte%C3%BAdos-o-campo-C6-OP-pode-ter)
