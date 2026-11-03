---
content_hash: 75c3b19e7590b1ac412eb5eee82197f9ecef8d5350279b9f07237df293732d29
fetched_at: '2026-06-29T00:05:51.543373+00:00'
page_id: '1051250781'
product: rm
source: tdn-rm
title: Como buscar dados da ficha financeira entre base de dados
type: documentation
url: https://tdn.totvs.com/display/LRM/Como+buscar+dados+da+ficha+financeira+entre+base+de+dados
version: 5
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **T****abelas utilizadas**

## **01.** **VISÃO GERAL**

Este documento tem o objetivo de demostrar como restaurar o backup contendo os dados anteriores à liberação da competência, com o objetivo de exportar a ficha financeira existente antes da liberação.  
A ficha financeira exportada será posteriormente importada na base de produção, conforme orientações abaixo.

**Reforçamos que a realização de backup é obrigatória, conforme estabelecido na rotina de liberação de competência. Para os meses e situações em que não há backup disponível, informamos que o processo mencionado acima não é viável de execução.**

## **02. ORIENTAÇÕES**

## **2.1. Exportação da Ficha Financeira**

### **2.1.1 Baixar os Layouts**

Acessar o menu: Gestão | TOTVS Compartilhamento

Aplicar os seguintes filtros:

* Buscar: Ficha Financeira
* Tipo: Layout
* Produto: Folha de Pagamento

Baixar os dois arquivos listados.

### **2.1.2 Importar os Layouts**

Clicar em Importar na tela apresentada ao acessar o link.

Em seguida:

* Clicar em Parâmetros
* Selecionar uma Categoria

Caso não exista categoria cadastrada, é possível criar uma nova diretamente na tela, utilizando o ícone (+).

**2.1.3 Gerar Arquivos para Exportação**

Acessar o menu: Gestão | Gerador de Saídas

Selecionar:

* Layout de Exportação
* Processos
* Geração de Saídas

**Anotar o diretório de destino, pois é onde o arquivo será gerado para posterior importação.**

Avançar para criar o filtro do período a ser exportado.

No exemplo, foi gerado para apenas um funcionário e um mês específico da ficha financeira.

Avançar e Executar.

**Importante: Repetir o processo para os dois layouts importados, pois no momento da importação serão necessários:**

* O arquivo do Período da Ficha Financeira
* O arquivo da Ficha Financeira

## **2.2. Importação da Ficha Financeira na Base de Produção**

Acessar o menu: Configurações | Importações | Importação de Dados da Folha de Pagamento

### **2.2.1 Primeira Tela**

* Avançar
* (Opcional) Gravar o perfil para reutilização futura

### **2.2.2 Segunda Tela**

#### Aba Funcionário I

* Marcar Período de Ficha
* Selecionar o arquivo do período da ficha financeira gerado anteriormente
* Clicar na aba Funcionário II

#### Aba Funcionário II

* Marcar Ficha Financeira
* Selecionar o arquivo da ficha financeira gerado anteriormente

Avançar e clicar em Executar.

## **03.****TABELAS UTILIZADAS**

* PFPERFF
* PFFINANC
