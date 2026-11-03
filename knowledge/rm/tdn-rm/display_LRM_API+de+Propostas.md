---
content_hash: 8c9458283d95c78b8ca4588a419a4651f3a74da98cf774178d3909e4c62fb7a8
fetched_at: '2026-06-29T00:11:32.325423+00:00'
page_id: '746489620'
product: rm
source: tdn-rm
title: API de Propostas
type: documentation
url: https://tdn.totvs.com/display/LRM/API+de+Propostas
version: 40
---

API de Validação de VPL

| Título | **API de Validação de VPL** |
| --- | --- |
| Endpoint | [http://localhost:8051/api/imb/v1/Sales/](http://localhost:8051/api/imb/v1/Sales/20_1914/VPL)[{Cod Coligada}\_{Número da Venda}](http://localhost:8051/api/imb/v1/sales/proposals/20_1914/approval?note=Solicitar)[/VPL](http://localhost:8051/api/imb/v1/Sales/20_1914/VPL) |
| Verbo | Get |
| Parameters | no parameters |
| Descrição | API que retornar o cálculo da análise da proposta do cliente comparando com a proposta padrão, entre os indicadores a VPL.  Baixe **[aqui](https://tdn.totvs.com/download/attachments/665033766/PLANILHA%20ANALISE%20VPL%20.xlsx?version=2&modificationDate=1657125942857&api=v2)**a planilha excel com o cálculo  Para o  cálculo da VPL os campos da modalidade da proposta do TCGI → Portal do Imóveis  Ao validar a VPL  os campos da tabela  de venda e regras serão espelhados nas tabelas antigas do PI (XPIPROPOSTA, XPIPESSOA\_PROPOSTA, XPIPROPOSTACOMPOSICAOHIST)  para manter o funcionamento dos relatórios e telas antigas |
| Modalidade  da Venda TCGI |  |

Modelo Json Solicitação Geração ComissãoBodytrueModelo Json Solicitação Geração ComissãoRESPONSEtrueParâmetros do Response

Parâmetros:

* codcoligada: coligada do empreendimento;
* numvenda : Número da venda;
* valortabelaprecopadrao:  Valor da Tabela de Preço Padrão da modalidade padrão
* valortabelaprecoproposta: Valor da Tabela de Preço Padrão da modalidade padrão
* valorfinanciadoatulizadopadrao: Valor sumarizado dos componentes de Entrada e Principal da modalidade padrão
* valorfinanciadoatulizadoproposta: Valor sumarizado dos componentes de Entrada e Principal da modalidade proposta
* valorpadraovpl: Valor sumarizado das parcelas da modalidade padrão - Inclui todos os valores de todos os componentes
* valorpropostavpl: Valor sumarizado das parcelas da modalidade proposta- Inclui todos os valores de todos os componentes
* percentualtma: Percentual da TMA - Taxa mínima de atratividade. A TMA é basicamente uma taxa de desconto que representa o retorno mínimo que o investidor deseja obter.
* aprovada:  O VPL foi aprovado, true ou false
* mensagem: Proposta AProvada ou Reprovada
* log: Detalhe da mensagem quando for reprovada
* itensvpl:
  + nomeparametro: Prazo de Financiamento;
  + valortabela: Nro de Meses do componente principal;
  + valorproposta:  Nro de Meses do componente principal;
  + parametrodeaprovacao: Não valida para esse tipo de parâmetro;

* + nomeparametro: % Captação a Vista;
  + valortabela: Percentual do componente de entrada;
  + valorproposta:  Percentual do componente de entrada;
  + parametrodeaprovacao: Pode validar entre %mínimo  e %máximo, se configurado com valor na modalidade;

* + nomeparametro: % Captação até Entrega;
  + valortabela: Percentual do valor previsto para receber até a entrega;
  + valorproposta:  Percentual do valor previsto para receber até a entrega;
  + parametrodeaprovacao: Não valida para esse tipo de parâmetro;

* + nomeparametro: % Captação até 1 mês Antes Entrega;
  + valortabela: Percentual do valor previsto para receber até um mês antes da entrega;
  + valorproposta:  Percentual do valor previsto para receber até um mês antes da entrega;
  + parametrodeaprovacao: Não valida para esse tipo de parâmetro;

* + nomeparametro: % Captação até Metade da proposta em relação a Entrega da Subunidade;
  + valortabela: Percentual do valor previsto para receber até a metade do tempo que falta para entrega;
  + valorproposta:  Percentual do valor previsto para receber até a metade do tempo que falta para entrega;
  + parametrodeaprovacao: Não valida para esse tipo de parâmetro;

* + nomeparametro: Valor m2;
  + valortabela: Valor do m2 ;
  + valorproposta:  Valor do m2 ;
  + parametrodeaprovacao: Não valida para esse tipo de parâmetro;

* + nomeparametro: Valor m2 VPL;
  + valortabela: Valor do m2 com a VPL;
  + valorproposta:  Valor do m2 com a VPL;
  + parametrodeaprovacao: Não valida para esse tipo de parâmetro;

* + nomeparametro: % Arrecadação;
  + valortabela: (Valor do total financiado / Valor Tabela Preço) - 1;
  + valorproposta:  (Valor do total financiado proposta / Valor Tabela Preço Proposta) - 1;
  + parametrodeaprovacao: Pode validar entre %mínimo  e %máximo, se configurado com valor na modalidade;

* + nomeparametro: % Desconto;
  + valortabela: 1- (Valor do total original / Valor Tabela Preço) ;
  + valorproposta:  1- (Valor do total original proposta / Valor Tabela Preço Proposta) ;
  + parametrodeaprovacao: Pode validar entre %mínimo  e %máximo, se configurado com valor na modalidade;

* + nomeparametro: % Diferença do VPL;
  + valortabela: Percentual de diferença da VPL em reação ao padrão, nesse caso sempre será 0, pois é a coluna do padrão;
  + valorproposta:  Percentual de diferença da VPL em reação ao padrão,  se for maior que 0, está abaixo da tabela padrão e se for maior que 0, está acima da padrão;
  + parametrodeaprovacao: Pode validar entre %mínimo  e %máximo, se configurado com valor na modalidade;
API - Validação de Parametrização

| Título | API - Validação de Parametrização |
| --- | --- |
| Endpoint | [http://localhost:8051/api/imb/v1/registrations/validate/pi/enterprises/](http://localhost:8051/api/imb/v1/registrations/validate/pi/enterprises/2057){Cod Empreendimento} |
| Verbo | GET |
| Parameters | Não tem Parãmetros. |
| Descrição | No preenchimento da proposta existem algumas validações ( parâmetro do financeiro sequência, corretor vinculado ao Cli/for, tabela de preço para unidade, modalidade de venda parametrizada) que ajudam o corretor a não continuar a proposta caso os mesmos já não estiverem já definidos. Essa API seria facilitadora para que o corretor não preencha cada campo para descobrir que falta parametrização padrão    Api geral - Valida todos Empreendimentos :  [http://localhost:8051/api/imb/v1/registrations/validate/pi](http://localhost:8051/api/imb/v1/registrations/validate/pi "Follow link")  Api por empreendimento : [http://localhost:8051/api/imb/v1/registrations/validate/pi/enterprise](http://localhost:8051/api/imb/v1/registrations/validate/pi/enterprises/1 "Follow link")s/2057 Neste exemplo passando pelo Empreendimento 2057    Neste exemplo da API , passou pelo empreendimento 2057 e o Response mostrando as parametrizações que precisam sem feitas. |
| Parãmetros TCGI | Não tem Parãmetros no TCGI. |

Modelo Json Solicitação Geração ComissãoBodytrueModelo Json Solicitação Geração ComissãoRESPONSEtrueAPI de Solicitação de Aprovação de Proposta Reprovada

| Título | **API de Solicitação de Aprovação de Proposta Reprovada** |
| --- | --- |
| Endpoint | [http://localhost:8051/api/imb/v1/sales/proposals/{Cod Coligada}\_{Número da Venda}/approva](http://localhost:8051/api/imb/v1/sales/proposals/20_1914/approval?note=Solicitar)l |
| Verbo | Post |
| Parameters | | Key | Value | | --- | --- | | note | Informe a mensagem de observação do corretor para o supervisor | | url | Informe o endereço da web para realizar a aprovação da proposta | |
| Descrição | Api para solicitar aprovação de proposta de venda quando a mesma foi reprovada pela validação.  Ao solicitar a aprovação da proposta o sistema enviára um e-mail para o supervisor do corretor solicitadando a sua aprovação, desde que o parâmetro "Permite Forçar Proposta" esteja marcado.  Para o envio do e-mail os campos dos parâmetros do TCGI → Portal do Imóvel→ Porposta de Venda devem ser preenchidos  Baixe  **aqui** o modelo do corpo do e-mail |
| Parâmetros  do TCGI |  |

Modelo Json Solicitação Geração ComissãoBodytrueModelo Json Solicitação Geração ComissãoRESPONSEtrueAPI Aprovar Proposta Forçada

| Título | **API Aprovar Proposta Forçada** |
| --- | --- |
| Endpoint | <http://localhost:8051/api/imb/v1/sales/proposals/{Cod> Coligada}\_{Número da Venda}/forceapproval |
| Verbo | Post |
| Parameters | | Key | Value | | --- | --- | | note | Informe a mensagem de observação do Supervisor para o Corretor | | userld | Informe Id do Superior vinculado ao Corretor da Proposta | |
| Descrição | Api para forçar a aprovação de uma Proposta reprovada, caso seja aprovada pelo Superior informado no cadastro dos parametros do Corretor.  Lembrando que o parâmetro no **PI** da Proposta ( **Reprovada** ) tem que estar marcada o parâmetro - **Permite forçar proposta.**  E-mail será enviado para Superior cadastrado configurado no cadastro do Corretor no Portal de Imóveis.  Uma proposta que foi reprovada , o Corretor envia um e-mail para seu Supervisor , conforme API : **API de Solicitação de Aprovação de Proposta Reprovada**citada  no exemplo acima , essa API força que uma proposta Reprovda possa se tornar APROVADA , fazendo que o e-mail possa ser enviado alterando a proposta de Reprovada para  Aprovada.  Baixe TCGIRELPI0002 - Corpo de E-mail para Forçar Aprovação de Proposta.TotvsReport[**aqui**](https://drive.google.com/drive/folders/1Kr00Gb95kIt5QCwHsPVvJv_x4f6Cmzzf) |
| Parâmetros  do TCGI |  |

Modelo Json Solicitação Geração ComissãoBodytrueModelo Json Solicitação Geração ComissãoRESPONSEtrueAPI - Inserir - Pessoas Adicionais

| Título | API - Inserir - Pessoas Adicionais |
| --- | --- |
| Endpoint | <http://localhost:8051/rmsrestdataserver/rest/ImbPVIClienteData> |
| Verbo | Post |
| Parameters | Não tem Parãmetros. |
| Descrição | Api para tratamento para criar um Fiador.  Tabela XPIPESSOA.TIPO  Incluído esses Típos de Fiadores.  5 = Procurador 6 = Procurador Cônjuge 7 = Representante Legal 8 = Fiador    No exemplo do Código Body - Inserindo um Fiador com código **= 8 ( Fiador ) TIPO = 8**  **Cadastro de Pessoas Adicionais:**  Contrato de Venda | Anexo | Pessoas Adicionais |
| Parãmetros TCGI | Não tem Parãmetros no TCGI. |

Modelo Json Solicitação Geração ComissãoBodytrueModelo Json Solicitação Geração ComissãoRESPONSEtrueAPI - Associar Pessoa na Proposta

| Título | API - Associar Pessoa na Proposta |
| --- | --- |
| Endpoint | [http://localhost:8051/api/imb/v1/sales/proposals/](http://localhost:8051/api/imb/v1/sales/proposals/20_1914)[{Cod Coligada}\_{Número da Venda}](http://localhost:8051/api/imb/v1/sales/proposals/20_1914/approval?note=Solicitar) |
| Verbo | Put ou Post |
| Parameters | Não tem Parãmetros. |
| Descrição | API para inserir a Pessoa cadastrada na API <http://localhost:8051/rmsrestdataserver/rest/ImbPVIClienteData> em uma proposta no TCGI.    No BODY , informo :  [ { "idcliente": 4, "clienteprincipal": 1, "pessoasadicionais": [{"idpessoa": 111,"tipopessoa": 8}, {"idpessoa": 112,"tipopessoa": 7}  ]    IDPESSOA cadastrada na API Pessoas Adicionais com seu TIPO.  Ao inserir uma Pessoa Adicional via API , retorna seu ID como mostra o cadastro da API acima. |
| Parãmetros TCGI | Não tem Parãmetros no TCGI. |

Modelo Json Solicitação Geração ComissãoBodytrueModelo Json Solicitação Geração ComissãoRESPONSEtrueAPI de Usuário Portal de Imóveis

| Título | **API de Usuário Portal de Imóveis - GET** |
| --- | --- |
| Endpoint | <http://localhost:8051/rmsrestdataserver/rest/ImbPIUsuarioData> |
| Verbo | Get |
| Parameters | No parameters |
| Descrição | Utilizando esta API com o verbo Get, o sistema retorna a lista de usuários cadastrados na Tabela XPIUSUARIO do Portal de Imóveis. |
| Parâmetros  do TCGI |  |

Modelo Json Solicitação Geração ComissãoBodytrueModelo Json Solicitação Geração ComissãoRESPONSEtrue

| Título | **API de Usuário Portal de Imóveis - POST** |
| --- | --- |
| Endpoint | <http://localhost:8051/rmsrestdataserver/rest/ImbPIUsuarioData> |
| Verbo | Post |
| Parameters | No parameters |
| Descrição | Utilizando esta API com o verbo Post, o sistema irá cadastrar o usuário do Portal de Imóveis alimentando as seguintes tabelas:   * XPIUSUARIO: Tabelas que armazena os dados dos usuários do PI; * FCFO: Tabela (principal) que armazena os dados dos Clientes no financeiro; * XPESSOACONJUGE: Tabela que  armazena os dados do cônjuge dos clientes no TCGI; e * XCLIENTEPESSOAFISICA: Tabela que armazena os dados complementares dos clientes no TCGI; |
| Parâmetros  do TCGI |  |

Modelo Json Solicitação Geração ComissãoBodytrueModelo Json Solicitação Geração ComissãoRESPONSEtrue

| Título | **API de Usuário Portal de Imóveis - PUT** |
| --- | --- |
| Endpoint | [http://localhost:8051/rmsrestdataserver/rest/ImbPIUsuarioData/{ID\_do\_Usuário\_na\_XPIUSUARIO]](http://localhost:8051/rmsrestdataserver/rest/ImbPIUsuarioData/{ID_do_Usuário_na_XPIUSUARIO) |
| Verbo | Put |
| Parameters | No parameters |
| Descrição | Utilizando esta API com o verbo Put, o sistema irá atualizar os dados informados, para o usuário repassado na ID, na tabela XPIUSUARIO, que armazena os dados dos usuários do PI.  Ao utilizar este verbo é preciso informar todos os campos/tags do cadastro do usuário porque os campos que não forem informados serão setados como nulos.  Para atualizar somente um campo/tag, utilize o verbo Patch descrito mais abaixo. |
| Parâmetros  do TCGI |  |

Modelo Json Solicitação Geração ComissãoBodytrueModelo Json Solicitação Geração ComissãoRESPONSEtrue

| Título | **API de Usuário Portal de Imóveis - PATCH** |
| --- | --- |
| Endpoint | [http://localhost:8051/rmsrestdataserver/rest/ImbPIUsuarioData/{ID\_do\_Usuário\_na\_XPIUSUARIO]](http://localhost:8051/rmsrestdataserver/rest/ImbPIUsuarioData/{ID_do_Usuário_na_XPIUSUARIO) |
| Verbo | Patch |
| Parameters | No parameters |
| Descrição | Utilizando esta API com o verbo Patch, o sistema irá atualizar os dados informados, para o usuário repassado na ID, na tabela XPIUSUARIO, que armazena os dados dos usuários do PI.  Este verbo deve ser utilizado para atualizar os campos especificados, sem alterar o valor dos demais campos da tabela. |
| Parâmetros  do TCGI |  |

Modelo Json Solicitação Geração ComissãoBodytrueModelo Json Solicitação Geração ComissãoRESPONSEtrue

| Título | **API de usuário Portal de Imóveis - DELETE** |
| --- | --- |
| Endpoint | [http://localhost:8051/rmsrestdataserver/rest/ImbPIUsuarioData/{ID\_do\_Usuário\_na\_XPIUSUARIO]](http://localhost:8051/rmsrestdataserver/rest/ImbPIUsuarioData/{ID_do_Usuário_na_XPIUSUARIO) |
| Verbo | Delete |
| Parameters | No parameters. |
| Descrição | Utilizando esta API com o verbo Delete, o sistema irá excluir os dados do usuário repassado no ID, na tabela XPIUSUARIO.  No exemplo de resposta abaixo, excluímos o usuário de ID 37, criado nos exemplos acima:  <http://localhost:8051/rmsrestdataserver/rest/ImbPIUsuarioData/37> |
| Parâmetros  do TCGI |  |

Modelo Json Solicitação Geração ComissãoBodytrueModelo Json Solicitação Geração ComissãoRESPONSEtrue
