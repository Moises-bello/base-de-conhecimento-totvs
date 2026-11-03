---
content_hash: 0a7ea37bdb98685446d887a916f18dbdc75f4129976ac19f9b6949f3a6f431a9
fetched_at: '2026-06-29T00:09:21.022263+00:00'
page_id: '422545767'
product: rm
source: tdn-rm
title: O Processo do Simples Nacional
type: documentation
url: https://tdn.totvs.com/display/LRM/O+Processo+do+Simples+Nacional
version: 41
---

## **Conteúdo**

32Conteúdo

## **01. Parametrização da Filial**

### **01.01. Filial Matriz do Estabelecimento**

Acesse os parâmetros do TOTVS Gestão Fiscal através do menu Ambiente | Parâmetros | TOTVS Gestão Fiscal |  03.02 - Apuração de Tributos | 03.02 - Apuração de Tributos | Etapa 22 - Filial Matriz do Estabelecimento e selecione a filial matriz da empresa.

### **01.02. Regime da Empresa**

No cadastro da filial , acesse o Anexos | Dados Fiscais na guia Tipo de Estabelecimento e marque a opção "Optante Regime Simplificado". Antes de salvar o cadastro verifique se o campo Regime da Empresa está preenchido corretamente.

### **01.03. Enquadramento**

Ainda no cadastro da Filial acesse Anexos | Enquadramento Simples Nacional e inclua uma data para o enquadramento.

Só preencha a Data de Desenquadramento e Motivo de Desenquadramento caso a operação se refira a esta situação.

Uma vez informada a data pra este anexo e salvo a mesma não poderá ser alterada ou excluída.

### **01.04. Valor Bruto de Folhas de Salários**

Caso a filial seja prestadora de serviços e se enquadre no anexo V do Simples Nacional o anexo Valor Bruto de Folhas de Salários deverá ser alimentado.

## **02. Cadastro de Tributos**

O cadastro deve seguir a seguinte configuração:

* Sigla: SN
* Descrição: Simples Nacional
* Tipo da Alíquota: Variável
* Abrangência do Tributo: Federal
* Periodicidade: Mensal
* Incidência: Ambos
* Procurar Alíquota no: Alíquotas Simples

## **03. Configuração do Processo**

### **03.01. Tabelas de Alíquotas do Simples Nacional**

Acesse o menu Obrigações Principais | Simples Nacional Acesse, nas opções dentro do Simples Nacional selecione "Alíquota Simples Nacional".

Observação:

No primeiro acesso do TOTVS Gestão Fiscal, todos os anexos do Simples Nacional serão criadas automaticamente.

