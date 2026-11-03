---
content_hash: d8411d31f65e1f1bbc3c9aa2f8125bce9c0af3ea041f0ceb5dee5116570ce8bd
fetched_at: '2026-06-29T00:09:15.403871+00:00'
page_id: '421385371'
product: rm
source: tdn-rm
title: Cadastro de Ciclos de Transporte
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastro+de+Ciclos+de+Transporte
version: 19
---

---

O ciclo de transporte representará o trajeto ou percurso que os equipamentos realizarão para a retirada de resíduos ou a carga e descarga de materiais a serem utilizados na obra, permitindo o acompanhamento das distâncias e o registro do tempo gasto nesse transporte.

Esta informação é disponibilizada aos coletores e retornada posteriormente ao TOTVS Obras e Projetos com o registro dos respectivos apontamentos, fornecendo os dados necessários para efetuar o cálculo das apropriações.

**Cadastro:**

Para cadastrar um Ciclo de Transporte o usuário deve acessar o menu Controle | Minha Obra | Ciclos de Transporte e inserir (ou editar) um registro de Ciclo de Transporte. O sistema valida se os campos obrigatórios estão preenchidos e só então salva o registro. No cadastro do ciclo de transporte também é informado se as variáveis distância e capacidade do bem irão compor o cálculo do valor para apropriação do Ciclo de Transporte.

ATENÇÂO

Existem algumas situações em que o local de descarga do ciclo pode não estar definido como um ponto especfico ou distância fixa, por ter vários pontos de descarga, desvios, ou acréscimos; e por isso será necessário calcular a distância pecorrida ao final do processo, ao registrar cada descarga no app Minha Obra.

Para atender essa necessidade foi criado um novo tipo de ciclo de transporte chamado "Ciclo por Distancia Pecorrida"  no qual será permitido esse registro da distância percorrida quando realizado apontamento de descarga.

No cadastro do ciclo de transporte será apresentado o campo para definir, a partir do tipo de ciclo de transporte; se a informação da distância é fixa entre o ponto de carga e descarga, ou variável, podendo ser informado na descarga.

Em um mesmo projeto poderão ser utilizados os dois tipos de ciclos.

Abaixo, mostramos duas imagens da tela de cadastro do ciclo. Na primeira, o ciclo é do tipo "Distância Pré-Definida", onde o usuário deverá informar a distância, além dos demais campos que serão descritos mais adiante. Na segunda, o ciclo é do tipo "Distância Percorrida", e o campo da distância passa a considerar a distância fixa entre os marcadores, e já vem preenchido com o valor default, se informado no parâmetro do projeto, podendo ser alterado caso necessário:

 

* **Tipos de Ciclo de Transporte:** Define qual o tipo de ciclo que será considerado no ciclo podendo ser "Distncia Pré-Definida" ou "Distância Percorrida".
  + **Distância Pré-definida:** Nesse tipo de ciclo a distância que o motorista deverá percorrer é conhecida, da carga até a descarga para completar o ciclo;
  + **Distânia Percorrida:** Ao optar por este tipo de ciclo, a distância total do ciclo será calculada após o apontamento da descarga, com base nos marcadores da carga e da descarga e na distância fixa entre os marcadores;
* **Descrição:** Descrição do ciclo de transporte;
* **Insumo:** O ciclo de transportes será associado a um insumo do TOP, que por sua vez contém informações de custo, bem associado ao insumo, unidade de medida, entre outras informações;
* **Distância:** (Km): Distância entre os pontos de carga e descarga. Sua unidade padrão será quilômetros (Km) e seu conceito varia dependendo do tipo de ciclo de transporte usado
  + **Distância Pré - Definida -** É distância entre os pontos de carga e descarga do ciclo.
  + **Distância Percorrida** **-**  O campo da distância passa a considerar a distância fixa entre os marcadores, e somente será possível salvar o ciclo do tipo Distância Pecorrida se o campo estiver preenchido, pois esse valor é usado no cálculo da distância total. Caso esteja informado nos parâmetros , o valor default é carregado automaticamente. Sendo necessário informar uma distância diferente entre os marcadores de um ciclo específico, o sistema permite a alteração do valor default;
* **Ativo:** Indica se o ciclo de transporte está ativo. Caso este campo esteja desmarcado, o sincronismo não enviará este ciclo para o app Minha Obra.
* **Disponível Coletor:** Indica que este Ciclo estará disponível para ser enviado ao coletor associado ao projeto;
* **Considera Distância:** Indica se a distância será utilizada no cálculo da apropriação;
* **Considera Capacidade do Bem:** Indica se a  será utilizada no cálculo da apropriação;

**Importante:**

* + **Inclusão do Ciclo de Transporte - Os campos obrigatórios devem ser preenchidos, são: "Tipo de Ciclo", “Descrição” e “Insumo”;**
  + **Exclusão do Ciclo de Transporte - Para que um ciclo possa ser deletado, ele deve estar inativo, ou seja, o atributo “Ativo” deve estar desmarcado. Além disso, a exclusão de registros de ciclo de transporte somente poderá ser realizada caso não existam no mesmo registros de apontamentos de carga ou descarga.**
  + **Sincronismo de Ciclo de Transporte - Caso no cadastro do Ciclo de Transporte o campo "Ativo" ou o campo "Disponível no Coletor" esteja desmarcado, o sincronismo não enviará o ciclo para o coletor. Caso o ciclo seja desativado após o sincronismo, os apontamentos feitos enquanto estava ativo não poderão ser sincronizados. Será necessário excluir esses apontamentos ou solicitar a reativação do ciclo antes de realizar o sincronismo. Se o ciclo não estiver mais disponível no coletor, mas ainda estiver ativo, os apontamentos realizados poderão ser sincronizados entretanto, o ciclo não estará mais disponível para futuros apontamentos, impossibilitando novas entradas neste ciclo.**

* ****Mapa de Apontamentos - Ciclos de Transporte:****

Para esta funcionalidade existe uma aba dentro da edição do ciclo de transporte chamada **'Mapa'**, durante o registro dos apontamentos informações da localização são coletadas e enviadas no sincronismo para o sistema, com isso é possível verificar as posições dos apontamentos do coletor. Para habilitar esta funcionalidade é preciso configurar em menu Ambiente > Parâmetros > Parâmetros Globais > aba Google, e preencher o campo 'Chave de identificação para o Google Maps'.

**Observação:**

Esta funcionalidade não deverá estar disponível para projetos globais.

   
  Informações Complementares

---

 

 

 

 Como Fazer

---
