---
content_hash: b42c7845ab34efb38d332b7315fb3d953075f5c86621d452c059844d640d0f9c
fetched_at: '2026-06-29T00:09:47.718203+00:00'
page_id: '435105052'
product: rm
source: tdn-rm
title: Processo - Cadastrar Tabela de Preços Importando Planilha Excel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105052
version: 75
---

**Processo - Cadastrar Tabela de Preços Importando Planilha Excel**

---

* Nome da Tabela de Preço
* Empreendimento
* Data de Início de Vigência

**Passo 5-** Preencha os campos de mapeamento da planilha Excel que informará os preços das subunidades. Os campos são:

* **Forma Seleção de Arquivo:** Tipo de arquivo da Tabela de Preços que será importada.
* **Arquivo da Planilha:** Planilha Excel que deve ter os dados:
  + Empreendimento
  + Bloco ou Unidade
  + Subunidade
  + Preço Base
  + Preço por M²
* **Célula do Código do Empreendimento:** Célula de valor fixo.
* **Célula do Código da Unidade:** Esta célula pode  conter um valor de célula variável ou fixo.
* **Célula do Código da Subunidade:** Célula de valor variável.
* **Célula  do Preço da Subunidade:** Célula de valor variável.
* **Nome da Planilha:** Célula de valor variável.
* **Célula do Preço Base:** Célula de valor variável.
* \*Célula do Preço por M²: \* Célula de valor variável.
* **Manter configurações para a Próxima Importação:** Se for selecionado, ao executar novamente o processo, os campos acima citados serão carregados com os dados da importação anterior.

* O nova tabela de preço criada terá a situação "em preparação".
* O período de vigência será informado no processo de efetivação da tabela de preço.
* Se o "registro da subunidade no cadastro de empreendimento" não existir no banco de dados, o sistema deverá exibir no log erro informando que a subunidade não foi cadastrada, mas continuar a importar os preços das outras subunidades que existem no banco de dados.
* Caso o "preço da subunidade na planilha" esteja zerado ou negativo, o sistema deverá logar o erro.
* Os preços serão importados independente da situação da subunidade (vendida ou disponível para venda).
* Após a execução do processo de importação, serão criados uma nova tabela de preço com os novos preços das subunidades. (tabelas "XTABPRECO" e "XTABPRECOSUBUNIDADE").
* Após a efetivação da tabela de preços gerada pela execução do processo de importação, será registrado no campo "Memória de cálculo" da tabela "XTABPRECOHISTORICO" o arquivo de origem da planilha Excel e os preços novos das subunidades.

**Alterando uma Tabela de preços através da importação de Planilha Excel**  
Para alterar uma tabela de preço utilizando a importação de planilha Excel basta apenas selecionar uma tabela de preços  com a situação "Em preparação" e executar o processo Importar Preço por Planilha.  
   
   
Voltar
