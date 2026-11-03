---
content_hash: 16321ad70baeed54d8d6acacb18b8ab39c12576e26fd68374cf8028fde6d32ba
fetched_at: '2026-06-29T00:09:29.795825+00:00'
page_id: '425458283'
product: rm
source: tdn-rm
title: Local de prova do Candidato
type: documentation
url: https://tdn.totvs.com/display/LRM/Local+de+prova+do+Candidato
version: 8
---

Esse serviço que também se apresenta na forma de anexo da tela "Inscrição de Candidato" torna possível visualizar e alterar a o local de prova de um candidato.

**Local de realização da prova:** de acordo com o processo seletivo e área ofertada selecionados, será disponibilizado uma listagem com os locais de realização da(s) prova(s) disponíveis. Serão visualizadas todas as cidades cujos prédios tenham locais de prova disponibilizados para o processo seletivo. Se a instituição tiver optado por informar em quais campus os prédios estão localizados, então essa informação será visualizada na lookup acompanhando o nome da cidade. Uma vez que a instituição tiver optado por detalhar os campus e o candidato tiver especificado um, ele só será alocado em prédios desse campus mesmo existindo prédios em outros campus da cidade.

**Local de prova online:**

Local de prova online

No momento da definição dos locais de prova, o TOTVS Processo Seletivo permite a seleção de um local que seja definido como "**Local de prova online**", este local online permite que o candidato, ao se inscrever pelo Portal do Processo Seletivo não precise selecionar um "Local de prova" na etapa final de inscrição.

O local de prova online possui alguns requisitos de quantidade de vagas, estes requisitos podem ser consultados aqui: .

Após a criação do local do tipo online, cadastrá-lo como um local do processo seletivo em questão, é necessário definir que a área ofertada utilize local online, esta ação é necessária pois é possível cadastrar locais físicos juntamente com o local online no mesmo processo seletivo, porém a área ofertada irá definir se o local utilizado será físico ou online. Para mais informações sobre a área ofertada acesse: 

**Importante**:

* Somente é possível parametrizar **Um(1) local de prova online**, ao tentar realizar o cadastro de um novo local online o sistema não permitirá.

* Estes locais de prova online devem ter vagas suficiente para o volume de candidatos esperado no processo seletivo.

Uma vez que o processo "Alocar Candidatos em Locais de Prova" tenha sido executado para um processo seletivo, a visão deste cadastro exibirá a listagem de candidatos e local em que farão a prova em cada etapa. Ao editar um desses registros, o usuário visualizará os detalhas da alocação. Por meio do campo "Local do processo seletivo" será possível que o usuário altere o local de prova de um candidato.

**Curiosidade**: Neste cadastro é possível realizar a alocação manual do candidato para participar da seleção. Ao salvar uma alocação manual, será verificado se o local comporta na vaga para atual etapa que o usuário participará e só será possível alocar para a 2ª etapa se o candidato estiver com o Status "Classificado para a próxima etapa" após a 1ª seleção e assim por diante.

Informações 

À partir da versão ***12.1.2306***, será incluído automaticamente um local, caso a área ofertada tenha a opção "Usa local de prova online" marcado. Esse local de prova, será um local de prova online, que somente funcionará para alocar candidatos que estão em uma área ofertada que usa prova online.

Para excluir este local de prova, não deve existir nenhuma área ofertada que usa local de prova marcado.
