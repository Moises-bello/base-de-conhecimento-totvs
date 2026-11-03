---
article_id: 35914753178903
category: Materiais - Compras (SIGACOM)
content_hash: ee649935404bd19a4913014909712453c977dc2892d66c9c4595eead55d54eb4
fetched_at: '2026-06-28T22:41:21.873188+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Ocorrência do
  erro The RCPT command failed no Novo Fluxo de Compra
type: support-article
updated_at: '2025-10-27T17:57:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35914753178903-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Ocorr%C3%AAncia-do-erro-The-RCPT-command-failed-no-Novo-Fluxo-de-Compra
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35914732775447) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Ao gerar pedido de compra na Análise da Cotação no NFC, é gerado o erro abaixo. Como corrigir?

AJUDA:AVG0001056 - Erro ao enviar o e-mail. Error (3) :The RCPT command failed. The specified account does not exsist.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - a partir da Release 12.1.2310  
  
**Solução**  
A mensagem apresentada possui relação com as contas que estão recebendo os e-mails. Muitas vezes podem ocorrer indisponibilidades com o Servidor, ou mesmo falta de espaço na conta que receberá o Workflow.  
Caso possua arquivos ".wfm" presos dentro da caixa "Outbox" do "Workflow", faça inicialmente um Backup da mesma e em seguida delete o conteúdo. Após tal ação, inicie um novo processo de Workflow para validação da ferramenta.  
Sugerimos também que retire todo e qualquer caractere especial do campo "Remetente" do Cadastro do Workflow, visto que o mesmo não entende os caracteres especiais eventualmente presentes no campo em questão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35914732777239)

Além disso, faça as validações abaixo:

1. O parâmetro **MV\_WFSNDAU** é fundamental no processo de envio automático do Workflow. Certifique-se de que o valor está configurado como **.T.**
2. Verificar se o parâmetro MV\_WFMLBOX está preenchido com o nome da caixa de email que foi cadastrada através do configurador, na rotina Contas de Email, o conteúdo do parâmetro deve ser igual a informação que consta no campo "Cx Correio".

Se mesmo assim persistir, adicione as chaves abaixo no appserver.ini do serviço REST onde foi configurado o WORKFLOW:  
  
[General]  
rest\_log\_level=4  
  
[Sessão Ambiente]  
tracestack=1  
FWTRACELOG=1  
FWLOGMSG\_DEBUG=1

Limpe o console.log do appserver.ini do serviço REST do WF > Gere o erro novamente na rotina NFC > Separe o novo console.log e nos encaminhe para analise!

***Saiba Mais:***

[Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Falha ao enviar mensagem: The RCPT command failed](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021255231-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Falha-ao-enviar-mensagem-The-RCPT-command-failed)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - O email não é enviado no Novo Fluxo de Compras.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28157401030423-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-O-email-n%C3%A3o-%C3%A9-enviado-no-Novo-Fluxo-de-Compras)

[Novo Fluxo de Compras: Guia de Referência](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
