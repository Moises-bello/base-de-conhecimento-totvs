---
content_hash: f8f81c15678ba044952dd16371198ddc77f7df0ca4aaeffb566ce1212859639a
fetched_at: '2026-06-29T00:11:45.082444+00:00'
page_id: '819061227'
product: rm
source: tdn-rm
title: DT - DIRF 2024
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+DIRF+2024
version: 63
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | DIRF 2024 -Ano Calendário 2023 |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | 1) [DRHROTRM-8426](https://jiraproducao.totvs.com.br/browse/DRHROTRM-8426 "View this issue")  2) [DRHROTRM-8601](https://jiraproducao.totvs.com.br/browse/DRHROTRM-8601 "View this issue")  3) [DRHROTRM-7312](https://jiraproducao.totvs.com.br/browse/DRHROTRM-7312 "View this issue")  4) [DRHROTRM-5919](https://jiraproducao.totvs.com.br/browse/DRHROTRM-5919 "View this issue")  5) [DRHROTRM-8637](https://jiraproducao.totvs.com.br/browse/DRHROTRM-8637 "View this issue") |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2302.257
* 12.1.2306.216
* 12.1.2310.148  ou superiores

## **03. SITUAÇÃO/REQUISITO**

Adequar o produto TOTVS Folha de Pagamento para geração do layout da DIRF 2024 ano calendário 2023, conforme publicação da [Receita Federal do Brasil](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=134962).

## **04. SOLUÇÃO**

Ajustamos o produto TOTVS Folha de Pagamento para atender ao leiaute de 2024, e realizamos algumas melhorias para proporcionar uma experiência ainda melhor aos nossos usuários.

Abaixo, apresentamos detalhes sobre os ajustes e melhorias realizados.

1) Após a atualização da versão, será necessário executar os scripts de adequação das tabelas e campos do sistema por meio do sistema **RM.Atualizador.exe**, conforme demonstrado abaixo.

2) Ajustado os campos:

Ano Referência: Permitindo informar '2024' 

Ano Calendário: Permitindo informar '2023' e Campo 'Identificador de Estrutura do Leiaute': Preencher com o código **B3VH8RQ**.

3) Criado o registro "**RTDS - Rendimentos Tributáveis - Dedução - Desconto Simplificado Mensal**" referente ao item "Registro de Valores Mensais". A tratativa adotada foi:

Conforme orientação da Receita Federal,  o campo "Desconto Simplificado" na DIRF 2024 deve ser preenchido somente se o desconto foi usado para calcular o IRRF daquele pagamento.

Devido a diferença na forma de registro entre nosso sistema (por envelope de pagamento) e a DIRF (por caixa), realizamos uma adaptação. Agora, o sistema verifica somente os envelopes com desconto de IRRF.

O valor do "Desconto Simplificado" será gerado somente se todos os envelopes com desconto de IRRF tiverem o campo "Desconto Simplificado" igual a "1"; caso contrário, não será gerado valor.  
Passamos a analisar somente os envelopes com desconto de IRRF, pois entendemos que quando o valor não atinge o limite para desconto de IR, não deve ser informado.

* + **FOLHA/FÉRIAS:** Verifica se o campo **PFPERFF.IRRF** ou o campo **IRRFFERIAS** são maiores que zero e analisa a regra do campo **PFPERFF.IRRFSIMPLIFICADO**
  + **13º SALÁRIO**: Verifica o campo **PFPERFF.IRRF13** é maior que zero e  analisa a regra do campo **PFPERFF.IRRF13SIMPLIFICADO**

 **OBSERVAÇÕES:**

1. Quando ocorre folha mensal e férias no mesmo caixa, e todos os períodos são simplificados, o valor do "Desconto Simplificado" é consolidado em uma única vez. Isso se deve ao fato de que a base de cálculo do IRRF para férias e folha de pagamento é única.
2. Quando ocorre uma rescisão e há base de IRRF mensal e IRRF sobre o 13º salário, o valor do "Desconto Simplificado" será gerado duas vezes. Isso se deve à distinção das bases de cálculo do IRRF, que são tratadas separadamente nesse contexto específico.

### ATENÇÃO: A adaptação para considerar somente os envelopes de pagamentos que tiveram desconto de IRRF foi a partir dos patches:

* 12.1.2302.264
* 12.1.2306.227
* 12.1.2310.166
* 12.1.2402.106 e superiores.

**Exemplo 1:**

Abaixo temos um envelope demonstrado no mês de 12/2023, onde o valor do IRRF é zero. Note que não apresenta a informação do simplificado.

Veja que no mês de dezembro não foi apresentado o valor no calculo simplificado.

**Exemplo 2:**

Abaixo temos dois envelopes demonstrado no mês de 08/2023, um com o calculo simplificado e outro sem o calculo simplificado.

Veja que no mês de agosto não foi apresentado o valor utilizado no calculo simplificado.

**Exemplo 3:**

Abaixo temos dois envelopes demonstrado no mês de 08/2023, ambos com o calculo simplificado.

