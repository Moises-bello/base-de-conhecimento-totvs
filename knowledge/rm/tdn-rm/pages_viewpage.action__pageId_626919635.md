---
content_hash: a8570f4efd63bca635b8d9be975f3ad71b87aa879d2d777aba3ac83e9cb514bc
fetched_at: '2026-06-29T00:11:04.448130+00:00'
page_id: '626919635'
product: rm
source: tdn-rm
title: Rascunho_Solicitação de Reembolso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=626919635
version: 1
---

O auxílio para visitas técnicas/eventos permite ao usuário gerenciar as solicitações de reembolso realizadas através da plataforma FLUIG.  
 Criar no FLUIG os papéis necessários para a execução do fluxo do projeto de inovação. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis.  
 Código = aluno| Descrição = Aluno  
 Código = reitoria| Descrição = Reitoria  
 Código = pesquisador| Descrição = Pesquisador  
    
 Em seguida, associar os usuários aos respectivos papeis cadastrados.  
 Associar adequadamente os usuários do FLUIG aos papéis criados anteriormente.  
    
 Importar o fluxo: Auxilio para visitas Técnicas/Evento para a ferramenta TOTVS Developer Studio (TDS).   
 Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em c:\totvs\CorporeRM\ObjetosGerenciais\Fluig.  
 ·       
 **Descrição do Processo:**  
 Logar com o papel de: Aluno deverá iniciar uma nova solicitação no FLUIG, escolhendo a opção:

* "FLUIG | Iniciar Solicitações | Educacional | Inovação, Pesquisa e Extensão | Visita Técnica/Evento | Auxílio para Visitas Técnicas/Eventos"

Ao selecionar esse fluxo será apresentado um formulário com o código do aluno vinculado ao usuário do FLUIG. Nele deverão ser informados a visita técnica/evento, os dados do reembolso e os tipos de auxílio. Após o preenchimento do formulário o fluxo avançará para a atividade "Aprovar Solicitação de Auxílio", onde um usuário vinculado ao papel "Reitoria" deverá avaliar os dados preenchidos e toda a documentação anexada. Após finalizar a avaliação ele terá 3 opções:  
    
          Retornar para a atividade "Solicitar Auxílio";           Reprovar Solicitação de Auxílio;  
           Avançar para a atividade "Analisar Documentação".  
    
 Na atividade "Analisar Documentação" o pesquisador, que solicitou a visita técnica/evento, deverá analisar os dados preenchidos e toda a documentação anexada. Após finalizar a avaliação ele terá duas opções:  
    
           Retornar para a atividade "Solicitar Auxílio";           Finalizar o Fluxo de Solicitação Auxílio.  
    
 Assim que o fluxo for finalizado o pesquisador deverá retornar para o processo "Solicitação de Visitas Técnicas/Eventos" e, na etapa "Executar Visita Técnica/Evento e Elaborar Relatório Final", anexar a documentação enviada pelo aluno.   
    
    
 Para visualizar o fluxo completo, segue abaixo o diagrama de atividades para ter uma visão mais clara do processo descrito.  
  

 Informações Complementares

---

[Documento Técnico - Solicitação de Reembolso Visitas Técnicas/Eventos](http://tdn.totvs.com/display/LRM/DT_AUXILIO_VISITA_EVENTO)
