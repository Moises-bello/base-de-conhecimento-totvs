---
content_hash: 52b80e6ca836a2a05d4c2c0b8874f6e4457818ef820eb5e3b357726a4070922c
fetched_at: '2026-06-29T00:09:36.065463+00:00'
page_id: '425459464'
product: rm
source: tdn-rm
title: Excluir Bolsa Retroativa - Criando lançamentos de devolução / Movimentando
  a Conta Corrente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459464
version: 15
---

---

Este processo fica disponível no menu *Financeiro/Contábil | Assistentes | Incluir / Excluir Bolsa Retroativa*.

A tela do processo é a mesma tanto para *incluir* como para *excluir* Bolsa Retroativa. Se desejar ***'Excluir Bolsa Retroativa'***, selecione o 'Tipo de operação' = **Exclusão**.

Este processo é responsável por cobrar os valores de bolsas anteriormente concedidas em parcelas com lançamentos financeiros gerados sem a necessidade de regeração dos mesmos. A exclusão de Bolsas Retroativas irá, conforme parametrização prévia, incluir novas parcelas no contrato do aluno afim de se cobrar os benefícios que estiverem sendo excluídos ou atualizar automaticamente a Conta Corrente dos alunos com estes valores.  
   
**Importante:**  
Caso tenha sido feita a inclusão de Bolsa Retroativa indevidamente e caso o crédito gerado pela inclusão da bolsa ainda não tenha sido aproveitado em nenhum lançamento ou caso o crédito já tenha sido aproveitado em outros lançamentos através da inclusão de 'Vínculos' mas estes lançamentos ainda estiverem com status 'Em aberto' ou 'Cancelado', o processo indicado para ser executado é o  para que assim o contrato volte ao estado original  sem necessidade de criação de parcelas.  
   
Na primeira etapa do assistente informe o *'Período Letivo'* para o qual as bolsas serão excluídas, em seguida indique o '*RA do aluno'* ou grupo de alunos ou uma sentença SQL, conforme desejar e clique no botão *'Adicionar alunos'*. Você pode preencher um 'Motivo da exclusão', o motivo aqui informado será preenchido no cadastro da bolsa que será inativada no contrato do aluno. Ainda nesta etapa, na aba 'Contratos selecionados' confirme os contratos para os quais deseja a **exclusão** da Bolsa Retroativa. Se desejar remover algum contrato da lista apresentada, selecione-o e clique no botão 'Remover'.   
   
Na próxima etapa, indique a *Bolsa* que deseja excluir dos contratos anteriormente selecionados e o *Serviço* para os quais a bolsa será excluída. Indique também a(s) parcela(s) ou uma data como *Período* válido para a exclusão da bolsa. Após estes preenchimentos, clique no botão 'Adicionar'.  
   
A exclusão da bolsa pode ser *total* ou *parcial*:

  - Exclusão **total**: é quando a bolsa é excluída de todas as parcelas do contrato ou de todo o período em que estava inicialmente aplicada no contrato.

  - Exclusão **parcial**: é quando a bolsa é excluída somente de algumas parcelas do contrato ou alguma parte do período em que estava inicialmente aplicada no contrato.

 Se desejar excluir mais alguma bolsa, informe todos os dados e novamente clique em 'Adicionar'. Para passar para a próxima etapa do processo clique no botão 'Avançar'.

Atenção:

  - Caso a opção escolhida previamente nos parâmetros do sistema para se trabalhar com Bolsa Retroativa tenha sido a opção '**Criar devolução de crédito (inclusão de bolsa) / lançamentos a receber (exclusão de bolsa)**', e caso o usuário tenha recebido permissão especial em seu perfil (*Perfil | Anexos | Parâmetros educacionais | <<aba>> Financeiro/Bolsa Retroativa | Alterar parâmetros de comportamento padrão na geração de devoluções*) para permitir alterar o comportamento definido previamente como padrão para a geração de cobrança, neste processo de *'Exclusão de Bolsa Retroativa'* ainda será apresentada mais uma etapa com as opções para cobrança do crédito devolvido gerados com a exclusão da Bolsa Retroativa com as opções:  
  - Gerar uma única parcela para pagamento,  
  - Dividir pela quantidade de parcelas restantes

  - Caso a opção escolhida previamente nos parâmetros do sistema tenha sido a opção **'Utilizar a movimentação em conta corrente'** o processo de *'Exclusão de Bolsa Retroativa'* somente possuirá as etapas descritas anteriormente, sendo finalizado aqui.

