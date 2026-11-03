---
content_hash: 39b6ba12e766fed856e9006c087d823d6f34671e981c6824e744d67b3005566f
fetched_at: '2026-06-29T00:11:37.980689+00:00'
page_id: '780787693'
product: rm
source: tdn-rm
title: TCGI - Visão da Cobrança
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=780787693
version: 5
---

**Cobrança| Visão de Cobrança**

A Visão de cobrança apresenta as cobranças existentes para cada cliente/fornecedor, é possível visualizar informações simplificadas da cobrança(Data de Abertura, Contrato, Origem da Cobrança e etc). Essa visão também contempla o Anexo Lançamentos da Cobrança, que apresenta informações do lançamento(s) que está associado a cobrança, além de possuir uma opção para visualizar as ações de cobrança que foram aplicadas no(s) lançamento(s) e Log para acompanhar todo o histórico no lançamento nesta cobrança.

##### Menu Processos

* **Gerar Cobrança**: Será possível executar a geração de cobrança diretamente da visão de Cobrança.
* **Alteração da Carteira de Cobrança**: Será possível alterar a carteira de uma ou varias cobranças, será necessário selecionar a(s) cobrança(s) e executar a rotina informando a nova carteira.
* **Gerar Ação Manual de Cobrança:**  Será possível manualmente executar as ações de cobrança que já estão cadastradas. É necessário selecionar uma ou mais cobranças e executar a rotina informando qual será a ação aplicada.

Tela de Cobrança

Para visualizar os dados consolidados de um cobrança é necessário abrir uma cobrança na visão de cobrança, posicione o cursor do mouse sobre a cobrança que deseja visualizar e de um duplo click, após essa ação será feito a abertura da tela de cobrança.

A tela de cobrança irá apresentar de forma organizada todas as informações da cobrança, como dados do cliente, informações do contrato(Venda e Aluguel), lançamentos que pertencem a cobrança.

**Identificação:**

