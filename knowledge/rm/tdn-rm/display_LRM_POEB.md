---
content_hash: 28fe0d149b532f81285b4740005bd8237ce59e7bc180a83b731272cce321d8c0
fetched_at: '2026-06-29T00:09:45.428657+00:00'
page_id: '433242188'
product: rm
source: tdn-rm
title: POEB
type: documentation
url: https://tdn.totvs.com/display/LRM/POEB
version: 29
---

# Conteúdo

## 2Conteúdononenone

# 1. Introdução

Com base na [Instrução Normativa RFB Nº 1394, de 12 de Setembro de 2013](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?visao=anotado&idAto=45931) o cálculo da POEB no sistema é realizado conforme orientação do artigo 4º como segue:  
  
"Art. 4º A POEB de que trata o inciso III do § 2º do art. 3º deverá ser calculada:  
I - em março, com base nos dados do 1º (primeiro) semestre do ano-calendário; e  
II - em setembro, com base nos dados do 2º (segundo) semestre do ano-calendário.  
§ 1º A POEB anual deverá ser calculada da seguinte forma:  
  
  
  
§ 2º O estoque de bolsas relativas a anos anteriores será considerado no cálculo da proporção de ocupação efetiva de que trata este artigo.  
§ 3º Caso o Ministério da Educação determine o encerramento das etapas do processo seletivo do Prouni para datas posteriores aos prazos estabelecidos no caput, a POEB deverá ser calculada: [(Incluído(a) pelo(a) Instrução Normativa RFB nº 2083, de 23 de maio de 2022)](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=124142#2341639)  [(Vide Instrução Normativa RFB nº 2083, de 23 de maio de 2022)](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=124142#2341665)  
I - em abril, com base nos dados do 1º (primeiro) semestre do ano-calendário; e [(Incluído(a) pelo(a) Instrução Normativa RFB nº 2083, de 23 de maio de 2022)](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=124142#2341640)  [(Vide Instrução Normativa RFB nº 2083, de 23 de maio de 2022)](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=124142#2341665)  
II - em outubro, com base nos dados do 2º (segundo) semestre do ano-calendário. [(Incluído(a) pelo(a) Instrução Normativa RFB nº 2083, de 23 de maio de 2022)](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=124142#2341641)  [(Vide Instrução Normativa RFB nº 2083, de 23 de maio de 2022)](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=124142#2341665)"

# 2. Cadastro

O cadastro do valor da POEB que será considerado no cálculo deve ser realizado no menu: Obrigações Principais | Eventos Tributários | POEB

Caminho da tela de cadastro

Para incluir a POEB, é necessário preencher os campos referente a data, valor.   
  
Serão considerados para o cálculo os meses cadastrados e com a Flag **POEB em Vigor** marcada

Cadastro POEB

# 3. Regras

* Serão considerados para o cálculo os meses cadastrados e com a Flag **POEB em Vigor** marcada.
* Caso não exista POEB para o primeiro Semestre, será verificado a última POEB vigente, considerando inclusive o ano anterior.
* O segundo semestre será calculado com a média do POEB Primeiro Semestre e Segundo Semestre, considerando somente o mês cujo campo "POEB em Vigor" esta marcado.

Exemplo

Cadastro:

| Ano | Mar | Em Vigor | Abr | Em Vigor | Set | Em Vigor | Out | Em Vigor |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2020 | 0,93 | Sim | 0,95 | Não | 0,85 | Sim | 0,84 | Não |
| 2021 | 0,93 | Não | 0,96 | Sim | 0,94 | Não | 0,85 | Sim |
| 2022 | 0,92 | Não | 0,92 | Sim | 0,98 | Não | 0,95 | Não |
| 2023 | 0,91 | Sim | 0,89 | Não | 0,99 | Sim | 0,88 | Não |

Considerando o cadastro acima, dentro do RM a POEB será calculada da seguinte forma:

| Ano | Jan | Fev | Mar | Abr | Mai | Jun | Jul | Ago | Set | Out | Nov | Dez |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2020 | 0 | 0 | 0,93 | 0,93 | 0,93 | 0,93 | 0,93 | 0,93 | 0,89 | 0,89 | 0,89 | 0,89 |
| 2021 | 0,89 | 0,89 | 0,89 | 0,96 | 0,96 | 0,96 | 0,96 | 0,96 | 0,96 | 0,91 | 0,91 | 0,91 |
| 2022 | 0,91 | 0,91 | 0,91 | 0,92 | 0,92 | 0,92 | 0,92 | 0,92 | 0,92 | 0,92 | 0,92 | 0,92 |
| 2023 | 0,92 | 0,92 | 0,91 | 0,91 | 0,91 | 0,91 | 0,91 | 0,91 | 0,95 | 0,95 | 0,95 | 0,95 |

# 4. Simulação do Evento Tributário

Na simulação do evento tributário, o valor da POEB calculado pelo sistema pode ser verificado na aba "Lucro da Exploração" coluna "Valor POEB" conforme imagem abaixo:

Imagem

# 5. Outras informações

* [Lucro da Exploração (Apuração)](https://tdn.totvs.com/pages/viewpage.action?pageId=422545825)
