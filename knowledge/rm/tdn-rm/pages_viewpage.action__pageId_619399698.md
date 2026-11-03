---
content_hash: f387a95a9d710d6ba966338c5a6b9c6b3fda60e8de215505708af42c24b404da
fetched_at: '2026-06-29T00:11:03.178014+00:00'
page_id: '619399698'
product: rm
source: tdn-rm
title: Parâmetros - Sistema
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=619399698
version: 20
---

| Parâmetro |
| --- |
| **Sistema Ativo** Altere para ***Sim*** para permitir que usuários efetuem login no sistema. **Nota:** Usuários de grupos que possuam a permissão de acesso ao backend sempre poderão efetuar login, mesmo que esta restrição esteja ***Não***. |
| **CNPJ do Contrato** **Alterar o CNPJ do contrato, fará com que o sistema gere uma nova licença. Não altere este campo a menos que seja solicitado.** |
| **Nome da Empresa** Digite aqui o nome da empresa que será usado no envio de e-mails e em algumas partes do sistema. |
| **API SMS: API** Defina aqui a API para usar para envio de SMS. Lembre-se de informar as credenciais abaixo. |
| **API SMS: Usuário** Senha da API de envio de SMS. **MobilePronto:** Project |
| **API SMS: Senha** Usuário da API de envio de SMS. **MobilePronto:** Credential |
| **API SMS: Intervalo Envio Início** Defina aqui o início do intervalo em que o servidor deverá enviar o SMS. Definido em horas e minutos. Para definir o dia todo, configure como 00:00. |
| **API SMS: Intervalo Envio Fim** Defina aqui o fim do intervalo em que o servidor deverá enviar o SMS. Definido em horas e minutos. Para definir o dia todo, configure como 23:59. |
| **Servidor SMTP: Host** Defina aqui o servidor SMTP a ser usado para envio dos emails do sistema. Você pode especificar mais de um servidor separando por vírgula. ex. [smtp.servidor1.com](http://smtp.servidor1.com),[smtp.servidor2.com](http://smtp.servidor2.com)  Atualmente, o sistema **não oferece suporte para envio de e-mails utilizando o servidor `smtp.office365.com`**.  Os tipos de autenticação SMTP atualmente suportados são: **CRAM-MD5**, **LOGIN** e **PLAIN**.  Para verificar possíveis erros ou acompanhar o registro de envios, consulte o arquivo **`/tmp/smtp.log`**. Esse arquivo é essencial para a análise e diagnóstico de eventuais falhas no processo de envio de e-mails. |
| **Servidor SMTP: Usuário** Defina aqui o usuário (as vezes o e-mail) do servidor de e-mail. |
| **Servidor SMTP: Senha** Defina aqui a senha do servidor de e-mail. |
| **Servidor SMTP: Servidor requer autenticação** Defina aqui se seu servidor SMTP requer autenticação. |
| **Servidor SMTP: Criptografia** Defina aqui se seu servidor exige criptografia. |
| **Servidor SMTP: E-mail de resposta** Defina aqui o e-mail de resposta caso o destinatário deseja responder. |
| **Servidor SMTP: Porta** Defina aqui a porta do servidor SMTP. |
| **Email: Texto impresso no rodapé dos e-mails enviados pelo sistema** Informe o texto que identifique quem enviou o e-mail |
| **Email: Link de instalação do Portal de Imóveis** Informe o qual o link impresso no rodapé dos e-mails enviados pelo portal de vendas |
| **Audittrail: Validade de dias dos logs armazenados na tabela de audittrail** Informe a quantidade de dias de validade dos registros de logs armazenados na tabela audittrail. Passado os dias parametrizados os registros de logs serão automaticamente excluídos |
| **Ativar validação de campos obrigatórios customizados** Se definido como **SIM**, haverá validação dos campos obrigatórios customizados. A parametrização para mapear quais campos são obrigatórios pode ser definida em **Backend > Sistema > Campos Obrigatórios**. Se definido como **NÃO** será utilizado a validação padrão do sistema |
| **Endereço de e-mails para copiar nos envios de e-mail do sistema** Informe um ou mais endereços de e-mail para que sejam enviadas cópias dos e-mails enviados pelo sistema. Separe os endereços de e-mails com um ponto vírgula. ex. [pessoa1@exemplo.combr](mailto:pessoa1@exemplo.combr);pessoa2@[exemplo.com.br](http://exemplo.com.br) |
| **Número de SQLs para executar ao sincronizar** Não deve ser maior que 600. |
| **Obrigatório informar CNPJ no cadastro de imobiliárias** Informe se será obrigatório informar CNPJ no cadastro de imobiliárias. |
| **Tamanho das miniaturas** Em pixels. |
| **Tamanho Máximo Documentos(Upload)** Limita o tamanho máximo do documento na proposta e pessoa. |
| **Token Google Maps** Token do Google para carregar os mapas cadastrados no portal.  Para mais informações de como criar o token . |
