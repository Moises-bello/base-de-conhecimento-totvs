---
content_hash: d4028798c8a0c7600f9e2020b6fc4ac591c64831c21b490221e32e9fee7612d1
fetched_at: '2026-06-29T00:12:00.190377+00:00'
page_id: '883049982'
product: rm
source: tdn-rm
title: DT - Smart UI - Linha de Vale Transporte
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Smart+UI+-+Linha+de+Vale+Transporte
version: 5
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Smart UI - Linha de Vale Transporte |
| País: | Brasil |
| Épico | [DRHCALCRM-7275](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-7275) |

## **02. SITUAÇÃO/REQUISITO**

Disponibilizar a nova tela de **Linha de Vale Transporte**, utilizando a tecnologia do **Smart UI**. Esta nova tela receberá uma evolução visual e em partes funcional, da tela que conhecemos como Linha de Vale Transporte já disponibilizada na nossa atual MDI.

## **03. SOLUÇÃO**

Disponibilizamos a tela de **Linha de Vale Transporte**, utilizando o Smart UI para as versões 12.1.2502 e superiores. Essa implementação alterou visualmente o que já existia trazendo uma visão atualizada da pagina e também a maneira com que a utilizamos. 

## **04. DEMAIS INFORMAÇÕES**

Neste modulo é possível realizar o cadastro das linhas de transporte. Este cadastro está vinculado ao controle de vale transporte do funcionário e ao cadastro de tarifas.

Através do modulo continuará sendo possivel administrar :  
  
**Tipo de Transporte**

Este campo está relacionado a tabela dinâmica INT18 disponível em Cadastros | Tabelas Dinâmicas

**Código Tarifa**

Esta informação deve ser previamente cadastrada em Cadastros | Tabelas Auxiliares | Tarifas de Transporte

**Grupo de Transporte**

Informe um grupo de compra para separar as linhas em grupos. Desta forma é possível emitir relatórios listando os vales por grupos. Caso não utilize esse recurso, selecione o grupo 00. Este campo está relacionado à tabela dinâmica INT20 disponível em Cadastros | Tabelas Dinâmicas

**Código de Itinerário**

Este campo está relacionado à tabela dinâmica INT21 disponível em Cadastros | Tabelas Dinâmicas

**Apenas um Vale Transporte**

Marque esta opção caso o vale transporte utilize um único ticket para todo o mês.

**Ativo**  
Desmarque esta opção caso não utilize mais esta Linha de Transporte. O sistema não apresentará mais a linha de transporte no  
Cadastro de Funcionários.  
   
**Trocar Código da Linha de Transporte**

Através deste processo é possível alterar o código da linha de transporte.

Tudo isso de forma prática, utilizando uma nova versão de control de Filtros, através da função **Filtros:**E **Filtros Avançados**, onde podemos criar e gerenciar filtros para maior agilidade no dia a dia:  
  
  
  
Para Incluir um novo registro, basta utilizarmos a função , e preenchermos os campos da tela de inclusão:  
  
  
  
Caso queira Editar um registro, basta selecionar a linha do registro desejada e clicar no icone do lapis (), como no exemplo abaixo:  
  
  
  
  
  
Caso a necessidade seja excluir um registro, basta selecionarmos a linha do registro e clicar no icone da lixeira ( ). É importante se atentar, caso o registro esteja associado a algum funcionario não será permitida a exclusão do mesmo

Atenção

Nesta versão, a exclusão de registros é **limitada a um por vez**.  
Ou seja, é necessário **selecionar apenas uma linha por vez**. A seleção múltipla (duas ou mais linhas) **não é permitida para exclusão**.

**É possível também realizarmos a copia de registros entre as coligadas, selecionando o registro e clicando em **Ações Relacionadas / Copiar linha vale transporte entre coligadas**  
  
  
  
  
Após isso, basta realizarmos a parametrização, selecionando qual coligada receberá o registro, e se ele deve substituir o registro existente em casos que hajam registros na coligada destino.  
  
  
  
E por fim, basta avançarmos para a execução do processo, podendo acompanhar o processo para a inclusão na base destino:  
  
Para acompanhar o processo, podemos clicar em **Ações Relacionadas e Acompanhar Processos:****

## **05. ASSUNTOS RELACIONADOS**
