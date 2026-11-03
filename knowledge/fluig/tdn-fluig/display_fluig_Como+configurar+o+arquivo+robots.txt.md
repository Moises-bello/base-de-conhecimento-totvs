---
content_hash: 527b36b64ad3938607e9a8dc72002ef5fe7e7c9c5beff005758e9152f6fc2b24
fetched_at: '2026-06-28T21:35:28.310416+00:00'
page_id: '651290256'
product: fluig
source: tdn-fluig
title: Como configurar o arquivo robots.txt
type: documentation
url: https://tdn.totvs.com/display/fluig/Como+configurar+o+arquivo+robots.txt
version: 9
---

4true.\*ndicenone

# Objetivo

---

Este guia visa mostrar como configurar o arquivo robots.txt.

# Detalhes técnicos

---

Conforme informado no guia de [boas práticas de segurança](https://tdn.totvs.com/x/yUZrJ), é importante configurar o arquivo robots.txt. Esse arquivo é constituído por regras que controlam quais arquivos os rastreadores podem acessar em um site.

A partir da atualização **1.7.1-211207** o arquivo robots.txt é instalado por padrão na plataforma, no diretório [instalação\_fluig]/repository/wcmdir, o qual já encontra-se configurado para bloquear todos os agentes de rastreamento de arquivos. É recomendável alterar esse arquivo, incluindo todas as configurações necessárias para ser indexado.

Caso a utilização do arquivo robots.txt seja via configuração de proxy, o usuário poderá continuar usando via proxy ou mover a configuração ou o arquivo existente para o diretório [instalação\_fluig]/repository/wcmdir robots.txt.

Por questões de segurança é recomendável que a configuração permita liberar somente as páginas que realmente devem ser indexadas.

# Permitir o rastreamento dos arquivos

---

Caso queira permitir o rastreamento dos arquivos no seu site por todos os agentes, deve-se alterar o arquivo robots.txt para:

User-agent: \* Allow: /

Lembrando que o procedimento acima não é recomendado, pois torna de conhecimento público a existência do seu site, expondo algumas informações de acesso. Para mais informações de como configurar o arquivo robots.txt, [acesse aqui](https://developers.google.com/search/docs/advanced/robots/create-robots-txt?hl=pt-br).
