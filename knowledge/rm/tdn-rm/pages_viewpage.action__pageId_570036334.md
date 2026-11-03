---
content_hash: 544b1c1ca96f14bce97c14cbdedee9ea8e9e88a4e1ffb7bbd3fd57025bf9fdb5
fetched_at: '2026-06-29T00:10:52.029138+00:00'
page_id: '570036334'
product: rm
source: tdn-rm
title: Validações Paciente Unimed BH
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=570036334
version: 11
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Registro de Atendimento**
4. **Tabelas utilizadas**

itensVisão Geral

## **01. VISÃO GERAL**

Quando o padrão de informação é Unimed BH, as seguintes informações não podem estar em branco:

* Campo "Sexo" do paciente;
* Campo "Data de nascimento" do paciente;
* Campo "Estado Civil" do paciente;
* Campo "CPF" do paciente, se Código de Nacionalidade Unimed BH = 1;
* Campo "CPF" e "RG", se Código Nacionalidade Unimed BH = 2;

Se qualquer um destes campos estiver em branco, não é possível encerrar a parcial.

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Log relacionado à validação:

Encerramento da Parcial

Iniciando processo de encerramento da conta.

Paciente: 35325 -  PACIENTE UNIMED BH   
Prontuário: 35325. Atendimento: 8.  
Parcial 1:

Falta informar o SEXO (obrigatório para paciente de INTERCÂMBIO). Informe o SEXO no cadastro do paciente.  
Falta informar o DATA DE NASCIMENTO (obrigatório para paciente de INTERCÂMBIO). Informe o DATA DE NASCIMENTO no cadastro do paciente.  
Falta informar o ESTADO CIVIL (obrigatório para paciente de INTERCÂMBIO). Informe o ESTADO CIVIL no cadastro do paciente.  
Falta informar o CPF (obrigatório para paciente de INTERCÂMBIO). Informe o CPF no cadastro do paciente.  
Falta informar o CPF OU RG (obrigatório para paciente de INTERCÂMBIO). Informe o CPF OU RG no cadastro do paciente.

Processo Finalizado

## **03. TELA REGISTRO DE ATENDIMENTO**

É possível alterar o padrão de informação na tela de Registro de Atendimento → Dados de Atendimento → Convênio → Padrão de Informação

## **04. TABELAS UTILIZADAS**

* SZATENDIMENTO
* SZCADGERAL
* SZAPACIENTE
]]>
