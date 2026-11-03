---
article_id: 31225494448279
category: Avisos Automáticos
content_hash: 6f95ebb2ce256143cb10738c0df35f5a4234e653363816a7590bb4cb38bdb6ec
fetched_at: '2026-06-28T22:46:40.524177+00:00'
product: rm
section_id: 31224122282519
source: central-rm
title: RH - RM - FOP - E-mail do Aviso automático não é enviado
type: support-article
updated_at: '2026-02-18T18:23:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31225494448279-RH-RM-FOP-E-mail-do-Aviso-autom%C3%A1tico-n%C3%A3o-%C3%A9-enviado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31225494408599) Tempo aproximado para leitura: **00:03:30 min**  
  
**Ocorrência**  
Ao tentar enviar um aviso automático, o e-mail não é enviado para nenhum destinatário.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
A falha pode ocorrer devido à configuração incorreta da rotina de envio de e-mails ou à parametrização dos próprios avisos automáticos.  
  
**Solução**  
Para identificar e corrigir a falha, siga os passos abaixo com base nas mensagens exibidas no log de execução da rotina de envio de avisos automáticos:

**Incidente:** Caso a mensagem apresentada seja: **"Buscando registros de avisos para funcionários..."** e **"Nenhum registro de avisos para funcionários atedende as condições"**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31225494409623)

**Solução:** Deve-se acessar o módulo **Folha de Pagamento** no menu **Configurações | Parametrizador | Avisos automáticos** onde marcamos a flag “**Ativar envio de avisos automáticos”**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31225494410903)**

**Incidente:** Caso a mensagem apresentada seja: **"Atualizando registro de aviso..."** e **"Registro de aviso atualizado: Coligada -- Tipo aviso -- Chapa funcionário sem realizar o envio do e-mail"** sem a informação **"Enviando e-mail"** ou **"E-mail enviado"**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31225482880151)

**Solução:** O principal teste a ser realizado é verificar se o envio de e-mails está funcionando corretamente tanto para a **coligada atual** quanto para a **coligada global**. Outra alternativa é executar a rotina acessando **Configurações | Enviar e-mails para Funcionários**. Esse procedimento permite identificar possíveis falhas de configuração no sistema que possam estar impedindo o envio de e-mails em qualquer rotina da Folha de Pagamento.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31225494412439)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31225482882071)

Após ajustar as configurações, execute novamente a rotina de avisos automáticos.   
Se o envio estiver funcionando corretamente, o log exibirá as mensagens:

* Enviando e-mail
* E-mail enviado!  
  antes da mensagem "Atualizando registro de aviso..."
* ![](https://centraldeatendimento.totvs.com/hc/article_attachments/31225494415511)

**Importante**

É necessário clicar no botão **"Enviar Mensagens"** ou acessar a rotina em **"Processos | Job que processa todos os avisos automáticos"** para que sejam enviados, caso desejar que sua execução seja automática conforme a periodicidade e horário definidos, é obrigatório que o ambiente esteja em N' Camadas.

**Passo a passo para agendamento dos avisos automáticos**

1. Consulte a documentação [Como agendar a execução de um processo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005088792-Framework-Linha-RM-Frame-Como-agendar-a-execu%C3%A7%C3%A3o-de-um-processo) para mais detalhes
2. Verifique se o ambiente está configurado em N' Camadas
3. Acesse a rotina Processos | Job que processa todos os avisos automáticos
4. Será apresentada a tela para configurar a execução e poder agendar os avisos automáticos.
5. Efetue o agendamento conforme necessário  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/31265339208855)
