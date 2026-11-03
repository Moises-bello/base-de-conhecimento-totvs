---
content_hash: 5841eec86b87203e46aeea710f8ed4205c46e0ec6f8b187a889832fc227c2258
fetched_at: '2026-06-29T00:09:32.367918+00:00'
page_id: '425458834'
product: rm
source: tdn-rm
title: Cálculo do valor de Bolsa x Contabilização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458834
version: 52
---

Quando o contrato do aluno possuir **bolsas** aplicadas às parcelas, o valor das bolsas contabilizadas do contrato será registrado na tabela SCONTRATO, no campo VALORBOLSA. Se ocorrer um aumento ou redução desse valor em algum momento, ao realizar uma nova contabilização, o campo VALORBOLSA será atualizado refletindo o novo valor.

Quando houver estorno total da contabilização, o valor desse campo será atualizado para zero.

Período de Competência Contábil definida no Contrato

Quando o contrato do aluno possuir **bolsas** aplicadas às parcelas, o valor da contabilização mensal da bolsa pode não corresponder ao valor financeiro aplicado em determinada parcela do contrato, pois o valor da Bolsa contabilizado em cada competência contábil é resultante da distribuição uniforme do valor total da Bolsa aplicada no contrato dividido pelo número de competências contábeis. Veja o exemplo abaixo:

**1º Passo:**O sistema fará o cálculo dos valores *individuais* das Bolsas, tomando como base o valor financeiro da Bolsa aplicada nas parcelas do contrato

Competência - Mês/Ano Inicial: 01/2015 - Mês/Ano Final  : 12/2015  
Data do Contrato: 03/03/2015  
Valor total dos serviços do contrato a ser contabilizado: 12.000,00  
O contrato possui 10 parcelas financeiras de 1.200,00 cada (12.000,00 / 10 parcelas)  
Bolsa de 50% aplicada somente na 1ª. parcela do contrato = **600,00**  (1.200,00 \* 50%)  
Bolsa de 80% aplicada somente na 5ª. parcela do contrato = **960,00**  (1.200,00 \* 80%)

**2º Passo:**O sistema fará o cálculo do valor *total* de Bolsas aplicadas no contrato:

Bolsa de 50% (600,00) + Bolsa de 80% (960,00) = **1.560,00**

**3º. Passo:**  
O sistema fará o cálculo do valor da Bolsa para ser contabilizado em cada *competência* contábil:

Neste exemplo, o valor total das Bolsas 1.560,00 será dividido e contabilizado em 10 meses (mês da Data do contrato até o Mês/Ano Final da competência | mês 03 até mês 12 = 10 meses), sendo que em cada competência contábil o valor a ser contabilizado referente à Bolsa será de **156,00** (1.560,00 / 10 meses).

A contabilização de bolsas ocorrerá de forma análoga à contabilização dos serviços, onde é possível definir no evento contábil um item de evento com contas específicas para receber a contabilização dos seus valores ou ainda definir um item de evento que busque as contas contábeis diretamente do cadastro de cada bolsa, através do *Default Contábil* de cada bolsa.

No **primeiro** modelo de contabilização, se os eventos contábeis determinarem a contabilização das bolsas, *todas* as bolsas presentes nos contratos dos alunos serão computadas e consideradas na contabilização do contrato e na apropriação mensal.

Já no **segundo** modelo de contabilização, se os eventos contábeis determinarem a contabilização das bolsas, *somente* as bolsas que tiverem a opção *"Compõe contabilização por competência"* *marcada* em seus cadastros serão consideradas na contabilização do contrato e na apropriação mensal. Portanto, certifiquem-se sobre esta opção presente no cadastro da bolsa!

Conforme o exemplo acima, se o evento contábil de 'Contrato' possuir um item de evento parametrizado para contabilizar Bolsas, será incluído um lançamento no valor total da bolsa (**1.560,00**) e, à medida que os serviços forem sendo realizados, e se o evento contábil indicado para contabilização 'Mensal' também possuir um item de evento parametrizado para contabilizar Bolsas, será incluído, mês a mês, e até o final da prestação dos serviços previstos no contrato, o lançamento apropriando-se a efetiva realização mensal do valor concedido pelas bolsas (**156,00**).

