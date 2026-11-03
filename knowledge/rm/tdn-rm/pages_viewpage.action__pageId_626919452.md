---
content_hash: fbd8a8988efd04521dbbc36672c4a75d8e960ca6785c890ab46d5a4b5cb4c6f3
fetched_at: '2026-06-29T00:11:04.367197+00:00'
page_id: '626919452'
product: rm
source: tdn-rm
title: Rascunho_Solicitações de Parcerias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=626919452
version: 1
---

**Solicitações de Parcerias**  
A solicitação de parcerias possibilita ao usuário gerenciar seus processos, permitindo realizar a apresentação, análise, avaliação e cadastro da Parceria, utilizando-se do processo de aprovação através do FLUIG.

Criar no FLUIG os papéis necessários para a execução do fluxo do projeto de inovação. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis.

* Código = pesquisador | Descrição = Pesquisador
* Código = reitoria | Descrição = Reitoria
* Código = contrato | Descrição = Contrato
* Código = jurídico | Descrição = Jurídico

Em seguida, associar os usuários ao respectivo papel cadastrado.

* Associar adequadamente os usuários do FLUIG aos papéis criados anteriormente.
* Importar o fluxo: Solicitação de Parcerias para a ferramenta TOTVS Developer Studio (TDS).

Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em c:\totvs\CorporeRM\ObjetosGerenciais\Fluig.  
  
**Descrição do Processo:**  
Logar com o usuário associado ao papel de: "Pesquisador" e iniciar uma nova solicitação no FLUIG, escolhendo a opção:

* "FLUIG | Iniciar Solicitações | Educacional | Inovação, Pesquisa e Extensão | Solicitação de Parceria | Solicitação de Parceria".

O formulário de cadastro será aberto com o código do pesquisador vinculado ao usuário do FLUIG, sendo esse o usuário que será cadastrado como pesquisador da solicitação de parceria no TOTVS Educacional.  
 Após preencher as informações do cadastro, o usuário enviará a solicitação para "Negociação de Parceria", onde um usuário vinculado ao papel de "Reitoria", irá verificar as informações preenchidas.  
 Nessa etapa, o usuário vinculado ao papel de "Reitoria" terá duas opções:

* Avançar etapa para "Montar Plano de Trabalho";
* Avançar etapa para "Fim", onde a solicitação de parceria não é aprovada e o fluxo é  finalizado.

Na etapa de "Montar Plano de Trabalho", o usuário vinculado ao papel de "Pesquisador", preencherá as informações necessárias e avançará para etapa de "Aprovar Plano de Trabalho", onde outro usuário vinculado ao papel de "Reitoria"  poderá aprovar esse plano de trabalho ou retornar o fluxo ao pesquisador para realizar ajustes. Esse processo pode acontecer quantas vezes for necessário até as informações do plano de trabalho estarem corretas.  
Quando tudo estiver correto, o usuário vinculado ao papel de "Reitoria",  avançará etapa para "Elaborar Instrumento", onde o usuário vinculado ao papel "Contrato" fará a elaboração do contrato (convênio) entre as partes. Nessa etapa é obrigatório a inclusão do contrato como anexo para futura aprovação/reprovação.

Ao avançar etapa para "Avaliar Minuta", o usuário vinculado ao papel de "Jurídico" deverá verificar se o contrato criado está de acordo e caso necessite de algum ajuste, deverá retornar o fluxo para a etapa "Elaborar Instrumento". Esse processo pode acontecer quantas vezes for necessário até as informações do contrato estarem corretas.

Quando tudo estiver correto, o usuário vinculado ao papel de "Jurídico",  avançará etapa para "Assinar Instrumento" (entidade e/ou sistema externo ao fluxo), onde o usuário vinculado ao papel de "Reitoria", assinará o contrato juntamente com o parceiro e o pesquisador. Caso seja encontrado alguma incoerência, o fluxo poderá ser retornado à etapa "Elaborar Instrumento" e deverá passar por todo o processo descrito acima novamente.  
Após a assinatura do contrato, o fluxo seguirá para a etapa de "Liberar Minuta", onde o usuário vinculado ao papel "Contrato" se certificará que está tudo correto e concluirá o fluxo. Nessa etapa ainda existe a possibilidade de encontrar alguma incoerência, nesse caso, o fluxo pode ser enviado à etapa "Elaborar Instrumento" novamente.

Durante toda a execução do fluxo são gerados registros de histórico por etapa de aprovação. Esse histórico é gravado na tabela SPROJSOLICITACAOAVALIACAO e contém informações sobre o usuário aprovador, a etapa movimentada, parecer, data da aprovação, dentre outras.  
  
Para visualizar o fluxo completo, segue abaixo o diagrama de atividades para ter uma visão mais clara do processo descrito.  
  
                                                                               
  
 Informações Complementares

---

[Documento Técnico - Solicitação Parceria](http://tdn.totvs.com/display/LRM/DT_SOLICITACAO_PARCERIA)
