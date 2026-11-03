---
content_hash: 5fc58e86b2df1e93e5920dfe29061e460cb907d3f017bbd8c0abc3a4a675fbfc
fetched_at: '2026-06-29T00:11:04.332350+00:00'
page_id: '626919346'
product: rm
source: tdn-rm
title: Rascunho_Acompanhamento de Bolsista (Desistência)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=626919346
version: 1
---

O ***Acompanhamento de Bolsista(Desistência)***, possibilita ao usuário gerenciar seus processos referente ao acompanhamento de desistência, permitindo solicitar sua desistência do projeto em andamento, através de uma justificativa que será encaminhado para avaliação da comissão.  
    
 ð Criar no FLUIG os papéis necessários para a execução do fluxo do projeto de inovação. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis.  
    
 §   Código = pesquisador | Descrição = Pesquisador  
    
 Em seguida, associar os usuários aos respectivos papeis cadastrados.  
 ð Associar adequadamente os usuários do FLUIG aos papéis criados anteriormente.  
    
 ð Importar o fluxo: "Cadastro Projeto de Pesquisa Extensão" para a ferramenta TOTVS Developer Studio (TDS).   
 Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em c:\totvs\CorporeRM\ObjetosGerenciais\Fluig.  
 ·       
 **Descrição do Processo:**  
 Logar com o usuário associado ao papel de: "Pesquisador" e iniciar uma nova solicitação no FLUIG, escolhendo a opção:

* "FLUIG | Iniciar Solicitações | Educacional | Inovação, Pesquisa e Extensão  | Acompanhamento Bolsista (Desistência) | Acompanhamento Bolsista (Desistência)"

O usuário deve iniciar uma nova solicitação escolhendo a opção "Educacional | Inovação, Pesquisa e Extensão | Acompanhamento Bolsista (Desistência) | Acompanhamento Bolsista (Desistência)". É necessário estar vinculado ao papel de "Pesquisador" para realizar essa solicitação.  
 Após preencher as informações necessárias ao acompanhamento do bolsista o usuário enviará a solicitação para "Confirmar Desistência/Desligamento", onde o coordenador do projeto vai verificar as informações preenchidas. O coordenador do projeto será identificado automaticamente e o fluxo será encaminhado para ele ao avançar a etapa.  
  Após validar as informações preenchidas pelo bolsista, o coordenador do projeto terá duas opções:  
 ·  Avançar etapa para "Desistência/Desligamento Confirmado".  
 Os dados serão gravados na base RM (SPROJDESISTENCIABOLSISTA) aprovando a desistência do bolsista (DESISTENCIAAPROV = S). O fluxo será concluído como "Desistência/Desligamento Confirmado  
 ·  Avançar etapa para "Desistência/Desligamento Não Aceito".  
 Os dados serão gravados na base RM (SPROJDESISTENCIABOLSISTA) negando a desistência do bolsista (DESISTENCIAAPROV = N). Será obrigatório informar um parecer e o fluxo será concluído como "Desistência/Desligamento Não Aceito".  
 Caso o bolsista tenha algum valor a receber, o mesmo deverá executar o fluxo de "Acompanhamento de bolsista (Frequência)" antes de solicitar sua desistência.  
    
 Para visualizar o fluxo completo, segue abaixo o diagrama de atividades para ter uma visão mais clara do processo descrito.  
    
    
          
    
    
  

 Informações Complementares

---

[Acompanhamento de Bolsista (Desistência)](http://tdn.totvs.com/display/LRM/DT_ACOMPANHAMENTO_BOLSISTA_DESISTENCIA)
