---
content_hash: a0f264d36ab4ac9eddafe826171e61cb86986e2b13fef26a45e9d4579853ed98
fetched_at: '2026-06-29T00:09:28.602251+00:00'
page_id: '423938721'
product: rm
source: tdn-rm
title: Eliminação de Valores 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938721
version: 8
---

A eliminação de valores visa regular o saldo da demonstração consolidada, realizando uma espécie de "estorno" daqueles saldos que são provenientes de operações entre entidades do mesmo grupo econômico.  
   
De acordo com a lei 6.404/76 e a NBC T8 DAS DEMONSTRAÇÕES CONSOLIDADAS, das demonstrações financeiras consolidadas serão excluídas:

* os valores dos investimentos da controladora em cada controlada e o correspondente valor no patrimônio líquido da controlada;
* os saldos de quaisquer contas decorrentes de transações entre as entidades incluídas na consolidação;
* as parcelas dos resultados do exercício, do patrimônio líquido e do custo de ativos de qualquer natureza que corresponderem a resultados ainda não realizados de negócios entre as entidades, exceto quando representarem perdas permanentes.

**Realizando a Eliminação no TOTVS Gestão Contábil**  
Exemplo:

* Uma controladora participa e consolida uma controlada em 100%;
* O capital próprio da controlada é de R$ 100.000,00, logo a controladora tem um investimento referente a essa controlada no valor de R$ 100.000,00.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | CONTROLADORA | CONTROLADA | ELIMINAÇÕES | | SALDO CONSOLIDADO | |
| **ATIVO** | | | DEBITO | CRÉDITO |
| **CIRCULANTE** | **R$ 250,00** | **R$ 100.500,00** |  |  | **R$ 100.750,00** | |
| Caixa | R$ 250,00 | R$ 50.000,00 |  |  | R$ 50.250,00 | |
| Bancos |  | R$ 50.500,00 |  |  | R$ 50.500,00 | |
| **NÃO CIRCULANTE** | **R$ 100.000,00** |  |  | **R$ 100.000,00** | **R$ -** | |
| Investimento | R$ 100.000,00 |  |  | R$ 100.000,00 | R$ - | |
| **TOTAL DO ATIVO** | **R$ 100.250,00** | **R$ 100.500,00** |  | **R$ 100.000,00** | **R$ 100.750,00** | |
| **PASSIVO** | | |  |  | R$ - | |
| **CIRCULANTE** | **R$ 150,00** | **R$ 500,00** |  |  | **R$ 650,00** | |
| Fornecedores | R$ 150,00 | R$ 500,00 |  |  | R$ 650,00 | |
| **NÃO CIRCULANTE** | **R$ -** | **R$ -** |  |  | **R$ -** | |
|  | R$ - | R$ - |  |  | R$ - | |
| **P.L.** | **R$ 100.100,00** | **R$ 100.000,00** | **R$ 100.000,00** |  | **R$ 100.100,00** | |
| Capital Social | R$ 100.100,00 | R$ 100.000,00 | R$ 100.000,00 |  | R$ 100.100,00 | |
| **TOTAL DO PASSIVO** | **R$ 100.250,00** | **R$ 100.500,00** | **R$ 100.000,00** |  | **R$ 100.750,00** | |

Para realizarmos a eliminação deste valor no sistema precisamos acessar a conta consolidada que representa as contas de investimento das empresas participantes e na aba "Eliminação de Valores" cadastrar uma nova eliminação.

 No cadastro de eliminação, haverá os seguintes campo

* Coligada detentora: Será a empresa que teve o saldo de investimento eliminado, no exemplo acima a CONTROLADORA;
* Coligada Contrapartida: Será a empresa que teve o saldo de P.L. eliminado, no exemplo acima a CONTROLADA.
* Conta contrapartida: Será a conta consolidada que sofreu a eliminação junto com a conta de investimento, referente ao nosso exemplo seria a conta consolidada referente ao P.L.;
* Data: Data final do período de escrituração. Esta data deve ser menor que a data de corte do novo modelo de eliminação.

  Data de Corte

  Esta data se encontra nos parâmetros do contábil e possui como padrão a data 01/01/2022. Após o preenchimento desta data só poderão ser criadas eliminações através da inclusão de partidas que possuam contrapartida de eliminação.
* Valor: No exemplo acima seria 100.000,00

Natureza: Para atender o validador da receita federal, ainda em relação ao exemplo acima a natureza deve ser DEVEDORA, pois a parcela que está sendo eliminada é de um valor de origem devedora, caso o usuário informe a natureza CREDORA tendo como base o exemplo acima, o saldo de 100.000,00 referente a eliminação será somado e não subtraído.

OBSERVAÇÃO  
 Quando o processo é executado para processar os saldo das contas, o sistema identifica se existe eliminação e, se houver ele utiliza a conta contrapartida e a coligada contrapartida informadas na eliminação para gerar os registros K310 e K315 referente ao K300 da conta contrapartida de forma automática, não exigindo do usuário o cadastro de uma nova eliminação.   
   
Exemplo: A eliminação acima gera os registros da seguinte forma após geração do arquivo:

|K300|CÓDIGO DA CONTA CONSOLIDADA QUE REPRESENTA INVESTIMENTO|100000,00|D|100000,00|D|0,00|D|  
|K310|CÓDIGO DA CONTROLADORA|100000,00|D|  
|K315|CÓDIGO DA CONTROLADA|CÓDIGO DA CONTA CONSOLIDADA QUE REPRESENTA O P.L.|100000,00|C|

Ao identificar a eliminação o sistema gera de forma automática os mesmos registros para a conta que foi cadastrada como contrapartida, porém com as naturezas e as empresas invertidas nos campos, ou seja, o que era devedor passa a ser credor e o que era coligada detentora passa a ser contrapartida, sendo:

|K300|CÓDIGO DA CONTA CONSOLIDADA QUE REPRESENTA O P.L.|200100,00|C|100000,00|C|100100,00|C|  
|K310|CÓDIGO DA CONTROLADA|100000,00|C|  
|K315|CÓDIGO DA CONTROLADORA|CÓDIGO DA CONTA CONSOLIDADA QUE REPRESENTA INVESTIMENTO|100000,00|D|

Veja Também

* Cadastro de Controladas
* K100 - Código do País
* Plano de Contas Consolidado
* [Cálculo Saldo Consolidado](http://tdn.totvs.com.br/pages/viewpage.action?pageId=423938856)
* [Eventos societários](http://tdn.totvs.com/x/U6sEGw)
