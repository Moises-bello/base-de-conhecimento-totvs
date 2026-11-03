---
content_hash: 16cf1c71494dd31706805dbde2a7a60fbf399140138f5f637520f71959a95961
fetched_at: '2026-06-29T00:11:36.788912+00:00'
page_id: '773517977'
product: rm
source: tdn-rm
title: TCGI - Comissão - Regra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=773517977
version: 6
---

### **Cadastro da Regra de Comissão**

O objetivo do cadastro de regra de comissão é informar os dados para a realização do cálculo dos valores da comissão. As regras definidas nesse cadastro poderão ser associados ao cadastro de modalidade de comissão, podendo uma regra ser definida em mais de uma modalidade.

Para utilizar o Cadastro de regra de comissão , é preciso primeiro liberar acesso para o Perfil do usuário em:  
clique na aba "Acesso a Menus" em 'Gestão de Imóveis >> Venda >> Contratos >> Comissões >> [1.01.05.03] Regras da Comissão' 

**Cadastro da Regra de Comissão tem:**

**Tipo de comissão:**

* Comissão
* Prêmio
* Apuração Mensal

**Tipo de Valor:**

* Valor fixo
* Percentual
* Fórmula para definir o valor
* Fórmula para definir o percentual

**Comissão recebida por:**

* Imobiliária da proposta
* Corretor da proposta
* SDR da proposta
* Outro Comissionado (Diretor, Supervisor, Gerente, Secretária e etc.)
* Comissionado Avulso Portal de Imóveis  (Permite adicionar um comissionado, no Portal de Imóveis, não previsto na Modalidade, com um regra predefinida )

Importante!

Quando o ***Tipo Pessoa Quem Recebe*** for ***Outro Comissionado*** (Diretor, Supervisor, Gerente, Secretária e etc.) e o cadastro deste *Cliente/Fornecedor* (FCFO.CODFCO) não for do Tipo ***Global*** (FCFO.CODCOLIGADA = 0), ou seja, acessível em todas as Coligadas, o cadastro deste Cliente/Fornecedor deverá ser replicado para **todas** as Coligadas que têm Empreendimentos Ativos no Portal de Imóveis.

Caso essa Regra não seja atendida, ao salvar uma Proposta com Comissão, o Sistema apresentará a exceção abaixo ao Usuário:

*"Não existe um fornecedor do tipo quem recebe [Outro Comissionado] cadastro na coligada [#] do contrato com o mesmo CPF do fornecedor [#######] associado a Regra para a geraçao da comissão do contrato [######]. Todos os comissionados devem ser copiados para todas as coligadas que forem gerar comissão, pois o sistema não está configurado como global o fornecedor."*

Caso seja necessário pagar a Comissão para algum *Usuário* que esteja associado ao ***Grupo de Administradores*** do Portal de Imóveis, o sistema irá validar as seguintes condições:

* O Grupo *Administrador*, no Portal de Imóveis deve ter *obrigatoriamente* o ID 1; e
* Os usuários deste Grupo não podem ter nenhum *Papel Exercido* associado (nem Corretor, nem Correspondente Bancário e nem SDR);

Sendo que as comissões gravadas para os Usuários desse Grupo serão enviadas com o *Tipo de Usuário* de Diretor/TI (*TipoUsuarioComissionado = 3*).

**Tipo de integração:**

* Folha de Pagamento
* Faturamento (Compras)
* Financeiro
* Sem integração (essa opção sempre será utilizada em caso de pagamento pelo cliente)

**Comissão paga por:**

* Empresa
* Cliente
* Híbrido (parte empresa e parte cliente)

**Código da Função:**

Função (campo texto informativo para definir qual é a função de quem recebe a comissão)

**Código do Comissionado:**

Informar  o código do comissionado para:

* Diretor
* Supervisor
* Superintendente
* Presidente
* Secretaria

**Chapa de Funcionário** :   
O fornecedor comissionado não está associado com a Chapa no TOTVS Folha de Pagamento, sendo que a integração configurada é com a Folha de Pagamento. Assim que possível, execute o processo de Associar Chapa ao Fornecedor da Comissão ou acesse o cadastro do Cli/For => Dados Complementares (TCGI) =>Ocupação Profissional => Tipo de Integração Folha de Pagamento e selecione a chapa   
Caso a Integração seja : TOTVS Folha de Pagamento , o Fornecedor tem que estar associado com uma Chapa do TOTVS Folha de Pagamento.

**Parâmetro: Pagar Comissão para Imobiliária.**

Este parâmetro marcado , indica que quem irá receber a Comissão será a Imobiliária e assim , depois repassar para o Vendedor.

Essa regra pode ser sobreposta no cadastro de cliente e fornecedor, conforme o destaque da informação abaixo

**Regra de Pagamento:**

Informar um tipo definido já cadastrado em Regras de Pagamento da Comissão

**Ordem de Cálculo da Regra** :

É para definir a ordem que será aplicada a Regra de Comissão, principalmente quando o cálculo é realizado por fórmula,

Tipo de Integração de Comissão - Cadastro do Fornecedor.

Tipo de Integração de Comissão na aba do TCGI do **Cadastro de Fornecedor** para indicar o tipo de integração que será realizado no processo de integração da comissão com os outros sistemas (Compras, Financeiro ou Folha de Pagamento).

Ao gerar a comissão, o sistema irá verificar se o tipo de integração do  Fornecedor está preenchido e utilizará na comissão.

Caso esteja "**Sem Integração**", o sistema buscará a configuração da **regra de comissão**.

Inserir - Dados Complementares ( TCGI )

Aba Comissão - Tipo de  Integração : Receberá a Comissão por :

* Sem Integração
* TOTVS Compras e Faturamento
* TOTVS Folha de Pagamento
* TOTVS Gestão Financeira

Pagar Comissão para Imobiliária

### Pagar Comissão para Imobiliária da Proposta

Pode definir se a comissão de um correto será paga a imobiliária. Somente com a opção marcada que esse parâmetro irá sobrepor a regra da comissão.
