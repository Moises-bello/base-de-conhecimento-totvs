---
content_hash: 4c5af94cb21673ab85a7cbfa73286fd530a75671b4ec8e52ba4dabfadf5809f2
fetched_at: '2026-06-29T00:11:27.264444+00:00'
page_id: '721718394'
product: rm
source: tdn-rm
title: RPT00047 - Ordem de Execução das Bandas e Controles
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=721718394
version: 34
---

# Índice:

---

.\*ndice:

# Introdução

---

Este documento tem como objetivo explicar a ordem de execução das bandas e dos controles no RM Report. Antes de mais nada precisamos entender o que é **Fonte de Dados, Bandas e** **Controles.** Para depois entendermos o momento de execução de cada um deles.

deck1Fonte de Dados

A **Fonte de Dados,** como o próprio nome sugere, são os dados que serão impressos em um relatório. Esses dados podem ser oriundos de **Tabela da Base**, **Sentença SQL** ou **Provedor de Dados**.

| Fonte de Dados: Tabela da Base | Fonte de Dados: Sentença SQL | Fonte de Dados: **Provedor de Dados** |
| --- | --- | --- |
|  |  |  |

Bandas

As **bandas** são faixas que podem ser inseridas no layout do relatório. São exemplos de bandas: Cabeçalho de Página, Detalhe, Rodapé de Página, Cabeçalho do Detalhe, Rodapé do Detalhe.

Controles

Os **controles** de relatório são elementos básicos que você pode arrastar e soltar nas bandas (faixas) do relatório, associar a fonte de dados, organizar e personalizar para construir um layout de relatório. São exemplos de controles: Texto, Totalizador, Expressão, Fórmula, entre outros.

# Entendendo o Momento da Extração da Fonte de Dados

---

A extração da **fonte de dados** é realizada e mantida em memória antes mesmo da renderização da banda em que está vinculada. No exemplo ilustrado abaixo temos uma fonte de dados **Tabela da Base** vinculada à **Banda de Detalhe1**.

Nas propriedades da **Banda de Detalhe** conseguimos ver se ela possui uma ligação de **Fonte de Dados**. Neste exemplo a fonte de dados é a tabela de Funcionários (PFUNC).

Como a extração da **Fonte de Dados** acontece em um momento anterior à impressão da **Banda de Detalhe** (vinculada a fonte de dados), podemos utilizar suas informações em uma [formatação condicional](https://tdn.totvs.com/x/o4KFDg), por exemplo para colorir o fundo do detalhe de acordo com um determinado valor.

Exemplo de uma formatação condicional utilizando um campo da Fonte de Dados:

Aplicando a formatação Condicional, apenas o detalhe do funcionário de chapa 00001 ficou com o fundo vermelho.

# Entendendo a Ordem de Execução dos Controles

---

Inicialmente os controles são impressos levando em consideração a ordem que os mesmos foram adicionados no layout do relatório, mas esta ordem pode ser alterada através do menu **Ordenação de Controles**. Essa ordem é muito importante, pois um **Controle A**, por exemplo, pode utilizar dados do **Controle B** e neste caso temos que garantir que o **Controle B** seja executado antes do **Controle A**. Isso é possivel através do recurso menu **Ordenação de Controles**.

Ao contrário da Fonte de Dados, os controles são executados em um momento posterior à execução da Banda de Detalhe.

Vamos imaginar o seguinte cenário para facilitar o entendimento: Temos um relatório que lista os dependentes de cada funcionário.

* Na **Banda de Detalhe de Funcionários** temos um controle **Expressão\_Tempo\_Serviço** que calcula o tempo de serviço do funcionário;
* Criamos uma Formatação condicional **FormataçãoCondicional1** que utiliza o controle **Expressão\_Tempo\_Serviço.**

1. Não podemos aplicarmos a Formatação Condicional **FormataçãoCondicional1** na **Banda de Detalhe de Funcionários**, pois a formatação utiliza o controle **Expressão\_Tempo\_Serviço** que está na **Banda de Detalhe de Funcionários.**
2. Podemos aplicar a Formatação Condicional **FormataçãoCondicional1** na **Banda de Detalhe de Dependentes**, pois esta banda é impressa após o controle **Expressão\_Tempo\_Serviço** ser executado.

Exemplo de uma formatação condicional utilizando um Controle:

Após aplicar a formatação condicional na **Banda de Detalhe de Dependentes** apenas dependentes de funcionários com 32 anos ou mais de serviço foram coloridos de amarelo corretamente.

# Entendendo a Ordem de Execução das Bandas

---

Abaixo segue exemplo de um relatório que lista os funcionários e seus respectivos dependentes.

A ordem de execução das bandas é a seguinte:

1. CabeçalhodePágina1
2. CabeçalhodoDetalhe1
3. Detalhe1  
   1. SubDetalhe1
   2. CabeçalhodoDetalhe2
   3. Detalhe2
4. RodapédePágina1

Obs: No momento da impressão de cada Banda de Detalhe os controles contidos nela são impressos na ordem explicada no tópico **Entendendo a Ordem de Execução dos Controles.**

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.34

false

**Processo:** Ordem de Execução dos Controlese Bandas

falsefalse

**Status:** Concluído

false

**Data:**

false

**Autores:**
