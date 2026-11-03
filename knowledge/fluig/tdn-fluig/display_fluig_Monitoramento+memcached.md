---
content_hash: b50b9d5e03a6d0c95ed779e1ece45f1f0f26b438b26c386ab365d0a6d955a87e
fetched_at: '2026-06-28T21:35:18.239751+00:00'
page_id: '152802227'
product: fluig
source: tdn-fluig
title: Monitoramento memcached
type: documentation
url: https://tdn.totvs.com/display/fluig/Monitoramento+memcached
version: 14
---

Importante!

Em novas instalações a partir da atualizações 1.6 não é mais utilizado por padrão o serviço de MemCached, pois o recurso de cache está sendo disponibilizado internamente na plataforma. Portanto esta documentação é direcionada para clientes que utilizam o serviço de MemCached nas atualizações 1.6.1, versões anteriores e ambientes de alta disponibilidade.

# Índice

true.\*ndicenone

# Ferramenta

---

Existem diversas ferramentas de monitoramento de memcached disponíveis no mercado, como o phpMemcachedAdmin, o memcache-top, o statsproxy, além do próprio console do memcahced acessado por telnet. Utilizaremos phpMemcachedAdmin como ferramenta de monitoração, ele possui uma interface web simples e fácil de utilizar também iremos enumerar alguns pontos o que devem ser monitorados e soluções de problemas.

# Guia de instalação do phpMemcachedAdmin

---

O  phpMemcachedAdmin deve ser baixado no site  <https://code.google.com/p/phpmemcacheadmin/> , ele é um script simples em php e como tal deve rodar em um servidor http que tenha suporte a php.

A ultima versão até a data em que esse guia foi escrito é a 1.2.2-r262 que pode ser obtida no link: <http://phpmemcacheadmin.googlecode.com/files/phpMemcachedAdmin-1.2.2-r262.tar.gz>

seguindo as instruções do site devemos descompactar o pacote, dar permissão de execução aos scripts e permissão de escrita no arquivo de configuração dos servidores e na pasta em que são gerados os relatórios na pasta raiz do seu servidor. Exemplo:

xml

# Como configurar

---

falsestubFlextrue0.511º Passofade

* Apontar o navegador para a instalação do phpMemcahedAdmin em seu servidor, no caso nossa instalação está em <http://localhost/phpMemcachedAdmin>.

0.522º Passofade

* Inicialmente o monitorador já vem configurado para se conectar a um memcached local na máquina em que foi instalado, caso o memcached esteja instalado em outro local devemos acessar o link "Edit Configuration" localizado no canto superior direito que irá direcionar a página abaixo.

0.533º Passofade

* Nessa tela é possível monitorar varias instalações de memcached, para a nossa configuração apenas vamos editar o endereço do servidor e a porta, lembrando que a porta padrão é a 11211, após salva as alterações já podemos seguir as páginas de monitoração clicando em "See Live Stats" ou "See Stats for"  mais a seleção do servidor no combo ao lado .
* Caso as configurações apresente algum problema você visualizará a página abaixo, caso isso ocorra verifique se o memcached está funcionando e alcançável do servidor que o phpMemcached foi instalado, uma maneira de verificar isso é fazendo um telnet no endereço do memcached na porta 11211.

# Pontos de atenção que devem ser monitorados e soluções

---

falsestubFlextrue0.511º Passofade

* No gráfico "Cache Size Graphic" temos uma clara indicação do tamanho da memoria alocada para ele versus o consumo e o desperdício de memoria. O TOTVS Fluig Plataforma foi desenhado de maneira a nunca expirar um registro que está no cache, porem um alto consumo de memoria pode fazer com que o memcached de forma voluntária expurgue os registros mais antigos fazendo com que os usuários percam certas permissões, esse comportamento é evidenciado na quantidade de "Evictions" que o sistema está fazendo.
* O memcached foi desenhado para trabalhar com blocos de 1 mega por padrão, esses blocos recebem o nome de Slab e agrupam registros de tamanhos similares. Quando solicitamos ao memcached para guardar um registro, é realizado um cálculo para saber em Slab ele vai ser inserido, se o Slab estiver cheio, vai ser criado uma nova página.  No exemplo abaixo, o Slab 1 guarda informações do tamanho de 96 bytes, como o tamanho da página do Slab foi parametrizado para 5 megas em uma conta aproximada  (1024\*1024\*5) / 96 = 54613, chegamos a conclusão que esse Slab comporta 54613 registros, caso mais um registro seja inserido o memcached irá criar uma nova página para esse Slab.

0.522º Passofade

* Existem situações, em que podemos ter grupos com mais de 100 mil usuários e que acaba gerando registros maiores que o suportado por padrão, para esses casos, devemos parametrizar o memcached para trabalhar com Slabs maiores alterando o parâmetro  -I ( I de Igreja).

0.533º Passofade

* No exemplo abaixo a configuração do tamanho da página do slab foi de 5 megas, esse numero é relativamente elevado e acaba gerando um grande desperdício de memoria, podemos verificar no exemplo abaixo que o tamanho máximo de registro é de 1.8 megas, logo podemos ter uma configuração mais assertiva e com um menor desperdício se o parâmetro fosse próximo dos 2 megas
* O desperdício acontece quando é criado uma página no slab, toda a memoria configurada é alocada, no caso 5 megas, se essa página não recebe mais nenhum ou poucos registros toda essa área vai ficar subutilizada.

# Parametrização do memcached

---

Maiores informações sobre as opções de parametrização podem ser obtidas nos sites do memcached e nesse site com a descrição dos parâmetros <http://linux.die.net/man/1/memcached>
