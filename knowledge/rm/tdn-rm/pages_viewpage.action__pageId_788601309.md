---
content_hash: 52f97a7761941a6d78358da21f4aaea21414211cfe9171bc45defa5948f36b34
fetched_at: '2026-06-29T00:11:39.145487+00:00'
page_id: '788601309'
product: rm
source: tdn-rm
title: Limitações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=788601309
version: 21
---

## Índice:

---

2

# Introdução

---

Nesta página, estão contidas as limitações conhecidas acerca da conversão de relatórios entre **RM Reports** e **Smart View**. Note que algumas das limitações contém formas de realizar as adaptações para que a conversão seja bem sucedida.

---

Controles ligados a Totalizadores

Se existir alguma **expressão** que possui ligação para algum controle de totalizador, a execução dessa expressão não será possível. Isso porque, a expressão é executada pelo GetData e o totalizador é executado somente na renderização do relatório pelo SmartView

### Exemplo de Não Conformidade

Se existir algum parâmetro de sentença sql ligado a um totalizador, a sentença não poderá ser executada pelo mesmo motivo

### Exemplo de Não Conformidade

---

## Totalizador e Sumário com campo sem dados no detalhe

Totalizadores e sumários que usem campos do detalhe, onde não possua dados na banda do campo selecionado, não terá o valor zerado por padrão.  
Exemplo: A Função “Suporte Técnico II” não possui Funcionários, e o totalizador da função utiliza o campo salário. No RM o resultado é 0,00, no Smart View, não existe valor para o campo.

### Exemplo de Não Conformidade

RM

Smart View

### Saída de contorno

Adicionar Texto de valor nulo, para ser exibido de acordo

Resultado:

## Totalizador de Página

Totalizadores de página não são suportados na migração, controles do tipo "Totalizador de página" terá apenas o layout convertido, porém não será exibido no relatório, sua propriedade de visibilidade será setada como invisível.

# Filtro

---

## Controle atrelado ao Texto Rico que possui formatação do tipo 'Geral'

A formatação do tipo 'Geral' de controles que estiverem atrelados ao Texto Rico não poderão ser exibidas no **Texto Rico**.

### Exemplo de Não Conformidade

---

50%

**Geração (Relatório não Conforme) - RM Reports**

50%

**Geração pós Conversão (Relatório não Conforme) - Smart View**

# Texto Rico

## Quebra de linha em texto dinâmico.

Texto Rico com texto dinâmico que usa quebra de linha "\par" não funciona no SmartView.

### Exemplo de Não Conformidade

No SmartView, ao invés de quebrar a linha, é impresso o valor "\par".

## Itens do Relatório e Função espelhados em Texto Rico

Controle Itens do Relatório e Funções não serão espelhados pelo Texto Rico após a conversão para o Smart View.

### Exemplo de Não Conformidade

# Binding Sentença SQL

---

## Binding de campo ligado a sentença SQL

Binding de campos ligados a sentenças SQL quando o alias de retorno contenha o caractere "." Ponto, Não terá correto funcionamento no Smart View.

### Exemplo de Não Conformidade

### Solução

Remova a pontuação nos alias da consulta para correto funcionamento.

# Tipos de Formatação por Extenso

---

A conversão dos tipos de formatação por extenso para os controles de Expressão, Fórmula e Totalizadores só está disponível nos tipos **Extenso** e **Extenso Monetário.** Os tipos "Extenso Monetário Cheque" e "Mês Extenso" não serão convertidos devido à limitações do Smart View.

---

Índicefalsefalse

**Produto:** Framework

false

**Versão:** 12.1.2310

false

**Processo:** Integração com o

falsefalseStatus

YellowEM DESENVOLVIMENTO
