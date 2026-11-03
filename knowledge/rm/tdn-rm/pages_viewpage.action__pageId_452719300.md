---
content_hash: ada4c40c944e32d6f459772f38ef23e37123680b57061ccb7b9237d9c0a9ef02
fetched_at: '2026-06-29T00:10:05.725031+00:00'
page_id: '452719300'
product: rm
source: tdn-rm
title: GPS - Compensação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719300
version: 80
---

falseATENÇÃO!

A partir da versão 12.1.2406, esse processo foi descontinuado. A GPS foi substituída pela DCTFWeb.

* Para a geração do lançamento financeiro da DCTFWeb, consulte a documentação: [Link](https://tdn.totvs.com/pages/viewpage.action?pageId=727915586)
* Para conferência dos valores da DCTFWeb, consulte a documentação: [Link](https://tdn.totvs.com/pages/viewpage.action?pageId=717708785)

{+}<http://mpas.gov.br/arquivos/office/3_081014-104500-450.pdf+>|http://mpas.gov.br/arquivos/office/3\_081014-104500-450.pdf]
 
 
Em +Encargos | Guia de INSS | Consulta Saldo de Compensações+
Na primeira utilização do controle, o usuário deve alimentar as informações, caso exista valores a compensar de meses anteriores.
Sendo que, se existir valores a compensar de meses anteriores para:
+Recolhimento 150{+}, deve cadastrar o saldo de retenções conforme a seção centralizadora da geração de INSS (matriz e filial), sendo desnecessário informar o tomador de serviço, devido neste caso, a guia de INSS ser gerada por estabelecimento (matriz/filial),
 
+Recolhimento 155{+}, é necessário cadastrar a seção centralizadora e o tomador de serviço (obra) e o saldo de retenções para cada tomador, devido neste caso, a guia de INSS é gerada por tomador.
 
O campo 'Tipo de Saldo' deve ser '3-Compensações Anteriores'
 
 
Em +Encargos | Parâmetros INSS/FGTS+
São informados os valores do mês a serem compensados (compensações e retenções) na guia de INSS.
Sendo que, para a seção (quebra de CNPJ) é verificado na +aba Valores I+ os campos 'Compensação', e para os tomadores é verificado o +Anexo Parâmetros Tomadores de Serviço | Valores os campos+ 'Compensação no mês' e 'Valor de Retenção (Lei 9711/98) '.
 
\*Observação I:\*
Quando utilizar o controle de compensação não é necessário o preenchimento dos campos 'Compensação' e 'Compensação no mês'.
O sistema verifica estes campos, devido existir a possibilidade de não estar parametrizado para utilizar o controle de compensação.
 
\*Observação II:\*
Para o recolhimento 150, a guia de INSS é gerada por estabelecimento (matriz/filial), devendo cadastrar os valores conforme a seção centralizadora da geração de INSS (matriz e filial), sendo desnecessário informar o tomador de serviço.
Para o recolhimento 155, a guia de INSS é gerada por tomador, sendo necessário cadastrar a seção centralizadora e o tomador de serviço (obra) e os valores para cada tomador.
 
\*Observação III:\*
Quando integrado com o RM Nucleus, os valores de retenções são verificados no momento do cálculo da guia de INSS.
 
 
Em +Encargos | Guia de INSS | Guia de INSS+
Após o cálculo da guia de INSS é disponibilizada a opção 'Atualizar Saldo de Comp. e Ret.', para que ao executar, os valores de compensação do mês (Retenção, Compensação e Dedução) que não serão utilizados na geração da guia de INSS devido não existir saldo, sejam guardados para compensação futura.
Os valores são atualizados automaticamente com 1% juros (processo interno do sistema) e quando a tabela SELIC está cadastrada, os valores são atualizados mais taxa SELIC, de acordo com a Instrução Normativa da Previdência Social no Artigo 203:
I - o valor originário integral a ser compensado pelo sujeito passivo será atualizado com juros calculados na forma do art. 230(\*);
(\*) Art. 230. O valor a ser compensado, reembolsado ou restituído será corrigido monetariamente conforme art. 509 e, a partir de 1º de janeiro de 1996, acrescido de juros calculado da seguinte forma:
I - em relação aos valores a serem compensados ou restituídos, um por cento relativamente ao mês em que houve o pagamento indevido, a taxa SELIC relativamente aos meses intermediários entre o pagamento indevido e a efetiva compensação ou restituição e de um por cento no mês em que estiver sendo efetuada a mencionada compensação ou restituição;
II - em relação aos valores a serem reembolsados, um por cento relativamente ao mês subsequente àquele que se referir o reembolso, a taxa SELIC relativamente aos meses intermediários entre aquele que se referir o reembolso e o do seu efetivo pagamento e de um por cento no mês em que estiver sendo efetuado o mencionado reembolso.
 
A compensação pode ser efetuada em tantos recolhimentos de competências subsequentes quantos forem necessários.
 
A compensação dos valores obedece a seguinte ordem: +Retenção | Dedução | Compensação/Reembolso{+}.
 
\*Atenção I:\*
Sempre que executar 'Atualizar Saldo de Comp. e Ret.', os valores armazenados anteriormente referente à competência da geração da guia de INSS são deletados e os novos valores são armazenados.
 
\*Atenção I:\*
Para empresas que o valor de Dedução, Retenção e Compensação/Reembolso é maior que o valor a pagar da guia é emitido uma mensagem e a guia é gerada com o valor de Terceiros, devido o pagamento de Terceiros ser obrigatório.
 
\*Atenção III:\*
São armazenados os valores a serem compensados somente quando a competência da geração da guia de INSS é igual ou anterior à competência da folha.
 
\*Atenção IV:\*
Somente são compensados os valores armazenados com o mesmo código de recolhimento.
 
\*Observação:\*
Para o recolhimento 150, a guia de INSS é gerada por estabelecimento (matriz/filial), os valores não compensados são armazenados conforme a seção centralizadora da geração de INSS (matriz e filial).
Para o recolhimento 155, a guia de INSS é gerada por tomador, os valores não compensados são armazenados por tomador.
 
Em +Encargos | Guia de INSS | Consulta Saldo de Compensações+ foi informado um valor de compensação no valor de R$800,00 referente ao mês anterior (este valor é referente a uma dedução superior ao valor da guia de INSS).
 
!worddav390cd839dc55a72856904989ef85e547.png|height=402,width=526!
Em +Encargos | Guia de INSS | Consulta Saldo de Compensações+ foi informado um valor de compensação no valor de R$800,00 referente ao mês anterior (este valor é referente a uma dedução superior ao valor da guia de INSS).
 
!worddavdec445326e01553279fde2656fa1c947.png|height=521,width=513!
 
 
Cadastrada a tabela SELIC em +Administração de Pessoal | Cadastros Globais | Cotações+
!worddav82125adeadbd968f7cc58bbf4d555abf.png|height=168,width=467!
O valor atualizado é obtido mediante aplicação do coeficiente disponível na tabela SELIC sobre o valor originário da contribuição, a partir do mês subsequente ao mês do fato gerador da compensação e 1% relativamente ao mês em que estiver sendo efetuada.
\*Exemplo:\*
Fator gerador da compensação: 12/2011
Valor não compensado:             R$800,00
Mês da efetivação:                    03/2012
 
Cálculo conforme tabela acima:
SELIC Janeiro/2012                   800,00 \* 0,88% = R$7,04
SELIC Fevereiro/2012                800,00 \* 0,94% = R$7,52
Juros fixos mês da efetivação     800,00 \* 1,00% = R$8,00
Total da correção monetária       R$22,56
 
\*Observação:\*
Existindo mais de um índice cadastrado na mesma competência, é considerado o último índice.
Ao calcular novamente a guia de INSS, o campo 'Compensação/reembolso' é preenchido com o valor de R$800,00 mais a correção monetária, sendo os valores:
!worddavfe51b1f976306ff053a85d1724ab3dcf.png|height=412,width=495!
Não sendo possível abater toda a compensação, é apresentada a mensagem novamente e ao clicar em \[Atualizar Saldo de Comp. e Ret.\], os valores são atualizados na tabela PGPS e a correção monetária apresentada é apenas sobre o valor compensado:
!worddavf39627644fad0b6dd4196d1764c90807.png|height=508,width=555!
 
Valor compensado                     = R$641,12
Correção                                  = R$18,08
SELIC Janeiro/2012                   = 641,12 \* 0,88% = R$5,64
SELIC Fevereiro/2012                = 641,12 \* 0,94% = R$6,03
Juros fixos mês da efetivação     = 641,12 \* 1,00% = R$6,41
 
No anexo +Compensações Realizadas na Guia de INSS+ são registrados os meses em que a compensação foi realizada até que o valor seja totalmente compensado. Conforme tela abaixo:
!worddav75524c8cdef30b7ae2bc61a8f385207e.png|height=363,width=505!
 ]]>

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Guia de INSS
