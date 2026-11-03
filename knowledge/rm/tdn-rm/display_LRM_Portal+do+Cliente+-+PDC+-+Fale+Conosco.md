---
content_hash: 4f2e73e2ea920b64eb571b2d636b61a7fa35d98e6c5bb2e4af63c7413198422d
fetched_at: '2026-06-29T00:09:48.412830+00:00'
page_id: '435105146'
product: rm
source: tdn-rm
title: Portal do Cliente - PDC - Fale Conosco
type: documentation
url: https://tdn.totvs.com/display/LRM/Portal+do+Cliente+-+PDC+-+Fale+Conosco
version: 5
---

**Fale Conosco**

---

**Descrição**  
O Fale Conosco é uma ferramenta que visa a comunicação entre o comprador e a construtora, de forma gerenciada, encaminhando os emails para os destinatários conforme assunto e empreendimento.

|  |  |
| --- | --- |
|  | Como Fazer |

---

**Gestão**  
O usuário administrador do portal, deverá configurar o sistema para que os compradores tenham as opções necessários para usar o Fale Conosco. Para isto, deverá criar Tipos de Fale Conosco conforme sua necessidade.  
O Tipo de Fale Conosco deve ser criado, preenchendo os seguintes campos:

* Tipo: Nome do Tipo de fale conosco. Este campo será exibido para que o comprador possa selecionar entre os tipos de fale conosco cadastrados.
* Modelo: Neste campo o Gestor poderá definir um texto padrão, que será exibido para o comprador, conforme o Tipo de Fale Conosco selecionado. Nele podem conter orientações sobre as informações que o comprador precisa informar para enviar a mensagem deste Tipo de Fale Conosco.
* Necessário selecionar unidade: Este campo permite que o Gestor defina a obrigatoriedade ou não de o Comprador selecionar a Unidade tratada no Fale Conosco.
* Anexo Obrigatório ?: Este campo permite que o Gestor defina a obrigatoriedade ou não de o Comprador enviar Anexos no Fale Conosco
* Email: Campo onde deverá ser informado o endereço do responsável por aquele Tipo de Fale Conosco. Poderá ser informado mais de um e-mail, separado por ";" (ponto e virgula) e sem espaço entre os e-mails-. Os e-mails cadastrados irão receber os "Fale Conosco" deste tipo, enviados pelos compradores.
* Empreendimento: Este campo apenas ficará visível se a opção "Necessário selecionar unidade" estiver selecionado como "SIM". Nele o Gestor irá selecionar os empreendimentos específicos que terão e-mails diferenciados. Por exemplo, em uma construtora com 5 empreendimentos, sendo 2 em construção, o Fale Conosco do tipo Manutenção pode estar configurado para que, para os 3 empreendimentos concluídos, o responsável por receber esta comunicação será o departamento geral de manutenção, enquanto os 2 empreendimentos em construção possuem um departamento responsável pela obra que receberá também esta solicitação.
  + Os empreendimentos selecionados, serão exibidos em uma lista abaixo, onde haverá um campo para preencher o(s) e-mail(s) específico(s) para cada empreendimento selecionado.
  + A mensagem será enviada verificando primeiramente o e-mail do empreendimento específico. Os empreendimentos que não possuírem e-mail específico, terão a mensagem enviada para o e-mail geral do Tipo de Fale Conosco.
* O servidor de envio do e-mail, será utilizado conforme configuração global de e-mail, no RM.EXE, em Ambiente > Parâmetros > Parâmetros Globais > Envio de E-Mails**.**

**Comprador:**

* O usuário irá selecionar o Assunto, dentre os assuntos cadastrados pelo gestor.
* O campo Unidade virá preenchido com a primeira unidade de contratos do cliente, e este poderá selecionar outra, caso o assunto seja referente a unidade diferente da selecionada.
* O Texto é livre e virá pré-definido com o que estiver cadastrado para o assunto selecionado.
* Os telefeones no cadastro do Cliente/Fornecedor serão enviados no Rodapé do E-mail.
* Anexos,  quando o cliente selecionar o assunto do Fale Conosco será apresentada uma mensagem solicitando a inclusão de um anexo (Imagem/documento) referente ao assunto selecionado. com a possibilidade do administrador do portal definir a obrigatoriedade da inclusão desse anexo de acordo com o assunto que for selecionado pelo cliente.

Ao enviar o e-mail, o Comprador verá a mensagem de que o e-mail foi enviado com sucesso. Isto significa que o processo foi executado, porem, não há como garantir se o servidor de e-mail do destinatário irá aceitar a mensagem. Isto pode ocorrer por falta de espaço, configuração errada no endereço de e-mail, etc. Para contornar isto, a construtora poderia cadastrar um e-mail de resposta automático, que seria disparado assim que o servido de e-mail recebesse o e-mail do comprador.  
O e-mail enviado para a construtora, conforme configuração do assunto selecionado do Fale Conosco, será enviado contendo o texto digitado e editado pelo Comprador, alem de algumas informações pré-definidas.  
Os campos Coligada, Usuário, Cliente, Telefone, Email do cliente, Empreendimento, Unidade e Subunidade são fixos e internos, não sendo possível o Comprador alterá-los ao enviar uma mensagem através do Fale Conosco.
