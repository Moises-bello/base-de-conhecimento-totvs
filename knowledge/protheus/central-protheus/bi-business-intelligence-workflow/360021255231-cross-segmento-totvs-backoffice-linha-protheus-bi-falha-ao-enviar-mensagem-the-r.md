---
article_id: 360021255231
category: BI - Business- Intelligence - Workflow
content_hash: 4098bead497f91453c5df866e59e94795cebcd50b5c9a00b8cf7868c40217ec6
fetched_at: '2026-06-28T22:37:03.042897+00:00'
product: protheus
section_id: 1500001550762
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Falha ao enviar mensagem:
  The RCPT command failed'
type: support-article
updated_at: '2024-03-06T17:47:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021255231-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Falha-ao-enviar-mensagem-The-RCPT-command-failed
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21851528867479) Tempo aproximado para leitura: 02:00 min****Dúvida**Falha ao enviar mensagem do Workflow: "**The RCPT command failed**"  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Bl Workflow - Todas as versões  
  
**Solução**A mensagem apresentada possui relação com as contas que estão recebendo os e-mails. Muitas vezes podem ocorrer indisponibilidades com o Servidor, ou mesmo falta de espaço na conta que receberá o Workflow.  
Caso possua arquivos ".wfm" presos dentro da caixa "Outbox" do "Workflow", faça inicialmente um Backup da mesma e em seguida delete o conteúdo. Após tal ação, inicie um novo processo de Workflow para validação da ferramenta.  
Sugerimos também que retire todo e qualquer caracter especial do campo "Remetente" do Cadastro do Workflow, visto que o mesmo não entende os caracteres especiais eventualmente presentes no campo em questão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21851513470743)

**Saiba Mais**[FAQ Workflow](http://tdn.totvs.com/display/public/PROT/FAQs+-+Workflow)  
[Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Funçao WFSENDMAIL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18669495725975-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Fun%C3%A7%C3%A3o-WFSENDMAIL)
