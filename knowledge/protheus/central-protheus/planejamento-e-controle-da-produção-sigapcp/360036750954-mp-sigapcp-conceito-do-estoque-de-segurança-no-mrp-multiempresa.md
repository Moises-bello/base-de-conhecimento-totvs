---
article_id: 360036750954
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 74dbf739b92952ccbfbc2cfe44eb6f42cb37fa9d937f401c4905fb8117719874
fetched_at: '2026-06-28T22:42:47.174268+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: MP - SIGAPCP - Conceito do estoque de segurança no MRP Multiempresa
type: support-article
updated_at: '2020-11-04T20:24:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036750954-MP-SIGAPCP-Conceito-do-estoque-de-seguran%C3%A7a-no-MRP-Multiempresa
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:40 min**  
 **Dúvida**Como o **PCPA107** considera o estoque de segurança no calculo da necessidade?  
   
 **Ambiente**Microsiga Protheus - Planejamento e Controle da Produção - Versão 12  
  
**Solução**Quando o parâmetro **MV\_ARQPROD** possui o conteúdo **SB1**, é gerada a necessidade referente ao estoque de segurança, considerando o valor do campo **B1\_ESTSEG** preenchido através da rotina **MATA010**, primeiramente para a unidade na qual o item possui estrutura, sendo o segundo critério a unidade na qual o item é componente da estrutura e por último a prioridade de cada unidade determinado na rotina **PCPA106**.  
  
Quando o parâmetro **MV\_ARQPROD** possui o conteúdo **SBZ**, o estoque de segurança considerado é o determinado através da rotina **MATA018** ou **MATA019 ,** através do campo **BZ\_ESTSEG**,para cada unidade. Se para alguma unidade não existir informação sobre o produto na rotina **MATA018** ou **MATA019,** a rotina considera para esta empresa o estoque de segurança informado no campo **B1\_ESTSEG** do item, determinado através do **MATA010**.  
Neste caso, o **PCPA107** pode apresentar diversas necessidades oriundas do estoque de segurança, sendo cada uma delas de uma empresa centralizada através do **PCPA106**.  
  
**Glossário****PCPA107** - MRP Multiempresa  
**MATA018** - Indicadores de Produtos  **MATA019** - Indicador Produto (Mod 2) **MATA010** - Cadastro de Produtos**PCPA106** - Empresa Centralizadora  
**B1\_ESTSEG** - Segurança  
**BZ\_ESTSEG** - Segurança  
**SB1** - Descrição Genérica do Produto   
**SBZ** - Indicadores de Produtos    
**MV\_ARQPROD** - O parâmetro configura se os dados de indicadores de produto serão considerados pela tabela SB1 ou se serão considerados pela da tabela SBZ
