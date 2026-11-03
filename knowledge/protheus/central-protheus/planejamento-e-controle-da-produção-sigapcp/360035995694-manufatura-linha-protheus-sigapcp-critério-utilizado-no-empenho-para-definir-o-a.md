---
article_id: 360035995694
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: a47545fbf86c444d6ed14e1351e85eaf7e6ab01a53181507626c9f182bb12da7
fetched_at: '2026-06-28T22:42:42.153269+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Critério utilizado no empenho para
  definir o armazém
type: support-article
updated_at: '2025-03-26T14:44:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035995694-Manufatura-Linha-Protheus-SIGAPCP-Crit%C3%A9rio-utilizado-no-empenho-para-definir-o-armaz%C3%A9m
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30937965844631)**Tempo aproximado para leitura: **00:01:34 min**  
 **Dúvida**Qual o critério utilizado no empenho para definir o armazém?  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**A rotina empenha no armazém padrão definido no **MATA010 - Cadastro de Produtos** ou na rotina **MATA018 - Indicadores de Produtos.** Para isso valida o conteúdo do parâmetro **MV\_ARQPROD - O parâmetro configura se os dados de indicadores de produto serão considerados pela tabela SB1 ou se serão considerados pela da tabela SBZ**.  
  
Além disso, para os produtos de apropriação indireta, que possuem o campo **B1\_APROPRI - Apropriação** definido como **Indireto** no **MATA010 - Cadastro de Produto**, será realizado o empenho no armazém de processo, que é definido no parâmetro **MV\_LOCPROC - Local padrão a ser enviado os materiais indiretos em processo.**  
Caso a rotina **MATA650 - Ordem de Produção** estiver parametrizado para já sugerir lote ou endereço, o empenho poderá ocorrer em outro armazém,  se o mesmo estiver quantidade disponível conforme a parametrização do **MATA650** na opção **F12**: **Consulta Somente Armazém Padrão**, **Considera do Armazém**, **Armazém Até**.  
  
**Importante**Somente os produtos de apropriação indireta serão empenhados no armazém de processo.
