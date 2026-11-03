---
content_hash: 11a20d7a19836ac791de7e13267e553b31f35a9a8f034a7e7048cf574676b555
fetched_at: '2026-06-29T00:10:30.322636+00:00'
page_id: '519722143'
product: rm
source: tdn-rm
title: 'Ativar Integração com o Middleware (eSocial do Futuro) - Disponíveis para
  todos os clientes nas versões: 12.1.28.106,  12.1.27.172,  12.1.26.216 e superiores.'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=519722143
version: 72
---

**CONTEÚDO**

**9230true**

## **01. Visão Geral**

Direcionado para clientes que não possuem a necessidade de importar para o TAF, xmls provenientes de softwares de terceiros ou de outra linha de produtos TOTVS (ex:  
Utilizar Folha de uma linha e BackOffice de outra linha).

O objetivo é prover um serviço de entrega direta dos xml’s da Folha de Pagamento para o governo sem a necessidade de gravação dos xml’s no ambiente do TAF, facilitar a gestão de configuração e agregar relatórios gerenciais para auxiliar os usuários nas validações das entregas do eSocial.

## **02. Premissas para adesão**

Para realizar a ativação do Middleware, é necessário:

1. Não utilizar o TAF para consolidação de eventos;
2. Possuir o ambiente RM e TAF atualizados para a versão que for disponibilizada;
3. Não possuir eventos pendentes de atualização, ou seja, não pode existir eventos com o status 3 - enviado TAF e 4 - Aceito TAF na fila de eventos do RM;
4. Ter realizado a atualização do recibo de entrega dos eventos.

**IMPORTANTE:** Uma das premissas para ir para o Middleware é não utilizar consolidação de dados, inclusive SST. O cliente que utiliza o SST de outro software (terceiros) e utilizar o middleware deverão importar os XML's do SST diretamente do outro software ao governo ou não poderá utilizar o middleware, deverá permanecer no TAF Full devido essa consolidação.

**ATENÇÃO:** Esse processo é IRREVERSÍVEL, ou seja, ao realizar a ativação de integração com o Middleware, não será mais possível retornar à integração com o modo OnPremisses.

**Sendo assim, sugerimos que façam primeiramente em base de homologação com o ambiente de produção restrita, para depois colocar em ambiente de produção.**

## **03. Exemplo de Utilização**

**Ativar integração com Middleware**

Esse processo realizará a ativação e configuração inicial dos dados da integração com o Middleware.

Na tela de ativação, informe:

Dados de conexão com o Web Service Middleware: 

* Servidor onde o middleware está instalado;
* Porta de conexão com o servidor que possui o middleware instalado;
* Usuário Administrador do TAF;
* Senha do usuário administrador do TAF.

Dados de conexão com o Web Service TSS:

* URL WebService TSS.

           Para mais detalhes, acesse: <https://tdn.totvs.com/pages/viewpage.action?pageId=334334296>

* Client Id
* Client Secret

**Obs.: A autenticação estará disponível a partir do *Release* 12.1.33 do TSS.**

           Para mais detalhes, acesse: <https://tdn.totvs.com.br/pages/releaseview.action?pageId=593238229>

Dados do Certificado digital

* Tipo de Certificado Digital: Este campo permite selecionar qual tipo de certificado será utilizado para envio das informações ao eSocial.

**A1-Formato PFX (.pfx ou .p12)**

