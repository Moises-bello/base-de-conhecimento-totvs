---
content_hash: a7266930e8f89b06e22e2e567c8cb90786ed644af5b26baf8803375520cab4b6
fetched_at: '2026-06-29T00:09:26.055652+00:00'
page_id: '423938236'
product: rm
source: tdn-rm
title: Lançamento Financeiro - Cálculo do IRRF e INSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938236
version: 4
---

O Percentual de Dedução do IRRF é calculado com base no valor a ratear do financeiro.   
Foram feitas algumas alterações no serviço de inclusão do lançamento financeiro, relacionadas ao cálculo do IRRF e INSS. As alterações são as seguintes:

1. Alterações no cálculo de impostos no TOTVS Gestão Financeiras: Para melhorar a integração entre os sistemas, foi alterada a forma de cálculo dos impostos realizada pelo TOTVS Gestão Financeiras. Os sistemas que utilizavam o serviço de inclusão de lançamentos, enviavam um percentual de dedução a ser aplicado sobre o valor original do lançamento. Esse percentual nem sempre traduzia a realidade, pois, algumas vezes, ele precisava ser manipulado para que o valor base do imposto ficasse correto. Isso porque apenas os serviços deverão ser tributados pelos impostos calculados no TOTVS Gestão Financeiras e o lançamento pode possuir um valor composto por serviços + produtos. Para isso, foi criado o campo "Valor do Serviço", que será utilizado como base para o cálculo dos impostos em substituição ao "Valor Original". Os campos relativos a percentuais serão mantidos. Além disso, o "Valor Base", após ser calculado pelo TOTVS Gestão Financeiras, passará a ser gravado na base de dados. Os valores passarão a ser calculados da seguinte maneira:

INSS do Empregado (PF): Cálculo da Base  Valor do Serviço   Percentual de Dedução do INSS do Empregado  
INSS do Empregador (PF): Cálculo da Base Valor do Serviço   Percentual de Dedução do INSS do Empregador  
IRRF (PF): Cálculo da Base (Valor do Serviço   Percentual de Dedução do IRRF)  Valor de Dedução  INSS do Empregado  
IRRF (PJ): Cálculo da Base (Valor do Serviço   Percentual de Dedução do IRRF)   
Campos criados na FLAN:

* Valor do serviço (VALORSERVICO)
* Valor base INSS (VRBASEINSS)
* Valor base IRRF (VRBASEIRRF)

Para que o imposto seja calculado corretamente, os sistemas que utilizam o serviço de inclusão de lançamentos deverão enviar para o TOTVS Gestão Financeiras, no lançamento financeiro, o "Valor do Serviço" e o "Percentual de Dedução", esse segundo para cada um dos impostos. Ou seja, deverão ser informados os seguintes valores na inclusão:

* Valor Serviço
* Percentual dedução IRRF
* Percentual dedução INSS empregador
* Percentual dedução INSS empregado

***Observação***: Para que o cálculo do IRRF e INSS continuem funcionando como era anteriormente, se o valor do serviço não for informado nos parâmetros de inclusão, o mesmo assumirá o valor original. Se for passado o valor zero no valor do serviço, o IRRF e o INSS não serão calculados.

            2. Alteração no cálculo do INSS, considerando o INSS recolhido em outras empresas. No modelo anterior, o usuário informava qual era o valor do INSS recolhido pela outra empresa e descontava esse valor do que ele deveria recolher.   
Após análise junto à consultoria trabalhista/previdenciária, concluiu-se que é necessário guardar a informação do Salário Base de Contribuição para o INSS e não o valor retido de INSS. O cálculo passa a ser feito da seguinte forma: Se o valor base para o INSS somado ao valor base utilizado em outra empresa não atingir o teto, calcula-se o INSS normalmente sobre o valor base.   
Caso contrário, calcula-se o INSS sobre a diferença entre o teto e o valor base em outra empresa. Essa alteração foi necessária, pois, no caso de entidades filantrópicas, a alíquota aplicada em outras empresas pode ser diferente da alíquota da empresa (caso o empregado tenha prestado serviço em empresas não filantrópicas).   
Nesse caso, o INSS calculado pelo modelo anterior não respeitaria a legislação.  
Alterações na inclusão: Internamente o campo INSSEmOutraEmpresa foi substituído pelo VrBaseINSSOutraEmpresa.   
O valor informado deverá ser a base de cálculo utilizada para calcular o INSS em outra empresa e é informado no lançamento financeiro.  
***Observação***: Nesse caso, o valor default é zero. Essa alteração afetará apenas os sistemas que já enviavam o valor de INSS recolhido em outra empresa.
