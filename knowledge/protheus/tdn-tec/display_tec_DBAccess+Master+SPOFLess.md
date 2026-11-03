---
content_hash: 03f0d3f12172be80d5b2a559e4c987001283647525a2768c608076a0244ca821
fetched_at: '2026-07-02T19:24:25.122069+00:00'
page_id: '498726573'
product: protheus
source: tdn-tec
title: DBAccess Master SPOFLess
type: documentation
url: https://tdn.totvs.com/display/tec/DBAccess+Master+SPOFLess
version: 9
---

## Descrição

Quando o true está configurado para trabalhar no modo distribuído, o DBAccess (Master) se torna um [SPOF](https://en.wikipedia.org/wiki/Single_point_of_failure), e em uma possível falha do mesmo (por questões de infraestrutura ou software), todos os usuários conectados ao DBAccess podem ser afetados, de modo que os mesmos teriam que entrar novamente no ERP.

Para mitigar esse cenário, foi projetado e implementado o DBAccess SPOFLess, que de uma maneira resumida é o espelhamento do DBAccess (Master), criando um modelo tolerante a falhas e mais resiliente, de modo que, em caso de falha do DBAccess (Master) o espelhamento/réplica assume o papel de Master do ambiente distribuído.

Vamos utilizar como exemplo um ambiente com 1000 usuários do ERP, distribuídos em 2 DBAccess (slave), usando o modelo SPOFLess do DBAccess. Nesse caso, se houver uma falha do Master, o Mirror (espelhamento) assume o papel de Master, e no máximo dois usuários poderiam ser afetados com a falha, ou seja, em um ambiente SPOFLess, o número máximo de usuários que poderia ser afetado é igual ao número de DBAccess (Slave) do ambiente.

 A configuração SPOFLess está disponível a partir da build 20181212 e/ou versão 18.2.1.0 do true.

## DBAccess distribuído

1. Os Application Servers conectam nos DBAccess (Slave)
2. Os DBAccess (Slave) conectam no DBAccess (Master) e no SGBD
3. O DBAccess (Master) se torna responsável por gerenciar locks, licenças, cache de estrutura de tabelas e caches de dados
4. Todas aplicações se comunicam através do protocolo TCP

## SPOF

Se o DBAccess (Master) ficar indisponível por qualquer razão, consequentemente todos DBAccess (Slave) vão perder a conexão com o gerenciador de locks, licenças, cache de estrutura de tabelas e caches de dados e uma vez que este cenário ocorra, todos DBAccess (Slave) vão gerar exceções AdvPL, por que esta é uma ocorrência critica e pode afetar a integridade de dados do ERP.

## SPOFLess

O modelo SPOFLess do DBAccess foi projetado e implementado de modo que o DBAccess (Master) seja replicado, de forma que todos DBAccess (Slave) passam a se conectar em 2 DBAccess (Master) e os DBAccess (Master) se comunicam entre si.

## SPOFLess em ação

Se o DBAccess (Master) ficar indisponível por qualquer razão, o DBAccess (Master) que está configurado como réplica, comunica todos DBAccess (Slave) que a partir daquele momento ele é o Master do ambiente.

## Exemplo de configuração dos DBAccess para uso do modelo distribuído SPOFLess

Neste modelo configuramos dois DBAccess (Master) de modo que um seja o espelho (Mirror) do outro (Master1 configura o espelhamento para o Master2 e vice-versa) e em cada DBAccess (Slave) será configurado o Master1 e o Master2.

| DBAccess Master 1 [General]  Port=7800  Mode=master  **MirrorServer=10.172.79.49**  **MirrorPort=7900** |
| --- |

| DBAccess Master 2 [General]  Port=7900  Mode=master  **MirrorServer=10.172.79.49**  **MirrorPort=7800** |
| --- |

| DBAccess Slave 1.. N [General]  Port=7901…N  Mode=slave  MasterServer=10.172.79.49  MasterPort=7800  MirrorServer=10.172.79.49  MirrorPort=7900 |
| --- |

## Veja também
