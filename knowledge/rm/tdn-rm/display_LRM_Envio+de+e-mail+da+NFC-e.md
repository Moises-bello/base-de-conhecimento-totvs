---
content_hash: e9487a7f388620af1fccff5ad97692961a96bea18d357d2dd584ff7b2c301e0d
fetched_at: '2026-06-29T00:09:20.572331+00:00'
page_id: '422545711'
product: rm
source: tdn-rm
title: Envio de e-mail da NFC-e
type: documentation
url: https://tdn.totvs.com/display/LRM/Envio+de+e-mail+da+NFC-e
version: 3
---

Através deste processo é possível enviar informações da NFC-e para o destinatário da nota.   
 Por default este processo envia apenas o XML da NFC-e.  
 Para que este processo funcione é imprescindível que os Parâmetros Globais | Envio de e-mail estejam configurados.  
 Pode-se ainda enviar uma cópia (CC) e cópia oculta (CCo) dos dados.   
 É enviado no corpo do e-mail o texto padrão abaixo:  
 *"@Nome.*  
 *Att: @Contato*  
    
 *Prezados,*  
    
 *Segue anexo arquivo XML referente NF-e/NFC-e @NumeroNota autorizada em @DataAutorizacao com chave de acesso: @ChaveAcesso.*  
    
 Atenciosamente,*"*

Este texto poderá ser alterado de acordo com as necessidades do usuário. O texto quando alterado por esta tela de envio vale somente para o envio corrente mas pode-se parametrizar uma mensagem padrão por tipo de movimento. As palavras iniciadas pela arroba são variáveis e são substituídas pelos valores constantes na NFC-e no ato do envio.

Ainda poderá ser enviada uma cópia da mensagem para a transportadora da mercadoria e ser anexada uma cópia do DANFE em PDF. Para que o DANFE seja enviado é necessário que a estrutura do relatório seja previamente importado para o RM.

**Definindo os padrões de envio de e-mail da NF-e**

O envio de e-mail da NFC-e pode ser automatizado através do tipo de movimento que irá gera-la.  
 Esta configuração é feita no parametrizador do TOTVS Gestão de Estoque e Faturamento no tipo de movimento na Etapa 66 - Fis - NFC-e no item Envio de e-mail.  
    
 Existem vários tipos de envio:

1. **Não enviar e-mail automaticamente**: Neste caso o processo de envio das informações da NFC-e deverão ser feitas manualmente pelo usuário após a nota ser autorizada.
2. **Enviar XML da Nota por e-mail**: Após ser autorizada a NFC-e o seu XML será enviado automaticamente para o endereço de e-mail gravado no cadastro do destinatário da NFC-e.
3. **Enviar XML da Nota por e-mail com cópia para transportadora:** Após ser autorizada a NFC-e o seu XML será enviado para o e-mail do destinatário com uma cópia para a transportadora.
4. **Enviar e-mail com XML/PDF do DANFE automaticamente:** Após ser autorizada a NF-e o seu XML e seu PDF será enviado para o e-mail do destinatário da NFC-e.
5. **Enviar e-mail com XML/PDF do DANFE automaticamente CC para a transportadora:** Após ser autorizada a NFC-e o seu XML juntamente com o PDF o DANFE serão enviados para o e-mail do destinatário e para a transportadora da mercadoria.

É possível definir uma mensagem padrão para o envio da NFC-e por tipo de movimento. Para isto clique no loockup de mensagens no processo de parametrização das informações de envio de e-mail do tipo de movimento e clique no botão novo para incluir um nova mensagem. Após incluir a nova mensagem selecione-a para o tipo de movimento e salve-o. Esta mensagem será utilizada sempre que for enviado e-mail para uma NFC-e gerada por este tipo de movimento manual ou automaticamente. Estas mensagens podem também ser criadas através do menu Cadastros | Tabelas Auxiliares | Mensagens.  
 Atenção: As mensagens para envio de e-mail de NFC-e devem possuir a classificação Outras.

**Variáveis possíveis no texto de uma mensagem padrão de e-mail da NF-e**  
 @Usuário: Usuário logado no sistema  
 @NomeFilial: Razão Social da Filial emissora da NFC-e  
 @TelFilial: Telefone da Filial emissora da NFC-e  
 @Nome: Nome do Destinatário da NFC-e  
 @ChaveAcesso: Chave de Acesso da NFC-e  
 @DataAutorizacao: Data de Autorização da NFC-e  
 @Contato: Contato do Destinatário da NFC-e  
 @NumeroNota: Número da NFC-e
