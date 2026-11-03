---
content_hash: 42310f6d5fd0908a5ca00049128508dc08a95fd19f99aa22faed36cb7dec9325
fetched_at: '2026-06-29T00:10:27.554206+00:00'
page_id: '516622639'
product: rm
source: tdn-rm
title: Importação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=516622639
version: 14
---

## 

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Importação por View**
4. **Importação por Arquivo Texto**
5. **Log de importação**
6. **Agregação/Validação**
   1. **Motivo de Óbito**
   2. **Cirurgia**
   3. **Antibiótico**
   4. **Validação de Importação de Antibiótico**
   5. **Validação de Consumo de Antibiótico**
   6. **Cultura Final**
7. **Dados gerados na importação**
8. **Exemplos para criação de Views integrado com o ERP TOTVS Gestão Hospitalar**
9. **Possíveis Problemas e Soluções**

sumarioVisão Geral

## **01. VISÃO GERAL**

**O que é a funcionalidade Importação?**

Este módulo é responsável pela importação de Dados do Sistema Hospitalar. A importação de dados tem como objetivo salvar no banco de dados do TOTVS CIH as informações pertinentes aos pacientes no período desejado.  
O sistema tem a capacidade de importar pacientes, suas internações, cirurgias, resultados de cultura, consumo de antibiótico, procedimentos Invasivos, procedimentos Cirúrgicos e CID de internação. Os dados importados podem ser de pacientes **internados ou ambulatoriais**.

Como realizar a Importação Via View?

Nesta importação, o TOTVS CIH utiliza uma string de conexão para acesso à base do sistema da instituição para fazer a leitura das views. Esta conexão pode ser feita com os SGBDs SQL Server e Oracle ou qualquer SGBD que pode ser acessado via ODBC ou OLEDB.

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Saúde > controle de infecção hospitalar > utilitários > importação

Importação por View

## **03. IMPORTAÇÃO POR VIEW**

| Ação | Descrição |
| --- | --- |
| Procedimento para inclusão | 1. No **TOTVS Controle de Infecção** acesse **Utilitários/Importação**, 2. Selecione o tipo de importação (Internação e alta, Movimentação de Leitos, Procedimento Invasivo, Cirurgia, Antibiótico, Cultura Final, Cultura Parcial ou CID). 3. Acesse a guia **Importação**. 4. Marque a opção **Importação por view**. 5. Para importação por período marque a opção correspondente e informe o período. 6. Para importação recorrente marque a opção correspondente e informe a defasagem e o número de dias. 7. No botão **Configurar Conexão** é selecionado o modo como a conexão é feita: com os SGBDs SQL Server e Oracle ou qualquer SGBD que pode ser acessado via ODBC ou OLEDB. |

03.01 Configuar Conexão

### **03.01 CONFIGURAR CONEXÃO**

Para configurar a string de conexão, preencha os campos contendo: Provider para o tipo de banco de dados, servidor do banco de dados, nome da base de dados, login e senha para conectar no banco.

### **SQL SERVER**

### **ORACLE**

1. pós a configuração clique em **OK**.
2. Na tela de Importação **Salvar Configurações** e em seguida clique em **Importar**.

Importação por Arquivo Texto

## **04. IMPORTAÇÃO VIA ARQUIVO TEXTO**

**Como realizar a Importação Via Arquivo de Texto?**

1. Deve ser informado o arquivo que contém os registros a serem importados.
2. No **TOTVS Controle de Infecção** acesse **Utilitários/Importação**,
3. Selecione o tipo de importação (Internação e alta, Movimentação de Leitos, Procedimento Invasivo, Cirurgia, Antibiótico, Cultura Final, Cultura Parcial ou CID).
4. Acesse a guia **Importação**.

1. Marque a opção **Importação por Arquivo Texto (.dat)**.
2. Clique em "**...**".
3. Será exibida a tela para seleção da pasta.

1. Selecione a pasta e clique em **OK**.

Log de importação

## **05. LOG DE IMPORTAÇÃO**

O que é o Log de Importação?

Ao final da importação é gerado um log para análise da equipe do SCIH, esta, deve acertar os possíveis erros, seja por inconsistência da base do sistema da instituição ou da base do TOTVS Gestão Hospitalar. As entradas de log são simples para que seja fácil sua leitura e acerto. Para minimizar as entradas de log o sistema deve estar alinhado com a base dos sistemas da instituição.

Há dois tipos de entradas de log:

* **Aviso**: O registro é importado parcialmente.
* **Erro**: O registro não é importado.

Como acessar os Logs de Importação?

