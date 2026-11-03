---
content_hash: 6aaf62f2e6dc7b48461a66bfeda4705470c01878a9e3f3cc1b9f147116ca8939
fetched_at: '2026-06-29T00:05:53.379686+00:00'
page_id: '1070064028'
product: rm
source: tdn-rm
title: Passo a Passo para atualizar o "Valor Dedução do Rendimento Tributável" do
  Dependente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1070064028
version: 13
---

false

**A partir das Versões:**

* [DT - Cadastro de Dependente - Valor Dedução do Rendimento Tributável](https://tdn.totvs.com/pages/viewpage.action?pageId=1068186521)
* [DT - Processo para atualizar Dedução por Dependente](https://tdn.totvs.com.br/pages/viewpage.action?pageId=1070066693)

## 

## **01. VISÃO GERAL**

Adequar o produto para atender à orientação da consultoria tributária TOTVS e ao retorno da SERPRO sobre o envio de dedução de dependentes no evento S-1210 do eSocial. [Link](https://tdn.totvs.com/pages/releaseview.action?pageId=1056129814)

“Ainda que as deduções legais não sejam utilizadas no cálculo do IRRF em razão da aplicação do desconto simplificado mensal, tais informações permanecem existentes no contexto fiscal do trabalhador e devem ser devidamente declaradas. A própria orientação oficial do eSocial, constante no FAQ 10.39 (atualizado em 17/12/2025), estabelece expressamente que, mesmo quando aplicado o desconto simplificado mensal, é obrigatório o envio dos dados de deduções legais aplicáveis ao trabalhador no evento de pagamento. Assim, a não utilização das deduções no cálculo não afasta a obrigatoriedade de sua informação no evento S-1210.”

## **02. OBJETIVO**

Apresentar o passo a passo para ajustar o campo “Valor de dedução do rendimento tributável”, disponível no anexo de Dependentes do Funcionário, nos casos em que o valor da competência não tenha sido enviado conforme a orientação do eSocial e do Informe de Rendimentos.

Vale reforçar que, atualmente, tanto o **Informe de Rendimentos** quanto o evento **S-1210 do eSocial** utilizam essa informação para considerar os valores de dedução de dependentes.

## **03. PASSO A PASSO**

O preenchimento do campo, conforme a regra mencionada no item 01, passa a ser realizado automaticamente a partir dos patches citados acima.

Dessa forma, será necessário ajustar o campo “Valor de dedução do rendimento tributável” para as competências desde o ano de 2025, conforme exemplo abaixo:

## **Exemplo**

**1 -** Atualize os valores existentes no menu Administração de Pessoal | Funcionário | Anexos | Folha de Pagamento | Dependentes | Anexos | Valor Dedução de Rendimento Tributável

Para isso execute o novo processo **Atualizar Dedução por Dependente** existente no Funcionário.

Mais informações acesse [Atualizar Dedução por Dependente](https://tdn.totvs.com/pages/viewpage.action?pageId=1070067509)

**2 -** Realize a retificação de períodos anteriores acessando o menu eSocial | Outros Processos | Retificação Informações Complementares Períodos Anteriores - S-1210.

Mais informações acesse

> **Nota:** Este menu é responsável por vincular o período que será retificado.

* **Seleção e Edição:** Selecione o funcionário desejado, clique no botão **Editar**  (ícone de lápis) e selecione os meses que serão retificados no eSocial para realizar a declaração dos dados complementares completos.

3 - Gere o XML de retificação do evento **S-1210** da competência **01/2026** dos funcionários selecionados no item 2. O arquivo será criado contendo o grupo `<perAnt>`, permitindo a retificação dos dados complementares do ano anterior.

false⚠️ ATENÇÃO: Mudança na Geração do XML

A partir das versões citadas, a geração do arquivo XML passa a acatar os dados salvos diretamente no seguinte caminho:

> **Administração de Pessoal | Funcionário | Anexos | Folha de Pagamento | Dependentes | Anexos | Valor Dedução de Rendimento Tributável**

Para realizar a atualização dos dados, existem **duas formas** possíveis:

* **Opção 1 (Retificação Retroativa):** Utilizar a retificação no mês de janeiro do ano posterior, conforme citado acima.
* **Opção 2 (Retificação Direta):** Retificar diretamente o evento no próprio mês de sua declaração original.

**4 - Informe de Rendimentos**

Para que os valores de dedução do dependente sejam refletidos no campo **05 - 13º Salário**, linha **13º Salário (Líquido)** do Informe de Rendimentos, basta realizar uma nova geração através do menu: Rotinas Anuais | DIRF / Informe de Rendimentos

Mais informações acesse: 

## **04. DEMAIS INFORMAÇÕES**

* [Consultoria - Envio de dedução de dependentes no S-1210](https://tdn.totvs.com/pages/viewpage.action?pageId=1056129814)
* [Valor Dedução do Rendimento Tributável](https://tdn.totvs.com/pages/releaseview.action?pageId=784779468)
* [Valor Dedução do Rendimento Tributável no Cadastro de Dependentes - Alterações no cálculo para atender ao leiaute S-1.2 que irá substituir a DIRF](https://tdn.totvs.com/pages/releaseview.action?pageId=786553670#tabs-passo3)
* [Processo Atualizar Dedução por Dependente](https://tdn.totvs.com/pages/viewpage.action?pageId=1070067509)
