---
article_id: 360036098973
category: FATURAMENTO - RELATÓRIOS
content_hash: 25a423cbdaf304c33a94e8c4f6c1bb193baba53da137a305ecfc0b4ab64c960c
fetched_at: '2026-06-28T22:38:23.013411+00:00'
product: protheus
section_id: 1500001539381
source: central-protheus
title: MP - FAT - Relatório Oportunidades x Processo de Vendas é alimentando campo
  de Vendedor Indevidamente
type: support-article
updated_at: '2021-04-28T15:15:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036098973-MP-FAT-Relat%C3%B3rio-Oportunidades-x-Processo-de-Vendas-%C3%A9-alimentando-campo-de-Vendedor-Indevidamente
---

**Ocorrência**

Relatório Oportunidades x Processo de Vendas é alimentando campo de Vendedor Indevidamente**.**

**Ambiente**

Protheus - A partir da versão 12.1.17.  
  
**Causa**

Quando acessa a busca **F3** no campo **Processo de Venda**, dos Parâmetros do relatório **CRMA450 - Oportunidades X Processos de Venda**, e selecionado o registro, é alimentado o campo **Vendedor**indevidamente. Isso ocorre devido ao uso da  consulta padrão utilizada no grupo de perguntas (**AC2**), para que ter o resultado esperado, verifique a possibilidade de alterar a consulta padrão atual para a consulta **AC1**.  
  
  
**Solução**

Alterar a consulta padrão, de **AC2** para **AC1**, da pergunta **Processo de Venda** contida nos parâmetros do relatório **FATR060**.

**IMPORTANTE !**

Não haverá a expedição de pacote de dicionário específico para a alteração dessa Consulta Padrão. A alteração automática da Consulta Padrão ocorrerá apenas na próxima **expedição oficial dos dicionários da release, prevista para Fevereiro/2020**. Caso necessite, a alteração da Consulta Padrão poderá ser realizada via Configurador (SIGACFG), conforme os procedimentos abaixo.

1. **Configurador** (**SIGACFG**) -> Clique em **Base de Dados ->**Clique em **Dicionário ->**Clique em **Base  -> de Dados->**Selecione a opção **Perguntas** e clique na Lupa:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047250853/mceclip0.png)

6. Busque por **FATR060** e clique no botão para editar:

![](https://tdn.totvs.com/download/attachments/515302009/image2019-9-17_16-35-15.png?version=1&modificationDate=1568750577273&api=v2)

Altere a consulta padrão **Consulta Padrão (Edit ) para AC1 - Processo de Venda -> Salve**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046389214/mceclip1.png)
