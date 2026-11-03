---
content_hash: 24fcb51bfc0a1ab0e97d38cd5a02ccb8b019575cb50a1a2b90457ab2e0524868
fetched_at: '2026-06-29T00:09:21.770416+00:00'
page_id: '422545902'
product: rm
source: tdn-rm
title: Atividade Imobiliária (Registros F200 e F210)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545902
version: 3
---

**Origem dos dados**

Os registros F200 e F210 serão gerados com as informações das unidades vendidas que tiveram parcelas pagas e baixadas no período da escrituração. Portanto a integração das parcelas deverá ser feita com o TOTVS Gestão Financeira. Em hipótese nenhuma estas informações serão geradas sem que o TOTVS Incorporação esteja instalado e implantado.

**Parametrizações necessárias**

Para a correta geração das informações da atividade imobiliária os empreendimentos/unidades vendidas deverão ter seus cadastros completos com todas as informações relevantes para a sua correta identificação de acordo com especificação técnica do TOTVS Incorporação.   
 Além dos dados de identificação do empreendimento e unidades os a seguir deverão ser informados.

1. Preencher os campos da aba - EFD-PIS/COFINS – Cadastro de empreendimento. Irá gerar o registro F200.
2. Executar o processo responsável por copiar as informações para a subunidade.
3. Informar os campos do anexo "EFD-PIS/COFINS – Custo Orçado – Ref.Pag. Pessoa Física", caso estes campos não seja preenchido no período em que se deseja gerar o EFD, o processo executado pelo financeiro não será finalizado corretamente. Irá gerar o registro F210

Para que as informações das unidades vendidas sejam geradas para o arquivo da rotina é necessária a criação de um processo no qual é informados os tipos de documentos utilizados para gerar as parcelas das vendas das unidades.  
 Para a criação do processo acesse Opções | Parâmetros | Processos:

1. Selecione o processo EFD PIS/COFINS e clique no botão Grupos e SubGrupos.
2. Selecione Registro F200 – Crédito da atividade imobiliária na parte esquerda da tela e dê um duplo clique no processo que será apresentada na parte direita da tela para o registro ser aberto para edição.
3. Em seguida acesse a guia Filtros. Nesta guia deverão ser incluídos os tipos de documentos utilizados para gerar as parcelas das vendas no TOTVS Gestão Financeira. Para cada tipo de documento deverão ser informados os tributos PIS e COFINS com suas respectivas CST. Deverá ser incluído um registro para cada tipo de documento utilizado.
4. Conforme manual e validador da EFD só serão aceitas:

* CST 01 e as alíquotas 0,65 ou 1,65 para o PIS
* CST 01 e as alíquotas 3,00 ou 7,60 para a COFINS

Este processo deverá ser executado para as informações dos tributos serem geradas nas parcelas.

**Execução do Processo**

Antes da geração da rotina o processo criado anteriormente deverá ser executado. Acesse Utilitários | Geração de Saídas | Cálculo das contribuições docs não escriturados e na tela que será apresentada selecione o mês e o ano para os quais será gerada a rotina e clique no botão incluir.  
***Observação:***  Este processo deverá ser executado sempre antes da geração da rotina e sempre que forem feitas alterações nas parcelas ou novas parcelas forem geradas para o financeiro.
