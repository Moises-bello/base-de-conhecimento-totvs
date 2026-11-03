---
content_hash: 06475ff51cbeed37fbc1b2687c8bb08228454da4c407465e647c25f7f350a06d
fetched_at: '2026-06-29T00:10:53.750197+00:00'
page_id: '579454186'
product: rm
source: tdn-rm
title: Configurar cache de arquivos
type: documentation
url: https://tdn.totvs.com/display/LRM/Configurar+cache+de+arquivos
version: 12
---

Cada browser utiliza uma estratégia de otimizar a exibição das páginas, uma forma de otimização é o cache de armazenamento das páginas, para que em execuções posteriores seja mais rápida a apresentação do site.

Com o uso do cache automático nos browsers podem ocorrer não conformidades. Por exemplo, a máquina do usuário final com uma versão desatualizada do portal ou uma mudança em algum arquivo de parametrização do portal não ser refletida automaticamente durante algum teste.

A configuração abaixo é um exemplo para que o Servidor WEB (*Internet Information Services* - IIS) otimize a resposta das requisições e indique a melhor forma de gerenciar o cache aos browsers. Sem esta configuração, cada browser pode realizar o cache automaticamente de um arquivo e o mesmo ser expirado somente quando for realizado uma limpeza de cache do browser.

Esta documentação é voltada para profissionais responsáveis pelo infraestrutura computacional das Instituições de Ensino.

## Configuração do Cache do IIS

No diretório "C:\TOTVS\CorporeRM\FrameHTML\Web\App\Edu\PortalEducacional\" criar um arquivo de nome "Web.config", neste arquivo deverá conter o XML abaixo:

xml0Web.configtrue








]]>

O código acima configura o IIS para que todos os arquivos Javascript do portal Educacional estejam em cache do servidor Web até que estes arquivos sejam modificados.

Na primeira execução, o browser realizará o download do arquivo (HTTP de resposta com código de status igual a 200) e nas próximas chamadas, deste mesmo arquivo, a resposta da requisição terá o código de status igual a 304. O IIS indicará ao browser que o arquivo não foi modificado, portanto eliminando a necessidade de atualizar o arquivo. Uma vez que o arquivo for modificado, o IIS indicará ao Browser que por sua vez, deverá realizar novamente o download.

Esta documentação cita um exemplo de configuração no ambiente do servidor WEB do cliente. A configuração vai depender da infraestrutura de redes de cada cliente e de como deseja proceder a expiração do cache.

A utilização de *Proxy*, *Load Balance* ou Redirecionamento de requisições pode impactar no funcionamento do cache.

O uso do cache do IIS é uma excelente solução, porém é necessário garantir sua configuração conforme os recursos disponíveis de memória e processamento dos servidores WEB.

## Artigos relacionados

IIS - Cache de saída

<https://docs.microsoft.com/en-us/iis/configuration/system.webserver/caching/>

<https://docs.microsoft.com/pt-br/iis/manage/managing-performance-settings/configure-iis-7-output-caching>

Criação de uma política de cache

<https://docs.microsoft.com/en-us/iis/configuration/system.webserver/caching/profiles/add>
