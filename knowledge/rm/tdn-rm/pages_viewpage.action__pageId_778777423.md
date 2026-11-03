---
content_hash: b1d2c589ea6f1e01b6a3ad57fbdd88299634a76f96cb3494ea3558c8904695a8
fetched_at: '2026-06-29T00:11:37.884442+00:00'
page_id: '778777423'
product: rm
source: tdn-rm
title: Detalhamento Apuração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=778777423
version: 75
---

#FFA500#FFFACD#FFE766dashedAviso Importante:1%99%

Informamos que o detalhamento da apuração está sendo desenvolvido gradualmente ao longo das próximas Releases. Algumas funcionalidades que não são suportadas atualmente, estarão disponíveis nas próximas Releases.

Essa mudança é parte do nosso compromisso com a evolução tecnológica e a otimização de nossas soluções, proporcionando maior estabilidade e alinhamento com as atualizações mais recentes do mercado. Isso garante que a transição ocorra de forma organizada e sem impacto**.**

# Conteúdo

Conteúdonone

# 1. Visão Geral

O Detalhamento da Apuração é um anexo do Período de Apuração (exibido apenas para os tributos PIS e COFINS), que apresenta os valores calculados correspondentes aos itens de origem Financeira, Fiscal e Origem Contábil existentes no Cadastro de Parâmetros de Processos em [Filtro de Operações Contábeis](https://tdn.totvs.com/pages/viewpage.action?pageId=772823527).

# 2. Campos

Detalhamento e origem dos campos apresentados no detalhamento da apuração.

| Registro\Campo | Origem Dados RM |
| --- | --- |
| Código Tipo Operação | Campo preenchido com a informação do campo Tipo Operação que possui os seguintes valores Operações Sujeitas a incidência de Crédito - Código = 0 Operações  Sujeitas a Contribuições - Código  = 1 Operações Não Sujeitas a Contribuição - Código = 2   Detalhes  Aviso A opção de "**Operações Sujeitas a incidência de Crédito - Código = 0**" não será calculada pelo sistema para atender a seguinte regra do [manual da rotina EFD Contribuições](http://sped.rfb.gov.br/pasta/show/1989):  **Registro F100 - Campo 03 - Validação** "[...] No caso do registro se referir a uma operação representativa de crédito (Campo IND\_OPER = “0”) o Campo 03 é de preenchimento obrigatório [...]".  No campo 03 (COD\_PART) deve ser apresentado o código do Cli/For, porém quando a origem do registro F100 é Contábil não há informação de Cli/For a ser gerada neste campo, por esse motivo a opção IND\_OPER=0 não é calculada. |
| Código da Situação Tributária | CST de PIS/COFINS dos lançamentos fiscais ou financeiros. |
| Natureza da Base de Cálculo do Crédito | Natureza da Base de Cálculo do Crédito. |
| Natureza da Receita | Natureza da Receita |
| Código Conta contábil | Código Conta contábil |
| Descrição | Descrição |
| Base de Cálculo: Crédito, Débito, Movimentação da conta | Base de Cálculo: Crédito, Débito, Movimentação da conta |
| Alíquota | Alíquota |
| Valor do Imposto | Valor do Imposto |
| Identificador Referência | Identificador Referência |
| Código Receita | Código Receita |
| Código Filial | Código Filial |
| Registro | Registro |
| Valor da Operação | Valor da Operação |
| Coligada Cliente/Fornecedor | Coligada Cliente/Fornecedor |
| Contratada | Código do Cliente/Fornecedor, para lançamentos de emissão própria este campo não é preenchido. |
| Data da Operação | Data da Operação |
| Código da Contribuição Social | Código da Contribuição Social |
| Condição Pessoa jurídica Declarante | Condição Pessoa jurídica Declarante |
| CNPJ Fonte Pagadora | CNPJ Fonte Pagadora |
| Natureza Retenção Fonte | Natureza Retenção Fonte |
| Tipo Detalhamento | Tipo Detalhamento |
| Alíquota por Valor | Alíquota por Valor |

# 3. Regras

* O anexo calcula automaticamente ao encerrar o Período de Apuração;
* O calculo será executado apenas para os tributos do tipo PIS e COFINS;
* No Detalhamento da Apuração será considerado na matriz os lançamentos das filiais que possuem o mesmo CNPJ base da matriz;
* Ao reabrir o Período de Apuração os dados são apagados;
* Se o resultado da Movimentação da conta for diferente do esperado, ou seja, Natureza Devedora com resultado negativo ou Natureza Credora com resultado positivo.   
  O item não será calculado e um log deve ser apresentado informando a inconsistência, indicando que o item não foi calculado e informando os dados básicos para o usuário identificar o item inconsistente.
* O sistema irá consistir o CST e alíquota do PIS COFINS para identificar se o tributo é cumulativo ou não cumulativo, com ou sem direito a crédito para o registro A170.
* Caso haja mais de um período de PIS/COFINS no mesmo intervalo (por exemplo, PIS e PIS NC para o mês de janeiro/2025), o detalhamento será agrupado apenas no período do PIS, gerando cada linha do detalhamento conforme a alíquota de seu período.

# 4. Detalhamento da Apuração

* Os valores gerados no detalhamento da apuração são pertinentes aos lançamentos fiscais de entrada e saída para os registros A170 e C170, contas contábeis, retenções de origem financeira, registro F600 e demais parametrizações realizadas nos parâmetros de processo do F100  - Anexo Filtros Contábeis -  conforme documentação do [cadastro de Parâmetro de Processos](https://tdn.totvs.com/pages/viewpage.action?pageId=499101633).

Detalhamento da ApuraçãoObservação

Ao encerrar o Período de Apuração dos tributos PIS e COFINS, os lançamentos das filiais que possuem o mesmo CNPJ base da matriz será considerado no detalhamento da apuração da filial matriz.

Esta informação estará disponível a partir da **Versão 12.1.2406**.

# 5. Valores Apuração Pis/Cofins

* Os valores gerados no detalhamento da apuração, serão inseridos na arvore de **Consolidação da Contribuição do Período** e em seu Bloco de origem.

Valores Apuração Pis/CofinsObservação

Esta informação estará disponível a partir da **Versão 12.1.2402**.

Consulta também a geração dos Registros

[Estrutura do arquivo EFD Contribuições](https://tdn.totvs.com/pages/viewpage.action?pageId=422545664)
