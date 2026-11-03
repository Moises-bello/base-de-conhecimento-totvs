---
content_hash: 70c01812734f6207e9e25fcd2f7586015c749750bf88ec2fe21400f296338162
fetched_at: '2026-06-29T00:10:56.926423+00:00'
page_id: '593452987'
product: rm
source: tdn-rm
title: Aluguel - Busca de Imóveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=593452987
version: 14
---

#FF9900Introdução

Visando facilitar as operações dos corretores quando lidam com um número grande de imóveis, foi desenvolvida uma busca de imóveis, que permite ao usuário uma pesquisa rápida ao backoffice para consultar os imóveis disponíveis para locação, e possível localizar além da *Busca*outras opções através do campo de pesquisa.

#FF9900Procedimentos para utilização

Para realizar a busca de um imóvel o usuário deveria preencher primeiro algum campo referente ao endereço do mesmo para que seja exibido no Portal de Imóveis, como mostra a imagem abaixo:

Ao preencher alguns dos campos, como bairro, cidade, quartos e valor do aluguel o usuário deverá clicar no botão "Encontrar Imóveis".

* É importante lembrar que somente os imóveis cujo status seja "disponível para locação" serão mostrados na busca.
* O portal irá também mostrar um registro para cada área do imóvel disponível.
* Caso existam muitos imóveis a serem exibidos, o sistema irá paginar a página e mostrar um botão de "carregar mais" no final da página. Por padrão serão exibidos os 5 primeiros imóveis que atendam os critérios da busca.

Na imagem acima, o usuário fez a busca por uma cidade, no caso Campinas. E também pelos bairros Centro e Cambuí. Podemos então remover todos os resultados ou somente um termo da busca, dando flexibilidade ao usuário. Para remover um termo basta clicar no X após a palavra. Ao remover um termo da pesquisa automaticamente o Portal de Imóveis irá refazer a pesquisa com os termos restantes.

Os resultados serão apresentados de duas formas. A padrão é em lista, porém podemos mudar para uma exibição de cards.

Será possível também ordenar os imóveis por valor, do menor para o maior e também do maior para o menor.

##### **Exibição dos imóveis em forma de lista**

---

##### **Exibição dos imóveis em formato de cards**

---

A exibição dos imóveis, independente dos parâmetros de exibição, contará com dados resumidos do cadastros dos mesmos no Backoffice RM.

Serão apresentados os campos de Quantidade de Quartos, o Valor da locação em reais (Valor do metro quadrado quando a área é fracionada) e área total do imóvel.

Além dessas informações, podemos clicar na opção "Ver Mapa". que abrirá um link externo com as informações de localização do endereço no Google Maps.

Caso a busca não retorne resultados, será apresentado um texto afirmando que não foram encontrados imóveis.

##### **Botão + Detalhes**

---

Ao pressionar este botão o usuário será apresentado com os detalhes do imóvel. Com maiores informações sobre o imóvel selecionado. Nesta tela serão apresentados campos como observações, localização, características e valor do aluguel, bem como as imagens do imóvel.

Ao clicar na imagem, o usuário será apresentado com um carrossel, facilitando a exibição de todas as imagens cadastradas no empreendimento. Este carrossel pode ser acessado também ao clicar na imagem do imóvel quando o mesmo aparece numa busca.
