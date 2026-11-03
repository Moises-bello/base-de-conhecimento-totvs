---
content_hash: 1fe6ae38764412f7df3fe6f4c3da1f7ac93bc921b54eb606475bb597f6bb2c28
fetched_at: '2026-06-28T21:35:19.804042+00:00'
page_id: '223919781'
product: fluig
source: tdn-fluig
title: BPM 029 - Como realizar downgrade do banco de dados para ajustar o horário
  de execução de uma atividade que está incorreto?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223919781
version: 15
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

**Versão:**Todas as versões

# Ocorrência

As solicitações abertas possuem - na aba Detalhes - o histórico de movimentação e por onde a solicitação passou anteriormente, bem com o usuário que executou a atividade.

Porém o tempo que é exibido sobre quando foi executada a atividade está incorreto e esta é uma informação importante que os usuários necessitam.

**Exemplo de Horário Incorreto**

# Causa

Problema no *driver*ojdbc (Oracle JDBC) superior à versão 6.

# Solução

Realizar o *downgrade* para a versão 6 do *driver* de conexão com o banco de dados Oracle: ojdbc6.jar

# Procedimentos

A seguir, estão descritos os procedimentos para realizar o *downgrade*:

0.5falsesamplesfadetrue1Passo 1

Primeiramente, pare os serviços do fluig;

Aconselhamos que seja efetuado um *backup* dos seguintes itens:

* Base de dados do fluig;
* Arquivos contidos no diretório <fluig>\jboss\modules\com\oracle\jdbc\main (fluig 1.5.x) ou <fluig>\appserver\modules\com\oracle\jdbc\main (fluig 1.6)

2Passo 2

Acesse o site da Oracle e faça o *download* do driver de conexão na versão 6.

Em seguida, copie o arquivo ojdbc6.jar que foi baixado e mova para o diretório <fluig>\jboss\modules\com\oracle\jdbc\main (fluig 1.5.x) ou <fluig>\appserver\modules\com\oracle\jdbc\main (fluig 1.6).

3Passo 3

No diretório <fluig>\jboss\modules\com\oracle\jdbc\main  (fluig 1.5.x) ou <fluig>\appserver\modules\com\oracle\jdbc\main (fluig 1.6), localize o arquivo 'module.xml' e altere o parâmetro path para 'ojdbc6.jar' conforme a linha 4 do exemplo abaixo:

 

xmltrue








]]>4Passo 4

Por fim, inicie os serviços do fluig e realize novos testes no histórico das solicitações.
