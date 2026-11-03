---
content_hash: c0ea704477a22269d3293378655e53d5eac064d9f08442dc449cadfb67388cf6
fetched_at: '2026-06-29T00:09:16.056226+00:00'
page_id: '421385448'
product: rm
source: tdn-rm
title: Insumo/Serviço - Importar Apropriação de Insumo/Serviço via Excel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385448
version: 7
---

---

A funcionalidade de importação de Apropriação de Insumo/Serviço via Excel, permite que seja feita a importação de lançamentos realizados numa planilha do Excel para as respectivas tarefas nas planilhas de atividades e serviços, atualizando através dos lançamentos a quantidade do insumo apropriado naquela tarefa.  
 Para realizar a importação é necessário que a planilha do Excel esteja estruturada devidamente, ou seja, cada tarefa é representada por uma linha na planilha, já as colunas, representam a quantidade, o código do insumo, a data de movimento, data da apropriação, código do funcionário, funcionário responsável, pessoa, pessoa responsável, evento, bem, preço, moeda, motivo de improdutividade e observação.

**Atenção:** A partir da versão 12.1.5, a importação de Apropriação de Insumo/Serviço via Excel, não será necessário ter o pacote Office instalado com o recurso Excel no ambiente em que está fazendo a importação.

**Observação:** Não é permitido efetuar importação onde a data apropriação é inferior a data mínima para apropriação definida nos parâmetros do projeto. Ao informar que o insumo não poderá ser fracionado em seu cadastro e na planilha de apropriação esse insumo estiver com quantidade fracionada, o sistema arredondará a quantidade de acordo com o parâmetro de projeto. Se o preço do insumo na planilha de apropriação não estiver na moeda do projeto, ele pode sofrer uma indexação, conversão ou ambas de acordo com a parametrização do projeto. Não será possível importar a planilha se caso algum dos campos obrigatórios estiver em branco ou igual a 0. Lançamentos que possuem código diferente aos códigos da planilha não serão importados. A importação é interrompida ao encontrar uma linha em branco, pois a mesma representa o final do documento.  
Segue abaixo os passos necessários para realizar a importação de apropriação de insumos/serviços via Excel:   
Acessar dentro do projeto o menu Projeto > Conversões > Importar Apropriação de Insumos/Serviços via Excel > Informar a localização do arquivo, que está localizado na máquina. No campo Linha Inicial, deverá ser informado qual linha da planilha se inicia os dados a serem importados. No campo Código da Tarefa, deverá ser informado o número da coluna na planilha que refere-se ao código da tarefa. Esse campo é obrigatório. No campo Quantidade, deverá ser informado o número da coluna na planilha que refere-se a quantidade. Esse campo é obrigatório.  Os demais campos, não são obrigatórios, serão preenchidos com o número da coluna referente aos dados localizados na planilha. Após essas informações, execute.

**Exemplo:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Tarefa (1)** | **Quantidade(2)** | **Insumo(3)** | **DataMov(4)** | **DataAprop(5)** | **Cod Func(6)** | **Cod Func Resp(7)** | **Cod Pessoa(8)** | **Cod pessoa Resp(9)** | **Cod Evento(10)** | **Cod Bem(11)** | **Preço(12)** | **Moeda(13)** | **Cod Mot Improd.(14)** | **Obs.(15)** |
| 002.01.01 | 1 | F00001 | 20/01/2015 | 20/01/2015 |  |  |  |  |  | 06.01 |  |  | 01 | Teste Importação do Bem |
| 002.01.02 | 1 | F00002 | 21/01/2015 | 21/01/2015 | 32 |  |  |  |  |  |  |  | 02 | Teste Importação do Func |
