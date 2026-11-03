---
content_hash: 859d3176422b6921328866141813aae5a7e61d7c76e1abe23757360f95d1a578
fetched_at: '2026-06-28T21:35:23.863813+00:00'
page_id: '267782633'
product: fluig
source: tdn-fluig
title: ARQ - Por que ocorre o erro "Unsupported version" ao configurar uma nova versão
  do MS SQL Server?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267782633
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Possuo duas versões do MS SQL Server instalados na mesma máquina, a versão 2008 e a atual 2012. Ao tentar apontar para a instalação da plataforma para o banco de dados compatível com a versão 2012, ocorre o erro abaixo. Como proceder?

# Causa

A instalação da plataforma está apontando para o banco de dados da versão 2008.

# Solução

Será necessário garantir que as configurações da porta TCP/IP de cada versão sejam distintas para que não ocorram conflitos.

Em seguida, verifique se no arquivo **standalone.xml**, localizado em [diretório\_instalação]/jboss/standalone/configuration, a porta esteja coerente com a configurada para a versão do banco de dados. Para isso, localize a linha abaixo e confira a porta:

xmlEclipsestandalone.xmljdbc:sqlserver://[HOST FLUIG]:1433;databaseName=[NOME DO BANCO]]]>

Para atualizações 1.6 até 1.8.2, verifique o arquivo **domain.xml**, localizado em [diretório\_instalação]/appserver/domain/configuration, se a porta está de acordo com a configurada no banco de dados da versão 2012. Para isso, procure o código abaixo e compare:

xmlEclipsedomain.xmljdbc:sqlserver://[HOST FLUIG]:1433;databaseName=[NOME DO BANCO]]]>Atenção!

O banco de dados MS SQL Server 2008 só é suportado até a atualização 1.5.9 conforme descrito na , pois a Microsoft não disponibiliza mais atualizações e canais de suporte para este produto. A partir da atualização 1.5.10 será necessário atualizar para o banco de dados SQL Server 2012 ou superior.
