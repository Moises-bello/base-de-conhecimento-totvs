---
content_hash: 95cab905348159489c5ab5eb033af9e1600344a54f55f0e51783043348e58c1a
fetched_at: '2026-06-29T00:11:04.338155+00:00'
page_id: '626919358'
product: rm
source: tdn-rm
title: Rascunho_Acompanhamento de Bolsista (Frequência)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=626919358
version: 1
---

O ***Acompanhamento de Bolsista(Frequência)***, possibilita ao usuário gerenciar seus processos referentes ao acompanhamento de frequência, permitindo informar suas atividades desenvolvidas naquele projeto mensalmente, e encaminhado para a avaliação (será aprovado pelo responsável pelo Projeto).

ð Criar no FLUIG os papéis necessários para a execução do fluxo do projeto de inovação. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis.  
 §   Código = pesquisador | Descrição = Pesquisador  
 §   Código = reitoria | Descrição = Reitoria  
 §   Código = coordenador\_pesquisa | Descrição = Coordenador de Pesquisa  
 Em seguida, associar os usuários aos respectivos papeis cadastrados.  
 ð Associar adequadamente os usuários do FLUIG aos papéis criados anteriormente.  
    
 ð Importar o fluxo: Acompanhamento de Bolsistas (Frequência) para a ferramenta TOTVS Developer Studio (TDS).   
 Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em c:\totvs\CorporeRM\ObjetosGerenciais\Fluig.  
 ·       
 **Descrição do Processo:**  
 Logar com o usuário associado ao papel de: "Pesquisador" e iniciar uma nova solicitação no FLUIG, escolhendo a opção:

* "FLUIG | Iniciar Solicitações | Educacional | Inovação, Pesquisa e Extensão | Acompanhamento Bolsista (Frequência) | Acompanhamento Bolsista (Frequência)"

Após preencher as informações necessárias ao acompanhamento do bolsista o usuário enviará a solicitação para "Confirmar Frequência", onde o coordenador do projeto vai verificar as informações preenchidas. O coordenador do projeto será identificado automaticamente e o fluxo será encaminhado para ele ao avançar a etapa.  
 Após validar as informações preenchidas pelo bolsista, o coordenador do projeto terá três opções:  
 §   Solicitar o pagamento das bolsas  
 O coordenador do projeto deverá aprovar/reprovar cada atividade informada pelo bolsista. Caso alguma atividade seja reprovada, será necessário informar uma justificativa. O coordenador do projeto deverá avançar para a etapa de "Solicitar Pagamento".  
 §   Retornar o fluxo ao bolsista para algum ajuste que ele julgue necessário  
 O coordenador do projeto poderá, antes de realizar a aprovação/reprovação das atividades, solicitar que o bolsista insira ou altere alguma informação que ele julgue necessário. Ao avançar para "Início - Retorno" o fluxo será devolvido para o bolsista que deverá realizar todo o procedimento novamente para devolver a solicitação ao coordenador do projeto.  
 §   Finalizar como "Ajuste Retroativo de Frequência (pagto bolsa já efetuado)"  
 Nesse caso, o coordenador estará aprovando uma frequência retroativa, ou seja, alguma atividade do bolsista que ficou com status "Não Iniciada" ou "Em Execução" e precisa ser encerrada, o sistema verificará se já houve solicitação de pagamento aprovada para o mês dessa atividade que está sendo lançada, e informará ao coordenador caso o mesmo tente enviar novamente para a tarefa "Solicitar pagamento".  
 Uma decisão automática será executada baseado na identificação de bolsista voluntário.  
 Caso o bolsista seja voluntário, não será necessário realizar nenhum pagamento para o mesmo. O fluxo é concluído como "Bolsista Voluntário (Sem Pagamento)".  
 Caso o bolsista NÃO seja voluntário, será necessário enviar o fluxo para a etapa "Solicitar Aprovação Pagamento", onde o coordenador de pesquisa, verificará as bolsas a serem pagas e solicitará aprovação de pagamento.  
 Após solicitar aprovação de pagamento, o fluxo será encaminhado para o papel da "Reitoria" que realizará a aprovação dessa solicitação de pagamento. Nessa etapa o usuário terá as seguintes opções:  
       §   Reprovar o pagamento concluindo o fluxo como "Pagamento Reprovado".  
         Os dados são gravados na base RM com a solicitação de pagamento reprovada (SPROJSOLICITACAOPGTO).  
       §   Enviar o fluxo para a etapa de "Realizar Pagamento Interno".  
 Após solicitar aprovação de pagamento, o fluxo será encaminhado para o papel da "Reitoria" que realizará a aprovação dessa solicitação de pagamento. Nessa etapa o usuário terá as seguintes opções:  
 §   Reprovar o pagamento concluindo o fluxo como "Pagamento Reprovado".  
 Os dados são gravados na base RM com a solicitação de pagamento reprovada (SPROJSOLICITACAOPGTO).  
 §   Enviar o fluxo para a etapa de "Realizar Pagamento Interno".  
 Na etapa de "Realizar Pagamento Interno" o processamento acontecerá de forma automática (decisão automática), ou seja, o fluxo fará a geração do lançamento financeiro a pagar para cada bolsa de fomento interno que estiver associada à solicitação de pagamento. Nessa etapa o fluxo terá as seguintes opções:  
 §   Caso aconteça algum erro na geração do(s) lançamento(s) financeiro(s), o fluxo permanecerá na etapa "Aprovar Solicitação Pagamento", onde o usuário vinculado ao papel de "Reitoria", deverá averiguar o problema e enviar novamente para a etapa de "Realizar Pagamento Interno".   
 §   Se não houver nenhum problema na geração do(s) lançamento(s) financeiro(s), o fluxo terá duas opções:  
 ·          Enviar para etapa de "Realizar Pagamento Externo"  
 O fluxo verificará automaticamente se existem bolsas de fomento externo vinculados a solicitação de pagamento, e enviará o fluxo para a etapa de "Realizar Pagamento Externo".  
 ·          Concluir o fluxo como "Pagamento Concluído"  
 Caso não existam bolsas de fomento externo, o fluxo será concluído como "Pagamento Concluído".  
 Para a correta geração do lançamento financeiro a pagar é necessário verificar alguns itens:  
 §   A pessoa associada ao usuário do FLUIG deve ter um cliente/fornecedor vinculado, classificado como "Fornecedor". Esse vinculo deve ser feito através do processo "Vincular/Desvincular Cli/For" na visão de pessoa do TOTVS Educacional.  
 §   Caso essa pessoa seja um funcionário da instituição, o vínculo do cliente/fornecedor deverá ser feito através do cadastro de funcionário.  
 §   O cliente/fornecedor vinculado, deve ter Defaults de Cli/For definidos para "Tipo de Documento".  
 As informações serão gravadas na base RM, vinculando o lançamento financeiro à bolsa de fomento interno e solicitação (SPROJSOLICITPGTOTIPOBOLSA e  SPROJSOLICITACAOPGTO).  
 Na etapa de "Realizar Pagamento Externo" o coordenador de pesquisa terá apenas a opção de concluí-la como "Pagamento Concluído".  
    
 Para visualizar o fluxo completo, segue abaixo o diagrama de atividades para ter uma visão mais clara do processo descrito.  
                      
                                                                             

 Informações Complementares

---

[Documento Técnico - Acompanhamento Bolsista (Frequência)](http://tdn.totvs.com/display/LRM/DT_ACOMPANHAMENTO_BOLSISTA_FREQUENCIA)
