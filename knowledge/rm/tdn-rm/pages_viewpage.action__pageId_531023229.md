---
content_hash: 4cca57173cf28e9515823ad43bf038d90bafdbf9ea2a66118bb491bd7817e28d
fetched_at: '2026-06-29T00:10:35.620066+00:00'
page_id: '531023229'
product: rm
source: tdn-rm
title: Condições Financeiras com Convênios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=531023229
version: 3
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Valores de CH / CO**
3. ****Plano****
4. **Sub-plano**
5. **Tipos de CH**
6. **Atenção**
7. **Valores de filmes**
8. **Valor de m2**
9. **Porte de CBHPM**
10. **Valores de UCO**

## **01. VISÃO GERAL**

Esse cadastro é responsável agrupar as informações dos Coeficientes Honorários (CHs) e do filme radiológico de cada Convênio, baseado numa data de vigência por Unidade de Faturamento. È armazenado nela também o histórico dos valores do CH e filme de cada convênio e data de vigência do mesmo.

## **02. VALORES DE CH/CO**

Nesta pasta serão informados os valores de CH / CO.

## **03. PLANO**

O Sistema permite controlar os CH's por Planos dos Convênios. De acordo com o Convênio selecionado, serão exibidos os respectivos planos.

**OBS:**

Caso algum Plano não possua nenhum CH cadastrado, o sistema entenderá que o valor será para TODOS as opções.

## **04. SUB-PLANO**

O Sistema permite controlar os CH's por Sub-Planos dos Convênios.

## **05. TIPOS DE CH**

Campo usado para indicar o valor do CH Principal, que é o CH básico do Convênio. Caso não possua CH Especial cadastrado, o CH básico servirá para todos os itens lançados.  
**Especial:** CH cadastrado para alguma situação especial. Este cadastro pode ser realizado em nível de Item, de Grupo ou de Especialidade.Opções:Especialidade,Grupo,Honorários,Diárias,Serviços,SADT,Taxas e Serviços

## **05. ATENÇÃO**

**O Sistema realiza a cobrança na seguinte ordem de prioridade:**

Verifica se tem CH Especial de Item para Plano e Sub-Plano  
Verifica se tem CH Especial de Grupo para Plano e Sub-Plano  
Verifica se tem CH Especial de Especialidade para Plano e Sub-Plano  
Verifica se tem CH Principal para Plano e Sub-Plano  
Verifica se tem CH Especial de Item para Plano  
Verifica se tem CH Especial de Grupo para Plano  
Verifica se tem CH Especial de Especialidade para Plano  
Verifica se tem CH Principal para Plano  
Se não houver nenhum CH cadastrado para Plano, ENTÃO  
Verifica se tem CH Especial de Item para Tipo Paciente ou Medico para plano TODOS  
Verifica se tem CH Especial de Grupo para Tipo Paciente ou Medico para plano TODOS  
Verifica se tem CH Especial de Especialidade para Tipo Paciente ou Medico para plano TODOS  
Verifica se tem CH Principal para Tipo Paciente ou Medico para plano TODOS  
Senão  
Verifica se tem CH Especial de Item para TODOS  
Verifica se tem CH Especial de Grupo para TODOS  
Verifica se tem CH Especial de Especialidade para TODOS  
Verifica se tem CH Principal para TODOS  
**Como demonstrado acima, o Sistema trabalhará apenas com um tipo de cobrança: ou por Plano / Sub-Plano, ou por Plano, ou por Tipo de Paciente ou por Credenciamento de Médico, não sendo possível combinar mais de um tipo.**

## **06. VALORES DE FILMES**

Nesta pasta serão informados os valores para o filme radiológico.Os tipos do Filme podem ser feitos por Básico, Especialidade, Grupo e Item. Podem ser cadastrados quantos valores de Filme forem necessários, mas não podem ter Condições repetidas. Caso não cadastre outros valores, o valor básico servirá para todos os itens lançados.

**Exemplo:**

Os códigos correspondentes a DIÁRIAS cobradas pelo PRESTADOR encontram-se entre as FAIXAS 80.01.01.10\_80.01.99\_.  
80.01.10\_ + (digito) Diárias (Diária de Apartamento)  
80.01.20\_ + (digito) Diárias (Diária de Berçário)  
80.01.30\_ + (digito) Diárias (Diária de Enfermaria)  
80.01.60\_ + (digito) Diárias (Diária de Quarto)  
80.01.70\_ + (digito) Diárias (Diária de UTI)  
Os códigos correspondentes a TAXAS DE SALA E INSTRUMENTAL cobrados pelo PRESTADOR encontram-se na FAIXA 80.02.\_ \_ \_  
80.02. \_ \_ \_ \_: Taxa de Portes (Porte 0, Porte 1, Porte 2, etc), Taxa de Instrumental (Instrumental 0, Instrumental 1, Instrumental 2, etc).  
Os códigos correspondentes a TAXAS DE SALA FORA DO CENTRO CIRÚRGICO cobrados pelo PRESTADOR encontram-se na FAIXA 80.03.\_ \_ \_ \_  
80.03. \_ \_ \_: Sala de recuperação pós anestesia, Sala de endoscopia, Sala de gesso, Sala de hemodiálise, etc.  
Os códigos correspondentes aos SERVIÇOS cobrados pelo PRESTADOR encontram-se entre as FAIXAS 80.04.\_ \_ \_ \_ a 80.08.\_ \_ \_ \_.  
   
**Estas faixas estão subdivididas em:**  
80.04.\_ \_ \_ \_: Serviços ( Curativo pequeno, Curativo médio, Aspiração, Aplicação de Injeção, etc).  
80.05.\_ \_ \_ \_: Uso de Equipamentos ( Bisturi, Aspirador, Taxas de Equipamentos, etc).  
80.06.\_ \_ \_ \_: Gasoterapia (Ar comprimido, Gás carbônico, Propósito de azoto, Oxigênio, etc).  
80.07.\_ \_ \_ \_: Faixa reservada para MATERIAIS E MEDICAMENTOS.  
80.08.\_ \_ \_ \_: Hotelaria ( Frigobar, Refeição para acompanhante, Refrigerante, etc).

## **07. VALOR DO M2**

Informe o valor do m2 para o filme de acordo com o tipo selecionado.  
Especialidade / Grupo / Item  
Caso o tipo do filme seja por Especialidade, Grupo ou Item, selecione neste campo a especialidade, grupo ou item que possuirá este valor de filme.

## **08. PORTE CBHPM**

Esta pasta será habilitada no lugar da pasta Valores de CH, caso o Convênio trabalhe com o padrão CBHPM.Nesta pasta poderão ser alterados os valores de cada porte.

**OBS:**

As inclusões de exceções são permitidas somente para procedimentos Honorários e SADT. Caso não seja informado valor dos portes, será calculado para efeito de cobrança o valor definido na Tabela de Portes de Procedimento CBHPM.

## **09. VALORES DE UCO**

Nesta pasta você poderá cadastrar os valores de UCO diferentes para faixas de procedimentos.  
Faixa Inicial  
Campo para informar a faixa inicial do procedimento.  
Faixa Final  
Campo para informar a faixa final do procedimento.  
Valor  
Campo para informar o valor de UCO correspondente à faixa do procedimento.  
Cópia de Valores de UCO  
Nesta tela você poderá escolher a partir de qual data serão copiados os valores de UCO.  
Data de Vigência  
Este campo exibe as datas de vigência anteriores à atual
