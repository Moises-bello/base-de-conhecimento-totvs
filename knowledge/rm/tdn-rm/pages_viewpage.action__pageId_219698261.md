---
content_hash: 92928996573f5cb941e0716898f9174b38174fcd9645c872b6f65d7d2d520d7e
fetched_at: '2026-06-29T00:06:19.484909+00:00'
page_id: '219698261'
product: rm
source: tdn-rm
title: DT_EXP#8_Unidades_Diagnóstico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=219698261
version: 4
---

# RM - Experiência 8 - Telas de Unidades de Diagnósticos

# Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Unidades de Diagnóstico | |
| **Cadastros Iniciais:** | Preparações de Exames, Padrões de Medidas para Exames, Tubos e Recipientes, Locais de Execução Externa, Informações Complementares, Tipos de Exceção, Método de Exame, Mensagem de Pedido de Exame, Mensagens do Rodapé de Resultados, Agentes de Coleta. |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server |
| **Tabelas Utilizadas:** | SZLABPREPARACAO, SZLABUNIDADE, SZLABTIPOVASILHAME, SZLABLOCEXECEXTERNA, SZINFCOMPEXAME, SZTIPOEXCECAO, SZMETODOSEXAMES, SZLABMSGPEDEXAME, SZMSGRODAPERESULT, SZAGENTECOLETA |
| **Sistema(s) Operacional(is):** | Todos*.* |
| **Versões/Release:** | 12.1.9 |

## Descrição

Foram reescritos os cadastros, Preparações de Exames, Padrões de Medidas para Exames, Tubos e Recipientes, Locais de Execução Externa, Informações Complementares, Tipos de Exceção, Método de Exame, Mensagem de Pedido de Exame, Mensagens do Rodapé de Resultados, Agentes de Coleta, visando adequar à experiência 8, que foi desenvolvida em cima do TOTVS HMTL Framework.

854480

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema (executáveis, dlls e arquivos de configuração):  
Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

* É necessária a instalação do Totvs Gestão Hospitalar na versão 12.1.9.
* Instalação do fluig versão 1.5.2.

divs
