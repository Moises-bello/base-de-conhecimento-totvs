---
content_hash: a71dc247dd88936c210de4d50c793239168abd0b975d7ae5644e99436d7e70fc
fetched_at: '2026-06-29T00:11:49.474037+00:00'
page_id: '834247089'
product: rm
source: tdn-rm
title: DT - FGTS Digital - Lançamento Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=834247089
version: 48
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | FGTS Digital - Lançamento Financeiro |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-9385](https://jiraproducao.totvs.com.br/browse/DRHROTRM-9385) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2306.254
* 12.1.2310.198
* 12.1.2402.138 e superiores

## **03.****SITUAÇÃO/REQUISITO**

Implementar no produto TOTVS Folha de Pagamento a geração do lançamento financeiro compatível com as normas do FGTS Digital, atendendo a geração mensal e rescisória. 

## **04. SOLUÇÃO**

Com a introdução do FGTS Digital, tornou-se necessário dissociar a geração do lançamento financeiro dos processos da SEFIP e GRRF. Isso exigiu a criação de um novo tipo de lançamento financeiro denominado "**24-Total Guia FGTS Digital**".

Os desligamentos que ocorrem a partir de 01/03/2024, o recolhimento do FGTS Mensal, Rescisório e Indenização Compensatória (multa do FGTS) passam a ser através do FGTS Digital. Não existindo mais a nomenclatura GRRF – Guia de Recolhimento Rescisório do FGTS. A guia passa a ser chamada de **GFD – Guia do FGTS Digital.**

Para composição dos valores a serem gerados, o sistema irá calcular os valores do FGTS folha, FGTS 13o. Terceiro e FGTS Indenizado.

## **Tratativa realizada no produto**

**IMPORTANTE**: Após a atualização da versão será necessário executar o sistema **RM.Atualizador.exe.** para a criação do novo tipo de lançamento financeiro.

Criado o tipo de lançamento "**24-Total Guia FGTS Digital**", para atender o cálculo da guia do FGTS Digital.

**PONTOS IMPORTANTES:**

1. Serão considerados os códigos de cálculos [27](https://tdn.totvs.com/pages/releaseview.action?pageId=452718588) e [148](https://tdn.totvs.com/pages/releaseview.action?pageId=452718594) para buscar o mês anterior a demissão.
2. Quando houver retificação da rescisão ou pagamento após a rescisão, os valores serão enviados no tipo Mensal, conforme descrito no site [Perguntas e Respostas 04.09](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/perguntas-frequentes#Rescisorio).
3. A quebra na geração será de acordo com os parâmetros de seleção do processo do Lançamento Financeiro.
4. Quando o lançamento financeiro for agrupado por lotação tributária (tomador de serviço), é fundamental executar o Relatório de Conferência de FGTS para alimentar a tabela PESOCIALTOTAISLOTACAO. Isso é essencial para evitar problemas de desempenho na geração do lançamento. Caso essa etapa não tenha sido realizada, ao gerar o lançamento financeiro, será exibida a seguinte mensagem: "**O lançamento "Total Guia FGTS Digital" está parametrizado por lotação tributária, é preciso executar o Relatório de Conferência de FGTS antes de gerar o lançamento para a chapa XXX.**"

**1)** Será possível definir o tipo de lançamento a ser realizado, conforme descrito no [Manual de Orientação do FGTS DIGITAL - Página 80](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-do-orientacao-do-fgts-digital-versao-1-1-01-03-2024.pdf). Podendo ser parametrizado conforme abaixo:

* **Mensal**

Ao selecionar esse tipo, o sistema irá gerar o lançamento considerando todos os funcionários, inclusive demitidos, com exceção dos demitidos com os tipos de demissão com direito a saque de FGTS.

* **Rescisório**

Ao selecionar esse tipo, o sistema irá gerar o lançamento considerando todos os funcionários demitidos com o tipo de demissão que tem direito a saque de FGTS e que possuem o parâmetro “**FGTS Mês anterior será recolhido na GRRF/FGTS Digital**“ desmarcado na rescisão.

* **Rescisório + Mensal**

Ao selecionar esse tipo, o sistema irá gerar o lançamento considerando todos os funcionários demitidos com o tipo de demissão que tem direito a saque de FGTS e que possuem o parâmetro “**FGTS Mês anterior será recolhido na GRRF/FGTS Digital**“ marcado na rescisão, considerando o mês da demissão e o mês anterior a demissão. Para atender a situação descrita no [Manual de Orientação do FGTS DIGITAL - Página 80](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-do-orientacao-do-fgts-digital-versao-1-1-01-03-2024.pdf).

Conforme Manual de Orientação do FGTS Digital, existem apenas dois tipos de valor que influenciam na apuração do FGTS (tpValor): Mensal e Rescisório, conforme [Página 72](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-do-orientacao-do-fgts-digital-versao-1-1-01-03-2024.pdf), diante disso não criamos o tipo de 13o. Salário.

**2)** **Agrupamentos**

* Agrupar por seção: Os lançamentos serão feitos com base na filial associada à seção do funcionário.
* Agrupar por coligada: Um único lançamento será feito utilizando a coligada atual.
* Agrupar por lotação: Os lançamentos serão feitos de acordo com as lotações tributárias. Lembrando que, é fundamental executar o Relatório de Conferência de FGTS para alimentar a tabela PESOCIALTOTAISLOTACAO.

**3) Cálculo da** **Multa Rescisória (Indenização Compulsória)**