1. Para visualizar o log gerado com a importação no TOTVS Controle de Infecção Hospitalar acesse Utilitários/Importação.
2. Selecione o tipo de importação (Internação e alta, Movimentação de Leitos, Procedimento Invasivo, Cirurgia, Antibiótico, Cultura Final ou CID).
3. Clique na guia **Log Usuário.**
4. Selecione a importação referente ao log que deseja visualizar.

1. Clique na guia **Log Técnico.**
2. Utilize o filtro para selecionar o tipo de log que deseja visualizar: Erros, Avisos ou Sucessos.

Agregação/Validação

## **06. AGREGAÇÃO/VALIDAÇÃO**

O que é e como realizar a Agregação/Validação?

Os dados importados devem ser validados pela equipe do SCIH. Nesta validação devem ser conferidos os dados trazidos pela importação e agregados os dados que extrapolam o escopo da importação.

Motivo de Óbito 

## **a.****MOTIVO DE ÓBITO**

Utilitários/Agregação/ Validação/Motivo de Óbito.

1. Na tela de **Motivo Óbito Pendentes** clique em **Exportar**.
2. Selecione o formato do arquivo que será gerado.
3. Será exibido o Assistente de Exportação.
4. Clique em **Avançar.**
5. Selecione o destino da exportação e clique em **Avançar**.
6. Caso seja selecionado o disco local para exportação, selecione o local para armazenagem no arquivo e clique em **Salvar**.
7. Após a importação do arquivo verifique o resultado, acertando as entradas de *log*, caso necessário.
Cirurgia

## **b.****CIRURGIA**

Utilitários/Agregação/ Validação/Cirurgia.

1. Na tela de **Validação de Importação de Cirurgia** clique em **Exportar**.
2. Selecione o formato do arquivo que será gerado.
3. Será exibido o Assistente de Exportação.
4. Clique em **Avançar.**
5. Selecione o destino da exportação e clique em Avançar.
6. Caso seja selecionado o disco local para exportação, selecione o local para armazenagem no arquivo e clique em **Salvar.**
7. Após a importação do arquivo (cirurgia.txt) verifique o resultado, acertando as entradas de *log*, caso ocorram.

**Importante:****Ao validar a cirurgia importada é necessário informar à qual procedimento NHSN corresponde o procedimento importado, que é baseado nas tabelas de faturamento dos convênios. Esta associação é feita apenas uma vez para cada procedimento de cada tabela.**

Antibiótico

## **c.****ANTIBIÓTICO**

A importação de antibiótico é validada em dois momentos diferentes:

* **Validação Inicial**: É o momento da validação dos dados da prescrição.
* **Fechamento de Consumo:** É o momento da validação das dispensações importadas, neste momento devem ser informadas a dose total consumida de cada antibiótico e sua data fim.
Validação de Importação de Antibiótico

## **d.****VALIDAÇÃO DE IMPORTAÇÃO DE ANTIBIÓTICO**

1. Na tela de **Validação de Importação de Antibiótico** clique em **Exportar**.
2. Selecione o formato do arquivo que será gerado.
3. Será exibido o Assistente de Exportação.
4. Clique em **Avançar.**
5. Selecione o destino da exportação e clique em **Avançar**.
6. Caso seja selecionado o disco local para exportação, selecione o local para armazenagem no arquivo e clique em **Salvar**.
7. Após a importação do arquivo verifique o resultado, acertando as entradas de *log*, caso ocorram.
Validação de Consumo de Antibiótico

## **e.****VALIDAÇÃO DE CONSUMO DE ANTIBIÓTICO**

1. No **TOTVS Controle de Infecção** acesse o menu **Utilitários/Agregação/ Validação/Antibiótico/Cabeçalho**.
2. Na tela de **Validação de Consumo de Antibiótico** clique em **Exportar**.
3. Selecione o formato do arquivo que será gerado.
4. Será exibido o Assistente de Exportação.
5. Clique em **Avançar.**
6. Selecione o destino da exportação e clique em **Avançar**.
7. Caso seja selecionado o disco local para exportação, selecione o local para armazenagem no arquivo e clique em **Salvar**.
8. Após a importação do arquivo verifique o resultado, acertando as entradas de *log*, caso ocorram.

Cultura Final

## **f.****CULTURA FINAL**

1. No **TOTVS Controle de Infecção** acesse o menu **Utilitários/Agregação/ Validação/Cultura Final**.
2. Na tela de **Validação de Importação de Cultura Final** clique em **Exportar**.
3. Selecione o formato do arquivo que será gerado.
4. Será exibido o Assistente de Exportação.
5. Clique em **Avançar.**
6. Selecione o destino da exportação e clique em **Avançar**.
7. Caso seja selecionado o disco local para exportação, selecione o local para armazenagem no arquivo e clique em **Salvar**.
8. Após a importação do arquivo verifique o resultado, acertando as entradas de log, caso ocorram.
Dados gerados na importação 

