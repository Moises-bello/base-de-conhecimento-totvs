---
content_hash: 5028d1da4d5a17644dfb4e3fc105d6eaebcc909536159fdcb3727d2a1d89b713
fetched_at: '2026-06-29T00:09:55.708825+00:00'
page_id: '450143307'
product: rm
source: tdn-rm
title: DSAUGHCOM-2128 DT Mudança de Leito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450143307
version: 2
---

# Mudança de Leito

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Mudança de Leito | SauProcBedTransferAction | |
| **Cadastros Iniciais:** | Cadastro de Leito, Registro de Atendimento (Interno). |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas Utilizadas:** | SZMUDANCALEITO |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Processo de Mudança de Leito.

## Procedimento para Utilização

Acesse a Mudança de Leitos através do menu **Atendimento / Outros Cadastros / Mudança de Leito**, ou através da action **SauProcBedTransferAction**.

1. Informe o **Paciente/Atendimento** que será transferido (obrigatório), o **Motivo da Transferência** (obrigatório), a **Data e a Hora da Transferência** (obrigatório), e o **Novo Leito** (obrigatório).  
  
  
  
  
2. Marque a opção de **Desocupar leito anterior?**caso queira que os leitos atualmente ocupados pelo paciente sejam desocupados. No caso de existir mais de um leito ocupado pelo paciente, será exibida uma lista com os leitos a serem desocupados, ficando a critério do usuário selecioná-los.  
  
  
  
  
3. Caso exista uma diferença na diária coberta pelo convênio e a diária do leito da transferência, será exibido uma lista com as diárias cobertas pelo convênio para que seja selecionado uma nova diária a ser utilizada como base para o cálculo dessa diferença. Será necessário também informar o **Responsável pela diferença** (obrigatório):  
  
  
  
  
4. Caso o paciente em processo de Mudança de Leito seja a **Mãe de um ou mais Recém Nascidos**, e estes estiverem no mesmo leito de sua mãe, será exibido uma lista para que sejam selecionados quais recém nascidos serão transferidos juntos com a mãe.  
  
  
  
  
5. Caso o paciente esteja acomodado em um leito do tipo **Centro Cirúrgico** e sendo transferido para outro tipo de leito, e o sistema estiver configurado com o parâmetro **Prescrições do Centro Cirúrgico só serão comandadas para o Local de Estoque de Atendimento após alocação do paciente em Unidade de Internação**, todas as Prescrições Médicas que ainda não foram encaminhadas a farmácia serão solicitadas para o **Local de Estoque** da nova localização do paciente.  
  
  
Após preencher todas as informações necessárias e **Executar** o processo, a transferência estará concluída. A transferência será registrada no **Histórico de Mudança de Leitos** deste Paciente/Atendimento (sendo possível consultá-lo através da tela inicial do processo de **Mudança de Leitos,**conforme a imagem inicial), e todas as informações referentes a localização do paciente (**Registro de Atendimento, Controle de Ocupação de Leitos, Cadastro de Leitos, e Cadastro de Recém Nascidos** (no caso do paciente ser um RN) serão atualizadas.
