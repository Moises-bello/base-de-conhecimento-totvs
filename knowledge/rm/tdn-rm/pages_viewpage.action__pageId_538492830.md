---
content_hash: 621dfbf479dfad9a575e2815b49f7ae73a1b78decf7c2b1d815d7287e810af38
fetched_at: '2026-06-29T00:10:37.234467+00:00'
page_id: '538492830'
product: rm
source: tdn-rm
title: Integrações com Portais - Zap Imóveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=538492830
version: 10
---

# **A) Visão Geral**

---

A integração com o portal ZAP Imóveis, visa publicar dados dos imóveis a serem locados, através de um XML que alimentará os dados relativos ao imóvel que será apresentado no portal. Foram criados dois serviços que estarão disponíveis a partir da versão 12.1.28, O primeiro retornará os dados do imóvel e o segundo, retornará as imagens cadastradas para este imóvel.

Importante: Para que a integração funcione corretamente, o imóvel em questão deverá possuir o campo "Realiza Integração com Portais Externos" marcado.   
Além disso, a URL do Host deve permitir acesso externo, para que os XML's de integração consigam ser lidos pelo portal Zap Imóveis.

# **B) XML de Integração do Imóvel**

---

Este serviço trará no formato de .xml, todos os dados pertinentes dos Imóveis, como sua descrição, imagens, detalhes do valor do aluguel, informações do endereço e do contato cadastrado entre outras. O formato utilizado é o seguinte:

[http://servidor:porta/api/imb/v1/integracao/integra.xml](http://servidorporta)

O .xml será exibido como no exemplo abaixo onde somente um imóvel está com o campo "Realiza integração com portais externos" marcado:

C1I1
Descrição do Imóvel
For Rent

http://localhost:8051/api/imb/v1/integracao//images/1/1/10.jpg
http://localhost:8051/api/imb/v1/integracao//images/1/1/11.jpg

3400.00000000
100

0
1
2
1
1
0

Brasil
Minas Gerais
Belo Horizonte
Santa Lúcia
Endereço
30350-300
1

Nome
email@totvs.com.br
31-21229000

Brasil
MG
SANTA LÚCIA
AVENIDA RAJA GABAGLIA,2664
30350-540
]]>

# **C) Serviço de Imagens do Imóvel**

---

Este serviço será responsável por fazer a leitura da imagem do imóvel que participara da integração. Serão lidas e apresentadas as imagens cadastradas no imóvel, no seguinte formato:

http://servidor:porta/api/imb/v1/integracao/images/CodColigada/CodImovel/CodImagem.jpg

* CodColigada: Coligada do imóvel cadastrado;
* CodImovel: Código do imóvel cadastrado;
* CodImagem: Código da imagem cadastrada.

Exemplo de URL que irá retornar uma imagem: <http://localhost:8051/api/imb/v1/integracao/images/1/1/1.jpg>
