---
article_id: 115008509088
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 7ac049a726b679fefd2babac4494ebef47be3787189e927970c37c57d81956c2
fetched_at: '2026-06-28T22:40:47.395566+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - o que fazer quando
  meu arquivo TXT não traz nenhuma informação
type: support-article
updated_at: '2024-04-23T18:13:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115008509088-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-o-que-fazer-quando-meu-arquivo-TXT-n%C3%A3o-traz-nenhuma-informa%C3%A7%C3%A3o
---

**Dúvida**

O que fazer quando meu arquivo TXT não traz nenhuma informação?

**Ambiente**  
  
Microsiga Protheus – Ativo fixo – A partir da versão 11.80

**Solução**

Todos os registros de saldos para o ECF dependem que o Plano de Contas e Centro de Custo (quando utilizado) estejam corretos. Neste caso é necessário verificar:

* Pelo módulo TAF, no menu Atualizações / Cadastros / Contábeis / Plano de Contas, se o plano de contas foi corretamente integrado.

* Após é necessário visualizar as contas do tipo Analítica e verificar se existe Conta Referencial amarrada.

No caso em que código da conta referencial é exibido como ERR001 significa que na integração entre os módulos SIGACTB e TAF foi enviado o código da conta referencial, porém este código não foi encontrado no cadastro de Autocontidas do TAF (Tabela CHA), isso pode acontecer quando:

* O cadastro das tabelas Autocontidas referentes ao Plano de Contas Referencial não contém informações. Para isso verifique pelo módulo TAF no menu Atualizações /Consultas / Tabela dinâmicas (Tabela CHA), caso não exista a informação execute o compatibilizado UPDISTR.

Link de Apoio: <http://tdn.totvs.com/pages/releaseview.action?pageId=181143062>

* A tabela Autocontida referente ao plano de contas referencial está carregada porém o código da conta referencial enviada não existe, para isso compare com os códigos de contas existentes no manual de Orientação ECF, pois o código pode estar incorreto.

Se o cadastro do plano de contas está correto, com as contas referenciais amarradas no TAF, é necessário verificar o registro em que a informação não vai para o TXT.

* Nos casos dos registros referentes ao Balanço Patrimonial, Demonstrativos de Resultados não deve-se utilizar a mesma Visão Gerencial aplicada para a entrega do ECD, pois a estrutura da visão Não é a mesma.

* Nos casos dos registros referentes ao Balanço Patrimonial, Demonstrativos de Resultados ou qualquer registro gerado a partir de Visão Gerencial, verifique se o código da conta enviado está no mesmo padrão solicitado pelo Manual de Orientação do ECF.

* Em alguns casos é utilizado um código diferente do padrão, e com isso ao acessar o registro pelo modulo TAF é gravado a informação com CODIGO e DESCRIÇÃO DA CONTA em branco e o valor preenchido corretamente.

Exemplo de código de Conta:  
Correto: 1.01.01.01.01  
Errado: 00000001

Para maiores informações acesse: [ECF](http://tdn.totvs.com/display/PROT/ECF)
