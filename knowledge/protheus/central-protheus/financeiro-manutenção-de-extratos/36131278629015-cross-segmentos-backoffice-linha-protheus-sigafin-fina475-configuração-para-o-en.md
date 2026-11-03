---
article_id: 36131278629015
category: Financeiro - Manutenção de Extratos
content_hash: 7cf6af07487240070ccda75e3a933cdc4f47878d6f8e11adea71624db33d5ede
fetched_at: '2026-06-28T22:37:31.171270+00:00'
product: protheus
section_id: 35057672519319
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA475 - Configuração
  para o envio de e-mail
type: support-article
updated_at: '2025-11-05T20:27:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36131278629015-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA475-Configura%C3%A7%C3%A3o-para-o-envio-de-e-mail
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36131223329175) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Como configurar o envio de e-mail no processo de extrato bancário via agendamento **FINA475**?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
1 **-** Para a importação de extratos bancários, é necessário gerar uma senha de APP, no caso do G-Mail, primeiro precisamos ativar a verificação em duas etapas:

![](https://tdn.totvs.com/download/attachments/747320567/Conta%20do%20Google%20-%20Google%20Chrome.jpg?version=1&modificationDate=1679579443870&api=v2)

Após a verificação de duas etapas ativada, é necessário adicionar um APP e gerar uma senha:

![Conta do Google - Google Chrome_3.jpg](https://tdn.totvs.com/download/attachments/747320567/Conta%20do%20Google%20-%20Google%20Chrome_3.jpg?version=1&modificationDate=1679579444043&api=v2)

![Senhas de app - Google Chrome.jpg](https://tdn.totvs.com/download/attachments/747320567/Senhas%20de%20app%20-%20Google%20Chrome.jpg?version=1&modificationDate=1679579444207&api=v2)

Copie a senha gerada e salve em um lugar seguro.

![Senhas de app - Google Chrome_2.jpg](https://tdn.totvs.com/download/attachments/747320567/Senhas%20de%20app%20-%20Google%20Chrome_2.jpg?version=1&modificationDate=1679579444353&api=v2)

**2 - Configurando o serviço de e-mail:**

Com a senha de app gerada, abra o Protheus no **SIGACFG, ambiente, E-mail/Proxy, Configurar.** Coloque o servidor de e-mail, o seu e-mail e a senha do APP gerada anteriormente. Em servidor de e-mail que necessita de autenticação, coloque sim.

![](https://tdn.totvs.com/download/attachments/747320567/001.jpg?version=1&modificationDate=1679580260823&api=v2&effects=drop-shadow)

Na próxima tela, apenas clique em avançar sem alterar nada:

![](https://tdn.totvs.com/download/attachments/747320567/002.jpg?version=1&modificationDate=1679580261220&api=v2&effects=drop-shadow)

Utiliza segurança TLS - SIM

![](https://tdn.totvs.com/download/attachments/747320567/003.jpg?version=1&modificationDate=1679580261673&api=v2&effects=drop-shadow)

Finalize a configuração de E-MAIL:

![](https://tdn.totvs.com/download/attachments/747320567/004.jpg?version=1&modificationDate=1679580262030&api=v2&effects=drop-shadow)

**Importante**

O parâmetro MV\_RETMAILpode ser configurado com um ou mais endereços de e-mail, separados por ponto e vírgula. Para que o processamento envie um e-mail contendo eventuais inconsistências com o resumo dos títulos como anexo. Caso o parâmetro não esteja corretamente preenchido ou esteja em branco, nenhum e-mail ou resumo será enviado, ou gravado.

Este parâmetro recebe o e-mail que receberá os e-mails de sucesso ou falha do processo.

**Saiba mais**

[FINA475 - Configuração do Retorno de Extratos Bancários Automático](https://tdn.totvs.com/pages/releaseview.action?pageId=747320567)
