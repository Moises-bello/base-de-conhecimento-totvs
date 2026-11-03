---
content_hash: 3bec9f95785c5e271e2c23ced3fa3eae53e4b944340800cfbbc05c3d87eca389
fetched_at: '2026-06-29T00:09:35.974948+00:00'
page_id: '425459452'
product: rm
source: tdn-rm
title: Incluir Bolsa Retroativa - Criando lançamentos de devolução / Movimentando
  a Conta Corrente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459452
version: 22
---

---

Este processo fica disponível no menu *Financeiro/Contábil | Assistentes | Incluir / Excluir Bolsa Retroativa*.  
   
A tela do processo é a mesma tanto para *incluir* como para *excluir* Bolsa Retroativa. Se desejar ***'Incluir Bolsa Retroativa'***, selecione o 'Tipo de operação' = **Inclusão**.  
   
Este processo é responsável por incluir bolsas em parcelas cujos lançamentos financeiros já foram gerados ou até mesmo baixados. A inclusão de Bolsas Retroativas irá, conforme parametrização prévia, incluir lançamentos financeiros a pagar para registrar as devoluções correspondentes à cada bolsa incluída retroativamente ou atualizar automaticamente a Conta Corrente dos alunos com os valores das bolsas incluídas retroativamente.  
   
Na primeira etapa do assistente informe o *'Período Letivo'* para o qual as bolsas serão incluídas, em seguida indique o '*RA do aluno'* ou grupo de alunos ou uma sentença SQL, conforme desejar e clique no botão *'Adicionar alunos'*. Ainda nesta etapa, na aba 'Contratos selecionados' confirme os contratos para os quais deseja a **inclusão** da Bolsa Retroativa. Se desejar não atribuir bolsa para algum dos contratos exibidos, remova-o desta lista, selecionando-o e clicando no botão 'Remover'.   
   
Na próxima etapa, indique a *Bolsa* que deseja incluir aos contratos anteriormente selecionados e o *Serviço* para os quais a bolsa será incluída. Indique também a(s) parcela(s) ou uma data como *Período* válido para a bolsa retroativa. Confirme ou indique o *Tipo de desconto* com o percentual ou o valor para o mesmo, lembrando que a alteração desta informação somente será permitida se no cadastro da referida Bolsa for dada a devida permissão. Após estes preenchimentos, clique no botão 'Adicionar'.

Nesta mesma etapa do processo será apresentada a aba 'Valores opcionais' cujas informações serão apresentadas conforme definidas previamente nos parâmetros do sistema (*Ambiente | Configuração | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin – Bolsa Retroativa 2/3*). Mantenha ou altere estas informações conforme desejar.  
   
Se desejar incluir mais alguma Bolsa, informe todos os dados e novamente clique em 'Adicionar'. Para passar para a próxima etapa do processo clique no botão 'Avançar'.

Atenção:

− Caso a opção escolhida previamente nos parâmetros do sistema para se trabalhar com Bolsa Retroativa tenha sido a opção '**Criar devolução de crédito (inclusão de bolsa) / lançamentos a receber (exclusão de bolsa)**', e caso o usuário tenha recebido permissão especial em seu perfil (*Perfil | Anexos | Parâmetros educacionais | <<aba>> Financeiro/Bolsa Retroativa | Alterar parâmetros de comportamento padrão na geração de devoluções*) para permitir alterar o comportamento definido previamente como padrão para a geração de devoluções, neste processo de *'Inclusão de Bolsa Retroativa'* ainda será apresentada mais uma etapa com as opções para o aproveitamento automático dos créditos gerados com a inclusão da Bolsa Retroativa.

− Caso a opção escolhida previamente nos parâmetros do sistema tenha sido a opção **'Utilizar a movimentação em conta corrente'** o processo de *'Inclusão de Bolsa Retroativa'* será finalizado aqui.

− Após todos os passos, ao executar o processo, caso o sistema perceba que o responsável financeiro do aluno é do tipo 'Cliente', uma mensagem é exibida, de forma que para prosseguir, será necessário permitir que o sistema altere o tipo do responsável para 'Ambos'.   
  
No final do processo, será gerado um LOG com informações sobre as bolsas incluídas, lançamentos gerados, créditos e 'Vínculos' atualizados.

**Observações importantes sobre o cálculo dos valores de bolsas:**

As bolsas serão adicionadas no contrato do aluno com o respectivo campo "Ordem" preenchido conforme ordem de inclusão das bolsas no processo.

Quando o sistema está parametrizado com o **"Modo de aplicação de bolsas"** por **"Contrato"**, e o tipo da bolsa no contrato for "Aplicar bolsas em cascata", a ordem de cálculo de valores de bolsas será conforme esse campo "Ordem" da bolsa do contrato.

Quando o sistema está parametrizado com o **"Modo de aplicação de bolsas"** por **"Classificação de Bolsa"**, o campo "Ordem" continuará sendo preenchido conforme ordem de inclusão de bolsas no processo, mas a ordem prioritária a ser seguida para cálculo dos valores de bolsas será a ordem preenchida no cadastro da classificação da bolsa. Quando estivermos trabalhando com classificação de bolsas, será habilitado um campo "i" com uma descrição explicando o funcionamento do cálculo por classificação tanto no processo de inclusão de bolsa retroativa quanto no cadastro da bolsa no contrato do aluno.

1
complete
**Período de competência contábil no processo de inclusão da Bolsa Retroativa**

