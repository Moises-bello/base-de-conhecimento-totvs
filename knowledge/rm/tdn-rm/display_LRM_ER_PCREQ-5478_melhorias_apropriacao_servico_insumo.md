---
content_hash: 5b01ee85f7f63006860fa76fc644b786f2f95bbcb5d2d59b052e1dc402b36d6a
fetched_at: '2026-06-29T00:06:12.193593+00:00'
page_id: '205914553'
product: rm
source: tdn-rm
title: ER_PCREQ-5478_melhorias_apropriacao_servico_insumo
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-5478_melhorias_apropriacao_servico_insumo
version: 2
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Apropriação |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP007 | **IRM1** |  |
| **Requisito1** | PCREQ-5478 | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** | Não |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Esta melhoria tem como objetivo permitir selecionar todos funcionários e terceirizados na apropriação de insumos do grupo DNIT “Mão de Obra” independente se a função dele não estiver entre as funções associadas ao insumo da apropriado, ou seja, a proposta desta melhoria consiste em permitir trazer todos os funcionário e terceiros do cadastro e não somente aqueles que tiverem a mesma função que não é aquela para a qual ele foi destinado. Esta flexibilidade ocorre atualmente para Equipamento por exemplo.

## Definição da Regra de Negócio

**Apropriação de Serviço/Insumo - Conceito**

 

A apropriação de insumos consiste na efetuação de registros diários do consumo (compra ou gasto) de insumos na obra, possibilitando um acompanhamento físico e financeiro da mesma através de um comparativo entre o previsto e o apropriado.A apropriação de insumos de mão de obra pode ser feita informando os funcionários ou tercerizados que executaram determinada atividade. Para isso é necessário integrar com RM Labore.

 

**Proposta de Melhoria**

 

**Conceito**

 

A melhoria trata-se de remover o filtro e consequentemente exibir todos os funcionários e terceirizados (pessoas) para associar em uma apropriação de insumo de mão de obra mesmo que a sua função não esteja associada no insumo. Atualmente são exibidos somente os funcionários e pessoas (terceirizados) onde sua função esteja em umas das funções associadas ao insumo selecionado na apropriação conforme fluxo de exemplo a seguir.

 

**Processo Atual**

 

1. Foi selecionado o insumo “F00100 – Pedreiro” que é de um grupo de custo de grupo DNIT “Mão de Obra” e possui a função “00027 - Pedreiro” associada a ele.
2. O campo “Cód. Funcionário”, “Cód. Funcionário Responsável” para Funcionário e “Cód. Pessoa”, “Cód. Pessoa Resposável” para Tercerizado ao lado direito da tela é habilitado para relacionar na apropriação.   
     
     

   OBS: Utilizaremos como exemplo o funcionário neste fluxo.
3. Ao abrir a tela para localizar o funcionário o sistema automaticamente exibe somente os funcionários que possuem a mesma função associada ao insumo selecionado

 

**Alteração no Processo**

A alteração que será implementa muda o processo a partir da listagem dos funcionários e terceirizados ([item 3](file:///C:/Docs_Proj/Roadmap_2013_2014/Construcao_e_Projetos/Projetos/R_TOP007/12.1.6/An%C3%A1lise/PCREQ-5478_MelhoriaNaApropriacaodeInsumos.docx#item3)), pois, serão exibidos todos os funcionários e pessoas independente da função conforme Protótipo 01.

**Impacto na versão Corpore.NET**

Corpore.NET: A mesma alteração será realizada na apropriação via CorporeRM, versão web do TOTVS Obras e Projetos, no Portal conforme Potótipo 02.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Apropriação de Serviços/Insumos | [Alteração] | Controle > Apropriação de Serviços/Insumos | - |

## Protótipo de Tela

**Protótipo 01**

****Protótipo 02****

******Protótipo 03******

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
