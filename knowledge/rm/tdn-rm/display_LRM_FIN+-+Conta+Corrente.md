---
content_hash: d6c6055b755aad95392bde94342c0349cd0c4d45de61e98b428e4ef4de1ed388
fetched_at: '2026-06-29T00:09:19.332197+00:00'
page_id: '421388841'
product: rm
source: tdn-rm
title: FIN - Conta Corrente
type: documentation
url: https://tdn.totvs.com/display/LRM/FIN+-+Conta+Corrente
version: 9
---

Através deste módulo você pode controlar várias contas bancárias para serem utilizadas em processos de integração bancária. Na janela principal é possível visualizar de forma simplificada, informações de uma ou de várias contas correntes. Você define quantas e quais contas serão apresentadas, criando filtros através do Gerenciador de Filtros (localizado na Barra de Ferramentas). Ao executar um filtro cada cadastro é apresentado em uma linha e as informações em colunas.

**Dicas**

A permissão para visualização de informações ou realização de processos deste módulo pode ser configurada por usuário ou por perfis, no cadastro de Segurança (menu Cadastros).

Ao clicar sobre o nome de algumas informações a janela de edição do cadastro da informação é apresentada.

Você pode definir quais as colunas que serão apresentadas na janela de visão dos registros, utilizando a funcionalidade "Configurar Colunas", ícone localizado na barra de ferramentas.

**Identificação**

Nesta pasta são apresentadas informações sobre qual banco e agência a conta corrente pertence. Informações sobre alguns campos: Global Com esta opção marcada o cadastro da conta corrente pode ser visualizado através de todas as coligadas.  
Esta opção estará disponível para edição apenas se o parâmetro "Permite Globais" (Assistente de Implantação de Processos | processo Lançamento | etapa Cliente/Fornecedor) estiver marcado.

Banco

Além de selecionar um banco é possível "visualizar", "incluir", "editar" e "excluir", cadastros de bancos e agências.

Agência

Associe um código de agência vinculado ao Banco definido no campo anterior.

Conta

Os caracteres a serem utilizados para definir a conta dependerão da configuração do campo "Máscara de Conta Corrente" (localizado no cadastro do Banco).

**Dados Adicionais**

Nesta pasta são apresentadas informações adicionais ao cadastro da conta corrente.

Tipo

Defina o tipo da Conta: Conta Corrente ou Poupança

Dados da partilha (apenas para o Banco Santander - Febraban 033)

Código do receptor. Informe o código do receptor cadastrado no sistema de cobrança do Banco Santander junto com a respectiva agência e conta para crédito da partilha. Esta informação será utilizada na remessa de cobrança partilhada (multicoligada).

**Observação**

Deve se estar sempre atento às modificações realizadas pelos bancos nos seus respectivos layouts. O sistema trabalha com as informações contidas nos layouts bancários, portanto, se o banco alterar/implementar alguma informação, o sistema deverá ser novamente parametrizado com estas novas informações. Cada banco pode alterar a forma de sua geração e tais informações competem ao próprio manual do Banco.

 Veja também

* [Chave PIX](https://tdn.totvs.com/x/uSEFIg)

Chave PIX

Através deste anexo pode cadastradas as chaves PIX vinculadas a conta corrente, que serão utilizadas nos processos de integração bancária.

**Identificação**

Nesta pasta são apresentadas informações sobre a chave PIX

Chave

É a chave PIX vinculada a conta corrente.

Ativo

Indica se a chave está ativa ou não.

Tipo

Tipo da chave. Com as seguintes opções: Telefone, Email, CPF, CNPJ ou Chave Aleatória.

Principal

Indica se a chave é a principal ou não. Sendo possível somente uma chave principal por conta corrente.
