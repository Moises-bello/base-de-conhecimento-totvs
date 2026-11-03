---
content_hash: a101e04b4ba0737d6b28d4dd0c24692a6c25d80898c6005bf1abaef4fe722b8b
fetched_at: '2026-06-29T00:09:26.492742+00:00'
page_id: '423938302'
product: rm
source: tdn-rm
title: Identificador de item do Razão Auxiliar de Subcontas 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938302
version: 6
---

**INTRODUÇÃO**

O livro razão auxiliar das subcontas foi implementado na ECD – Escrituração Contábil Digital, a partir de janeiro de 2016. Portanto, as empresas obrigadas ao livro razão auxiliar, conforme Instrução Normativa RFB 1.515/2014, transmitirão o livro "Z" na ECD de 2016 (ano-calendário 2015). As empresas que também estão obrigadas ao razão auxiliar no ano-calendário 2014, também entregarão o livro "Z" na ECD de 2016.

Os parágrafos 3º e 4º do art. 33 da IN 1.515 informam quando o RAS será obrigatório.  
§ 3º No caso de conta que se refira a grupo de ativos ou passivos, de acordo com a natureza desses, a subconta poderá se referir ao mesmo grupo de ativos ou passivos, desde que haja livro razão auxiliar que demonstre o detalhamento individualizado por ativo ou passivo.  
§ 4º Nos casos de subcontas vinculadas a participação societária ou a valor mobiliário a que se referem os arts. 54 a 61, que devam discriminar ativos ou passivos da investida ou da emitente do valor mobiliário, poderá ser utilizada uma única subconta para cada participação societária ou valor mobiliário, desde que haja livro razão auxiliar que demonstre o detalhamento individualizado por ativo ou passivo da investida ou da emitente do valor mobiliário.

O RAS deverá ser enviado quando os valores lançados na Subcontas não estão detalhados, neste caso o usuário deverá entregar o livro "Z" contendo o detalhamento individualizado das Subcontas por ativo ou passivo no RAS.

**O detalhamento individualizado a ser enviado no RAS pode não ser controlado no ERP RM** e em alguns casos o usuário cadastra apenas o Lançamento Contábil consolidado.

**EXEMPLO:**

Empresa JJMJ possui um investimento temporário em 3 ações (VALE5, PETR4 e BBAS3):

* Valor do Investimento em 2015 = R$ 100.000,00
* Valor Justo das Ações em 30/06/2015 = R$ 70.000,00
* Livro Razão Auxiliar das Subcontas: deve identificar o AVJ (Ajuste Valor Justo) por ação.

VALE5 = R$ 10.000,00 (10.000 ações compradas em 02/02/2015 por R$ 30.000,00)

PETR4 = R$ 15.000,00 (10.000 ações compradas em 15/02/2015 por R$ 50.000,00)

BBAS3 = R$ 5.000,00  (10.000 ações compradas em 31/05/2015 por R$ 20.000,00)

No exemplo acima teremos no TOTVS Gestão Contábil os Lançamentos Contábeis com os valores detalhados na conta de Investimentos. Ex: A aquisição das ações em 02/02/2015 corresponde a um fato contábil e foi registrado no dia 02/02/2015, no dia 15/02/2015 e dia 31/05/2015 também foram registrados os respectivos fatos, porém não houve detalhamento em contas distintas, os lançamentos foram feitos todos utilizando a conta "Investimentos Temporários".

O lançamento referente ao (Investimento - AVJ) de R$ 30.000 (detalhamento das perdas por ações) que se encontra em subconta conforme Art. 47 da IN 1.515 não foi detalhado em contas específicas,  o valor de R$ 30.000 é referente ao investimento em 3 empresas, mas foi consolidado em apenas uma conta.

**Identificador de Item**

Cadastro de identificação do item que será detalhado nos lançamentos de detalhamento do RAS.

Aqui serão informados alguns dados, tais como:

* Código do patrimônio;
* CNPJ da investida;
* Descrição;
* Reconhecimentos: Ocorre quando acontece o registro do ativo ou passivo na contabilidade. EXEMPLO: Na compra de ações, o reconhecimento é QUANDO a compra foi
* registrada na contabilidade;
* Realizações: Ocorre por exemplo quando há depreciação ou baixa de um ATIVO. EXEMPLO: A realização de uma máquina ocorre à medida que ela deprecia.

OBSERVAÇÕES

* Os reconhecimentos devem ser informados manualmente quando o campo "Identificar a Data do Reconhecimento / Saldo Inicial da Conta Contábil correspondente ao item através do lançamento contábil?" estiver desmarcado. Caso contrário será necessário informar o identificador do item dentro da própria partida contábil na aba "SPED Contábil", desta forma o sistema vincula automaticamente o valor referente a cada investimento (no caso do exemplo acima);
* Não será possível adicionar mais de um reconhecimento com a mesma data.

Veja também
