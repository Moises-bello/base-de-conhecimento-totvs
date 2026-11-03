---
content_hash: 804010f50995b195a220fce3aa4c7c7a9f6d2e90146f85a9db1f40addfce30bb
fetched_at: '2026-06-29T00:09:32.677651+00:00'
page_id: '425458899'
product: rm
source: tdn-rm
title: Execução do Processo de Repasse de Bolsa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458899
version: 3
---

---

O processo de ***Repasse de Bolsa*** visa automatizar a cobrança ou restituição dos valores devidos à Instituição de Ensino superior, referentes a bolsas de crédito às quais os alunos possam ter.   
Ao executar o processo, o sistema irá verificar os repasses feitos por terceiros, que estejam previamente cadastrados em *Contrato | Bolsa |Anexos | Repasse de bolsa,* e os lançamentos financeiros do contrato do aluno referentes à responsabilidade dos terceiros (bolsa de crédito) efetuando automaticamente a baixa para estes lançamentos.

Caso haja divergência entre os valores cadastrados nos repasses e os valores dos lançamentos/boletos, o sistema gerenciará esta diferença da seguinte forma:

* Quando o valor cadastrado para o repasse for **maior** que o valor financeiro devido, o sistema irá efetuar a baixa total do(s) lançamento(s) da bolsa de crédito e irá incluir diretamente no sistema financeiro um lançamento do tipo **a pagar** para o responsável financeiro do aluno com o valor da diferença a ser devolvida. Como estes lançamentos referentes aos valores a serem devolvidos para o responsável financeiro do aluno são do tipo **a pagar** e serão criados diretamente no sistema financeiro, sem vínculo algum com contrato e serviços do sistema Educacional, algumas informações indispensáveis para a inclusão destes lançamentos, tais como *Tipo de documento*, *Tipo contábil*, etc, serão lidas diretamente nos Defaults parametrizados dentro do sistema financeiro. Estas informações indispensáveis para a criação dos lançamentos serão lidas e apresentadas na devida etapa/tela do processo nomeada como 'Repasse de Bolsa – **Dados de lançamentos a pagar**'. Caso estas informações não estejam definidas dentro do sistema financeiro, defina-as (ou modifique-as) neste momento diretamente na tela do processo de Repasse de Bolsa.

* Quando o valor cadastrado para o repasse for **menor** que o valor financeiro devido, o sistema irá efetuar a baixa total do(s) lançamento(s) da bolsa de crédito e irá incluir no contrato do aluno uma parcela *extra*, assim como o seu respectivo lançamento financeiro, para o responsável financeiro do aluno com o valor restante que a Instituição de Ensino ainda tem **a receber**. O valor da baixa atribuído ao lançamento financeiro referente à bolsa de crédito (lançamento do outro sacado) será o valor cadastrado para o repasse, e o restante do valor a receber, encontrado entre a diferença do valor total do lançamento e o valor cadastrado para o repasse, será lançado no campo *'Valor de integração'* do respectivo item de baixa, completando assim o valor total do lançamento. Clique aqui para saber como parametrizar o campo 'Valor de integração'.

* Quando o valor cadastrado para o repasse for **igual** ao valor financeiro devido, o sistema irá efetuar a baixa total do(s) lançamento(s) da bolsa de crédito e neste caso, como os valores são iguais, o processo será finalizado, sem a necessidade de inclusão de novos lançamentos.

**Exemplo**   
Valor do lançamento referente à Mensalidade = 1.000,00   
Valor do lançamento referente à bolsa de crédito (50%) = **500,00**   
Valor do repasse indicado no cadastro do Repasse dentro da bolsa = 200,00   
Após a execução do processo de Repasse de bolsa, o lançamento referente à bolsa de crédito (500,00) será baixado, porem o 'Valor da baixa' será = 200,00 (valor cadastrado no Repasse) e o item de baixa deste lançamento terá o campo 'Valor de Integração' = 300,00 (compondo assim o valor total do lançamento = 500,00).   
O mesmo valor lançado no campo 'Valor de Integração' será utilizado para inclusão da parcela *extra* no contrato do aluno e o seu respectivo lançamento a receber = 300,00 (valor da diferença). Como este novo lançamento será do tipo **a receber**, algumas informações necessárias para a sua inclusão, tais como *Tipo de documento*, *Tipo contábil*, etc, serão as definidas nos parâmetros do sistema Educacional e, caso não sejam encontradas, defina-as (ou modifique-as) neste momento diretamente na tela do processo de Repasse de bolsa nomeada como '**Dados de lançamentos**'.

