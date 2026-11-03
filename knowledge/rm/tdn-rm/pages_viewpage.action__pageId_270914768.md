---
content_hash: 483e28c7843dc3476c224412badd756cb475c48b520460e9f2133dae842e6d44
fetched_at: '2026-06-29T00:08:25.439023+00:00'
page_id: '270914768'
product: rm
source: tdn-rm
title: RMEDU00002_Emissão de Boletos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270914768
version: 11
---

Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Educacional |
| **Versões:** | Todas as versões |
| **Passo a passo:** | Emissão de Boletos - Portal do Aluno |

Requisitos:

Conhecimentos no RM Reports, Consultas SQL e criação de Fórmula

Criação das Fórmulas IPTE e Código de Barras

Serviços Globais | Fórmulas

Criar um filtro para exibição somente das fórmulas do Gestão Financeira

Mudar o sistema

Criação das Fórmulas

IPTE

Campos

Código, recomendamos que o código seja intuitivo para facilitar a identificação

Título, recomendamos que o código seja intuitivo para facilitar a identificação

Conteúdo padrão da Fórmula

IPTEBOLETO (-1)

Código de Barras

Campos

Código, recomendamos que o código seja intuitivo para facilitar a identificação

Título, recomendamos que o código seja intuitivo para facilitar a identificação

Conteúdo padrão da Formula

CODBARRABOLETO (-1)

Criação da Consulta SQL para utilização no Relatório

Gestão | Visão de dados

Criação do Filtro para listar somente as consultas criadas para o TOTVS Gestão Financeira

Criação da consulta SQL

Campos

Código, recomendamos que o código seja intuitivo para facilitar a identificação

Título, recomendamos que o código seja intuitivo para facilitar a identificação

Aplicação, deve ser apontado para o TOTVS Gestão Financeira (RM Fluxus)

Conteúdo padrão da SQL

Será necessário incluir a consulta SQL que retorne o resultado da fórmula criada.

Abaixo a sintaxe da consulta:

SELECT CAST(:CODBAR AS VARCHAR(100)) AS BOLETO  
FROM FLAN  
WHERE FLAN.CODCOLIGADA = :CODCOLIGADA  
AND FLAN.IDBOLETO = :IDBOLETO

***Deverá se atentar para a criação da consulta SQL e Fórmulas no TOTVS Gestão Financeira***

Criação do Relatório

Gestão | RM Reports

Criação do Filtro para listar somente Relatórios do Gestão Financeira

Criação do Relatório

Campos

Código, recomendamos que o código seja intuitivo para facilitar a identificação

Descrição, recomendamos que o código seja intuitivo para facilitar a identificação

Tipo, 81 – Boleto de Cobrança Bancária

Aplicação, deve ser apontado para o TOTVS Gestão Financeira (RM Fluxus)

Adicionar as Formulas no Relatório

Fórmula de IPTE

1 – Selecionar a Função de Formula e clicar no >

2 – clicar em (...) para listar as formulas criadas

3 – Localizar a formula criada para geração do IPTE

4 – Ok

1 – Selecionar função de formula

2 – Selecionar Grade de Propriedades

3 – Alterar o nome do campo idêntico ao código da fórmula criada

3 – Altere o nome do Design para IPTEBOL idêntico ao da formula

Formula de Código de Barras

1 – Selecionar a Função de Formula e clicar no >

2 – clicar em (...) para listar as formulas criadas

3 – Localizar a formula criada para geração do Código de Barras

4 – Ok

1 – Selecionar função de formula

2 – Selecionar Grade de Propriedades

3 – Alterar o nome do campo idêntico ao código da fórmula criada

4 – Altere o nome do Design para CODBAR idêntico ao da formula e do retorno da consulta SQL.

Adicionar SQL no Relatório

1 – Adicionar Fonte de Dados

2 – Sentença SQL

Localizar consulta pelo código

3 – Selecionar a consulta

4 – Adicionar

5 – Ok

Adicionar tabela máster

O relatório deverá ter a sua tabela Master definida como FBOLETO

1 – Tabela da base

2 – FBOLETO

3 – Boletos

4 – Adicionar

5 – Ok

Expandir os campos da tabela

Adicionar o campo da tabela Código da Coligada no detalhe 1 do relatório

Alterar a descrição do campo nas propriedades

1 – Selecionar o campo (Boletos.Código da Coligada) inserido no relatório

2 – Selecionar Grade de Propriedades

3 – Alterar o nome para o retorno da consulta SQL (CODCOLIGADA)

Adicionar o campo Boletos.Referência do registros no detalhe 1 do relatório

Alterar a descrição do campo nas propriedades

1 – Selecionar o campo (Boletos.Referência do Registros) inserido no relatório

2 – Selecionar Grade de Propriedades

3 – Alterar o nome para o retorno da consulta SQL (IDBOLETO)

Inserir o componente Código de Barras

Caixa de Ferramenta | Controles Padrões | Código de Barras

Configurar Propriedades do código de barras

Texto

Ligar a função inserida ao relatório com a retorno da consulta SQL

Alterar a simbologia da função

1 – Clicar na função

2 – Selecionar a Grade de Propriedades

3 – Selecionar a opção simbologia

4 – Calcular uma Soma, mudar de Sim para “Não”

Alterar na Grade de Propriedades - Design do campo, inserindo o retorno da consulta SQL

1 – Selecionar a função código de barras inserida no relatório

2 – Seleciona Grade de Propriedades

3 – Design - Nome

4 – Alterar o nome do campo para CODBAR (nome da Formula e do retorno da SQL)

Ordenar execução das funções

As formulas sempre devem ser organizadas antes da consulta SQL, para movimentar as funções selecionar e usar as setas no lado direito.

Informar o relatório criado no TOTVS Gestão financeira nos parâmetros do TOTVS Educacional

Configurações | Parâmetros

Acessar o Portal do Aluno

Educacional

Financeiro

Extrato Financeiro

Clicar no ícone de boleto