## **07****DADOS GERADOS NA IMPORTAÇÃO**

Quais são os dados gerados na Importação?

Importação de Internação e Alta

**Importação de Internação e Alta**

**A importação de internação e alta gera dados para os itens de paciente com dados de cadastro, data e hora de internação e alta.**Importação de Movimentação de Leitos

A importação de movimentação se destina a busca de dados de movimentações de leitos e unidade de internação com data e hora.  
Para importar a movimentação de leito é necessário que o paciente esteja registrado na base.   
Porém antes de realizar a importação da movimentação terá que ser definido o "DE - PARA" entre o sistema de origem e o Controle de Infecção Hospitalar na tela de Cadastro/Unidade Clínica.  
Caso não exista uma unidade de internação cadastrada, o sistema irá criar uma "UNID. TEMPORÁRIA" para validação do cliente depois de feita a importação da movimentação.  
Se não existir a data de saída, o importador, irá fechar automaticamente a data de saída de acordo com a data de entrada da próxima movimentação.  
Caso o usuário não possa realizar esta integração eletrônica ou não tiver no seu sistema de origem este tipo de informação, é possível realizar e inserção manual dessas informações para geração das taxas de infecções por procedimentos.

Importação de Procedimento Invasivo

### Importação de Procedimento Invasivo

A importação de procedimento invasivo gera dados como passagem de cateteres, ventilação mecânica ou outros procedimentos que estejam cadastrados na base do TOTVS CIH para monitoramento do SCIH.

Importação de Cirurgia

### Importação de Cirurgia

A importação de cirurgia gera os seguintes dados: os procedimentos realizados com seus dados de equipe médica, tempo cirúrgico e ASA. Para importar a cirurgia é necessário que o paciente esteja registrado na base.

Importação de Antibiótico

### Importação de Antibiótico

Para importação de antibiótico é necessário que o paciente esteja registrado na base. A importação de antibiótico não abrange o tipo de profilaxia e os sítios de infecção. A data fim de cada antibiótico e seu consumo final deve ser informado na validação de fechamento de consumo, traz as dispensações realizadas.  
Na importação do antibiótico o sistema grava as informações do sitio secundário, porém, para isso deve-se cadastrar no sitio secundário o código do cliente.

Importação de Cultura Final

### Importação de Cultura Final

A importação de cultura final gera dados de resultados de cultura com seus germes e antibiograma.   
Para esta importação, é necessário que o paciente esteja registrado na base. A importação de cultura final não abrange a relevância clínica do resultado de cultura, o tipo e o sítio de infecção.

Importação de Cultura Parcial

### Importação de Cultura Parcial

A importação de cultura parcial, realizado o acompanhamento dos exames laboratoriais, coletados no período de internação do paciente na instituição desde a coleta do material até seu resultado. Nas atualizações é possível fazer o acompanhamento do crescimento bacteriano no material colhido.   
O registro só será importado, nas seguintes condições:

1. O paciente esteja internado e o registro a importar, esteja com a data da coleta igual a mesma data da internação ou da alta.
2. Quando o registro estiver com a data da coleta maior que data da internação e menor que a data da alta.
Exemplos para criação de Views integrado com o ERP TOTVS Gestão Hospitalar 

## **08** **EXEMPLOS PARA CRIAÇÃO DE VIEWS INTEGRADO COM O ERP TOTVS GESTÃO HOSPITALAR**

As Views RMV\_CULTURA, RMV\_CULTURA\_PARCIAL, RMV\_GERMES, RMV\_ANTIBIOGRAMA são informações de Laboratórios terceirizados (que não usa sistema Totvs), portanto devem ser criadas pelo Laboratório, que fornecerá as informações para preenchimento seguindo o layout citado.

Layout para criação de views: [https://tdn.totvs.com/x/tmOgJg](https://tdn.totvs.com/x/tmOgJg "Follow link")

Para as demais View, já são criadas com os dados do Totvs Gestão Hospitalar.

RMV\_ANTIBIOTICO  
RMV\_CID  
RMV\_CIRURGIA  
RMV\_CIRURGIOES  
RMV\_INTERALTA  
RMV\_MOVIMENTACAO  
RMV\_PROCEDIMENTOS  
RMV\_PROCINVASIVO

### **Os script abaixo encontram-se no conversor da release 12.1.2310 marcação SA.2023.09\_17**

Possíveis Problemas e Soluções

## **09. POSSÍVEIS PROBLEMAS E SOLUÇÕES**

| Problema | Causa Provável | Solução |
| --- | --- | --- |
| Erro ao importar CID: "RMV\_CID.PRONTUARIO" viola NotNull | Campo **Prontuário** do paciente não está preenchido | Preencha o campo *Prontuário* corretamente antes de realizar a importação do CID. |
