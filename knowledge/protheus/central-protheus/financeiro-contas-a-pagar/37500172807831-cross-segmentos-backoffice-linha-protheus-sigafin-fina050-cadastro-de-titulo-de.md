---
article_id: 37500172807831
category: Financeiro - Contas a Pagar
content_hash: 23c1611070eb82a7652ab0595eeef9e1675c6ec1aaa676097bfeae1569c25632
fetched_at: '2026-06-28T22:38:07.088744+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA050 - Cadastro
  de titulo de Fornecedor Pessoa Física - Carreteiro
type: support-article
updated_at: '2026-03-25T17:51:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37500172807831-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Cadastro-de-titulo-de-Fornecedor-Pessoa-F%C3%ADsica-Carreteiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37500209261975) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Quais os cadastros de título de fornecedores pessoa física - carreteiro?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Para o cálculo do IRPF para Carreteiro, o sistema segue a regra conforme o cadastro de código de **naturezas** e **Fornecedores** e **tabela progressiva** de Imposto de Renda Pessoa Física, cadastrada por meio do configurador.

Vamos considerar o seguinte cadastro na **natureza**:

Calcula INSS (ED\_CALCINS) = Sim  
Base INSS (ED\_BASEINS)= 20%  
Porc. INSS (ED\_PERCINS) = 2,2%  
Calcula IR (ED\_CALCIRF)= Sim  
IRRF Carreteiro (ED\_IRRFCAR)= Sim  
Base IR Carreteiro (ED\_BASEIRC) = 40%

Cadastrar **fornecedor** configurando os campos abaixo:

Tipo (A2\_TIPO) = Físico  
Calc INSS (A2\_RECINSS)= Sim  
Calc IRRF (A2\_CALCIRF) = Normal

**Parâmetros**  
MV\_INSIRF = 1  - Abate o valor do INSS da base de cálculo do IRRF  
MV\_VLRETIR = 10.00

Considerando a tabela progressiva do exemplo abaixo:

![](https://tdn.totvs.com/download/attachments/235590049/image2018-6-27_11-48-31.png?version=1&modificationDate=1530110911000&api=v2)

**Cenário 1: Valor do IR atinge o mínimo para retenção**  
  
Fazer a inclusão de um título no valor de R$ 10.000,00 para os cadastros acima no contas a pagar.  
Forma do cálculo para retenção do imposto IRPF.

1 - Valor do titulo R$ 10.000,00  
2 - Base de cálculo do INSS: R$ 10.000,00 x 20% (ED\_BASEINS) = R$ 2.000,00  
3 - Valor do INSS: R$ 2.000,00 x 2,2% = R$ 44,00  
4 - Base de cálculo do IRRF: R$ 10.000,00 x 40% (ED\_BASEIRC) = R$ 4.000,00  
Como o parâmetro MV\_INSIRF = 1, descontar da base do IRRF o valor do INSS: R$ 4.000,00 - R$ 44,00 (INSS) = R$ 3.956,00  
5 - Valor do IRRF: R$ 3.956,00 (base do IRRF) \* 22,50% (alíquota conforme faixa da tabela progressiva)= R$ 890,10  
6 - Deduzir o valor de dedução conforme faixa da tabela progressiva: R$ 890,10 - R$ 636,13 (valor de dedução do IRRF) = R$ 253,97  
7 - Valor do imposto R$ 253,97

Como este valor de R$ 253,97 é maior que o valor mínimo para retenção configurado no parâmetro **MV\_VLRETIR**, irá ocorrer a retenção.

Se o valor do IR fosse menor que o configurado no parâmetro **MV\_VLRETIR**, não irá ocorrer a retenção de IR, sendo acumulado este valor de IR no cálculo do IR do próximo título dentro do mesmo mês. Veja o exemplo do cenário 2.

**Cenário 2: Valor do IR não atinge o mínimo para retenção.**  
  
Fazer a inclusão de um título no valor de R$ 1.000 para os cadastros acima no contas a pagar.  
Forma do cálculo para retenção do imposto IRPF.

1 - Valor do titulo R$ 1.000,00  
2 - Base de cálculo do INSS: R$ 1.000,00 x 20% (ED\_BASEINS) = R$ 200,00  
3 - Valor do INSS: R$ 200,00 x 2,2% = R$ 4,40  
4 - Base de cálculo do IRRF: R$ 1.000,00 x 40% (ED\_BASEIRC) = R$ 400,00   
Como o parâmetro MV\_INSIRF = 1, descontar da base do IRRF o valor do INSS: R$ 400,00 - R$ 4,40 (INSS) = R$ 395,60.  
5 - Valor do IRRF: R$ 395,60 (base do IRRF) \* 0,0% (alíquota conforme faixa da tabela progressiva)= R$ 0,00  
6 - Veja que a base do IR, dentro da tabela progressiva, não possui alíquota, portanto, não deve reter o IR.

Incluir um segundo título dentro do mesmo mês para os cadastros acima no contas a pagar.  
1 - Valor do titulo R$ 5.000,00  
2 - Base de cálculo do INSS: R$ 5.000,00 x 20% (ED\_BASEINS) = R$ 1.000,00  
3 - Valor do INSS: R$ 1.000,00 x 2,2% = R$ 22,00  
4 - Base de cálculo do IRRF: R$ 5.000,00 x 40% (ED\_BASEIRC) = R$ 2.000,00  
Como o parâmetro MV\_INSIRF = 1, descontar da base do IRRF o valor do INSS: R$ 2.000,00 - R$ 22,00 (INSS) = R$ 1.978,00.  
5 - Como o valor do IR anterior não foi retido por não atingir o mínimo, será considerado na cumulatividade do cálculo do IR no mesmo mês, então temos: valor base do IR do título anterior somado ao valor base do IR do título atual.   
R$ 395,60 (base do IR do título anterior) + R$ 1.978,00 (base do IRRF do título atual) = R$ 2.373,60  
6 - Aplicar a alíquota conforme a faixa da tabela progressiva: R$ 2.373,60 x 7,5% (alíquota conforme faixa da tabela progressiva) = R$ 178,02.  
7 - Deduzir o valor de dedução conforme a faixa da tabela progressiva: R$ 178,02 - 142,80 (dedução conforme faixa da tabela progressiva) = R$ 35,22  
8 - Valor do IR: R$ 35,22

**Observação:** o campo E2\_BASEIRF será gravado com o valor bruto sem o desconto do INSS, pois todo o sistema irá considerar o desconto do INSS no momento do cálculo, por exemplo, na inclusão do título ou na baixa do título, o valor do INSS será descontado do valor do campo E2\_BASEIRF ao calcular o IR. Além disso, o valor do campo E2\_BASEIRF é considerado para o envio na DIRF, sendo o rendimento total, sem o desconto de INSS.

**Saiba mais:** [FIN0026\_CPAG\_Calculo\_de\_IRRF\_ Carreteiro](https://tdn.totvs.com/display/public/PROT/FIN0026_CPAG_Calculo_de_IRRF_+Carreteiro)
