---
content_hash: a4f4e494ecba62e784008254a6bb35d9dfb485e48ea4a00a9d57ce27ea9e9858
fetched_at: '2026-06-29T00:11:36.906830+00:00'
page_id: '773520485'
product: rm
source: tdn-rm
title: API - Comissão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=773520485
version: 2
---

### Apis de Comissões

API : POST: [http://localhost:8051/api/imb/v1/commission/view](http://localhost:8021/api/imb/v1/commission/view)

API Comissão View

Exemplo API

{  
    "TipoUsuarioComissionado": "0",  
    "CpfOuCnpjUsuarioComissionado": {  
        "CpfCnpj": "XXX.XXX.XXX.XX"  
    },  
    "CpfOuCnpjSubordinados": [  
        { "CpfCnpj": "" },  
        { "CpfCnpj": "" }  
    ],  
    "CnpjImobiliaria": {  
        "CpfCnpj": ""  
    },  
    "DataInicial": "2022-03-01",  
    "DataFinal": "2022-03-11",  
    "CodigoEmpreendimento": null  
}

API: GET: <http://localhost:8051/api/imb/v1/commission/103>

API para buscar as comissões de acordo com o ID da comissão.

Modelo Json Solicitação Geração ComissãoRESPONSEtrueParâmetros

Parâmetros:

* Id da comissão que fica no final da URL.

Dados recebidos:

* idcomissao: Id da comissão;
* idmodcomissao: Código da modalidade da comissão
* data: Data da comissão;
* codcolcontrato: Código da coligada do contrato;
* contrato: Código do contrato;
* codpessempr: Código do empreendimento;
* nomefantasia: Nome fantasia do empreendimento;
* numunid: código da unidade do contrato;
* numsubunid: código da subunidade do contrato;
* nomecorretor: Nome do Corretor Principal
* statuscomissao: Status da Comissão
* datavenda: data que a venda foi efetivada
* valorcomissaototal: Valor total da comissão;
* valorbase: valor da base de cálculo da comissão
* valormar: valor máximo que uma comissão pode ter
* comissionados: Lista dos comissionados da comissão.

Dados recebidos dos comissionados:

* + - idcomissao: id da comissão pai;
    - iditemcomissao: Código desse item na comissão;
    - idregracomissao: Código da regra da comissão;
    - percentualcomissao: Percentual da Comissão do comissionado
    - valorcomissaocorretor: Valor da comissão do comissionado;
    - nroparcelas: quantidade de parcelas do comissionado;
    - statuscomissaocorretor: Status da Comissão do Comissionado;
    - codfuncao: código da função;
    - dscfuncao: Descrição da função;
    - tipoquempaga: Tipo de quem paga;
    - percentual: Percentual de quem paga a comissão - Cliente ou Empresa;
    - codcolcfo: Código da coligada do comissionado;
    - codcfo: Código do comissionado;
    - nomecfo: Nome do comissionado;
    - pagarcomissaoaimob: Pagar comissão a imobiliária;
    - tipoquempaga: Descrição de quem paga;
    - codtipoquempaga: Código de quem paga;
    - tipocomissao: Descrição do tipo da comissão;
    - codtipocomissao: Código do tipo da comissão;
    - tipocalculocomissaoitem: Descrição do tipo de cálculo da comissão;
    - codtipocalculocomissaoitem: Código do tipo de cálculo da comissão;
    - tipovalor: Descrição do tipo de valor da comissão;
    - codtipovalor: Código do tipo de valor da comissão;

API: POST: [http://localhost:8051/api/imb/v1/commission/](http://localhost:8051/api/imb/v1/commission/view)

Api para buscar comissões de acordo com o usuário logado.

Modelo Json Solicitação Geração ComissãoGET - Exemplo requisiçãotrueModelo Json Solicitação Geração ComissãoRESPONSEtrueParâmetros

Parâmetros:

* **TipoUsuarioComissionado: Corresponde ao tipo de usuário logado no Portal de Imóveis (0=Corretor, 1=Gerente, 2=Imobiliária);**
* **CpfOuCnpjUsuarioComissionado: CPF ou CNPJ do usuário logado no Portal de Imóveis;**
* CpfOuCnpjSubordinados: Lista de CPF ou CNPJ dos usuários do Portal de Imóveis subordinados ao Superior/Gerente;
* CnpjImobiliaria: CNPJ da imobiliária associada ao usuário logado no Portal de Imóveis, para restringe comissões da imobiliária;
* DataInicial: Data Inicial do período para buscar as comissões;
* DataFinal: Data final do período para buscar as comissões;
* CodigoEmpreendimento: Filtro de restrição para empreendimento das comissões.

Dados Recebidos:

* count: quantidade de itens encontrados.
* hasNext: Se tem próximo item.
* items: Lista dos itens encontrados.

Dados recebidos dos itens é o mesmo da primeira API da comissão por ID

API: GET: <http://localhost:8051/api/imb/v1/commission/103/sellers>

Api para buscar os comissionados de uma comissão específica e retorna a mesma estrutura da API de busca uma comissão.

API: GET: <http://localhost:8051/api/imb/v1/commission/103/sellers/1>

Api para buscar um comissionado específico de uma comissão específica e retorna a mesma estrutura da API de busca uma comissão.

API: DELETE: <http://localhost:8051/api/imb/v1/commission/103/sellers/1>

Api para deletar um comissionado específico de uma comissão específica e retorna a mesma estrutura da API de busca uma comissão.

Parâmetros

Caso seja deletado um comissionado que tem comissão paga pela empresa e pelo cliente, o valor da comissão/percentual fica para uma das duas situações.

Sendo assim, caso apague o comissionado cliente, então o valor/percentual da comissão vai para comissionado empresa e vice-versa.

Se for um comissionado comum é apagada normalmente o registro

API: PUT: <http://localhost:8051/api/imb/v1/commission/103/sellers/1>

Api para atualizar o dado de um comissionado específico de uma comissão específica e retorna a mesma estrutura da API de busca uma comissão.

Modelo Json Solicitação Geração ComissãoPUT - Exemplo requisiçãotrueParâmetros

* % Quem paga -
  + Só pode alterar entre 1 e 100%;
    - se passar diferente será ignorado a alteração
    - Se deseja zerar o percentual para excluir um dos comissionados quem paga cliente ou empresa deve excluir o registro para o sistema manter apenas um deles e recalcular o percentual de quem paga.
    - se estou alterando o comissionado para 100% quem paga a comissão, exemplo Empresa, e existe o seu par, cliente,  
      então essa ação deve ser feita deletando o cliente comissionado, pois os seus valores não existe mais, ficando zerados
  + Caso o percentual esteja 100 e seja reduzido, então deve-se criar o comissionado parte empresa ou parte cliente com a diferença;
  + Se alterar esse campo, sempre terá prioridade em relação a alteração do valor da comissão ou do percentual, vai depender do tipo de valor da comissão;
  + Alterando esse campo, ele interfere diretamente nos valores de %Comissão ou Valor da Comissão, pois mudando o percentual de quem paga vou alterar esses campos campos com  base na nova proporção de de quem paga.
    - Exemplo: Corretor quem paga é 100% empresa e o tipo valor da comissão é PERCENTUAL, que tem o valor de 2%.
      * Vou alterar o percentual de quem paga empresa para 60%, dessa forma o percentual da comissão ficara 60% de 2% = 1,2%;
      * Vou criar o corretor quem paga cliente que ficará com o restante de 40%, dessa forma ficará com o resto do percentual 0,8%;
    - O mesmo raciocínio valerá para o tipo Tipo de valor quando for valor comissão;
* Pagar a Imobiliária; (Está bloqueado nesse momento , não iremos liberar)
  + só pode alterar se não for imobiliária  e for quem paga empresa
    - se passar diferente será ignorado a alteração
* Tipo de Cálculo;
  + Se quem paga for empresa,  pode alterar conforme o tipo de cálculo para 0 e 1
    - se passar diferente será ignorado a alteração;
  + Se quem paga for cliente, pode alterar para o tipo 0, 1 e 2;
    - se passar diferente será ignorado a alteração
* Nro de Parcelas;
  + Só pode alterar se quem paga for empresa;
    - se passar diferente será ignorado a alteração
* % Comissão;
  + só pode alterar se o tipo valor for Percentual e não tiver alterado o percentual de quem paga;
    - se passar diferente será ignorado a alteração
    - Exemplo:  Corretor quem paga é 50% empresa  e 50% cliente, o tipo valor da comissão é PERCENTUAL, que tem o valor total de 2%, sendo 1% para cliente e 1% para empresa.
      * Vou alterar o percentual da comissão do corretor empresa para 2% e a parte cliente ficará com 1%, dessa forma o percentual de quem paga não é mais 50% para cada, vou recalcular a proporção de ambos que ficará com 66,6667% parte empresa e  33,3332% parte cliente%;
      * Vou criar o corretor quem paga cliente que ficará com o restante de 40%, dessa forma ficará com o resto do percentual 0,8%;
    - o mesmo raciocínio valerá para o tipo Tipo de valor quando for valor comissão;
* Valor Comissão.
  + Só pode alterar se o tipo valor for valor comissão e não tiver alterado o percentual de quem paga.
    - se passar diferente será ignorado a alteração

Parâmetros:

* idcomissao: será utilizado da API;
* iditemcomissao: será utilizado da API;
* idregracomissao: Id da regra não permite alteração;
* **percentualcomissao: Informar o percentual da Comissão do comissionado, caso seja o tipo valor seja percentual**
* **valorcomissaocorretor: Informar o percentual da Comissão do comissionado, caso seja o tipo valor seja valor;**
* **nroparcelas: Informar a quantidade de parcelas do comissionado;**
* codfuncao: Código da função não permite alteração;
* dscfuncao: Descrição da função não permite alteração;
* tipoquempaga: Tipo de quem paga não permite alteração;
* **percentual: Informar o percentual de quem paga a comissão (Cliente ou Empresa);**
* codcolcfo: código da coligada do comissionado não permite alteração;
* codcfo: Código do comissionado não permite alteração;
* nomecfo: Nome do comissionado não permite alteração;
* pagarcomissaoaimob: Pagar comissão a imobiliária não permite alteração;
* tipoquempaga: Descrição de quem paga não permite alteração;
* codtipoquempaga: Código de quem paga não permite alteração;
* tipocomissao: Descrição do tipo da comissão não permite alteração;
* codtipocomissao: Código do tipo da comissão não permite alteração;
* tipocalculocomissaoitem: Descrição do tipo de cálculo da comissão não permite alteração;
* codtipocalculocomissaoitem: Código do tipo de cálculo da comissão não permite alteração;
* tipovalor: Descrição do tipo de valor da comissão não permite alteração;
* codtipovalor: Código do tipo de valor da comissão não permite alteração;

Dados recebidos dos itens é o mesmo da primeira API da comissão por ID

API: POST: <http://localhost:8051/api/imb/v1/commission/103/sellers/1>

Api para incluir um comissionado específico de uma comissão específica e retorna a mesma estrutura da API de busca uma comissão.

Modelo Json Solicitação Geração ComissãoPOST - Exemplo requisiçãotrueParâmetros

Só pode criar uma comissionado o tipo quem recebe "Comissionado Avulso PI"  e esteja na modalidade dessa comissão, pois isso indica que o usuário permite incluir novos comissionados com valores defaults. É permitido inserir vários desse tipo e nunca para a mesma pessoa. Se já existir a pessoa para esse tipo de avulso basta realizar o Put desse registro.

O Id da regra é o campo mais importante, pois ele busca esse comissionado avulso de sua modalidade e insere  com os valores defaults para essa comissão.

Caso seja incluindo um comissionado que tem comissão paga pela empresa com percentual menor que 100%, então será criado o comissionado cliente com o a diferença desse percentual e calculando a nova proporção do percentual da comissão em cima dessa proporção de cliente e empresa.

Se for criado um comissionado com regra quem paga 100%, regra padrão, então cria apenas o próprio registro.

Parâmetros:

* idcomissao: será utilizado da comissão que está inserindo a regra;
* iditemcomissao: sequencial que será criado pela API;
* **idregracomissao: Código da regra da comissão do comissionado que será inserido;**
* **percentualcomissao: Informar o percentual da Comissão do comissionado ou buscará o valor default da regra**
* valorcomissaocorretor: Será calculado com base do percentual ou informar o valor da comissão do comissionado ou buscará o valor default da regra;
* **nroparcelas: Informar a quantidade de parcelas do comissionado ou buscará o valor default da regra;**
* **codfuncao: Informar o código da função ou buscará o valor default da regra;**
* dscfuncao: Descrição da função - Buscará o valor default da regra;
* **tipoquempaga: Informar o tipo de quem paga ou buscará o valor default da regra;**
* **percentual: Informar o percentual de quem paga a comissão (Cliente ou Empresa) ou buscará o valor default da regra;**
* **codcolcfo: Informar o código da coligada do comissionado;**
* **codcfo: Informar o código do comissionado;**
* nomecfo: Nome do comissionado;
* pagarcomissaoaimob: Pagar comissão a imobiliária - Buscará o valor default da regra;
* tipoquempaga: Descrição de quem paga - Buscará o valor default da regra;
* codtipoquempaga: Código de quem paga - Buscará o valor default da regra;
* tipocomissao: Descrição do tipo da comissão - Buscará o valor default da regra;
* codtipocomissao: Código do tipo da comissão - Buscará o valor default da regra;
* tipocalculocomissaoitem: Descrição do tipo de cálculo da comissão - Buscará o valor default da regra;
* codtipocalculocomissaoitem: Código do tipo de cálculo da comissão - Buscará o valor default da regra;
* tipovalor: Descrição do tipo de valor da comissão - Buscará o valor default da regra;
* codtipovalor: Código do tipo de valor da comissão - Buscará o valor default da regra;

Dados recebidos dos itens é o mesmo da primeira API da comissão por ID

API: GET: [http://localhost:8051/api/imb/v1/commission/103/single\_sellers/](http://localhost:8051/api/imb/v1/commission/103/sellers/6 "Follow link")

API para buscar a regra do comissionado avulso para o Lookup do portal de imóvel, para todos os comissionados do tipo avulso que estejam na modalidade da regra da comissão editada, seguir o padrão abaixo de URI 

Modelo Json Solicitação Geração ComissãoRESPONSEtrueParâmetros

Dados recebidos dos itens é o mesmo do padrão da primeira API dos comissionados

API: POST: [http://localhost:8051/api/imb/v1/commission/generate](http://localhost:8051/api/imb/v1/commission/register)

API para gerar a comissão de forma automática.

Modelo Json Solicitação Geração ComissãoPOST - Exemplo requisiçãotrueParâmetros

Parâmetros:

* **codColContrato: Código da coligada do contrato;**
* **contrato: Código do contrato;**
* dataComissao: Data da comissão;
* valorBaseComissao: Valor base da comissão;
* **cpfOuCnpjCorretorProposta: CPF ou CNPJ do corretor;**
* cpfOuCnpjImobiliariaProposta: CPF ou CNPJ da Imobiliária;
* cpfOuCnpjSDRProposta: CPF ou CNPJ do SDR.

Dados recebidos dos itens é o mesmo da primeira API da comissão por ID

API: POST: <http://localhost:8051/api/imb/v1/commission/103/recalculates>

API para recalcular e alterar informações da comissão já cadastrada.

Modelo Json Solicitação Geração ComissãoPOST - Exemplo requisiçãotrueParâmetros

Parâmetros:

* valorbase: Valor base da comissão (Obs.: Caso não informado, será utilizado o valor da venda);
* data: Data da comissão (Obs.: Caso não informado, será utilizado a data da venda);

Dados recebidos dos itens é o mesmo da primeira API da comissão por ID

API: GET: <http://localhost:8051/api/imb/v1/commission/103/sellers/payments>

API para retornar as parcelas de pagamento da comissão

Regras

Regras:

* Se quem paga for o cliente, então devolve a parcela criada na comissão com os comissionados e seus valores;
* Se quem paga for  a empresa e o tipo de cálculo que quem paga NÃO for atrelado a baixa, então devolve as parcelas criadas na comissão com os comissionados e seus valores;
* Se quem paga for a empresa e o tipo de cálculo que quem paga for atrelado a baixa, teremos que fazer uma previsão desse pagamento com base no plano de financiamento gerado e a data de vencimento e calcular quando seria pago a comissão e qual o percentual dessa parcela seria destinado a comissão
Modelo Json Solicitação Geração ComissãoRESPONSEtrue
