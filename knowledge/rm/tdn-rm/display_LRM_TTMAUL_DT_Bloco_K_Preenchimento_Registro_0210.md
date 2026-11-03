---
content_hash: 8c1819c11bdf38c6ffd19aae288090e8ab9e3368029534c40e3cb702fa77c051
fetched_at: '2026-06-29T00:06:16.333333+00:00'
page_id: '212896176'
product: rm
source: tdn-rm
title: TTMAUL_DT_Bloco_K_Preenchimento_Registro_0210
type: documentation
url: https://tdn.totvs.com/display/LRM/TTMAUL_DT_Bloco_K_Preenchimento_Registro_0210
version: 3
---

# BLOCO K - PREENCHIMENTO DO REGISTRO 0210

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | ***Gestão de Estoque Compras Faturamento*** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *LI.01.0036* | *OBRIGAÇÕES ACESSÓRIAS - SPED FISCAL* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *PCP.44.272* | *COMPOSICAO DE ESTRUTURAS* | | *PCP.44.241* | *ESTRUTURA* | |
| **Cadastros Iniciais:** | *Não se aplica.* |
| **Parâmetro(s):** | *Não se aplica.* |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Chamados relacionados** | *Não se aplica.* |
| **Requisito (ISSUE):** | *Não se aplica.* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *Não se aplica.* |
| **Tabelas utilizadas:** | **KEstrutura, KComponente** |
| **Sistema(s) operacional(is):** | *Não se aplica.* |
| **Versões/Release:** | *11.82.42, 12.1.8 ou superior* |

## Descrição

Disponibilização do campo "PercentualPerda" no cadastro de Componentes da Estrutura, sendo o valor default igual a ZERO.

Necessário edição dos cadastros para informar o real valor percentual da perda do componente/insumo, quando houver, para se produzir uma unidade de produto resultante.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *11.82.42, 12.1.8 ou superior* deste chamado.

## Procedimento para Utilização

*Produção Simples:*

No módulo "Gestão de Estoque, Compras e Faturamento", aba "Estoque > Produção > Componentes", escolha o filtro desejado e edite o(s) registro(s) necessários informando no campo "Percentual de Perda" o valor correspondente, quando for pertinente.

*Planejamento e Controle de Produção (RMFactor):*

No módulo "Planejamento e Controle de Produção", menu "Cadastros > Engenharia > Estruturas", escolha o filtro desejado e edite a(s) estrutura(s) necessárias, acesse a pasta "Componentes" e edite o(s) componente(s) desejados informando no campo "Percentual de Perda" o valor correspondente, quando for pertinente.

***ATENÇÃO:*** O campo "Percentual de Perda" é meramente informativo para o devido preenchimento do respectivo campo "PERDA" no Registro 0210 ao gerar o SPED (Bloco K).
