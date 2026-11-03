---
content_hash: 597b1166e35474556e19c210ff5df714ff913e5c30ce2d326b5de629cdba6d11
fetched_at: '2026-06-29T00:08:17.147036+00:00'
page_id: '253987681'
product: rm
source: tdn-rm
title: DT_Remuneração Base do Professor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=253987681
version: 108
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Informe o segmento.* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Função:** | *Informe a função.* |
| **Situação/Requisito:** | *Informe a situação/requisito.* |
| **Solução/Implementação:** | *Informe a solução/implementação.* |
| **Conversores e Parâmetros:** | *Informe os conversores/parâmetros.* |
| **Chamados relacionados:** | *Informe o(s) chamado(s) relacionado(s).* |
| **Requisito (ISSUE):** | *Informe o requisito relacionado.* |

### 1. Cadastro de Evento

Foi criado o parâmetro “Compõe Remuneração Base de Professor”, onde o usuário irá marcar os eventos, cujo valores serão utilizados para apuração da média de Remuneração.

Caso algum evento deva ser considerado somente na remuneração de um determinado Sindicato, esse só deve constar na ficha financeira de funcionários deste Sindicato.

### 2. Cadastro de Sindicato

Foi criado um parâmetro para habilitar todo o processo “Utiliza cálculo de média de Remuneração Base para Professor”.  
Caso esta opção seja marcada, serão habilitadas as abas específicas, e alterado o salário base de todos os funcionários tipo P – Professor, nos cálculos de Férias, 13º Salário, Rescisão e Salário Maternidade.

**2.1. Aba “Remuneração Base”**

Nesta pasta serão exibidas 6 subpastas com parâmetros para o cálculo da Remuneração nos 6 tipos de cálculo: Férias, Férias Rescisão, 13º Salário, 13º Rescisão, Aviso Prévio, Licença Maternidade.

**2.1.1. Campos que irão constar em todas as subpastas:**

* - “No caso de valor proporcionalizado, efetuar engenharia reversa para obter valor integral”

Quando for marcado este parâmetro, será aplicada uma proporção tipo “regra de 3” na carga horária dos eventos do tipo Hora e no valor calculado nos eventos tipo Valor, para os funcionários que não trabalharam a escala integral do mês competência.

Segue um exemplo:

Deverá considerar a remuneração 4741,27.

Para calcular os valores integrais dos meses 12/2015 e 01/2016 devido a férias, deverá realizar uma engenharia reversa para obter o valor integral, já que os valores estão proporcionalizados no mês.  
Férias no período de 29/12 a 27/01  
12/2015 – 3 dias férias – 27 dias trabalhados  
01/2016 – 27 dias férias – 3 dias trabalhados  
12/2015 = (380,06 / 27) \* 30 = 422,29  
01/2016 = (42,23 / 3) \* 30 = 422,29

* - “Quantidade de meses”

Neste campo deverá ser informado os últimos N meses a serem utilizados para apuração da média.  
Somente para os cálculos de Férias Normais e Férias na Rescisão, se for informado zero, serão considerados os meses do Período Aquisitivo.  
Caso a admissão do funcionário tenha ocorrido após a projeção do período de apuração, a quantidade de meses será diminuída proporcionalmente aos meses trabalhados.  
Por exemplo, se foi solicitada a média dos últimos 12 meses, e o funcionário foi admitido somente a 7 meses atrás, o cálculo da média passará a ser dos últimos 7 meses.

* - Deverá ser selecionado um dos tipos de cálculo abaixo (Descrição detalhada no item 3):

A- Maior Remuneração  
B- Média da Remuneração  
C- Última Remuneração  
D- Comparativo Média X Última Remuneração

**2.1.2. Campo existente somente nas subpastas 13º Salário e 13º Rescisão**

* - Desconsiderar meses do ano competência anterior.

Considerando um exemplo de rescisão no mês 08/2016, com este parâmetro marcado, será calculada a média dos últimos 7 meses, de 01/2016 a 07/2016.  
O último mês a ser considerado é sempre o mês anterior à competência do cálculo.

### 3. Tipos de Cálculo

**3.1. Maior Remuneração**

Nesta opção será verificada a quantidade de meses informada pelo usuário, e buscar nos últimos N meses o maior valor total, somando os valores de todos os eventos marcados com a incidência citada no item 1.

Este somatório de valores será efetuado aplicando a carga horária dos eventos do tipo Hora ao salário atual, e somando o valor pago na época dos eventos tipo Valor.  
O salário atual é a soma do Salário Composto vigente na competência corrente.

**3.2. Média da Remuneração**

