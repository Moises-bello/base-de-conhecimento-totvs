---
content_hash: 372dbbae2f5ee198df27a30e653dce5abb5122aebcb4a1694e176d9a9bf01019
fetched_at: '2026-06-29T00:08:30.948819+00:00'
page_id: '272706466'
product: rm
source: tdn-rm
title: ER_FRW_FRW002-259_ReliableSession
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_FRW_FRW002-259_ReliableSession
version: 114
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | WCF |
| **Segmento Executor** | Framework | | |
| **Projeto1** | Framework BH - 004 | **IRM/EPIC1** |  |
| **Requisito/Story/Issue1** | FRW\_FRW002-259 | **Subtarefa1** | FRW\_FRW002-261 |
| **Chamado/Ticket2** |  | | |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### Objetivo

Atualizar as rotinas base de comunicação WCF para trabalhar com Reliable Session.

Com Reliable Session, o RM estará preparado para trabalhar com Buffer no envio de pacotes e de manter a conexão de um serviço viva por mais tempo para reaproveitar as novas chamadas. Desta forma, evita-se novos handshakes e aspira-se um ganho de performance em cenários onde a comunicação do client com o server tenha uma latência muito alta.

O RM deverá saber trabalhar com e sem Reliable Session ao mesmo tempo, decidindo através da verificação da latência no processo de comunicação.

Esta solução foi desenhada para cenários que envolvam serviços em Cloud.

### (Obrigatório)

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Novo Endpoint no Host | [Criação] |  | Para se trabalhar com Reliable Session e Sem Reliable Session ao mesmo tempo, o RM deverá trabalhar com dois Endpoints distindos no Host, cada qual escutando por uma porta diferente. A porta para o novo Endpoint será considerada como o valor da porta padrão somados mais 100. Exemplo: Port: 8050 / ReliablePort: 8150 |
| Canal Único WCF | [Criação] |  | Com um Endpoint criado exclusivamente para atender as chamadas com Reliable Session, é necessário criar uma Interface de Serviço que sirva de Gateway entre o client e os Serviços originais do RM. Este Gateway será o único serviço consumido pelo client em todas as chamadas com Reliable Session, enviando como parâmetro os dados do serviço original para serem resolvidos no lado do servidor pelo host |
| Gerar Proxy Dinâmico para os Serviços RM | [Criação] |  | Todo serviço RM que for chamado através de uma Reliable Session, deverá antes passar pelo Gateway. Para isto, será necessário criar uma classe que implemente as interfaces de serviço originais e que herde de uma classe proxy base. Em cada chamada, direcionar os dados que configuram aquela chamada para a classe proxy base que fará a comunicação com o Gateway para garantir um único canal |
| Resiliência do RM para comunicação com os Endpoints Reliable e Não Reliable | [Criação] |  | Caso uma chamada com Reliable Session seja realizada e falhe, identificar o motivo da falha de comunicação com o Endpoint Reliable para decidir se tenta mais uma vez ou se realiza a chamada clássica sem Reliable Session no Endpoint padrão |
| Configuração para definir o comportamento do client | [Criação] |  | Criar chaves de configuração para o client, definindo como tag o nome EnableReliableSession com as seguintes opções:   * Auto: O RM identifica através da latência, se deve utilizar Reliable Session em um determinada chamada, ou não. Este valor é considerado o novo padrão RM * OnlyReliable: O RM não testa mais a latência do client com o server e sempre usa Reliable Session * DisableReliable: O RM não testa mais a latência do client com o server e sempre usa a chamada clássica sem Reliable Session   Exemplo de uso (No arquivo RM.exe.config):   <add key="EnableReliableSession" value="Auto" /> |
| Outras chaves de configuração para se trabalhar com ReliableSession | [Criação] |  | Existem algumas chaves de configuração que sobrescrevem o comportamento padrão do RM para se trabalhar com alguns recursos. São estes:   * ReliablePort: Esta tag permite que a porta do RM destinada para se trabalhar com Reliable Session seja sobrescrita do comportamento padrão descrito no item **Novo Endpoint no Host** e assuma o novo valor informado. Esta tag só poderá ser utilizada no arquivo **RM.exe.config**. Exemplo:   <add key="ReliablePort" value="5568" />   * ReliableSessionSendTimeout: Esta tag define o tempo em segundos para envio de pacotes. Por padrão o RM considera esta opção com o valor infinito (0 - zero) e caso ela seja utilizada, este novo valor será considerado para situações com Reliable Sessions. Esta tag poderá ser utilizada nos arquivos **RM.exe.config**, **RM.Host.exe.config** e **RM.Host.Service.exe.config**. Exemplo para 10 segundos:   <add key="ReliableSessionSendTimeout" value="10" />   * ReliableSessionReceiveTimeout: Esta tag define o tempo em segundos para receber pacotes. Por padrão o RM considera esta opção com o valor infinito (0 - zero) e caso ela seja utilizada, este novo valor será considerado para situações com Reliable Sessions. Esta tag poderá ser utilizada nos arquivos **RM.exe.config**, **RM.Host.exe.config** e **RM.Host.Service.exe.config**. Exemplo para 15 segundos:   <add key="ReliableSessionReceiveTimeout" value="15" />   * ReliableSessionInactivityTimeout: Esta tag define o tempo de inatividade em segundos antes de cortar a conexão. Por padrão o RM considera esta opção com o valor de 10 segundos e caso ela seja utilizada, este novo valor será considerado para situações com Reliable Sessions. Esta tag poderá ser utilizada nos arquivos **RM.exe.config**, **RM.Host.exe.config** e **RM.Host.Service.exe.config**. Exemplo para 20 segundos:   <add key="ReliableSessionInactivityTimeout" value="20" /> |

