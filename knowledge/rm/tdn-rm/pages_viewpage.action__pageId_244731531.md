---
content_hash: d6fba4ff4c8f5aebabc71346de15220737b240c7f0b7678c022d66a96ce4a24d
fetched_at: '2026-06-29T00:08:15.113747+00:00'
page_id: '244731531'
product: rm
source: tdn-rm
title: DT_Períodos_para_Cálculo_de_Data_Hora_Extraordinária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244731531
version: 115
---

# Períodos para Cálculo de Data Hora Extraordinária

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Registro de Atendimento Externo | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server®/ Oracle® |
| **Tabelas Utilizadas:** | SZPADRAOFATCODIFIC, SZATENDIMENTO |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Melhoria consiste na possibilidade de informar o horário inicial para cobrança de valores extras nos sábados, domingos e feriados. Além disso a funcionalidade permitirá atribuir porcentagens de valores extras de maneira individualizada para sábados, domingos e feriados.

## Procedimento para Utilização

## Padrões**de Faturamento e Codificação**

1. Acesse o menu **Cadastros** / **Faturamento** / **Padrões de Faturamento e Codificação**.
2. Selecione o Padrão de Faturamento que será utilizado na **Elaboração de Contas**.
3. Atribua o horário inicial e final para o período de hora extra e suas respectivas porcentagens de acréscimo de hora extra.  
     
     

   **Lançamento de Honorários pela Elaboração de Contas**
4. Acesse o **Lançamento na Conta de Paciente.**
5. Clique na **Pesquisa de Atendimento.**
6. Preencha ao menos um dos seguintes campos para pesquisar um atendimento URGENTE.
7. Pesquise o Atendimento, selecione o Atendimento e clique em **OK**.
   1. Código e/ou Nome e/ou Prontuário e/ou Cód do Atend  e/ou etc.
8. Lance dois honorários para o mesmo procedimento, onde um deles a data de realização deste estar fora da faixa de hora extra e o segundo deve estar dentro da faixa de hora extra. Assim o valor do procedimento dentro da faixa de hora extra deverá ter recebido o respectivo acréscimo configurado no passo 3.  
     
   **Lançamento de Honorários pelo Registro de Informações Cirúrgicas.**
9. É necessário com os passos 1, 2 e 3 configurados.
10. Acesse o menu **Cuidados com o Paciente / Centro Cirúrgico / Registro de Informações Cirúrgicas**.
11. Inclua dois **Registros de Informações Cirúrgicas** com o mesmo procedimento, onde um deles a data de realização deste estar fora da faixa de hora extra e o segundo deve estar dentro da faixa de hora extra.
12. Selecione cada um dos registros e em **Processos** clique em **Enviar Dados o Faturamento**.
13. Repita os passos 4, 5 e 6.
14. Assim na **Elaboração de Contas** o valor do procedimento dentro da faixa de hora extra deverá ter recebido o respectivo acréscimo configurado no passo 3.

divs