Nesta opção irá buscar na ficha financeira, todas as ocorrências dos eventos marcados com a incidência citada no item 1, considerando o período de apuração informado no Sindicato, de acordo com cada processo de cálculo.

Para os eventos do tipo Hora, será apurada a média aritmética da carga horária do período para aplicar ao salário atual. Caso o evento tenha como Base de Salário um evento que não consta atualmente no cadastro de Salário Composto, será considerado o valor pago na época, sem a atualização para o salário atual.

Para os eventos do tipo Valor, será apurada a média aritmética do valor pago na época.  
No caso de haver aumento salarial retroativo, nos processos de Diferença as fórmulas serão recalculadas considerando o novo salário vigente.  
Se durante o período de apuração ocorrer algum mês em que o funcionário esteve integralmente afastado, sem nenhuma remuneração, será aplicada a última carga horária trabalhada antes do afastamento.

**3.3. Última Remuneração**

Nesta opção será considerada a Remuneração Integral do mês anterior, somando os valores de todos os eventos marcados com a incidência citada no item 1.  
Este somatório de valores será efetuado aplicando a carga horária dos eventos do tipo Hora ao salário atual, e somando o valor pago na época dos eventos tipo Valor.  
Se no mês anterior o funcionário esteve integralmente afastado, sem nenhuma remuneração, será considerada a última carga horária trabalhada antes do afastamento.

**3.4. Comparativo Média X Última Remuneração**

Nesta opção serão efetuados os cálculos descritos nos itens 3.2 e 3.3, e então aplicado o Maior valor entre eles.

### 4. Provisões de Férias e 13º Salário

A geração do histórico de Provisões, quando executado para funcionários Ativos considerará o mesmo cálculo parametrizado para “Férias Normais” e “13º Salário”, e quando a execução for para demitido no mês, o cálculo irá verificar a parametrização selecionada para “Férias Rescisão” e “13º Rescisão”.

### 5. Diferença Salarial

**5.1. Diferença de 13º Salário**

Quando ocorrer aumento salarial retroativo a dezembro, após o pagamento da 2ª Parcela do 13º Salário, deverá ser efetuado o cálculo da Diferença de 13º.

Neste processo será considerada a mesma parametrização utilizada no cálculo da 2ª Parcela, onde a Remuneração apurada será aplicada ao salário vigente em dezembro.  
Os eventos do tipo Hora terão a carga horária aplicada ao salário hora de dezembro, e os eventos tipo Valor com fórmula, terão as fórmulas recalculadas, considerando o novo salário e a parametrização vigente na competência dezembro.

**5.2. Diferença de Férias**

Quando ocorrer aumento salarial retroativo ao período em que o funcionário estiver de férias, deverá ser efetuado o cálculo da Diferença de Férias.

Neste processo será considerada a mesma parametrização utilizada no cálculo do Recibo de Férias, onde a Remuneração apurada será aplicada ao novo salário do funcionário.  
Os eventos do tipo Hora terão a carga horária aplicada ao novo salário hora, e os eventos tipo Valor com fórmula, terão as fórmulas recalculadas, considerando o novo salário e a parametrização vigente no mês das férias.  
Em uma situação de férias partidas, iniciando em um mês, e terminando no mês posterior, caso o aumento salarial comece a vigorar no início no segundo mês das férias, o valor calculado de diferença será proporcionalizado aos dias de férias do segundo mês.

**5.3. Rescisão Complementar**

Quando ocorrer aumento salarial retroativo ao mês de demissão do funcionário ou durante a projeção do Aviso Prévio Indenizado, deverá ser efetuado o cálculo da Rescisão Complementar.

Neste processo serão consideradas as mesmas parametrizações utilizadas no cálculo da Rescisão, considerando os tipos “Férias Rescisão”, “13º Rescisão” e “Aviso Prévio”, onde a Remuneração apurada será aplicada ao novo salário do funcionário.  
Os eventos do tipo Hora terão a carga horária aplicada ao novo salário hora, e os eventos tipo Valor com fórmula, terão as fórmulas recalculadas, considerando o novo salário e a parametrização vigente no mês do aumento.  
Caso o aumento salarial tenha início da vigência durante a projeção do Aviso Prévio Indenizado, no mês posterior ao mês da demissão, o aumento será aplicado proporcionalmente ao Aviso Prévio considerando somente os dias após a alteração salarial. No caso de Férias e 13º a diferença será paga integralmente com o novo salário.

### 6. Relatórios

Todos os processos efetuados para apurar a Remuneração Base do Professor serão exibidos em uma Memória de Cálculo através de arquivo txt.  
Todos os valores processados serão gravados em tabelas específicas para posterior utilização em relatórios.

divs
