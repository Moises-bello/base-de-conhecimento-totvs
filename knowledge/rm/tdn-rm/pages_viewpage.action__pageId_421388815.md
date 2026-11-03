---
content_hash: a4a8b31384b418af91e4ed33ac672f9aeae5687a77a32357ddefa8a79698b968
fetched_at: '2026-06-29T00:09:19.193650+00:00'
page_id: '421388815'
product: rm
source: tdn-rm
title: Dados Bancários de Cliente/Fornecedor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388815
version: 13
---

LGPD - Lei Geral de Proteção de Dados

Informamos que possui dados pessoais contidos nesta entidade. Foram colhidos para geração de rotinas financeiras.

Para mais informações sobre a LGPD e as soluções oferecidas pela TOTVS consulte nossa página neste link ([https://tdn.totvs.com/pages/releaseview.action?pageId=514427789](https://tdn.totvs.com/pages/releaseview.action?pageId=514427789 "Follow link")).

Através deste módulo você pode cadastrar diversos dados bancários para serem utilizados na edição de lançamentos financeiros do Cliente/Fornecedor.  
Na janela principal é possível visualizar de forma simplificada, informações de um ou de vários dados bancários. Você define quantos e quais dados bancários serão apresentados, criando filtros através do Gerenciados de Filtros (localizado na Barra de Ferramentas). Ao executar um filtro cada dado bancário será apresentado em uma linha e as informações em colunas.

**Dicas**

É possível selecionar um dado bancário para ser apresentado por default na edição de um novo lançamento. Para isso, selecione o dado bancário desejado no campo "Dados Bancários", no anexo "Defaults de Clientes/Fornecedores" (pasta Outros Dados).

A permissão para visualização de informações ou realização de processos deste módulo pode ser configurada por usuário ou por perfis, no cadastro de Segurança (menu Cadastros).   
Na inclusão de um novo dado bancário é possível que alguma informação já seja apresentada por default, para isso, edite um cadastro já existente, clique com o botão direito do mouse sobre a informação desejada, posicione o cursor do mouse sobre a opção "Valor Default" e clique sobre a informação.

As informações de alguns campos podem ser obrigatórias, para isso, clique com o botão direito do mouse sobre o campo e clique sobre a opção "Preenchimento Obrigatório".  
Ao clicar sobre o nome de algumas informações a janela de edição do cadastro da informação é apresentada.

**Identificação**

Nesta pasta são apresentadas informações sobre a identificação do dado bancário.

Ativo  
Se o dado bancário estiver "inativo" ele não poderá ser selecionado em nenhum cadastro que possua o campo dados bancários.

Forma de Pagamento  
  
Se a forma de pagamento definida no fornecedor for "PIX QR-Transferência", é necessário informar o Banco, Agência e Conta.  
  
Se a forma de pagamento definida no fornecedor for "PIX QR-Code", é necessário informar o Banco e o QR-Code PIX no respectivo lançamento financeiro.  
  
Se a forma de pagamento selecionada for "Doc", "TED CIP" ou "TED STR", é necessário informar os dados complementares, ou seja, se é do tipo C ou D e também o código de finalidade.  
  
Se a forma de pagamento definida no fornecedor for "Título de Cobrança (Boleto)", é necessário informar o IPTE ou o Código de Barras no respectivo Lançamento Financeiro.

Código Finalidade  
Varia de banco para banco – ver manual de pagamento do referido banco.

Doc - Documento de Ordem de Crédito  
No sistema bancário, define autorização de crédito a ordem, de um banco a outro, para transferência de moeda escritural em conta corrente, sem emissão de cheque. O DOC permite abertura imediata do crédito, o que consiste numa vantagem sobre o cheque, por evitar o prazo da compensação. Os recursos são disponibilizados para o favorecido, para saque, no dia útil seguinte.

TED – Transferências Eletrônicas Disponíveis

Os recursos são disponibilizados para o favorecido, para saque, no mesmo dia. Dados Complementares Tipo C = transferência efetuada para conta de terceiros. Tipo D = transferência efetuada para conta de mesma titularidade.

Chave PIX e Tipo Chave PIX

Em preparação às evoluções previstas para os processos de pagamento através do PIX, foram criados os campos para registro da Chave PIX e do Tipo de Chave PIX no cadastro de dados bancários de Cliente/Fornecedor. *Disponíveis desde a versão 12.1.28, com script específico.*

**Tratamento do Registo "B" padrão FEBRABAN CNAB 150 para Débito Automático.**

Para facilitar o tratamento de Débito Automático, sem a necessidade do cadastramento manual dos "**Dados Bancários**" foi implementado no sistema o tratamento do registro "B", onde serão tratadas essas informações na inclusão ou exclusão de optantes pelo débito em conta corrente.

Criado na tabela FCFO os campos IDCFO e DIGVERIFICDEBAUTOMATICO, onde serão armazenadas informações sobre o identificador e o dígito verificador do identificador para Débito Automático, conforme orientação do manual do CNAB 150 da Febraban. Esse dígito verificador será calculado também na inclusão do Cliente / Fornecedor, junto com a geração do identificador.

**Alteração Global de Dados Bancários**

Neste anexo serão exibidos os registros de dados bancários vinculados ao cliente/fornecedor global cadastrados na coligada corrente e em outras. O processo de alteração global estará disponível quando a permissão por perfil "Editar Dados Bancários do Cliente/Fornecedor" ativa.
