---
content_hash: c24ffde9a41c9b5efb38bed583b79b8f7a3b522f4380dcb12d3518351f6f66d0
fetched_at: '2026-06-29T00:08:10.733480+00:00'
page_id: '240978882'
product: rm
source: tdn-rm
title: DT_Revisão_dos_Tempos_de_Sala_e_Vínculo_Folha_de_Sala
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240978882
version: 113
---

# Revisão dos Tempos de Sala e Vínculo da Folha de Sala

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Registro de Informações Cirúrgicas | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server® / Oracle® |
| **Tabelas Utilizadas:** | SZREGINFCIRURGIA, SZREGINFCIRURGIAFOLHASALA |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Melhoria consiste na verificação e validação do vínculo entre o **Tempo de Sala**, o **Tempo de Anestesia** e o **Tempo de Cirurgia** dos **Registros de Informações Cirúrgicas**. A melhoria também engloba a funcionalidade de vincular a **Folha de Sala** automaticamente.

## Procedimento para Utilização

**Revisão dos tempos de Sala**

1. Acesse o menu **Cuidados com o Paciente** / **Registro de informações cirúrgicas**.
2. Utilize o botão **Incluir**.
3. Pesquise um paciente através do botão **Pesquisar**.
4. Preencha alguma informação para pesquisar um paciente (**Código ou Nome ou Prontuário**), selecione o **Paciente** e clique em **OK**.
5. Preencha os campos obrigatórios da aba I**dentificação**:
   1. **Tipo de cirurgia**
   2. **Local de realização**
   3. **Sala; Porte de Sala**
   4. **Tempo de Cirurgia**
6. A funcionalidade **Revisão dos Tempos de Sala** é acionada de acordo com os seguintes cenários:
   1. Tempo de Sala **menor** do que o Tempo de Cirurgia.
   2. Tempo de Anestesia **menor** do que o Tempo Cirurgia.

Observação

O processo é o mesmo para edição de registros.

**Vínculo de Folha de Sala**

1. A funcionalidade Vínculo de Folha de Sala é acionada quando atende os seguintes requisitos:
   1. Ter pelo menos um Tipo de Movimentação de Estoque do tipo Folha de Sala  
       Menu **Opções** / **Parâmetros** / **Integração RM Nucleus** / Aba **Tipos de Mov. Estoque**
   2. Ter pelo menos uma Movimentação de Estoque para o paciente que será utilizado.              Menu **Estoque** / **Movimentação de****Estoque**
2. Acesse o menu **Cuidados com o Paciente** / **Registro de informações cirúrgicas**.
3. Utilize o botão **Incluir**.
4. Pesquise um paciente através do botão **Pesquisar**.
5. Preencha alguma informação para pesquisar um paciente (**Código ou Nome ou Prontuário**), selecione o **Paciente**  e clique em **OK**.
6. Preencha os campos obrigatórios da aba I**dentificação**:
   1. **Tipo de cirurgia**
   2. **Local de realização**
   3. **Sala; Porte de Sala**
   4. **Tempo de Cirurgia**
7. Se o registro salvo atender aos requisitos do **item** **1**, na aba **Folha de Sala** o vínculo será realizado **automaticamente** ao **salvar** o registro.

Observação

O processo é o mesmo para edição de registros.

divs
