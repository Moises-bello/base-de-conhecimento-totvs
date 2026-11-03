---
content_hash: b5bfca59a6493dbefa2c37168ce26847dd7ecf170b7c20bb61d75f93ba738a23
fetched_at: '2026-06-29T00:09:02.424667+00:00'
page_id: '379307979'
product: rm
source: tdn-rm
title: RMFIS00008 - ECF - Eventos Especiais (Cisão, Fusão, Incorporação, início de
  atividade, etc..)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=379307979
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.X |
| **Ocorrência:** | ECF - Eventos Especiais |
| **Ambiente:** |  |
| **Passo a passo:** | (OBS.: As implementações abaixo estão disponíveis a partir do Patch Específico 11.82.40.111)  As orientações que se seguem devem ser observadas pelas empresas que tiveram a ocorrência de eventos especiais durante o ano calendário, como:   * Extinção * Cisão * Fusão * Incorporação * Início de atividades * Desenquadramento de Imune/Isenta * Inclusão no Simples nacional     Nos Parâmetros do TOTVS Gestão Fiscal, acesse o Processo “**03.02.08 – IRPJ**”, Etapa 13 – “**Ocorrências de Cisão, Incorporação e Fusão**”, e inclua a Data da Ocorrência do evento especial:        Os Períodos de Apuração devem ser criados respeitando essa Data.  **Exemplo 1:**  Empresa tributada pelo **Lucro Real Anual**, realizou Cisão parcial no dia **15/03/2014**.   * Deve ser criado um período de apuração para cada mês para cálculo das estimativas mensais: janeiro, fevereiro e março. * Entretanto, no mês de março, esse período deve ser de **01/03/2014 à 15/03/2014**(compreende a data do evento). * Deve ser criado, também, um período “**anual**” que corresponderá ao ajuste anual, com o intervalo de **01/01/2014 à 15/03/2014**.       Para o período após o evento especial, segue a mesma regra:   * Deve ser criado um período de apuração para cada mês para cálculo das estimativas mensais: março, abril, maio, ... e dezembro. * Entretanto, no mês de março, esse período deve ser de **16/03/2014 à 31/03/2014**(inicia no dia subsequente à data do evento). * Deve ser criado, também, um período “**anual**” que corresponderá ao ajuste anual, com o intervalo de **16/03/2014 à 31/12/2014**.       No Anexo “Parâmetros da Escrituração Contábil Fiscal” do Cadastro da Filial, devem ser inseridos dois registros, um para cada período: antes da cisão e após a cisão:         1. Considerando o mesmo exemplo acima, a escrituração anterior à cisão, terá os seguintes dados:    1. **Intervalo**: “01/01/2014 à 15/03/2014”    2. **Indicador do início do Período**: Regular (Início no primeiro dia do ano)    3. **Indicador de Situação especial**: Cisão Parcial    4. **Data da Situação Especial/Evento**: 15/03/2014      1. A escrituração posterior à cisão, terá os seguintes dados:    1. **Intervalo**: “16/03/2014 à 31/12/2014”    2. **Indicador do início do Período**: Resultante de cisão/fusão ou remanescente de cisão, ou realizou incorporação    3. **Indicador de Situação especial**: Normal    4. **Data da Situação Especial/Evento**: não preencher     Para o ano calendário de 2014, deve ser gerado apenas o arquivo do segundo período uma vez que situações especiais ocorridas em 2014 devem ser entregues através da DIPJ.    Para situações especiais ocorridas em 2015, entretanto, devem ser gerados duas escriturações:   1. Uma para o período anterior ao evento, que deve ser entregue juntamente com a ECF de 2014, até 30/09/2014. 2. Outra para o período após o evento, que será entregue no período normal em 2016.     **Exemplo 2:**  No caso de **início das atividades**, a Data da Ocorrência, OBRIGATORIAMENTE, deve ser **o dia anterior ao evento**.  Suponhamos uma empresa tributada pelo Lucro Real Trimestral, que iniciou suas atividades no dia **11/01/2015**.  No Processo “**03.02.08 – IRPJ**”, Etapa 13 – “**Ocorrências de Cisão, Incorporação e Fusão**”, a Data da Ocorrência será 10/01/2015.        Isso é necessário para que o sistema permita a inclusão do período de apuração, que ficará assim:        A seleção do Evento Tributário para encerramento desses Períodos de Apuração, continua da mesma forma. O sistema irá selecionar o Evento Tributário vigente para o período através do Cadastro de Vigências.  **NOVIDADE:**  A partir da versão **12.1.22** também deverá ser informada a Filial de ocorrência da Cisão para que a mesma também não seja aplicada para as Filiais SCP quando houver. |
| **Observações:** |  |
