---
content_hash: 2b8fc0d84c72416ff811f8d730234c0e233c551e96297c95f219710a785b8549
fetched_at: '2026-06-29T00:05:55.194099+00:00'
page_id: '126714055'
product: rm
source: tdn-rm
title: COMO FAZER - Diferença Salarial e SEFIP por Dissídio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=126714055
version: 1
---

**Produto**: TOTVS Folha de Pagamento                             **Versão**: 11.4X e superiores  
**Processo de Negocio**: Processo de cálculo de diferença salarial por dissídio  
**Subprocesso**: Diferença salarial por dissídio

##### Introdução

Este documento visa demonstrar o processo de cálculo de diferença salarial por dissídio. Também será demonstrado, como gerar a guia da SEFIP nos meses em que ocorrer o lançamento destas diferenças.  
Procedimentos a serem realizados antes do cálculo da diferença salarial:  
  
**1 –** Para o cálculo da diferença salarial por dissídio, os seguintes eventos devem estar cadastrados na base de dados [módulo CADASTROS -> EVENTOS]:  
  
**\* DIFERENÇA SALARIAL – DISSÍDIO**  
Este evento deve ser um Provento, Valor e ter o código de cálculo 37.  
NÃO tem incidência em INSS.

**\* BASE DE FGTS DE DIFERENÇA SALARIAL**  
Este evento deve ser Base de cálculo, Valor e ter o código de cálculo 69.  
Não tem nenhuma incidência.

**\* ESTORNO BASE INSS DISSÍDIO RET.FOLHA**  
Este evento deve ser Base de cálculo, Valor e ter o código de cálculo 114.  
Ele deve ter incidência em Estorna INSS de folha.  
  
  
  
  
**\* DIFERENÇA DE PENSÃO ALIMENTICIA FOLHA**  
Este evento deve ser um Desconto, Valor e ter o código de cálculo 195.  
Ele ter incidência em Dedutível IRRF de folha.

**2 -** Acessar o cadastro do funcionário, módulo CADASTROS -> FUNCIONÁRIOS, aba “Base de cálculo”, sub-aba “Base de cálculo”. Alterar o salário informando a data do dissídio e o motivo da alteração.  
  
**Antes da alteração**  
  
  
  
**Dados da alteração**  
  
  
  
  
**Histórico salarial após a alteração**  
  
  
  
  
Os eventos de diferença salarial podem ser lançados de forma discriminada ou em um único evento (evento de código de cálculo 37).  
  
**\* Cálculo da diferença utilizando apenas o evento de código de cálculo 37:**  
Segue abaixo um exemplo deste processo:  
  
No mês de setembro, o salário do funcionário acima, foi alterado para R$ 1000,00, com data retroativa a 01/08/2010. O salário anterior do funcionário, era R$ 850,00.  
A folha de agosto da empresa já estava fechada e a competência atual do RM Labore é setembro.  
  
**1** – Acessar o módulo MOVIMENTO -> FOLHA DE PAGAMENTO -> LANÇAMENTOS AUTOMÁTICOS -> DIFERENÇA SALARIAL.  
  
Preencher os seguintes campos:  
• Código de quebra: este campo deve ser preenchido de acordo com seu cadastro de seções;  
• Informar a seleção de funcionários;  
• Dissídio: SIM;  
• Competência inicial: Informar o primeiro mês em que será calculada a diferença;  
• Competência final: Informar o último mês em que será calculada a diferença;  
• Utiliza jornada para o cálculo da diferença: Ao marcar este campo, o sistema passa a utilizar o valor do salário hora para realizar o cálculo da diferença salarial do funcionário (exemplo no Help do aplicativo);  
• Aumentos a desconsiderar: Esta função servirá para desconsiderar aumentos que foram concedidos dentro do período de apuração da diferença  
  
Clicar no botão ‘Lançar’.

O envelope do funcionário ficará da seguinte maneira:  
  
**Envelope do mês de agosto**  
  
  
  
**Envelope da diferença salarial referente ao mês de agosto**  
  
  
  
  
No evento ‘0244 – DIFERENÇA SALARIAL – DISSÍDIO’, foi lançado o valor de R$ 163,64 que equivale a:  
- R$ 150 referente à diferença do evento ‘0002 – DIAS TRABALHADOS’  
- R$ 13,64 referente à diferença do evento ‘0083 – HORAS EXTRA 100%’  
  
  
  
