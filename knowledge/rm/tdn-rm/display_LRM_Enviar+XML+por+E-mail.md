---
content_hash: 1f0e8cd00a13ca300a457afe6cd5a8eedacfbd32bbb71d2fca885aa962271907
fetched_at: '2026-06-29T00:09:20.567574+00:00'
page_id: '422545709'
product: rm
source: tdn-rm
title: Enviar XML por E-mail
type: documentation
url: https://tdn.totvs.com/display/LRM/Enviar+XML+por+E-mail
version: 7
---

Através deste processo é possível enviar informações da NF-e para o destinatário da nota.  
Por default este processo envia apenas o XML da NF-e.  
Para que este processo funcione é imprescindível que os Parâmetros Globais | Envio de Email devidamente estejam configurados.  
Pode-se ainda enviar uma cópia (CC) e cópia oculta (CCo) dos dados.   
É enviado no corpo do e-mail o texto padrão abaixo:  
"*@Nome.* *Att: @Contato*  
*Prezados,*  
*Segue anexo arquivo XML referente NF-e @NumeroNota autorizada em @DataAutorizacao com chave de acesso: @ChaveAcesso.*  
*Atenciosamente,"*  
Este texto poderá ser alterado de acordo com as necessidades do usuário. O texto quando alterado por esta tela de envio vale somente para o envio corrente mas pode-se parametrizar uma mensagem padrão por tipo de movimento. As palavras iniciadas pela arroba são variáveis e são substituídas pelos valores constantes na NF-e no ato do envio.  
Ainda poderá ser enviada uma cópia da mensagem para a transportadora da mercadoria e ser anexada uma cópia do DANFE em PDF. Para que o DANFE seja enviado é necessário que a estrutura do relatório seja previamente importado para o RM.

**Definindo os padrões de envio de e-mail da NF-e**

O envio de e-mail da NF-e pode ser automatizado através do tipo de movimento que irá gera-la.  
Esta configuração é feita no parametrizador do tipo de movimento na Etapa 66 - Fis - NF-e no item Envio de e-mail.  
Existem vários tipos de envio:

1. **Não enviar e-mail automaticamente**: Neste caso o processo de envio das informações da NF-e deverão ser feitas manualmente pelo usuário após a nota ser autorizada.
2. **Enviar XML da Nota por e-mail**: Após ser autorizada a NF-e o seu XML será enviado automaticamente para o endereço de e-mail gravado no cadastro do destinatário da NF-e.
3. **Enviar XML da Nota por e-mail com cópia para transportadora:** Após ser autorizada a NF-e o seu XML será enviado para o e-mail do destinatário com uma cópia para a transportadora.
4. **Enviar e-mail com XML/PDF do DANFE automaticamente:** Após ser autorizada a NF-e o seu XML e seu PDF será enviado para o e-mail do destinatário da NF-e.
5. **Enviar e-mail com XML/PDF do DANFE automaticamente CC para a transportadora:** Após ser autorizada a NF-e o seu XML juntamente com o PDF o DANFE serão enviados para o e-mail do destinatário e para a transportadora da mercadoria.

É possível definir uma mensagem padrão para o envio da NF-e por tipo de movimento. Para isto clique no loockup de mensagens no processo de parametrização das informações de envio de e-mail do tipo de movimento e clique no botão novo para incluir um nova mensagem. Após incluir a nova mensagem selecione-a para o tipo de movimento e salve-o. Esta mensagem será utilizada sempre que for enviado e-mail para uma NF-e gerada por este tipo de movimento manual ou automaticamente. Estas mensagens podem também ser criadas através do menu Cadastros | Tabelas Auxiliares | Mensagens.  
***Atenção!*** As mensagens para envio de e-mail de NF-e devem possuir a classificação Outras. A maioria dos anti-virus bloqueia o envio de emails por programas instalados no computador para evitar a propagação de vírus. Adicione uma exceção para o RM Nucleus.exe e o rm.host.service.exe em seu software para evitar problemas de bloqueio. Selecione a nota clicando no seu Chekbox. Clique no botão Processos e escolha Enviar XML por e-mail.

**Variáveis possíveis no texto de uma mensagem padrão de e-mail da NF-e**

Se o "Ambiente de envio das NF-e's" informado nos parâmetros da Nota Fiscal Eletrônica for "Homologação", o XML será enviado para o e-mail informado no cadastro da Filial emitente.  
Se o "Ambiente de envio das NF-e's" informado nos parâmetros da Nota Fiscal Eletrônica for "Produção" o XML será enviado para o e-mail informado no Cliente/Fornecedor.  
Para que o e-mail seja enviado, é necessário que no cadastro do Usuário, o campo "E-mail" esteja preenchido.  
A mensagem que será enviada no e-mail pode ser editada. As palavras com "@" são variáveis que podem ser duplicadas ou excluídas, conforme desejar, na edição da mensagem.

@Usuário: Usuário logado no sistema  
@NomeFilial: Razão Social da Filial emissora da NF-e  
@TelFilial: Telefone da Filial emissora da NF-e  
@Nome: Nome do Destinatário da NF-e  
@ChaveAcesso: Chave de Acesso da NF-e  
@DataAutorizacao: Data de Autorização da NF-e  
@Contato: Contato do Destinatário da NF-e  
@NumeroNota: Número da NF-e

**Anexo - Histórico**

Após envio do XML por email, manual ou automático, o histórico de envio é armazenado no anexo da NF-e.
