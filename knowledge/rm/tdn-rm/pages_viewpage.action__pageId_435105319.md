---
content_hash: 42aeaabc5900baa48c74000c8d4ffc1f255e7744eac7ccf22955586a07f4cb23
fetched_at: '2026-06-29T00:09:49.558626+00:00'
page_id: '435105319'
product: rm
source: tdn-rm
title: Lançamentos de Repasse
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105319
version: 5
---

**Lançamentos de Repasse**

---

Atenção

Toada vez que o repasse foi marcado depois da geração do plano, deverá executar o reajuste em seguida, pois ele criará as parcelas de repasses antes de qualquer operação no repasse. E quando for baixar, o financeiro visualizará a parcela de repasse e fará a sua liberação para ser baixado.

Não será gerado repasse para parcelas que não tem reajustes, pois a premissa é na geração do plano ou via aditivo. No reajuste é gerado porque o valor da parcela é alterado e o repasse é cancelado e gerado novamente.

Uma outra saída de contorno, seria fazer um aditivo global de alteração de valor de parcela para uma componente novo, do tipo encargo, colocar uma valor simbólico, selecionar as vendas e parcelas com repasses, executar o aditivo  e despois desfazer o aditivo na visão global de aditivo. É uma sugestão paliativa.

**O que é Repasse?**  
   
O TOTVS Incorporação permite que nos seus lançamentos financeiros da venda sejam feitos repasses de acordo com as configurações de parceiros dos Empreendimentos, Unidade e Subunidade.  
   
O Repasse é um valor pago ao parceiro da imobiliária de acordo com o percentual da subunidade em que este é dono. Ou seja, a incorporadora recebe o valor integral do cliente (comprador), mas paga um percentual desse recebimento para quem é sócio do empreendimento.  
   
*Por exemplo:*  
*O Parceiro XYZ é sócio de 25% do empreendimento ABC. Logo, para cada venda efetivada para este empreendimento, o parceiro XYZ receberá 25% de cada pagamento feito no financiamento das subunidades.*  
   
Esse pagamento de 25% não é feito automaticamente na parcela que o cliente da Incorporadora paga (Lançamento a receber). Para isso, são criados automaticamente parcelas de repasse vinculadas ao Parceiro, que basicamente é um Fornecedor cadastrado no sistema.  
   
Nos modelos pré-fixados como PRICE, SAC e SACRE, os Juros serão adicionados tanto nas parcelas do financiamento quanto nos lançamentos de repasse. O Cálculo é feito de acordo com o percentual referente ao parceiro cadastrado.  
   
**Observação:** A funcionalidade de repasse está disponível tanto para a versão de mercado quanto a de revitalização. Na versão de Mercado, o repasse não é gerado automaticamente pelo módulo do TIN, para que isso seja feito, basta ir no módulo financeiro, selecionar os lançamentos referentes à venda, ir nos processos e na opção de gerar repasse. Já na versão revitalizada, todo esse processo é feito automaticamente ao gerar os lançamentos da venda, ou seja, com a venda efetivada, já é possível gerenciar as parcelas de repasse financeiro.  
   
Para mais informações sobre o repasse do empreendimento acesse:  
Repasse do Empreendimento

