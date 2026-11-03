---
content_hash: 94cf46a7e3b2bd47df3c8c9c8bb2eaa97312812ba23c9ca2e7909a140ab7fd43
fetched_at: '2026-06-29T00:09:28.574821+00:00'
page_id: '423938713'
product: rm
source: tdn-rm
title: Opções de Agregação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938713
version: 2
---

Esta pasta permite agregar os objetos de manutenção filhos para o objeto de manutenção pai selecionado.   
Na agregação quando um objeto filho tiver um indicador de uso desabilitado na pasta indicador de uso e o mesmo for igual ao do pai, após a agregação o indicador de uso será habilitado no objeto filho.  
Procurar Objeto de Manutenção:  
Esta opção permite a localização rápida de Objetos de Manutenção pelo primeiro identificador, modelo, submodelo ou tipo de objeto. Digite parte do nome do Objeto de Manutenção que se deseja consultar que automaticamente irá diferenciar os objetos.   
Caso o objeto procurado seja encontrado, o cursor irá parar exatamente na linha em que se encontra o objeto cujo identificador coincida com o informado, exemplo: Selecione o (s) objeto(s)-filho(s) que será(ão) vinculado(s) ao objeto-pai e clique no botão "<<".   
É necessário que o objeto-filho tenha sido cadastrado previamente e obrigatoriamente tenha a mesma unidade de indicador de uso que o objeto pai. Para remover um agregado, selecione-o e clique no botão ">>".  
Para efetuar a agregação de tipos objetos, a mesma dever estar configurada em Opções | Parâmetros | Tipos de Objetos de Manutenção, edição de um Tipo de Objeto de Manutenção, pasta Opções de Agregação.   
Para agregar um determinado Tipo de Objeto em outro com o qual ele não esteja vinculado (cadastrado), a agregação não será permitida.   
Caso exista o vínculo (exista o cadastro da agregação), serão disponibilizadas as posições pré-cadastradas entre esse dois Tipos de Objetos.  
Para localizar o objeto agregado, objeto pai ou objeto raiz, basta clicar com o botão direito sobre os objetos do lado esquerdo e selecionar a opção desejada.  
   
**Ordenar Visão dos Objetos Agregados**

Para ordenar a visão dos objetos agregados na tela de objeto de manutenção basta escolher uma das duas opções, por tipo ou por objeto, e marcá-la.   
Ao selecionar a opção "Identificador do objeto", os objetos agregados serão ordenados pelo identificador e ao clicar em "Tipo / Posição objeto" os objetos serão ordenados pelo tipo.  
***Atenção!*** Ao fazer uma agregação e os objetos de manutenção pai e filho estiverem integrados a um BEM no RM Bonum (pasta integração) e os BENS integrados ao objeto pai e filho estiverem em filial e/ou local diferente, o sistema emitirá uma mensagem que será necessário realizar uma transferência física de BENS no RM Bonum entre a filial e/ou local para que o sistema prossiga com a agregação do objeto filho no objeto pai.

Caso seja feito um cancelamento da transferência física entre filial e/ou local do BEM no RM Bonum e esse BEM estiver integrado a um objeto de manutenção pai, o sistema irá permitir o cancelamento de transferência.   
Mas se o BEM estiver integrado a um objeto filho ao fazer a transferência, o sistema emitirá uma mensagem informativa.  
Não é permitido fazer "Lançamentos de Indicadores de uso" e/ou "Alteração de medidor" para objeto filho.   
Quando é feita uma agregação, os anexos, "Histórico de indicadores de uso" e "Alteração de medidor", ficam ocultos para o objeto filho.   
Após a desagregação do objeto os anexos voltam a ficar visíveis.
