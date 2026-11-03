---
article_id: 235301527
category: Gestão de Armazenagem (WMS)
content_hash: 585d424759591b3cf482e46923c82151daacd7af97339fca055bd5a65b9ed70f
fetched_at: '2026-06-28T22:45:47.982512+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - Cadastros básicos para a utilização do SIGAWMS
type: support-article
updated_at: '2024-01-30T00:07:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/235301527-Log%C3%ADstica-Linha-Protheus-WMS-Cadastros-b%C3%A1sicos-para-a-utiliza%C3%A7%C3%A3o-do-SIGAWMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Quais são os cadastros básicos necessários para a utilização do **SIGAWMS - Gestão de Armazenagem**?  
  
**Ambiente**  
TOTVS Logística - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (WMS) - Todas as versões.  
  
**Solução**Os cadastros básicos para utilização do **WMS *-* Warehouse Management System** - são:

1. **Unitizadores**: cadastrar as estruturas que comportam o produto, como: *pallet*, caixa, entre outras;
2. **Complemento de Produtos**: aba **WMS**. Para que ocorra o cadastro de complemento, o produto deve constar no castrado de **Produtos**;
3. **Tipos de Movimentação**: identifica as regras dos movimentos internos de materiais de requisição, de devolução e de produção;
4. **Locais de Estoque**: armazéns para controlar os saldos em estoque atualizados pela aquisição de material, movimentos internos de entrada e saída de produtos e por meio da venda da produção;
5. **Tipos de Entrada e Saída**: ou ainda **TES**, responsável pela correta classificação dos documentos fiscais de entrada e saída registrados no Sistema;
6. **Unidades de Medida:** são registradas todas as unidades de medida a serem utilizadas no Sistema.
7. **Recursos Humanos**: relacionar usuários a alguma função específica. Indivíduo responsável por um determinado tipo de atividade no armazém;
8. **Estruturas Físicas:** definição de estruturas de cada endereço: *picking*, pulmão, doca/box e *crossdoking*. São os locais internos de um armazém, ou seja, estruturas físicas de armazenamento, onde serão estocados os produtos;
9. **Endereços**: cadastrar os endereços conforme cada estrutura física. Trata da organização dos produtos dentro dos armazéns, determinando o lugar exato onde o produto é armazenado: prateleira, fila ou qualquer outro tipo de localização física;
10. **Sequência de Abastecimento**: definição de quais estruturas físicas cada produto poderá ser movimentado;
11. **Normas**: definição da capacidade dos unitizadores: lastro e camada;
12. **Tarefas x Atividades**: definição de quais atividades existirão para cada tarefa, além do relacionamento das funções de cada usuário;
13. **Serviços x Tarefas**: definição de quais tarefas farão parte do serviço e suas funções;

**Importante**  
O produto deve ser configurado para utilizar o controle de endereçamento, **B1\_LOCALIZ = Sim**.  
Para o novo **WMS**, além desta configuração acima, necessita também indicar na rotina **Complemento de Produtos** que controla endereçamento no **WMS**, **B5\_CTRWMS = Sim.**
