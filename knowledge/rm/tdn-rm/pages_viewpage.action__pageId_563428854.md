---
content_hash: 6d0600c089e87051220cfec3106f477fccb1a818181be559d1683aba9384dddb
fetched_at: '2026-06-29T00:10:50.797570+00:00'
page_id: '563428854'
product: rm
source: tdn-rm
title: Passos para ativação do Middleware, configuração do Relatório de Conferência
  e Edição de XML
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=563428854
version: 9
---

## O que é o Middleware?

O Middleware é um serviço do TAF direcionado para clientes que não possuem a necessidade de importar para o TAF xmls provenientes de softwares de terceiros ou de outra linha de produtos TOTVS.

Seu objetivo é prover um serviço de entrega direta dos xml’s da Folha de Pagamento para o governo sem a necessidade de gravação dos xml’s no ambiente do TAF, facilitar a gestão de configuração e agregar relatórios gerenciais para auxiliar os usuários nas validações das entregas do eSocial.

falseImportante!

A ativação do Middleware é **irreversível**. Sendo assim, avalie se sua empresa se enquadra no cenário de uso e, em caso de dúvidas, entre em contato com o [suporte do eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039208694).

Versões RM e TAF que possuem o Middleware disponível:

**RM**: 12.1.26.216, 12.1.27.172, 12.1.28.106 e superiores  
**TAF**: Último pacote acumulado disponível na Central de Download

Abaixo vamos apresentar os passos necessários para a ativação do Middleware e configuração do Relatório de Conferência.

passosPremissas

Para realizar a ativação deve-se, primeiramente, atender às premissas abaixo:

* **Não utilizar o TAF para consolidação de eventos**: todas as informações necessárias para geração dos eventos eSocial devem estar no produtos da linha RM. Caso utilize softwares terceiros ou outras linhas de produto TOTVS (ex.: Datasul, Protheus, etc) que gerem dados ao eSocial, será necessário o uso do TAF Full para consolidação, não podendo utilizar o Middleware no momento;
* **Possuir o ambiente RM e TAF atualizados**: TAF atualizado com o último pacote acumulado e RM atualizado com o Patch mais atual da sua respectiva release;
* **Não possuir eventos pendentes de atualização**: não pode existir eventos na fila do RM com o status **3 - Enviado TAF** e/ou **4 - Aceito TAF**.Necessário atualizar os status antes da ativação;
* **Recibo de entrega dos eventos atualizados**: atualizar os recibos do eSocial no RM antes de realizar a ativação¹.

