---
content_hash: 150b89301a3aae07ff13c628b6f5ce5ae178e00f063485bd7bda32c70f7bb4e3
fetched_at: '2026-06-29T00:09:30.386127+00:00'
page_id: '425458459'
product: rm
source: tdn-rm
title: Inserir Discussão/Anexos a partir de E-mails
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458459
version: 1
---

**Inserir Discussão/Anexos a partir de E-mails**   
Esta funcionalidade permite o registro na discussão (do texto do e-mail) e inserção de arquivos anexos a partir de resposta aos e-mails de atendimentos. Essas informações são coletadas do e-mail da caixa postal (informado no cadastro de Grupo de E-mails) sejam inseridos nos atendimentos do RM Agilis de acordo com o modelo especificado.   
Este serviço permite a otimização do processo através da parametrização de sua recorrência e dispensabilidade de intervenções manuais. De acordo com o programado para execução, a caixa postal do e-mail será verificada e as respostas serão inseridas nos respectivos atendimentos.  
É possível controlar quando o serviço será executado:  
Hora de execução (1ª execução)  
Agora = Executa o processo uma única vez e imediatamente na data corrente.  
Executar em = Executa o processo uma única vez e na data e hora especificada. Essa opção possui como padrão a data corrente do dia sendo possível alterá-la.  
Sob demanda = Executa o processo de acordo com o recebimento dos e-mails.  
Repetir a execução  
Deve ser utilizada quando houver a necessidade de executar o processo de forma recorrente. Ela apresenta as seguintes opções:   
• Semanal - Todas as semanas no mesmo horário e no(s) dia(s) de acordo com o definido.  
• Mensal - Todos os meses, no mesmo horário e no(s) dia(s) de acordo com o definido.  
• Diário - Diariamente, a cada intervalo (em horas) de acordo com o definido.  
**Observação**  
Para habilitar esta opção é necessário que a Hora da execução (1ª execução) esteja marcada como "Executar em".  
O sistema disponibiliza a leitura de e-mail utilizando o padrão universal MIME, ou seja, os e-mails serão lidos para qualquer servidor de e-mail que siga esse mesmo padrão, como por exemplo, hotmail, gmail, yahoo e bol. Mas, para pleno funcionamento do recurso o usuário da máquina servidora deve possuir acesso ao caminho e a porta do servidor que serão utilizados no serviço.  
**Atenção**  
Para que o serviço funcione corretamente a parametrização do Grupo de E-mail ( Serviços| Grupo de E-mails) deve ser feita. Nela são configurados: o endereço de e-mail que terá as respostas dos e-mails inseridos nos respectivos atendimentos, o modelo do atendimento e o atendente responsável.  
Os e-mails exibem uma tag de segurança e para que os mesmos sejam inseridos nos atendimentos pelo processo nas repostas a tag não deve ser alterada.  
Para qualquer serviço desabilitado, verifique com o Supervisor as permissões do usuário em questão em Serviços Globais | Segurança| Perfis | Acesso a Menus.
