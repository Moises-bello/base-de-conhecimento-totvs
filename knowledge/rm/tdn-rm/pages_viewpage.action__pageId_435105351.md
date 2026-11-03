---
content_hash: 9f9a631237249545350a0296838bb7b19fad4f8856c506eeb7dfcee27412bc5e
fetched_at: '2026-06-29T00:09:49.713729+00:00'
page_id: '435105351'
product: rm
source: tdn-rm
title: Subunidade - Processo - Gerar Imóvel(is) para Aluguel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105351
version: 7
---

Este processo possibilita a criação de Imóveis (Módulo de Aluguéis), a partir de Subunidades cadastradas no sistema.

**Pré-requisitos para a geração de Imóveis a partir de Subunidades:**

* É preciso ter subunidades geradas.
* É preciso ter uma tabela de preço associada a subunidade, pois assim a subunidade terá um preço, que será utilizado na criação do Imóvel. Para maiores informações sobre Tabela de Preço ;

**O processo pode ser executado das seguintes maneiras:**

* + Executado na tela de Empreendimentos: Será realizada a geração de imóveis, com todas as subunidades cadastradas no empreendimento.
  + Executado na tela de Unidades: Será realizada a geração de imóveis, com todas as subunidades cadastradas na unidade.
  + Executado na tela de Subunidades: Será realizada a geração de imóveis, com a(s) subunidade(s) selecionada(s).

**Geração do Imóvel a partir de Subunidade:**

1. Para a geração do imóvel a partir da Subunidade é necessário acessar um dos seguintes cadastros: Empreendimento, Unidades ou Subunidades;
2. Em Processos selecionar a opção "Gerar imóvel(is) para aluguel";
3. Será executado o processo de Geração do Imóvel;
4. Ao final do processo, será exibido uma mensagem informando sobre o resultado do processo;
5. Caso o processo seja executado com sucesso, o Imóvel será criado no módulo de Aluguel, com as informações correspondentes ao que está cadastrado na subunidade;

**Observações:**

* O campo Área Total (m²) do imóvel gerado por este processo será preenchido pelo valor do campo Área (m²) do cadastro da subunidade.
* O valor de locação do imóvel criado pelo processo, será o resultado do valor da subunidade multiplicado pela porcentagem definida no parâmetro **"Cap Rate**",  que se encontra no seguinte caminho Parâmetros >> Totvs Incorporação >> Aluguel >> Imóvel. Para maiores informações sobre o parâmetro **"Cap Rate"** ;

**Figura 1: Subunidade após a geração do Imóvel, passa a possuir um link para o imóvel no qual está associada. A subunidade acima possui o valor de R$ 100.000,00.**   
**Figura 2: Parâmetro de "Percentual do Cap Rate" com o valor de 10%.**

**Figura 3: Imóvel criado pelo processo, no qual se possui um link para a subunidade relacionada. O Valor de locação do Imóvel, foi resultado da multiplicação do valor da Subunidade pela porcentagem do parâmetro Cap Rate.**

* O endereço do imóvel criado pelo processo, será buscado primeiramente no cadastro da Subunidade. Caso a Subunidade não possua endereço, o mesmo será buscado no Empreendimento, no qual é obrigatório;
* O sistema também permite a seleção de coligada ao gerar o imóvel, bastando selecionar uma coligada diferente durante a execução do processo.
* É permitido criar apenas um imóvel para uma subunidade. Dessa forma se o processo for executado em uma Subunidade que já possui um Imóvel, o sistema não permitirá a criação de um novo Imóvel, exibindo uma mensagem de erro no final do processo.
* Caso a Subunidade possua características associadas, as mesmas serão copiadas para o Imóvel a ser gerado. Para maiores informações sobre as características .
* Na criação do Imóvel alguns campos serão preenchidos com valores fixos, segue os campos:
  + Situação do imóvel = disponível para locação;
  + Tipo de área = urbano;
  + Tipo de locação = imóvel;
  + Data de cadastro = data atual;
  + Centro de custo = centros de custo da unidade;
  + Imóvel de propriedade da administradora = marcado;
  + Percentual de propriedade = 100;
  + Locador aceita negociação = desmarcado.

Informações Complementares

---
