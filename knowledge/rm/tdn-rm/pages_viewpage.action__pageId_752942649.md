---
content_hash: 61db14fbe68c604d8267f928ab8c0c45dbd420dd97494a10753f282ec937c055
fetched_at: '2026-06-29T00:11:33.199106+00:00'
page_id: '752942649'
product: rm
source: tdn-rm
title: Criando cabeçalho de relatório com o logo da Coligada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=752942649
version: 6
---

# Índice:

---

* [Índice:](https://tdn.totvs.com/display/LRM/Compartilhamento+de+Recursos+no+TReports#CompartilhamentodeRecursosnoTReports-%C3%8Dndice:)
* [Introdução:](https://tdn.totvs.com/display/LRM/Compartilhamento+de+Recursos+no+TReports#CompartilhamentodeRecursosnoTReports-Introdu%C3%A7%C3%A3o:)
* [Como Usar:](https://tdn.totvs.com/display/LRM/Compartilhamento+de+Recursos+no+TReports#CompartilhamentodeRecursosnoTReports-ComoUsar:)

# Introdução:

---

          O objetivo dessa página é mostrar como criar um cabeçalho de relatório no Smart View contendo o logo da coligada. Para isso será utilizada a funcionalidade de sub-relatório associada ao Objeto de Negócio de nome Coligadas.

# Objeto de Negócio Coligadas

---

           O Objeto de Negócio (O.N.) Coligadas, disponibilizado na área TOTVS Inteligência de Negócios, foi criado com o intuito de fornecer as informações e o logo de uma coligada. Ele possui como parâmetro obrigatório o Código da Coligada e, por essa razão, sempre retorna apenas um registro. As propriedades que compõem o esquema desse Objeto de Negócio são:

falseColigada

* Código Coligada;
* CNPJ/CPF/CEI;
* Nome;
* Nome Fantasia;
* Rua;
* Número;
* Complemento;
* Bairro;
* Cidade;
* Estado;
* País;
* CEP;
* Logo\*;
Logo\*

O Smart View suporta apenas os tipos primitivos (string, número, data e booleano). Por esse motivo o logo da coligada, que é uma imagem, é entregue como uma string.

# Criando um cabeçalho com imagem utilizando o O.N. Coligadas

---

           Para criar um cabeçalho com imagem, é necessário primeiramente criar um relatório e associá-lo ao Objeto de Negócio Coligadas. Em seguida, no design do relatório, incluir um componente do tipo Caixa de Imagem, arrastar o campo *Logo*nesse componente e  ajustar o tamanho da imagem (sugerimos configurar como "Comprimir"). Ao acessar o Preview do relatório, deve-se preencher o parâmetro de Código da Coligada e, em seguida, será exibido o resultado. O vídeo abaixo mostra esse processo:

75%75%

# Utilizando o cabeçalho em um relatório

---

           Num relatório onde se deseja utilizar o cabeçalho criado, deve-se incluir um sub-relatório apontando para o relatório do cabeçalho e realizar o binding dos parâmetros, conforme mostrado no vídeo abaixo.

Nesse exemplo, o relatório principal já possui um parâmetro de código de coligada. Esse parâmetro será ligado ao parâmetro do sub-relatório, o qual contêm o cabeçalho.

75%75%