Para executar o processo de ***Repasse de Bolsa*** acesse o menu *Financeiro/Contábil| Assistente | Repasse de bolsa* e preencha os dados necessários para selecionar os contratos conforme sua necessidade, em seguida informe os dados dos repasses:

* Data do repasse: A data aqui informada será utilizada para selecionar e somar todos os repasses cadastrados na bolsa de crédito **até a data informada**, assim como servirá para selecionar os lançamentos de bolsa de crédito que serão processados, baixando todos os que possuírem data de vencimento **até a data informada**.

**Exemplo:**O aluno possui 3 lançamentos de bolsa de crédito:  
- Lançamento 1 = data de vencimento = 01/01/2017  
- Lançamento 2 = data de vencimento = 01/02/2017  
- Lançamento 3 = data de vencimento = 01/03/2017  
Repasses cadastrados na bolsa de crédito do aluno:   
- Repasse 1 = 100,00 = 01/01/2017   
- Repasse 2 = 100,00 = 01/02/2017   
- Repasse 3 = 100,00 = 01/03/2017   
Se a data informada no processo de repasse for **01/02/2017**, o sistema irá apurar o valor de 200,00 de Repasse (soma Repasse 1 + Repasse 2) e irá baixar os lançamentos 1 e 2.

**Observação**   
Os repasses que já tiverem sido realizados, terão seu cadastro bloqueados para alterações (Repasses 1 e 2 conforme exemplo acima).

* Data de vencimento do(s) novo(s) lançamento(s):\* Os novos lançamentos que por ventura forem criados pelo processo, provenientes das diferenças entres os valores apurados, receberão a data aqui informada.
* Não calcular juros e multas ao baixar os lançamentos:\* Com a opção **'Marcada'**, será considerada como data da baixa a *data de vencimento* do lançamento, desta forma o lançamento será baixado sem cálculo de juros e multas. Com a opção **'Desmarcada'**, será considerada como data da baixa e data base para os cálculos de juros e multas a *data do repasse* informada aqui no processo.
* A data do repasse informada não pode ser maior que a data em que o processo esta sendo executado.

**Atenção:**1- Neste processo o usuário pode optar por realizar um repasse ou por *cancelar* um repasse já existente. Escolhendo a opção ***'Cancelar repasses'***, todas as ações realizadas quando da execução do repasse serão desfeitas:

* Os lançamentos referentes às bolsas de crédito baixados, terão sua baixa cancelada.
* Os novos lançamentos a receber ou a pagar, resultantes de possíveis divergências entre os valores repassados, serão excluídos.
* As parcelas extras cadastradas com a diferença a menor, serão excluídas.

2- Como a execução deste processo pode ocasionar a criação de novos lançamentos financeiros, algumas informações necessárias para inclusão destes lançamentos deverão ser informadas ou confirmadas durante a sua execução, na própria tela do processo:

* Caso o valor do repasse seja **menor** que o valor devido dos lançamentos, será incluído um lançamento do tipo **a receber** no valor da diferença e as informações necessários para a inclusão destes lançamentos serão os dados presentes na tela do processo nomeada como **'Dados de lançamentos'**:  
  . Histórico  
  . Tipo de documento  
  . Tipo Contábil  
  . Conta Caixa  
  . Moeda  
  . Opcionais: informações de tabelas opcionais e campos alfas.

* Caso o valor do repasse seja **maior** que o valor devido dos lançamentos, será incluído um lançamento do tipo **a pagar** no valor da diferença e as informações necessários para a inclusão destes lançamentos serão os dados presentes na tela do processo nomeada como **'Dados de lançamentos a pagar'**:  
  . Departamento  
  . Centro de Custo  
  . Evento p/inclusão do lançamento: somente será habilitado se o campo "Tipo Contábil" escolhido nesta tela de Lançamentos A Pagar seja "Contábil" ou "A Contabilizar".  
  . Tipo contábil  
  . Data de competência p/contabilização: somente será habilitado se o parâmetro *Educacional | Integração | Financeiro | "Data de contabilização"* for igual a "Data de competência da parcela".  
  . Tipo de documento  
  . Conta Caixa  
  . Meio de pagamento  
  . Banco  
  . Agência  
  . Código da Natureza Financeira
