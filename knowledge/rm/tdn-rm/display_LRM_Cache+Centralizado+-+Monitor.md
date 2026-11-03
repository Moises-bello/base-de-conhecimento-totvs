---
content_hash: 6ae456a1e244304527bfddb1ee05a113117e846485feff39b1006efb900cbbb3
fetched_at: '2026-06-29T00:09:11.435186+00:00'
page_id: '403749439'
product: rm
source: tdn-rm
title: Cache Centralizado - Monitor
type: documentation
url: https://tdn.totvs.com/display/LRM/Cache+Centralizado+-+Monitor
version: 11
---

# Sumário

---

Sumário|Revisão|Download dos arquivos

# Revisão

---

|  |  |  |
| --- | --- | --- |
| Versão do Documento | Modificação | Autor / Revisor |
|  | Criação do documento |  |
|  |  |  |

.panelContent, .panelContent p, .panelContent p span{
color: white !important;
background: #202020 !important;
}
]]>

# 1 Introdução

      O monitor de cache é utilizado para avaliarmos a quantidade de inserções, buscas e seus respectivos tempos de resposta. Pois podemos a partir disso tomar decisões de alterar o comportamento padrão dos objetos, para permanecerem em memória ou serem enviados para o cache centralizado.

---

## 1.1.  Configuração

a) Edite o arquivo RM.Host.Service.exe.config / RM.Host.exe.config e insira a chave abaixo.

|  |
| --- |
| <add key="TRACECACHE" value=" **true**” /> |

b) Reinicie o RM.Host.Service / RM.Host. Realize esta configuração em todos os Servidores de App e Servidores de Job.

c) Os arquivos de trace serão gerados no diretório: Instalação do RM\Processos\Logs\Cache

# 2 Visualizando o log de forma estruturada.

---

a) O arquivo de log gerado não está de forma agrupada, utilize o Excel (por exemplo) para manipular o arquivo e visualizar de forma mais estruturada.

Segue um exemplo para visualizar quais objetos estão sendo enviados para o cache e o volume de requisição dos mesmos.

falseTestePasso 1

Importe o arquivo, utilizando a opção de dados do Excel.

Passo 2

Defina Ponto e Vírgula como separador e clique em avançar até o final.

Passo 3

Insira uma tabela dinâmica com a configuração conforme print abaixo:

# 2 Monitorando o redis

---

## 2.1.  Monitorando via telnet

a) Basta abrir um telnet no servidor de porta (por padrão é 6379) do redis e executar o comando MONITOR. A partir desse momento qualquer operação no redis será visualizada.

## 2.2.  Monitorando via redis-cli

a) Baixe o redis-cli através do link <https://redis.io/download>;

b) Execute o mesmo pela linha de comando da seguinte forma redis-cli -h 10.31.0.163 -p 6379;

b) Com um client qualquer (nesse caso o redis-cli) é possível executar algumas operações, como:

* Get key - Busca pela chave
* Put key value - Insere uma nova chave
* scan 0 - busca os 10 primeiros os objetos que estão no redis
* scan 0 count 100 - busca os objetos que estão no redis definindo a quantidade

## 2.3.  Utilizando o redis-stat

a) É possível colocar ferramentas de monitoramento do redis, segue exemplo de como utilizar o redis-stat.

b) Execute o comando via linha de comando:

```
$ docker run --name redis-stat -p 8080:63790 -d insready/redis-stat --server 123.123.123.123
```

```
c) acesse pelo browser http://localhost:8080/?host=redis
```

Para maiores detalhes do redis-stat veja em <https://hub.docker.com/r/insready/redis-stat/>

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.20 ou Superior

false

Cache Centralizado - **Get Started**

falsefalse

**Status:** **Finalizado**

false

**Data:**

false

**Autores:**

false 250
