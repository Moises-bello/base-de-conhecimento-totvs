---
content_hash: a27ed69f3734e503343d3cdb936eb9c15267981085f329d6c3903051eaaef4c9
fetched_at: '2026-06-29T00:09:53.638789+00:00'
page_id: '440846260'
product: rm
source: tdn-rm
title: FIN - Novidades da versão 12.1.14
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=440846260
version: 5
---

**12.1.14 -** [**Verificar Impactos Novo Boleto Registrado**](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388664)**.**  
Para esta versão é obrigatório executar o processo Verificar Impactos Novo Boleto Registrado. Este processo irá exibir em formato de LOG as alterações que deverão ser realizadas no sistema, motivadas pela nova regra FEBRABAN do boleto Registrado. Estas alterações não são inconsistências do sistema e sua correção é simples, podendo ser realizadas manualmente pelo usuário.   
**12.1.14 - Inclusão de dados no cadastro de Convênio.**  
O cadastro de [convênio](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388845) na aba Remessa Bancária foi criado campos para definir pasta, nome do arquivo e extensão para geração de remessa de cobrança, débito automático e pagamento. Esses diretórios e nomes dos arquivos serão carregados automaticamente ao iniciar o processo de remessa.  
**12.1.14 - Inclusão de dados default para boleto no cadastro de Convênio.**  
No cadastro de [convênio](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388845) na aba Cobrança Bancária foi criado os seguintes campos:

* Valores defaults CNAB (Espécie, Comando, Aceite, Instrução Cod1 e Instrução Cod2)
* Registro online.

**12.1.14 - Relatório default para boleto.**  
No cadastro de [convênio](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388845) na aba Cobrança Bancária foi criado o campo "Relatório default para impressão de boleto" para informar automaticamente o relatório a ser utilizado na impressão.  
Caso seja selecionado mais de um boleto de diferentes convênios que estejam parametrizados com diferentes relatórios, na impressão de boletos não será selecionado o relatório automaticamente.  
**12.1.14 - Inclusão de boleto.**  
Na inclusão de [boleto](http://tdn.totvs.com.br/display/LRM/Boletos), foi acrescentado a opção "Utilizar conta e convênio do lançamento". Selecionando essa opção, a inclusão do boleto irá utilizar a conta/caixa e convênio do lançamento, e desmarcando essa opção, o sistema permite escolher a conta/caixa e o convênio no processo de inclusão do boleto.  
**12.1.14 - Retirada geração de Código de Barras para boletos de Débito Automático.**  
Ao incluir um [boleto](http://tdn.totvs.com.br/display/LRM/Boletos) com o tipo Débito Automático não será possível gerar código de barras para o mesmo, com isso ao editar o boleto o botão de geração do código de barras estará desabilitado.  
**12.1.14 - Dados do boleto no lançamento.**  
Nos [lançamentos](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388578) a receber que contém boletos gerados, não serão mais gravadas as informações do boleto. As informações estarão disponíveis somente no "Anexo/Boletos" de lançamentos financeiros e na visão de Boletos.  
**12.1.14 - Limpar código de barras ao cancelar remessa.**  
Ao realizar processo de [cancelamento de remessa](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388722), o sistema irá limpar automaticamente o código de barras do boleto. Dessa forma, quando o boleto for remetido novamente ao banco, o Código de Barras poderá ser gerado novamente.  
**12.1.14 - Adequação nas Fórmulas para boleto registrado.**  
As fórmulas que contém informações relacionadas ao [boleto](http://tdn.totvs.com.br/display/LRM/Boletos) (nosso número, código de barras, IPTE, vínculo com lançamento) foram alteradas. O contexto de lançamento (FLAN) deixará de ser utilizado, dando lugar para o contexto de boleto (FBOLETO).  
**12.1.14 - Geração de Código de Barras ao realizar a remessa.**  
A geração de código de barras do [boleto](http://tdn.totvs.com.br/display/LRM/Boletos) poderá ser realizada automaticamente durante a remessa de cobrança. No caso de ocorrer algum erro na geração, o lançamento não será enviado para a remessa e a informação será registrada no LOG do processo.  
A remessa de cobrança não irá gerar o código de barras automaticamente se no convênio estiver configurado para o nosso número ser gerado pelo banco.  
**12.1.14 - Parametrização para registro online.**  
Foi criado o parâmetro para definir o "Convênio default para registro online do boleto" que será utilizado no [registro online](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388845) dos portais. Somente convênios com o campo "Permite registro de boleto online" marcado serão apresentados.  
Estes parâmetros estão disponíveis em Ambiente | Parâmetros | TOTVS Gestão Financeira | Contas a Receber| Integração Bancaria | Cobrança Bancária.  
**12.1.14 - Geração de Nosso Número.**  
Foi tratado no sistema a [geração de nosso número](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388567) através do padrão definido pelo documento "Cobrança UNICRED - Composição da Ficha de Compensação - Versão 3 0". A base será definida pelo tipo nosso número do convênio, será possível utilizar um número sequencial definindo o limite inferior e superior, ou a própria referência do boleto e com o dígito verificador sendo calculado pelo sistema.  
**12.1.14 - Geração do Código de Barras.**  
Realizado o tratamento para [geração do código de barras](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388789) através do padrão definido pelo documento "Cobrança UNICRED - Composição da Ficha de Compensação - Versão 3 0".  
**12.1.14 - Agendamento de Remessa.**  
Criado parâmetro "Permite Agendamento das remessas bancárias", define permissão para o [Agendamento de Remessas](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388542) Bancarias (Remessa de Cobrança, Remessa de Débito Automático, Remessa de Pagamento e Remessa de Custódia de Cheques).  
**12.1.14 - Melhoria no detalhamento de LOG de retorno bancário.**  
Melhoria no processo de Baixa durante o processo de retorno bancário. Foi criado um parâmetro para permitir que o sistema faça um detalhamento mais elaborado tecnicamente no Log do processo de baixa durante o retorno bancário para ajudar a identificar qualquer tipo de inconsistência.
