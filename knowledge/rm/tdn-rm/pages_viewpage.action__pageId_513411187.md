---
content_hash: 620daae06f27e222c5d6db4b8e24072bcec430bb30f8334d9a917587a0673b02
fetched_at: '2026-06-29T00:10:26.132061+00:00'
page_id: '513411187'
product: rm
source: tdn-rm
title: Cadastro Métodos e Parâmetros de Exames
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=513411187
version: 8
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**

sumarioVisão Geral

## **01. VISÃO GERAL**

Nesta pasta você define qual será o Método de um respectivo Exame e seus parâmetros específicos, que deverão se aplicar a todos os Exames que utilizem o Método: **Imprime Método, Imprime Referências** e **Método Ativo.**  
Ao incluir um Método para um exame, primeiro será necessário Pesquisar um exame, e depois incluir um Método para o Exame pesquisado, selecionando-o no campo **Método.**  
Seq. Método  
Número para identificar o Método.  
Método:  
Selecione o Método do exame.  
Neste campo são exibidos todos os Métodos cadastrados na função Métodos de Exame

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Relatório de Laudo  
Neste campo você poderá informar qual o relatório do Gerador de Relatórios será utilizado na Emissão de Resultados / Laudos de Exames.  
O relatório a ser utilizado deverá ter no mínimo os seguintes parâmetros: **NUMEROPEDIDO, CODEXAME, SEQEXAME, CODMETODO e ORDEMSERVICO.**  
   
Imprime Método  
Este parâmetro marcado indica que o Método será impresso no Resultado do Exame.  
   
Imprime Referências  
Este parâmetro marcado indica que os Valores de Referência utilizados no Método serão impressos no Resultado do Exame.  
   
Método Ativo  
Este parâmetro marcado indica que o Método está ativo.  
Métodos que não estejam ativos não serão exibidos no momento da associação do Método a um determinado Exame.  
   
Rodapé  
Neste campo você poderá inserir um texto que será exibido no Resultado do Exame.

No TOTVS Gestão Hospitalar acesse o menu **Cadastros> Unidades de Diagnóstico> Métodos e Parâmetros de Exames.**

2. Clique em **Incluir** (página em branco).

3. Na aba Identificação, selecione o Exame e o Método, defina se o **Método** será impresso no resultado do exame e se os valores de **Referência** serão impressos no resultado do exame, marque a caixa **Ativo**.

Preenchido todos os campos, clique em **Salvar**.

4. Clique na guia **Parâmetros,** clique em **Incluir**.

5. Preencha as informações dos parâmetros de exame e clique em **Salvar>** **OK**.

* Descrição do Parâmetro (o que ele faz);
* Selecione a Unidade de Medida;
* Marque a caixa "Utiliza texto para resultado?" caso desejado;
* Selecione o Percentual Parâmetro;
* Insira as Casas decimais;
* Insira o Resultado Padrão;
* Expressão para cálculo do parâmetro;
* Marque os checkbox: Subtítulo, Espaço e Comentário se desejar.

6. Clique na guia **Dados de Referência** e em **Incluir**.

Preencha de acordo com o filtro desejado:

7. Este dado será utilizado ao realizar um cadastro de **Exames e Serviços.**

8. Na aba **Execução Externa,** preencha o campo **Método** com Método e Parâmetro de Exame anteriormente cadastrado.
