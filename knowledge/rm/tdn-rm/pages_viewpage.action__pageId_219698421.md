---
content_hash: 6c047922ba2318a73f44434bfdc860c7161fe88e796daf0a1f4dcf4cc841a361
fetched_at: '2026-06-29T00:06:19.500357+00:00'
page_id: '219698421'
product: rm
source: tdn-rm
title: DT_EXP#8_Registro_e_Controle
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=219698421
version: 2
---

# RM - Experiência 8 - Telas Registro e Controle

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Registro e Controle | |
| **Cadastros Iniciais:** | Salas, Procedências, Religiões, Raça/Cor, Motivos de Cancelamento de Atendimentos, Motivos de Transferência de Leito |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server |
| **Tabelas Utilizadas:** | SZSALA, SZPROCEDENCIA, SZRELIGIAO, SZRACACOR, SZMOTIVOCANCELATEND, SZMOTIVOTRANSLEITO |
| **Sistema(s) Operacional(is):** | Todos |
| **Versões/Release:** | 12.1.9 |

## Descrição

Foram reescritos os cadastros Salas, Procedências, Religiões, Raça/Cor, Motivos de Cancelamento de Atendimentos, Motivos de Transferência de Leito, visando adequar à experiência 8, que foi desenvolvida em cima do TOTVS HMTL Framework.

854480

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema (executáveis, dlls e arquivos de configuração):  
Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

* É necessária a instalação do Totvs Gestão Hospitalar na versão 12.1.9.
* Instalação do fluig versão 1.5.2.

divs
