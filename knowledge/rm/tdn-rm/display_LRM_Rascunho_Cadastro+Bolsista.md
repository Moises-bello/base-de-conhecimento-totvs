---
content_hash: ce86d1635c3116be51e8d9e637e4ed73c1bdb14dc9364c699f683d1dec3cf44e
fetched_at: '2026-06-29T00:11:04.348366+00:00'
page_id: '626919382'
product: rm
source: tdn-rm
title: Rascunho_Cadastro Bolsista
type: documentation
url: https://tdn.totvs.com/display/LRM/Rascunho_Cadastro+Bolsista
version: 1
---

O ***Cadastro de Bolsistas (é realizado após a aprovação do Projeto de Pesquisa)***, possibilita ao usuário gerenciar seus processos referentes ao cadastro do bolsista, permitindo realizar o cadastro, submeter a análise e avaliação utilizando-se do processo de aprovação através de FLUIG.   
Criar no FLUIG os papéis necessários para a execução do fluxo do projeto de inovação. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis.  
Código = pesquisador | Descrição = Pesquisador  
Código = reitoria | Descrição = Reitoria  
    
 Em seguida, associar os usuários aos respectivos papeis cadastrados.  
Associar adequadamente os usuários do FLUIG aos papéis criados anteriormente.  
    
Importar o fluxo: Cadastro de Bolsistas para a ferramenta TOTVS Developer Studio (TDS).   
 Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em c:\totvs\CorporeRM\ObjetosGerenciais\Fluig.  
 ·       
 **Descrição do Processo:**  
 Logar com o usuário associado ao papel de: "Pesquisador" e iniciar uma nova solicitação no FLUIG, escolhendo a opção:

* "FLUIG | Iniciar Solicitações | Educacional | Inovação, Pesquisa e Extensão | Solicitação de Parceria | Solicitação de Parceria".

Serão listados apenas os projetos onde o usuário logado seja coordenador.  
 Após preencher as informações necessárias ao cadastro do bolsista o usuário enviará a solicitação para "Confirmar Cadastro Bolsista", onde um usuário vinculado ao papel de reitoria vai verificar as informações preenchidas e confirmar esse cadastro. Existe a opção também de recusar esse cadastro. Nesse caso o fluxo será concluído com "Cadastro Recusado".  
 Caso a solicitação esteja sendo feita para um bolsista já existente, as bolsas serão listadas na primeira etapa e o usuário poderá alterar a data início e data fim dessas bolsas, incluir novas bolsas ou excluir bolsas existentes.  
 Bolsas com lançamento financeiro vinculado (campo IDLAN preenchido na tabela SPROJSOLICITPGTOTIPOBOLSA) não poderão ser excluídas do cadastro do bolsista.  
 Ao avançar para a etapa "Confirmar" o fluxo verificará se o pesquisador que está sendo cadastrado como bolsista é maior de idade. Caso seja maior de idade, o fluxo será redirecionado para o bolsista onde o mesmo realizará o aceite dos termos do bolsista. Caso seja menor de idade, o fluxo identificará, através do RA preenchido pelo pesquisador, qual é o responsável acadêmico desse candidato a bolsista, e redirecionará o termo de aceite para ele.  
 Nas duas situações, "Aceite dos Termos pelo Bolsista" e "Aceite dos Termos pelo Responsável", após o aceite desses termos, o fluxo será encaminhado para o coordenador do projeto para que o mesmo possa confirmar o termo de aceite e concluir o fluxo como "Cadastro Confirmado".  
 Nessas três etapas "Aceite dos Termos pelo Bolsista", "Aceite dos Termos pelo Responsável" e "Aceite dos Termos", existe a ação de recusar o termo, "Termo de Aceite Não Confirmado", onde o fluxo é concluído sem que o bolsista seja cadastrado como ativo.  
 Para visualizar o fluxo completo, segue abaixo o diagrama de atividades para ter uma visão mais clara do processo descrito.  
    
    
                                 
    
  

 Informações Complementares

---

[Documento Técnico - Cadastro Bolsistas](http://tdn.totvs.com/display/LRM/DT_CADASTRO_BOLSISTA)
