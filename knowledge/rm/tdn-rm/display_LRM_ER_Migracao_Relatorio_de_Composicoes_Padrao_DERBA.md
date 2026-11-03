---
content_hash: 0e56db70ae7bc440f0122aa8389ecf0291eaf4f2ef64e9f41d40d76a3ae9defd
fetched_at: '2026-06-29T00:06:02.105125+00:00'
page_id: '198943431'
product: rm
source: tdn-rm
title: ER_Migracao_Relatorio_de_Composicoes_Padrao_DERBA
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Migracao_Relatorio_de_Composicoes_Padrao_DERBA
version: 4
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOP(Totvs Obras e Projetos) |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP007 | **IRM1** | PCREQ-6011 |
| **Requisito1** | PCREQ-6012 | **Subtarefa1** | PDR\_CP\_TOP007-1377 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** | não |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 Migração do relatório padrão Derba da planilha eletrônica em Delphi, para a planilha eletrônica .NET

## Definição da Regra de Negócio

Com a mudança de plataforma Delphi para .Net, é necessário migrar o relatório Derba para a planilha eletrônica .Net.

* Serão listadas na tela de filtro as composições da coligada corrente, projeto corrente e que possuem o seguinte filtro:
  + Se for marcada a opção “Composição por pordução”:
    - Será filtrado todas as composições que possuem o campo "Produção por Hora" preenchido.
  + Se marcada a opção “Composição de preço unitário”:
    - Será filtrado todas as composições que não possuem o campo "Produção por Hora" preenchido, e do tipo CPU.

Após selecionar as composições (seleção obrigatória) e clicar  no botão “**Gerar**”, o relatório será enviado para impressora e/ou será gravado em formato Excel (dependendo da opção de filtro selecionado).

De acordo com a planilha selecionada, serão gerados relatórios (um para cada composição selecionada) de acordo com o padrão de planilha selecionada no componente de seleção de planilhas. Caso seja selecionada a opção de gerar no formato Excel, será gerada uma planilha com diversas abas (um para cada composição).

Ele está disponível da seguinte forma:

* No menu Relatórios -> Relatório padrão Derba.

**Restrição**

As planilhas do RM Solum cadastradas atualmente na ferramenta de planilhas Delphi deverão ser convertidas para a nova ferramenta de planilhas da RM.

## Protótipo de Tela

**Protótipo 01 : Formulário de Filtro**

****Protótipo 02 : Planilha Padrão Derba****

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
