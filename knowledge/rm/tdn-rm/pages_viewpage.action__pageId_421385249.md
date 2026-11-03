---
content_hash: ec7fb8590fef27166d1539b42b49f099de80c7b6e52768a9d1d17845aed3d5a5
fetched_at: '2026-06-29T00:09:14.760234+00:00'
page_id: '421385249'
product: rm
source: tdn-rm
title: Fórmulas para calcular o valor dos insumos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385249
version: 3
---

---

Esta funcionalidade se resume em criar uma rotina automática para se calcular o preço ativo do insumo atualizando o campo Valor.   
 Para criar, editar ou excluir uma fórmula selecione o Insumo, clique em Anexos, clique no botão Fórmula de Cálculo e na tela de anexos que será exibida, clique nos botões Incluir, Editar ou Excluir.  
 Para a elaboração da Fórmula existem duas maneiras. Na primeira basta definir no Lookup a Variável e o Operador e por fim dar um duplo clique no item desejado da Grid superior para que os dados sejam carregados no editor da fórmula.  
 Para a segunda selecione o Operador e em seguida arraste a célula desejada da Grid superior para o editor de elaboração da fórmula.  
 Em cada Insumo, será permitido apenas um cadastro de fórmula, e a elaboração de fórmulas utilizando fatores com casas decimais, a separação deverá ser feita por ponto(.). Ex.: 1.3  
 Depois de cadastrada a fórmula e Salvar, clique no botão OK e na tela de Insumos selecione o insumo na Grid e clique sobre o botão "Calcular o preço de todos os insumos apresentados". O novo Preço de Insumo Ativo será criado.  
    
 Na elaboração da fórmula, as variáveis a serem utilizados são:   
 Valor, Valor Sem Leis e Valor Improdutivo.   
    
 **Nos cálculos podemos utilizar os Operadores:**

* + (Soma);
* (Subtração);
* (Multiplicação);
* \ (Divisão);
* ^(Potência);
* MOD (Retorna o resto da divisão após um número ter sido dividido por um divisor);
* (...) Parênteses.

**Nomenclaturas utilizadas na elaboração da Fórmula.**

* IL (Insumo Local);
* IG (Insumo Global);
* VL (Valor);
* VSL (Valor Sem Leis);
* VI (Valor Improdutivo).

**Funções:**  
 Existem funções básicas pré-cadastradas para auxiliar na elaboração das fórmulas, onde cada qual contém uma definição. Para poder visualizar, basta clicar no botão Funções, e a partir daí selecionar a desejada e dar um duplo clique para utilizá-la na fórmula.   
  
**Seleção de Fórmulas:**  
 As Fórmulas cadastradas a partir do Menu Cadastro > Fórmulas estão disponíveis ao clicar sobre o botão Seleção de Fórmulas. Basta selecioná-la para utilização na elaboração das fórmulas do recurso.  
  
**Verificar Sintaxe:**  
 Após a elaboração da fórmula utilizando os recursos citados anteriormente, para verificar se a Sintaxe está correta, basta clicar sobre o botão Verificar Sintaxe para encontrar os possíveis erros.

**Exemplo:**  
 (VL( 'IL039.0015' ) + VL ( 'IG02' ) – VSL( 'IL039.0015' ) ) \* 1.3

O Valor do Insumo Local 039.0015, somado ao Valor do Insumo Global 02, subtraído ao Valor Sem Leis do Insumo Local 039.0015 e multiplicado pelo fator 1.3 definido pelo usuário será o Valor do Preço Ativo do Insumo.
