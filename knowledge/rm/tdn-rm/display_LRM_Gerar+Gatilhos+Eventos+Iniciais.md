---
content_hash: e02690a8eb66fc84f4c9f401155fa195b7f426e4bf125edb6b77ee110ec37540
fetched_at: '2026-06-29T00:10:07.976351+00:00'
page_id: '452719489'
product: rm
source: tdn-rm
title: Gerar Gatilhos Eventos Iniciais
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerar+Gatilhos+Eventos+Iniciais
version: 3
---

Esse processo tem como objetivo dar inicio a vida da empresa no eSocial, por ele será gerado a carga inicial das informações presentes no base de dados. O processo será divido em duas fases, sendo:

* **1ª Fase -**Eventos de Tabela.
* **2ª Fase -** S-2200 e S-2300, além dos eventos S-2299 e S-2399 caso exista algum funcionário que tenha sido demitido após a data de inicio da obrigatoriedade dos eventos não periódicos.

**O que é um gatilho?**   
 É um registro da fila de eventos do eSocial, ainda sem as informações do XML. Sua função é sinalizar a necessidade de envio de informações para o Governo.

**Quando um gatilho é gerado?**  
 Na carga inicial (Gerar Gatilhos Eventos Iniciais) ou sempre que um fato gerador do eSocial acontece.   
 Exemplos:

* Ao incluir um Funcionário, o sistema irá gerar um gatilho para o evento S-2200.
* Ao alterar um Funcionário, o sistema irá gerar um gatilho para o evento S-2205 ou S-2206.
* Ao excluir um período de gozo de férias, será gerado um gatilho para o Evento de Exclusão (S-3000).

**Observações:**

* Não há a geração de gatilhos automáticos para os "Eventos Periódicos". Para estes, deverá realizar diretamente a geração do XML através do processo de "Gerar XML".
* Para as coligadas que Utilizam Tomadores de Serviços, será necessário executar o processo "Gerar Lotação Tributária" antes de efetuar a Geração dos Gatilhos de Eventos Iniciais.
* Caso seja necessário efetuar mais de uma vez a geração dos eventos iniciais, o sistema apagará todos gatilhos gerados anteriormente e executará novamente o processo se o usuário confirmar a operação. Se houver eventos já integrados com o TAF, não será possível executar esse processo novamente. Nesse último caso, poderá avaliar a necessidade de executar o processo "Limpar Fila de Eventos".
* Ao realizar a Geração dos Gatilhos de Eventos Iniciais da 2ª fase, caso já existam gatilhos de eventos não periódicos na fila de eventos, e que ainda não tenham sido enviados ao TAF, esses serão apagados.
* Poderá parametrizar a geração de Gatilhos Iniciais por Eventos, ou seja, habilitar a seleção de eventos na primeira fase. Na segunda fase será obrigatório a geração dos eventos S-2200 e S-2300 juntos.
* Para executar esse processo, é obrigatório o preenchimento das datas de obrigatoriedade nos parâmetros do eSocial.
