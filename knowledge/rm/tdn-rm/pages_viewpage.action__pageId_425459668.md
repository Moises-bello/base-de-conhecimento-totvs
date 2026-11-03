---
content_hash: ef0df1ccb0404cc2071e7adf3a047ee6a6879c673086226f04bfab807628f6a8
fetched_at: '2026-06-29T00:09:38.003082+00:00'
page_id: '425459668'
product: rm
source: tdn-rm
title: TOTVS Obras e Projetos x BackOffice Protheus - Cadastro Empresas/Filiais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459668
version: 2
---

**TOTVS Obras e Projetos x BackOffice Protheus - Cadastro Empresas/Filiais**

---

A inclusão, alteração e exclusão de empresas e filiais são realizadas no Protheus, sendo permitido realizar no TOP apenas a consulta dos registros sincronizados.   
    
 Como visto nos Parâmetros, é necessário informar no parâmetro MV\_RMCOLIG o código da Coligada RM correspondente à Empresa Protheus corrente. Este procedimento deve ser feito para cada empresa no Protheus.  
    
 Para cadastrar as Coligadas (Empresas) no RM, acesse: RM | Serviços Globais | Administração | Coligadas   
 Para configurar o parâmetro MV\_RMCOLIG, realize o login na empresa desejada e acesse: Protheus | SigaCFG | Ambiente | Cadastros | Parâmetros   
    
 **Dados Sincronizados**  
    
 Os dados sincronizados do Protheus para o TOP referente ao cadastro Empresas/Filiais são:

* Código da Coligada
* Código da filial
* Nome
* Nome fantasia
* CNPJ
* Código da filial em sistemas externos

***Observações:***

* No Protheus, o cadastro das Empresas/Filiais é realizado pela importação de um arquivo no momento da implantação do mesmo.
* Para utilizar uma Filial no Protheus não basta cadastrá-la, é necessário "liberá-la" para utilização.
* Quando for efetuada uma exclusão no Protheus, o registro correspondente será inativado no TOP.
* A sincronização de empresas e filiais no Protheus ocorre apenas quando são gravadas alterações no cadastro de Empresa/Filial.

Neste caso, acesse: Protheus | SigaCFG | Empresa | Arquivo | Criação da Empresa  
 Abra a edição dos dados cadastrais da empresa, e mesmo sem realizar nenhuma alteração clique em gravar. Ao sair do cadastro é iniciado o sincronismo da empresa selecionada no contexto e de suas filiais. Ao final o RM e o Protheus estarão sincronizados. Este procedimento deve ser feito para cada empresa.  
    
    
 **Tipos de Movimento**  
    
 Para cada nova filial sincronizada para o RM, são criados automaticamente os tipos de movimentos utilizados na integração. São eles:

* 1.1.01 – Solicitação de Compra (Requisição Almoxarifado)
* 1.1.02 – Solicitação de Compra Histórico
* 1.2.01 – Pedido de Compra
* 1.2.02 – Adiantamento a Pagar
* 1.2.03 – Despesa Avulsa
* 2.1.01 – Pedido de Venda
* 2.2.01 – Baixa de Estoque
* 2.2.02 – Estorno
* 2.2.03 – Adiantamento a Receber

***Observação:***

Quando apenas o TOP está instalado, o cadastro de tipos de movimento no RM está como somente leitura. Através da integração o acesso deve ser restrito ao supervisor do sistema.   
    
 É possível ver os tipos de movimento acessando:RM | Projetos | Construção e Projetos | Opções | Construção e Projetos | Projetos | Integração | Suprimentos e Faturas | guia Geral e guia Tipos de Mov. Pedidos   
    
    
 **Local de Estoque**  
    
 A manutenção de Local de Estoque será realizada no TOP e não será sincronizada imediatamente. Os almoxarifados no Protheus são criados à medida que são referenciados pela primeira vez. Por exemplo, quando o Protheus receber uma Requisição de Armazém (RA), o local de estoque será criado, caso já não exista.  
    
 A Filial e o Local de Estoque definidos no RM não serão alterados durante o faturamento, permanecendo até a Nota Fiscal.Para realizar a manutenção de local de estoque no TOP acesse: RM | BackOffice | Gestão de Estoques, Compras e Faturamento | Cadastros | Local de Estoque