Quando a bolsa for do tipo "**Outro sacado**", após a execução do processo de exclusão, os lançamentos referentes ao outro sacado serão cancelados, o valor do débito a ser pago, será incluído em um registro de conta corrente ou será gerado lançamento de devolução, conforme parametrização feita anteriormente: "Criar devolução de crédito (inclusão de bolsa) / lançamentos a receber (exclusão de bolsa)" ou "Utilizar a movimentação em conta corrente".

No final do processo, será gerado um LOG com informações sobre as bolsas excluídas, parcelas e lançamentos gerados, débitos e 'Vínculos' atualizados.

Criar devolução de crédito (inclusão de bolsa) / lançamentos a receber (exclusão de bolsa)

1 - Utilizando a opção **'Criar devolução de crédito (inclusão de bolsa) / lançamentos a receber (exclusão de bolsa)'**:

Utilizando esta opção e caso tenha permissão especial no perfil de usuário, será apresentada mais uma etapa neste processo onde você deverá selecionar a opção que indicará como o sistema irá cobrar os valores dos créditos devolvidos gerados pela exclusão da Bolsa. Lembrando mais uma vez que a opção aqui selecionada foi indicada previamente como default nos parâmetros do sistema e você pode neste momento simplesmente confirmar esta indicação clicando no botão 'Avançar' e finalizar o processo, ou selecionar a opção desejada.

1.1- Exclusão de bolsas pelo processo de Bolsa Retroativa em parcelas que ***não possuem*** lançamentos financeiros gerados:

Como a bolsa que está sendo excluída ainda não foi utilizada efetivamente em lançamentos financeiros no contrato, não será incluída nenhuma parcela para cobrança no contrato do aluno e:  
  - Se a exclusão da bolsa foi ***total***, a bolsa em questão permanecerá no contrato do aluno mas será *inativada*, e neste caso, todos os campos do cadastro desta bolsa no contrato ficarão bloqueados para edição.  
  - Se a exclusão da bolsa foi ***parcial***, a bolsa terá a sua validade alterada para o período ou parcelas para as quais permanecerá ainda vinculadas. Se a exclusão parcial for no meio da validade da bolsa, o registro atual da bolsa no contrato conterá a validade até a parcela anterior à exclusão e será gerado um outro registro de bolsa no contrato do aluno fazendo referência à bolsa de origem com a validade inicial a partir da parcela posterior à exclusão até a parcela final que estava indicada anteriormente.

1.2- Exclusão de bolsas pelo processo de Bolsa Retroativa em parcelas que ***já possuem*** lançamentos financeiros gerados:

A exclusão de bolsa retroativa aplicada em parcela que já possui lançamento gerado irá resultar na inclusão de novas parcelas nos contratos dos alunos para gerar as cobranças referentes aos valores anteriormente não cobrados. Como a origem destas parcelas será 'Bolsa retroativa', estas não poderão ser editadas ou excluídas manualmente. A cobrança destes débitos irá variar conforme a opção abaixo escolhida:

**1 - Gerar uma única parcela para o pagamento:**   - Se a exclusão da bolsa foi ***total***, a bolsa em questão permanecerá no contrato do aluno mas será inativada, e neste caso, todos os campos do cadastro desta bolsa no contrato ficarão bloqueados para edição.  
   - Se a exclusão da bolsa foi ***parcial***, a bolsa terá sua validade alterada para o período ou parcelas para as quais permanecerá ainda vinculadas. Na Conta Corrente do aluno serão incluídos registros de débitos correspondentes à parte da bolsa que foi removida.  
  
  
  
**2 - Dividir pela quantidade de parcelas restantes:**Se o contrato não possuir mais parcelas ainda não geradas, será incluída no contrato do aluno uma única parcela com o valor total da bolsa que foi excluída e, neste caso, a Data de vencimento obedecerá às informações também parametrizadas previamente e:  
   - Se a exclusão da bolsa foi ***total***, a bolsa em questão permanecerá no contrato do aluno mas será inativada, e neste caso, todos os campos do cadastro desta bolsa no contrato ficarão bloqueados para edição.  
   - Se a exclusão da bolsa foi ***parcial***, a bolsa terá sua validade alterada para o período ou parcelas para as quais permanecerá ainda vinculadas. Na Conta Corrente do aluno serão incluídos registros de débitos correspondentes à parte da bolsa que foi removida.