No processo de Incluir Bolsa Retroativa é possível informar o Período de competência contábil para bolsa, assim ao incluir a bolsa retroativa no contrato essa data já será preenchida.

Caso o período de competência contábil já estiver preenchido no cadastro da**Bolsa | Bolsas por período letivo** essa data virá automaticamente no processo, mas terá também a opção de alterar esse período antes de Adicionar a bolsa.

Criar devolução de crédito (inclusão de bolsa) / lançamentos a receber (exclusão de bolsa)

**1 -** Utilizando a opção **'Criar devolução de crédito (inclusão de bolsa) / lançamentos a receber (exclusão de bolsa)'**:

Utilizando esta opção e caso tenha permissão especial no perfil de usuário, será apresentada mais uma etapa neste processo onde você deverá selecionar a opção que indicará como o sistema irá devolver os créditos que serão gerados pela inclusão da Bolsa. Lembrando mais uma vez que a opção aqui apresenta selecionada foi indicada previamente como default nos parâmetros do sistema e você pode neste momento simplesmente confirmar esta indicação clicando no botão 'Avançar' e finalizar o processo, ou selecionar a opção desejada. A forma de aproveitamento selecionada é armazenada para o crédito gerado e, caso esse crédito seja aproveitado em um outro contrato, o comportamento do aproveitamento será o mesmo.

* Inclusão de bolsas pelo processo de Bolsa Retroativa em parcelas que ***não possuem*** lançamentos financeiros gerados:  
  As bolsas serão incluídas normalmente no contrato do aluno, mas estas ficarão marcadas como bolsa comum e não serão incluídos lançamentos de devolução nem serão gerados créditos. Ao serem gerados os lançamentos financeiros das parcelas deste contrato, estas bolsas serão computadas como desconto normalmente.
* Inclusão de bolsas pelo processo de Bolsa Retroativa em parcelas que ***já possuem*** lançamentos financeiros gerados:  
  Com este processo serão incluídos lançamentos financeiros a pagar para registrar as devoluções correspondentes à cada bolsa incluída em parcela que já possui lançamento financeiro gerado com o valor da respectiva bolsa incluída retroativamente, gerando assim um crédito de bolsa retroativa. E atenção, como será incluído um lançamento a pagar, o responsável financeiro do aluno deve estar classificado como *'Ambos'* e não mais apenas como cliente.  O mês/ano de competência do lançamento de devolução incluído pode ser preenchida conforme parâmetro "".  O aproveitamento do crédito gerado irá variar conforme a opção abaixo escolhida:

**1.1 – Aplicar devolução no lançamento da primeira parcela em aberto**: **1.2 – Dividir devolução pela quantidade de parcelas restantes**: **1.3 – Devolver em espécie:**

Na geração do lançamento a pagar do crédito de bolsa retroativa as instituições que trabalharem com o regime de caixa e que desejarem contabilizar as inclusões dos lançamentos financeiros poderão integrar neste mesmo momento com o sistema contábil, basta parametrizar os sistemas envolvidos. Assim, no momento em que o lançamento financeiro do crédito for gerado, além de haver a sua respectiva inclusão no TOTVS Gestão Financeira, estando parametrizado para tal, haverá também a inclusão no TOTVS Gestão Contábil.   
Para saber mais sobre a contabilização da inclusão do lançamento financeiro, [clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=421388804)

Utilizar a movimentação em conta corrente

**2-** Utilizando a opção **'Utilizar a movimentação em conta corrente'**:

Conforme descrito anteriormente, a última etapa deste processo, onde é possível selecionar a forma de aproveitamento do crédito de devolução não será apresentada quando a opção escolhida previamente nos parâmetros do sistema tiver sido a opção '**Utilizar a movimentação em conta corrente**', pois neste caso as bolsas incluídas retroativamente *não* irão resultar na inclusão de lançamentos de devolução, uma vez que os créditos gerados pela inclusão de Bolsa Retroativa serão lançados diretamente na Conta Corrente dos alunos.  
  
− Inclusão de bolsas pelo processo de Bolsa Retroativa em parcelas que ***não possuem*** lançamentos financeiros gerados:  
As bolsas serão incluídas normalmente no contrato do aluno, mas estas ficarão marcadas como bolsa comum e não serão incluídos créditos na Conta Corrente do aluno. Ao serem gerados os lançamentos financeiros das parcelas deste contrato, estas bolsas serão computadas como desconto normalmente.

− Inclusão de bolsas pelo processo de Bolsa Retroativa em parcelas que ***já possuem*** lançamentos financeiros gerados:  
As bolsas serão incluídas no contrato do aluno e ficarão marcadas como Bolsa Retroativa. Na Conta Corrente do aluno serão incluídos automaticamente os créditos para registrar as devoluções correspondentes às bolsas incluídas retroativamente, neste caso então, **não** serão incluídos lançamentos financeiros para registrar as devoluções.

Caso a bolsa incluída seja do tipo "outro sacado", se for identificado um registro em conta corrente de débito ao aluno referente a parcela, o sistema irá gerar um registro de crédito com o mesmo valor, de modo que, ao ser aproveitado os créditos, esse valor não irá impactar as demais parcelas.

O aproveitamento dos créditos gerados na Conta Corrente do aluno provenientes das inclusões de Bolsa Retroativa serão aproveitados futuramente conforme parametrização específica que deverá ser realizada para a utilização da Conta Corrente. Para obter informações sobre a parametrização e utilização da Conta Corrente dos alunos, .
