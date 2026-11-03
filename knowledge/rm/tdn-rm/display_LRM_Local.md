---
content_hash: beced52ca927968e926608102d1ea564de474df074a739381afc9082ff3bea6f
fetched_at: '2026-06-29T00:09:29.793341+00:00'
page_id: '425458282'
product: rm
source: tdn-rm
title: Local
type: documentation
url: https://tdn.totvs.com/display/LRM/Local
version: 8
---

A tabela auxiliar Local armazena todas as dependências físicas situadas nos prédios que serão utilizados nos processos seletivos. Ou seja, um local é basicamente uma sala ou qualquer outro ambiente que será utilizado para aplicação das provas ou lugar de ocupação de profissionais e candidatos em dias de seleção.  Essa tabela também se encontra disponível como anexo da tabela auxiliar "Prédio". Quando acessada do anexo do prédio, serão exibidos somente os locais pertencentes ao prédio selecionado. Ao se cadastrar um local deve ser obrigatoriamente informado em qual prédio ele está situado, assim como tipo de local no qual se enquadra.   
Por exemplo, no prédio "Prédio da Faculdade de Direito", poderá ser cadastrado um LOCAL chamado "Sala 101" do TIPO DO LOCAL "Sala" e outro TIPO DE LOCAL "Banheiro Masculino 1º piso".  
O que caracteriza os locais ou salas é o nº de lugares verticais e horizontais que ele possui. Sendo assim, se tomarmos banheiros como exemplo, concluímos que, em princípio, eles sempre serão cadastrados com os valores zeros para Nº de lugares vertical, Nº de lugares horizontal e Nº de canhotos. Se for uma sala de prova com 50 lugares, então poderá ser 5 o Nº de lugares vertical e 10 o Nº de lugares horizontal.   
Será possível definir se a sala estará preparada para portadores das seguintes necessidades especiais: Física, Auditiva, Fala, Visual, Mental, Intelectual, Reabilitado(BR) ou outra.  Uma vez que um local for cadastrado suportando necessidades especiais, então este local suportará apenas candidatos portadores destas necessidades. Portanto, futuramente quando o processo de alocar candidatos for executado, o mesmo irá alocar nestes locais somente candidatos com estas necessidades parametrizadas na inscrição.

**Utilizações importantes**:  
Alocar candidatos em local de prova dependerá da quantidade de lugares disponíveis. No cadastro "Processo Seletivo" deverá ser informado os locais disponíveis para que sejam utilizados como local de prova de candidato e alocados os profissionais. No Portal o "Comprovante de Inscrição" terá informações referentes do local de prova do candidato.

Informações 

A funcionalidade de parametrizar "Local de prova online" está disponível à partir da versão ***12.1.2306.***

**Local de prova online:** Durante o cadastro de local de prova, tem-se a opção **"Local de prova online".**Ao seleciona-la, este local será parametrizado como prova online.

**Importante**:

* Somente é possível parametrizar **Um(1) local de prova online**, ao tentar realizar o cadastro de um novo local online o sistema não permitirá.

* Este local de prova online deve ter vagas suficiente para o volume de candidatos esperado no processo seletivo, é recomentando que a quantidade de vagas no local seja alta, ou seja, o resultado da operação "Nº de lugares vertical x Nº de lugares horizontal" deve resultar em muitas vagas, por exemplo "500 x 100" totalizando 50 mil vagas, isso é necessário pois o fluxo de execução de avaliações ainda faz uma alocação do candidato, mesmo que de forma fictícia, mas é necessária para a execução das avaliações. Para mais informações acesse:
