---
content_hash: 107ea24d52bd62b1dc6b205b9267a1d220e2485e568efd1fcb62d9f82d9cb37a
fetched_at: '2026-06-29T00:09:23.679731+00:00'
page_id: '422546105'
product: rm
source: tdn-rm
title: Registro Y540 - Discriminação da Receita de Vendas dos Estabelecimentos por
  Atividade Econômica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546105
version: 2
---

A geração deste registro irá ocorrer de forma automática conforme algumas parametrizações da ECF. Será gerado um registro Y540 para cada filial, desde que não seja SCP.

**Regras de Processamento do Campo "VL\_REC\_ESTAB"**   
 Dependendo da regra, os valores a serem apresentados neste campo serão processados pelo módulo TOTVS Gestão Contábil e  outros pelo TOTVS Gestão Fiscal.  
 Legenda:   
 COD\_QUALIF  = Qualificação da Pessoa Jurídica:  
 01 – PJ em Geral  
 02 – PJ Componente do Sistema Financeiro   
 03 – Sociedades Seguradoras, de Capitalização ou Entidade Aberta de Previdência Complementar 

FORMA\_TRIB   = Forma de Tributação: 

FORMA\_APUR = Indicador do Período de Apuração do IRPJ e da CSLL:

IND\_RED\_ISEN = Isenção e Redução do Imposto para Lucro Presumido:   
 S – Sim |  N – Não

Para processar o valor a ser apresentado iremos utilizar a própria regra definida no manual da ECF, que será baseado nas contas do plano de contas referencial (plano de contas paralelo), ou seja, **o sistema irá identificar o valor referente movimentação (conforme a Filial) da conta contábil associada a conta paralela** **que faz parte da regra**, depois ira aplicar a regra conforme detalhamento abaixo.   
 **Observação:**   
  - As contas que irão fazer parte da regra abaixo sempre serão contas paralelas, para efeito de validação deverão ser analisadas as movimentações das contas contábeis associada à conta paralela destacada na regra.

Serão processadas as movimentações correspondentes ao período da regra (Trimestre ou Ano)

|  |  |  |
| --- | --- | --- |
| **#** | **CONDIÇÕES PARA A GERAÇÃO DO REGISTRO** | **As expressões abaixo consideram a movimentação das contas contábeis associadas a conta paralela destacada** |
| 1 | COD\_QUALIF\_PJ = "01" E FORMA.TRIB       =  Lucro Real E FORMA\_APUR    =  Trimestral | 3.01.01.01.01 – 3.01.01.01.02.01 – 3.01.01.01.02.02 +   3.11.01.01.01 – 3.11.01.01.02.01 –     3.11.01.01.02.02 |
| 2 | COD\_QUALIF\_PJ = "01" E FORMA.TRIB       =  Lucro Real E   FORMA\_APUR    =  Anual | 3.01.01.01.01 – 3.01.01.01.02.01 – 3.01.01.01.02.02 + 3.11.01.01.01 – 3.11.01.01.02.01 –   3.11.01.01.02.02 |
| 3 | FORMA.TRIB = Lucro Presumido E 0020.IND\_RED\_ISEN = S | Para esta combinação será apresentada a seguinte mensagem no Log da ECF:   Não foi possível gerar o registro Y540 porque toda a receita da empresa foi armazenada agrupada na Matriz no momento do encerramento do período e as informações devem ser prestadas por Estabelecimento. Esse registro deve ser informado diretamente no PVA. |
| 4 | FORMA.TRIB = Lucro Presumido E   IND\_RED\_ISEN = "N" | 3.01.01.01.01 – 3.01.01.01.02.01 – 3.01.01.01.02.02 +  3.11.01.01.01  – 3.11.01.01.02.01 – 3.11.01.01.02.02 |
| 5 | FORMA.TRIB = Lucro Arbitrado | Para esta combinação será apresentada a seguinte mensagem no Log da ECF:   Não foi possível gerar o registro Y540 porque toda a receita da empresa foi armazenada agrupada na Matriz no momento do encerramento do período e as informações devem ser prestadas por Estabelecimento. Esse registro deve ser informado diretamente no PVA. |
| 6 | COD\_QUALIF\_PJ = "02" E   FORMA.TRIB       =  Lucro Real E   FORMA\_APUR    =  Trimestral | 3.1.7.1.0.00.00 |
| 7 | COD\_QUALIF\_PJ = "02" E   FORMA.TRIB       =  Lucro Real E   FORMA\_APUR    =  Anual | 3.1.7.1.0.00.00 |
| 8 | COD\_QUALIF\_PJ = "03" E   FORMA.TRIB       =  Lucro Real E   FORMA\_APUR    =  Trimestral | 3.01.01.01.01.01 + 3.01.01.01.01.02 |
| 9 | COD\_QUALIF\_PJ = "03" E   FORMA.TRIB       =  Lucro Real E   FORMA\_APUR    =  Anual | 3.01.01.01.01.01 + 3.01.01.01.01.02 |

***Observação*:**Serão gravadas mensagens no log de geração da rotina nos seguintes casos:

* Alguma das contas paralelas consideradas no cálculo não possua conta contábil associada.
* Se o valor final do cálculo  for negativo. Neste caso o registro não será gerado.
* A memória de cálculo do registro.
