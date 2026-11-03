---
content_hash: b296ca148f621060d8ce665f4ecf7f54261f028841a91922cc9f377b6a9ac987
fetched_at: '2026-06-29T00:05:51.710340+00:00'
page_id: '1053192192'
product: rm
source: tdn-rm
title: Registro 1400 - Anual
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+1400+-+Anual
version: 27
---

#FFA500#FFFACD#FFE766dashedAviso Importante:1%99%

O registro denominado **“1400 Anual”** não corresponde a uma simples totalização dos registros 1400 gerados anteriormente ao longo do período. É importante destacar que ele não deve ser confundido com o registro 1400 de apuração mensal.

A utilização do registro 1400 na modalidade anual se justifica pelo fato de que determinadas Unidades Federativas (UFs) têm exigido a geração de um registro adicional ao final do exercício, ou em situações específicas, como processos de cisão, fusão, entre outros eventos societários.  
  
O Registro Anual deve ser gerado apenas quando exigido por sua Unidade Federativa, nesses casos, é necessária a apresentação da **totalização da Receita Bruta** em um único registro consolidado.

## Conteúdo

Conteúdonone

# 1. Visão geral

O Registro 1400 – Informação sobre Valores Agregados tem como finalidade fornecer informações para o cálculo do valor adicionado por município, sendo utilizado pelos Estados para determinar os índices de participação dos municípios (IPM) na arrecadação do ICMS.

Atualmente, o módulo fiscal já contempla a geração do Registro 1400 com periodicidade mensal, utilizado pelas UFs que exigem essa informação no arquivo do SPED Fiscal de cada período de apuração.

Entretanto, conforme legislações específicas publicadas pelo Estado do Rio de Janeiro (RJ), passou a ser obrigatória a entrega anual do Registro 1400, contendo o valor total da receita bruta auferida pelo estabelecimento no exercício corrente, a ser apresentado no mês de dezembro ou no mês de baixa da inscrição estadual.

# 2. Parametrização

Relatórios

Para geração do Registro 1400 acesse o menu Cadastros | Parâmetros de Processos

Imagem

Inclua um parâmetro de processo informando:

**Processo =** EFD - ICMS/IPI

**Grupo do Processo** = registro 1400 - Anual e

**Data Inicial =** Informe o período desejado

Imagem

Após o cadastro do Parâmetro de processo acesse o Menu Anexos | Filtro por Natureza

Imagem

Inclua as naturezas que devem ser consideradas na geração do 1400 anual e informe qual o campo de valor deve ser utilizado.

Imagem

# 3. Geração da Rotina

Na tela de geração da rotina pasta Personalização marque o parâmetro **Gera Registro: 1400 anual** e preencha o campo **Código do item IPM.**

visaoImagem

# 4. Regras

* Vão ser considerados os lançamentos com base nas **Naturezas** e Período do **Parâmetro de Processos** cadastrado.
* Não serão considerados lançamentos Cancelados ou Estornados.
* O registro [1400 Mensal](https://tdn.totvs.com/display/LRM/SPED+Fiscal+-+Bloco+1) continua sendo gerado, dessa forma vão ser gerados os 1400 mensais e também o 1400 anual quando parametrizado.
* Não ocorreram Alterações no 1400 Mensal que já era gerado, este possui outras regras de geração que podem ser consultadas na documentação -> [1400 Mensal](https://tdn.totvs.com/display/LRM/SPED+Fiscal+-+Bloco+1).   
  Já para o 1400 Anual deve ser realizada a parametrização informada nos itens 2 e 3 desta documentação.

# 5. Origem dos dados

VisaoDeDadosPasso 1

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem do dado** |
| 01 | REG | Texto fixo contendo "1400" | Valor fixo “1400” |
| 02 | COD\_ITEM\_IPM | Identificação de itens para fins de apuração do **Índice de Participação dos Municípios (IPM)** | Será gerado com base no valor informado pelo usuário no campo *“Código do Item IPM”*, disponível na tela de parametrização da rotina, na aba **Personalização**. |
| 03 | MUN | Código do município da filial (código IBGE) |  |
| 04 | VALOR | Valor total anual apurado para o município da filial. |  |

# 6. Registro gerado.