**3.1)** Precisaremos realizar o cálculo, pois o valor não é retornado no evento "S-5003 - Informações do FGTS por Trabalhador" do eSocial. Esses valores são gerados diretamente pela plataforma do FGTS Digital no módulo 4, "Remunerações para Fins Rescisórios". Diante disso, iremos reproduzir o mesmo cálculo, que consiste em:

| Campo | Produto |
| --- | --- |
| Saldo Rescisório FGTS | PFUNC.SALDOFGTS |
| FGTS folha | Serviço da Máquina de Cálculo |
| FGTS 13o. Sal. | Serviço da Máquina de Cálculo |
| FGTS Indenizado | Serviço da Máquina de Cálculo |

**3.2)** O cálculo será a soma dos campos acima multiplicado pelo percentual da multa (40% ou 20%).

**3.3)** Serão considerados somente os códigos de desligamentos que é aplicado o percentual de multa calculada pelo FGTS Digital, ou seja, os motivos que geram direito ao saque do FGTS, conforme descrito no [Manual de Orientação do FGTS Digital](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-do-orientacao-do-fgts-digital-versao-1-1-01-03-2024.pdf) (página 36)

**Tabela com percentual de multa calculada pelo FGTS Digital em desligamentos**

| Código do Desligamento FGTS DIGITAL | Código do Desligamento PRODUTO | Descrição do desligamento | % |
| --- | --- | --- | --- |
| 2 | 2 | Rescisão sem justa causa, por iniciativa do empregador | 40 |
| 3 | 2 e PFUNC.TEMPRAZOCONTR seja  1 e PFUNC.FIMPRAZOCONTR seja maior que PFUNC.DTDESLIGDTDESLIGAMENTO | Rescisão antecipada do contrato a termo por iniciativa do empregador | 40 |
| 5 | C | Rescisão por culpa recíproca | 20 |
| 14 |  | Rescisão do contrato de trabalho por encerramento da empresa, de seus estabelecimentos ou supressão de parte de suas atividades ou falecimento do empregador individual ou empregador doméstico sem continuação da atividade | 40 |
| 17 | N | Rescisão indireta do contrato de trabalho | 40 |
| 26 |  | Rescisão do contrato de trabalho por paralisação temporária ou definitiva da empresa, estabelecimento ou parte das atividades motivada por atos de autoridade municipal, estadual ou federal | 40 |
| 27 | G | Rescisão por motivo de força maior | 20 |
| 33 | V | Rescisão por acordo entre as partes (art. 484-A da CLT) | 20 |
| 47 |  | Rescisão do contrato de trabalho por encerramento da empresa, de seus estabelecimentos ou supressão de parte de suas atividades | 40 |
| 48 |  | Falecimento do empregador individual sem continuação da atividade | 40 |

**3.4)** Dependendo do motivo de desligamento, haverá o cálculo automático da multa para as seguintes categorias:

| Categoria | Descrição |
| --- | --- |
| 101 a 111 | (1xx - Empregado e Trabalhador Temporário) |
| 721 | (Contribuinte individual – Diretor não empregado, com FGTS) |

**3.5)**Não haverá cálculo de multa para as categorias abaixo:

| Categoria | Descrição |
| --- | --- |
| 201 a 202 | (Avulso) |
| 301 a 314 | (3xx - Agente Público) |
| 401 e 410 | (Cessão) |
| 701 a 781 | exceto 721 (7xx – Contribuinte Individual) |
| 901 a 906 | (Bolsista) |

## **5. EXEMPLO DE UTILIZAÇÃO**

Aba 1true1MENSALMENSAL

**1)** Acesse Administração de Pessoal | Cadastros Globais | Tabela dinâmicas e crie o lançamento ativo para os lançamentos, conforme demonstrado abaixo:

**OBSERVAÇÃO:** Criamos no exemplo como sugestão três tipo de lançamentos ativos, 07 - Mensal, 08 - Rescisório e 09 Rescisório + Folha.

