---
content_hash: 2cf1318a34eb62f0e0abbb2576fa8cccefe4961fc657d752a1c0b4e94529600b
fetched_at: '2026-06-29T00:11:33.946951+00:00'
page_id: '763248017'
product: rm
source: tdn-rm
title: 3.0 - Configuração dos Host's.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=763248017
version: 2
---

Essa configuração é utilizada para a requisição da **API** que chega no **IIS**, ela é filtrada pelo **URL Rewrite** e é redirecionada para o **host**, mas como a requisição vem do **IIS**, o mesmo **não consegue encontrar** o endereço do host, desta forma, a configuração que é feita no arquivo de **host do Windows,** irá informar para o **IIS** qual a máquina do host.

Atenção

**A partir da versão 12.1.2402** está configuração **não é necessária**.

Esta configuração é necessária ser realizada em **todas as máquinas que o IIS** estiver configurado.

* Acessar o arquivo de host do windows (geralmente se encontra em C:\Windows\System32\drivers\etc\hosts)

* Para cada alias cadastrado no rm, deve existir um registro no arquivo de host. Deve ser inserido um registro no mesmo padrão que foi informado no arquivo de configuração do host (ver a configuração do [Rewrite](https://tdn.totvs.com/pages/viewpage.action?pageId=837434579#temp--771829624), na aba configuração do config), onde deve ser inserido no seguinte padrão: Nome\_Do\_Alias.Nome\_Da\_Maquina\_Do\_Host **todo em minúsculo.**
* Caso a máquina em que o host se encontra configurado seja a mesma máquina em que o IIS está instalado, **deve ser informado o nome ou IP das configurações do [Rewrite](https://tdn.totvs.com/pages/viewpage.action?pageId=837434579#temp--771829624) (na opção: "Actions" e no campo Rewrite URL), lembrando que o valor pode localhost ou 127.0.0.1**, caso o host esteja configurado em uma máquina diferente da do IIS, o IP informado deve ser o IP da máquina do host.

**Exemplo 1**:

Como exemplo, existem dois alias cadastrados no RM.exe, um com o nome de CorporeRM e outro com o nome de CorporeRMOracle, e existe duas máquinas rodando o**IIS** e nestas maquinas rodam o host, uma com o nome de ServerXYZ e outra com o nome de SERVERZYX, desta forma, no arquivo de host da máquina ServerXYZ, ficaria da seguinte maneira:

- 127.0.0.1 corporerm.serverxyz  
- 127.0.0.1 corporermoracle.serverxyz

Para a máquina SERVERZYX:  
- 127.0.0.1 corporerm.serverzyx  
- 127.0.0.1 corporermoracle.serverzyx

**Exemplo 2:**

Como exemplo, existe dois alias cadastrados no rm, um com o nome de CorporeRM e outro com o nome de CorporeRMOracle, e existe duas máquinas rodando o*IIS* e uma máquina rodando o host, as máquinas rodando o IIS tem os nomes de ServerXYZ e outra com o nome de SERVERZYX, e a máquina de host tem o nome de hostxyz e o IP 10.0.0.52, desta forma, no arquivo de host da máquina ServerXYZ, ficaria da seguinte maneira:

- 10.0.0.52 corporerm.serverxyz  
- 10.0.0.52 corporermoracle.serverxyz

Para a máquina SERVERZYX:  
- 10.0.0.52 corporerm.serverzyx  
- 10.0.0.52 corporermoracle.serverzyx
