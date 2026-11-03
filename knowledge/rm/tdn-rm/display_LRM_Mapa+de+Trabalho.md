---
content_hash: 4a52942835280e68edffda88859a6145219fcfd51703f43525f2a95f43da63a6
fetched_at: '2026-06-29T00:10:47.013380+00:00'
page_id: '556873017'
product: rm
source: tdn-rm
title: Mapa de Trabalho
type: documentation
url: https://tdn.totvs.com/display/LRM/Mapa+de+Trabalho
version: 27
---

1. **Visão Geral**
2. **Exemplo de utilização**

sumarioVisão Geral

## **01. VISÃO GERAL**

Para gerar, visualizar ou reprocessar um Mapa de Trabalho é necessário criar um mapa de trabalho. Em seguida, clicar em processos e "Gerar, Reprocessar Mapa de Trabalho". Escolher as amostras que serão incluídas no mapa e processar.

A partir da versão 12.1.2410 foram criados os relatórios padrão de:

* A partir da versão 12.1.2410, foram disponibilizados os relatórios padrão:

  + **Mapa de Trabalho – Grupo de Exames** (código: **SAUREL0155**): Para a utilização deste relatório, deve-se configurar o parâmetro **"Relatório de impressão do mapa de trabalho"**.
  + **Mapinha** (código: **SAUREL0153**): Neste caso, deve-se utilizar o parâmetro **"Relatório de Impressão do 'Mapinha'"**.

O relatório para o mapa é utilizado na impressão da tela de MAPA, e o relatório do Mapinha é usado na impressão do mapa na tela de pedido de exame.

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

falseMapa de TrabalhotrueCriação do Mapa de Trabalho

Para acessar a página clique em Unidade de diagnóstico > Mapa de trabalho:

Para adicionar um mapa escolha um departamento:

Processo Gerar Mapa

Para gerar um mapa clique em Processos e em seguida "Gerar, Reprocessar Mapa de Trabalho"

Em seguida escolha a opção Gerar Mapa

Escolha as amostras que serão incluídas:

Por fim, execute o processo:

Para verificar volte na visão e verifique se a quantidade foi alterada:

Visualizar Mapa

Antes de começar o processo de visualizar o mapa deve ser cadastrado um Report

Crie um novo relatório em Rm Reports com os campos COLIGADA e CODMAPA.

Em seguida, escolher esse Report que foi criado em Ambiente > Parâmetros > Gestão Hospitalar >Avançar  > Unidade de Diagnostico > Avançar >  > "Relatório de impressão mapa de trabalho"

Para visualizar um mapa clique em Processos e em seguida "Gerar, Reprocessar Mapa de Trabalho"

Em seguida escolha a opção Visualizar Mapa

As amostras que estão no mapa são apresentadas no segundo passo:

Por fim, execute o processo para o relatório ser gerado:

Reprocessar Mapa

Para Reprocessar um mapa selecione uma conta, clique em Processos e em seguida "Gerar, Reprocessar Mapa de Trabalho"

Em seguida escolha a opção Reprocessar

**Exclusão da amostra**

Escolha a opção "Exclusão de amostras" e selecione as contas que deseja remover do mapa de trabalho.

Por fim, execute o processo:

**Cancela Mapa de Trabalho**

Escolha a opção "Cancelamento do mapa", nessa rotina não será necessário selecionar nenhum conta.

Por fim execute o processo, todas as amostras devem ser removidas do mapa de trabalho e o mapa será cancelado.
