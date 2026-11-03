---
content_hash: dfd4c732d41815bf3675dff21673b3aef54d9bca2d9ec3f054fd99a80357332e
fetched_at: '2026-06-29T00:11:50.426971+00:00'
page_id: '841167609'
product: rm
source: tdn-rm
title: Guias DARF
type: documentation
url: https://tdn.totvs.com/display/LRM/Guias+DARF
version: 25
---

# Conteúdo

Conteúdononenone

# 1. O que é Guia DARF:

O Documento de Arrecadação de Receitas FederaisDARF é uma guia que serve para arrecadação de impostos, contribuições e taxas. Este documento é um dos principais instrumentos de recolhimento de tributos à Receita Federal.

A geração da guia DARF estará disponível para tributos dos seguintes tipos: CIDE, PIS, COFINS, CSLL, IRPJ, IRRF, IOF.

# 2. Encerrando do Período de Apuração

Para a geração da guia é necessário encerrar o Período de Apuração.

Encerrando do Período de Apuração

##### **Funcionamento do Saldo Credor/Devedor**

O Saldo Credor/Devedor é calculado e preenchido automaticamente ao se executar o processo de “**Geração de Guias a partir de Lançamentos Financeiros**”, pois é por meio desse processo que se apura o valor do débito do imposto. Esse processo só pode ser realizado após o encerramento do período de apuração.

Caso o período de apuração seja reaberto, o Saldo Credor/Devedor será zerado, porém a guia gerada anteriormente não será removida.

Para que o Saldo Credor/Devedor seja recalculado e preenchido novamente temos 2 opções:

Incluir o valor manualmente, e ou

Estornar executar o processo de “**Estorno do Lançamento Financeiro da Guia**”.

Aviso

Verifique se existe guia gerada para o Período de Apuração a mesma não será removida abrir o Período.

# 3. Valores Apuração Pis/Cofins

Para a geração da guia, serão utilizadas as informações contidas na aba Valores Apuração Pis/Cofins dentro do Período de Apuração de Pis ou Cofins.

Valores Apuração Pis/Cofins

# 4. Geração Automática das Guia DARF

A geração automática será apenas para os tributos do tipo PIS e COFINS

O Vencimento do Período da Apuração deve estar preenchido e o Valor Apurado na guia deve ser maior que zero, caso contrário o controle não gerará a guia.

Geração Automática das Guia DARF

## 4.1 Geração de Guia Automaticamente

Observação

A geração da guia deve ser feita individualmente por tributo.

## 4.2 Anexo Guia DARF

## 4.3 Preenchimento da Guia

# 5. Informações específicas para guias de PIS/COFINS

**01 -** Para os tributos PIS e COFINS utilizamos o campo "Código da Obrigação", na aba Outros Dados da guia para identificar o código da contribuição a recolher e fazer o agrupamento da apuração.

Podendo ser:

* "08" para regime não cumulativo
* "12" para regime cumulativo.

É necessário respeitar o tamanho do campo de dois dígitos, para validação no PVA.  
  
  
  
**02 -** Para o correto preenchimento do código de receita das guias, quando há incidência tributária nos regimes cumulativo e não cumulativo, além dos tributos PIS COFINS informados nos parâmetros, é necessário incluir mais 4 parâmetros, correspondentes aos códigos de receita de PIS COFINS regime cumulativo e não cumulativo conforme passo a passo abaixo:

11Passo 01

Definir corretamente o código de receita no cadastro dos tributos utilizados no regime cumulativo e não cumulativo

2Passo 02

Passo 02: Acessar o menu "Obrigações Acessórias", "Rotina Fiscal", "Anexos", "Parâmetros da Rotina"

3Passo 03

Incluir os seguintes parâmetros conforme imagens abaixo onde

**Chave: PIS\_CODRECEITA\_CUMULATIVO** (Deve ser informado exatamente o valor **PIS\_CODRECEITA\_CUMULATIVO** para identificar o parâmetro correspondente ao código de receita das guias no regime cumulativo)  
**Valor: PIS** (Deve ser informado a sigla do tributo correspondente a guia no regime cumulativo)  
**Descrição:** PIS CODRECEITA CUMULATIVO (Pode ser informado qualquer texto)

**Chave: PIS\_CODRECEITA\_NAOCUMULATIVO** (Deve ser informado exatamente o valor **PIS\_CODRECEITA\_NAOCUMULATIVO** para identificar o parâmetro correspondente ao código de receita das guias no regime cumulativo)  
**Valor: PIS NC** (Deve ser informado a sigla do tributo correspondente a guia no regime cumulativo)  
**Descrição:** PIS CODRECEITA NAO CUMULATIVO (Pode ser informado qualquer texto)

**Chave: COFINS\_CODRECEITA\_CUMULATIVO** (Deve ser informado exatamente o valor **COFINS\_CODRECEITA\_CUMULATIVO** para identificar o parâmetro correspondente ao código de receita das guias no regime cumulativo)  
**Valor: COFINS** (Deve ser informado a sigla do tributo correspondente a guia no regime cumulativo)  
**Descrição:** COFINS CODRECEITA CUMULATIVO (Pode ser informado qualquer texto)

**Chave: COFINS\_CODRECEITA\_NAOCUMULATIVO** (Deve ser informado exatamente o valor **COFINS\_CODRECEITA\_NAOCUMULATIVO** para identificar o parâmetro correspondente ao código de receita das guias no regime cumulativo)  
**Valor: COFINS NC** (Deve ser informado a sigla do tributo correspondente a guia no regime cumulativo)  
**Descrição:** COFINS CODRECEITA NAOCUMULATIVO (Pode ser informado qualquer texto)

Consulta também a geração dos Registros

M205 e M605
