---
article_id: 360040276633
category: Desenvolvedor de Produtos (SIGADPR)
content_hash: 11e1aae25ae9974728525f4d1c3e25638fd661de26222cf3526f53b26d338c44
fetched_at: '2026-06-28T22:42:48.741065+00:00'
product: protheus
section_id: 360005696254
source: central-protheus
title: Manufatura - Linha Protheus - SIGADPR - Compartilhamento correto das tabelas
  DPR
type: support-article
updated_at: '2021-09-20T11:43:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040276633-Manufatura-Linha-Protheus-SIGADPR-Compartilhamento-correto-das-tabelas-DPR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:40 min****Dúvida**Para implantação do **Desenvolvedor de Produtos**, qual é o compartilhamento correto das tabelas **DPR - Desenvolvedor de Produtos**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Desenvolvedor de Produto (SIGADPR) - Versão 12  
  
**Solução**As tabelas **DPR** devem ser alteradas para que possuam o mesmo compartilhamento da sua tabela par.

|  |  |
| --- | --- |
| **Tabela DPR** | **Tabela Par** |
| **DG0 - Versão Produto** | **SG1 - Estruturas de produtos** |
| **DG1 - Estrutura Produto** | **SG1** |
| **DG2 - Alternativos Operação** | **SG1** |
| **DG3 - Produto Desenvolvido** | **SB1- Descrição Genérica do Produto** |
| **DG4 - Componente Alternativo** | **SG1** |
| **DG5 - Custo da Versão** | **SG1** |
| **DG6 - Narrativa Desenvolvedor Produto** | **SG1** |
| **DG7 - Operação Alternativa Versão** | **SG1** |
| **DG8 - Consumível Operação** | **SG1** |
| **DG9 - Operação Produto** | **SG1** |
| **DGA - Preço do Produto Concorrente** | **SG1** |
| **DGB - Atributo Extra** | **SG1** |
| **DGC - Pendência Desenvolvimento** | **SC5 - Pedidos de Venda** |
| **DGD - Rede Pert de Operações** | **SG1** |
| **DGE - Critério Ou Qualidade Percebid** | **SG1** |
| **DGF - Peso do Critério no valor do P** | **SG1** |
| **DGG - Lista Atribuídos Extras Versão** | **SG1** |
| **DGH - Ordem Protótipo** | **SC2 - Ordens de Produção** |
| **DGI - Valor Critério Concorrente** | **SG1** |
| **DGJ - Valor Critério** | **SG1** |
| **DGK - Lista Atribuídos Extras Produto** | **SG1** |
| **DGL - Hist. Mudança Situação Versão** | **SG1** |
| **DGM - Desenho Produto Desenvolvido** | **SG1** |
| **DGN - Ficha Técnica** | **SG1** |
| **DGO - Atributo Ficha Técnica** | **SG1** |
| **DGP - Pendência Versão** | **SC5** |
| **CYB - Máquina** | **SH1 - Recursos** |
| **CYH - Recurso** | **SH4 - Ferramentas** |
| **CYI - Centro de Trabalho** | **SHB - Centro de Trabalho** |
| **CZ3 - Item** | **SB1** |
| **CY6 - Família** | **SX5 - Tabelas** |
| **CY7 - Grupo Estoque** | **SBM - Grupo de Produto** |
| **CZ9 - Unidade Medida** | **SAH - Unidade de Medida** |
| **CZX - Depósito** | **NNR - Locais de Estoque** |
| **CZA - Desenho** | **SG1** |
