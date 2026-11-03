---
content_hash: 25d3011328581e77d57e9c9a0dce92e24d7a6ca60dbf1e4dc58acde7a70474d7
fetched_at: '2026-06-28T21:35:23.377850+00:00'
page_id: '244925501'
product: fluig
source: tdn-fluig
title: Consumo de memória pelo servidor de aplicação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244925501
version: 12
---

4.\*ndice

# Objetivo

---

O objetivo deste guia é mostrar a configuração correta para evitar problemas quanto ao consumo de memória pelo servidor de aplicação.

# Memória alocada pela JVM

---

O total de memória utilizado pela JVM depende de diversos fatores, como: Java Heap Space, Coletor de lixo, Cache de código, Compilador, Metadados, *Threads*, etc. Como são muitos os fatores envolvidos, não existe uma maneira garantida de estimar o total de memória que será utilizada por um processo Java.

O parâmetro XMX define o quanto de memória estará disponível para o Java Heap Space (memória dinâmica) que é uma das áreas de memória utilizada pela JVM (*Java Virtual Machine*).

Devido a um uso mais alto temos um consumo mais elevado das *threads* tanto de HTTP, como de EJB.

É possível verificar que a configuração de *threads* está desta forma:

falseVersão2A partir da 2.0

No arquivo **standalone.xml** em produção (localizado em [diretório\_instalação]/appserver/standalone/configuration):

xmlEclipsestandalone.xml


















]]>11.6 até a 1.8.2

No arquivo **domain.xml** em produção (localizado em [diretório\_instalação]/appserver/domain/configuration):

xmlEclipsedomain.xml


















]]>

Quanto maior o uso, mais alto será o consumo de memória. Os espaços de memória são configurados separadamente, o valor máximo é definido pela soma das variáveis (como explicado acima) e o uso real vai variar conforme a carga de processamento atual.
