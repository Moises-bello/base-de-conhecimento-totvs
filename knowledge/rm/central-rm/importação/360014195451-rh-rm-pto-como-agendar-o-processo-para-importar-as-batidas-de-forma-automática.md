---
article_id: 360014195451
category: Importação
content_hash: 0d1e881cee92143ddc82fd9aa5b602475b4ff2d5e4d16bcf52ba468fc497f404
fetched_at: '2026-06-28T22:46:33.744774+00:00'
product: rm
section_id: 6045469428631
source: central-rm
title: RH - RM - PTO - Como agendar o processo para importar as batidas de forma automática
type: support-article
updated_at: '2025-01-16T12:45:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014195451-RH-RM-PTO-Como-agendar-o-processo-para-importar-as-batidas-de-forma-autom%C3%A1tica
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16034526171159) Tempo aproximado para leitura: 00:01:30 min  
  
Dúvida**Como realizar a importação automática de batidas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto – A partir da versão 11.80  
  
**Solução**Para utilizar a funcionalidade de importação automática de batidas, é importante observar que essa opção está disponível apenas para o ambiente em 3 camadas. Portanto, é necessário que você esteja utilizando esse tipo de ambiente ou simule um ambiente de 3 camadas.

**Se o seu ambiente já é 3 camadas, poderá seguir para a parte do agendamento no PASSO 2 mais abaixo**.

**PASSO 1:**  
Para simular um ambiente de 3 camadas, siga as instruções abaixo:

1. Acesse a pasta de instalação do seu ambiente e navegue até Unidade: **\TOTVS\CorporeRM\RM.Net**.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21867229564055)
2. Localize todos os arquivos com extensão **.config** e edite-os utilizando o Bloco de Notas:  
     
   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12500686769175)
3. Altere o valor da tag a seguir para *true*:  **<add key="JobServer3Camadas" value="true" />**  
   ![2018-08-21_09_11_33-_C__totvs_CorporeRM_RM.Net_RM.exe.config_-_Notepad__.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360009572871)  

   **Atenção**: É importante ressaltar que essa alteração deve ser realizada em todos os arquivos **.config** que contenham a tag **JobServer3Camadas**.
4. Após efetuar esses ajustes, será necessário reiniciar o serviço RM.Host.ServiceManager.exe. Para isso, clique no botão "Desinstalar". Em seguida, ao aparecer a mensagem de que o **Serviço não existe**, clique em "Instalar" e aguarde até que a mensagem **Iniciado** seja exibida.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21865104901911)  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21865104925207)
5. Ao fazer login novamente no RM, acesse o menu **Ambiente | Cockpit** e localize o servidor onde o RM está instalado. Na seção "Informações de Processamento e Memória", inicie o processo, caso esteja parado, e aguarde até que ele seja iniciado.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21866390046871)  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21866450304407)

**PASSO 2:**  
Para agendar a importação automática de batidas no módulo **Automação de Ponto**, siga as etapas abaixo:

1. Acesse o menu **Entrada de Dados | Importar**.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21865093960727)
2. Na janela de Importação, realize as configurações desejadas para o agendamento da importação, conforme as orientações do documento disponível em [RH - RM - PTO - Como importar as marcações para o Automação de Ponto.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000486068-RH-RM-PTO-Como-importar-as-batidas-para-o-Automa%C3%A7%C3%A3o-de-Ponto)
3. No campo "**Fim**" da seção **Período de Importação**, insira a data em que o job será finalizado, indicamos sempre inserir uma data futura. Ao alterar a data de fim para uma futura, poderá receber a mensagem *"A data Fim é maior que a data de hoje DD/MM/AAAA!"*, que é um alerta e pode ser desconsiderado.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21865104978711)  
   **Observação**: Atente-se para **não** colocar a data fim em 29/02 por ser uma data de ano bissexto.
4. No campo "Arquivo para importação", informe o caminho do local onde o arquivo está salvo ou o caminho de rede do arquivo, no qual deverá estar compartilhado. Exemplo: [\\servidor\batidas.txt](file://servidor/batidas.txt)
5. Marque a opção de "**Considera a última linha importada",** pois esse parâmetro deve ser utilizado para a importação automática de batidas para ganho de performance, onde o processo de importação não reler novamente as linhas que já foram importadas em processos anteriores.
6. Na seção Perfil de Parâmetros, insira o nome do perfil desta parametrização e clique em "**Salvar perfil ao concluir**".  
   No exemplo, utilizamos o ano de **2050**, para que este job (processo) permaneça sendo executado no servidor.   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21865104958231)
7. Avance no processo de importação e configure o agendamento do processo, defina a data da primeira execução, o horário, os dias a serem gerados e o intervalo de cada importação.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21865527077271)
8. Após definir a parametrização e o intervalo de agendamento desejado, clique no botão **Executar**.

**Saiba mais**[TDN - Como Fazer - Importação Automática de Batidas Utilizando Layout AFD](https://tdn.totvs.com/pages/releaseview.action?pageId=4812726)  
[TDN - Importação de batidas](https://tdn.totvs.com/pages/releaseview.action?pageId=452719301)  
[RM - Frame - Tipo de recorrência da tabela GJOBX](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007124831)
