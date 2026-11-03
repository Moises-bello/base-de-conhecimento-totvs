---
content_hash: 67637e203b2a1a4507bb0293db3510dcb822dea542e5d062069b2590743102ac
fetched_at: '2026-06-29T00:06:19.557060+00:00'
page_id: '219698938'
product: rm
source: tdn-rm
title: DT_EXP#8_Estoque
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=219698938
version: 2
---

# RM - Experiência 8 - Estoque

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Estoque | |
| **Cadastros Iniciais:** | Classificação Terapêutica, Laboratórios Brasíndice, Apresentações Brasíndice, Classificação de Medicamentos Controlados, Classificação DCB |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server |
| **Tabelas Utilizadas:** | SZCLASTERA, SZCadLaboratorio, SZCadApresentacao, SZSUBSTANCIA, SZDCB |
| **Sistema(s) Operacional(is):** | Todos |
| **Versões/Release:** | 12.1.9 |

## Descrição

Foram reescritos os cadastros Classificação Terapêutica, Laboratórios Brasíndice, Apresentações Brasíndice, Classificação de Medicamentos Controlados, Classificação DCB, visando adequar a experiência 8, que foi desenvolvida em cima do TOTVS HMTL Framework.

854480

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema (executáveis, dlls e arquivos de configuração):  
Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

* É necessária a instalação do Totvs Gestão Hospitalar na versão 12.1.9.
* Instalação do fluig versão 1.5.2.

divs
