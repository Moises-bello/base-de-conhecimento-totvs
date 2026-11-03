---
content_hash: 9b1acf52b85ac4893ca1930b6860841c34ee8e0bd6eeed28c22dd7ddb1711fb1
fetched_at: '2026-06-29T00:08:19.915521+00:00'
page_id: '267797977'
product: rm
source: tdn-rm
title: TTVSKB_DT_Inclusao_Campo_Nome_Social_Portal_Processo_Seletivo
type: documentation
url: https://tdn.totvs.com/display/LRM/TTVSKB_DT_Inclusao_Campo_Nome_Social_Portal_Processo_Seletivo
version: 116
---

# CADASTRO DE CANDIDATOS E RESPONSÁVEIS - PORTAL DO PROCESSO SELETIVO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **TOTVS Processo Seletivo - Portal** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cadastro de candidatos através do portal* | *N/A* | | *Cadastro de responsáveis *através do portal** | *N/A* | | *Dados pessoais *através do portal** | *N/A* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Inscrição de candidatos *através do portal** | *N/A* | |
| **Cadastros Iniciais:** | *Configuração dos parâmetros de dados pessoais para que seja definido se o campo nome social será visível e obrigatório para candidatos e responsáveis* |
| **Parâmetro(s):** | * + *Parâmetros do sistemas | Portal | Pessoa | Dados básicos | Candidato/Nome Social - Visível*   + *Parâmetros do sistemas | Portal | Pessoa | Dados básicos | Candidato/Nome Social - Obrigatório*   + *Parâmetros do sistemas | Portal | Pessoa | Dados básicos | Responsáveis/Nome Social - Visível*   + *Parâmetros do sistemas | Portal | Pessoa | Dados básicos | Responsáveis/Nome Social - Obrigatório* |
| **Ponto de Entrada:** | *Portal do processo seletivo:*   * *Portal do processo seletivo | Cadastro de candidato* * *Portal do processo seletivo | Cadastro de responsáveis* * *Portal do processo seletivo | Acesso usuário | Dados pessoais* |
| **Chamados Relacionados** | **N/A** |
| **Requisito (ISSUE):** | - |
| **País(es):** | - |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas Utilizadas:** | *PPESSOA* |
| **Sistema(s) Operacional(is):** | - |

## Descrição

Foi feito a inclusão do campo "nome social" no cadastro de candidatos e responsáveis no portal do processo seletivo, este campo já existe no cadastro de pessoa através da aplicação desktop, sendo assim foi feito a configuração do campo para que seja mostrado na tela conforme os parâmetros definidos do processo seletivo.

## Procedimento para Implantação

```
A exibição do campo 'nome social' no portal do processo seletivo estará disponível a partir da versão 12.1.14 sendo necessário ativar os parâmetros conforme necessidade.
```

**Observação**: por padrão o campo não será visível, será necessário habilitar nos parâmetros.

## Procedimento para Utilização

## Sistema

Configuração dos parâmetros que definem o campo como visível e obrigatório para candidatos e responsáveis:

### Portal do processo seletivo

Exibição do campo no portal do processo seletivo:

divs