**2)** Acesse Encargos | Cadastros Financeiros | Parâmetros e crie a parametrização conforme demonstrado abaixo:

* Tipo do lançamento financeiro: "24 - Total Guia FGTS Digital"
* Opção marcada: "Mensal" no parâmetro "Gerar Guia para o Tipo".

Na aba "Parâmetros" no item "Agrupamentos" marcar para gerar um único lançamento por coligada.

Na aba "Lançamentos Ativos" deverá marcar "MENSAL"

**3)** Acesse o menu Encargos | Geração dos Lançamentos

Através dessa tela, é possível realizar a parametrização para todos os funcionários ou fazer a seleção. No exemplo abaixo, faremos o lançamento mensal apenas para uma chapa específica.

Nessa tela marcamos o lançamento ativo criado no item 1 e associado no item 2

O processo é finalizado com sucesso e a aba de debug está disponível, mostrando os valores encontrados.

Exemplo do lote gerado:

2RESCISÓRIO COM SAQUE FGTSRESCISÓRIO COM SAQUE FGTS

1) Acesse Administração de pessoal | Cadastros Globais | Tabela dinâmicas e crie o lançamento ativo para os lançamentos

OBSERVAÇÃO: Criamos no exemplo como sugestão três tipo de lançamentos ativos, 07 - Mensal, 08 - Rescisório e 09 Rescisório + Folha.

2) Acesse Encargos | Cadastros Financeiros | Parâmetros

Criado a parametrização, note que o tipo do lançamento financeiro deverá ser - 24 - Total Guia FGTS Digital e foi marcada a opção Gerar Guia para o tipo: Rescisório.

Em agrupamento foi marcado para gerar um único lançamento por coligada.

Em lançamento ativo marcado o RESCISORIO

3)Acesse Encargos | Geração dos Lançamentos

Nessa tela pode ser realizado para todos os funcionários ou realizar a seleção no exemplo abaixo faremos o lançamento rescisório para somente uma chapa

Nessa tela marcamos o lançamento ativo criado no item 1 e associado no item 2

Processo é finalizado com sucesso e tem disponível a aba debug com os valores encontrados

Exemplo do lote gerado

3RESCISÓRIO COM SAQUE FGTS + MENSALRESCISÓRIO COM SAQUE FGTS + MENSAL

1) Acesse Administração de pessoal | Cadastros Globais | Tabela dinâmicas e crie o lançamento ativo para os lançamentos

OBSERVAÇÃO: Criamos no exemplo como sugestão três tipo de lançamentos ativos, 07 - Mensal, 08 - Rescisório e 09 Rescisório + Folha.

2) Acesse Encargos | Cadastros Financeiros | Parâmetros

Criado a parametrização, note que o tipo do lançamento financeiro deverá ser - 24 - Total Guia FGTS Digital e foi marcada a opção Gerar Guia para o tipo: Rescisório + Mensal (somente demitido)

Em agrupamento foi marcado para gerar um único lançamento por coligada.

Em lançamento ativo marcado o RESCISORIO + MENSAL

3)Acesse Encargos | Geração dos Lançamentos

Nessa tela pode ser realizado para todos os funcionários ou realizar a seleção no exemplo abaixo faremos o lançamento rescisório + mensal para somente uma chapa

Nessa tela marcamos o lançamento ativo criado no item 1 e associado no item 2

Processo é finalizado com sucesso e tem disponível a aba debug com os valores encontrados

Exemplo do lote gerado

Importante: só será gerado com o tipo Digital Rescisório + Mensal (somente demitido) caso o funcionário tenha marcado na sua rescisão a flag **FGTS Mês anterior será recolhido na GRRF/FGTS**

## **5. DEMAIS INFORMAÇÕES**

[Folha Analítica](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719339)

## **6. DEMAIS INFORMAÇÕES**

Webinar: <https://www.youtube.com/watch?v=uw71WNl0P-8>

How To: <https://www.youtube.com/watch?v=FGSBi39urRI>

<https://www.totvs.com/blog/fiscal-clientes/fgts-digital-construcao-da-base-para-fins-rescisorios/>

<https://www.totvs.com/blog/fiscal-clientes/fgts-digital-orientacao-em-situacao-de-contingencia/>

[PERGUNTAS E RESPOSTA GOVERNO](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/perguntas-frequentes#Rescisorio)

[Cadastros Financeiros](https://tdn.totvs.com.br/display/LRM/Cadastros+Financeiros)

[MANUAL DE ORIENTAÇÃO DO FGTS DIGITAL](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-do-orientacao-do-fgts-digital-versao-1-1-01-03-2024.pdf)