No caso de alguma alteração das alíquotas pelos Órgãos competentes, o usuário deverá alterar manualmente. Deve-se atentar para a particularidade da [tabela do Anexo III](http://normas.receita.fazenda.gov.br/sijut2consulta/anexoOutros.action?idArquivoBinario=48432), pois foi criado nela um campo para a alíquota do ISS.

Esta alíquota é a constante na mesma faixa de enquadramento do Anexo V, exemplo:

* Se a filial se enquadra no Anexo III na faixa de 1.080.000,01 a 1.200.000,00 ele deverá transferir do Anexo V, na mesma faixa de enquadramento a alíquota de 4,65% para o Anexo III.
Para que seja executado o encerramento de todas as Alíquotas do Simples de uma só vez, basta acessar o processo Encerrar Vigência Alíquota Nacional.

### **03.02. Combinações de Situações Tributárias**

Acesse o menu Obrigações Principais | Simples Nacional Acesse, nas opções dentro do Simples Nacional selecione "Combinações de Situações Tributárias".

Deverão ser criadas tantas combinações forem as situações tributárias da filial.

Deverão ser considerados os produtos e os tributos incidentes sobre eles e se os mesmos sofrem retenções.

Os produtos a serem considerados no cálculo, devem ser selecionados nos Anexos do cadastro de Combinações de Situação Tributárias.  
Um mesmo produto não pode ser incluído em duas combinações.

Os tributos selecionados no cadastro de Combinações de Situação Tributária NÃO serão considerados no cálculo da alíquota final, exemplo:

* Usa Substituição Tributária

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ICMS | IPI | PIS | COFINS | ISS |
| ❌ | ❌ | ❌ | ❌ |  |

* No cadastro da Alíquotas Simples definida as seguintes alíquotas

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IRPJ | CSLL | COFINS | PIS/PASEP | CPP | ICMS | IPI | ISS |
| 0,35% | 0,35% | 1,05% | 0,25% | 3,02% | 32% | 7,50% | 0,00% |

Neste exemplo hipotético, o percentual da alíquota que será considerado para o cálculo do valor do imposto será equivalente a 3,72%¹.

**¹Onde**: Soma da alíquota das tributos IRPJ, CSLL e CPP.

Para cenários criados a partir do mês de **Outubro de 2022** os tributos que estiverem selecionados na seção Substituição Tributária no cadastro de combinações de Substituições Tributárias terão suas aliquotas desconsideradas no Cálculo do Percentual de Repartição.

Imagem

### **03.03. Cenários de Apuração**

O cadastro de Cenário de Apuração deve ser acessado pelo menu Cadastros | Tabelas Auxiliares | Obrigações Federais | Cenário de Apuração do Simples Nacional.  
No cadastro do cenário selecione a Combinação de Situações Tributárias e o Anexo nas quais o contribuinte se enquadra.  
As receitas dos últimos 12(doze) meses anterior a apuração, deve ser no anexo Últimas Receitas. Este anexo só deve ser executado na implantação do processo.   
A partir do primeiro mês de apuração o valor das receitas é acumulado automaticamente quando o período de apuração é encerrado.   
No anexo Naturezas do Cenário devem ser listadas os CFOP´s que compõem a receita para aquele cenário. Desta forma, ao encerrar o período de apuração, serão selecionados todos os lançamentos que foram feitos para aquele CFOP para compor a receita do cenário.   
Os lançamentos que possuam os CFOP´s de devolução listados neste anexo serão excluídos da composição da receita bruta. Uma mesma natureza não poderá ser incluída em dois cenários diferentes.   
O campo "Grupo de Receitas" possibilita a separação da receita bruta geradas no mercado interno e a receita bruta de exportação. Para que essa apuração seja separada é necessária a criação de dois cenários um selecionado a opção "Padrão" e o segundo cenário selecionando a opção "Exportação".

Em caso de implantação do processo, as 12 (doze) últimas receitas deverão ser incluídas manualmente no anexo "Ultimas Receitas" do cadastro do Cenário de Apuração do Simples Nacional.

No caso de existir mais de um cenário de apuração, estas receitas deverão ser proporcionalizadas por cenários de apuração previamente cadastrado ou incluídas integralmente apenas um cenário.

## **04. Apuração do Tributo**

### **04.01. Período de Apuração - Encerramento**

Deverão ser incluídos períodos de acordo com a periodicidade do tributo por considerar receitas acumuladas.   
Um período só poderá ser encerrado se os anteriores já tiverem sido encerrados antes.   
Um período só poderá ser aberto se os posteriores tiverem sido abertos antes.   
Um período só poderá ser encerrado de houver um Cenário de Apuração do Simples incluído com uma vigência igual ou maior. Após o encerramento do período de apuração serão demonstrados na guia Apuração Simples Nacional as informações da apuração por Filial e pelo tipo Grupo de Receitas definido no cadastro do cenário.

Para a correta apuração do tributo dentro da vigência de 2018, os demais anexos cadastrados anterior a este período deverão ser encerrados.

O sistema não disponibilizará a emissão da guia de recolhimento porque o contribuinte a emitirá pelo PGDAS diretamente no site da Receita federal.   
O sistema não disponibilizará nenhuma saída demonstrando as informações do Simples Nacional pelo fato do PGDAS não possuir um importador de dados. Para conseguir estas informações o usuário poderá desenvolver um relatório.  
Nessa primeira versão da Apuração do Simples Federal não será disponibilizada a contabilização, a mesma estará disponível em uma versão posterior, ainda a ser definida.

### **04.02. Exemplo de cálculo**

Na guia Apuração Simples Nacional do período de apuração do tributo, o cálculo será executado de acordo com o seguinte exemplo:

1 - Para o cálculo serão consideradas as receitas do período que está sendo apurado. No nosso exemplo não existe receita em Janeiro/2017. Em Fevereiro/2017 o valor da receita foi de R$50.000,00. O cálculo seguirá da seguinte maneira:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mês Referente a Receita** | **Valor da Receita¹** | **Alíquota²** | **Valor do Imposto³** | **Receita Último 12 meses****⁴** |
| Janeiro | 0,00 | 2,75 | 0,00 | 0,00 |
| Fevereiro | 50.000,00 | 3,72 | 1.860,00 | 600.000,00 |

¹**Onde**: Receita bruno do mês (venda).

**²Onde:** Alíquota nominal constante dos Anexos I a V da lei definida no cadastro de Alíquota do Simples.

**³Onde:** Valor da Receita \* Alíquota (50.000,00 \* 3,72)

**⁴Onde**: Valor da Receita \* 12 (correspondente a quantidade de meses) = 50.000,00 \* 12  
   
2 - No mês de Março/2017 foi gerada uma receita de R$20.000,00. O sistema seguirá com o cálculo considerando os demais meses já apurados da seguinte maneira:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mês Referente a Receita** | **Valor da Receita¹** | **Alíquota²** | **Valor do Imposto³** | **Receita Último 12 meses****⁴** |
| Março | 20.000,00 | 3,33 | 666,00 | 300.000,00 |

**¹Onde**: Receita bruno do mês (venda)

**²Onde**: Alíquota nominal constante dos Anexos I a V da lei definida no cadastro de Alíquota do Simples

**³Onde**: Valor da Receita \* Alíquota (50.000,00 \* 3,33)

**⁴Onde**: Valor da Receita do mês de fevereiro / 2 (relativo a quantidade de meses já apurados) \* 12 (meses) = 50.000,00 / 2 \* 12 (meses).

## **05. Simples Nacional - 2018**

### 05.01. Principais Mudanças

As principais mudanças do Simples Nacional 2018 são:

* Aumento do dos limites em relação ao faturamento;
* O Anexo VI deixará de existir;
* Os Anexos III e V vão passar por fortes alterações;
* A alíquota progressiva passa a ser calcula conforme o faturamento;
* No anexo V não é mais feito o cálculo sobre a folha de pagamento.

De acordo com a [Lei Complementar nº 155](http://www.planalto.gov.br/ccivil_03/Leis/LCP/Lcp155.htm), o cálculo de 2018 passa a ser da seguinte maneira:  
 \*RBT12¹  Aliq²  PD³  RBT12¹\*

**¹Onde**: Receita Bruta acumulada nos 12 (doze) meses anteriores ao período de apuração.  
**²Onde**: Alíquota nominal constante dos Anexos I a V da lei.  
**³Onde**: Parcela a deduzir constante dos Anexos I a V da lei.

### **05.02. Configuração do Processo**

**Tabelas de Alíquotas do Simples Nacional - 2018**

Primeiramente é necessário informar a Data de Final da vigência dos Anexos utilizados até o ano de 2017.  
Em relação ao campo Alíquota para vigência até 31/12/2017 o cálculo permanece igual ao já existente conforme demonstrado acima.  
Já a partir de janeiro/2018 o campo não será mais calculado, o mesmo deverá ser preenchido manualmente pelo usuário. A Alíquota informado será utilizada no cálculo da Alíquota Efetiva.

Observação:

Para a data de vigência a partir de 2018 será habilitado o campo "Valor a Deduzir" conforme alterações aplicadas na apuração do Simples Nacional.

### **05.03. Calculo da Alíquota na inclusão do Movimento**

Na coluna Procurar Alíquota Em, do Tipo de Movimento - Etapa Fis-Tributação Item, será selecionado a opção Simples Nacional, dessa forma o sistema realizará o seguinte calculo:  
-  Alíquota efetiva do Período de Apuração SN anterior  \* (Percentual de Partilha do tributo \ 100)  
  
Ex: Alíquota efetiva do Período de apuração SN anterior = 9,3387  
Percentual de Partilha do tributo = 10,00  
Calculo: 9,3387 \* (10,00/100) = Alíquota resultante 0,93.

Na linha do tributo no Item do Movimento será apresentado a alíquota de 0,93 para calculo do valor do tributo.

OBS: Para o correto calculo da alíquota do tributo, o período de apuração do Simples Nacional anterior deve estar encerrado.  
O campo "Procurar alíquota em" do cadastro do Tributo deve estar selecionado como "Tipo de Movimento"

**05.04. Apuração do Tributo**

**Período de Apuração - Encerramento**

Com as novas alterações os valores apresentados na guia Apuração Simples Nacional do período de apuração do tributo serão da seguinte maneira, exemplo:  
A empresa se enquadra no Anexo I - Comércio. Tabela Anexo I (LC 155/16) disponibilizada pela Receita

|  |  |  |
| --- | --- | --- |
| Receita Bruta em 12 meses (em R$) | Alíquota | Valor a Deduzir (em R$) |
| Até 180.000,00 | 4% | - |
| De 180.000,01 a 360.000,00 | 7,30% | 5.940,00 |
| De 360.000,01 a 720.000,00 | 9,50% | 13.860,00 |
| De 720.000,01 a 1.800.000,00 | 10,70% | 22.500,00 |
| De 1.800.000,01 a 3.600.000,00 | 14,30% | 87.300,00 |
| De 3.600.000,01 a 4.800.000,00 | 19,00% | 378.000,00 |

1 - Para o cálculo iremos considerar que a receita do período foi de R$155.122,00 e a Receita Bruta dos últimos 12 meses correspondente a R$1.551.138,00.

Neste caso a empresa se enquadra na 4ª faixa da tabela do Anexo I (De 720.000,01 a 1.800.000,00), com a Alíquota Nominal de 10.70% e Valor a Deduzir de R$22.500,00.

|  |  |  |
| --- | --- | --- |
| Receita Bruta em 12 meses (em R$) | Alíquota | Valor a Deduzir (em R$) |
| De 720.000,01 a 1.800.000,00 | 10,70% | 403.317,20 |

2 - O cálculo do Percentual de Repartição considerando os % informados na Alíquota do Simples Nacional, exemplo:

* IRPJ = 4,00
* CSLL = 3,50
* COFINS = 12,82
* PIS/PASEP = 2,78
* CPP = 43,40
* ISS = 33,50

Que resulta: 4,00 %  3,50%  12.82%  2,78%  43,40%  33,50% **100%**

Figura

Sequência de cálculo realizada:

* Alíquota efetiva ((1.551.138,00¹  10,70%²  125.640,00³)  1.551.138,00)**2,60%**

* Percentual de Repartição cadastrado: 4.00%  3.50%  12.82%  2.78%  43.40%  33,50% **100%**

* Alíquota Ajustada (Alíquota efetiva  Percentual de Repartição cadastrado)  2,60%  100% **2,60%⁴**

* Valor a ser recolhido (Faturamento do mês  Alíquota Ajustada) 155.122,00 x 2,60% **403.317,20**

**¹Onde**: Receita Bruta acumulada nos 12 (doze) meses.  
**²Onde**: Alíquota Nominal constante no Anexos I informado no cadastro de Alíquota do Simples.  
**³Onde**: Valor a Deduzir conforme constate na tabela do Anexo I cadastro de Alíquota do Simples.  
**⁴Onde**: Alíquota Efetiva

3 - O cálculo no período de apuração será apresentado da seguinte maneira:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mês Referente a Receita** | **Valor da Receita** | **Alíquota** | **Valor do Imposto** | **Receita Último 12 meses** |
| Abril | 155.122,20 | 2,60 | 403.317,20 | 1.551.138,00 |

### 05.05. Regras

O cálculo do faturamento de referência para enquadramento da alíquota de empresas optantes pelo Regime de Apuração Simplificado (Simples Nacional) deve considerar as regras abaixo.

A regra geral é utilizar a receita bruta total acumulada nos 12 (doze) meses anteriores ao do período de apuração (RBT12).  
No caso de empresa optante desde o início de suas atividades, ela utilizará a RBT12 proporcional ao período de atividade da empresa. Isso significa que:  
1. No primeiro mês, a RBT12 proporcional será a receita do próprio mês de apuração multiplicada por doze; e  
2. nos 11 meses posteriores ao do início de atividade, a RBT12 proporcional será a média aritmética da receita bruta acumulada dos meses anteriores ao do período de apuração, multiplicada por 12 (doze);  
3. no 13º mês de atividade, passa-se a utilizar a RBT12 da regra geral  
   
Já no caso em que a empresa só é optante a partir de janeiro do ano seguinte ao do início de suas atividades, ela utilizará a regra prevista no item 2 até chegar ao período de apuração do 13º mês de atividade, quando, então, adotará a regra geral

### 05.06. Exemplo de cálculo

1. Empresa optante no **primeiro mês** de atividade:  
**PA (período de apuração) =** julho/2018  
**RPA (receita do PA) =** R$ 9.000,00  
**RBT12 proporcionalizada =** R$ 9.000,00 × 12 = R$ 108.000,00  
Enquadramento: (1ª faixa de receita dos Anexos da LC 123 de 2006)  
   
2. Empresa optante no **segundo mês** de atividade:  
**PA =** agosto/2018  
**RPA =** R$ 40.000,00  
**Receita Bruta do mês anterior:**  \* julho/2018 = R$ 9.000,00

**RBT12 proporcionalizada =** R$ 9.000,00 × 12 = R$ 108.000,00  
Enquadramento: (1ª faixa de receita dos Anexos da LC 123, de 2006)  
   
3. Empresa optante no **terceiro mês** de atividade:  
**PA =** setembro/2018  
**RPA =** R$ 6.000,00  
**Receitas dos meses anteriores:** \* julho/2018 = R$ 9.000,00

* agosto/2018 = R$ 40.000,00

**MA (média aritmética) =** (R$ 9.000,00 + R$ 40.000,00) / 2 = R$ 24.500,00  
**RBT12 proporcionalizada (MA × 12) =** R$ 24.500,00 × 12 = R$ 294.000,00  
Enquadramento: (2ª faixa de receita dos Anexos da LC 123, de 2006)  
   
4. Empresa optante no **quarto mês** de atividade (com receita zero em alguns PA):  
**PA =** outubro/2018  
**RPA =** R$ 50.000,00  
**Receita dos meses anteriores:** \* julho/2018 = R$ 0,00

* agosto/2018 = R$ 0,00
* setembro/2018 = R$ 60.000,00

**MA (média aritmética) =** (R$ 0,00 + R$ 0,00 + R$ 60.000,00) / 3 = R$ 20.000,00  
**RBT12 proporcionalizada (MA × 12) =** R$ 20.000,00 × 12 = R$ 240.000,00  
Enquadramento: (2ª faixa de receita dos Anexos da LC 123, de 2006)

## **06. Redistribuição de ISS**

### 06.01. Introdução

De acordo com a Lei Complementar nº 155/2016 Art. 18 e em conformidade com a Resolução CGSN nº 94/2011, arts. 9º, § 1º e 20, Anexos I a V, para fins de aplicação do regime simplificado do Simples Nacional, consideram-se:

a) **alíquota nominal** - aquela constante dos Anexos I a V da Resolução CGSN nº 94/2011;

b)**alíquota efetiva -** o resultado de: (RBT12 x Aliq -PD) / RBT12, em que:b.1) RBT12: receita bruta acumulada nos 12 meses anteriores ao período de apuração;b.2) Aliq: alíquota nominal constante dos Anexos I a V da Resolução CGSN nº 94/2011;b.3) PD: parcela a deduzir constante dos Anexos I a V dessa Resolução;