[Repasse com Multa, Juros e Desconto](https://tdn.totvs.com/x/fT7dKQ)  
   
   
**Funcionamento**  
   
O Repasse funciona da seguinte forma:  
   
Primeiramente deve ser cadastrado o percentual do repasse no Empreendimento. Pode-se cadastrar um ou mais parceiros com percentuais distintos, respeitando o total de 100%. De acordo com esta regra podem ser incluídos parceiros para as unidades do empreendimento e para as subunidades existentes, se o repasse for cadastrado diretamente na subunidade, ela tem prioridade no repasse, assim como a unidade tem prioridade sobre o empreendimento.  
   
Com os percentuais cadastrados, é necessário configurar um componente que gere o repasse. Para isso deve-se cadastrar um tipo de Parcela com essa parametrização, basta acessar o cadastro de tipo de parcela, ir no anexo "Parâmetros do tipo de parcela" e marcar a opção Gerar Repasse.   
   
Crie um componente do tipo Principal e com o Tipo de parcela que gere repasse. Este tipo de parcela pode ser cadastrado no sistema conforme a necessidade do negócio.  
   
Com os cadastros devidamente realizados, podemos criar a venda para uma subunidade que contenha os dados de repasse cadastrados, gerar o plano de financiamento, efetivar e gerar os lançamentos financeiros.   
   
   
   
**Alteração dos lançamentos de Repasse**  
   
Alguns processos do TIN podem alterar o lançamento de repasse, seja no percentual, no Parceiro e no valor a ser repassado inclusive. Seguem abaixo as situações em que podem ocorrer essas alterações:  
   
**Reajuste:** No reajuste, o valor da parcela do financiamento é alterado, seja pelo Juros ou pela Correção Monetária. Com esse valor diferente na parcela, automaticamente o valor da parcela de Repasse é alterado proporcionalmente.  
   
*Exemplo:*  
*Valor da parcela antes do reajuste: R$1000,00 -> Valor a ser repassado 10% = R$100,00*  
*Valor da parcela após reajuste: R$1000,00 + R$10,00 (Juros) + R$5,00 (CM) = R$1015,00 -> Valor a ser repassado 10% R$101,50.*  
   
Observação: O Reajuste sempre irá verificar se existe parcelas de Repasse, em casos onde inicialmente não existe um parceiro para a subunidade, mas no futuro entrar algum parceiro, o lançamento de repasse será incluído no financiamento após o próximo reajuste acontecer.  
   
   
**Distrato:** Suponha que em uma determinada venda que contenha repasse, algumas parcelas foram baixadas parcialmente, inclusive suas parcelas de repasse.   
   
*Exemplo:*   
*Parcela 1: R$ 1000,00 -> Baixado: R$ 500,00*  
*Repasse: R$100,00 -> Baixado: R$ 50,00*  
   
Ao realizar um distrato seja com devolução ou não o sistema irá cancelar as parcelas baixadas parcialmente, depois irá criar novas parcelas com o valor do saldo devedor e então quitá-las, lembrando que essa nova parcela terá o valor proporcional em seu repasse. Se o saldo devedor é de R$500,00, então o valor do repasse novo será de R$50,00.  
Na versão revitalizada, caso o distrato houver parcelas de devolução, esse processo só ocorrerá quando a parcela de devolução estiver baixada e o distrato estiver quitado, para isso basta executar o processo Quitar Distrato.  
   
   
**Aditivo de alteração de valor de parcela:** Neste aditivo o TIN irá recalcular o valor da parcela do financiamento e fazer a proporção dos valores para o lançamento de repasse correspondente.   
   
   
**Aditivo de Renegociação de Contrato:** Da mesma forma no aditivo de alteração de valor, a renegociação de contrato irá alterar o valor da parcela, porém ela irá incluir esse valor em outra parcela, em um novo lançamento financeiro. Dependendo da configuração da nova parcela, ela poderá ou não ter um lançamento de repasse. O que definirá isso é se a nova parcela é de um tipo de parcela que gera repasse.  
Dentro da renegociação de contrato temos três opções:

* Inclusão de Parcelas: A nova parcela, se for de um tipo que gere repasse, acontecerá como na geração de lançamentos financeiros.
* Padrão: Serão canceladas as parcelas selecionadas e nas novas parcelas, se forem do tipo que gerem repasse, então será feito proporcionalmente o lançamento de repasse de acordo com a soma dos valores das parcelas selecionadas.
* Cancelamento de Parcelas: Para cancelar as parcelas, tanto o lançamento do financiamento quanto o lançamento de repasse serão cancelados.

**Aditivo de troca de subunidade:** Inicialmente esse aditivo não altera o valor das parcelas do financiamento, porém o repasse depende do parceiro que está cadastrado na subunidade, na unidade ou no empreendimento. Caso a troca acontecer pra uma subunidade que não tem dados de repasse cadastrados, então o lançamento de repasse não existirá nas parcelas. E o contrário também é verdadeiro. Caso a nova subunidade pertencer a outro parceiro ou então possuir um percentual diferente, o lançamento de repasse será alterado de acordo com as novas configurações.  
   
   
**Aditivo de troca de Comprador:** Caso houver parcelas parcialmente baixadas no financiamento, os lançamentos de repasse sofrerão alterações na troca de comprador, assim como nos aditivos de renegociação de contrato, as parcelas parcialmente baixadas se tornam quitadas, é gerado um lançamento novo com o valor do saldo devedor da parcela e então esta parcela é cancelada. E ao mesmo tempo é gerado uma parcela em aberto com o valor do saldo devedor para o novo comprador. Esta nova parcela em aberto terá o lançamento de repasse com o percentual sobre o valor desta nova parcela.  
   
**FIDEICOMISO**: A partir da versão 12.1.19 o Totvs incorporação terá o gerenciamento de repasse também pelo FIDEICOMISO. A grande diferença para a forma de repasse atual é que será feito via geração de movimento e irá atender ao mercado internacional.  
   
   
**Diferenças entre a versão de Mercado e a versão Revitalizada:** Na versão de Mercado, para gerar os lançamentos de repasse, devemos ir nos lançamentos financeiros da venda, ir no menu *Processos -> Repasse -> Repasse automático*. Dessa forma podemos escolher um tipo de parcela para gerar os lançamentos de repasse, que são gerados com a data de vencimento o para a data atual do sistema.  
Já na versão revitalizada do Totvs Incorporação, cada lançamento de repasse é gerado juntamente com a geração do plano de financiamento, a data de vencimento de cada repasse é igual à data de vencimento do lançamento de origem.   
Para verificar os dados do repasse, basta ir em *Processos -> Repasse -> Exibir Repasse*.

|  |  |
| --- | --- |
|  | Veja Também |

---

Dados de Repasse do Empreendimento  
Distrato Contratual Aditivos  
Tipo de Parcela  
Parâmetros do Tipo de Parcelas