* Clique no lookup e selecione o [certificado digital](https://tdn.totvs.com/display/LRM/Middleware+-+Certificado+Digital) desejado.

**A3- HSM (Hardware Security Module)**

* slot: Número do Slot

  idHex: Id Hexadecimal. Esta informação pode ser substituída pelo campo module.

  Localização do Module:Caminho da DLL da máquina onde o certificado encontra-se instalado. Esta informação pode ser substituída pelo campo idHex. (obs: se informado, o TSS deve ter acesso ao diretório)

  label: Label do certificado digital

* Esse campo apenas é necessário quando já foram transmitidos eventos de tabela de rubricas(S-1010) através do TAF OnPremisse. Se trata do valor a ser enviado no campo “ideTabRubr”. Deve verificar no TAF o valor a ser informado nesse campo.

## **04.****Parametrizador**

Após a ativação do Middleware, sua configuração ficará disponível no parametrizador do sistema. Caso necessite atualizar os dados preenchidos no momento da ativação, basta acessar os parâmetros do eSocial, mais informações [clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=566479573)

## **05.****Limpar base de Produção Restrita do eSocial**

Executando esse processo, será enviado um comando ao ambiente de Produção Restrita do eSocial excluindo todos os eventos já enviados.

**Atenção**: Esse comando é **IRREVERSÍVEL** após a sua confirmação.

Obs.: A sua execução estará disponível apenas para o ambiente de Produção Restrita. Não executará para o ambiente de Produção do eSocial.

## **06. Integração com o BackOficce(RM Fluxus)**

Caso um trabalhador esteja cadastrado como funcionário no RM e possua lançamentos como autônomos do RM Fluxus, ao gerar os XML’s de pagamentos(S-1200/S-1210), as rubricas serão unificadas em um só XML’s para envio ao eSocial.

**Atenção:**

1. Essa situação ocorrerá apenas quando possuir integração com o Middleware. Quando não utilizar o Middleware, o sistema continua gerando dois XML’s e a consolidação será feita no TAF OnPremisse;
2. Na fila de eventos periódicos, o XML poderá ser localizado pelo código da pessoa no cadastro do funcionário;
3. Por padrão, o número do período informado(ideDmDev) nos valores referentes ao autônomo será 1. Caso possua lançamento para o funcionário no mesmo período de folha de pagamento, será necessário utilizar o parâmetro “Considerar Prefixo Período Funcionário apenas a partir da competência”,  e no cadastro do funcionário, informar um prefixo a ser gerado no XML no campo ideDmDev:

## **07.** **Relatórios de Conferência**

Ao utilizar a integração com o Middleware, serão disponibilizados relatórios de conferência de INSS/FGTS. Esses relatórios comparam o retorno que o governo nos envia nos eventos S-5001/S-5003, com o que foi calculado pelo Totvs Folha de Pagamento.

Mais detalhes desses relatórios podem ser encontrados nos links abaixo:

[Relatório de Conferência de INSS](https://tdn.totvs.com/pages/viewpage.action?pageId=536721262)

[Relatório de Conferência de FGTS](https://tdn.totvs.com/pages/viewpage.action?pageId=536720973)

## **08.** **Edição de XML's**

Processo direcionado para alterações em XML’s a serem enviados ao governo, cuja alteração direta seja a última opção como saída de contorno de possíveis inconsistências sistêmicas, e não seja possível a correção do mesmo antes do seu prazo de envio.

Mais detalhes no link abaixo:

[Edição de XML's - eSocial do Futuro](https://tdn.totvs.com/pages/viewpage.action?pageId=540888308)

## **09.** **Tabelas Utilizadas**

* PESOCIALEVENTOS
* PESOCIALTOTALIZADORES
* PESOCIALTOTAISLOTACAO

## **10.** **FAQ's**

Ainda tem dúvidas? Acesse nossas FAQ's sobre o assunto: [01.10 FAQ - eSocial do Futuro(Middleware) - RM](https://tdn.totvs.com/display/LRM/01.10+FAQ+-+eSocial+do+Futuro%28Middleware%29+-+RM)

## **11.** **WEBINAR**

Quer saber mais sobre a utilização do Middleware?  Assista o vídeo do webinar apresentado no dia [22/01/2020](https://www.youtube.com/watch?v=zfa0zJ042FU&feature=youtu.be) ou [28/10/2020](https://www.youtube.com/watch?v=hgDsmuZgfJo)

]]>