* **Dados do Cliente**: Será apresentado informações para contato do cliente em forma de hiperlink, que possibilita um rápido acesso ao cadastro do cliente.
* **Dados do Contrato**: Apresentado informações básicas do contrato(Venda ou Aluguel), e com acesso rápido para o contrato de venda/aluguel ou empreendimento/imóvel através de hiperlink.
* **Lançamentos em Atraso**:  
  ♦ ***Lançamentos***: Apresenta todos os lançamentos que compõem a cobrança. Foi incluído no menu Processos a opção **Inclusão de Borderô de Negativação**, com isso é possível selecionar o lançamento(s) e incluir diretamente ao Borderô para negativação.

  Importante:

  + A opção Inclusão de Borderô de Negativação ficará disponível apenas na edição da Cobrança/Atendimento.
  + Link com maiores informações do processo: [Negativação / Cobranca Terceirizada](https://tdn.totvs.com/pages/viewpage.action?pageId=553906289)
  + Para contratos de Aluguel será possível visualizar as garantias através do menu Anexos>>Garantias.

  ♦ **Valores**: Ao selecionar os lançamentos e utilizar a opção Calcular será retornado o valor liquido do lançamento considerando a Data do Liquido informado, os lançamentos ficam desabilitados até que seja utilizado a opção 'Limpar'.  
  ♦ ***Boleto***: Após calcular o valor, será possível incluir o [boleto](https://tdn.totvs.com/display/LRM/FIN+-+Boleto)para os lançamentos que foram selecionados.  Se a cobrança for para outra coligada diferente da selecionada, a conta/caixa a ser exibida será a da coligada da cobrança.

**Atendimento:**

O menu de atendimentos estará disponível apenas ao acessar a tela de cobrança através da visão de atendimentos, com isso o atendente irá visualizar apenas os atendimentos que é responsável.

**Historio de Cobrança:**

Ao se gerar uma Ação Manual de Cobrança , a mesma ficará guardada no **Histórico de cobrança** .

Esta visão apresenta o histórico de todas as ações de cobrança executadas, inclusive com a opção para mostrar estas informações por título financeiro.

          Anexos | Histórico de Cobrança

**Histórico****Financeiro:**

Retorna todo o histórico financeiro do cliente/financeiro que está vinculado a cobrança. Ao acessar a visão, é exibido na tela do cockpit um resumo de informações referentes à:

* Cadastro do cliente/fornecedor
* Saldo devedor Atual
* Gráfico de quitação do contrato
* Solicitações de atendimento
* Últimos Vencimentos
* Quantidade de contratos
* Quantidade de parcelas atrasadas
* As vendas do cliente

Nesta tela é informado quantos contratos tem o Cliente e caso queira ver todos os contratos , basta clicar em Contrato ( 3 ).

**Cliente/Fornecedor:**

* **Cliente/Fornecedo**r: Apresenta o cliente/fornecedor da cobrança, sendo possível atualizar o seu cadastro.

**Fiadores/Outros Clientes:**Nesta visão serão apresentados os fiadores que estiverem associados aos contratos de vendas/locação. Para contratos que possuem mais de um comprador/locatário ativos, esses também serão apresentados nesta tela.

Os registros desta tela serão apresentados em forma de Card, ao dar um duplo clic será aberto o cadastro do cliente/fornecedor associado ao mesmo.

Somente fiadores associados a um cliente/fornecedor serão apresentados nesta tela.

**Contratos de Venda/Locação:**

* **Contrato**: Apresenta o contrato da cobrança.

Tela da Visão de Cobrança:

Selecionar a cobrança e editar.

Principal tela na qual os Analistas de atendimento irão trabalhar.

**Sobre informações do Cliente.**

**Nome do cliente : encontra-se em azul o nome , pois ao clicar sobre o nome já vai direto para tela de Cliente / Forncedor ou cilcar em Cliente / Fornecedor da aba Esquerda da tela.**

**Celular : Caso cliente tenha por exemplo Skype e servidor configurado já irá fazer a integração com o número do cliente.**

**E-mail : Se estiver configurado , já abrirá automaticamente por exemplo ou Outlook.**

**Sobre Informações do Cobrança.**

**Informa o Lançamento mais antigo vencido**

**Sobre Informações sobre Lançamentos.**

**Informa lançamentos em atraso no contrato.**

**Sobre informações do Contrato.**

**Contrato : Pode entrar direto no contrato do cliente ao clicar no número na cor azul , ou do lado esquerdo da tela em Contrato | Contratos de Vendas**

**Empreendimento: Entra no cadastro do Empreendimento**

**Sobre Informações de Acordo.**

Exemplo desta opção : Cliente tem 7 parcelas em atraso , esta querendo quitar todas parcelas , neste caso o usuário seleciona todas parcelas acima e em seguida , basta clicar em Calcular.

Imediatamente são bloqueados os lançamentos - Cliente pode voltar atrás antes de GERAR BOLETO e por exemplo , querer pagar apenas 4 parcelas e não mais as 7 Parcelas .. Neste exemplo , basta clicar em LIMPAR como na imagem.

Gerando boleto para 4 parcelas - Abre o processo para geração de Boletos.

Ou o cliente pode fazer um Acordo.

Neste caso , selecionar as parcelas que deseja efetuar o Acordo - Em seguida , Calcular e ( Fazer Acordo ).

Que momento devo gerar um Acordo ou Aditivo ?

**Acordo:** cliente deve por exemplo , 4 Parcelas como mostra o Print acima e quer pagar em 2 boletos, Neste caso pode ser utilizado o Acordo, caso não queira incluir CM e nem Juros novamente.

**Ao selecionar o Aditivo :**  Utilizado caso queira incluir IGPM - INCC por exemplo .  Se quer incluir qualquer índice de contrato IGPM ou Juros Price novamente para calucular , o cliente obrigatóriamente tem que entrar em ADITIVO e fazer a negociação normal por ele como é mostrado no Print abaixo:

Clicar em Aditivo e em seguida : Novo.

Mais sobre ACORDO FINANCEIRO : [CLIQUE AQUI !](https://tdn.totvs.com/display/LRM/FIN+-+Acordo)

**Parametro para utilzar Acordo no TCGI**

Verificar os Parâmetros Financeiro do TCGI - Vincular o código do Componente para ser gerado o Acordo ( Lembrando que tem que ser somente Principal )

Exemplo do Componente.

Exemplo de Tipo de Parcela.

Exclusão de Cobrança

Exclusão da Cobrança.

Foi implementado no TCGI a opção de se ***excluir uma cobrança*** . Para solucionar uma situação em que o usuário pode ter ocasionado um erro de lançamento. Por exemplo, pode ter ocorrido uma duplicação de cobrança devido a uma falha no sistema ou um erro humano durante o processo de entrada de dados. Corrigir esses erros é crucial para manter a precisão dos registros financeiros da incorporadora e garantir a transparência com os clientes. Além disso, manter registros precisos é essencial para evitar litígios futuros e manter a confiança dos clientes na empresa. Portanto, ao identificar um erro de cobrança, é importante agir prontamente para corrigi-lo e excluir a cobrança incorreta do sistema.

Para se utilizar a opçao de Exclusão de cobrança , é preciso habilitar o perfil do usuário específico na qual irá utilizar esta funcionalidade , pois ao se excluir uma cobrança , todo histórico é perdido também.
