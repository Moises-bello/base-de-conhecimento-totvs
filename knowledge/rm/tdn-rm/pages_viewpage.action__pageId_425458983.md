---
content_hash: 7cf7f252aeffaa9f7e2c2f59097518c0f82250196f03fa53b8c5627e774b18df
fetched_at: '2026-06-29T00:09:33.339860+00:00'
page_id: '425458983'
product: rm
source: tdn-rm
title: Parâmetros - Apontamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458983
version: 2
---

**Apontamento**   
 Uma das funcionalidades agregadas ao módulo de atendimentos é o recurso de apontamentos. Ele serve para manter o tempo que cada atendente atuou no atendimento. Ele mantém as informações de tempo, período, percentual de completude, atividade (o apontamento pode ser realizado para uma atividade e não para um atendimento) e armazena também o grupo de atendimento, tipo de atendimento e etapa/tarefa em que o atendimento se encontra.   Não permite realizar apontamento em um mesmo intervalo de horário para o usuário logado   
    
 O apontamento pode ser feito informando o período de tempo (data inicial e data final) onde o atendente trabalhou no atendimento. Por padrão é permitido que ele insira dois registros de apontamentos com o mesmo período dando a "falsa impressão" de que ele trabalhou em duas coisas ao mesmo tempo. Este parâmetro visa proibir este tipo de registro e a partir do momento que ele esteja marcado o sistema não mais permitirá que se insiram registros de apontamentos onde exista uma interseção entre datas iniciais e finais no mesmo dia, isto é, não permite ao atendente informar que trabalhou em duas atividades (apontamentos) ao mesmo tempo.  
    
 **Atividade referente ao apontamento automático**  
    
 O apontamento pode ser realizado para um atendimento ou para uma atividade. Mesmo quando o sistema funciona com o apontamento automático ele se utiliza de uma atividade para lançar os apontamentos e posteriormente localizá-los e substituir pela chave primária do atendimento, é apenas uma forma de manter um controle entre os apontamentos lançados a ainda não finalizados. Este parâmetro deve ser informado como sendo uma das atividades do cadastro de motivos de atividade/inatividade e que será utilizado neste módulo de apontamento automático.  
    
 **Observação**  
    
 Lembrando que o recurso de apontamento automático é por atendente e deve-se marcar o atributo adequado no cadastro de atendentes para informar ao sistema que para tal atendente o apontamento automático será utilizado.  
    
 **Tempo para que o apontamento automático seja considerado**  
    
 O sistema disponibiliza uma funcionalidade de realizar um apontamento automático sem a necessidade do atendente entrar no módulo de apontamentos e criar um novo registro. Esta funcionalidade começa a contar o tempo no momento que o atendente edita um atendimento e quando fecha a tela de edição de atendimento (ou troca de registro) esta contagem é cessada e um registro de apontamento é lançado. Mas o atendente pode estar navegando entre os atendimentos (pela edição) para encontrar o atendimento a ser trabalhado. O sistema lança registros de apontamentos para atendimento durante a navegação.  
    
 Para evitar este inconveniente, gerar vários apontamentos a medida que se navega, o sistema usa este parâmetro. Caso o tempo que o atendente ficou com a tela aberta em um atendimento for menor que o tempo definido neste parâmetro então o registro de apontamento não é lançado.  
    
 **Observação**  
    
 Lembrando que o recurso de apontamento automático é por atendente e deve-se marcar o atributo adequado no cadastro de atendentes para informar ao sistema que para tal atendente o apontamento automático será utilizado.  
    
 **Não permitir apontamento em atendimento sem etapa**  
    
 Este parâmetro deve ser utilizado quando se deseja que os apontamentos não possam realizados para atendimentos que não estão em nenhuma etapa, ou seja, só será permitido realizar apontamento para um atendimento desde que este esteja em um fluxo e em uma etapa.
