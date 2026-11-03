---
article_id: 360043260934
category: Chão de Fábrica (SIGASFC)
content_hash: eefb368545692b1b5bed62e6e5a97dc16d9cc01b0b01dddb9c56ef9f633ba32f
fetched_at: '2026-06-28T22:42:49.827712+00:00'
product: protheus
section_id: 360005696234
source: central-protheus
title: Manufatura - Linha Protheus - SIGASFC - Compartilhamento tabelas para implantação
  do SFC
type: support-article
updated_at: '2021-05-27T11:03:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043260934-Manufatura-Linha-Protheus-SIGASFC-Compartilhamento-tabelas-para-implanta%C3%A7%C3%A3o-do-SFC
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:02:00 min**  
**Dúvida**Quais tabelas é preciso corrigir o compartilhamento para implantação do **SFC - Chão de Fábrica**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Chão de Fábrica (SIGASFC) - Versão 12  
  
**Solução**As **Tabelas SFC** devem ser alteradas para que possuam o mesmo compartilhamento da sua **Tabela par**:

|  |  |
| --- | --- |
| **Tabela SFC** | **Tabela par** |
| **CY0 - Apontamento de Refugo** | **SC2 - Ordens de Produção** |
| **CY1 - Tabela Resultado** | **SC2** |
| **CY2 - Componente Tabela Resultado** | **SC2** |
| **CY3 - Indicador Filho** | **SC2** |
| **CY4 - Histórico Componente Máquina** | **SC2** |
| **CY5 - Meta Máquina** | **SC2** |
| **CY6 - Família** | **SX5 - Tabelas** |
| **CY7 - Grupo Estoque** | **SBM - Grupo de Produto** |
| **CY8 - Meta Indicador** | **SC2** |
| **CY9 - Operação da Ordem** | **SHY - Operações X Ordem APS** |
| **CYA - Área de Produção** | **SC2** |
| **CYB - Máquina** | **SH1 - Recursos** |
| **CYC - Máquina x Recurso** | **SC2** |
| **CYD - Pert das Operações da Ordem** | **SC2** |
| **CYE - Máquina x Item Controle** | **SC2** |
| **CYF - Turno Semana** | **SH7 - Calendário** |
| **CYG - Calendário Genérico** | **SH9 - Bloqueios e Exceções** |
| **CYH - Recurso** | **SH4 - Ferramentas** |
| **CYI - Centro de Trabalho** | **SHB - Centro de Trabalho** |
| **CYJ - Indicador** | **SC2** |
| **CYK - Item Controle** | **SC2** |
| **CYL - Máquina x Turno** | **SH1** |
| **CYM - Turno** | **SH7** |
| **CYN - Motivo Parada** | **SC2** |
| **CYO - Motivo Refugo** | **SC2** |
| **CYP - Componente da Ordem** | **SC2** |
| **CYQ - Ordem de Produção** | **SC2** |
| **CYR - Turno Dia** | **SH7** |
| **CYS - Componente da Meta Produção** | **SC2** |
| **CYT - Apontamento Item Controle** | **SC2** |
| **CYU - Meta Produção** | **SC2** |
| **CYV - Apontamento de Produção** | **SH6 - Movimentação da Produção** |
| **CYW - Apontamento de Mão-de-Obra** | **SC2** |
| **CYX - Apontamento Parada** | **SH6** |
| **CYY - Split da Operação Ordem** | **SC2** |
| **CYZ - Calendário** | **SH9** |
| **CZ0 - Apontamento Ferramenta** | **SC2** |
| **CZ1 - Equipe Operador** | **SC2** |
| **CZ2 - Manutenção Programada** | **SC2** |
| **CZ3 - Item** | **SB1 - Descrição Genérica do Produto** |
| **CZ4 - Dados Indicadores** | **SC2** |
| **CZ5 - Detalhes Gerenciamento** | **SC2** |
| **CZ6 - Apontamento Parada Mão-de-obra** | **SC2** |
| **CZ7 - Apontamento de Parada Geral** | **SC2** |
| **CZ8 - Dados Indicadores** | **SC2** |
| **CZ9 -Unidade de Medida** | **SAH - Unidade de Medida** |
| **CZA - Desenho** | **SG1 - Estruturas dos Produtos** |
| **CZP - Reservas Usadas** | **SD4 - Requisições Empenhadas** |
| **CZW - Apontamento GGF** | **SH6 -** |
| **CZX - Depósito** | **NNR - Locais de Estoque** |