### Cenários Homologados

Quando o recurso foi desenhado para ser desenvolvido, foram mapeados cenários de alta latência para realizar e registrar testes de performance, comparando o comportamento do RM quando utilizava-se Reliable Session ou não. Os testes concluíram que o ganho de performance em cenários de alta latência foram enormes, principalmente no quesito **tráfego de rede**. Foram trabalhados os seguintes cenários:

* AWS (Brasil) se conecta ao AZURE (Brasil) - Latência de **6ms** (Cenário **estável** de **Alta Performance**) - **Ganho de 4%** com **Reliable Session ativado**
  + Configurações do AWS (Brasil)
    - Firewall do Windows desativado
    - Portas 8050 e 8150 liberadas
    - Configurar SSL para RM, registrando o certificado conforme [orientação do TDN](http://tdn.totvs.com.br/display/public/LRM/Habilitar+SSL+no+Host)
    - RM.exe.config
      * Tag Host com o valor apontando para o IP do Load Balance na AZURE (Brasil)
      * Tag EnableReliable Session com os valores OnlyReliable e DisableReliable para testar a performance do RM de duas formas
      * Tag EnableCompression com o valor True
      * Ativar as Tags de certificado SSL
  + Configurações do AZURE (Brasil)
    - Load Balance
      * Permitir acesso externo gerando IP para o RM.exe do AWS (Brasil) acessar
      * Portas 8050 e 8150 liberadas
      * Direcionamento para uma única máquina de Host
    - Máquina para Host
      * Firewall do Windows desativado
      * Portas 8050 e 8150 liberadas
      * Configurar SSL para RM, registrando o certificado conforme [orientação do TDN](http://tdn.totvs.com.br/display/public/LRM/Habilitar+SSL+no+Host)
      * RM.Host.Service.exe rodando na porta 8050
        + Tag EnableCompression com o valor True
        + Ativar as Tags de certificado SSL
      * Alias.dat configurado para acessar a Máquina para Banco de Dados
    - Máquina para Banco de Dados
      * Firewall do Windows desativado
* TOTVS BH (Brasil/Belo Horizonte) se conecta ao TOTVS INTERA (Brasil/São Paulo) - Latência de **16ms** (Cenário **instável - latência variada -** de **Alta Performance**) - **Ganho de 11%** com **Reliable Session ativado**
  + Configurações da TOTVS BH (Brasil/Belo Horizonte)
    - Qualquer máquina que pertença à rede da TOTVS BH pode ser utilizada
    - Firewall do Windows desativado
    - Portas 8050 e 8150 liberadas
    - Configurar SSL para RM, registrando o certificado conforme [orientação do TDN](http://tdn.totvs.com.br/display/public/LRM/Habilitar+SSL+no+Host)
    - RM.exe.config
      * Tag Host com o valor apontando para o IP do Load Balance na TOTVS INTERA (Brasil/São Paulo)
      * Tag EnableReliable Session com os valores OnlyReliable e DisableReliable para testar a performance do RM de duas formas
      * Tag EnableCompression com o valor True
      * Ativar as Tags de certificado SSL
  + Configurações da TOTVS INTERA (Brasil/São Paulo)
    - Load Balance
      * Permitir acesso externo gerando IP para o RM.exe da TOTVS BH (Brasil/Belo Horizonte) acessar
      * Portas 8050 e 8150 liberadas
      * Direcionamento para duas máquinas de Host
    - Duas Máquinas de Host (Possuem a mesma configuração)
      * Mesma disposição de memória e processador
      * Mesmo ambiente RM
      * Firewall do Windows desativado
      * Portas 8050 e 8150 liberadas
      * Configurar SSL para RM, registrando o certificado conforme [orientação do TDN](http://tdn.totvs.com.br/display/public/LRM/Habilitar+SSL+no+Host)
      * RM.Host.Service.exe rodando na porta 8050
        + Tag EnableCompression com o valor True
        + Ativar as Tags de certificado SSL
      * Alias.dat configurado para acessar a Máquina para Banco de Dados
    - Máquina para Banco de Dados
      * Firewall do Windows desativado
* TOTVS BH (Brasil/Belo Horizonte) se conecta ao AZURE (Brasil) - Latência de **25ms** (**Cenário estável** de **Média/Alta Performance**)
  + **NÃO TESTADO POIS O FIREWALL DA TOTVS NÃO PERMITE**
* AZURE (USA) se conecta ao AWS (Brasil) - Latência de **129ms** (**Cenário estável** de **Baixa Performance**) - **Ganho geral de 213%** e **Ganho de rede de 360%** com **Reliable Session ativado**
  + Configurações do AZURE
    - Firewall do Windows desativado
    - Portas 8050 e 8150 liberadas
    - Configurar SSL para RM, registrando o certificado conforme [orientação do TDN](http://tdn.totvs.com.br/display/public/LRM/Habilitar+SSL+no+Host)
    - RM.exe.config
      * Tag Host com o valor apontando para o IP direto da máquina AWS (Brasil) (**Não tem Load Balance aqui**) acessar
      * Tag EnableReliable Session com os valores OnlyReliable e DisableReliable para testar a performance do RM de duas formas
      * Tag EnableCompression com o valor True
      * Ativar as Tags de certificado SSL
  + Configurações do AWS (Brasil)
    - Máquina para Host
      * Permitir acesso externo gerando IP para o RM.exe do AZURE (USA) acessar
      * Firewall do Windows desativado
      * Portas 8050 e 8150 liberadas
      * Configurar SSL para RM, registrando o certificado conforme [orientação do TDN](http://tdn.totvs.com.br/display/public/LRM/Habilitar+SSL+no+Host)
      * RM.Host.Service.exe rodando na porta 8050
        + Tag EnableCompression com o valor True
        + Ativar as Tags de certificado SSL
      * Alias.dat configurado para acessar a Máquina para Banco de Dados
    - Máquina para Banco de Dados
      * Firewall do Windows desativado
      * Banco de dados Oracle
* AZURE (USA) se conecta ao AZURE (Brasil) - Latência de **131ms** (**Cenário estável** de **Baixa Performance**) - **Ganho geral de 138%** e **Ganho de rede de 369%** com **Reliable Session ativado**
  + Configurações do AZURE (USA)
    - Firewall do Windows desativado
    - Portas 8050 e 8150 liberadas
    - Configurar SSL para RM, registrando o certificado conforme [orientação do TDN](http://tdn.totvs.com.br/display/public/LRM/Habilitar+SSL+no+Host)
    - RM.exe.config
      * Tag Host com o valor apontando para o IP do Load Balance na AZURE (Brasil)
      * Tag EnableReliable Session com os valores OnlyReliable e DisableReliable para testar a performance do RM de duas formas
      * Tag EnableCompression com o valor True
      * Ativar as Tags de certificado SSL
  + Configurações do AZURE (Brasil)
    - Load Balance
      * Permitir acesso externo gerando IP para o RM.exe do AZURE (USA) acessar
      * Portas 8050 e 8150 liberadas
      * Direcionamento para uma única máquina de Host
    - Máquina para Host
      * Firewall do Windows desativado
      * Portas 8050 e 8150 liberadas
      * Configurar SSL para RM, registrando o certificado conforme [orientação do TDN](http://tdn.totvs.com.br/display/public/LRM/Habilitar+SSL+no+Host)
      * RM.Host.Service.exe rodando na porta 8050
        + Tag EnableCompression com o valor True
        + Ativar as Tags de certificado SSL
      * Alias.dat configurado para acessar a Máquina para Banco de Dados
    - Máquina para Banco de Dados
      * Firewall do Windows desativado
* AZURE (USA) se conecta ao TOTVS INTERA (Brasil/São Paulo) - Latência de **12ms a 171ms** (Cenário **muito instável** - **latência muito variada** - de **Duvidosa Performance**) - **Ganho de 7%** com **Reliable Session ativado**
  + Configurações do AZURE (USA)
    - Firewall do Windows desativado
    - Portas 8050 e 8150 liberadas
    - Configurar SSL para RM, registrando o certificado conforme [orientação do TDN](http://tdn.totvs.com.br/display/public/LRM/Habilitar+SSL+no+Host)
    - RM.exe.config
      * Tag Host com o valor apontando para o IP do Load Balance na TOTVS INTERA (Brasil/São Paulo)
      * Tag EnableReliable Session com os valores OnlyReliable e DisableReliable para testar a performance do RM de duas formas
      * Tag EnableCompression com o valor True
      * Ativar as Tags de certificado SSL
  + Configurações da TOTVS INTERA (Brasil/São Paulo)
    - Load Balance
      * Permitir acesso externo gerando IP para o RM.exe da AZURE (USA) acessar
      * Portas 8050 e 8150 liberadas
      * Direcionamento para duas máquinas de Host
    - Duas Máquinas de Host (Possuem a mesma configuração)
      * Mesma disposição de memória e processador
      * Mesmo ambiente RM
      * Firewall do Windows desativado
      * Portas 8050 e 8150 liberadas
      * Configurar SSL para RM, registrando o certificado conforme [orientação do TDN](http://tdn.totvs.com.br/display/public/LRM/Habilitar+SSL+no+Host)
      * RM.Host.Service.exe rodando na porta 8050
        + Tag EnableCompression com o valor True
        + Ativar as Tags de certificado SSL
      * Alias.dat configurado para acessar a Máquina para Banco de Dados
    - Máquina para Banco de Dados
      * Firewall do Windows desativado
* AZURE (USA) se conecta ao TOTVS INTERA (Brasil/São Paulo) - Latência de **148ms** (Cenário **estável**de **Baixíssima Performance**) - **Ganho geral de 173%** e **Ganho de rede de 198%** com **Reliable Session ativado**
  + Mesma configuração do item anterior, porém foi realizada uma manutenção na TOTVS INTERA (Brasil/São Paulo) e o **cenário ficou estável** para realização apropriada de testes.

Os testes consistiram em medir o tempo de processamento das telas de visão e edição de funcionários **sem o Reliable Session** e depois comparado com a medição o tempo de processamento das mesmas telas **com o Reliable Session**. A diferença entre estes tempos resultou no percentual de **Ganho geral**. Para se calcular o **Ganho de rede**, mediu-se também o tempo de **processamento local** **com o Reliable Session**, ou seja, o RM.exe foi rodado na mesma máquina do Host para eliminar o tempo gasto em rede do tempo medido inicialmente. A diferença da comparação entre o tempo de processamento local com o tempo de processamento da máquina cliente resultou no percentual de **Ganho de rede**.

O tempo foi medido através do recurso da **Tela de Performance (Ctrl + Alt + F9)** ativado quando utilizada a tag **LogWcfCalls** com o valor True.

### Sugestão para Novos Testes de Homologação

Com a novidade do Reliable Session, foi necessário preparar a estrutura do RM para não quebrar uma execução quando houver falhas e por isto, foram implementadas rotinas que identificam as possíveis falhas para maximizar principalmente a capacidade resiliente do RM. Em caso de uma exceção disparada em alguma rotina principal que envolva o Reliable Session, o RM prepara a execução da rotina novamente desativando pontualmente o Reliable Session. Desta forma, outros testes são necessários para validar a resiliência do RM quanto à utilização em sua totalidade (Envolvendo todos os produtos da linha RM):

1. Execução de Processos
2. Criação de Relatórios
3. Geração de Relatórios
4. Geração e Execução de Metadados
5. etc...

A resiliência pode ser testada localmente (RM.exe e RM.Host.Service.exe na mesma máquina) independente dos cenários em cloud testados no item anterior, desde que obedecida as regras dos configs apontadas nestes cenários:

1. SSL
2. Compression
3. ReliableSession

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
