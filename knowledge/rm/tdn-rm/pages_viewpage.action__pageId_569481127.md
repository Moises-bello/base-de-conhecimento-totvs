---
content_hash: a5fd396fc38eada4fbaaaf83764e73f295441b897245bc3225aecce2f9ba032c
fetched_at: '2026-06-29T00:10:51.615486+00:00'
page_id: '569481127'
product: rm
source: tdn-rm
title: DT EAI 2.0 Geração de SA/SC
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=569481127
version: 10
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão de Estoque, Compras e Faturamento |
| Função: | Adapter Request versão 1.010 |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | MATESTCNTFTOF01-8735 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar solicitações de armazém para uma determinada Ordem de Serviço, o cliente deseja que os insumos que são produtos não estocáveis no BackOffice RM sejam gerados em outro tipo de movimento. O comportamento para solicitações de compra não foi alterado.

## **03. SOLUÇÃO**

Disponibilizado o parâmetro geral de integração com o módulo Manutenção de Ativos Protheus (SIGAMNT), nos parâmetros do Gestão de Estoque, Compras e Faturamento. Estes parâmetros ficarão disponíveis para configuração apenas quando existir integração ativa entre Manutenção de Ativos e BackOffice RM no EAI 2.0.

Melhoria no processo de geração de Solicitação de Armazém para insumos de Ordem de Serviço que são produtos não estocáveis na filial. Quando a coligada estiver parametrizada para gerar movimentos de produtos não estocáveis, no recebimento da mensagem Request versão 1.010 / Type 001 (Solicitação de Armazém) foi implementado a quebra dos itens (insumos) em movimentos com produtos estocáveis na filial e movimento com produtos não estocáveis na filial.

Parâmetros, Passo 02, Passo 03, Passo 04passo1yesParâmetros

Para realizar a configuração de gerar os movimentos para produtos não estocáveis realize os seguintes procedimentos:

1. Acesse o RM módulo BackOffice \ Gestão de Estoque, Compras e Faturamento
2. Acesse o menu Ambientes \ Parâmetros \ Gestão de Estoque, Compras e Faturamento e clique em Avançar
3. Na janela de Assistente de Implantação de Processos, selecione 04.03 - Integrações \ 04.03.06 - Manutenção de Ativos  (Protheus) e clique em avançar
4. Será apresentado a janela na Etapa Definições SigaMnt Protheus, onde será permitido realizar a configuração necessária.
5. Quando marcado o parâmetro "Gera movimento para produto não estocável", é obrigatório informar o tipo de movimento default.
6. Os movimentos a serem listados para seleção, devem estar parametrizado da seguinte forma:
   1. Série diferente da definida no movimento padrão (Parâmetros da Integração) para geração de Solicitações de Armazém (SA) e Solicitação de Compras (SC):
      1. Etapa 1 - Movimento - Identificação do movimento padrão de SA/SC.
      2. A consistência da série ser diferente é necessária porque o número da SA/SC é gerada pelo Protheus, se for utilizada a mesma série para ambos os movimentos iria ocorrer problemas de repetir a numeração já que ocorre a quebra da SA/SC somente no RM.
   2. Integrado com o SigaMNT:
      1. Etapa 67 - Manutenção.
   3. Mensagem de Integração igual a "Não Integrado":
      1. Etapa 78 - Integração Mensagem Única.
      2. O movimento não pode ter mensagem de integração com o SigaMnt porque este parâmetro é marcado somente quando o movimento do RM envia a mensagem para o Protheus. No caso da SA/SC o RM apenas recebe a mensagem.

No campo Movimento Gerado (Default) serão listados somente os tipos de movimentos que possuem integração com o SigaMNT e atendam os requisitos do item 6.

nopasso2

2. Use quando for necessário descrever um passo a passo.

## **04. DEMAIS INFORMAÇÕES**

Outras ações/ações relacionadas 

**Os parâmetros de integração com o Manutenção de Ativos Protheus ficarão disponíveis apenas quando existir integração ativa entre Manutenção de Ativos e BackOffice RM no EAI 2.0.IMPORTANTE!**

## **05. ASSUNTOS RELACIONADOS**


div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
.aui-tabs.horizontal-tabs>.tabs-menu>.menu-item.active-tab a::after {
background: #FF9900; !important
}
.menu-item.active-tab {
border-bottom: none !important;
}
]]>
