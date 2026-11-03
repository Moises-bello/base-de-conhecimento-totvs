---
content_hash: 4e56d08d38de6c228784a5c724e0ac24681d89601afe4c188d23de99575f11db
fetched_at: '2026-06-29T00:10:37.707018+00:00'
page_id: '540881707'
product: rm
source: tdn-rm
title: Gestão de Recebíveis e Conciliação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=540881707
version: 17
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. ****Permissão****
4. **Assuntos relacionados**

**Obs: Funcionalidade está disponível a partir da versão 12.1.26.**

## **01. VISÃO GERAL**

Este recurso tem como objetivo dar visibilidade dos principais indicadores financeiros, principalmente o recebimento com cartão de crédito e as informações sobre a conciliação.

### **Indicadores de recebimento:**

* **Faturado**: Valor total dos títulos a receber emitidos
* **Recebido**: Valor total dos títulos recebidos total ou parcialmente. No caso de baixa parcial será considerado o valor baixado.
* **A receber**: Valor total dos títulos a receber em aberto ou recebido parcialmente. No caso de baixa parcial será considerado o valor em aberto (Valor Original - Valor Original Baixado).
* **Inadimplência**: Valor total dos títulos com vencimento superior a 30 dias.

Os títulos considerados nos indicadores acima são filtrados pela data de vencimento.

### **Indicadores de recebimento com cartão:**

* A receber: Transações com cartão de crédito a receber da adquirente
* Recebido: Transações com cartão de crédito já recebidas da adquirente
* Chargeback: pagamentos via cartão de crédito cancelados via contestação diretamente com a administradora do cartão.
* Taxas: valor total de taxas pagas no período
* Recorrência: quantidade de contratos cadastrados para cobrança recorrente no cartão de crédito.

### Outras informações**:**

Informação da última vez em que os processos "Conciliação automática" e de "Recorrência" ocorreram com sucesso. Caso NÃO seja encontrada execução com sucesso de algum destes processos, a data/hora de execução relativa a tal processo será apresentada em branco.

Será considerado apenas o filtro de coligadas e a busca selecionará a maior data (mais recente) observando as coligadas selecionadas.

## **02. EXEMPLO DE UTILIZAÇÃO**

Ao exibir o **Dashboard Financeiro** de visão geral, o filtro inicial utilizará todas as filiais de todas coligadas considerando como data inicial o primeiro dia do mês corrente e data final o último dia. O usuário poderá alterar os filtros selecionando as coligadas e filiais que desejar, bem como o período desejado e clicar em filtrar para visualizar as informações.

**Obs:** Os filtros serão utilizados para calculo dos indicadores e exibição dos gráficos .

### Conceitos de conciliação:

* **Pendentes:** Transações que ainda não foram conciliadas com as informações da adquirente.
* **Não conciliado:**  Transações que foram conciliadas e apresentaram alguma divergência nas informações retornadas da adquirente.
* **Conciliado:** Transações que foram conciliadas corretamente.

Os detalhes das transações não conciliadas podem ser conferidos na visão de transações não conciliada.

**Obs:** Essa é uma visão padrão do sistema que oferece todos os recursos já existentes para filtros, agrupamentos e etc.

## **03. Permissão**