**Observações:**- **Bolsas Condicionais** são aquelas cuja opção *'Bolsa incondicional'*, presente no próprio cadastro da bolsa estiver *desmarcada,* indicando assim, que dependem de determinadas condições para serem atribuídas financeiramente. - -Estas bolsas, mesmo presentes nos contratos dos alunos, ***não*** serão computadas e contabilizadas pelo regime de competência.  
- No **segundo** modelo de contabilização, *somente* as bolsas que tiverem a opção *"Compõe contabilização por competência "**marcada* em seus cadastros serão consideradas na contabilização do contrato e na apropriação mensal  
- A contabilização dos valores de ***Descontos*** concedidos nos contratos se dará de forma análoga à contabilização das Bolsas.  
- Os valores de serviços, bolsas e/ou descontos serão registrados na contabilização conforme a parametrização realizada nos eventos contábeis utilizados para tal. Valores originais utilizarão sempre os eventos contábeis destinadas à contabilização do 'Contrato' e à contabilização 'Mensal' (válido para os dois modelos de contabilização). Caso utilizem o ***primeiro*** modelo de contabilização, as alterações ocorridas em qualquer um destes valores serão registradas sempre utilizando-se estes mesmos eventos contábeis (evento para 'Contrato' e evento 'Mensal'), mas caso utilizem o ***segundo*** modelo de contabilização as alterações ocorridas em qualquer um destes valores serão registradas sempre utilizando-se os respectivos eventos contábeis destinados à contabilização de 'Cancelamento' e de 'Aumento'.

Período de Competência Contábil definida na Bolsa

Para algumas Instituições de Ensino a bolsa poderá ser concedida para o aluno em um mês especifico, ou seja, não é uma bolsa que é aplicada em todas as parcelas do contrato, neste caso entendemos que para a contabilização a bolsa pode ter uma competência diferente da competência contábil do contrato.

Quando o usuário do TOTVS Educacional entender que este cenário deve ser aplicado, a competência da bolsa deverá ser definida no contrato no anexo do cadastro da bolsa do aluno na aba "Contabilização".

O processo de contabilização por competência irá contabilizar as bolsa respeitando as competências definidas no cadastro da bolsa do alunos, caso a competência não esteja preenchida, a contabilização da bolsa continuará respeitando a competência do contrato.

**Importante:**

Quando o processo de contabilização identificar uma bolsa com competência diferenciada, esta informação  será armazenada na tabela SCONTRATOBOLSACONTCOMPETENCIA e serão também discriminadas no log de contabilização através da coluna da memória de cálculo.

É possível definir uma competência contábil default no cadastro da bolsa, neste caso quando a bolsa for incluída no contrato de qualquer aluno a competência contábil já será carregada automaticamente, podendo o usuário alterar caso seja necessário.

Para maiores informações consulte [Bolsa por Período Letivo](https://tdn.totvs.com/display/LRM/Bolsa+por+Periodo+Letivo) / [Bolsa do Contrato](https://tdn.totvs.com/display/public/LRM/Bolsa+do+contrato)

Este recurso estará disponível a partir da versão 12.1.27 com a contabilização revitalizada e para habilitar é necessário executar o RM Atualizador (execução dos novos script) disponível no patch da versão.

Detalhamos alguns exemplos como será o novo comportamento com o período de competência contábil informado na bolsa:

**[Exemplo 1 - Contrato com bolsas com competências definidas](https://tdn.totvs.com/pages/viewpage.action?pageId=576599918)**

**[Exemplo 2 - Contrato com uma bolsa com competência definida e a outra busca a competência do contrato](https://tdn.totvs.com/pages/viewpage.action?pageId=576599977)**

**[Exemplo 3 - Contrato contabilizado com aumento de bolsa](https://tdn.totvs.com/pages/viewpage.action?pageId=576600034)**

**[Exemplo 4 - Cancelamento de Contrato com bolsa por competência já apropriada](https://tdn.totvs.com/pages/viewpage.action?pageId=577896466)**

**[Exemplo 5 - Cancelamento de Contrato com bolsa por competência não apropriada](https://tdn.totvs.com/pages/viewpage.action?pageId=577923148)**

Regras

* Não será permitido na primeira contabilização do diferimento mensal ter uma **bolsa X** sem o período de competência e no mesmo contrato possuir a mesma **bolsa X** com um período de competência preenchido.
* Não será permitido na primeira contabilização do diferimento mensal uma **bolsa X** com período de competência que não esteja entre a competência contábil identificada para o processamento da contabilização do contrato.  
  A competência da bolsa deverá respeitar o período de competência informado no contrato / período letivo / parametrização por curso
* Se o contrato já possui apropriação mensal não será possível modificar:   
  - O período da competência no cadastro da bolsa do contrato  
  - A quantidade de parcelas ou período (data) na bolsa do contrato  
  Caso a alteração seja em função de ajustes que tenham como consequência o aumento na quantidade de parcelas ou período de bolsa, é recomendado que seja adicionado um novo registro para a bolsa com uma nova competência ou que seja executado o estorno da contabilização do contrato.

 Informações Complementares

---
