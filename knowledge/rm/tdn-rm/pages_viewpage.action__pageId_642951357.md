---
content_hash: cb2bd7ea04efadef6d6fc329418b8f373d1de99810cc6f43deeac6cd873afe18
fetched_at: '2026-06-29T00:11:10.248615+00:00'
page_id: '642951357'
product: rm
source: tdn-rm
title: 02 - Configuração Configuração dos Host's
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=642951357
version: 3
---

**Caso tenha realizado essa parametrização para o Novo Portal do professor, não é necessário realizar essa confirguração.**

Esta configuração é necessária ser realizada em todas as  máquinas que o *IIS* (internet information service) estiver configurado. Isto é necessário porque quando a requisição da api chega no iis, ela é filtrada pelo módulo do *Rewrite* e é redirecionada para o host, mas como a requisição vem do *IIS*, o mesmo não consegue encontrar o endereço do host, desta forma, a configuração que é feita no arquivo de host do *Windows*, irá informar para o *IIS* qual a máquina do host. A seguir segue o passo a passo da configuração:

* Acessar o arquivo de host do windows (geralmente se encontra em C:\Windows\System32\drivers\etc\hosts)

* Para cada alias cadastrado no rm, deve existir um registro no arquivo de host. Deve ser inserido um registro no mesmo padrão que foi informado no arquivo de configuração do host (ver a configuração do [Rewrite](https://tdn.totvs.com/x/BCl0Ig), na aba configuração do config), onde deve ser inserido no seguinte padrão: Nome\_Do\_Alias.Nome\_Da\_Maquina\_Do\_Host **todo em minúsculo.**
* Caso a máquina em que o host se encontra configurado seja a mesma máquina em que o IIS está instalado, deve ser informado o IP 127.0.0.1, caso o host esteja configurado em uma máquina diferente da do IIS, o IP informado deve ser o IP da máquina do host.

**Exemplos**:

* Como exemplo, existem dois alias cadastrados no rm, um com o nome de CorporeRM e outro com o nome de CorporeRMOracle, e existe duas máquinas rodando o *IIS* e nestas maquinas rodam o host, uma com o nome de ServerXYZ e outra com o nome de SERVERZYX, desta forma, no arquivo de host da máquina ServerXYZ, ficaria da seguinte maneira:

3.0 - Configuração dos Host's  
- 127.0.0.1 corporerm.serverxyz  
- 127.0.0.1 corporermoracle.serverxyz

Para a máquina SERVERZYX:  
- 127.0.0.1 corporerm.serverzyx  
- 127.0.0.1 corporermoracle.serverzyx

* Exemplo2: existe dois alias cadastrados no rm, um com o nome de CorporeRM e outro com o nome de CorporeRMOracle, e existe duas máquinas rodando o *IIS* e uma máquina rodando o host, as máquinas rodando o IIS tem os nomes de ServerXYZ e outra com o nome de SERVERZYX, e a máquina de host tem o nome de hostxyz e o IP 10.0.0.52, desta forma, no arquivo de host da máquina ServerXYZ, ficaria da seguinte maneira:

- 10.0.0.52 corporerm.serverxyz  
- 10.0.0.52 corporermoracle.serverxyz

Para a máquina SERVERZYX:  
- 10.0.0.52 corporerm.serverzyx  
- 10.0.0.52 corporermoracle.serverzyx