c) **percentuais efetivos de cada tributo** - aqueles calculados a partir da alíquota efetiva, multiplicada pelo percentual de repartição constante dos Anexos I a V da citada Resolução, observando-se que:

c.1)  o  percentual  efetivo  máximo  destinado  ao  ISS  será  de  5%  e  que  eventual  diferença  será  transferida,  deforma proporcional, aos tributos federais da mesma faixa de receita bruta anual;

Conforme orientação acima o cálculo da apuração do Simples Nacional, no encerramento do período, foi alterado para considerar a redistribuição dos tributos federais em uma eventual diferença quando a alíquota destinada ao ISS for superior a 5%.  
  
Segue abaixo detalhamento do novo cálculo quando o faturamento ultrapassa o sublimite:  
  
Considere:  
**RBT12**: Receita Bruta dos últimos 12 meses;  
**RBA**: Receita Bruta acumulada no ano corrente;  
**RPA**: Receita Bruta do mês.

Parcela da RPA que não excedeu o sublimite (P1)  RPA  P2  
Parcela da RPA que excedeu o sublimite (P2)  RBA  sublimite   
Alíquota Efetiva ((RBT12  alíquota nominal da respectiva faixa)  parcela a deduzir da faixa)  RBT12  
Valor parcial devido  Parcela do faturamento do mês que não excedeu o sublimite  (alíquota efetiva da 6ª faixa  percentual ISS da 5ª faixa)  
Alíquota Efetiva do Excesso Apurado  ((Sublimite  Alíquota Nominal Aplicada)  Parcela a Deduzir))  Sublimite  
Valor do Excesso Apurado  Alíquota Efetiva do Excesso Apurado  Parcela excedente (P2)  
Valor Total Devido  Valor do Excesso Apurado  Valor parcial devido

### 06.02. Exemplos de Cálculos

### 06.03. Referências

* [https://tdn.totvs.com/pages/releaseview.action?pageId=721718904](https://tdn.totvs.com/pages/releaseview.action?pageId=721718904 "Follow link")
* <https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/PerguntaoSN.pdf>
* <https://www8.receita.fazenda.gov.br/simplesnacional/arquivos/manual/manual_pgdas-d_2018_v4.pdf>

## **07. Outras Informações**

* [Encerramento Período de Apuração - Simples Nacional](http://tdn.totvs.com/pages/viewpage.action?pageId=334335674)
* [Apuração do Simples Nacional](http://tdn.totvs.com/pages/viewpage.action?pageId=219695050)
* [Simples Nacional - Responsabilidade do recolhimento - Serviço de código 7.10 Limpeza, manutenção e conservação de vias e logradouros públicos](https://tdn.totvs.com/display/public/ConSeg/Simples+Nacional+-+ISS+-+Responsabilidade+do+recolhimento)
