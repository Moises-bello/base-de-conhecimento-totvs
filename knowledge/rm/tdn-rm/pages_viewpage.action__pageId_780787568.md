---
content_hash: 8621b51644fdc749c108bd8d6b443c8d8c58fe1690d0400b0b248a918d6dcac0
fetched_at: '2026-06-29T00:11:37.972501+00:00'
page_id: '780787568'
product: rm
source: tdn-rm
title: TCGI - Carteira de Cobrança
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=780787568
version: 1
---

**Cobrança| Carteira de Cobrança**

Com a carteira de cobrança será possível criar perfis de cobrança. O perfil é criado considerando a régua definida e o filtro utilizado.

* A régua será utilizada para automação da carteira de cobrança, caso a carteira não seja automatizada o campo deve ficar sem preenchimento.

##### Criando o Filtro:

Para criar um novo filtro é necessário inserir/editar uma carteira, é clicar na opção **Selecionar o Filtro da carteira**(...), neste momento o sistema irá abrir uma visão de **Filtro de Carteira**, primeiramente será necessário criar/selecionar o filtro no menu superior da visão, após selecionar o filtro e executar é necessário clicar na opção **Selecionar Filtro** no rodapé da visão. Em seguida basta salvar a carteira que o filtro está aplicado.

* Será possível criar os filtros utilizando campos das tabelas FCFO ou XCOBRANCA.
* Ao utilizar mais de 1 carteira é importante que os filtros estejam alinhados para que a cobrança seja gerada na carteira correta, por exemplo, na carteira 2 existe um filtro CODCFO = "A123", na carteira 1 deve ter um filtro CODCFO <> "A123". Caso não exista essa combinação ao executar o processo de gerar a cobrança a carteira 1 irá gerar a cobrança para o cliente/fornecedor "A123".
* Para validar o retorno dos filtros criados é preciso possuir registros na tabela XCOBRANCA, sendo assim pode ser executado o processo de Gerar Cobrança para que as cobranças sejam criadas, com isso ao criar e executar o filtro será possível ver exatamente quais registros o filtro irá contemplar, ao concluir a criação dos filtros basta ir na **Visão de Cobrança**e executar o processo de **Alterar a****Carteira****de Cobrança**. Após isso as novas cobranças serão automaticamente criadas para a carteira correta.
* É possível criar filtros usando consulta SQL:

  | O exemplo a seguir retorna os contratos de Venda vinculados ao Empreendimento com o código 2007.  SELECT XCOBRANCA.CONTRATO FROM XCOBRANCA JOIN XVENDA ON XCOBRANCA.CONTRATO = XVENDA.NUM\_VENDA AND XCOBRANCA.CODCOLIGADA = XVENDA.CODCOLIGADA WHERE XVENDA.COD\_PESS\_EMPR = 2007 AND XVENDA.CODCOLIGADA = 1    Link com maiores informações sobre o procedimento: [Melhorando Performance de filtro com SQL](https://tdn.totvs.com/display/LRM/Melhorando+Performance+de+filtro+com+SQL) |
  | --- |

**Mais sobre Carteira de cobrança**

Sobre a C.C , esta funcionalidade vai dizer qual regua de cobrança será utilizada e qual automação **- Não é obrigatória -**  pois pode-se fazer tudo manual , não necessáriamente é preciso ter uma régua de cobrança. Mas ela vai ajudar a disparar as ações da cobrança . **Essa Carteira de Cobrança é um Agrupador.**

**Exemplo:**

Cliente quer trabalhar com **2 Perfis diferentes para Carteira de cobrança**.

## **Perfil de Analista de Atendimento Junior** e um outro **Perfil de Analista Senior.**

Como pode separar ambos perfis ?

# **Analista de Atendimento Junior :** Exemplo - serão feitas cobranças de até 60 dias de atraso.

Criar um Filtro - Basta clicar no 

Neste filtro , foi criado para Analista Junior com até 60 dias de atraso.

Foi encontrado um lançamento com até 60 dias de atraso.

Ao clicar em Visão de Cobrança - Cód da Carteira encontra-se em Branco , para preencher o campo Cód da Carteira - Processos | Gerar Cobrança.

Em visão de Cobrança foi preenchido o Código da Carteira com a Carteira criada com o Filtro ( Analista Junior até 60 dias ) Corretamente.

# **Analista de Atendimento Senior :** Exemplo - serão feitas cobranças acima de 60 dias.

Filtro criado para pegar lançamentos acima de 60 dias em atraso.

Filtro aplicado e sistema mostra neste exemplo os lançamentos acima dos 60 dias para o Filtro de Analista Senior.

Filtro criado com código Carteira = 4

Dias em atraso : Como pegar esse número 305 dias de atraso por exemplo ?

É o lançamento mais antigo em atraso deste contrato em especifico. O Lançamento mais antigo em atraso do contrato 2567 por exemplo , encontra-se com 305 dias em atraso.

Gerar cobrança em seguida.

Preenchido o código da Carteira na vsião de cobrança com o a Carteira criada para o Perfil ( Analista Senior ) Acima dos 60 dias de atraso.

Campo : **Contrato Externo** - É o numero do contrato cadastrado em Venda / Aluguel.

Régua de Cobrança na Carteira.

Ao informar a **Régua de Cobrança** na Carteira, passa ser **automatizada a cobrança** , seguindo os passos da Régua de cobrança , e deixando em **branco esse campo** , se torna manual.

# **Exemplo com Régua inserida dentro da Carteira de Cobrança:**

Na tela de Visão de atendimento , é informado o número de dias de atraso, neste exemplo tem o lançamento com **( 122 )** dias em atraso.

Cadastro da Régua de Cobrança - Primeiro Nível , observe que o envio de SMS encontra-se cadastrado para ser enviado quando chegar em **122 dias** de atraso.

No cadastro da Carteira , inserido o código da Régua.

Visão da Cobrança - Gerar cobrança.

Processo executado com sucesso

SMS enviado para o celular do Cliente.

Histórico informa todos processos de cobrança na visão deste cliente , erros e sucessso ao enviar.
