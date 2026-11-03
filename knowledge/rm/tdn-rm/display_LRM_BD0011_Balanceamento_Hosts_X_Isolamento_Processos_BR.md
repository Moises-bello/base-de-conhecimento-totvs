---
content_hash: e3aeb55bbe83f0bdb0663d5079f7c246181998c12316f675fd1cbb4160759c92
fetched_at: '2026-06-29T00:08:05.898118+00:00'
page_id: '236421391'
product: rm
source: tdn-rm
title: BD0011_Balanceamento_Hosts_X_Isolamento_Processos_BR
type: documentation
url: https://tdn.totvs.com/display/LRM/BD0011_Balanceamento_Hosts_X_Isolamento_Processos_BR
version: 5
---

|  |  |
| --- | --- |
| **Produto:** | Performance |
| **Versões:** | 11.82.42 ou superior |
| **Ocorrência:** | Balanceamento Hosts x Isolamento Processos |
| **Ambiente:** | RM |
| **Passo a passo:** | Este caso é indicado quando não existe um **servidor de Jobs** dedicado, dessa forma o servidor de aplicação poderá ter **Multiplos Hosts** (<http://tdn.totvs.com/x/e9fuDQ>) e **Isolamento de Processos** (<http://tdn.totvs.com/x/ndfuDQ>) trabalhando no mesmo servidor, sem que o JobRunner seja disparado por qualquer um dos 4 hosts.  A configuração abaixo faz com que o Isolamento de Processos seja direcionado para apenas um host evitando possíveis problemas de balanceamento. O objetivo é utilizar um servidor com Balanceamento Nativo e deixar apenas um host para processamento de Jobs.   1. No arquivo de configuração RM.Host.Service.exe.config do host principal RM.Host.Service.exe adicionar a tag: **<add key="ALIASPATH" value="C:\totvs\CorporeRM\RM.Net\Alias" />** 2. Criar uma pasta no caminho informado anteriormente: 3. Dentro da pasta adicionar uma cópia do arquivo **Alias.dat** 4. O arquivo Alias.dat do caminho **C:\totvs\CorporeRM\RM.Net** deverá ficar com as tags de processamento como false:  **<JobServerEnabled>false</JobServerEnabled>** **<JobServerLocalOnly>false</JobServerLocalOnly>** 5. O arquivo **Alias.dat** do caminho **C:\totvs\CorporeRM\RM.Net\Alias** deverá ficar com as tags de processamento como **true**, este arquivo é que o host principal irá ler por causa da **tag** adicionada no **item 1**.   **<JobServerEnabled>true</JobServerEnabled>** **<JobServerLocalOnly>false</JobServerLocalOnly>** 6. Os outros hosts **RM.Host.Service1.exe.config, RM.Host.Service2.exe.config** e **RM.Host.Service3.exe.config** não terão a **tag** do **item 1**, dessa forma utilizarão o **Alias.dat** origina do diretório **C:\totvs\CorporeRM\RM.Net** 7. Após realizar toda configuração citada, deverá ser reiniciado todos os Hosts 8. Quando abrir o sistema e acessar o Cockpit, a configuração já estará correta. Apenas o **RM.Host.Service.exe.config** processando **Jobs**. |
| **Observações:** | Para mais informações:  **COMUNIDADE** [R@Tecnologia](http://fluig.totvs.com/portal/p/10097/post/rtecnologia-community/1639774)   **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 8 – (Tecnologia), 2 – (Banco de Dados) |
