---
article_id: 360019902592
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 031f687284191737e20ef02460883f801950b83a3d0111c132ac1eaeab3b7131
fetched_at: '2026-06-28T22:39:07.852664+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como gerar o LogProfiler
  e Dbtrace?
type: support-article
updated_at: '2026-03-04T21:28:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019902592-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-gerar-o-LogProfiler-e-Dbtrace
---

O artigo explica como habilitar e gerar o LogProfiler e Dbtrace no TOTVS Protheus para análise de performance em rotinas, recomendando ambiente exclusivo e limpeza prévia dos arquivos console.log. Destaca a configuração no appserver.ini, cuidados com a queda de performance, e o procedimento para coleta e fechamento do SmartClient. Para ambientes cloud, orienta abrir ticket com o time responsável. Após uso, deve-se desativar o LogProfiler para evitar impacto na performance.

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17844928492055)***Tempo estimado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como habilitar e gerar o **LogProfiler** e Dbtrace para análise de performance nos processos de uma rotina?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da Versão 12.17.  
  
**Solução**

**Como Fazer | MP - SIGAEST - MATA330 - Coletar o Logprofiler e Dbtrace #TOTVS\_Backoffice\_linha\_Protheus** [**https://youtu.be/pocbYGWH6ys**](https://youtu.be/pocbYGWH6ys)

**Ativando o Logprofiler**  
Para realizar a coleta do Logprofiler, recomenda-se definir um ambiente preferencialmente exclusivo, a fim de efetuar a coleta da thread correta e específica. Antes de iniciar, proceda com a limpeza do arquivo console.log existente no appserver.

Configure a chave **Logprofiler=1** na seção do seu **[Environment]**, e as chaves Consolelog=1 e **ConsoleMaxSize=104857600** na seção **[GENERAL]**.

![Screenshot_3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33488727936919)

**Pontos a considerar:**

* Ao habilitar o LogProfiler, ocorre uma leve queda de performance no ambiente; por isso, recomenda-se habilitá-lo em um "Application Server (Appserver)" exclusivo para o teste.
* A extração do Log [via <SHIFT>+<F6>](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019236251-Log%C3%ADstica-Linha-Protheus-TMS-Gerar-LogProfiler-atrav%C3%A9s-do-Shift-F6) abrange apenas a thread corrente. Quando a rotina utiliza várias threads, é possível obter os dados somente através do console.log/console.bak, que são gravados a partir da configuração da chave **LogProfiler=1** no appserver.ini, conforme instruído neste material.

Os arquivos são normalmente gravados na pasta **\System**, entretanto, a cláusula "**ConsoleFile**" documentada no appserver.ini permite alterar o local de gravação, assim como seu nome físico.

Atente-se a esta configuração para localizar adequadamente os arquivos gerados.

**Executando a Rotina com o LogProfiler**

**Lembre-se:** Antes de executar a rotina que será monitorada, é necessário limpar os arquivos console.log e console.bak.

Não é possível limpar os arquivos enquanto os serviços do appserver.exe estiverem em execução; portanto, interrompa os serviços e limpe os arquivos. (Antes de parar os serviços, verifique se há usuários conectados ao sistema, para evitar perda de trabalhos em andamento.)

**1. Abra o SmartClient (ou Smartweb)**

**2. Execute a rotina desejada** **(se você deseja gerar o Dbtrace, não execute o processo ainda, apenas abra a rotina)**

**3. Após finalizar o processamento, feche o SmartClient.**

Este passo é extremamente importante, pois o log somente será gerado quando você fechar completamente a rotina e o SmartClient.

**4. Sempre verifique dentro dos arquivos console.log e console.bak**

Se o LogProfiler foi executado e gerado com sucesso, antes de enviar o arquivo para análise da equipe de Suporte Técnico, segue um exemplo com a estrutura do profiler gerado.

Veja abaixo como identificar se o **LogProfiler** foi gerado corretamente dentro dos arquivos de console, no caso estamos realizando a coleta após clicar no botão Incluir da rotina MATA010.

Veja abaixo como identificar a rotina que foi monitorada pelo **LogProfiler**:

![Screenshot_7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33488736939543)

**Como coletar os dados junto com Dbtrace**

Assim que você abrir a rotina, no processo "**2. Execute a rotina desejada"** do LogProfiler, você deverá abrir o DBMONITOR e rastrear a sessão da rotina desejada. Clique em "Rastrear" e, após, realize o processo da rotina desejada. Finalizando o processo, salve o arquivo dbtrace e finalize a rotina para gerar o LogProfiler no console.log do appserver.

![Captura de tela 2025-07-15 153337.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33488727942167)

**E se o meu ambiente fica no CLOUD da TOTVS?**

Devera abrir um ticket para o time CLOUD, solicitando efetuarem a configuração da chave de logprofiler no ambiente desejado, bem como combinar com o time CLOUD um dia e horario para que executem a ativação do DBTRACE afim de coletar o processamento da rotina, sugerimos contatar o CLOUD e solicitar um meet para que seja executado tais ações, dessa forma após finalizado o processamento, basta coletar os dados gerados e encaminhar ao suporte do produto para validação.

**Observações**:

* O **LogProfiler** não consegue registrar processamentos realizados por Stored Procedures; por este motivo, antes de habilitar o monitoramento, verifique se a rotina em questão possui Procedures.
* O **LogProfiler** é gerado nos arquivos **Console.log** e **Console.bak** (caso existam em seu ambiente).
* Para utilização, é necessário habilitar o **ConsoleLog=1** na seção **General** do arquivo **appserver.ini.**
* **Após a coleta do LOGPROFILER, desative a chave ativa na seção, para não afetar a performance; o log deve ser gerado apenas para a coleta do processamento e, em seguida, desativado.**

**Saiba mais:**

[*FAT0100 Habilitar e gerar o LogProfiler para avaliação de desempenho (rotinas ADVPL)*](https://tdn.totvs.com/x/h6GFDg)

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
