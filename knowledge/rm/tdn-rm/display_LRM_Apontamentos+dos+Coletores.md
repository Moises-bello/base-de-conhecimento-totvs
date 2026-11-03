---
content_hash: 75f7a9f4f0e87c79ce55667a7266022e691959a4177e1a83e43f404e7862181b
fetched_at: '2026-06-29T00:09:13.715024+00:00'
page_id: '421385094'
product: rm
source: tdn-rm
title: Apontamentos dos Coletores
type: documentation
url: https://tdn.totvs.com/display/LRM/Apontamentos+dos+Coletores
version: 24
---

---

Após os coletores (via seus usuários) registrarem seus apontamentos e transmiti-los ao sistema através do sincronismo, estes registros ficam disponíveis para visualização e alteração no anexo Apontamentos dos Coletores no menu Controle | Minha Obra | Ciclos de transporte. Os apontamentos realizados nos coletores entrarão no TOTVS Obras e Projetos com o status "Pendente".

A função do anexo "Apontamentos dos Coletores" é exibir todos os apontamentos provenientes dos coletores com as devidas informações de equipamento, o ciclo, data/hora do apontamento, tipo (carga/descarga), o coletor em que o apontamento foi feito, o usuário que efetuou o apontamento., o equipamento responsável pela carga, e os motivos de inconsistência.  
Além de permitir a visualização dos apontamentos, este anexo da condições aos usuários de realizar ajustes, identificar os emparelhamentos de cargas e descargas referentes aos equipamentos/ciclos para posteriormente efetuar a consolidação destes conjuntos gerando registros de apontamentos na entidade de apontamentos já consolidados (para possibilitar a apropriação).

Nesta tela serão exibidos tanto apontamentos pendentes como conciliados. Sendo assim, são disponibilizados filtros pré-configurados (como um botão na barra de ferramentas da visão) onde tais filtros permitirão uma maior agilidade no gerenciamento dos registros principalmente para localização e seleção para operação em grupo.  Os filtros são de "Apontamentos dos últimos 7 dias", "Apontamentos nos último 30 dias", "Apontamentos por data", "Apontamentos pendentes". Lembrando ainda das funcionalidades inerentes à visão que são a ordenação e agrupamentos por campos, capacidade de se utilizar funções de média, somatórios, etc. por campo.

**IMPORTANTE:** Ao sincronizar os apontamentos de carga e descarga, realizados através da leitura do QR Code, estes já serão exibidos no RM com status "Conciliado" e não "Pendente" como ocorre no apontamento de ciclo de transporte feito sem QR Code, demonstrados na imagem abaixo:

**Observação:**  
Na visão de Apontamentos de Coletores o usuário poderá alterar somente os registros que ainda não foram conciliados, ou seja, os que têm o status "Pendente".

**Editando um apontamento de ciclo de transporte:**

Acesse o menu: Construção \ Obras e Projetos \ Controle \ Minha Obra \ Ciclos de Transporte. No anexo de Apontamentos dos Coletores, inclua ou edite um apontamento sincronizado.

Será exibida a tela abaixo caso o apontamento seja do tipo distância pré-definida:

Para apontamentos de ciclo de transporte cujo tipo seja distância percorrida, além dos campos acima, serão exibidos também os campos de Marcador e Acréscimos (apontamento do tipo descarga):

Os apontamentos de Ciclo de transporte recebidos dos coletores são armazenados no sistema da forma que foram recebidos:

* + Registros correspondentes às cargas dos ciclos (início de ciclo);
  + Registros correspondentes às descargas dos ciclos (fim do ciclo).

Os apontamentos transmitidos ao TCOP entrarão no sistema com o status “Pendente”. Caso os apontamentos tenham sido feitos através da leitura do QR code, os mesmos já serão sincronizados conciliados

Este cadastro apresenta as seguintes informações:

* **Data Apontamento:** Data e hora em que o apontamento foi realizado. A data irá também considerar os minutos e segundo (HH:mm:ss);
* **Tipo de apontamento:** Indica se o apontamento é de Saída ou Entrada;

  + Carga: Indica o início do ciclo;
  + Descarga: Indica o fim do ciclo;

* **Status:** Indica se o apontamento está pendente ou conciliado;

  + - Pendente: Quando o registro foi exportado do coletor e está no sistema. Indica que o registro ainda não foi conciliado;
    - Conciliado: O apontamento já foi utilizado como origem/destino de um apontamento conciliado.
* **Ciclo de transporte:** A que ciclo se refere o apontamento ;
* **Tipo de Ciclo:** Se é do tipo de distância pré-definida ou distância percorrida;
* **Equipamento:** Equipamento que realizará o transporte da carga;
* **Coletor:** Coletor que realizou o apontamento. O coletor deverá estar associado ao mesmo projeto do apontamento;
* **Usuário:** Usuário que realizou o apontamento. Este usuário deverá estar associado ao coletor em que o apontamento foi coletado;
* **Turno:** Caso o parâmetro esteja habilitado o sistema informa em qual turno o apontamento foi realizado; (O parâmetro deve estar habilitado e existir turnos cadastrados no parâmetro de projeto veja detalhes em :[Mobilidade - Turnos (F6)](https://tdn.totvs.com/pages/viewpage.action?pageId=781864972)
* **Equipamento Responsável pela Carga:**Exibe o registro do equipamento que realizou a carga do veículo que irá realizar o transporte (esse campo fica visível somente com a marcação do );
* **Motivo Inconsistência:** Descreve inconsistências encontradas durante o sincronismo do apontamento;
* **Observação:** Campo texto para inclusão de observações sobre os apontamentos;
* **Marcador:** Define o marcador da carga ou descarga;
* **Acréscimos:** Quando existe algum desvio indicando um acréscimo ou impactando no cálculo realizado entre os marcadores e a distância fixa, deverá ser informado nesse campo, no momento da descarga, para que possa compor a distância calculada.

Nos apontamentos do tipo Distância Percorrida, para alterar apontamentos incorretos que já estiverem conciliados, o usuário deverá cancelar a conciliação, editar o campo incorreto e realizar a conciliação manual dos apontamentos; para que o recálculo da Distância Percorrida seja realizado conforme as novas informações.

Para apontamentos retroativos há um parâmetro que determina o  número máximo de dias que um usuário pode retroceder. [Saiba mais](https://tdn.totvs.com/pages/viewpage.action?pageId=421385196)

**Campos Complementares** Essa aba somente estará disponível caso existam campos complementares cadastrados para os apontamentos de ciclo de transporte. 

A criação desses campos complementares é feita no menu "Cadastros Gerais | Campos Complementares | Apontamentos de Ciclo de Transporte". Veja os detalhes em:

Após serem cadastrados, os campos ficarão visíveis na aba "Campos complementares" ao editar apontamento, e será possível definir quais desses campos complementares estarão disponíveis nos apontamentos de Ciclo de Transporte do App Minha Obra, através de parametrização de projeto em .

 Como Fazer

---
