---
content_hash: bd94de97535fc138eddf80dad464a511c881bf5239c33ed435b31ba28a8a4e85
fetched_at: '2026-06-29T00:06:25.709715+00:00'
page_id: '224443860'
product: rm
source: tdn-rm
title: Manual Instalação Proxy Mashup
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224443860
version: 151
---

# Índice:

---

.\*ndice:

# Objetivo:

---

Fornecer ao usuário um manual para a instalação do Proxy Mashup.

# Introdução:

---

O serviço de Proxy do TOTVS Mashups deve ser utilizado para transferir a lógica de execução dos Mashups do Servidor TOTVS para o ambiente local onde estiver instalado.

# O Problema:

---

Atualmente, toda a lógica de execução do TOTVS Mashup é baseada em um servidor hospedado no Data Center da TOTVS, por este motivo, toda a comunicação com os sites de terceiros é feita a partir da rede da TOTVS, o que em alguns casos, causa um bloqueio de IPs devido ao alto número de requisições vindos da mesma rede.

# A Solução:

---

Com o serviço de Proxy, toda a comunicação com os sites de terceiros será feita diretamente da rede local. O serviço irá fazer a comunicação com o servidor TOTVS somente para carregar a lógica de execução do Mashup e para a validação do usuário, assim quando o Mashup for atualizado no servidor, automaticamente será atualizado no Proxy. Com esta solução iremos diminuir o número de requisições vindos do mesmo IP e consequentemente diminuir as chances de bloqueio.

# Pré-requisitos:

     Antes de realizar o processo de instalação do Proxy Mashup , é necessária instalar o pacote Redistribuível do Visual C++ para Visual Studio 2013 de acordo com sua arquitetura (vc\_redist.x64.exe ou vc\_redist.x86.exe ), disponível na página da Microsoft.

     O serviço deverá ser instalado em uma máquina Windows conforme homologado em nossa *[portabilidade](https://tdn.totvs.com/x/XDVNDQ) (Item 03 da portabilidade)*, 64 Bits, com suporte a .NET Framework 4.0, com pelo menos 4 GB de RAM e 4 núcleos de processamento. Ele deverá ter permissão de saída para internet sem necessidade de proxy. Também comunicará em qualquer porta com qualquer site, utilizando os protocolos HTTP e HTTPS.

# Instalação:

---

      Para instalar o serviço, execute o instalador **TOTVSMashups.Setup.exe** com um usuário com privilégios de administrador.

      Este instalador se encontra em: <http://mashups.totvs.com.br/> link [Proxy](http://mashups.totvs.com.br/TOTVSMashups.Setup.zip).

      Por padrão o serviço irá utilizar a porta 8055 para comunicação, o instalador deve liberar automaticamente a porta padrão no Firewall do Windows. Para testar se o serviço está funcionando corretamente, acesso pelo browser o seguinte endereço: <http://localhost:8055/TOTVSSoa.Host/SOAManager.svc>

      Deverá ser apresentada a seguinte página:

      

Observação

Caso a página não seja exibida, verifique se o serviço **TotvsSOA Proxy Service** está iniciado nos serviços do Windows. Se não estiver, inicie-o.

# Configurando o ERP:

---

 

ERP ProtheusfalseProtheusERP Protheus

      Para validação dessa alteração, será necessário que os fontes estejam com as seguintes datas:

APCFG10l.PRW com data igual ou superior a 05/10/2015.

FWSendSMS.PRW com data igual ou superior a 05/10/2015

      Caso não esteja, será necessário a aplicação do último pacote de lib liberado no portal para download. A atualização irá liberar a configuração DEFAULT do endereço do Mashup através do parâmetro **MV\_URLMSHP**.

      Com o pacote aplicado, ir até o configurador do PROTHEUS e criar o parâmetro **MV\_URLMSHP**, este parâmetro é do tipo caracter, e terá o conteúdo de acordo com o endereço da máquina onde foi instalado e configurado o proxy do Mashup (meu\_servidor\_mashup:8055). Poderá ser utilizado também o endereço IP ou nome da máquina onde o serviço foi instalado, na porta 8055.

      Ex.: <http://localhost:8055/TOTVSSoa.Host/SOAManager.svc>.

Observação

Para maiores detalhes sobre este tópico favor contatar o Suporte do Protheus.

ERP RMfalseRMAcesso

      Para configurar o servidor do Mashup no RM, acesse o Menu Processos / Mashups / Gerenciar da tela em que quiser configurar o Mashup.

      Exemplo: tela de Cadastro de Cliente/Fornecedor.

Tela do Mashup

      A tela do TOTVS Mashup será aberta:

Configure o Servidor como localhost:8055, informe o **usuário** e **senha** do **Mashups**.

Caso já esteja configurado

      Caso já estiver configurado, deverá alterar as configurações conforme abaixo (botão superior direito da barra de ferramentas, alterar conexão ao servidor de mashup):

Vídeo

      A seguir, um vídeo que demonstra os passos da configuração no RM além de um exemplo de utilização do Mashups.

divs

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.5 ou Superiores

false

**Processo:** Manual de Instalação Proxy Mashup

falsefalse

**Status:** Finalizado

false

**Data:** 19/07/2016

false

**Autores:**
