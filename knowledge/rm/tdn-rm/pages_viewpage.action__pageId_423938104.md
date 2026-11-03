---
content_hash: 046a0315638ee405309d25e771a955bc8d9397ae5da7633121da3afd3ffc426b
fetched_at: '2026-06-29T00:09:25.292383+00:00'
page_id: '423938104'
product: rm
source: tdn-rm
title: Enviar E-mail para Cliente/Fornecedor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938104
version: 3
---

Este recurso tem como finalidade informar aos respectivos destinatários sobre os dados do movimento em questão, baseado no relatório escolhido pelo usuário.

**Relatório**

Selecione como anexo ou no corpo do e-mail qual relatório será enviado. Os relatórios apresentados são criados no menu Relatório | Gerador (Delphi) e Gerador.NET.  
   
**Enviar Relatório**

* No corpo de e-mail apenas para relatórios em formato texto: Marcando essa opção o texto do relatório selecionado será inserido no corpo do e-mail.
* Anexado ao e-mail: Marcando essa opção o relatório será enviado como arquivo anexo ao e-mail no formato parametrizado no próprio relatório.
* Ao selecionar o relatório a ser enviado, o assunto do e-mail será preenchido com 'MOVIMENTO Nº xxxx + nome do relatório selecionado'. Este texto poderá ser alterado pelo usuário.
* Caso queria enviar cópia do e-mail para outros destinatários informe nesse campo o endereço de cada uma delas, separados por vírgula(,) ou ponto e vírgula(;)

**As opções de Envio de E-mail**

* E-mail para o fornecedor;
* E-mail para o representante;
* E-mail para a transportadora;
* Email para Vendedor/Comprador;
* Cópia de e-mail para Usuário Logado;
* E-mail para contatos Cliente/Fornecedor.

É possível informar um texto para o corpo do e-mail e anexar outros arquivos para envio como um documento auxiliar, uma imagem e etc.  
 ***Observações**:*Quando mais de um movimento for escolhido para o envio de e-mail, o campo assunto não será preenchido e ao enviar os e-mails cada e-mail terá o assunto preenchido automaticamente com o Número do Movimento respectivo. Caso o usuário informe um assunto, este sempre será levado para todos os e-mails enviados.  
  
Em ambiente de Produção o sistema considera o e-mail informado no campo E-Mail Fiscal da tela de Tributos do cadastro de Cliente/Fornecedor conforme imagem abaixo, caso este campo esteja vazio será considerado o campo E-Mail da tela Identificação do cadastro de Cliente/Fornecedor. Se os dois campos de e-mail estiverem vazios o sistema não executa o processo e apresenta a seguinte mensagem no log de execução: "E-mail não foi enviado. Endereço de e-mail do destinatário não informado".

**Status de Envio de E-mail**  
  
Na visão do movimento existe uma coluna  para identificar o Status de Envio de Email de ordem de compra. Este campo ficará disponível caso o parâmetro envio de e-mail esteja habilitado. Os status serão: Enviado e Não Enviado.

**Parametrização**  
  
Acesse Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento| Tipo de Movimento Desejado | Etapa: Mov - Impressão 2/2. Para habilitar o envio de e-mail para Clientes / Fornecedores marque o parâmetro **Envia E-mail**.  
Para exibir a opção E-mail para Contatos Cliente/Fornecedor no assistente de Enviar E-mail para Cliente/Fornecedor marque o parâmetro **Usar contato do fornecedor no envio de e-mail**.
