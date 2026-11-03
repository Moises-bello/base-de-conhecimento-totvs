---
content_hash: 775d22b5353f31f3ade5a05625c892e1aa13aaca52493640af8c2108ba97cb57
fetched_at: '2026-06-29T00:05:51.838685+00:00'
page_id: '1056136930'
product: rm
source: tdn-rm
title: TISS
type: documentation
url: https://tdn.totvs.com/display/LRM/TISS
version: 4
---

tissCadastrosvisaoGeralVisão Geral

Para faturamento de convênios que utilizam padrão ANS - TISS é necessário cadastrar as informações das Terminologias da ANS no menu **Cadastros/Uso Geral/TISS**

Alguns destes cadastros já são inseridos automaticamente na base de dados, via Atualizador.exe, sempre que é liberado uma nova versão TISS nos patch de mercado do Gestão Hospitalar.

versaoTissVersão TISS

Este menu é utilizado para cadastrar a versão TISS disponível para os convênios e os relatórios para impressão das respectivas guias.

Na Elaboração de contas do paciente é possível imprimir as guias selecionando a Parcial desejada e executando o processo "Imprimir guia no padrão ANS - TISS", vide explicação em  <https://tdn.totvs.com/x/GaJjIw>

centroconsumoidCentro de Consumo

Disponível a partir do Release 12.1.2606.

A versão TISS 4.03 criou uma nova terminologia chamada Terminologia de Centro de Consumo (tabela 82) que foi implementado no Release 12.1.2606 e será disponibilizado futuramente nos patch de mercado.

O Atualizador de base de dados irá executar as marcações abaixo para a criação das novas tabelas:

* Criação da tabela TISS/ANS-Centro de Consumo (SZANSCENTROCONSUMO), referente à Terminologia de Centro de Consumo (tabela 82), da versão 4.03.00 da TISS, **marcação SA.2026.02\_11**

* Criação da  tabela SZANSCENTROCONSUMOCORRELA utilizada no menu Cadastros/Uso Geral/TISS/Correlação Centro de Consumo, **marcação SA.2026.03\_06**

Não existe um menu para cadastrar centro de consumo, os registros são inseridos automaticamente pelo Atualizador.exe com os códigos e descrições fixas da ANS.

centroConsumoCorrelaCorrelação Centro de Consumo

Este menu estará disponível a partir do Release 12.1.2606.

Criação do menu Cadastros/Uso Geral/TISS/Correlação Centro de Consumo, para associar os códigos de centro de consumo da TISS-ANS (tabela 82) com os centros de custo do Gestão Hospitalar.

O campo Centro de Consumo será gravado nos arquivos XML e relatórios das guias: Guia de Resumo de Internação e Outras Despesas; Recurso de Glosa; Demonstrativo de Análise de Conta.
