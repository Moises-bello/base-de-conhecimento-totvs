---
article_id: 1500003167281
category: Gestão de Frotas
content_hash: 6730e15856ff4f3861c630d468c664453598e578955521038142f75141a4a6f8
fetched_at: '2026-06-28T22:42:39.289827+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Alterar tamanho do campo Valor Unitário
  Combustível
type: support-article
updated_at: '2021-08-13T16:47:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003167281-Manufatura-Linha-Protheus-MNT-Alterar-tamanho-do-campo-Valor-Unit%C3%A1rio-Combust%C3%ADvel
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:45 min****Dúvida**Como alterar o tamanho dos campos referentes ao **Abastecimento Manual - MNTA655**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas - Todas as versões  
  
**Solução**Para realizar o procedimento é necessário seguir os passos abaixo:

1. Acessar o **Configurador - SIGACFG**;
2. Ir em **Base de Dados / Dicionário / Bases de Dados - CFGX031**;
3. Selecionar sobre **Dicionário de dados**;
4. O Sistema exibe todas as tabelas para alteração do compartilhamento das tabelas e de seus respectivos campos.
5. Buscar pela Tabela **TQN - Entrada Manual Abastecimento** e clicar sobre **Editar**;
6. Posicionar sobre o campo **TQN\_VALUNI - Valor Unitário** e alterar o campo **Decimal** para **cinco - 5**;
7. Buscar pela Tabela **TQH - Preços dos Combustíveis** e clicar sobre **Editar**;
8. Posicionar sobre os campos **TQH\_PREBOM - Preço Bomba** e **TQH\_PRENEG - Preço Negociado** e alterar em ambos o campo **Decimal** para **cinco - 5**.

**Exemplo**Contextualizando o ajuste supracitado dentro de um abastecimento onde o valor do combustível oscila entre três e seis casas posteriores à vírgula e a quantidade de abastecimento é única e 501 litros.  
 **Primeira situação:**

* Quantidade de abastecimento 501.
* Para valor unitário de combustível com três casas após a vírgula. Exemplo: R$ 2,994
* Total: 501 \* 2,994 = R$1.499,994

**Segunda situação:**

* Quantidade de abastecimento 501.
* Para valor unitário de combustível com quatro casas após a vírgula. Exemplo: R$ 2,9940
* Total: 501 \* 2,9940 = R$1.499,9940

**Terceira situação:**

* Quantidade de abastecimento 501.
* Para valor unitário de combustível com cinco casas após a vírgula. Exemplo: R$ 2,99401
* Total: 501 \* 2,99401 = R$1.499,99901

**Importante**  
Nota-se a partir dos exemplos acima, que a cada casa decimal adicionada aos campos relacionados ao abastecimento, mais o valor se aproxima de um total de R$1.500,00.
