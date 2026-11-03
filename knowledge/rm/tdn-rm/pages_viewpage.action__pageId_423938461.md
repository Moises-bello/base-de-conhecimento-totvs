---
content_hash: a3f9e169cdec3326a5636eb05efd8e927caaee0291c0b8681d0d3c8599f4de45
fetched_at: '2026-06-29T00:09:27.247168+00:00'
page_id: '423938461'
product: rm
source: tdn-rm
title: Histórico de Indicadores de Uso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938461
version: 4
---

Neste anexo poderá ser cadastrado os indicadores de uso do objeto de manutenção. Os seguintes campos deverão ser preenchidos:

* **Data da coleta**: Data em que o registro do indicador de uso foi coletado.
* **Medidor**: Valor do medidor.

O Indicador de Uso é composto pelos campos "Medidor" e "Acumulado". O Acumulado só é alimentado através da inserção de vários Medidores.  
***Observação***: Como a descrição do Indicador de Uso é baseada no Tipo de Objeto de Manutenção, somente a descrição dos campos Medidor, Acumulado e Média/Dia é fixa. O título da caixa que engloba estes três campos será de acordo com o Tipo do Objeto de Manutenção, e é cadastrado em Opções | Parâmetros | Tipos de Objetos de Manutenção | edição do Tipo de Objeto | Pasta Identificação. Exemplo: Você tem um objeto Veículo e ele tem um objeto agregado Pneu. Todo indicador de uso inserido no Veículo será replicado ao Pneu. Sendo assim, quando você está na edição do Pneu, pasta Indicador(es) de Uso, selecionamos o indicador de uso que foi inserido no Veículo, e clicamos em Dados do Lançamento Raiz, ele trará o indicador de uso do objeto pai, ou seja, o Veículo que possui o Pneu.  
Por default, quando um novo objeto é cadastrado, todos os indicadores do tipo daquele objeto vêm habilitados. Para desabilitar o uso de um indicador de uso basta desmarcar o "Check Box", mas existe algumas restrições, são elas:

* Para editar um indicador de uso de um objeto pai:

1. 1. Para selecionar não há restrições;
   2. Para desse lecionar, os objetos agregados não podem utilizar o indicador que se deseja não utilizar.

* Para editar um indicador de uso de um objeto agregado:

1. 1. Para selecionar é necessário que o objeto pai possua o indicador que se deseja utilizar;
   2. Para desse lecionar não há restrições.

Para agregar um objeto (seja pela pasta Agregação ou pela visão em árvore) é necessário que os indicadores de uso sejam compatíveis, ou seja, os indicadores de uso do objeto filho devem necessariamente selecionados no objeto pai.  
***Atenção!***Não é possível alterar indicadores de uso em objetos-filhos, devendo proceder a alteração apenas nos objetos-pai.  
O grau de indicador de uso do objeto-pai será distribuído entre todos os objetos filhos agregados, sendo que, se este objeto filho já possuir um grau de identificador de uso, ao determinar um novo valor para o objeto pai, será efetuado a distribuição por diferença para todos os objetos-filhos agregados.
