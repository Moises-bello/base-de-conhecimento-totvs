---
content_hash: 9b67d5a2ba6595e7a4088a3928f08a4fe79e2958266a372e58b582184c66c689
fetched_at: '2026-06-29T00:06:19.520259+00:00'
page_id: '219698592'
product: rm
source: tdn-rm
title: DT_EXP#8_Cuidados_Paciente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=219698592
version: 2
---

# RM - Experiência 8 - Cuidados com o Paciente

# Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Cuidados com o Paciente | |
| **Cadastros Iniciais:** | Vias de Administração de Medicamentos, Frequências de Administração de Medicamentos, Observações do Médico na Prescrição, Tipos de Cirurgia, Salas do Bloco Cirúrgico, Locais de Realização de Cirúrgias, Motivos de Suspensão de Cirurgias, Agentes Anestésicos, Status do Agendamento |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server |
| **Tabelas Utilizadas:** | SZAPLICPRESCMED, SZFreqPrescMed, SZOBSPRESCRICAO, SZTPCIRURGIA, SZSALABLOCOCIRURGICO, SZLOCALCIRURGIA, SZMOTIVOSUSPENSAO, SZAGANESTESICO, SZSTATUSAGENDAMENTO |
| **Sistema(s) Operacional(is):** | Todos |
| **Versões/Release:** | 12.1.9 |

## Descrição

Foram reescritos os cadastros Vias de Administração de Medicamentos, Frequências de Administração de Medicamentos, Observações do Médico na Prescrição, Tipos de Cirurgia, Salas do Bloco Cirúrgico, Locais de Realização de Cirurgias, Motivos de Suspensão de Cirurgias, Agentes Anestésicos, Status do Agendamento, visando adequar à experiência 8, que foi desenvolvida em cima do TOTVS HMTL Framework.

854480

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema (executáveis, dlls e arquivos de configuração):  
Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

* É necessária a instalação do Totvs Gestão Hospitalar na versão 12.1.9.
* Instalação do fluig versão 1.5.2.

divs
