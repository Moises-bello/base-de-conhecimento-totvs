---
content_hash: aa5d1b9acfe0ce90843cd586102d72e4d2f055465e2900ffe5939cc1324ad5b7
fetched_at: '2026-06-29T00:11:20.497075+00:00'
page_id: '685895647'
product: rm
source: tdn-rm
title: TOTVS Folha de Pagamento - Fracionamento de Jobs
type: documentation
url: https://tdn.totvs.com/display/LRM/TOTVS+Folha+de+Pagamento+-+Fracionamento+de+Jobs
version: 22
---

É possível realizar no sistema RM.exe a "quebra" (paralelização/divisão) de um processo em "N" processos menores quando do agendamento de um Job. Veja informações em <https://tdn.totvs.com.br/display/LRM/Processos+de+JOBS>

No módulo TOTVS Folha de Pagamento existe a possibilidade de executar os processos com o fracionamento de jobs, onde permite o fracionamento em N processos, e consequentemente acelerar o processamento que serão executados paralelamente.

Processos em que há possibilidade de fracionar:

* Cálculo da folha (Lançamento Multi-Coligadas, Grupo de Eventos, Executa Recálculo, Recálculo Multi-Coligadas)
* Cálculo do 13º Salário
* Cancelamento de Movimento
* Geração de Lançamentos Financeiros
* Atualiza Campo Desconto Simplificado
* Geração dos Encargos
* Geração do Histórico de Provisão
* Geração da Contabilização
* Marcar Férias Compulsórias
* Atualizar Status eSocial
* Gerar XML eSocial
* Gerar Gatilho em Lote eSocial
* Gerar XML Periódicos eSocial
* Integração com TAF/Midleware (eSocial)
* Integridade RM x TAF (eSocial)
* [Copia de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060801054-Framework-Linha-RM-Frame-C%C3%B3pia-de-dados)

Para o fracionamento de Jobs na folha de pagamento deve ser habilitado o parâmetro “Habilita Fracionamento de Jobs” em Parametrizador / Folha Normal / Geral. Veja informação sobre o parâmetro em <https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719263>

O processo poderá ser agendado. Para o agendamento com fracionamento de jobs, primeiro deverá ser preenchida a tela do agendamento e logo em seguida se deseja ou não fracionar o processo, em caso de sim, deverá preencher em quantas partes o processo será dividido, caso selecione o não, o processo executará de forma padrão ao sistema.

Veja informações em <https://tdn.totvs.com/display/LRM/Agendamento+com+fracionamento+jobs>

A tela de Segurança de Jobs Fracionáveis tem por função, realizar a segurança do Job que está sendo executado, de acordo com os parâmetros solicitados na tela. Veja informação em:

<https://tdn.totvs.com.br/pages/viewpage.action?pageId=547231277>

Veja como parametrizar conforme exemplos:

* Exemplo de fracionamento de Jobs marcando o parâmetro “Habilita Fracionamento de Jobs” em Parametrizador / Folha Normal / Geral:

Veja informações em <https://tdn.totvs.com.br/display/LRM/EXEMPLO+DE+FRACIONAMENTO+DE+JOBS>

* Parametrização para o Fracionamento de Jobs para o processo de Geração de Contabilização:

Veja informações em <https://tdn.totvs.com.br/pages/viewpage.action?pageId=545232022>

**Observação:** Nos processos elegíveis para o fracionamento de Jobs será apresenta a mensagem para melhorar o desempenho do processamento quando o parâmetro “Habilita Fracionamento de Jobs” em Parametrizador / Folha Normal / Geral não estiver habilitado e a mensagem não será mais apresentada quando o parâmetro for habilitado ou o usuário marcar o parâmetro "NÃO VER ESTA INFORMAÇÃO NOVAMENTE" na própria mensagem e clicar em fechar (X) no canto superior. Esse último parâmetro na tela será salvo por usuário, coligada e processo.
