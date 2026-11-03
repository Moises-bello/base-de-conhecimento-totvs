---
content_hash: 461f1af717db395a941743131d840d5cd6b8dac263ddeec2d26e11d4eba5537f
fetched_at: '2026-06-29T00:08:18.775064+00:00'
page_id: '266969509'
product: rm
source: tdn-rm
title: Configuração para simular 3 camadas - JobServer
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=266969509
version: 3
---

# Como configurar o ambiente para simular 3 camadas

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 11.XX; 12.1.XX |
| **Ocorrência:** | Orientações para simular 3 camadas |
| **Ambiente:** |  |
| **Passo a passo:** | Para que seja possível realizar o agendamento de processos, faz-se necessário que o ambiente esteja instalado em 3, N camadas ou simule 3 camadas.  Seguem abaixo orientações para configurar o ambiente cuja instalação realizada foi local para simular 3 camadas.  Acesse o diretório UNIDADE:\totvs\CorporeRM\RM.Net, localize **TODOS** os arquivos do tipo .config, conforme print abaixo:       Edite o valor da tag abaixo para o valor true (Esse procedimento deve ser realizado em TODOS OS ARQUIVOS DE CONFIGURAÇÃO):   **<add key="JobServer3Camadas" value="true" />**  Segue exemplo de um arquivo de configuração com o valor da tag alterado:    Para versões anteriores à 12, deve-se alterar os arquivos de configuração de todos os aplicativos instalados, por exemplo, RM Labore:    À partir da versão 12, todos os arquivos de configuração, inclusive dos aplicativos Delphi, estão localizados no diretório RM.Net. Todos eles devem ter o valor da tag alterado para true.  Caso utilize o RM Portal na mesma máquina, a alteração deve ser realizada no arquivo .config do mesmo:  Acesse o diretório: C:\totvs\CorporeRM\Corpore.Net:    Altere o valor da tag "JobServer3Camadas" para true:    Acesse o arquivo RM.AliasManager.exe (C:\totvs\CorporeRM\RM.Net), e marque a flag "Habilitar Processamento de Job" e a flag "Executar apenas Jobs Locais":    Através do aplicativo RM.Host.ServiceManager.exe (C:\totvs\CorporeRM\RM.Net), reinicie o serviço do Host:    Após o restart do serviço do Host, a máquina configurada para simular 3 camadas será apresentada no Cockpit com status On - Local (apta para executar processos):    Realizando a parametrização corretamente, na execução dos processos, será apresentada a tela de agendamento de processos, conforme segue exemplo abaixo, na geração de um relatório .Net (Gestão | RM Reports | Processos | Gerar relatório), de modo que não seja necessário startar o modo Server no aplicativo Delphi: |
| **Observações:** | O Valor (**FALSE OU TRUE**) deve ser o mesmo para **todos** os arquivos .CONFIG  O valor setado como False é para instalações no modo "Local". O valor setado como TRUE é para ambientes 3, N camadas ou simulando 3 camadas.  Considerando que este ambiente (máquina) esteja simulando 3 camadas, os processos serão executados por ela mesma, ou seja, não se faz necessário configuração das tags FileServerPath e LogPath (estas tags são necessárias para realizar o mapeamento do diretório utilizado para geração e recuperação dos arquivos temporários apenas em ambiente cuja instalação é 3 camadas ou N camadas).  **DICA:**  CONFIG - JOBSERVER3CAMADAS = TRUE  ALIAS - JOBSERVERENABLED = TRUE  ALIAS - LOCALONLY = TRUE  Resultado: Dados nas  tabelas  GJOBSERVER e GKNOWNJOBSERVER. Executa somente os Jobs que o próprio servidor gerou (servidor e não client) e ninguém processa os seus jobs. |