**\* Cálculo da diferença utilizando eventos discriminados:**  
  
Segue abaixo um exemplo deste processo (usaremos a mesma situação acima neste exemplo) :  
  
**1** - Acessar o módulo CADASTROS -> EVENTOS e criar um evento de diferença salarial para o evento de horas extras. Este Evento terá as mesmas incidências do evento de horas extras, somente o código e a descrição serem diferentes.  
  
OBS: este evento deve ser do tipo VALOR.  
  
  
  
  
**2** – Acessar o cadastro do evento ‘0083 – HORA EXTRA 100%’.  
No campo ‘Evento de diferença de salário’, informar o evento de diferença criado anteriormente.

**3** – Processar o módulo MOVIMENTO -> FOLHA DE PAGAMENTO -> LANÇAMENTOS AUTOMÁTICOS -> DIFERENÇA SALARIAL (a parametrização deve ser a mesma informada no exemplo anterior).  
  
O envelope do funcionário ficará da seguinte maneira:  
  
**Envelope do mês de agosto**  
  
  
  
**Envelope da diferença salarial referente ao mês de agosto**  
  
  
  
  
Os eventos de diferença salarial foram discriminados no envelope do funcionário.  
  
Notem que neste processo, o sistema lançou o evento ‘0250 - ESTORNO BASE INSS DISSÍDIO RET.FOLHA’.  
Este evento irá estornar a base de INSS referente ao valor do evento ‘0083 – HORA EXTRA 100%’.  
Este valor será somado ao evento ‘0238 – BASE DE FGTS DE DIFERENÇA SALARIAL’, que será considerado na geração do arquivo SEFIP.  
  
  
**Geração do arquivo SEFIP:**  
  
Quando houver diferença salarial por dissídio, o procedimento referente à geração do arquivo SEFIP será um pouco diferente.  
  
Será necessário gerar dois arquivos distintos.  
  
**1** – O primeiro arquivo é o padrão gerado na rotina mensal da empresa.  
Nele serão consideradas as verbas mensais lançadas para o funcionário, ou seja, as verbas que não foram geradas por diferença salarial;  
  
**2** – O segundo arquivo, deverá ser gerado utilizando o código de recolhimento 650.  
Nele serão consideradas as verbas geradas por diferença salarial.  
OBS: Será considerado o valor do evento ‘0238 – BASE DE FGTS DE DIFERENÇA SALARIAL’, que soma o valor de todos os eventos de diferença salarial lançados no envelope dos funcionários.  
  
Segue abaixo um exemplo de como gerar este arquivo:  
  
- Acessar o módulo RELATÓRIOS -> SEFIP -> PARÂMETROS DO SEFIP .NET.  
Informar a competência de geração do arquivo e o código de recolhimento 650.  
Clicar no botão ‘Incluir’.  
  
  
  
Na aba “Identificação”, será necessário informar novamente o mês de geração do arquivo, o código de recolhimento 650 e a seção centralizadora do CNPJ.  
  
  
  
Na aba “Valores I” será necessário informar os dados referentes às ‘Informações de processo’.  
Estes campos devem ser preenchidos com as informações referentes ao dissídio e podem ser verificadas com o sindicato do funcionário.  
  
  
  
Após isso, acessar o módulo CADASTROS -> SEFIP -> SEFIP .NET.  
  
Na aba “Recolhimento e Declaração”, informar os dados referentes à geração do arquivo.  
A competência deve ser a atual e o código de recolhimento deve ser o 650.  
  
  
  
Na tela de “Seleção de coligadas”, selecionar a coligada e clicar no botão ‘Adicionar parâmetros à coligada’.  
  
  
  
  
Na aba “Geral”, poderá ser criada uma parametrização específica para a coligada selecionada.  
Se não for necessário, o parâmetro ‘Usar parâmetros específicos’ deverá estar desmarcado.  
  
  
  
Na aba “Dissídio”, os campos ‘Data do dissídio’ e ‘Retroativo a’ devem ser preenchidos.  
  
  
  
Finalizar o processo de geração do arquivo da SEFIP.  
  
Ao importar o arquivo no programa da SEFIP, os valores referentes à diferença salarial, são levados corretamente.  
  
  
  
Fim do procedimento.
