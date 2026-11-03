---
article_id: 18161075539351
category: CRM - Dúvidas Gerais
content_hash: 7893d0798eb2f9e4ac3c1b5b47cc0895c811291e1fbca97591efe60b7081f306
fetched_at: '2026-06-28T22:40:27.690092+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGACRM - Fornecedores (CRMA510)
type: support-article
updated_at: '2024-03-21T17:19:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18161075539351-Cross-Segmentos-Backoffice-Protheus-SIGACRM-Fornecedores-CRMA510
---

**![tempo Ícone](https://cdn-icons-png.flaticon.com/128/4608/4608011.png) Tempo aproximado para leitura: 00:02:30 min****Dúvida:**Qual funcionalidade da rotina "Fornecedores" (CRMA510)?  
  
**Ambiente:**Cross Segmentos - Backoffice Protheus - SIGACRM - Todas as versões.  
  
**Solução:**

Esta rotina permite registrar fornecedores tipo: **Pessoa física**, **Pessoa jurídica**, ou **Outros** (Exterior - uso para importação). O pagamento dos fornecedores é feito por meio de títulos a pagar gerados pelos registros dos documentos de entrada, ou por registros manuais utilizando os recursos disponíveis no módulo **Financeiro**.

Os dados gerados e movimentados para o fornecedor, no módulo **Financeiro**, atualizam a **Consulta Posição Financeira** do Fornecedor, em que estão destacados: **Saldo em duplicatas a pagar, Maior compra, Primeira compra, Última compra, Maior saldo, Média de atraso, Quantidade de compras, Títulos em aberto, Títulos pagos**, entre outros.

O devido preenchimento deste cadastro é importante para definir o perfil completo do fornecedor. Dados que podem ser utilizados em outras rotinas do Sistema.

```
![Help_button](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/help_button.zoom40.gif)Importante!  
  
Fornecedor é a entidade que tem por objetivo suprir as necessidades de produtos ou serviços de uma empresa, seja ela nacional ou não.  
  
Quando o fornecedor é um prestador de  serviços, o registro deve existir no Cadastro de Produtos.  
  
Quando o ERP Protheus possuir integração com o Gestão de Frete Embarcador (SIGAGFE), esse cadastro é integrado com a rotina Cadastro de Emitentes (GFEA015).
```

```
![Help_button](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/help_button.zoom40.gif)Dica!  
  
É importante destacar também os cadastros de amarrações Produto x Fornecedor e Grupo x Fornecedor, pois vinculam um Fornecedor a um ou mais Produtos, ou Grupos de Produtos. Entretanto, o Sistema permite receber produtos e serviços de outros fornecedores, mesmo que não haja amarração.  
  
As amarrações Produto x Fornecedor e Grupo x Fornecedor são essenciais para a geração da Cotação de Compras a partir da Solicitação de Compras.
```

**Objetivos Específicos por ambiente:**

* [Comércio Exterior (SIGAEIC, SIGAECO, SIGAEFF e SIGAECO)](https://tdn.totvs.com/pages/viewpage.action?pageId=345541948)
* [Gestão Agrícola](https://tdn.totvs.com/pages/viewpage.action?pageId=345543040)

 Se configurada a rotina *Schedule* e o *Adapter* EAI, temos a integração do TIN (TOTVS Incorporações) e Microsiga Protheus® para envio e recebimento de arquivos XML, de acordo com o XSD homologado pela Totvs®.

```
![Help_button](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/help_button.zoom40.gif)Importante  
  
Disponível o parâmetro MV_AGCUSTO para utilização da aglutinação de custos por empresas ou filiais realizando o cálculo on-line (direto na tabela de saldos SB2).  
  
Para utilizar a aglutinação é necessária a configuração do parâmetro MV_CUSFIL com o conteúdo E (Empresa) para aglutinar por Empresa e com conteúdo F (Filial) para que seja por Filial.
```

**Procedimentos:**

Para cadastrar um fornecedor:

1. Em **Fornecedores**, selecione **Incluir**. O Sistema apresenta a tela de inclusão subdividida em pastas que facilitam o gerenciamento das informações.
2. Preencha os dados conforme orientação do *help* de campo.
3. Observe, porém, o preenchimento de alguns campos nas seguintes pastas:

* + [Pasta Cadastrais](https://tdn.totvs.com/pages/viewpage.action?pageId=345543106)
  + [Pasta Adm/Fin](https://tdn.totvs.com/pages/viewpage.action?pageId=345543136)
  + [Pasta Fiscais](https://tdn.totvs.com/pages/viewpage.action?pageId=345543151)
  + [Pasta Compras](https://tdn.totvs.com/pages/viewpage.action?pageId=345543158)
  + [Pasta TMS](https://tdn.totvs.com/pages/viewpage.action?pageId=345543855)
  + [Pasta Outros](https://tdn.totvs.com/pages/viewpage.action?pageId=345543875)

         4. Confira os dados e confirme.

Para cada fornecedor, podemos relacionar diversos contatos. Consulte o item **Relacionando Contatos** para mais informações.

```
![Help_button](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/help_button.zoom40.gif)Observação:  
  
Argentina: Quando o percentual do IVA for inferior a 100% é impossível excluir o fornecedor.
```
