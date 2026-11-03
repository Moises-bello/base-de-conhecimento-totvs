---
content_hash: 1509e961adec58ec29ac52461afc1248d1b5fcceec9e8df1af529cd582878a43
fetched_at: '2026-06-29T00:09:52.990628+00:00'
page_id: '439707890'
product: rm
source: tdn-rm
title: DSAUGHCOM-906 DT Pedido de Exames - Cadastro de Exames
type: documentation
url: https://tdn.totvs.com/display/LRM/DSAUGHCOM-906+DT+Pedido+de+Exames+-+Cadastro+de+Exames
version: 3
---

# Pedido de Exames - Cadastro de Exames

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Exames | SauPedExameItemAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Pedido de Exame. | SauPedExameAction | |
| **Cadastros Iniciais:** | É necessário ter um Pedido de Exame cadastrado |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas Utilizadas:** | SZPEDEXAMEITEM, SZPEDEXAME |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Solicitação de exames para o pedido cadastrado para o atendimento do paciente.

## Procedimento para Utilização

* Acessar: Unidade de Diagnóstico \ Registro de Atendimento\ Pedido de Exames \ Aba Exames

* Também é possível acessar a tela através da tela do pedido na aba Exames

1. Para cadastrar um novo Pedido de Exame é necessário clicar no botão Incluir
2. Então abrirá a tela de cadastro do Exame   
     
   Para o realizar o cadastro é disponibilizado os seguintes campos:  
   Código do Exame (Obrigatório)  
   Tipo Exame - Normal; Urgência, Emergência (Obrigatório)  
   Material Biológico  
   Datas - Material Pendente; Data Coleta; Data Entrega; Hora da Entrega; Previsão de Execução  
   Local  
   Método  
   Médico Responsável  
   Com os campos acima preenchidos, clicar em Salvar,  é possível visualizar o registro salvo na aba de Exames:
3. Botão Instruções: Responsável por mostrar as instruções do exame selecionado.
4. **Cancelamento do Exame:** Com o Exame cadastrado, vá em Processos/Cancelar Exame
5. Informe o Motivo do cancelamento e clique em executar.
