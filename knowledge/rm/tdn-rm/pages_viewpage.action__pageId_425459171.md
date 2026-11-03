---
content_hash: 2b4c4d36452b3a4dce405c57750492f9990e594153ea19390ba68b5580cdd2d8
fetched_at: '2026-06-29T00:09:34.499397+00:00'
page_id: '425459171'
product: rm
source: tdn-rm
title: Linha RM x Protheus SigaMNT - Cadastro de Produto/Serviço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459171
version: 3
---

**Linha** **RM x Protheus SigaMNT - Cadastro de Produto/Serviço** 

---

As inclusões, alterações e exclusões de Produto/Serviço são feitos através do Linha RM, que identifica o evento em sua entidade e envia uma mensagem ao Protheus SigaMNT . Através da sincronia de dados o Protheus pode utilizar os produtos  ou serviços enviados, em seus processos de Manutenção de Ativos ou Gestão das Frotas de Veículos.   
 Os dados sincronizados pela mensagem única são :

**Aba Identificação**

* Código do Produto
* Data Cadastramento
* Inativo
* Nome fantasia
* Tipo
* Número do Produto no Fabricante

**Aba Detalhes / Descrição**

* Descrição

**Aba Detalhes / Caracteristicas**

* Peso Bruto
* Peso Líquido

**Aba Detalhe / Outros Dados**

* Ref.

**Aba preço**

* Preço à Prazo / Preço
* Preço à Vista / Data-Base
* Preço à vista / Preço

**Aba Controle de Estoque**

* Controlado por lote
* Unidade de Controle
* Usa número de série

**Aba custos**

* Custo Médio / Valor
* Custo unitário / Valor

**Aba Informações por Filial / Editar o registro da respectiva Filial :**

* Consignado

**Anexos / Informações do Estoque**

* Lote Econômico de Compras

**Observações:**

1 - Os campos abaixo informados serão enviados somente  depois que for feita alguma alteração  no produto  cadastrado anteriormente:

* + Data Cadastramento
  + Lote Econômico de Compras
  + Cód.Cliente/Fornecedor

2 -  A integração Linha RM x Protheus SigaMNT permite que seja informado  somente o campo Controlado por lote  ou Usa número de Série. Se forem informados ambos os campos simultaneamente  será emitida uma mensagem  de informação .  
 3 -   O  campo Tipo  envia na mensagem os valores abaixo de acordo com a seleção:

* + 06 – mercadoria
  + 07 – mão de obra

              4 - Os campos exibidos na tela do Protheus SigaMNT são :

* + Armazem Pad.
  + Ativo
  + C Unitario
  + Cliente
  + Codigo
  + Custo Stand.
  + Descricao
  + Fator Conv.
  + Grupo
  + Lote Minimo
  + Origem
  + Peso Liquido
  + Pos.IPI/NCM
  + Preco Venda
  + Produto
  + Seg.Un.Medi
  + Tipo
  + Ult. Calculo
  + Ult. Preco
  + Unidade

**Observações :**

1. Serão enviados para o PROTHEUS somente os Produtos/Serviços de Último Nível.
2. Caso a integração esteja ativa, não será permitido o cadastramento de produtos controlados por lote e série, devendo ser selecionada somente uma das opções.
3. Produtos globais no BackOffice RM não serão considerados globais no sistema de destino, sendo enviada uma mensagem de inclusão para cada empresa a qual o produto faz parte.
4. Produtos globais no BackOffice RM não serão considerados globais no sistema de destino, sendo enviada uma mensagem de inclusão para cada empresa a qual o produto faz parte.
5. Caso haja ao menos uma mensagem enviada com sucesso ao SigaMNT, mesmo havendo erro nas mensagens referentes ao produto para as outras coligadas, não será apresentada mensagem de erro e a alteração/inclusão não será desfeita.
6. Não serão enviadas informações de Cliente/Fornecedor do Produto.
7. O campo B1\_CODITE no cadastro de Produtos do PROTHEUS deve ser alterado, via apsdu, para não obrigatório e também deve-se retirar sua validação.
8. O campo "Código do Produto" no PROTHEUS deve ser alterado para tamanho 30 caracteres para manter compatibilidade com o RM.

---

Para mais detalhes sobre o cadastro , acese o Boletim Técnico.

**Recursos Adicionais**

TDN - Boletim Técnico :  [Produto / Serviço](http://tdn.totvs.com/download/attachments/76251248/CONNECTOR_BT_CADASTRAR+PRODUTO+OU+SERVI%c3%87O_BR_CON000158.pdf?version=1&modificationDate=1380044697000)
