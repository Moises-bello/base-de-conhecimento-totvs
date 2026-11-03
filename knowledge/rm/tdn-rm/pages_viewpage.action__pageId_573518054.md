---
content_hash: 745db479ee34f764a62563fc6ee8aaad20e3b76b0b1f149b8ce70db8cc71e805
fetched_at: '2026-06-29T00:10:52.978087+00:00'
page_id: '573518054'
product: rm
source: tdn-rm
title: Validações Guias SP/SADT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=573518054
version: 3
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Caso existam Guias SP/SADT para o atendimento, as seguintes validações serão executadas:

* Caso o campo de médico requisitante estiver vazio, retorna a mensagem "Não foi informado o requisitante. Informe o requisitante na página dados do atendimento do registro de atendimento".
* Caso o Tipo de consulta seja 0 ou vazio, retorna a mensagem "Falta informar o tipo de consulta para este atendimento. Registre as informações necessárias de acordo com a guia informada através do botão outras informações(TISS) da função de registro de atendimento".
* Se o tipo de consulta estiver preenchido, verifica se o Tipo de consulta é compatível e retorna a mensagem "Tipo de consulta incompatível com a versão {VersãoTiss} do padrão TISS - ANS. Registre as informações necessárias de acordo com a guia informada".
* Caso o Indicador de acidente seja 0, retorna a mensagem "Falta informar o 'Indicador de acidente'. Registre as informações necessárias de acordo com a guia informada através do botão outras informações (TISS) da função de registro de atendimento".
* Se o indicador de acidente estiver preenchido, verifica se Indicador de acidente é compatível e retorna a mensagem "Indicador de acidente está incompatível com a versão {VersãoTiss} do padrão TISS - ANS. Registre as informações necessárias de acordo com a guia informada"
* Verifica se o Código do motivo de alta é maior que 0 e é 11, 12, 14, 15, 16, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 31, 32, 41, 43, 51, 61, 62, 63, 64, 65, 66 ou 67, se não estiver dentro desses valores retorna a mensagem "O motivo de saída do paciente não esta nos tipos definidos pela ANS para a versão {VersãoTiss}. Registre as informações necessárias de acordo com a guia informada através do botão outras informações (TISS) da função de registro de atendimento."
* Caso o Tipo de atendimento estiver vazio, retorna a mensagem "Falta informar o tipo de atendimento. Registre as informações necessárias de acordo com a guia informada através do botão outras informações (TISS) da função de registro de atendimento".
* Se o tipo de atendimento não estiver vazio, valida se é compatível e retorna a mensagem "Tipo de atendimento incompatível com a versão {0} do padrão TISS - ANS. Registre as informações necessárias de acordo com a guia informada através do botão outras informações (TISS) da função de registro de atendimento".
* Se o parâmetro "Informar local de execução de atendimento" estiver ligado e o código do local de execução estiver vazio, retorna a mensagem "Falta informar o local de execução. Informe o local de execução na página 'Dados Atendimento' da função de registro de atendimento"
* Se o tipo de paciente do atendimento for “Externo”, e tipo de atendimento for “Pequena Cirurgia” ou “Terapias” e existir "cabeçalho na Guia", verifica se Indicação Clínica está vazio e retorna a mensagem "Indicação clínica obrigatória para Tipo de Atendimento Pequena Cirurgia, Terapia e Alta Complexidade. Acesse a Guia de SP/SADT da parcial e preencha o campo Indicação Clínica"

## **02. EXEMPLO DE UTILIZAÇÃO**

**Passo 1: Escolher registro que possua guia SP/SADT.**

**Passo 2: Executar o processo de encerramento de conta**

**Passo 3: Verificar mensagens de erro no log do encerramento da conta.**

## **03. TABELAS UTILIZADAS**

* SZATENDIMENTO
* SZANSATEND
* SZATENDAUTORIZ

]]>
