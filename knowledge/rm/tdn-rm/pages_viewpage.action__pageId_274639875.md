---
content_hash: d61846d54ebbe05a35724164bc5f759171d8d8cbea1e223efaf2d8075a0bd8a6
fetched_at: '2026-06-29T00:08:33.991872+00:00'
page_id: '274639875'
product: rm
source: tdn-rm
title: BD0019_Configuração_Arquivo "HOSTS" - Tempo de resolução no DNS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274639875
version: 3
---

|  |  |
| --- | --- |
| **Produto:** | Banco de Dados |
| **Versões RM:** | Todas |
| **Ocorrência:** | Configuração\_Arquivo "HOSTS" - Tempo de resolução no DNS |
| **Ambiente:** | Sistemas Operacionais |
| **Introdução:** | O que é o arquivo Hosts? Localizado no diretório " %WinDir%\System32\Drivers\Etc ", o arquivo de configuração "HOSTS" nos permite encontrar um "máquina" de forma simples e ágil através do relacionamento de HOSTNAME e IP incluso em sua estrutura.    Esta resolução ocorre em menor tempo, visto que suas definições são carregadas em memória (cache) ao iniciar a máquina, o que permiti ao sistema operacional efetuar a leitura antes de requisitar as mesmas informações ao Servidor de DNS. Neste cenário, a busca no servidor é realizada quando as informações de hostname/ip não estão dispostas no arquivo.  Cada identificação/mapeamento de máquinas, devem ser mantidos em uma linha individual, primeiramente deve ser incluso o "endereço IP" na primeira coluna e seguido do nome de "Hostname" correspondente ao IP, lembrando que devem ser separados por pelo menos um espaço, conforme segue exemplo:  **Exemplos:**  10.31.201.1 SRVTESTE1 10.31.201.3 SRVTESTE2 10.31.201.9 PRINTSERVER1 10.31.201.11 SRVBD |
| **Estrutura do arquivo:** | Observe que no exemplo citado, foram inclusos 4 mapeamentos de servidores ( SRVTESTE1, SRVTESTE2, PRINTSERVER1 e SRVBD), alterando a estrutura do arquivo padrão. Visando melhor entendimento, segue abaixo detalhes sobre a estrutura do arquivo antes e após a inclusão dos registros:   * Default      * Alterada     **Observações**:   * Em alguns casos, o Windows poderá bloquear a edição do arquivo, sendo necessário realizar a abertura do bloco de elevado ("Executar como Administrador") para edição. * É importante que o tamanho do arquivo não ultrapasse 135 kb, acima deste valor pode ser apresentado uma queda de performance de inicialização. * Comentários podem ser inseridos em linhas individuais, indicados pelo um símbolo “**#**”. Isto também pode ser usado para desativar temporariamente uma entrada/linha.  Exemplos:  ```  10.31.201.1 SRVTESTE1  10.31.201.3 SRVTESTE2  # 10.31.201.9 PRINTSERVER1  10.31.201.11 SRVBD ```  ```   ``` |
| **Utilização:** | É Importante frisar, que este tipo de otimização é utilizada sempre que os produtos TOTVS ou ferramentas em uso estão sendo impactadas pelos problemas de redes.  Uma das formas de detectar este tipo de situação, é navegando na tela "Gerenciamento de processos" disponível na MDI (RM.exe), módulo "Serviços Globais", Menu "Ambiente" > Gerenciamento de processos.  Caso o tempo de de alteração entre um registro e outro na visão, ou o tempo de abertura de cada registro esteja alto, possivelmente estamos com um delay na resolução das informações no servidor de DNS, sendo necessário otimizar o arquivo HOSTS e solicitar uma avaliação da equipe de redes de sua empresa. |
| **Fontes:** | <http://support.microsoft.com/kb/923947/en-us>  <http://support.microsoft.com/kb/105997/en-us>  <http://support.microsoft.com/kb/219843/en-us>  <http://www.microsoft.com/technet/prodtechnol/sms/smssp2/spsecurity/68359d63-8884-4327-9c75-5f2693cb4221.mspx?mfr=true> |
| **Observações:** | Para mais informações:  **COMUNIDADE** [R@Tecnologia](http://fluig.totvs.com/portal/p/10097/post/rtecnologia-community/1639774)  **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 8 – (Tecnologia), 2 – (Banco de Dados) |
