---
content_hash: 6e11686c732f60bb89b75ec4948a2b0c6b1d4efeef45f3bbe1960effe7801c1d
fetched_at: '2026-06-29T00:09:30.790975+00:00'
page_id: '425458525'
product: rm
source: tdn-rm
title: Gerar Atendimentos a partir de um Grupo de E-mail
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerar+Atendimentos+a+partir+de+um+Grupo+de+E-mail
version: 3
---

**Gerar Atendimentos a partir de um Grupo de E-mail**   
Esta funcionalidade permite que os e-mails da caixa de entrada (informado no cadastro de Grupo de E-mails) sejam transformados em atendimentos do RM Agilis de acordo com o modelo especificado. O recurso possui a possibilidade de armazenamento de anexos (caso existam no e-mail) e o repasse ao atendente definido como responsável.   
Este serviço permite a otimização do processo através da parametrização de sua recorrência e dispensabilidade de intervenções manuais. De acordo com o programado para execução, a caixa de entrada do e-mail será verificada e cada e-mail será transformado em um atendimento, tendo opções de repasse no Grupo de E-mail ("Manter um atendente fixo", "Repassar ao grupo de atendentes" ou "Definido através do avanço de Etapa").   
Ao final do serviço será encaminhado um e-mail a todos os integrantes do Grupo de Atendentes, alertando sobre a abertura do novo atendimento. Este procedimento é realizado para todos os grupos de e-mails cadastrados.  
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
O sistema disponibiliza a leitura de e-mail utilizando o padrão universal MIME, ou seja, os e-mails serão lidos para qualquer servidor de e-mail que siga esse mesmo padrão, como por exemplo, hotmail, gmail, yahoo e bol. Mas, para pleno funcionamento do recurso o usuário da máquina servidora deve possuir acesso ao caminho e a porta do servidor que serão utilizados no serviço.  
**Atenção**  
Para que o serviço funcione corretamente a parametrização do Grupo de E-mail ( Cadastros| Grupo de E-mails) deve ser feita. Nela são configurados: o endereço de e-mail que terá os e-mails transformados em atendimentos, o modelo do atendimento, o atendente responsável e o grupo de atendentes que receberão os e-mails informativos sobre a abertura dos atendimentos.  
Após a execução do serviço, os e-mails da caixa de entrada do endereço cadastrado no grupo, serão deletados.  
Para qualquer serviço desabilitado, verifique com o Supervisor as permissões do usuário em questão em Cadastros | Segurança| Perfis | Acesso a Menus.

**Importante:**

Alguns servidores de e-mail descontinuaram o acesso via POP, verifique o link abaixo se for o caso
