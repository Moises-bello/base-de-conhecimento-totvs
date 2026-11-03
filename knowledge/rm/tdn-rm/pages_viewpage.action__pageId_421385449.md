---
content_hash: 03290e06d1fe6b6d151073f9df8ade39f99d1e47db8d030754a76878273ef14b
fetched_at: '2026-06-29T00:09:16.062660+00:00'
page_id: '421385449'
product: rm
source: tdn-rm
title: Importar Apropriação de Insumo/Serviço via Excel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385449
version: 3
---

---

A funcionalidade de importação de Apropriação de Insumo/Serviço via Excel, permite com que seja feita a importação de lançamentos realizados numa planilha do Excel para as respectivas tarefas nas planilhas de atividades e serviços, atualizando através dos lançamentos a quantidade do insumo apropriado naquela tarefa.

Para realizar a importação é necessário que a planilha do Excel esteja estruturada devidamente, ou seja, cada tarefa é representada por uma linha na planilha, já as colunas, representam a quantidade, o código do insumo, a data de movimento, data da apropriação, código do funcionário, funcionário responsável, pessoa, pessoa responsável, evento, bem, preço, moeda, motivo de improdutividade e observação.

**REGRAS GERAIS:**  
 Não é permitido efetuar importação onde a data apropriação é inferior a data mínima para apropriação definida nos parâmetros do projeto, através do menu Opções | Parâmetros | RM Solum | Projetos, pasta Apropriação, campo Data Limite para Apropriação. Ao informar que o insumo não poderá ser fracionado em seu cadastro, mas na planilha de apropriação esse insumo estiver com quantidade fracionada, o sistema arredondara a quantidade de acordo com o parâmetro do projeto. Se o preço do insumo na planilha de apropriação não estiver na moeda do projeto, ele pode sofrer uma indexação, conversão ou ambas de acordo com a parametrização do projeto. Não será possível importar a planilha se caso algum dos campos obrigatórios estiver em branco ou igual a 0. Lançamentos que possuem código diferente aos códigos da planilha não serão importados. A importação é interrompida ao encontrar uma linha em branco, a linha em branco representa o final do documento.

Segue abaixo os passos necessários para realizar a importação de apropriação de insumos/serviços via Excel:

**IMPORTAR APROPRIAÇÃO DE INSUMOS/SERVIÇOS VIA EXCEL:**

Acessar dentro do projeto o menu Conversões > Importar Apropriação de Insumos/Serviços via Excel > Informar a localização do arquivo, que está localizado na máquina. - No campo Linha Inicial, deverá ser informado qual linha da planilha se inicia os dados a serem importados. - No campo Código da Tarefa, deverá ser informado o número da coluna na planilha que refere-se ao código da tarefa. **Esse campo é obrigatório.** - No campo Quantidade, deverá ser informado o número da coluna na planilha que refere-se a quantidade. **Esse campo é obrigatório.** - Os demais campos, não são obrigatórios, serão preenchidos com o número da coluna referente aos dados localizados na planilha. Após essas informações, pode confirmar clicando em 'Executar'. Abaixo, um exemplo de planilha estruturada para importação e a configuração de colunas na tela de importação:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Tarefa (1)** | **Quatde(2)** | **Insumo(3)** | **DataMov(4)** | **DataAprop(5)** | **Cod Func(6)** | **Cod Func Resp(7)** | **Cod Pessoa(8)** | **Cod pessoa Resp(9)** | **Cod Evento(10)** | **Cod Bem(11)** | **Preço(12)** | **Moeda(13)** | **Cod Mot Improd.(14)** | **Obs.(15)** |
| 002.01.01 | 1 | F00001 | 20/01/2015 | 20/01/2015 |  |  |  |  |  | 06.01 |  |  | 01 | Teste Importação do Bem |
| 002.01.02 | 1 | F00002 | 21/01/2015 | 21/01/2015 | 32 |  |  |  |  |  |  |  | 02 | Teste Importação do Func |
