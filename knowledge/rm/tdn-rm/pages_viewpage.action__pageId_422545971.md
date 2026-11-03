---
content_hash: 5f43242e9c7ef89007ecf657defc7dd769f3f51a840782a76eedc798984204c9
fetched_at: '2026-06-29T00:09:22.108521+00:00'
page_id: '422545971'
product: rm
source: tdn-rm
title: Cancelar Lançamento (Fiscal)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545971
version: 6
---

Por esta opção o usuário poderá realizar o cancelamento de lançamentos posterior a emissão da NF(s) de Saída da mercadoria na Empresa. Esses lançamentos portanto serão eliminados da subtotalização dos relatórios / saldos do período sem serem excluídos da tela de consulta/cadastro.

*****Observações:*****Somente serão cancelados pelo sistema, lançamentos que pertencerem a Períodos Fiscais com status em ABERTO  
Ao cancelar um Lançamento Fiscal que tenha gerado lançamentos contábil no TOTVS Gestão Contábil, o TOTVS Gestão Fiscal irá excluir o lançamento contábil. O lançamento contábil somente será excluído, caso não tenha sido integrado ao Lote 0 ( zero ) no TOTVS Gestão Contábil.  
Não é permitido cancelar lançamentos de entrada emitido por terceiros. Quando tentar cancelar uma mensagem é apresentada, avisando que esta operação não será possível.  
O sistema respeita as seguintes regras para o cancelamento de Lançamentos Fiscais:

* Notas Fiscais emitidas pelo próprio contribuinte;
* Lançamento Fiscal que não seja extemporâneo;
* Lançamento Fiscal que não seja referente à Redução Z (exceto se o estado da Filial for MG);
* Lote Fiscal associado ao Lançamento deve estar aberto;

***Atenção*:** Não é possível cancelar Lançamentos Fiscais incluídos pelo TOTVS Gestão de Estoques, Compra e Faturamento, apresentada a seguinte mensagem:

*Lançamento Fiscal com origem no Módulo de Compras/Vendas. Operação não poderá ser efetuada.*

Para cancelar o Lançamento deve ser executado o processo de Estorno de Escrituração, através do TOTVS Gestão de Estoque, Compra e Faturamento, cancelar o movimento e posteriormente escriturar o movimento novamente.
