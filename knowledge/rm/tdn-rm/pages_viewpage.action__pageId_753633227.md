---
content_hash: cb03150bb1367ee6baa8982dfe8bae894889cf8657a00abba8d362d3ffcb3698
fetched_at: '2026-06-29T00:11:33.205787+00:00'
page_id: '753633227'
product: rm
source: tdn-rm
title: Registro de Atendimento Pré Registro Externo com Pedido de Exames agendados
  com data futura de realização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=753633227
version: 9
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

A partir da versão 12.1.2302 foi disponibilizado a possibilidade de Registrar um Atendimento do tipo “Pré Registro  Externo” vindo de uma agenda de atendimento contendo Exames programados com Data Futura de Realização.

Possibilidade de registrar o “Pré Registro Externo” de atendimento na data atual, porém com o pedido de exame e guia SP-SADT contendo uma data futura, pois a organização da coleta do exame é realizada no dia anterior.

Desta forma, possibilita agilizar o atendimento do cliente quando ele chegar para realizar o exame, pois já terá quase todas as informações necessárias e o pedido de exames já gerado.

## **02. EXEMPLO DE UTILIZAÇÃO**

PreRegistroExternoParametrizaçãoParametrização Necessária

Parametrização necessária para o uso desta funcionalidade:

* **No RMSaude.exe:**

No menu Parâmetros Gerais / Registro e Controle II , marcar o campo  “Pré-Registro de Atendimento”.

No menu Parâmetros Gerais / Registro e Controle III, marcar o campo “Lança exames da agenda ao gerar informações de atend. externo”.

* **No RM.exe:**

**Importante:**  no menu “Agenda de Atendimento” é obrigatório que este agendamento tenha preenchido “Exames”, somente assim será gerado automaticamente um atendimento “Pré Registro Externo”.

Se tentar registrar um atendimento com data futura e que não tenha exames neste agendamento, o sistema irá emitir mensagem de erro.

“Não é permitido registrar atendimento para agendamentos futuros”.

- (Opcional) Caso queira lançar o exame na conta do paciente: No RM.exe, menu Cadastros / Unidade de Diagnóstico / Exames e Serviços,  “Lança itens de débitos na conta do paciente”.

AgendamentoAgenda de Atendimento

**Criar um agendamento com data futura contendo Exames.**

**Neste exemplo a data de hoje é 13/04/2023 e a data do agendamento é para 21/04/2023.**

---

Necessário conter Exames no agendamento

Na agenda de atendimento, ao clicar no botão “Atend.Externo”, será criado um Registro de Atendimento cujo tipo de paciente será "Pré Registro Externo", contendo Pedido de Exames e guia de SP-SADT.

RegistroAtendimentoRegistro de Atendimento

**Registro de Atendimento - Pré Registro Externo**

A partir da agenda, foi criado um registro de atendimento com as seguintes características:

* **Tipo Paciente =  “Pré Registro Externo”**
* **Data de Entrada = Data Atual** (data em que o usuário registrou o atendimento através da agenda de atendimento).

* Será criada uma **Parcial 1** cuja data início também será uma **Data Futura**.

Caso o ambiente esteja configurado para lançamento automático dos exames na Elaboração de Contas, estes procedimentos serão incluídos na conta do paciente com data futura.

* Geração automática do **Pedido de Exames** no Pré Registro Externo de atendimento oriundo da agenda de atendimento, com **data futura.**

A visualização do Pedido de Exames, para um atendimento “Pré Registro Externo” somente poderá ser visualizado no menu do “Registro de Atendimento”.

No menu “Unidade de Diagnóstico”, o pedido não será listado, visto que neste momento não podem ser realizado nenhuma digitação.

A partir do momento em que o Registro do Atendimento for alterado de “Pré Registro Externo” para “Externo” (no dia da realização do exame), o pedido de exames segue seu fluxo normal no menu “Unidade de Diagnóstico”.

* Criação de uma **Guia de SP-SADT** com os itens dos exames (**data futura**).

* Impressão antecipada das etiquetas primárias para tubos de coletas oriundos do pré-registro externo, agilizando a coleta no Home Care.

No Registro de Atendimento, item Pedido de Exames, temos os respectivos Processos para impressão, são eles:

- Imprimir Mapinha: relatório configurado em RMSaude.exe, Parâmetros Gerias / Unidade de Diagnóstico – “Relatório de Impressão do Mapa de Trabalho”

- Imprimir Pedido de Exames: relatório configurado em RMSaude.exe, Parâmetros Gerias / Relatórios via gerador – “Pedido de Exames de Laboratório”

- Imprimir Etiqueta de Material Biológico: relatório configurado em RMSaude.exe, Parâmetros Gerias / Unidade de Diagnóstico – “Relatório de Impressão de Etiquetas de identificação do Material Biológico”.

“Emite Etiquetas para identificação do Material Biológico?”

“Relatório de etiquetas de Tubos”

Obs.: o processo “Pedido de Exames Simplificado” não será executado para o Pré Registro Externo.

ContaPacienteLançamento na Conta do Paciente

**Elaboração de Contas do Paciente**

Caso o ambiente esteja configurado para lançamento automático dos exames na Elaboração de Contas, estes procedimentos serão incluídos na conta do paciente com data futura.

## **03. TABELAS UTILIZADAS**

* SZATENDIMENTO
