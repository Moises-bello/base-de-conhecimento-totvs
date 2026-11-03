---
content_hash: 8dee56e14c60f131711c2ac973d5aa464592cf956632bcfea3356ac45cf8db2a
fetched_at: '2026-06-29T00:09:48.328270+00:00'
page_id: '435105123'
product: rm
source: tdn-rm
title: Contratos de Venda - How To - Como cadastrar uma Venda
type: documentation
url: https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+How+To+-+Como+cadastrar+uma+Venda
version: 7
---

**Como cadastrar uma Venda**   
O cadastro genérico de uma Venda é realizado da seguinte forma:   
   
**Pré Condições**

* Empreendimento, Unidade e Subunidade cadastrados;
* Comprador do Contrato cadastrado como Cliente/Fornecedor;
* Componentes de Financiamento.

**Passos**

* Deve se acessar o cadastro de Contratos de Venda, no TOTVS Incorporação, e clicar no botão **Incluir**;
* Caso o parâmetro "**Venda Sequencial**", que se encontrar no menu Ambiente | Parâmetros | TOTVS Incorporação| Contrato | Venda/Aluguel esteja desmarcado, será necessário informar o Número da Venda no campo Venda/Aluguel;
* Informe no campo **Data Venda/Aluguel**, a data da Venda;
* Informe qual o **Empreendimento** da Venda no campo Empreendimento;
* Caso ache necessário informe os campos de **Modalidade e Conta/Caixa**;
* Insira um **Item Contrato**, que será a subunidade envolvida na venda. Preencha os campos Unidade, Subunidade. Caso a subunidade possua Tabela de Preço vinculada, o preço será preenchido automaticamente.
* Insira um ou mais **Comprador**, definindo um deles como Comprador Principal, no qual será vinculado os Lançamentos Financeiros gerado pela Venda;
* Cadastre as **Condições de Financiamento**. Caso tenha inserido uma Modalidade no Contrato, as Condições de Financiamento será preenchida com os componentes da Modalidade, podendo ser alterados;
* Após o Cadastro  das Condições de Financiamento, será possível executar o processo **Gerar Plano de Financiamento**.

Através desse processo será gerado os Lançamentos Financeiros, Bloqueados ou Provisionados conforme parametrizado no campo: Tipo de bloqueio venda", que se encontra no seguinte caminho: Ambiente|Parâmetros|Totvs Incorporação|Integração Financeira|Bloqueio de lançamentos venda.

* Após a Geração do Plano de Financiamento, poderá ser executado o processo **Efetivar Contrato,** no qual será confirmado a venda da subunidade vinculada ao Contrato;
* Execute o processo **Desbloquear os Lançamentos Financeiros,** para assim ser possível realizar os processos dos Lançamentos Financeiros, como Baixa e Emissão de Cheque.

false

Veja Também

---

* [Desbloquear Lançamento Financeiro](http://tdn.totvs.com/pages/viewpage.action?pageId=435105171)
Versão 12.1.2606 em Diante

Agora será possível acessar o HELP Contrato de vendas pela tela de Vendas , basta clicar com Botão direito do Mouse sobre o contrato de vendas e selecionar - Documentação.