Veja que no mês de agosto foi apresentado o valor utilizado no calculo simplificado.

**Exemplo 4:**

Abaixo temos um envelope demonstrado no mês de 08/2023, sem o calculo simplificado.

**ATENÇÃO:** Esse campo passou a ser gerado somente a partir de Abril/2023, conforme publicada [Instrução Normativa nº 2.141](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=130822).

**Adequação da DIRF para Conferência para trazer as informações do desconto simplificado.**

**ATENÇÃO:** Para visualizar o campo do desconto simplificado na DIRF para conferência, é essencial excluir o relatório anterior e importar o novo leiaute disponível no TOTVS Compartilhamento.

4) Realizamos ajustes na geração do código de receita para garantir total compatibilidade com as categorias do eSocial.

**REGRA ANTERIOR**

**Código de receita 0588:** Será aplicado quando:

* + - o campo PFUNC.CODTIPO for igual a 'A' ou
    - o campo PFUNC.CODTIPO for igual a 'D' ou
    - (o campo PFUNC.CODTIPO for igual a 'C' e PFUNC.VINCULORAIS igual a '7' e PFUNC.CODCATEGORIA seja igual '5' ou '11);

**Código de Receita 3533:** Será aplicado quando o parâmetro "**DIRF - Informar remuneração no Cód. da Receita 3533**" existente no funcionário (pfunc.CODIGORECEITA3533) estiver marcado.

**Código de Receita 3562:**Código criado para declaração dos rendimentos referente a PLR (Participação nos Lucros ou Resultados). 

**Código de Receita:1889:**Código criado para declaração dos Rendimentos Recebidos Acumuladamente. 

**Código de Receita 0561:** Será aplicado quando não atender as restrições do código de receita 0588.

**REGRA ATUAL**

**Código de Receita 0588:** Será aplicado quando a categoria do eSocial for igual a: 201, 202, 701, 711, 712, 731, 734, 738, 741, 751, 771 ou 781.

**Código de Receita 3533:** Será aplicado quando o parâmetro "**DIRF - Informar remuneração no Cód. da Receita 3533**" existente no funcionário (pfunc.CODIGORECEITA3533) estiver marcado.

**Código de Receita 3562:**Código criado para declaração dos rendimentos referente a PLR (Participação nos Lucros ou Resultados). 

**Código de Receita:1889:**Código criado para declaração dos Rendimentos Recebidos Acumuladamente. 

**Código de Receita 0561:** Será aplicado quando não estiver de acordo com as categorias do eSocial do código de receita 0588 e também não atender aos critérios dos códigos de receita 3533, 3562 e 1889.

5) Alterada a ordenação dos funcionários para geração da DIRF e Informe de Rendimentos:

| **DE** | **PARA** |
| --- | --- |
| ORDER BY CPF ASC, PFUNC.DTTRANSFERENCIA DESC, PFUNC.DATADEMISSAO ASC, PFUNC.CODSITUACAO ASC | ORDER BY CPF ASC, ISNULL(PFUNC.DATADEMISSAO, '') ASC, ISNULL(PFUNC.DTTRANSFERENCIA, '') DESC, PFUNC.DATAADMISSAO ASC, PFUNC.CODSITUACAO ASC |

6) Adequação da DIRF para Conferência, para tratar a situação em que um funcionário demitido em janeiro, com envelope nos meses de janeiro e dezembro do ano anterior (sem desconto de IRRF, apenas dedução de INSS em janeiro) não seja considerado. Com essa adequação, o sistema garante compatibilidade entre a DIRF em Arquivo e a DIRF para Conferência.

7) Ajuste na DIRF para considerar os parâmetros "Desconsiderar o período da ficha financeira quando a data de pagamento for igual à data de demissão", criado na tela de rescisão por transferência, e o parâmetro "Desconsiderar Mês Transferência DIRF/IR", criado no período da ficha financeira.

    **Exemplo:**

Funcionário transferido pelo tipo "5" com data de pagamento igual à data de demissão, e com movimentação na ficha financeira apenas nos meses de novembro e dezembro ao longo do ano de 2023.

 Na tela de transferência selecionamos mesma coligada e marcamos o parâmetro "**Desconsiderar o período da ficha** **financeira quando a data de pagamento for igual a data de demissão**":

Gerando a DIRF em arquivo com o parâmetro marcado no período da ficha financeira de competência (11/2023).

O arquivo da DIRF deverá ser gerado somente com valores de dezembro desconsiderando o mês da transferência que foi novembro.

 Parâmetro desmarcado no período da ficha financeira competência (11/2023):

 

O arquivo retornou com valores de novembro e dezembro.

 

**OBSERVAÇÃO:**

Nos links abaixo contém informações detalhadas sobre os parâmetros acima.

[Transferência -](https://tdn.totvs.com/pages/viewpage.action?pageId=806761064)

## **05. DEMAIS INFORMAÇÕES**

[DIRF/Informe de Rendimentos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719351)
