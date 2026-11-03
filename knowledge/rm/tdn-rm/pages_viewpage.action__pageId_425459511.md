---
content_hash: a1816d1d026fb8f67205be7f9f27384a0dba8a9ddf4aa988e921296e21c138b9
fetched_at: '2026-06-29T00:09:36.400974+00:00'
page_id: '425459511'
product: rm
source: tdn-rm
title: Backoffice RM x Protheus SigaMNT - Processo de Honorários de Despachante
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459511
version: 3
---

**Backoffice RM x Protheus SigaMNT - Processo de Honorários de Despachante**

---

O valor a ser pago aos despachantes é criado à partir do faturamento de  parcelas dos pedidos de pagamento , gerados pelo envio da mensagem ORDER ao cadastrar um documento, definidos como honorários, e gerados no SigaMNT. A integração Linha RM x Protheus SigaMNT permite que os pedidos de pagamento de honorários de despachante sejam faturados e estornados, exibindo assim os valores faturados no relatório gerado ao executar o processo.Para mais informações sobre o processo de Transferência de Pneus, acesse os boletins técnicos.  
    
   
    
 **Pré-Condições:**

1. Sincronizar um produto que possua estoque do Backoffice RM para referenciá-lo como documento no Protheus SigaMNT.
2. Configurar o parâmetro MV\_PRODTS8 informando o p roduto sincronizado pela integração .O parâmetro pode ser acessado através de : SigaCFG / Base de dados / Dicionario / Base de Dados / Parâmetros /Pesquisar/ MV\_PRODTS8 / Editar.
3. Sincronizar uma condição de pagamento do Backoffice RM.
4. Sincronizar um Fornecedor do Backoffice RM.
5. Sincronizar um um Patrimônio do Backoffice RM.
6. Cadastrar um veículo no Protheus SigaMNT e vinculá-lo ao Patrimônio sincronizado do Backoffice RM. Paracadastrar o veículo acesse : Atualizações / Controle de Oficina / Bens / Bens.
7. Ter Cadastrado o tipo de movimento 1.1.86 – TMVPP – Pedido de Pagamento , no Backoffice RM,
8. Ter cadastrado o Adapter responsável por receber o pagamento das parcelas(InfoParcelValues)efetuado no Backoffice RM.
9. Importar a Fórmula Visual - Informação de Parcelas no sistema RM.
10. Configurar o parâmetro de integração 'TMVPedidoPagamento' com o código do tipo de movimento criado na pré-condição 7.
11. vincular um Documento Obrigatório ao Bem(Veículo)acessando : Atualizações / Gestão de Documentos / Cadastros / Docto. Obrigat.
12. Incluir um Serviço de Despachante acessando : Atualizações / Gestão de Documentos / Cadastros / Serviço/Despachante.
13. Vincular o Serviço Cadastrado a um Despachante acessando : Atualizações / Gestão de Documentos /Cadastros / Serviços | Fornecedor.
14. Ter Incluido um documento no Protheus SigaMNT
15. Ter efetuado Baixa das Parcelas do Pedido de Pagamento incluído no Backoffice RM, gerado à partir docadastro do documento no Protheus SigaMNT.

**Executando o Processo:**  
    
 **Passo 1-** Vincular o documento criado a um veículo acessando : Atualizações / Gestão de Documentos / Cadastros / Docto. Obrigat. Veiculo. **Passo 2–** Preencher os campos abaixo :

* Código Bem
* Placa
* Valor
* Emissao
* Vencimento
* Nº Titulo
* Fornecedor
* Loja
* Cond.Pagto

**Passo   3-** Selecionar o documento que  teve suas parcelas  faturadas no Backoffice RM(Ver Boletim técnico – Processo  de Geração de Documentos) ,  a vincular ao Veículo e confirmar as parcelas .

**Passo   4-** Para incluir os serviços  do despachante acesse : Atualizações / Gestão de Documentos / Cadastros / Serviço/Despachante.

**Passo   5-** Incluir  um  novo registro. O código do serviço será relacionado ao pagamento de um ou vários documentos.

**Passo   6-** Acesse  :  Atualizações / Gestão de Documentos / Cadastros / Serviços/Fornecedor

**Passo   7-** Incluir um novo registro vinculando o serviço criado anteriormente ao Fornecedor.

**Passo   8-** Acesse  : Atualizações / Gestão de Documentos / Custos / Honorários Despach.

**Passo   9-** Preencher os  campos   do filtro de pesquisa   e clicar em ok  :

**Passo  10-** Selecionar o serviço  a  realizar o pagamento e confirmar.

**Passo  11–** Foi gerado um relatório referente ao pagamento  de Honorário  de Despachante

**Passo  12-** Acessar : RM / Backoffice / Gestão de Estoque, Compras e Faturamento.

**Passo  13-** Acessar :  Compras / Ordem de Compra

**Passo  14-** Informar o código do tipo de movimento criado para o Pedido de Pagamento  e cliar em OK.

**Passo  15-** Selecionar o  Pedido de Pagamento gerado pela Mensagem Order enviada pelo Protheus SigaMNT  na criação do Documento e clicar em Editar.

**Passo  16–** Acesse a aba Lançamentos / Financeiro para visualizar as parcelas  geradas a partir da inclusão dos Honorários de Despachante , criado no Protheus SigaMNT.

**Observação**:  As parcelas de pedido de pagamento, gerado para  um processo de Honorários de Despachante, podem ser  baixadas ou estornadas.

---

 **Recursos Adicionais**

TDN - Boletim Técnico : [**Processo de Geração de Honorários de Despachante**](http://tdn.totvs.com/download/attachments/76251261/PROTHEUS_BT_HONOR%c3%81RIOS+DE+DESPACHANTE_BR_CON000158.pdf?version=1&modificationDate=1380053412000)
