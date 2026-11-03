---
content_hash: 219c24d46d97af0d6661de7508aeb110fad93cc1d203bfc0b0a4e979a754338a
fetched_at: '2026-06-29T00:06:19.419951+00:00'
page_id: '219697784'
product: rm
source: tdn-rm
title: DT_EXP#8_Uso_Geral
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=219697784
version: 5
---

# RM - Experiência 8 - Telas Uso Geral

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Uso Geral | |
| **Cadastros Iniciais:** | Motivos, Motivos de Exceção, Classificação de Autorização, Conselho Profissional, Tipo de acomodação, Status do agendamento, Especialidade, Faixa de Peso, Faixas Etárias, Tipos de indicação, Ação de Controle de Temperatura, Áreas com Controle de Temperatura, Grau de participação |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server |
| **Tabelas Utilizadas:** | SZMOTIVO, SZMOTIVOEXCECAOAGENDA, SZANSCLASSIFAUTORIZ, SZCONSPROF, SZTIPOACOMODACAO,  SZSTATUSAGENDAMENTO, SZESPECIALIDADE, SZFAIXAPESO, SZFAIXAETARIA, SZTIPOINDICACAO,  SZACAOTEMP, SZAREACONTROL, SZFUNCPRESTADOR |
| **Sistema(s) Operacional(is):** | Todos |
| **Versões/Release:** | 12.1.9 |

## Descrição

Foram reescritos os cadastros Motivos, Motivos de Exceção, Classificação de Autorização, Conselho Profissional, Tipo de acomodação, Status do agendamento, Especialidade, Faixa de Peso, Faixas Etárias, Tipos de indicação, Ação de Controle de Temperatura, Áreas com Controle de Temperatura, Grau de participação, visando adequar à experiência 8, que foi desenvolvida em cima do TOTVS HMTL Framework.

854480

## Procedimento para Implantação

 

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema (executáveis, dlls e arquivos de configuração):  
Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

* É necessário a instalação do TOTVS Gestão Hospitalar na versão 12.1.9.
* Instalação do fluig versão 1.5.2.

divs
