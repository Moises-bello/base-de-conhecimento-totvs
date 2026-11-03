---
content_hash: f2c63e18d2fd98c06a3f7331765ed857894dea0fe8b12593061c27a102481c8e
fetched_at: '2026-06-29T00:09:14.756655+00:00'
page_id: '421385248'
product: rm
source: tdn-rm
title: Fórmula para calcular o recurso associado à Composição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385248
version: 1
---

**Fórmula para calcular o recurso associado à Composição**   
Esta funcionalidade se resume em informar uma fórmula para se calcular o Preço Unitário e a Quantidade do recurso, usando como base, índices especificados no Totvs Construção e Projetos e também os recursos que compõem essa composição.   
Para criar, editar ou excluir uma fórmula selecione a Composição, dê dois cliques no Recurso desejado, em seguida na aba Fórmulas do Recurso, agora clique nos botões Incluir, Editar ou Excluir.  
Para a elaboração da Fórmula existem duas maneiras. Na primeira basta definir no Lookup a Variável e o Operador e por fim dar um duplo clique no item desejado da Grid superior para que os dados sejam carregados no editor da fórmula.  
Para a segunda selecione o Operador e em seguida arraste a célula desejada da Grid superior para o editor de elaboração da fórmula.  
Em cada Recurso da Composição, será permitido apenas o cadastro de uma fórmula para Quantidade e uma fórmula para Preço Unitário, e a elaboração de fórmulas utilizando fatores com casas decimais, a separação deverá ser feita por ponto(.). Ex.: 1.3  
Depois de cadastrada a fórmula clique no botão OK, em seguida Salvar e no botão OK novamente. Para obter o valor a ser calculado pela fórmula, basta selecionar a Composição e clicar no botão Cálculo de Composição.  
Na elaboração da fórmula, as variáveis a serem utilizados são:   
Quantidade, Preço Unitário, Preço Parcial, Preço Improdutivo e Valor do Recurso.   
   
**Nos cálculos podemos utilizar os Operadores:**  
+ (Soma);

* (Subtração);

* (Multiplicação);  
  \ (Divisão);  
  ^(Potência);  
  MOD (Retorna o resto da divisão após um número ter sido dividido por um divisor);  
  (...) Parênteses.  
  **Nomenclaturas utilizadas na elaboração da Fórmula:**

* RIL (Recurso Insumo Local);
* RIG (Recurso Insumo Global);
* RCL (Recurso Composição Local);
* RCG (Recurso Composição Global);
* QT (Quantidade);
* PU (Preço Unitário);
* PP (Preço Parcial);
* PI (Preço Improdutivo);
* VR (Valor do Recurso).  
  Funções:  
  Existem funções básicas pré-cadastradas para auxiliar na elaboração das fórmulas, onde cada qual contém uma definição. Para poder visualizar, basta clicar no botão Funções, e a partir daí selecionar a desejada e dar um duplo clique para utilizá-la na fórmula.   
  Seleção de Fórmulas:  
  As Fórmulas cadastradas a partir do Menu Cadastro > Fórmulas estão disponíveis ao clicar sobre o botão Seleção de Fórmulas. Basta selecioná-la para utilização na elaboração das fórmulas do recurso.  
  Verificar Sintaxe:  
  Após a elaboração da fórmula utilizando os recursos citados anteriormente, para verificar se a Sintaxe está correta, basta clicar sobre o botão Verificar Sintaxe para encontrar os possíveis erros.  
  **Exemplo**  
  (QT('RILRG-482') + PU('RIGRG-489') - PP('RILRG-482') - VR('RILRG-484') + PI('RILRG-485') ) \* 1.3  
  A Quantidade do Recurso Insumo Local RG-482, somado ao Preço Unitário do Recurso Insumo Global RG-489, subtraído ao Preço Parcial do Recurso Insumo Local RG-482, subtraído ao Valor do Recurso do Recurso Insumo Local RG-484, somado ao Preço Improdutivo do Recurso Insumo Local RG-485, e multiplicado pelo fator 1.3, será a Quantidade ou o Preço Unitário do recurso, dependendo do Campo que se deseja calcular.
