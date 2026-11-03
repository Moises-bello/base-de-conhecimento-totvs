---
content_hash: 1586c3df17fb8256b5861cc9d3c85b8be644144bf85c7408d22e96693df7ae16
fetched_at: '2026-06-29T00:11:51.369553+00:00'
page_id: '847884848'
product: rm
source: tdn-rm
title: DT - Smart View - Espelho de Ponto Digital
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Smart+View+-+Espelho+de+Ponto+Digital
version: 36
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Função: | Emitir o Espelho de Ponto Digital via Smart View |
| País: | Brasil |
| Requisito/Story/Issue: | [DRHJORNRM-6193](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-6193) |

## **02. SITUAÇÃO/REQUISITO**

Emitir o relatório do Espelho de Ponto Digital via Smart View.

## **03. SOLUÇÃO**

Desenvolvido o relatório do Espelho de Ponto Digital para ser emitido via Smart View.

## **04. VERSÕES**

12.1.2406.100 até 12.1.2406.305.

## **05. CONFIGURAÇÃO**

Para gerar o Espelho de Ponto Digital via Smart View é necessário realizar a instalação e configuração conforme os artigos abaixo:

1 - [Instalação Smart View](https://tdn.totvs.com/pages/viewpage.action?pageId=626926739)

2 - [Configuração do RM para integrar ao Smart View](https://tdn.totvs.com.br/pages/releaseview.action?pageId=725737666)

3 - Importar o recurso smart view **PTOTRP0002 - Espelho de Ponto Digital** através do [TOTVS Compartilhamento](https://tdn.totvs.com/display/public/LRM/TOTVS+Compartilhamento#TOTVSCompartilhamento-DownloaddeobjetogerencialnoTOTVSCompartilhamento)

## **06. EXEMPLO DE UTILIZAÇÃO**

11Emitir Espelho de Ponto Digital via Smart View Agent

1. Acessar o **Smart View**.

2. Clicar em **Relatórios**.

3. Clicar em **Visualizar** no relatório do **Espelho de ponto Digital**.

4. Informar os parâmetros **Cód. Coligada**, **Matrícula do Funcionário**, **Data Início**, **Data Fim**, **Departamento**, **Nome Social** e **Imprimir Marcações Desconsideradas**. Os parâmetros são obrigatórios.   
 **Importante:**

* Para conseguir preencher os parâmetros **Cód. Coligada**, **Matrícula do Funcionário** e **Departamento** é necessário clicar em

* Para filtrar mais de uma coligada, matrícula e departamento é necessário adicionar mais campos, fazemos isso clicando no botão  mais vezes

* Para filtrar todas as coligadas, matrículas e departamentos de uma só vez é necessário informar o valor -1 nos parâmetros

5. Clicar em **Enviar**.

6. O Espelho de Ponto Digital será exibido.

2Emitir Espelho de Ponto Digital via RM

1. Acessar o menu **Gestão**.

2. Clicar em **SV**.

3. Selecionar o recurso **PTOTRP0002 Espelho de ponto Digital**.

4. Clicar em **Mais ações > Executar no Smart View**.

5. Informar os parâmetros **Cód. Coligada**, **Matrícula do Funcionário**, **Data Início**, **Data Fim**, **Departamento**, **Nome Social** e **Imprimir Marcações Desconsideradas**.Os parâmetros são obrigatórios.   
 **Importante:**

* Para conseguir preencher os parâmetros **Cód. Coligada**, **Matrícula do Funcionário** e **Departamento** é necessário clicar em

* Para filtrar mais de uma coligada, matrícula e departamento é necessário adicionar mais campos, fazemos isso clicando no botão  mais vezes

* Para filtrar todas as coligadas, matrículas e departamentos de uma só vez é necessário informar o valor -1 nos parâmetros

6. Clicar em **Enviar**.

7. O Espelho de Ponto Digital será exibido.

3Informações Complementares

* **Parâmetros:**
  + **Cód.Coligada:** Deve ser informado o código da coligada que deseja emitir o relatório.
  + **Matrícula do Funcionário:** Deve ser informado a chapa do funcionário.
  + **Data Início:** Deve ser informado a data inicial do período do relatório.
  + **Data Fim:** Deve ser informado a data final do período do relatório.
  + **Departamento:** Deve ser informado a seção do funcionário.
  + **Nome Social:** Deve ser informado se deseja ou não exibir o nome social do funcionário. 'Verdadeiro' exibe o nome social se houver no cadastro do funcionário, 'Falso' exibe o nome civil do funcionário.
  + **Imprimir Marcações Desconsideradas:** Deve ser informado se deseja ou não exibir as marcações desconsideradas do funcionário. 'Verdadeiro' exibe as marcações desconsideradas, 'Falso' não exibe as marcações desconsideradas.
* **Jornada contratual:** este campo é preenchido no relatório com a última jornada vinculada ao funcionário no período.

* **Resumo de horas extras:** Os campos **Extras normais, Extras feriado, Extras descanso/folga e Extras adic. noturno** são preenchidos com o valor total de cada tipo de extra realizada no período do relatório. São consideradas extras que foram para o banco de horas ou movimento e extras autorizadas ou não autorizadas.
* **Marcações Desconsideradas:** Para que as marcações desconsideradas sejam exibidas é necessário que o parâmetro **'Imprimir Marcações Desconsideradas'** esteja com o valor **'Verdadeiro'**. As marcações serão exibidas após as marcações da jornada. Segue exemplo abaixo:
* **Total de marcações superando 10 batidas no dia:** Se as marcações realizadas superarem 10 batidas no dia sendo elas marcações consideradas e/ou desconsideradas, o dia em questão será exibido exibido duas vezes para exibir todas as batidas. Segue exemplo abaixo:
* **Total de horas:** O campo **T.horas** é alimentado com as horas trabalhadas na jornada, o valor é exibido na data da jornada de referência, segue exemplos abaixo:  
    
  **Jornada diurna:** Na imagem abaixo a jornada inicia no dia 01/04 e finaliza no dia 01/04, o **T.horas** será exibido no dia 01/04 pois é a data de referência da jornada.  
    
    
    
  **Jornada noturna:** Na imagem abaixo a jornada inicia no dia 08/04 e finaliza no dia 09/04, o **T.horas** será exibido no dia 08/04 pois é a data de referência da jornada.  
    
    
    
  **Jornada noturna com horário contíguo:** Na imagem abaixo a jornada inicia no dia 08/04 e finaliza no dia 09/04, o **T.horas** será exibido no dia 08/04 pois é a data de referência da jornada.
* **Feriado:** O nome do feriado é exibido no relatório somente se não houver batidas no dia do feriado, se houver batidas será exibido apenas as batidas. Segue exemplo abaixo:  
    
  **Dia de feriado sem batidas realizadas**  
    
    
  **Dia de feriado com batidas realizadas**
* **Detalhamento de horas:** Os valores de **Abono**, **Atraso**, **Falta**, **Hora extra**, **Adic.noturno**, **B.de Horas(+)**, **B.de Horas(-)** e **Justificativas** são exibidos na data de referência da jornada.
* **Justificativas:** Se houver mais de uma justificativa para ocorrências da mesma jornada, os valores serão exibidos apenas em um registro e nos demais será exibido apenas a justificativa. Segue exemplo abaixo:
Atenção

O Relatório do Espelho de Ponto Digital evoluiu e possui novos campos. Para conferir acesse a documentação: [Adição dos parâmetros 'Imprimir Eventos do Movimento do Período', 'Imprimir Campos Complementares' e 'Imprimir Horas Extras' no Espelho do Ponto Digital](https://tdn.totvs.com/pages/viewpage.action?pageId=856935871) .

## **07. ASSUNTOS RELACIONADOS**
