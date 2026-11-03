---
content_hash: 09a821d4f0d984bc09d56816bf41eacc65fe9e62cb13edff0cb4f98a8f2a672a
fetched_at: '2026-06-29T00:11:18.316371+00:00'
page_id: '684996490'
product: rm
source: tdn-rm
title: Nota Orientativa nº 06/2021 - Leiaute S-1.0 - Revisão da tabela “21 – Códigos
  de Incidência Tributária da Rubrica”.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=684996490
version: 22
---

false

**A partir dos patches:**

* 12.1.33.257
* 12.1.34.156
* 12.1.2205.101
* e Superiores.

Objetivo:

Em 26/11/2021 foi disponibilizada a [Nota Orientativa S-1.0. 2021.06](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota_orientativa-s-1-0-06-2021.pdf), com orientações sobre a vigência dos itens de tabela do eSocial na transição de versões dos leiautes 2.5 e S-1.0.

*"**c) Criação de uma tabela para os códigos de incidência de Imposto de Renda e revisão dos códigos.***  
*Na versão 2.5 do leiaute os códigos de incidência de Imposto de Renda Retido na Fonte eram valores constantes do próprio campo {codIncIRRF} do leiaute do evento S-1010 (Tabela de Rubricas). Na versão S-1.0 os códigos de incidência de Imposto de Renda foram retirados do referido campo do evento e passaram a constar de tabela anexa (Tabela 21 - Códigos de Incidência Tributária da Rubrica para o IRRF) com algumas alterações em relação à versão anterior, com o fim de validade de alguns códigos e a criação de outros.*

*Durante o período de convivência das versões 2.5 e S-1.0, o empregador poderá enviar os eventos S-1200 e S-1210, com rubricas cadastradas em qualquer das versões. Os códigos de incidência relacionados para as rubricas no respectivo S-1010 serão aceitos.*

*Após fim do período de convivência, havendo rubricas cadastradas com código de incidência não vigente na Tabela 21 (da versão S-1.0), o empregador deverá atualizar as rubricas, nesta situação, com o envio do S-1010 utilizando os novos códigos (codIncIRRF) em vigor conforme a tabela 21.*

*As rubricas que referenciem os códigos relacionados na tabela abaixo deverão ser atualizadas, até o fim do período de convivência, para contemplar os códigos válidos na Tabela 21 da versão S-1.0. "*

|  |  |  |
| --- | --- | --- |
| CÓDIGOS COM FIM DE VIGÊNCIA | | |
| CÓDIGO | DESCRIÇÃO | NOVO CÓDIGO |
| 00 | Rendimento não tributável | 7XX |
| 01 | Rendimento não tributável em função de acordos internacionais de bitributação | 1X |
| 15 | Rendimentos Recebidos Acumuladamente - RRA | 1X |
| 35 | Rendimentos Recebidos Acumuladamente - RRA | 3X |
| 44 | PSO - RRA | 4X |
| 55 | Pensão alimentícia - RRA | 5X |
| 78 | Valores pagos a titular ou sócio de microempresa ou empresa de pequeno porte, exceto pró-labore e aluguéis | (não informado no eSocial) |
| 81 | Depósito judicial | 98XX |
| 82 | Compensação judicial do ano-calendário | 9082 |
| 83 | Compensação judicial de anos anteriores | 9083 |
| 91 | Remuneração mensal | 9011 |
| 92 | 13º salário | 9012 |
| 93 | Férias | 9013 |
| 94 | PLR | 9014 |
| 95 | RRA | 90XX |

## **Seguem orientações referente ao produto TOTVS Folha de Pagamento para atender essa alteração:**

true2AlteraçõesAlterações1true1Passo 1Passo 1

Tag <codIncIRRF> igual = "00 - Rendimento não tributável"

1) Acesse o menu**RH | Folha de Pagamento | Gestão | Visões de Dados** e inclua uma consulta, conforme **Print B** abaixo:

**Print A**

**Código:** SEMINCIRFF

**Título:** SEM INCINDÊNCIA DE IRFF

**Consulta:** SELECT CODIGO FROM PEVENTO

WHERE PROVDESCBASE = 'P'

AND INCIRRF = 0

AND INCIRRF13 = 0

AND INCIRRFFERIAS = 0

AND INCIRRFSUSPENSAO IS NULL AND INCIRRFISENCAO IS NULL AND (INCIRRFFORCADA IS NULL OR INCIRRFFORCADA = '00')

AND (RENDNAOTRIBACORDOINTERNAC IS NULL OR RENDNAOTRIBACORDOINTERNAC = 0)

AND CODCOLIGADA = (SELECT CODCOLIGADA FROM GCOLIGADA WHERE CODCOLIGADA = :$CODCOLIGADA)

**Print B**

2) Acesse o menu**RH | Folha de Pagamento | Administração de Pessoal | Eventos | Eventos** e crie o filtro associando a SQL mencionada acima no item 1):

**Print A**

**Print B**

**Print C**

Edite o evento desejado e preencha a nova incidência conforme orientado [Nota Orientativa S-1.0. 2021.06](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota_orientativa-s-1-0-06-2021.pdf).

Após salvar a alteração o sistema irá gerar um gatilho de alteração dessa rubrica que deverá ser enviada ao RET.

2Passo 2Passo 2

Tag <codIncIRRF> igual = "01 - Rendimento não tributável em função de acordos internacionais de bitributação"

1) Acesse o menu**RH | Folha de Pagamento | Administração de Pessoal | Eventos | Eventos** e caso possua Rendimento não tributável em função de acordos internacionais de bitributação, crie um filtro, conforme **Print B** abaixo:

**Print A**

**Print B**

Edite o evento desejado e desmarque o campo "Rendimento não tributável em função de acordos internacionais de bitributação" e marque a incidência correspondente.

Após salvar a alteração o sistema irá gerar um gatilho de alteração dessa rubrica que deverá ser enviada ao RET.

3Passo 3Passo 3

Validação de diferenças pendentes.  Esse passo deverá ser realizado após o envio dos eventos criados pelos passos 1 e 2 acima mencionados.

1) Acesse o menu**RH | Folha de Pagamento | eSocial | Outros Processos | Comparativo de Incidências de Rubricas** e selecione os campos conforme **Print B** abaixo:

**Print A**

**Print B**

Clique na opção **"Exibir Visão do Resultado"**:

Sistema irá apresentar a listagem dos eventos restantes para ajuste:

Acesse oprocesso **"Gerar gatilho de rubricas divergentes entre último XML e base"** para que o sistema gere gatilho de alteração dessas rubricas que deverão ser enviadas ao RET.