Todos os pacotes de atualização encontram-se disponíveis na [Central de Download](https://suporte.totvs.com/download) do portal do cliente.

As [atualizações de status](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719862) e de [recibo](https://tdn.totvs.com/pages/viewpage.action?pageId=435097908) podem ser feitas dentro do TOTVS Folha de Pagamento.

¹ Caso possua eventos na Fila Complementar, realize a [restauração](https://tdn.totvs.com/pages/viewpage.action?pageId=506143967) desses eventos antes de atualizar os recibos.

Ativação

Atendendo às premissas anteriores, o processo de ativação do Middleware poderá ser iniciado. Siga os passos abaixo:

1. No **TOTVS Folha de Pagamento**, acesse o menu **eSocial | Outros Processos | Ativar Integração com Middleware**;  
1.1. Será exibida a tela abaixo, sendo necessário o preenchimento dos campos conforme detalhamento:

• **Web Service Middleware:**  
   - **Servidor** e **Porta** de instalação do TAF: o servidor e porta do TAF podem ser validados através do parametrizador de integração com o TAF (menu Configurações | Parametrizador | eSocial | Integração com TAF) caso já utilize a integração atualmente.  
   - **Usuário** e **senha** utilizados para acesso ao TAF: importante ser um usuário administrador.

• **Web Service do TSS:**  
   - **URL WebService TSS**: link URL com servidor e porta do TSS. Dados podem ser encontrados no arquivo appserver.ini do diretório [...]TSS\bin\appserver conforme exemplo abaixo:

   URL: <http://localhost:8080>

• **Certificado Digital**: arquivo certificado utilizado para transmissão ao governo. Serão aceitos certificados nos formatos \*.pfx ou \*.p12.  A partir dos Patches 12.1.27.274, 12.1.28.188 e 12.1.29.112 deve ser seguido o procedimento abaixo para importação do Certificado Digital:  
[Middleware - Certificado Digital](https://tdn.totvs.com/display/public/LRM/Middleware+-+Certificado+Digital)

• **Identificador da tabela de rubricas utilizado pelo TAF**: esse campo apenas é necessário quando já foram transmitidos eventos de tabela de rubricas (S-1010) através do TAF OnPremisse (TAF padrão). Deve-se verificar no TAF acessando o menu "Atualizações | Eventos eSocial | Tabelas | Rubricas", verificando o a coluna "Iden.Tab Rub". O dado também poderá ser validado através da tabela C8R, verificando a coluna "C8R\_IDTBRU".

Sugerimos sempre realizar o teste conexão também através do Browser, conforme exemplos abaixo:

TAF: http://localhost:8081/restTSS: http://localhost:8080/ 

Ao concluir a ativação com êxito, será possível visualizar as informações através do menu Configurações | Parametrizador | eSocial | Integração com Middleware:

Relatórios de Conferência e Edição de XML

Após concluir a ativação do Middleware, será necessário realizar mais algumas configurações para utilização dos relatórios de conferência e também para edição do XML no RM. Siga os passos abaixo:

1. Realize a configuração do DefaultDB no config do Host. Informações em: [Configurando DefaultDB](https://tdn.totvs.com/display/LRM/Configurando+DefaultDB);

2. Acesse o menu Configurações | Parametrizador | eSocial | Integração com Middleware e selecione a aba Outros Parâmetros;

2.1. Preencha os dados de Relatório de conferência conforme orientações abaixo:

 

• **Servidor API**  
   - **Servidor** e **porta** onde o serviço de API"s RM está sendo executado. Esta informação pode ser encontrada dentro dos arquivos RM.Host.exe.config e RM.Host.Service.exe.config, através da TAG **ApiPort.**Quando a ApiPort não estiver discriminada nos configs do Host, informar na Porta API o mesmo valor da porta APP. Quando estiver discriminada, deve possuir uma porta diferente da HttpPort.  
  
• **Servidor APP**  
   - **Servidor** e **porta** onde o aplicativo THF está sendo executado. Esta informação pode ser encontrada dentro dos arquivos RM.Host.exe.config e RM.Host.Service.exe.config, através da TAG **HttpPort**. 

***Obs.:** Quando utilizar DNS, **não deverá** ser informado o trecho "http://" ou "https://" no campo **Servidor**. Exemplo: DNS "http://teste.rmcloud.com.br", informar no campo somente "teste.rmcloud.com.br".*

Veja exemplos das tags

 Se estiver executando o **RM.Host.exe** o mesmo deve ser executado como **administrador**.

Para mais informações sobre ApiPort e HTTPPort acesse:  
     • [O que é e como configurar a HttpPort e ApiPort?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044519633)

Sugerimos realizar testes para validação se o servidor e porta estão acessíveis conforme exemplos abaixo:

Teste API (ApiPort)

[http://servidor:porta/api/swagger/ui/index#/](http://servidorporta)

Teste APP (HttpPort)

[http://servidor:porta/wspageindex/](http://servidorporta)

Importante

Nas versões e *patches* iguais e superiores a 12.1.28.147, 12.1.27.237 e 12.1.26.255 é imprescindível a execução do sistema **RM.Atualizador.exe** para a criação da tabela **PESOCIALTOTALIZADORESAUTONOMOS**, que será utilizada no relatório de conferência de INSS para comparação dos autônomos cadastrados no TOTVS Gestão Financeira ou autônomos externos. 

A partir da 12.1.29 não é necessário executar o RM.Atualizador.exe.

Os **relatórios** podem ser acessados através do menu eSocial | Conferência INSS/FGTS:

Para mais detalhes sobre os relatórios de conferência, acesse:

• [Middleware - Relatório de Conferência de INSS](https://tdn.totvs.com/pages/viewpage.action?pageId=536721262)  
• [Middleware - Relatório de Conferência de FGTS](https://tdn.totvs.com/pages/viewpage.action?pageId=536720973)

Já a **edição de XML** estará disponível dentro da Fila de Eventos, conforme print:

Para mais detalhes sobre a edição de XML, acesse:

• [Middleware - Edição de XML's](https://tdn.totvs.com/pages/viewpage.action?pageId=540888308)
