---
article_id: 21490763079447
category: SIGAACD - Automação e Coleta de Dados
content_hash: 1aae3e47f3fc196af909d9551b7c2223a26a6c7ea938cdd706a70ac180a7bb96
fetched_at: '2026-06-28T22:39:13.853703+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Travamento no SIGAACD
type: support-article
updated_at: '2026-01-15T12:00:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21490763079447-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Travamento-no-SIGAACD
---

Casos de travamento no módulo SIGAACD do Protheus são geralmente causados por falhas de configuração ou artefatos incompatíveis. Recomenda-se ajustar chaves como InactiveTimeOut, ConsoleMaxSize, MaxQuerySize, testar a MultiProtocolPort, verificar latência de rede, atualizar artefatos, desativar customizações e analisar logs detalhados. Para ambientes TOTVS Cloud, enviar dados de conexão e validar portas TELNET é essencial para evitar travamentos e quedas de conexão.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21490763054999) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como devo corrigir situações de Travamento no módulo SIGAACD?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Casos de travamento no SIGAACD são frequentemente ocasionados por falha nas configurações do ambiente, ou por artefatos incompatíveis. Abaixo listamos os principais tópicos já mapeados para corrigir essas situações:

* **01** - Chave **InactiveTimeOut**

Configure a chave InactiveTimeOut conforme o boletim:  [SIGAEST - SIGAACD - É possível estabelecer a tag InactiveTimeout para ociosidade na sessão VTDEBUG?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8890844378263-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-SIGAACD-%C3%89-poss%C3%ADvel-estabelecer-a-tag-InactiveTimeout-para-ociosidade-na-sess%C3%A3o-VTDEBUG?source=search)

É recomendável nessa situação utilizar a chave indicando o conteúdo de 30 minutos (ao invés de 60 minutos).

* **02** - Chaves ConsoleMaxSize e MaxQuerySize

Configure no appserver.ini , na sessão GENERAL, as chaves conforme documentação:

* + [chave ConsoleMaxSize](https://tdn.totvs.com/display/tec/ConsoleMaxSize)=**104857600**
  + [chave MaxQuerySize =](https://tdn.totvs.com/display/tec/MaxQuerySize) **31960**

* **03** - Chave MultiProtocolPort

Realize um teste em base de Homologação, desabilitando a porta [MultiProtocolPort](https://tdn.totvs.com/pages/viewpage.action?pageId=538506039).

* **04** - Log de latência

Verifique junto a sua área de Infraestrutura o controle da sua rede de conexão e também a latência de sua rede, conforme documentação: [LatencyLog *(*](https://tdn.totvs.com/display/tec/LatencyLog)*Caso o ambiente estiver alocado no Cloud da TOTVS, verifique essa etapa com o time de Suporte Cloud).*

* **05** - Atualização e equiparação de artefatos

Essa etapa é crucial pois manter versões incompatíveis tendem a ocasionar uma série de inconsistências não previstas. Atualize o Ambiente com todos os artefatos envolvidos no processamento (atualizar em ambiente de Homologação, para validação):

* + [Acumulado SIGAEST conforme sua versão](https://tdn.totvs.com/x/2hgdHw)
  + [LIB Atual](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/) - [Logo Guará](https://suporte.totvs.com/portal/p/10098/download?e=989259) | [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1050526)
  + [Appserver](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/)
  + [Smartclient](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFSC/search/searchAll) - [Lobo Guará](https://suporte.totvs.com/portal/p/10098/download#detail/947510) | [Harpia](https://suporte.totvs.com/portal/p/10098/download#detail/1112221)
  + [DBAccess](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/)
  + [Central de Atualizações](https://suporte.totvs.com/portal/p/10098/download?e=946864#000006/368/TFSC/)

* **06** - Desative as customizações, impreterivelmente conforme os três métodos recomendados na documentação: [Linha Protheus - Como ativar e desativar customizações no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114292--Cross-Segmentos-Linha-Protheus-Como-ativar-e-desativar-customiza%C3%A7%C3%B5es-no-Protheus)

Persistindo o problema, para análise da ocorrência pelo Suporte Técnico TOTVS, é necessário encaminhar os seguintes insumos::

* **Log TraceStack:** Habilite a chave TraceStack conforme o boletim [TraceStack](https://tdn.totvs.com/display/tec/TraceStack) e envie o log;
* **Console.log:** Localize os arquivos [console.log e console.bak](https://tdn.totvs.com/display/tec/ConsoleLog) na pasta appserver. Limpar/excluir os arquivos após backup. Acessar a rotina e refazer o processo até gerar o travamento, de modo que grave as informações no arquivo console.log. Envie o arquivo gerado;
* **Inspetor de objetos:** Extraia e envie o **inspetor de objetos** do ambiente;
* **LogProfiler:** Gere o LogProfiler criteriosamente conforme a instrução: [SIGAEST - Como habilitar e gerar o LogProfiler](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019902592-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-habilitar-e-gerar-o-LogProfiler) e envie.

Caso seu ambiente esteja hospedado no **TOTVS Cloud**, enviar também os dados de conexão conforme abaixo:

* Nome do ambiente;
* ID do ambiente;
* Nome de usuário e senha (utilizar a ferramenta [**GetMyPassword**](https://getmypassword.cloudtotvs.com.br/));
* Porta de conexão do coletor;
* IP para conexão do coletor.

**07** - Caso o cliente utilize Broker para [Balanceamento de Carga](https://tdn.totvs.com/display/tec/Balanceamento+entre+cliente+Telnet+e+servidor+Application+Server) dos coletores, solicitar validação diretamente na porta do **TELNET**.  

Clientes CLOUD TOTVS solicitar a liberação da porta Externa do **TELNET** conforme o exemplo: 

**[TELNET]**  
Enable=1  
Main=SIGAACD  
Environment=produção   
Port=8600  
MaxRow=8  
MaxCol=20

O [TOTVS Broker Telnet](https://tdn.totvs.com/display/tec/Balanceamento+entre+cliente+Telnet+e+servidor+Application+Server), utilizado para uso do ACD, funciona somente como um balanceador de conexões, diferente do Broker [SmartClient Desktop](https://tdn.totvs.com/display/tec/Balanceamento+entre+SmartClient+Desktop+e+servidor+Application+Server) que segura a conexão em 90 segundos onde torna mais resiliente a comunicação entre SmartClients e TOTVS | Application Server.

O Broker Telnet não possui resiliência de conexão, estando suscetível a quebra de conexão em quaisquer oscilações de rede.

**08 -** **Travamento Balance Telnet**

Retirar a chave **STANDBY\_TIME=90** nos Brokers para que não ocorra travamento ou queda de conexão nos coletores.

**Saiba Mais:**  
[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
