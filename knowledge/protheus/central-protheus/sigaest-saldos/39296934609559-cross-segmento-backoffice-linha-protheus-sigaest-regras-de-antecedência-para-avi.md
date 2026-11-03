---
article_id: 39296934609559
category: SIGAEST - SALDOS
content_hash: e5c206b7d0e42563759d0327375ccc8d2eb949cce76464b88bef0636ee728e96
fetched_at: '2026-06-28T22:39:14.941151+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Regras de antecedência
  para aviso de vencimento ESTA010
type: support-article
updated_at: '2026-03-31T20:36:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39296934609559-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Regras-de-anteced%C3%AAncia-para-aviso-de-vencimento-ESTA010
---

A rotina Cadastro de Regras de Antecedência (ESTA010) permite configurar alertas automáticos por e-mail sobre vencimento de lotes, definindo dias de antecedência. Após cadastrar a regra, deve-se configurar o Evento 089 no Event Viewer para envio dos avisos e agendar a rotina ESTA010A para execução periódica no Schedule, garantindo notificações automáticas conforme regras estabelecidas.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39296934605335) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Como configurar o sistema para enviar notificações automáticas de aviso de vencimento de lotes de produtos?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus - SIGAEST - Versão 12.1.2510)

**Solução**  
A rotina **Cadastro de Regras de Antecedência (ESTA010)** permite definir com quantos dias de antecedência o sistema deve alertar sobre o vencimento de um lote. Essa notificação é integrada ao Event Viewer, permitindo o envio de alertas por e-mail para usuários ou grupos específicos.

Veja um vídeo do Processo:

**Passo a Passo**  
**1. Pré-requisitos Técnicos**  
Certifique-se de que o pacote de expedição contínua do Backofficecom (data igual ou superior a 12/11/2025) esteja aplicado.

Execute o compatibilizador de dicionário UPDDISTR utilizando o arquivo de dicionário contido no pacote de expedição.

**2. Configuração do Menu**  
Caso a rotina não esteja visível em seu menu (devido ao release de transição), adicione-a manualmente via Configurador (SIGACFG):

**Programa**: ESTA010  
**Módulo**: 04 (Estoque/Custos)  
**Sugestão de caminho**: Atualizações -> Cadastros -> Produtos -> Regras de dias de antecedência.

**3. Cadastro da Regra (ESTA010)**  
Acesse a rotina Regras de dias de antecedência para vencimento e clique em Incluir.

Defina a abrangência da regra: Pode ser por Produto, Tipo de Produto, Grupo de Produto ou Categoria.

Caso deseje uma regra global para todos os produtos, deixe os campos de filtro em branco.

No campo "Dias Anteced.," informe a quantidade de dias antes do vencimento que o alerta deve ser gerado (Ex: 100 dias) e confirme a gravação.

**4. Configuração do Event Viewer**  
No Configurador (SIGACFG), acesse Ambiente -> Cadastros -> Inscrição Event Viewer.

Localize ou inclua o Evento 089 (Aviso antecipado de vencimento de lote).

Configure os parâmetros:

**Canal**: 002 (Ambientes).  
**Categoria**: 001 (Módulos).  
**Envio de E-mail**: Sim.  
Vincule o Usuário, Grupo ou E-mail que deverá receber as notificações.

**5. Agendamento do Processo (Schedule)**  
No Configurador (SIGACFG), acesse Ambiente -> Schedule -> Schedule.

Crie um novo agendamento para a rotina ESTA010A.  
Defina a periodicidade (ex: Diária) e o horário de execução (ex: 22:00).  
Na aba de parametrização, selecione a Empresa, Filial e o módulo 4 (Estoque/Custos).

Ao final da execução programada, o sistema verificará os lotes e enviará os e-mails conforme as regras cadastradas.

**Saiba mais:**

[*Mais artigos sobre Saldos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538801-SIGAEST-SALDOS)
