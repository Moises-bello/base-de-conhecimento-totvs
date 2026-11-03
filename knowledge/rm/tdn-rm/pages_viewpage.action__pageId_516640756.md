---
content_hash: 17bedad99a5941bf988aa222f5ead8bc9b89c75eb2c2208098712caff71004a8
fetched_at: '2026-06-29T00:10:27.726853+00:00'
page_id: '516640756'
product: rm
source: tdn-rm
title: Relatório de produção do Cirurgião CIH
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=516640756
version: 1
---

## 

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela inicial**
   1. **Outras Ações / Ações relacionadas**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Essa rotina tem como objetivo o envio de um relatório de produção médica para os médicos que realizaram cirurgias em um determinado período.

Ao utilizar o envio de e-mail de produção médica o sistema irá selecionar todos as cirurgias realizadas por período para os médicos. Serão considerados na rotina de envio de e-mail apenas os médicos classificados como cirurgião principal, ou seja, os auxiliares não serão considerados na massa de dados.  Serão consideradas também todas as cirurgias feitas pelo médico no intervalo de datas do último envio da produção até a data selecionada na tela da rotina (número de dias de defasagem de hoje). Para que a cirurgia seja considerada na seleção os dados da via de acesso deverão ser preenchidos. Filtros utilizados na rotina:

## **02. EXEMPLO DE UTILIZAÇÃO**

Exemplo de utilização: Usuário irá enviar os e-mails no dia 15/09/2015 e informará uma defasagem de 2 dias. Com essa parametrização o sistema irá selecionar todas as cirurgias que ocorreram do último envio de produção ao médico até a data de 13/09/20015.

## **03. TELA INICIAL**

**Outras Ações / Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| Procedimento para inclusão | Saúde > controle de infecção hospitalar > utilitários > processos > envio de e-mail > produção do cirurgião |

## **04. TABELAS UTILIZADAS**

* Tela do processo de envio de e-mail > produção do cirurgião
* Informe a defasagem de dias em relação à data atual da data de alta da cirurgia no campo “Defasagem”.

Descrição de funcionamento de cada parâmetro:

* **CODCOLIGADA:** Indica ao relatório qual coligada que a cirurgia em questão pertence;
* **CODIGO:** Indica ao relatório o código interno do cirurgião (CODIGO na tabela SZJMEDICO)
* **DATAINICIAL :** Indica ao relatório a data do último envio de e-mail do médico em questão;
* **DATAFINAL:** Indica ao relatório a data calculada pela informação de defasagem de dias informada na tela da rotina;

* No campo Título do E-Mail deve ser colocado uma breve descrição do assunto que será exibido no e-mail que o médico irá receber.
* Ao executar o processo o sistema irá percorrer cada cirurgia selecionada e enviar o e-mail com o conteúdo do relatório desenvolvido no corpo do e-mail aos médicos em questão.
* Como temos vários médicos em várias cirurgias no período selecionado o sistema irá realizar o envio de e-mail para cada internação encontrada nas condições informadas e se houver algum problema ao enviar o e-mail o sistema adicionará no log de execução do processo o motivo de não envio do e-mail por médico.
* Cada mensagem deve ser analisada e ajustada para que processo de envio de e-mails funcione corretamente. No log conterá também, os e-mails enviados com sucesso.
* Para que o processo funcione corretamente o endereço de e-mail do paciente deve ser preenchido corretamente em seu cadastro:
