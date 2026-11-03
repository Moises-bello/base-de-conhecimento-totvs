---
content_hash: a5f5b7b380fda1378fa702e26270f17f5b80a7eed34a7c0c8bd43cad53678279
fetched_at: '2026-06-29T00:09:25.285078+00:00'
page_id: '423938102'
product: rm
source: tdn-rm
title: Envio de Ordens de Compra via E-mail
type: documentation
url: https://tdn.totvs.com/display/LRM/Envio+de+Ordens+de+Compra+via+E-mail
version: 2
---

Este recurso está disponível na edição de uma cotação com Status = "Pedido de Compra".   
Este processo tem como finalidade informar aos respectivos destinatários sobre os dados do movimento de ordem de compra gerado na cotação baseado no relatório escolhido pelo usuário.

**Relatório**: Selecione como anexo ou no corpo do e-mail qual relatório será enviado. Os relatórios apresentados são criados no menu Relatório | Gerador (Delphi) e Gerador.NET.

**Enviar relatório**: No corpo de e-mail apenas para relatórios em formato texto: Marcando essa opção o texto do relatório selecionado será inserido no corpo do e-mail.

**Anexado ao e-mail**: Marcando essa opção o relatório será enviado como arquivo anexo ao e-mail no formato parametrizado no próprio relatório. Ao selecionar o relatório a ser enviado, o assunto do e-mail será preenchido com 'MOVIMENTO Nº xxxx + nome do relatório selecionado'. Este texto poderá ser alterado pelo usuário. Caso queria enviar cópia do e-mail para outros destinatários informe nesse campo o endereço de cada uma delas, separados por vírgula(,) ou ponto e vírgula ((piscar o olho). As opções de envio de e-mail são:

* E-mail para o fornecedor;
* E-mail para o representante;
* E-mail para a transportadora;
* Email para Vendedor/Comprador;
* Cópia de e-mail para Usuário Logado;
* E-mail para contatos Cliente/Fornecedor.

É possível informar um texto para o corpo do e-mail e anexar outros arquivos para envio como um documento auxiliar, uma imagem e etc.

**Status de Envio de E-mail**: Na cotação, em Anexos | Pedidos Gerados existe uma coluna para identificar o Status de Envio de E-mail de ordem de compra. Este campo ficará disponível caso o parâmetro envio de e-mail esteja habilitado. Os status serão: Enviado e Não Enviado.

**Parametrização**: Para habilitar o envio de e-mail basta marcar o parâmetro Envia E-mail em Ambiente | Parâmetros | TOTVS Gestão de Estoque,Compras e Faturamento | Tipo de Movimento Desejado | Etapa: Mov - Impressão 2/2.
