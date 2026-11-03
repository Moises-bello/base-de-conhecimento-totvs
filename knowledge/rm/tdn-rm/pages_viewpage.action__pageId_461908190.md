---
content_hash: c6790cf20af20d3839567b817c85ab1ce037837bcb91f81202df7f35a1c10ea1
fetched_at: '2026-06-29T00:10:14.513869+00:00'
page_id: '461908190'
product: rm
source: tdn-rm
title: 11.20.0 (Estoque, Compras e Faturamento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=461908190
version: 3
---

**Inventário por número de série**  
A partir desta versão é possível realizar um controle de inventário de produtos que trabalham com número de série. Sendo assim, o recurso de inventário passa a contemplar todos os tipos de estoque de produto (estoque simples, lote, grade numerada e número de série).

**Associar o tipo de frete na visão do contrato**

Ao acessar o menu Contratos, Manutenção de contratos e logo em seguida edita-lo o sistema permite informar o Tipo de Frete na aba Outros Dados, onde ao faturar o contrato foi verificado que o movimento gerado carrega os dados da transportadora. Desde que o tipo de movimento gerado pelo contrato esteja parametrizado para editar o tipo de frete.

**Aprimorado o cadastro de Funcionário/Vendedor, otimizando a seleção e associação de pessoas ao cadastro**Nesta versão, o sistema foi aprimorado para que o cadastro de Funcionários/Vendedores utilize recursos otimizados na seleção e associação de Pessoas à este cadastro, facilitando a usabilidade do sistema e garantindo vínculos adequados à utilização de recursos em movimentações de Compras e Vendas no sistema.

**Consistência no módulo de inventário**

Criada uma consistência para que o inventário não permita apurar diferença do saldo do produto selecionado e também não permita encerrar o mesmo caso o recalculo do saldo esteja desatualizado.  
***Observação***: Criação dos campos RECALCSALDO 1 a 10 na tabela TPRD onde caso o campo esteja preenchido = 1 o sistema não permitirá realizar a apuração do inventario do produto associado.  
Ao realizar o processo de Regeração de saldos e custos o sistema automaticamente preenche o campo RECALCSALDO = 0 permitindo assim a apuração do inventario.

**Consistências para inclusão no cadastro de transportadora**  
Será possível configurar através do botão direito, defaults para os campos do cadastro, assim como aqueles que serão de preenchimento obrigatório.

**Melhoria no campo NUMERO do cadastro de transportadoras**

Realizada uma melhoria no cadastro de Transportadoras, para que possa aceitar caracteres no campo 'NUMERO'. Com isto, cadastros como 'S/N' (Sem Número) pode ser utilizado a partir de então.

**Local de Estoque**  
Implementado nesta versão a possibilidade de inativar um determinado local de estoque; com isto, o mesmo não ficará disponível para movimentações.

**Disponibilizado o recurso de filtro por status do produto (Ativo/Inativo) na consulta de saldos e custos**  
O sistema passa a permitir que o Usuário possa efetuar um filtro, na Consulta de Saldos e Custos, para a identificação de Produtos inativos, evitando perda de tempo na análise de informações dos produtos que não mais são movimentados pela empresa.

**Consistências para inclusão no cadastro de transportadora**  
Será possível configurar através do botão direito, defaults para os campos do cadastro, assim como aqueles que serão de preenchimento obrigatório.

**Procedência da mercadoria**  
No cadastro de produtos, detalhes | outros dados, foram alterados os nomes dos campos referentes à procedência da mercadoria para “Ref. (0-99)” e “Descrição”. E ao digitar no primeiro campo 0, 1 ou 2, o campo “Descrição” será preenchido automaticamente com “Nacional”, "Estrangeira adquirida via importação direta" e "Estrangeira adquirida mercado interno" respectivamente.

**Ordem dos movimentos ao regerar Ficha Física-Financeira**  
Foi excluído o parâmetro “Ordem de inclusão/alteração do movimento” do campo “Ordem dos movimentos ao regerar Ficha Física-Financeira” nos parâmetros de gestão de estoque, etapa custos.

**Outras atualizações:**

Atualização nas consistências do campo CODIGOEX no cadastro de produto, sendo que este deve ser numérico e conter 2 ou 3 algarismos.  
Atualização na inclusão de funcionários com valores atrelados.  
Atualização no tamanho do campo complemento para 60 caracteres nos Cadastros de Representante, Transportadora, Fabricante, Local de Estoque e na aba CTRC do movimento.  
Atualização na inclusão de meios de pagamento com defaults contábeis utilizando conta com rateio gerencial.  
Atualização na visão dos campos complementares e utilização de tabelas dinâmicas atreladas aos campos incluídos.  
Atualização no agrupamento dos rateios de acordo com a natureza orçamentária/financeira de movimentos gerados através do módulo de contratos.  
Atualização na cópia de produtos entre coligadas que utilizem natureza orçamentária.  
Atualização no tamanho do campo bairro para 80 caracteres nos cadastros de representante, transportadora, fabricante, local de estoque e na aba CTRC do movimento.  
Atualização no comportamento do anexo log de produtos.  
Atualização na importação de movimentos utilizando o campo SUBSERIE.  
Atualização na cópia de produtos entre coligadas, no qual este já existe na coligada de destino.  
Atualização na visualização das filiais de cada coligada.  
Atualização nas consistências executadas ao parametrizar um movimento com integração com o TOTVS Gestão de Pessoas.  
Atualização no acesso as permissões de "Voltar ao status de separação anterior" quando usuário não é supervisor.  
Atualização no processo de cópia de permissões em tipos de movimento e no anexo permissões em tipos de movimento no cadastro de usuários.  
Atualização na visão da filial de destino quando o movimento é do tipo empresa/empresa.  
Atualização na impressão do Quadro Comparativo Simples do Módulo de Cotação.  
Atualização nas consistências para o cancelamento de movimentos originários do TOTVS Gestão de Obras e Projetos.  
Atualização nas consistências para definição do código do Local de Estoque de acordo com o que foi definido na parametrização.  
Atualização na visão das telas dos cadastros de tributos, IRRF e exercício fiscal. (1881812)  
Atualização na visão da tela do cadastro de eventos contábeis quando acessado de uma nova coligada.  
Atualização na seleção de coligadas para execução do processo de cópia de tipo de movimento no parametrizador.
