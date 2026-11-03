---
content_hash: 044798ce6cb50277fd885dec2ec0631c61e03e3c0f8480aa33ad3550ada6349e
fetched_at: '2026-06-29T00:06:21.868965+00:00'
page_id: '223182686'
product: rm
source: tdn-rm
title: DT_Integração_Controle_de_Caixa_EMS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223182686
version: 126
---

# Integração com o Controle de Caixa EMS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Tesouraria | Controle de  Solicitação p/ Emissão de Nota Fiscal / Recibos |  |  | | --- | | **Rotina(s) envolvida(s)** | | Parâmetros de Integração, Parâmetros por Estação de trabalho, Registro de Atendimento, Registro de Responsável, Elaboração de Contas | |
| **Cadastros Iniciais:** | Relacione os cadastros necessários que precisam ser preenchidos antes da utilização desse requisito. |
| **Parâmetro(s):** | Utiliza Controle de Caixa |
| **Requisito (ISSUE):** | PCREQ-8993 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | SZPEDIDOATEND |
| **Sistema(s) Operacional(is):** | Windows |
| **Versões/Release:** | 12.1.9 |
| **Versão Expedida:** | 12.1.9.0 |

## Descrição

Esta implementação consiste em utilizar o controle de Caixa do EMS para efetivar o recebimento de contas particulares.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):  
   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.9 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.9.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).
2. Faça o login, com seu E-mail e Senha.
3. Na barra de menu superior, clique em DOWNLOAD.
4. No boxe Central de Downloads aplique os filtros conforme campos abaixo:  
   1. Linha: RM
   2. Versão: RM 12.1.9
   3. Tipo: Patch

Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.  
   Importante: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

### Script para configuração das mensagens de integração

Solicite os scripts:

* Script\_TradingProcess.sql
* Script\_TradingProcessReturn.sql
* Script\_TradingProcessCancel.sql
* Script\_ReceiveInvoiceDocument.sql
* Script\_PendingPaymentCancel.sql

### Utilização do TBC

É necessário realizar a instalação do TBC para que o EMS faça a utilização do Webservice de integração.

Após a instalação padrão, adicione o arquivo **wsEMSService.asmx** na pasta padrão do TBC.

O arquivo **web.config** deve ser alterado nesta integração para incluir usuário e senha que a utilização do serviço.

As tags devem ficar dentro de appSettings:

<add key="UserWCF" value="mestre"/>  
 <add key="PwdWCF" value="totvs"/>

## Procedimento para Utilização

1. Para utilizar a integração do Controle de Caixa do EMS, acesse o menu **Opções/ Parâmetros/ Parâmetros de Integração**, e marque o parâmetro abaixo.
2. Na página Nota Fiscal, informe os parâmetros da nota que será gerada no EMS a partir das informações de recebimento no **Controle de Caixa**.
3. O código do Caixa para o qual será enviado as informações de pagamento deve ser parametrizado por estação de trabalho no menu Opções / Parâmetros / Parâmetros por Estação de Trabalho.
4. Uma vez parametrizado o sistema, abra um registro de atendimento. Selecione o convênio e informe pelo menos um responsável pelo atendimento (responsável financeiro).
5. No **Cadastro de Responsável** informe o tipo, que dependendo da opção o sistema já preencherá algumas informações. Informe o nome do responsável e o CPF. Neste momento o sistema verifica o CPF e caso o mesmo já esteja na base de dados, o mesmo já buscará os dados já informados. Para a integração, as informações contidas na página **Informações Complementares** deverão ser informadas dependendo do que é exigido no EMS. Se for um cadastro novo, a integração não ocorrerá neste momento, somente ao enviar os dados para pagamento para o EMS.
6. Faça o lançamento dos itens realizados pelo paciente e clique no botão **Encerra** para fechar a conta.
7. Após o fechamento da conta, acesse o menu **Tesouraria / Controle de  Solicitação p/ Emissão de Nota Fiscal / Recibos**. Clique no primeiro botão em destaque (Gerar solicitação de emissão de documento) para que o sistema processe os dados para pagamento.
8. Ao clicar no botão, será exibida a tela abaixo. Selecione o paciente cuja conta foi encerrada. Neste momento o sistema identifica os gastos do paciente e exibe no campo “Controle” as opções disponíveis para pagamento particular. Quando a conta é de paciente particular, todos os itens lançados na conta serão considerados. Caso a conta seja de convênio, somente os Gastos Particulares serão considerados. Selecione o responsável financeiro caso exista mais de um. Clique em “Processar” para que o sistema calcule o valor e o agrupamento que será utilizado.
9. A forma que os itens serão enviados para o EMS depende de parametrizações. Se o parâmetro “**Utilizar sempre discriminação única na NF**” estiver marcado, o sistema utiliza o produto parametrizado na tela de **Parâmetros de Integração**.
10. Se no cadastro de grupo de gasto estiver parametrizado para agrupar, o sistema considerará os produtos configurados para paciente interno e paciente externo.
11. Caso não utilize por grupo de gasto, o produto utilizado será o definido por faixa de codificação. Todos os itens lançados na conta devem possuir um produto corresponde nas parametrizações. Se o sistema não encontrar, emitirá um erro de falta de parametrização.
12. Após processar, selecione o paciente que se deseja receber pelo EMS e clique no segundo botão (Gera Pedido de Emissão de documento para o EMS). Ao integrar, o status passará para G de Gerada. O campo Id, corresponderá à coluna “Referência” no EMS.
13. Apôs integrar com o EMS, acesse o EMS e na página Área de Trabalho, selecione “**Operador de Caixa**”.
14. Clique na imagem “**Movimentar Caixa**”.
15. A tela abaixo é exibida. Para realizar o pagamento, clique no link “**Preencher informações**”.
16. Clique no botão **Editar** para informar a forma de pagamento, tipo de pagamento, parcelas, etc.
17. Após informar os valores recebidos, feche a tela anterior, efetive o pagamento. Neste momento, ocorre uma integração onde as informações de pagamento são enviadas para o Saúde e o Saúde gera uma mensagem para inclusão da nota no EMS. A nota pode ser visualizada acesso no EMS como “**Faturista**” e clique no link “**Detalhar**”.
18. Selecione a nota gerado e clique em **Detalhar**.
19. Detalhe das notas.
20. Mensagens utilizadas para a integração do **Controle de Caixa**.
21. Log do processamento das mensagens. Caso ocorra algum erro, deve-se buscar o detalhe na tela de edição.

 

divs
