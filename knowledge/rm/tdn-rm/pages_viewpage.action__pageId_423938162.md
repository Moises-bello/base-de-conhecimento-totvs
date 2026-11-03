---
content_hash: 8058f3f938ffd7d004cbcbd8c3337af09eb044adf0d1c246eb0227fe3f0d2966
fetched_at: '2026-06-29T00:09:25.475985+00:00'
page_id: '423938162'
product: rm
source: tdn-rm
title: Funcionário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938162
version: 16
---

**Informamos que possui dados pessoais contidos nesta entidade.**

**Para mais informações sobre a LGPD e as soluções oferecidas pela TOTVS consulte nossa página neste link ([https://tdn.totvs.com/pages/releaseview.action?pageId=514427789](https://tdn.totvs.com/pages/releaseview.action?pageId=514427789 "Follow link")).**

Nesta opção, cadastram-se os compradores e vendedores responsáveis pelas rotinas de movimentações do sistema, incluindo Cotações, Contratos e Ressuprimento de Materiais no Estoque.  
A denominação 'Funcionário' é um padrão do sistema, porém esta informação poderá ser alterada através do Parametrizador à Parâmetros Gerais à Tabelas à Funcionário.  
A seleção de um Comprador/Vendedor dentro da movimentação depende de parametrização de cada Tipo de Movimento (parametrizador do Tipo de Movimento, Etapa 8 - Movimentos - Tabelas - Funcionários), que é também onde é determinada se a indicação de Compradores/Vendedores é facultativa ou obrigatória.  
Além das informações básicas de cadastro, como Nome, Cargo, Comissões (que podem ser utilizadas em relatórios), Filial a qual o Funcionário pertence e um percentual de desconto máximo (validado também nos parâmetros do tipo de movimento), o sistema ainda conta com informações de:

**Tipo**: Localizado na pasta Principal do cadastro, o Tipo do Funcionário indica para quais rotinas este Funcionário estará associado. Como exemplo, podemos citar que, caso um Funcionário esteja cadastrado com o Tipo 'Vendedor', este Funcionário não poderá ser utilizado em movimentações de Compras.   
***Observação***: Algumas opções não geram impactos nas movimentações e, consequentemente, não fazem tal validação.

**Identificador da Pessoa**: Também localizado na pasta Principal, este campo permite a associação do Funcionário à uma Pessoa cadastrada em TOTVS Gestão de Pessoas. Desta forma, é possível, inclusive, que este Funcionário também seja vinculado a um Usuário do sistema. Assim, ao efetuar movimentações, o sistema carrega automaticamente o Funcionário associado à Pessoa que, consequentemente, está relacionada ao Usuário utilizado para logar no sistema.  
***Observação***: Este recurso também depende de parametrização do Tipo de Movimento (parametrizador do Tipo de Movimento, Etapa 8 - Movimentos - Tabelas - Funcionários).

**Perfil do Funcionário**: Localizado na pasta Frente de Loja, as informações de Perfil do Funcionário são utilizadas pelo PDV Consult (parceiro), o qual relaciona informações do TOTVS Gestão de Estoque, Compras e Faturamento com o Ponto de Venda.  
***Observação***: Estas informações somente são utilizadas pela integração entre o Ponto de Venda e o TOTVS Gestão de Estoques, Compras e Faturamento.

**Valores**: Localizado na pasta Valores, é possível fazer um cadastro de valores de comissões para o Funcionário, de acordo com Filial e Centro de Custos. Estas informações podem ser utilizadas em relatórios de metas de Vendas, de acordo com o Centro de Custo utilizado na movimentação.

---

true

Outras Informações

[Painel de Metas dos Funcionários](http://tdn.totvs.com/pages/viewpage.action?pageId=4816380)

***Observação:***

Esta rotina dispõe da funcionalidade de integração com TOTVS PDV PROTHEUS, MasterSales e [NG - Quírons](https://tdn.totvs.com/pages/viewpage.action?pageId=662437193). As informações podem ser consultadas no item [Integração Protheus X RM](https://tdn.totvs.com/x/gKpWF) do Controle de Lojas e Front Loja e também no documento de integração [TOTVS PDV x BackOffice RM](https://tdn.totvs.com/display/public/INT/DI_TOTVS_PDV_x_BackOffice_RM)

Consistências de funcionários aplicadas nas movimentações:

* Título do Funcionário é obrigatório quando tipo de movimento está parametrizado Edita Funcionários diferente de Não edita;
* Consiste se código está de acordo com a máscara;
* Verifica se inativo;
* Verifica se o funcionário está vinculado a outra filial;
* Verifica tipo do funcionário
  + Quando Emitente ou Destinatário igual a Fornecedor Tipo não pode ser Vendedor
  + Quando Emitente ou Destinatário igual a Cliente Tipo não pode ser Comprador
  + Quando Emitente ou Destinatário igual a Empresa:
    - Tipo Vendedor só pode ser usado quando código do tipo de movimento começar com 1.
    - Tipo Comprador só pode ser usado quando código do tipo de movimento não com 1.
