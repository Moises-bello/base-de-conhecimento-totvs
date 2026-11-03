---
content_hash: 6b9aad02e329a3ab5c3ee31e3ccf560e3809f3a4e51d59aae5b0fa1ac925774b
fetched_at: '2026-06-29T00:11:10.144488+00:00'
page_id: '641464976'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Shopping
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=641464976
version: 82
---

## Introdução

Shopping center é uma locação atípica (um contrato misto, em que se sobressai a locação), onde existe várias empresas que realizam determinadas cobrança por entidade vigente no contrato:

* **Aluguel Mínimo:** Valor do contrato de locação.
* **Aluguel sobre Faturamento:** Percentual cobrado sobre o faturamento do Lojista.
* **Condomínio:** Cobrança de Encargos Comuns, Medições e despesas.
* **Fundo promocional:** Cobrança por valor/percentual sobre o marketing.

Através do nosso módulo podem ser efetuadas todas essas cobranças, bastando configurar a regra do seu contrato.

---

TOTVS Construção Gestão de Imóveis – Shopping – Confissão de Dívida
  
[TOTVS Construção Gestão de Imóveis – Shopping – Template de Confissão de Dívida](https://tdn.totvs.com/pages/viewpage.action?pageId=825295895)  
[TOTVS Construção Gestão de Imóveis – Shopping – Fundo Promocional](https://tdn.totvs.com/pages/viewpage.action?pageId=661867357)  
[TOTVS Construção Gestão de Imóveis – Shopping – Lançamentos](https://tdn.totvs.com/pages/viewpage.action?pageId=893920960)  
[TOTVS Construção Gestão de Imóveis – Shopping – Cobrança Partilhada](https://tdn.totvs.com/pages/viewpage.action?pageId=893921587)  
[TOTVS Construção Gestão de Imóveis – Shopping – Boletos](https://tdn.totvs.com/pages/viewpage.action?pageId=893922236)  
[TOTVS Construção Gestão de Imóveis – Shopping – Negociação de Boletos](https://tdn.totvs.com/pages/viewpage.action?pageId=1062376748)  
[TOTVS Construção Gestão de Imóveis – Shopping – Mapa de Cobrança](https://tdn.totvs.com/pages/viewpage.action?pageId=643555980)  
[TOTVS Construção Gestão de Imóveis – Shopping – Relatórios](https://tdn.totvs.com/pages/viewpage.action?pageId=815588371)
]]>

---

INTRODUÇÃOProcedimentos para utilização

Para cadastrarmos um fundo promocional, primeiramente será necessário habiltar nos parâmetros / Gestão de imóveis / Aluguel / Menu Shopping e marcar a opção: Utilizar módulo de shopping.   
Em seguida precisaremos dar a permissão para o usuário realizar o cadastros de fundo promocional que se encontra em *Segurança >* *Perfil > Shopping > Fundo de Promoção*

Habilitando esta permissão, basta ir no menu *Shopping / Fundo Promocional* e realizar um cadastro.

Segue uma breve descrição dos campos:

* **Coligada**: A coligada onde serão gerados os lançamentos do fundo promocional. Pode ser diferente da coligada dos contratos associados.
* **Descrição**: Descrição do cadastro.
* **Aplicar reajuste do contrato:** A opção aplicar reajuste, define se o fundo deverá ser reajustado. O reajuste ocorrerá quando o tipo de cobrança é definido como "Valor" e o processo de reajuste é executado para o contrato associado ao fundo de cobrança.
  + Processo do reajuste de fundo promocional
    - Serão utilizados os mesmos índices cadastrados no contrato para reajustar o fundo associado.
    - O valor do fundo promocional será reajustado independente da data de inicio de cobrança.
    - A data do reajuste do fundo é a mesma data do reajuste do contrato de locação. Esta data e valor reajustado serão preenchidos na aba histórico de valores.
    - Quando houver a geração do lançamento financeiro, ele irá valer-se da regra de vencimento do contrato associado (vencido, vincendo ou personalizado) para definir o início do período da parcela e gerar um lançamento de fundo promocional. Será respeitada a data de vencimento que é definida no cadastro de fundo e os valores então, serão definidos de acordo com a data inicial e final do histórico. Se existe reajuste neste período ou não.
* **Tipo de evento financeiro:** O evento financeiro que será utilizado para geração do fundo promocional. Somente eventos do tipo "Fundo Promocional" podem ser associados.
* **Parâmetros de integração financeira:** Os parâmetros que serão utilizados para geração do fundo promocional.
* **Tipo de cobrança:** Valor ou percentual.

Importante:  
O sistema permitirá associar um mesmo contrato a N templates de fundos promocionais diferentes, flexibilizando cobranças diferentes nos mesmos períodos ou não.

Geração e exclusão de lançamentos para fundo promocional

Toda a geração de lançamentos para fundo promocional é realizada através da [geração de lançamentos](https://tdn.totvs.com/pages/viewpage.action?pageId=435105008) do contrato de aluguel. A partir da versão 12.1.2302 também será possível gerar os lançamentos de fundo promocional em um processo próprio na visão do contrato de locação.

Para a geração de lançamentos do fundo promocional, o contrato de locação deverá estar associado a um template de fundo promocional, com todos os parâmetros preenchidos.

Para entender como anexar um contrato de aluguel a um template de fundo promocional, [veja o procedimento seguindo este link (clique aqui).](https://tdn.totvs.com/display/LRM/Fundo+Promocional+-+Anexos+-+Contratos+do+Fundo+Promocional)

Estando o cadastro associado e o fundo preenchido, Ao gerar os lançamentos do contrato de locação o sistema irá verificar se para este contrato existe fundo promocional cadastrado.

Os lançamentos, serão incluídos num evento financeiro do tipo "**Fundo Promocional**", e obedecerão o parâmetro de dia de vencimento cadastrado [no anexo de contrato do fundo promocional.](https://tdn.totvs.com/display/LRM/Fundo+Promocional+-+Anexos+-+Contratos+do+Fundo+Promocional)

O mês e o ano do vencimento da parcela do fundo irá valer-se da regra de vencimento do contrato associado (vencido, vincendo ou personalizado). A data de vencimento será sempre a cadastrada no fundo promocional.

Para excluirmos os lançamentos de um fundo promocional, o processo também é realizado através do contrato de locação, utilizando o [processo de exclusão de lançamentos financeiros.](https://tdn.totvs.com/pages/viewpage.action?pageId=435105003)

---

A partir da Versão 12.1.2302 será possível parametrizar o sistema para não gerar o fundo promocional no momento de gerar o lançamento do contrato de locação.  
Para utilizar esta funcionalidade será necessário realizar algumas parametrizações:  
  
1) No perfil do usuário será necessário disponibilizar acesso a estes menus:  
  
  
  
No menu Processos da visão de contratos de locação, as seguintes opções serão apresentadas apresentados:   
  
  
  
2) Em seguida acesse os Parâmetros : TOTVS Incorporação | Aluguel | Contrato de Locação, desmarque a opção: Gerar lançamentos de fundo promocional juntamente com lançamentos de locação.  
Quando desmarcado as parcelas de fundo promocional serão geradas apenas quando selecionado o seu processo específico na visão de contratos.

3) Ao acessar a visão de contratos e selecionar a opção: Gerar lançamentos financeiros de fundo promocional, somente as parcelas de fundo promocional serão geradas.

Cobrança em dobro

Através do anexo de cobrança em dobro, poderemos parametrizar competências onde existirão cobranças em dobro, de acordo com os parâmetros definidos neste cadastro.

Para saber como cadastrar a cobrança em dobro, [veja o procedimento seguindo este link (clique aqui).](https://tdn.totvs.com/pages/viewpage.action?pageId=676048646)

**Veja mais**

---

* [Contratos do Fundo Promocional](https://tdn.totvs.com/display/LRM/Fundo+Promocional+-+Anexos+-+Contratos+do+Fundo+Promocional)
* [Cobrança em Dobro](https://tdn.totvs.com/pages/viewpage.action?pageId=676048646)
* [Aplicar Reajuste](https://tdn.totvs.com/pages/viewpage.action?pageId=435104980)
* [Desfazer Reajuste](https://tdn.totvs.com/pages/viewpage.action?pageId=435105398)
* [Fechamento de contas a receber](https://tdn.totvs.com/pages/createpage.action?spaceKey=LRM&fromPageId=641464976)
Exemplos de contratos sobre Faturamento

Processo responsável pela geração de aluguel complementar (ou aluguel sobre faturamento) de contratos de locação. As parcelas geradas são avulsas, ou seja, não são agregadas aos lançamentos financeiros de locação, e podem ser visualizadas pelo anexo **Lançamentos financeiros** do contrato de locação.

Antes de executar o processo é necessário considerar alguns pontos:

* Contrato de locação parametrizado para aluguel complementar conforme definido em contrato. Para mais informações dos campos, .
* Faturamento cadastrado na respectiva competência. Para mais informações dos campos a serem preenchidos, .

São os seguintes campos na tela de execução do processo:

* **Mês/Ano:** Mês e ano do faturamento;
* **Código locatário:** Este campo possibilita filtrar as informações de Aluguel Complementar por locatário;
* **Contrato locação:** Este campo possibilita filtrar as informações de Aluguel Complementar por Contrato de Locação;
* **Filtrar Coligadas:** Neste campo o usuário seleciona quais coligadas farão parte da busca;
* **Botão Pesquisar:** Botão faz a busca, caso algum período de algum contrato de locação esteja dentro do Mês/Ano informado, o mesmo será mostrado na grid para a geração do aluguel complementar;
* **Grid com as medições:** Mostra os registros das medições encontrados para o período informado;

Ao selecionar os faturamentos e prosseguir com a execução do processo, então o sistema irá realizar o cálculo do valor do aluguel complementar, gerar um evento financeiro automático do tipo locação complementar para cada contrato de locação se ainda não houver, e finalmente gerar a(s) parcela(s).

O cálculo do valor do aluguel complementar é realizado de acordo com os parâmetros definidos. Para todos os cálculos será necessário preencher as faixas de faturamento. São os diferentes tipos de cálculo que o sistema realiza:

#FF9000ALUGUEL CONSIDERANDO CONDOMÍNIO E FUNDO PROMOCIONAL (CTO FIXO)

Para geração de lançamentos utilizando CTO Fixo em contratos de shopping poderemos parametrizar o sistema seguindo os passos do vídeo abaixo.   
Este processo não necessita de parametrização de faixas para aluguel complementar. Todo o valor definido de CTO é gerado pelo processo de "Geração de Lançamentos" do contrato de aluguel.

**Fique atento! A partir da versão 12.1.2209, o campo CTO mensal passa a compor o cadastro das faixas. Para maiores informações, clique aqui:**

#FF9000FATURAMENTO CONSIDERANDO CONDOMÍNIO E FUNDO PROMOCIONAL (CTO ZERADO)

Caso o Valor mínimo no período e o Valor CTO Mensal não sejam preenchidos, ao marcar a opção "Considera condomínio", ou a opção "Considera fundo promocional" o valor do condomínio e do fundo promocional serão descontados junto ao valor do aluguel base do valor do Faturamento.

*Contrato locação > Aluguel Complementar*

Exemplo: Valores Mínimos não preenchidos, marcado o campo **Considera condomínio** na aba de Aluguel Complementar:

*Contrato locação > Lançamento Financeiro de Condomínio*

Valor condomínio na competência:

*Contrato de Locação > Anexos > Controle de Faturamento:*

Faturamento: **R$ 550.000,00**.

Porcentagem: **3%**.

3% de R$550.000,00 = **R$ 16.500,00**

Valor do aluguel mensal: **R$ 1.000,00.**

Valor do condomínio na competência:  **R$ 3.500,00.**

R$ 16.500,00 - (R$ 1.000,00 + R$ 3.500,00) = **R$ 12.000,00**

Exemplo: Contrato com o campo marcado "Considera fundo promocional":

Para que o fundo promocional seja descontado do valor total do faturamento, devemos primeiramente acessar o cadastro de fundo promocional.

Após o cadastro do fundo, deveremos gerar os lançamentos do contrato de aluguel para a determinada competência.  O sistema irá gerar um evento financeiro do tipo Fundo Promocional, com as devidas parcelas já integradas ao Financeiro.

Para que o lançamento do fundo promocional seja considerado no cálculo do aluguel complementar, também devemos realizar o procedimento abaixo:

*Contrato locação > Aluguel Complementar*

Marcado o campo **Considera fundo promocional** na aba de Aluguel Complementar do contrato de locação:

Acessar *Contrato de locação > Controle de faturamento;*

Inserir um faturamento **na mesma competência** que o evento do tipo fundo promocional foi integrado.

Exemplo: Evento financeiro do tipo fundo promocional integrado e na competência 12/21.

Faturamento cadastrado na competência 12/21

Acessar *Contrato de Locação > Anexos > Controle de Faturamento:*

Faturamento: **R$ 220.000,00**.

Porcentagem: **10%.**

*Ao gerar o lançamento do aluguel complementar, o fundo promocional será calculado no seguinte formato:*

Valor do faturamento na competência de 12/2021: 220.000,00  
Percentual do faturamento na competência de 12/2021: 10,0000%  
Cálculo do valor do aluguel complementar (Valor do faturamento \* percentual / 100): 220.000,00 \* 10,0000% / 100 = 22.000,00

Considerar fundo promocional: Sim  
Fundo Promocional: 2000,0000

Cálculo do valor do aluguel complementar (faturamento - (valor do aluguel + valor do condomínio + valor do fundo promocional)):  
22.000,00 - 2.000,00 = 20.000,00

### Gerando lançamentos para o sócio do empreendimento

---

Quando o contrato não possui um valor mínimo definido, ou seja, o campo Valor período é = 0 e o meu valor do contrato é também igual a zero e eu ainda preciso considerar o condomínio e o fundo promocional, haverão momentos onde o meu valor de faturamento é menor do que o valor do meu faturamento. Nestes casos específicos, toda a diferença será gerada na forma de um lançamento cadastrado para o sócio do empreendimento.

Para cadastrar um sócio do empreendimento, [siga este exemplo (clique aqui).](https://tdn.totvs.com/display/LRM/Empreendimento+-+Anexo+-+Dados+de+Repasse+Empreendimento)

Estando o sócio ou os sócios cadastrados no empreendimento, podemos continuar com essa geração.

A imagem acima mostra que não temos um valor mínimo definido e nem mesmo o contrato possui um valor de aluguel.

Neste exemplo básico, na competência do mês 01/21 o controle de faturamento que temos é o seguinte:

E o condomínio e o fundo promocional para esta competência são respectivamente **R$ 4850 e R$ 780;**

Diante disso, ao geramos o aluguel complementar para esta competência teremos o seguinte cálculo:

**7% de R$ 50.000 = R$ 3500**

**R$ 3500 (Valor de Aluguel) - R$ 4850 (Valor de Condomínio) - R$ 780 (Fundo Promocional)**

**Total residual = R$ 2130**

O Valor então de **R$ 2130** será gerado para os sócios cadastrados no empreendimento como mostramos acima.

O sistema também faz o rateio de acordo com os percentuais cadastrados no empreendimento.

Estes lançamentos são gerados durante o processo do aluguel complementar como mostra a imagem abaixo:

Os lançamentos do sócio podem ser acessados na aba de lançamentos financeiros do contrato de aluguel.

O faturamento na competência 01/21 passa a ter o status "Valor residual para sócios" exemplificando que não tivemos geração de aluguel complementar, mas sim apenas a geração dos lançamentos para os sócios do empreendimento.

Quando o lançamento do sócio é gerado o sistema irá fazer o recálculo do lançamento financeiro de condomínio e irá utilizar um valor de integração com a ação de desconta para refletir este valor que será pago no condomínio.

Este valor de integração é definido por sócio do empreendimento e refletirá no lançamento de condomínio com seu devido rateio.

O rateio dos valores de integração referente aos sócios, será exibido na tela de apurações de cálculos do condomínio, como mostra a imagem abaixo:

Para cadastrar um valor de integração para o sócio do empreendimento, [siga este exemplo (clique aqui).](https://tdn.totvs.com/display/LRM/Empreendimento+-+Anexo+-+Dados+de+Repasse+Empreendimento)

Importante: Quando a soma do valor residual for maior que o valor do próprio condomínio, por exemplo, quando o fundo promocional em alguma competência tiver o seu valor maior que o próprio condomínio, Não serão gerados lançamentos para o sócio do empreendimento e o sistema irá emitir uma mensagem de erro na geração.

Quando o lançamento de sócio é excluído através do processo de cancelar aluguel complementar, todos os valores de integração serão removidos do lançamento de condomínio. Além disso, na apuração deste cálculo, teremos a informação de que estes valores foram removidos.

O lançamento do condomínio, quando possuir valores de integração referentes aos lançamentos residuais para os sócios, não poderá ser cancelado sem que antes sejam excluídas as parcelas do sócio via processo. Para detalhes sobre a exclusão dos lançamentos de sócio, verificar a documentação abaixo.

### Excluindo parcelas do sócio

---

Acesse a visão de contratos de locação, selecionando o registro de contrato que será cancelado, em seguida acesse: Processos > Aluguel Complementar > Cancelar Aluguel Complementar.

Informe a Competência e clique em executar;

Ao final da execução do processo o lançamento será cancelado.

Mais informações acesse:

[Contrato de Locação - Processo - Cancelar Aluguel Complementar](https://tdn.totvs.com/pages/viewpage.action?pageId=520659357)

#FF9000FATURAMENTO MÍNIMO MENSAL (VALOR CTO MENSAL)

O valor do faturamento mínimo mensal definido no campo **Valor CTO Mensal**, é entendido como a soma de todos os valores, Condomínio, Fundo Promocional e Aluguel.

Caso o valor esteja preenchido o checkbox de **Considera condomínio** é marcado automaticamente, pois já está incluso no valor.

O valor do faturamento é calculado sobre a porcentagem da faixa. O resultado é subtraído pelo valor mínimo mensal que é definido no contrato. Se o valor for menor ou igual a zero, então nenhum aluguel complementar é gerado. Exemplo de aplicação:

Exemplo de cadastro de Aluguel Complementar com o Valor CTO Mensal definido:

Cadastro de uma Medição de Faturamento que irá incidir os 3% definidos na aba de Aluguel Complementar:

*Contrato de Locação > Anexos > Controle de Faturamento:*

Faturamento: **R$ 550.000,00**.

Porcentagem: **3%**.

3% de R$550.000,00 = **R$ 16.500,00**

Valor mínimo mensal: **R$ 15.000,00.**

R$ 16.500,00 - R$ 15.000,00 = R$ 1.500,00

Portanto o sistema irá gerar um aluguel complementar no valor de **R$ 1.500,00**.

Neste tipo de cálculo, os lançamentos mensais de locação são gerados regularmente pelo processo de **Gerar lançamentos financeiros**. O valor da parcela poderá ser o valor do contrato, ou então se o contrato estiver com o valor zerado, neste caso o sistema irá gerar um aluguel residual para cada mês.

O aluguel residual é calculado subtraindo o valor mínimo mensal sobre o condomínio e fundo promocional. Por exemplo:

Valor mínimo mensal: **R$ 7.500,00.**

Condomínio: **R$ 4.750,00.**

Fundo promocional: **R$ 387,00.**

Aluguel mensal = Valor mínimo mensal - (condomínio + fundo promocional)

Aluguel mensal = R$ 7.500,00 - (R$ 4.750,00+ R$ 387,00)

Aluguel mensal = R$ 2.363,00

Portanto neste exemplo o valor do aluguel para esta competência seria de **R$ 2.363,00.**

**Importante:** A data de referência para o cálculo do aluguel residual é a data de início do período do contrato de aluguel.

**Exemplo:**

Período da parcela entre 01/01/21 e 31/01/2021;  
Fechamento de condomínio na competência 01/21.

Ao gerar o lançamento de aluguel no período 01/01 a 31/01 o sistema irá verificar a competência 01/21 do fechamento de condomínio caso exista, para abater o valor de condomínio deste lançamento.

#FF9000FATURAMENTO MÍNIMO POR PERÍODO

O valor do faturamento é calculado sobre a porcentagem da faixa. O resultado é subtraído pelo valor do condomínio e este será o único valor mensal do aluguel.  
Assistam no vídeo como é realizado este processo no sistema.

Agora um outro Exemplo de aplicação:

Faturamento:  **R$ 680.000,00**.

Porcentagem: **2,8%**.

2,8% de R$ 680.000,00 = R$ 19.040,00

Aluguel mensal: **R$ 19.040,00.**

Condomínio: **R$ 2.500,00**.

R$ 19.040,00 - R$ 2.500,00 = R$ 16.540,00

Neste cálculo seria gerado um aluguel complementar no valor de **R$ 16.540,00**. Este seria o valor mensal do aluguel para o locatário.

Além do valor mensal, o sistema também irá calcular o valor complementar por período. Neste caso o contrato deve ter cadastrado um limitador por período e a periodicidade. Se durante este período a soma dos valores mensais for menor que o limitador, então um outro lançamento complementar será gerado com a diferença. Por exemplo:

Limitador: **R$ 100.000,00**

Periodicidade: **6 meses**

Exemplo de valores mensais gerados:

|  |  |
| --- | --- |
| 1 | R$ 10.000,00 |
| 2 | R$ 15.000,00 |
| 3 | R$ 5.000,00 |
| 4 | R$ 20.000,00 |
| 5 | R$ 15.000,00 |
| 6 | R$ 5.000,00 |
| Total | R$ 70.000,00 |

Valor complementar por período = Limitador - aluguel mensal complementar

Valor complementar por período = R$ 100.000,00 - R$ 70.000,00

Valor complementar por período = **R$ 30.000,00**

#FF9000FATURAMENTO DE CINEMAS

Para contratos de locação do tipo cinema, as faixas de aluguel complementar devem ser configuradas com duas porcentagens: bilheteria e bomboniere. O sistema irá calcular o faturamento sobre a bilheteria e depois o faturamento sobre o bomboniere. Estes dois resultados serão somados e a soma será subtraída pelo valor do condomínio e fundo promocional. Por fim o valor será descontado do aluguel mensal e o resultado será o aluguel complementar. Exemplo de aplicação:

* Faturamento da bilheteria: **R$ 250.000,00**
* Porcentagem de faturamento da bilheteria: **8%**
* 8% de R$ 250.000,00 = R$ 20.000,00
* Faturamento do bomboniere: **R$ 78.000,00**
* Porcentagem de faturamento do bomboniere: **15%**
* 15% de R$ 78.000,00 = R$ 11.700,00
* Total de faturamento: R$ 20.000,00 + R$ 11.700,00 = **R$ 31.700,00**
* Valor do condomínio: **R$ 3.500,00**
* Valor do fundo promocional: **R$ 750,00**
* Valor do aluguel: **R$ 15.000,00**
* Valor do aluguel complementar = Valor do faturamento - (condomínio + fundo promocional + aluguel mensal)
* Valor do aluguel complementar = R$ 31.700,00 - (R$ 3.500,00 + R$ 750,00 + R$ 15.000,00)
* Valor do aluguel complementar = R$ 12.450,00
* Portanto o sistema irá gerar um aluguel complementar no valor de **R$ 12.450,00**.
#FF9000CONSIDERA FUNDO PERCENTUAL COM ALUGUEL FIXO E CTO PERCENTUAL 

No exemplo abaixo temos um cálculo de um contrato nas seguintes condições

* Aluguel fixo (Valor de Contrato definido diferente de zero)
* Encargos de condomínio (Lançamento de condomínio gerado na competência)
* Fundo promocional percentual (Template de Fundo Promocional definido com cálculo percentual)
* Faturamento (Medição de faturamento inserida na competência do cálculo)
* CTO Percentual (Definido na faixa do aluguel complementar do contrato)

Seguindo essas premissas, um exemplo de cálculo do faturamento com valores de exemplo, seguirá da forma abaixo:

Valor do faturamento: [200.000,00]  
Percentual sobre faturamento: [5%]  
Aluguel Complementar: (Valor do faturamento \* percentual) [200.000,00 \* 5% = 10.000,00]

Condomínio: [2000]

Fundo Promocional: [200]

Cálculo do valor do aluguel complementar (faturamento - valor do aluguel + valor do condomínio + valor do fundo promocional):  
10.000,00 - 4.200,00 = **7.800,00**

E o cálculo do fundo percentual neste mesmo contrato:

Fundo promocional da parcela gerada: 7 - Percentual  
O valor da parcela [200,00] na competência  [01/2023]

Valor do contrato: [R$ 2.000,00]  
Percentual do fundo promocional: [10,00%]  
Fundo Promocional \* Valor contrato: [10,00% \* R$ 2.000,00 = R$ **200,00**]

#FF9000CONSIDERA FUNDO PERCENTUAL SEM ALUGUEL FIXO E CTO MENSAL FIXO

No exemplo abaixo temos um cálculo de um contrato nas seguintes condições

* Sem Aluguel fixo (Valor de Contrato zerado)
* Encargos de condomínio (Lançamento de condomínio gerado na competência)
* Fundo promocional percentual (Template de Fundo Promocional definido com cálculo percentual)
* Faturamento (Medição de faturamento inserida na competência do cálculo)
* CTO Percentual (Definido na faixa do aluguel complementar do contrato)
* CTO Mensal (Definido na faixa do aluguel complementar do contrato)

Seguindo essas premissas, um exemplo de cálculo do faturamento com valores de exemplo, seguirá da forma abaixo:

Valor do faturamento: [200.000,00]  
Percentual sobre faturamento: [5%]  
Aluguel Complementar: (Valor do faturamento \* percentual) [200.000,00 \* 5% = 10.000,00]

Cálculo do valor do aluguel complementar (faturamento - valor CTO fixo (Valor Mensal)):  
10.000,00 - 5.000,00 = **5.000,00**

E o cálculo do fundo percentual neste mesmo contrato:

Fundo promocional da parcela gerada: 7 - Percentual  
O valor da parcela [272,73] na competência  [01/2023]

Valor do contrato: [R$ 0,00]  
Percentual do fundo promocional: [10,00%]  
Parcela: [R$ 5.000,00]  
Condomínio: [R$ 2.000,00]

Fundo promocional: (CTO Mensal - Condomínio) / (1 + (Percentual do fundo promocional))  
(R$ 5.000,00 - R$ 2.000,00) / (1 + R$ 10,00%)  = **R$ 272,73**

**Observações:**

* Caso exista um escalonamento para a mesma competência do faturamento, então será considerado o valor do escalonamento, e não o valor do aluguel.
* Com a execução da geração dos valores de Aluguel Complementar, serão criados automaticamente os registros de Eventos Financeiros com o tipo de Locação Complementar.
* Em caso de necessidade de cancelamento do lançamento do aluguel complementar e a sua regeração com novos dados, o usuário deverá ir no controle do faturamento, alterar qualquer campo editável na tela conforme desejado e salvar. O sistema irá solicitar uma confirmação de regeração do lançamento. Após a confirmação, o lançamento antigo será cancelado e excluído e o novo lançamento será criado e vinculado à medição. Este procedimento não é possível de ser realizado quando o lançamento estiver baixado.
* Ao incluir um faturamento de aluguel complementar, o registro fica com o status de 'Pendente', porém ao gerar os lançamentos do aluguel complementar, quando o faturamento não atingir o percentual necessário para incluir o lançamento complementar, a medição terá o status da medição alterado para 'Sem valor complementar'
* Ao gerar um aluguel complementar com o parâmetro **Considera condomínio** marcado porém sem valores de condomínio relacionados para o período do faturamento, o processo ira concluir com a mensagem de alerta, informando que não existe condomínio para a competência correspondente.

Para obter maiores informações sobre Aluguel Complementar

Tópicos relacionados:

---

Mapa de cobrança

O mapa de cobrança irá possibilitar ao usuário gestor do shopping visualizar todas as cobranças de todas as entidades do shopping associado em uma determinada competência.

Após o processo de fechamento todas as entidades de cobrança serão visualizadas, bem como seus valores, possibilitando assim um maior controle de todas as cobranças relacionadas a gestão do shopping.

#FF9000Procedimentos para Utilização

Para acessar o mapa de cobrança, precisamos primeiramente, dar acesso no Perfil do Usuário. Este acesso se dá no módulo de Serviços Globais em **Perfil / *Gestão de Imóveis / Shopping / Cadastro / Mapa de Cobrança.***

Após o acesso, o cadastro de mapa de cobrança estará disponível. Os campos deste cadastro são:

* **Competência: A competência das cobranças cujo mapa de cobrança irá agrupar;**
* **Identificador do Shopping: O shopping cujo mapa de cobrança será cadastrado;**
* **Observação: Texto livre de informações pertinente àquele mapa e ou competência.**

O anexo do mapa de cobrança irá exibir de forma detalhada todas as cobranças e valores associados à competência cadastrada.   
Esse resultado pode ser utilizado para o gerenciamento de cobranças possibilitando uma visão geral dos contratos em determina competência.

Os campos apresentados no anexo de mapa de cobrança são:

* **Código do contrato de locação;**
* **Valor do condomínio:** O valor do condomínio gerado na competência. Este valor somente será apresentado caso o fechamento tenha sido realizado e o lançamento de condomínio seja criado.
* **Número contrato de locação;**
* **Valor mínimo mensal:** Valor mínimo que deverá ser cobrado mensalmente. Parametrizado no aluguel complementar.
* **Valor período mínimo:** O valor total em R$ determinado no aluguel complementar
* **Período mínimo (meses):** O período definido em meses no cadastro de aluguel complementar onde haverá cobrança da diferença no aluguel complementar.
* **Situação contrato locação:** O mapa irá exibir apenas contratos efetivados ou rescindidos.
* **Valor de aluguel:**Compreende os valores somados dos lançamentos financeiros de aluguel na competência

Observação

Quando um faturamento não atingir o valor mínimo mensal (CTO Mínimo mensal) O campo valor do aluguel será mostrado com valores negativos, exemplificando a cobrança que será repassada ao sócio do empreendimento.

* **Valor de aluguel complementar:** Os valores em reais de aluguel complementar gerado na competência para um determinado contrato.
* **Valor de faturamento:** O valor total de faturamento na competência para um determinado contrato.
* **% de faturamento:** O percentual da medição de acordo com a faixa cadastrada nos parâmetros de aluguel complementar.
* **Valor do segundo faturamento:** Caso exista será preenchido de acordo com os parâmetros do aluguel complementar**;**
* **% Faturamento 2:**O percentual de faturamento 2 da medição de acordo com a faixa cadastrada nos parâmetros de aluguel complementar.
* **Total:** Compreende os valores somados dos lançamentos financeiros de aluguel na competência + valor complementar caso exista + valor do condomínio caso exista.
* **Valor de encargos:** Valores de fundo promocional quando cobrados atrelados ao aluguel complementar.
* **Coligada.**
Configurações de condominio

* [TOTVS Construção Gestão de Imóveis - Condomínio - Manutenção de Empreendimentos](https://tdn.totvs.com/pages/viewpage.action?pageId=435105380)
* [TOTVS Construção Gestão de Imóveis - Condomínio - Básicos](https://tdn.totvs.com/pages/viewpage.action?pageId=435105228)
* [TOTVS Construção Gestão de Imóveis - Condomínio - Fechamento do Condomínio](https://tdn.totvs.com/pages/viewpage.action?pageId=435104834)
RelatóriosImportante

Todos os relatórios listados abaixo estarão disponíveis a partir da versão **12.1.2306,** utilizando a nova estrutura do **Smartview.** Para saber mais sobre o Smartview e como instalá-lo**, [clique aqui!](https://tdn.totvs.com.br/pages/viewpage.action?pageId=626926739)**

* [Inadimplência](https://tdn.totvs.com/pages/viewpage.action?pageId=749058225)
* [Despesas do Sócio Empreendedor](https://tdn.totvs.com/pages/releaseview.action?pageId=747313890)
* [Rentabilidade](https://tdn.totvs.com/pages/viewpage.action?pageId=749067080)
* [Fechamento de contas a receber](https://tdn.totvs.com/pages/viewpage.action?pageId=751516019)
* [Encerramentos e Rescisões](https://tdn.totvs.com/pages/viewpage.action?pageId=753645721)
* [Extrato do condomínio](https://tdn.totvs.com/pages/viewpage.action?pageId=756461299)
