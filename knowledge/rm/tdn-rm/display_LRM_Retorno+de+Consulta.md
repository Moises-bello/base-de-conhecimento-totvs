---
content_hash: 62c1d85502e62826d983c8c9dff2c629dff406d604ecbc51bde69e17baba72f6
fetched_at: '2026-06-29T00:10:52.184545+00:00'
page_id: '570375985'
product: rm
source: tdn-rm
title: Retorno de Consulta
type: documentation
url: https://tdn.totvs.com/display/LRM/Retorno+de+Consulta
version: 5
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Passo a passo das telas utilizadas**
4. **Documentação Relacionada**

## **01. VISÃO GERAL**

**OBSERVAÇÃO**

---

Em rotinas separadas o atendimento é classificado como retorno e depois os honorários

## **02. EXEMPLO DE UTILIZAÇÃO**

Acesse a tela Registro de Atendimentos Externos

No menu Atendimento / Pronto Atendimento/Ambulatório / Registro de Atendimentos Externos.

## **03. PASSO A PASSO DAS TELAS UTILIZADAS**

Na tela de registro de atendimento externo, siga os seguintes passos: 

* Clicar em novo
* Pesquisar o paciente retorno de consulta
* As informações registradas para o atendimento foram:

Unidade de Atendimento: AMBULATÓRIO CAMBUCI

Plano: Bronze S/Obst – Enfermaria

Foi informada a data de atendimento como 30/10/2020 para o primeiro atendimento, para seja possível realizar outros atendimentos que possam ser considerados como retorno em um período de 15 dias, que é o intervalo de tempo parametrizado como retorno.

Tipo Atendimento: Consultório

Clínica/Especialidade: CLÍNICA MÉDICA

Médico solicitante e Médico Responsável: Médico Externo.

* Gravado, incluir novo atendimento

* Selecione sim

* Fora da conta - OK

* Novo atendimento

* Selecionar não

* NOVO ATENDI DATA 13/11/2020 – RETORNO

* DATA SUPERIOR AOS 15 DIAS

* Dentro da conta

## **04. DOCUMENTAÇÃO RELACIONADA**

Documentação Relacionada Como Parametrizar Atendimento de Retorno

1. **Visão Geral**
2. **Telas utilizadas**

## **01. VISÃO GERAL**

 Auxiliar o usuário a parametrizar um atendimento de retorno.

## **02. TELAS UTILIZADAS**

Realize os seguintes passos:

* No **TOTVS Gestão Hospitalar** acesse **Cadastros**> **Faturamento**> **Condições Contratuais com Convênios**.

* Selecione o convênio desejado

* Na aba **Parâmetros 1**, Quando o parâmetro "**Considera como retorno apenas o primeiro atendimento dentro do prazo**" está marcado, o sistema irá considerar como retorno somente o primeiro atendimento registrado dentro do período de retorno.

* Caso o parâmetro, **Considerar contagem de retorno a partir de atendimentos não classificados como retorno**esteja marcado, qualquer atendimento dentro do período será considerado como retorno.

* Para o sistema considerar corretamente o retorno, acesse **Anexos> Retorno de Consulta**.

* Acesse a aba **Retorno de consulta**,clique em **Incluir**  para configurar um novo retorno, preencher o **Plano**, selecionar o **Tipo** se é **Especialidade**, **grupo ou item,** **Unidade de Atendimento**e**Retorno em dias**, por fim clique em **OK** para finalizar.

* É importante salientar que ao realizarmos o lançamento de um procedimento na conta, quando o atendimento está como retorno, o sistema faz o lançamento **fora da conta**.

* Por fim ao registrarmos um atendimento e o mesmo encontrasse em período de retorno, o aviso **Procedimento EM CONSULTÓRIO está no período de retorno com data de lançamento**será exibido.
