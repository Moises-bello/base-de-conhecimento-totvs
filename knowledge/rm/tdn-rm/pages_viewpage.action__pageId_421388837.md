---
content_hash: f296c060ea9e8547cec14a2322700b87ba7cf8cdb41c7503270c39dd722a015d
fetched_at: '2026-06-29T00:09:19.285254+00:00'
page_id: '421388837'
product: rm
source: tdn-rm
title: FIN - Conta / Caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388837
version: 64
---

**Informamos que possui dados pessoais contidos nesta entidade. Foram colhidos para geração de rotinas financeiras.**

**Para mais informações sobre a LGPD e as soluções oferecidas pela TOTVS consulte nossa página neste link ([https://tdn.totvs.com/pages/releaseview.action?pageId=514427789](https://tdn.totvs.com/pages/releaseview.action?pageId=514427789 "Follow link")).**

Através da conta/caixa você pode controlar os saldos de uma conta bancária, os saldos dos caixas de uma empresa, os saldos do caixa de uma tesouraria. Os saldos são atualizados automaticamente de acordo com as movimentações realizadas no cadastro de Extratos de Caixa, ou seja, os saldos da conta/caixa são os resumos dos valores de cada registro de extrato de caixa relacionado com a conta/caixa.

Na janela principal é possível visualizar de forma simplificada, informações de uma ou de várias contas/caixa. Você define quantos e quais cadastros serão apresentados, criando filtros através do Gerenciados de Filtros (localizado na Barra de Ferramentas). Ao executar um filtro cada cadastro será apresentado em uma linha e as informações em colunas.

**Dicas**

A permissão para visualização de informações ou realização de processos deste módulo pode ser configurada por usuário ou por perfis, no menu Segurança dos Serviços Globais.

Na inclusão de um novo registro é possível que algumas informações já sejam apresentadas por default, para isso, edite um cadastro já existente, clique com o botão direito do mouse sobre a informação desejada, posicione o cursor do mouse sobre a opção "Valor Default" e clique sobre a informação.

As informações de alguns campos podem ser obrigatórias, para isso, clique com o botão direito do mouse sobre o campo e clique sobre a opção "Preenchimento Obrigatório". Ao clicar sobre o nome de algumas informações a janela de edição do cadastro da informação é apresentada.

É poissível definir quais colunas serão apresentadas na janela de visão dos registros utilizando a funcionalidade "Configurar Colunas", ícone localizado na barra de ferramentas. Utilizando a opção "Saldo Total" da funcionalidade "Configurar Colunas", você pode visualizar o saldo total da conta/caixa na janela de visão, ou seja, a soma dos saldos "instantâneos" e "não compensados".

Conta CaixaIdentificação

Nesta aba são apresentadas informações que identificam a conta/caixa.

Global

Quando a conta/caixa é global o seu cadastro será visualizado em todas as coligadas cadastradas no aplicativo. Após concluir a inclusão esta opção não poderá ser alterada. Para que a conta caixa global cadastrada no sistema seja visualizada nas demais coligadas é preciso que o parâmetro "[Permite Global](https://tdn.totvs.com/x/KOIdGQ)" seja marcado.

Ativa

A conta/caixa inativa não é apresentada para seleção na inclusão de lançamentos financeiros.

Filial

A informação deste campo possui integração com os seguintes campos do sistema:

Tipo

Para facilitar a classificação de cada conta/caixa, foram criadas algumas opções. Essa classificação é utilizada para agrupar os saldo que são visualizados pelo gestor/operador financeiro no [Gestão de Caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=840773775).

* Conta Corrente
* Aplicação Financeira
* Caixa
* Outros

Liquidez

Define a liquidez da conta no qual é definido no cadastro de . 

Conta Caixa / Inclusão de lançamentos

Ao incluir um lançamento financeiro informando uma conta caixa que possui uma filial parametrizada o lançamento em questão somente permitirá ser salvo quando a filial informada no mesmo seja igual a filial parametrizada na conta caixa, no contrário será exibida a seguinte mensagem:  
"O código da Filial do Lançamento é diferente do código da Filial no cadastro da Conta Caixa."

Inclusão e Edição de Extratos

Na inclusão do extrato o sistema valida a filial parametrizada na conta caixa com a filial inserida no extrato gerado, uma vez verificado que os campos possuem a mesma filial o extrato é inserido corretamente, porém ao incluir um extrato utilizando uma conta caixa que possui filial diferente do registro inserido é apresentado a seguinte mensagem:  
Valor inválido para o campo "Conta/Caixa".

Processo de fatura

Ao gerar uma fatura para dois lançamentos selecionados, sistema não permite que o lookup apresente o código da conta caixa que possui filial parametrizada quando é verificado que um dos  lançamentos que estão sendo faturados possui filial diferente da parametrizada na conta caixa.

Emissão / Recebimento de cheque

Somente será permitido emissão de cheque com a filial igual a filial da conta caixa do lançamento selecionado. Ao gerar um cheque com a filial diferente da conta caixa que está parametrizada no lançamento o sistema apresenta a seguinte mensagem:  
"Erro na geração do extrato/cheque. O código da Filial do Extrato é diferente do código da Filial no cadastro da Conta Caixa."

Geração de Acordo

No processo de acordo do lançamento, o sistema não permite que seja utilizada uma conta/caixa de filial diferente da filial do lançamento durante esse processo. Uma vez realizando processo inverso o sistema apresentará a seguinte mensagem:  
"O código da Filial do Lançamento é diferente do código da Filial no cadastro da Conta Caixa."

Aplicação financeira

Não é possível incluir na aplicação financeira uma conta caixa diferente da filial da aplicação parametrizada.

Dados Bancários

Não será possível realizar inclusão de um lançamento financeiro que possui o dado bancário com uma filial parametrizada diferente do lançamento.

Remessa

Na geração de remessa o sistema apresentará a seguinte mensagem ao selecionar os lançamentos para envio:  
"Apenas os lançamentos da filial selecionada serão enviados para a remessa. Se existirem lançamentos de outras filiais no filtro, serão ignorados."

Retorno Bancário

No Retorno de Pagamento somente serão baixados os lançamentos da filial informada na tela de importação de pagamento eletrônico. Quando a filial não for informada, o sistema irá baixar todos os lançamentos de todas as filiais.

Saldos

Saldo Instantâneo: É o saldo dos extratos de caixa compensados. As compensações dos extratos de caixa irão alterar o saldo instantâneo.

Saldo Não Compensado: É o saldo dos extratos de caixa não compensados.

Data Base

O saldo da data base permanecerá o mesmo, até que haja uma liberação de extratos de caixa relacionados á conta/caixa, passando assim a adotar o valor do saldo instantâneo.  
Após salvar o cadastro o valor do "Saldo na Data Base" não pode ser alterado.

Ao tentar incluir uma Conta/Caixa com este saldo igual a zero, o sistema irá perguntar se você realmente quer realizar esta operação, pois este saldo não poderá ser alterado posteriormente.

Banco

Saldo Bancário: É o saldo do banco correspondente à conta/caixa cadastrada em determinada data.

Data do Saldo Bancário: Deve ser informada a data em que o saldo bancário informado no campo anterior foi consultado.

Observação

O grupo Banco, que contém os campos Saldo Bancário e Data do Saldo Bancário, está disponível a partir da versão 12.1.2406.

Esses campos poderão ser alimentados automaticamente através do uso do processo de importação de arquivos de conciliação bancária nos formatos OFX, CNAB 240 e 200 posições.

O Saldo e a Data só serão preenchidos pelo processo de importação do arquivo de conciliação, caso a data do saldo do arquivo importado seja maior que a data salva no cadastro da conta/caixa.

Para mais detalhes sobre a importação de arquivo no formato OFX, [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=853311029).

Para mais detalhes sobre a importação de arquivo no formato CNAB, [clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=421388581).

Coligada Proprietária

Este campo estará disponível para edição apenas quando a opção "Global" e o parâmetro "Usar Contabilização de Mútuo" (Assistente de Implantação de Processos | Etapa Contabilização do Extrato de Caixa) estiverem marcados.  
A coligada proprietária é uma informação específica para a funcionalidade de contabilização de mútuo.

Moeda

Você pode controlar uma conta/caixa com a moeda em Real (R$) ou utilizar outros tipos de moedas.  
As moedas devem ser cadastradas no cadastro de Moedas e Índices (menu Cadastros | Moedas e Índices).

Dados Adicionais

Módulo de Caixa

Permitir Abertura de Sessão: Com esta opção marcada a conta/caixa poderá ser utilizada na abertura de uma Nova Sessão de Caixa.

Último número de Caixa Aberto: Será apresentado o número do último caixa aberto com essa conta/caixa.

Limite Inferior

Através desta opção você pode definir um saldo instantâneo mínimo para a conta/caixa.

**Exemplo**  
Em uma determinada conta bancária o saldo não pode ser inferior a R$ 1.000,00 (Hum mil reais). Se você determinar um limite inferior para a conta/caixa relacionada a esta conta bancária, o sistema não permitirá que nenhum extrato de caixa seja compensado após o saldo instantâneo atingir o limite inferior. O saldo instantâneo só pode ser igual ou maior que o limite inferior.

Período para Inclusão de Extratos

Através desta opção você pode definir um período para a inclusão de extratos de caixa por conta/caixa.

**Exemplo**

Para a conta/caixa 001, só podem ser incluídos extratos de caixa com a data do mês corrente.  
No mês de março de 2005, você define: Período para Inclusão de Extratos - Inicial = 01/03/2005 Período para Inclusão de Extratos - Final = 31/03/2005  
Após esta definição, a inclusão de extratos de caixa utilizando esta conta/caixa só será permitida se a data do extrato estiver dentro deste período.

**Observações**

A definição deste período é individual, ou seja, cada conta/caixa pode ter um período diferente.  
A funcionalidade desta opção valida Extratos de Caixa "Manuais" e Extratos de Caixa "gerados por outros módulos do sistema".  
A funcionalidade do parâmetro "Período Inclusão do Extrato" (Assistente de Implantação de Processos | Etapa Extrato de Caixa do Financeiro) tem prioridade sobre o período de inclusão informado na conta/caixa, mas apenas para extratos de caixa manuais.

Geração de CPMF

Através deste campo você pode controlar a geração automática do CPMF individualmente por conta/caixa, ou seja, cada conta/caixa pode ter um controle de geração de CPMF individual.  
Respeitar Parametrização: A geração do extrato de caixa de CPMF respeitará o parâmetro "Gerar CPMF automaticamente" (Assistente de Implantação de Processos | Etapa Extrato de Caixa do Financeiro).  
Gerar Automaticamente: Ao gerar um extrato de caixa de saque que possui esta conta/caixa, o extrato de caixa de CPMF é gerado automaticamente.  
Não Gerar: Ao gerar um extrato de caixa de saque que possui esta conta/caixa, o extrato de caixa de CPMF não será gerado automaticamente.  
Podendo ser gerado manualmente através da inclusão de um extrato de caixa com o "Tipo de Operação" Saque CPMF (menu Cadastros | Extratos de Caixa).

**Atenção**

A funcionalidade deste campo tem prioridade sobre o parâmetro "Gerar CPMF automaticamente" (Assistente de Implantação de Processos | Etapa Extrato de Caixa do Financeiro).

Último Cheque

Neste campo é apresentado o número do último cheque emitido para esta conta/caixa.  
Você também pode alterar este número quando a seqüência de cheques for atualizada, desta forma, ao solicitar a emissão de um cheque utilizando esta conta/caixa, o sistema apresentará por default o número informado + 1(um).

**Exemplo**

Na conta/caixa 10, você informa no campo "Último Cheque" o número 1000. Ao solicitar a emissão de um cheque utilizando esta conta/caixa, o sistema apresenta por default o número "1001" (o número que você informou + 1). Ao confirmar a emissão do cheque, o sistema atualizará automaticamente o número informado no campo para o último número, ou seja, "1001".

Livro de Caixa Produtor Rural

Código: O código inserido neste campo será considerado no LCDPR. Este código deve ser de três digitos e quando gerado o arquivo da rotina, os dados da conta caixa com esse código serão carregados nos Registro 0050 e  Q100.

[Data de Corte](https://tdn.totvs.com/x/AOEdGQ)

* Saldo Data de Corte - Nesse campo será informado o saldo que irá substituir o saldo na data base da conta caixa caso a data base seja anterior a data de corte.
* Data de Corte - nesse cadastro ocampo  é apenas informativo, trata-se do valor preenchido a partir do processo de carga da data de corte.

**Observações:**

* Os campos referente a data de corte só serão apresentados no cadastro de conta caixa quando configurado no sistema o uso de data de corte.
* A parametrização de data de corte será usada no novo Fluxo de Caixa.
Integração Bancária

Ao utilizar esta conta/caixa na edição de um lançamento financeiro com a natureza a Receber, estas informações serão utilizadas na pasta Integração Bancária do Lançamento,

Banco, Agência e Conta.

Além de selecionar estas opções é possível "visualizar", "incluir", "editar" e "excluir", registros destes cadastros.

Contabilidade

Nesta aba são apresentadas as configurações relacionadas à contabilidade gerada para o extrato de caixa a partir da Conta Caixa selecionada.

Defaults Contábeis

Nesta opção é possível definir as informações contábeis que serão utilizadas para geração dos lançamentos contábeis do extrato de caixa, como: Conta Contábil, Filial, Departamento, etc.

**Observação:**

* A opção de  [Mútuo](https://tdn.totvs.com/x/NFpsHQ) só fica disponível para Conta Caixa Global, desde que a coligada do contexto seja a proprietária da mesma e o parâmetro de sistema "Usar Contabilização de Mútuo" esteja marcado.

Lotes contábeis do extrato

Nesta opção é possível definir quais lotes contábeis serão utilizados para inclusão e estorno de extrato de caixa.

**Observação:**

* Conta Caixa Global não permite o cadastro de Lote Contábil, já que os lotes são definidos para cada coligada diferente, por exemplo, da conta corrente, que pode ser global.
Extrato Online

Configurações relacionada a chamada API bancária de extrato  que tem como objetivo [consultar o saldo bancário online](https://tdn.totvs.com/display/LRM/Consulta+Saldo+Online). Esse saldo será atualizado no campo saldo bancário da aba identificação. **(A partir do release 12.1.2406)**

**Configurações**

Habilita Extrato Online: Define se a conta caixa está habilitada para consultar o extrato bancário online.

Ambiente: Define se o ambiente da chamada do serviço será "Teste" ou "Produção".

**Obs.: Para ambiente de teste utilizar os dados abaixo:**

* **Agência 551 e conta 5087**
* **Agência 1505 e conta 1348**
* **Agência 452 e conta 123873**

Extrato OnLineBanco do Brasil

* URL do Serviço de Extrato Online: Deve ser informada a URL do serviço de extrato online disponibilizada pelo banco.
  + <https://api-extratos.bb.com.br/extratos/v1>
* URL de Homologação do Serviço de Extrato Online: Deve ser informada a URL de homologação do serviço de extrato online disponibilizada pelo banco. 
  + <https://api.hm.bb.com.br/extratos/v1> (sem mTLS) ou <https://api-extratos.hm.bb.com.br/extratos/v1> (com mTLS)
* URL do Serviço de Autorização: Deve ser informado a URL do sistema autorizador que retornará o token de acesso ao serviço de extrato online.
  + [https://oauth.bb.com.br/oauth/token](https://oauth.hm.bb.com.br/oauth/token)
* URL de Homologação do Serviço de Autorização: Deve ser informado a URL de homologação do sistema autorizador que retornará o token de acesso ao serviço de homologação do exrtato online. 
  + <https://oauth.hm.bb.com.br/oauth/token>
* Client ID: Código de acesso ao sistema autorizador fornecido pelo banco.
* Client Secret: Senha de acesso ao sistema autorizador fornecido pelo banco.
* Ap-Key: Chave secreta (produção) de validação do cliente disponibilizada pelo banco.
* App-Key de homologação: Chave secreta (homologação) de validação de disponibilizada pelo banco

TOTVS Pagamento Instantâneo

Nesta aba é apresentado o campo para ser preenchida a chave PIX que deve ser utilizada nos pagamentos realizados via PIX, quando utilizada a [solução de pagamento "TOTVS Pagamento Instantâneo (TPI/TPD)](https://tdn.totvs.com/pages/viewpage.action?pageId=577622236)". Disponível a partir dos patchs 12.1.2502.230, 12.1.2506.179 e 12.1.2510.112 da BibliotecaRM. **Importante**: Necessário executar o [RM.Atualizador](https://tdn.totvs.com/display/LRM/RM+Atualizador) para a criação do campo na base de dados. 

Chave PIX  
  
Defina a chave PIX que deverá ser utilizada nos pagamentos via PIX.

Veja Também