Na geração do lançamento a receber da exclusão da bolsa retroativa as instituições que trabalharem com o regime de caixa e que desejarem contabilizar as inclusões dos lançamentos financeiros poderão integrar neste mesmo momento com o sistema contábil, basta parametrizar os sistemas envolvidos. Assim, no momento em que o lançamento financeiro da parcela for gerado, além de haver a sua respectiva inclusão no TOTVS Gestão Financeira, estando parametrizado para tal, haverá também a inclusão no TOTVS Gestão Contábil.   
Para saber mais sobre a contabilização da inclusão do lançamento financeiro, [clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=421388804)

Quando o parâmetro **Dividir pela quantidade de parcelas restantes**, orientamos a não parametrizar o evento para Aplicar e Bolsa, pois o valor contabilizado será o valor total da bolsa em todas as parcelas geradas pela exclusão, orientamos então a utilizar o evento para Aplicar em Lançamento e buscar o Valor Original do lançamento.

Utilizar a movimentação em conta corrente

2 - Utilizando a opção **'Utilizar a movimentação em conta corrente'**:

Conforme descrito anteriormente, a última etapa deste processo, onde é possível selecionar a forma de cobrança dos débitos não será apresentada quando a opção escolhida previamente nos parâmetros do sistema tiver sido a opção '**Utilizar a movimentação em conta corrente**', pois neste caso as bolsas excluídas retroativamente *não* irão resultar na inclusão de lançamentos de cobrança, uma vez que os débitos gerados pela exclusão de Bolsa Retroativa serão lançados diretamente na Conta Corrente dos alunos.

2.1- Exclusão de bolsas pelo processo de Bolsa Retroativa em parcelas que ***não possuem*** lançamentos financeiros gerados:

Como a bolsa que está sendo excluída ainda não foi utilizada efetivamente em lançamentos financeiros no contrato, não será então incluído nenhum registro na Conta Corrente do aluno e:  
  - Se a exclusão da bolsa foi ***total***, a bolsa em questão permanecerá no contrato do aluno mas será *inativada*, e neste caso, todos os campos do cadastro desta bolsa no contrato ficarão bloqueados para edição. (mas poderá ser excluída!!!!)  
  - Se a exclusão da bolsa foi ***parcial***, a bolsa terá a sua validade alterada para o período ou parcelas para as quais permanecerá ainda vinculadas. Se a exclusão parcial for no meio da validade da bolsa, o registro atual da bolsa no contrato conterá a validade até a parcela anterior à exclusão e será gerado um outro registro de bolsa no contrato do aluno fazendo referência à bolsa de origem com a validade inicial a partir da parcela posterior à exclusão até a parcela final que estava indicada anteriormente.  
  
  
  
2.2- Exclusão de bolsas pelo processo de Bolsa Retroativa em parcelas que ***já possuem*** lançamentos financeiros gerados:

Neste caso, como as bolsas já foram utilizadas nos lançamentos financeiros das parcelas, serão incluídos na Conta Corrente do aluno registros de débitos correspondentes ao valor de cada bolsa removida, ficando assim registrado o valor não cobrado e:  
  - Se a exclusão da bolsa foi ***total***, a bolsa em questão permanecerá no contrato do aluno mas será *inativada*, e neste caso, todos os campos do cadastro desta bolsa no contrato ficarão bloqueados para edição.  
  - Se a exclusão da bolsa foi ***parcial***, a bolsa terá a sua validade alterada para o período ou parcelas para as quais permanecerá ainda vinculadas. Na Conta Corrente do aluno serão incluídos registros de débitos correspondentes à parte da bolsa que foi removida.

Atenção:

  - O aproveitamento dos débitos gerados na Conta Corrente do aluno provenientes das exclusões de Bolsa Retroativa serão aproveitados futuramente conforme parametrização específica que deverá ser realizada para a utilização da Conta Corrente. Para obter informações sobre a parametrização e utilização da Conta Corrente dos alunos, .  
  - Se a bolsa que estiver sendo excluída retroativamente for uma bolsa de crédito, além de atualizar a Conta Corrente do aluno com o valor da bolsa removida, o lançamento financeiro referente ao crédito do outro sacado será cancelado.  
  - Não será permitida a exclusão de bolsa de crédito que possuir Repasses cadastrados.  
  - Não será permitida a exclusão de bolsas em contratos 'Cancelados'.

 Informações Complementares

---

[Contabilização de Cancelamento/Exclusão de Bolsa](https://tdn.totvs.com/pages/viewpage.action?pageId=787844231)
