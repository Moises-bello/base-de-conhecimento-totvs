---
content_hash: e002b7d456c77d31337665c8317f57f1b5e25d691cb990a546de1727464ce065
fetched_at: '2026-06-28T21:35:18.603603+00:00'
page_id: '172295291'
product: fluig
source: tdn-fluig
title: Utilizando o Guia de Estilos
type: documentation
url: https://tdn.totvs.com/display/fluig/Utilizando+o+Guia+de+Estilos
version: 36
---

true.\*ndicenone

# Sobre

---

Com o **fluig 1.4** lançamos o ***fluig Style Guide***, o guia de estilos que ajuda que desenvolvimentos sobre a plataforma sejam mais ágeis e que gerem um visual padrão do fluig mesmo no caso de personalizações.

Este guia é destinado a desenvolvedores que desejam construir páginas, *widgets* e formulários com as folhas de estilos (CSS) do guia de estilos do fluig.

## O Guia

---

Temos um guia para o acesso completo a todos os componentes do guia de estilo, antes de desenvolver observe a documentação e exemplos de uso.

Documentação Online

Acesse [style.fluig.com](http://style.fluig.com/) e confira todos os componentes disponíveis

Documentação no seu fluig

A sua instalação do fluig também possui o style Guide para consult e terá exatamente o que sua atualização permite utilizar, visto que regularmente trazemos novos componentes para o Style Guide.

Acesse **<seu endereço do fluig>/style-guide** para consultar seu Style Guide disponível.

Exemplo de URL: <https://suaempresa.fluig.com/style-guide>

## Passos para Utilização

---

Os seguintes passos devem ser observados para a utilização do fluig Style Guide:

passosPasso 1

* Importe os artefatos necessários no seu desenvolvimento.

xmlArtefatostrue

]]>

Será necessário ter as fontes locais, pois alguns navegadores impedem carregamento de outros domínios, acrescente no seu ambiente as fontes e altere o CSS acima.

Atenção

Ao ser liberado o Fluig 1.4, todos os *layouts* de páginas do fluig receberão essas linhas por padrão, por isso não será necessário adicionar essas linhas manualmente.

Passo 2

* Encapsule seu código sobre a classe ***fluig-style-guide***. Assim você não afeta outros desenvolvimentos que ainda não usam fluig Style Guide.

xmlColocando seu código dentro da classetrue
