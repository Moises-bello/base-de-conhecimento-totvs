---
content_hash: b76068361345c80e090e4337c00d83a66bd7fa0fe536c0e6fd2538004aedfefa
fetched_at: '2026-06-29T00:11:56.408739+00:00'
page_id: '865420413'
product: rm
source: tdn-rm
title: FIN - Cobrança Partilhada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=865420413
version: 19
---

A [Gestão de Shoppings](https://tdn.totvs.com/pages/releaseview.action?pageId=845754694) agora conta com o recurso de Boletos com cobrança partilhada para o banco Santander. É possível gerar um boleto de cobrança unificado para títulos de coligadas diferentes e, através da remessa bancária de cobrança partilhada, o banco faz o repasse para as contas correntes configuradas. Alguns cadastros do Gestão Financeira foram adequados para atender esta modalidade cobrança. Abaixo citamos os requisitos para o uso deste recurso no sistema.

Configurações

* Na aba 'Dados adicionais' do cadastro da [conta corrente](https://tdn.totvs.com/display/LRM/FIN+-+Conta+Corrente) é possível definir os dados da partilha, informando o código do receptor da conta corrente cadastrado junto ao banco.
* O l[ayout bancário](https://tdn.totvs.com/pages/viewpage.action?pageId=421388586), localizado nos anexos do cadastro do [banco](https://tdn.totvs.com/pages/viewpage.action?pageId=421388658), está estruturado para que seja possível informar os dados da partilha e então os dados da mesma serem lidos ao importar o arquivo de retorno de cobrança registrada. A subaba 'Partilha' é exibida na aba "Retorno de Cobrança" no cadastro de Banco que tiver o código febraban igual a '033' (Santander). Para o sistema importar os dados da partilha que estiver no arquivo bancário, esta subsba deverá ser preenchida conforme o manual bancário.
* Nos parâmetros do TOTVS Gestão Financeira, é necessário assinalar a opção "Não gerar outro boleto para lançamento após baixa parcial" em todas as coligadas envolvidas na cobrança partilhada. Esta opção se encontra no seguinte caminho: Menu 'Ambiente - Parâmetros - TOTVS Gestão Financeira - Avançar - Contas a Receber - Avançar - Etapa Baixa a Receber'. Obs: Para isto, a opção "Permitir inclusão de boleto parcial" (se encontra na etapa 'Inclusão a Receber') deve estar desmarcada.
Remessa

Para remessa de cobrança partilhada deverá ser usado o layout específico do [gerador de saídas](https://tdn.totvs.com/pages/viewpage.action?pageId=425459363) "", com os devidos tratamentos relacionados aos dados da partilha que devem ser enviados ao banco. Obs: Não houve mudança no processo de geração da remessa mas somente no layout.

Regras sobre geração de boleto parcial:

* 1 - O sistema precisa estar parametrizado para permitir a geração de boleto parcial (etapa 'Inclusão a receber' dos parâmetros do TOTVS Gestão Financeira);
* 2 - Somente boletos com apenas um lançamento podem ser gerados valores parciais;
* 3 - O valor no arquivo de remessa será considerado como sendo o valor do boleto e não do lançamento que está associado.

Regras sobre geração de Multa e Juros:

Obs.: As regras implementadas estão no manual e são aplicadas no layout citado nesta documentação.

* Regras para multa
  + Caso a multa seja um valor fixo (Campo FBOLETO.MULTA > 0)
    - Posição no Registro 1 = 075 - 075;  Valor do registro = 0;
    - Posição no Registro 1 = 076 - 088;  Valor do campo do boleto (FBOLETO.MULTA);
  + Caso a multa seja um percentual
    - Posição no Registro 1 = 075 - 075;  Valor do registro = 1;
    - Posição no Registro 1 = 076 - 088;  Valor do campo do boleto (FBOLETO.MULTADIA) multiplicado por 30. Como o sistema não trabalha com percentual fixo, foi necessário multiplicar por 30 dias;

* Regras para juros
  + Caso os juros seja um valor fixo (Campo FBOLETO.JUROS > 0)
    - Posição no Registro 1 = 161 - 161;  Valor do registro = 0;
    - Posição no Registro 1 = 162 - 173;  Valor do campo do boleto (FBOLETO.JUROS) dividido por 30, pois no manual do banco o valor de juros é diário;
  + Caso os juros seja percentual diário (Juros ao dia = Taxa)
    - Posição no Registro 1 = 161 - 161;  Valor do registro = 1;
    - Posição no Registro 1 = 162 - 173;  Valor do campo do boleto (FBOLETO.JUROSDIA) multiplicado por 30. Como o sistema não trabalha com percentual de juros mensal, foi necessário multiplicar por 30 dias, pois o banco Santander trabalha com taxa mensal;
  + Caso os juros seja valor diário (Juros ao dia = Valor)
    - Posição no Registro 1 = 161 - 161;  Valor do registro = 0;
    - Posição no Registro 1 = 162 - 173;  Valor do campo do boleto FBOLETO.JUROSDIA;
Retorno

O processo de [retorno de cobrança](https://tdn.totvs.com/pages/viewpage.action?pageId=421388703) está estruturado para utilizar a cobrança partilhada ao selecionar o tipo de retorno 'Retorno de Cobrança Registrada'. Na tela dos dados da importação, ao informar uma conta/caixa que possui o banco Santander (código Febraban '033') associado, o sistema apresenta na etapa seguinte a opção 'Cobrança Partilhada'. Ao assinalar esta opção, o sistema também processará os registros de partilha contidas no arquivo de retorno selecionado.
