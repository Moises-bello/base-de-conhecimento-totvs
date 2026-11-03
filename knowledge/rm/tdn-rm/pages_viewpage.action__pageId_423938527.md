---
content_hash: 9aca33c2c25f50cf4b585607820f49b4b1fddcba35c3a2b83fc2e6f427dbefcf
fetched_at: '2026-06-29T00:09:27.501442+00:00'
page_id: '423938527'
product: rm
source: tdn-rm
title: Geração de Lançamentos Periódicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938527
version: 11
---

Dica

A partir da versão 12.1.2310 o processo pode ser executado para várias Estruturas e Coligadas ao mesmo tempo.

Processo responsável por gerar automaticamente lançamentos contábeis baseados em estruturas pré-definidas, possibilitando ao usuário preencher os campos referentes às possíveis variáveis definidas na estrutura selecionada.  
Na execução do processo, serão feitas as mesmas consistências do cadastro de lançamento contábil.

Na tela serão apresentados os dados indicados na estrutura:

* **Lote** - lote onde lançamento será incluído
* **Data** -  data do lançamento
* **Lançamento** - Link que apresenta o lançamento que será gerado com suas respectivas partidas, onde os campos estarão preenchidos conforme os dados da estrutura e as variáveis informadas.
* **Variáveis** - Todas as variáveis criadas e **vinculadas** a algum campo do molde.
* **Lançamento Gerado** – Para cada estrutura, é exibida uma coluna com um link para acessar o lançamento gerado.
  + **Pré-requisito:** os campos obrigatórios devem estar preenchidos.
  + **Acesso:**
    - **Estruturas da coligada corrente:** permitem visualizar, editar e incluir informações adicionais (ex.: rateios gerenciais).
    - **Demais estruturas:** apenas visualização é permitida.

Visualize a tela

**Regras**

* Os lançamentos **não serão incluídos diretamente no lote oficial** da contabilidade, mas sempre em um Lote N. Este lote depois de conferido deverá ser integrado ao lote oficial.
* Os lançamentos **não serão gerados com diferença** entre débitos e créditos.
* O processo irá considerar os valores informados nas variáveis para gerar o lançamento, exceto quando algum valor for editado diretamente na tela de lançamento/partida.
* A edição de lançamentos e partidas só é permitida para estruturas que pertençam à mesma coligada do contexto. As demais estruturas podem ser visualizadas, mas não editadas.

**Observações**

* O processo de Geração de Lançamentos Periódicos executado em ambiente 3 Camadas pode utilizar o recurso de Agendamento de Processos.
* Também para ambiente 3 Camadas, na tela do cadastro de estruturas, está disponível em *Anexos*a opção *Agendamento*. Através desta opção você poderá consultar, acompanhar e gerenciar todas as gerações executadas por estrutura sejam elas executadas imediatamente ou agendadas.

Veja também
