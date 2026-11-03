---
content_hash: 62376913eae874ecd0f9ed5d80df895eeb18e8f69201076204b7517b9b32cd42
fetched_at: '2026-06-29T00:10:26.883660+00:00'
page_id: '515290296'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-5833 DT Agrupamento de lançamento do movimento (TOTVS Gestão
  de Faturamento) a boletos no Educacional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=515290296
version: 15
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Gestão Educacional |
| Função: | Geração de lançamento |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : |  |

## **02. SITUAÇÃO/REQUISITO**

A venda de material escolar é realizada através do TOTVS Gestão de Faturamento onde é gerado o lançamento financeiro que não tem nenhum vínculo com o Educacional, no entanto o cliente deseja que os boletos gerados pelo educacional agrupe aos lançamentos financeiros originados das vendas de material escolar.

## **03. SOLUÇÃO**

Realizamos uma evolução no TOTVS Gestão Educacional para que seja possível agrupar nos boletos das parcelas lançamentos originados do TOTVS Gestão Faturamento.

**Parametrização**

O agrupamento de lançamento originados da venda de produtos irá ocorrer durante a geração do lançamento da parcela no educacional, para que o educacional saiba qual filial que será consultada é necessário que a mesma esteja parametrizada.

Foi disponibilizado no cadastro da filial no anexo “Dados Educacionais” a aba integração, no qual deverá ser marcada a opção que habilita o agrupamento, e informado quais o tipo de movimento são permitidos.

A opção apresentada na imagem acima deverá ser marcada no cadastro da filial em que a venda do produto é faturada.

Esta melhoria está disponível para todos os clientes a partir da versão 12.1.25, sendo necessário instalar o patch mais recente da versão e executar o RM Atualizador pra que a opção fique disponível.

**Agrupamento de Lançamentos**

O lançamento financeiro originado da venda do produto será agrupado ao boleto da parcela do educacional durante a geração do lançamento, neste momento o processo realizará uma análise na filial parametrizada identificando se existem lançamentos gerados para o tipo de movimento parametrizado que podem ser agrupados ao boleto da parcela que está sendo gerada.

Regras para que o lançamento seja agrupado:

* Deve ter o mesmo responsável financeiro
* Mesma dada de vencimento
* As parcelas não podem ser do tipo extra
* A conta caixa parametrizada deve ser a mesma para o lançamento Educacional e a do movimento
* No cadastro da conta caixa a filial não pode ser informada
* Se o lançamento já estiver gerado, o status tem que ser igual a “Aberto”, e o boleto não pode esta remetido ao banco.
* Se o lançamento já estiver gerado, não será permitido realizar o agrupamento quando pelo menos um deles estiver em processo de cobrança terceirizada nas **versões 12.1.2302 e superiores**
* O lançamento originado da venda do produto não pode ter boleto gerado

O agrupamento de lançamento será aplicado somente para a forma de agrupamento por “**Aluno**” ou “**Responsável financeiro**”

No agrupamento por “**Aluno**” só será executado no lado do Educacional, pois no movimento não é possível identificar qual material é para cada aluno.   
Então após o Educacional agrupar os lançamentos por aluno o mesmo irá no movimento e fará uma analise se existe para o mesmo responsável financeiro com as mesmas características dos lançamentos que serão agrupados e fará o agrupamento no primeiro aluno. 

Ao finalizar a execução do processo de geração de lançamentos se houver lançamentos que foram agrupados serão discriminados no log.

Conforme a imagem abaixo o TOTVS Gestão Financeira pode estar parametrizado para aceitar o vencimento a receber em finais de semanas e feriados considerando o primeiro dia útil posterior ou anterior.

Portanto é importante que o TOTVS Gestão Educacional também esteja com a parametrização compatível, pois a data de vencimento é utilizado para identificar os lançamentos que serão agrupados, veja a imagem abaixo.

div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
]]>
