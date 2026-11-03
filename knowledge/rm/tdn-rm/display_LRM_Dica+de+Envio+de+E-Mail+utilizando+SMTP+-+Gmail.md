---
content_hash: dc68b5af1696942ffcd4f335d508a21ab2654fc7fe78ef262aef600705e2e90f
fetched_at: '2026-06-29T00:08:07.580828+00:00'
page_id: '237381522'
product: rm
source: tdn-rm
title: Dica de Envio de E-Mail utilizando SMTP - Gmail
type: documentation
url: https://tdn.totvs.com/display/LRM/Dica+de+Envio+de+E-Mail+utilizando+SMTP+-+Gmail
version: 4
---

# Nas configurações de envio de e-mail são informados os dados de envio de acordo com a parametrização SMTP, Usuário, Senha e Porta. Nesta dica, demonstraremos a parametrização para envio de e-mail utilizando conta GMAIL.

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 12.1.XX |
| **Ocorrência:** | Envio de E-mail |
| **Ambiente:** | Parâmetros Globais |
| **Passo a passo:** | 1 – Acessar conta do gmail.  Acesse o link (<https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier>)  1.1 – Digite sua conta de e-mail:  1.2 – Digite sua senha:  2 – Configurando conta gmail.  2.1 – Execute o link para liberar utilização do e-mail em outros aplicativos <https://www.google.com/settings/security/lesssecureapps>  [2.2 – Execute o link para permitir liberação da conta em outros dispositivos](https://www.google.com/settings/security/lesssecureapps) <https://accounts.google.com/DisplayUnlockCaptcha>    Caso sua conta google esteja aplicada a configuração em duas etapas para outros aplicativos o Google (gmail) passou a tratar a validação em duas etapas na configuração de segurança dos e-mails. Com isso para manter o endereço de e-mail do Google para envio pelo RM é necessário criar uma senha especifica para aplicativos menos seguros. Isto esta descrito em detalhes nos links abaixo:[https://support.google.com/accounts/answer/6010255?p=less-secure-apps&hl=pt-BR&visit\_id=637467639654186362-3200236859&rd](https://support.google.com/accounts/answer/6010255?p=less-secure-apps&hl=pt-BR&visit_id=637467639654186362-3200236859&rd=1)<https://support.google.com/accounts/answer/185833>  [2 – Parametrização envio de e-mail:](https://accounts.google.com/DisplayUnlockCaptcha)  <http://tdn.totvs.com/display/public/rm/Envio+de+email+-+LINHA+RM>      Abaixo informações cadastradas para Gmail:  1 – Conforme configuração do Gmail servidor deve ser “[smtp.gmail.com](http://smtp.gmail.com)” 2 – Habilite está opção para servidor validar o usuário e senha do usuário que está enviado e-mail. 3 – Informe e-mail configurado no passo “1.1 – Digite sua conta de e-mail” 4 – Informe a senha do e-mail indicado 5 – Para configuração do Gmail não é necessário informar um domínio. 6 – Conforme configuração do Gmail porta deve ser “587” 7 – Habilite conforme configuração do servidor |
| **Observações:** |  |
