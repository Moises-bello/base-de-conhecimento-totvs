---
content_hash: d832ea00e832eab222f3d092c04752206c24cc6fd8fdbbfb80e5c79c7a7186a7
fetched_at: '2026-06-29T00:08:20.615586+00:00'
page_id: '268579982'
product: rm
source: tdn-rm
title: DT_Pedido_Exames_Integração_PEP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268579982
version: 118
---

# Pedido de exames - Integração Prontuário Eletrônico do Paciente (PEP 2.0) e TOTVS Gestão Hospitalar

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Integração Prontuário Eletrônico do Paciente (PEP 2.0) e TOTVS Gestão Hospitalar / Pedidos de Exames | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server®/ Oracle® |
| **Tabelas Utilizadas:** | SZLABEXAME, SZPEDEXAMEITEM, SZUNIDATEND, SZATENDSADT |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Melhoria consiste na disponibilização do recurso de Integração de Pedidos de Exames entre o Prontuário Eletrônico do Paciente (PEP 2.0) e o TOTVS Gestão Hospitalar, quando há integração com sistema terceiros, como por exemplo, outros sistemas de laboratórios ou diagnósticos por imagem.

## Procedimento para Utilização

### **Parametrização da Unidade de Atendimento**

1. Acesse o menu **Cadastros / Uso Geral / Unidades de Atendimento**.
2. Selecione um registro de Unid. Atendimento\*.  
    

   \*Observação

   Para a correta parametrização, é necessário selecionar o registro da unidade de atendimento responsável pela realização do exame que será solicitado durante o processo de integração.
3. No grupo **Unidade de ...** marque a opção **Diagnóstico por imagem.**
4. No grupo **Integrações** selecione a integração na opção **Diagnóstico por Imagem.**
5. No grupo **Diagnóstico Imagem - Setores** marque todas as opções disponíveis.

* Integra PEP - Exames complementares.
* Integra atendimento interno.
* Integra atendimento externo

Observação

O mesmo processo é valido para parametrizar Unidades de Atendimento de Laboratório, fazendo-se necessário apenas utilizar as opções Laboratório ao invés de Diagnóstico por imagem.

### Solicitação de Pedido(s) de Exame(s) - Prontuário Eletrônico do Paciente (PEP 2.0)

1. Realize o seu login no Prontuário Eletrônico do Paciente (PEP 2.0).
   1. Preencha os campos **Usuário** e **Senha**,e clique em **Acessar**.
2. Selecione a Unidade de Atendimento desejada.
3. Em Prontuário Eletrônico selecione a opção **Prontuário Eletrônico do Paciente**.
4. Selecione um Paciente.
5. Solicite um ou mais exames que serão integrados posteriormente e clique em **Incluir**.
6. Libere a prescrição através do botão **Liberar Prescrição.**
7. Acesse o menu **Planejamento Terapêutico** e clique em **Libere o Aprazamento**.

### Verificação do Pedido Exame - TOTVS Gestão Hospitalar

1. Acesse o menu **Unidades de Diagnóstico / Controle de Pedidos de Exames.**
   1. Utilize o filtro desejado para encontrar os pedidos solicitados (ex.: pelo nome do paciente).
2. Será apresentada a tela onde é possível visualizar os pedidos de exames solicitados através da integração Prontuário Eletrônico do Paciente (PEP 2.0) e TOTVS Gestão Hospitalar.

divs
