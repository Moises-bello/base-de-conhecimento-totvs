---
content_hash: 761b83c998c649393b0230543a8384f85a4e76b131f2019527db57e49498d09d
fetched_at: '2026-06-29T00:09:16.958911+00:00'
page_id: '421388540'
product: rm
source: tdn-rm
title: Conciliar Títulos em Cobrança
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388540
version: 9
---

O processo de captura consiste na importação de um arquivo gerado pelo banco, com os dados dos títulos de DDA pendentes para confirmação, e o processo de conciliação utiliza um ou mais campos chaves para fazer a associação entre os dados do DDA e a lista de lançamentos a pagar em aberto no RM.

Conciliação com o Valor Líquido

Pra realizar a conciliação utilizando o Valor Líquido, deve selecionar o parâmetro 'Utilizar valor líquido na conciliação DDA*'* por coligada para definir que será utilizado o Valor Líquido como critério de pesquisa no processo “Conciliar Título de Cobrança”. Este parâmetro se encontra em *Contas a Pagar | Pagamento Eletrônico | Integração Bancária*. Por default a opção fica desabilitada.

**Obs:**

* Quando o parâmetro estiver habilitado, ao selecionar o campo “Valor Líquido”, obrigatoriamente é exigido que pelo menos um outro filtro também seja selecionado;
* A execução de cálculo de valor líquido poderá tornar o processo mais lento dependendo da quantidade de informações selecionadas para conciliação do DDA.

Ao iniciar o processo, deve realizar a definição das informações que o sistema utilizará para procurar os lançamentos, tais como:

* Número do Documento
* Data Emissão
* Data Vencimento
* Valor (Valor Original ou Valor Líquido)
* CPF/CNPJ
* Raiz do CNPJ

Após realizar a procura será exibido o título e a referência do lançamento encontrado.  
As seguintes ações serão disponibilizadas:

Conciliar automaticamente  
É conciliado o título encontrado pelo sistema, conforme as opções selecionadas na primeira etapa do processo de Conciliar Títulos em Cobrança.

Conciliar manualmente  
Selecionar outro lançamento de acordo com a sua necessidade e finalizar o processo.

Não conciliar o título  
Selecionar um status de captura e finalizar o processo, o título não será conciliado e ficará com o status que você selecionou.  
Posteriormente o título poderá ser conciliado novamente.

Após finalizar o processo o "Status" do título será atualizado, a referência do lançamento conciliado será relacionada ao título e os campos do lançamento serão preenchidos.

Status dos Títulos:

* 0 - Não conciliado;
* 1 - Conciliado Automaticamente;
* 2 - Conciliado Manualmente;
* 3 - Indevido;

Veja Também

* [DT- Conciliação Automática no DDA considerando Valor Liquido](https://tdn.totvs.com/x/bab1H)
