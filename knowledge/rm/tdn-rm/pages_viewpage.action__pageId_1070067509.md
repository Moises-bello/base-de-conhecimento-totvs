---
content_hash: 32cb4dde2f869bdd0944a25d25318ec6c02d043902e09a174f36aadd5c6c9ff8
fetched_at: '2026-06-29T00:05:53.391576+00:00'
page_id: '1070067509'
product: rm
source: tdn-rm
title: Processo Atualizar Dedução por Dependente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1070067509
version: 8
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Atualizar Dedução por Dependente**
   1. **Principais Campos e Parâmetros**
4. **Tabelas utilizadas**

false

**A partir das Versões:**

* [DT - Cadastro de Dependente - Valor Dedução do Rendimento Tributável](https://tdn.totvs.com/pages/viewpage.action?pageId=1068186521)
* [DT - Processo para atualizar Dedução por Dependente](https://tdn.totvs.com.br/pages/viewpage.action?pageId=1070066693)

## **01. VISÃO GERAL**

Possibilitar a atualização do campo “Valor de Dedução do Rendimento Tributável”, existente no anexo de Dependentes do Funcionário, para que a dedução do dependente seja considerada sempre que aplicável, mesmo quando não houver desconto de IRRF ou quando for utilizado o desconto simplificado mensal.

 "Ainda que as deduções legais não sejam utilizadas no cálculo do IRRF em razão da aplicação do desconto simplificado mensal, tais informações permanecem existentes no contexto fiscal do trabalhador e devem ser devidamente declaradas. A própria orientação oficial do eSocial, constante no FAQ 10.39 (atualizado em 17/12/2025), estabelece expressamente que, mesmo quando aplicado o desconto simplificado mensal, é obrigatório o envio dos dados de deduções legais aplicáveis ao trabalhador no evento de pagamento. Assim, a não utilização das deduções no cálculo não afasta a obrigatoriedade de sua informação no evento S-1210."

Veja mais detalhes da consultoria no link: [eSocial - Envio de dedução de dependentes no S-1210](https://tdn.totvs.com/pages/releaseview.action?pageId=1056129814)

O processo “Atualizar Dedução por Dependente”,  encontra-se disponível em: Administração de Pessoal | Funcionário | Processos.

Com essa melhoria, o histórico dos dependentes passa a ser preenchido sempre que existir direito à dedução, e não apenas nos casos em que houver desconto de IRRF.

IMPORTANTE:

A permissão de acesso para esse processo é a mesma permissão do processo "Atualiza Campo Desconto Simplificado", disponível em: Administração de Pessoal | Funcionário | Processos por se tratar de processos para atualização de base para envio para o eSocial. Então para liberar acesso ao processo  “Atualizar Dedução por Dependente” basta dar acesso ao processo "Atualiza Campo Desconto Simplificado".

## **02. EXEMPLO DE UTILIZAÇÃO**

Supondo que um funcionário não tem cálculo de IRRF devido seu salário não atingir as faixas de dedução:

Antes da implementação, no anexo do cadastro de dependentes não haverá informações do valor a deduzir por dependente:

Executando o processo e selecionando as competências:

No anexo do cadastro de dependentes será inserido as informações do valor a deduzir por dependente:

Dicas:

Para que a tabela seja preenchida corretamente, é necessário que:

* O dependente esteja com o parâmetro **IRRF** marcado no cadastro de dependentes;
* Exista valor de **Base IRRF** na tabela de período da ficha financeira (**PFPERFF**);
* Para dependentes até completar 22 anos, basta o parâmetro IRRF esta marcado;
* Para dependentes entre 23 e 25 anos, além do IRRF, é necessário marcar também a opção de **Universitário**.

**Importante:**

* Ao executar o processo, caso já existam registros na tabela **PFDEPIRRFDED**, eles não serão excluídos antes da nova atualização. somente serão inseridos novos registros caso não existam, mas para isso é necessário que o parâmetro **IRRF** esteja marcado no cadastro de dependentes;
* Para composição da informação do mês caixa das férias, será considerada a data de pagamento das férias.

## **03.** **TELA Atualizar Dedução por Dependente**

****Principais Campos e Parâmetros****

| Campo | Descrição |
| --- | --- |
| Quebra de Seção | Informar a quebra de seção |
| Seleção de Funcionários | Informar a seleção de funcionários |
| Competência Inicial | Informar a competência inicial da execução do processo |
| Competência final | Informar a competência final da execução do processo |

## **04. TABELAS UTILIZADAS**

* PFDEPIRRFDED
* PFFINANC
* PFDEPEND
