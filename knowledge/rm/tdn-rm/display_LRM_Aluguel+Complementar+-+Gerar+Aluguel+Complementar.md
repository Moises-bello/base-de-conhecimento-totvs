---
content_hash: 6ec7fc989cbbfe3b180e95c1080c36aa871d32ecc4bf7209e5a99fa52572cb8d
fetched_at: '2026-06-29T00:09:47.272906+00:00'
page_id: '435105013'
product: rm
source: tdn-rm
title: Aluguel Complementar - Gerar Aluguel Complementar
type: documentation
url: https://tdn.totvs.com/display/LRM/Aluguel+Complementar+-+Gerar+Aluguel+Complementar
version: 67
---

IMPORTANTE

A Partir da Versão 12.1.2410, os parâmetros necessários para a geração do aluguel complementar nos cenários abaixo, foram migrados diretamente para as

Processo responsável pela geração de aluguel complementar (ou aluguel sobre faturamento) de contratos de locação. As parcelas geradas são avulsas, ou seja, não são agregadas aos lançamentos financeiros de locação, e podem ser visualizadas pelo anexo **Lançamentos financeiros** do contrato de locação.

Antes de executar o processo é necessário considerar alguns pontos:

* Contrato de locação parametrizado para aluguel complementar conforme definido em contrato. Para mais informações dos campos, .  
  **Obs: Com a reforma tributária**, passamos a gerar no lançamento financeiro, os tributos IBS e CBS com base de cálculo, alíquota e valor, de acordo com a regra tributária informada no contrato de locação.: Para mais informações acesse: [Geração de lançamento financeiros - Locação, Aluguel Complementar e Aluguel em Dobro](https://tdn.totvs.com.br/pages/viewpage.action?pageId=1024340646)
* Faturamento cadastrado na respectiva competência. Para mais informações dos campos a serem preenchidos, .

São os seguintes campos na tela de execução do processo:

* **Mês/Ano:** Mês e ano do faturamento;
* **Código locatário:** Este campo possibilita filtrar as informações de Aluguel Complementar por locatário;
* **Contrato locação:** Este campo possibilita filtrar as informações de Aluguel Complementar por Contrato de Locação;
* **Filtrar Coligadas:** Neste campo o usuário seleciona quais coligadas farão parte da busca;
* **Botão Pesquisar:** Botão faz a busca, caso algum período de algum contrato de locação esteja dentro do Mês/Ano informado, o mesmo será mostrado na grid para a geração do aluguel complementar;
* **Grid com as medições:** Mostra os registros das medições encontrados para o período informado;

Ao selecionar os faturamentos e prosseguir com a execução do processo, então o sistema irá realizar o cálculo do valor do aluguel complementar, gerar um evento financeiro automático do tipo locação complementar para cada contrato de locação se ainda não houver, e finalmente gerar a(s) parcela(s).

Desconto do CTOObservação: A partir da versão 12.1.2406, o campo Desconto, presente na faixa de faturamento irá incidir sobre todos os cálculos abaixo, que envolvem CTO. Esse valor de desconto sempre será abatido do valor final do CTO calculado para a faixa em questão. Esse valor não é reajustado, sendo sempre fixo. Para alterá-lo o usuário deverá utilizar um aditivo de alteração de parâmetros de aluguel complementar e parametrizar novos valores de desconto para as faixas de faturamento. 

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

Quando o contrato não possui um valor mínimo definido, ou seja, o campo Valor período é = 0 e o meu valor do contrato é também igual a zero e eu ainda preciso considerar o condomínio e o fundo promocional, haverão momentos onde o meu valor de faturamento é menor do que o valor do meu CTO. Nestes casos específicos, toda a diferença será gerada na forma de um lançamento cadastrado para o sócio do empreendimento.

Para cadastrar um sócio do empreendimento, [siga este exemplo (clique aqui).](https://tdn.totvs.com/display/LRM/Empreendimento+-+Anexo+-+Dados+de+Repasse+Empreendimento)

Estando o sócio ou os sócios cadastrados no empreendimento, podemos continuar com essa geração.

Neste exemplo básico, na competência do mês 01/21 o controle de faturamento que temos é o seguinte:

E o condomínio e o fundo promocional para esta competência são respectivamente **R$ 4850 e R$ 780;**

Diante disso, ao geramos o aluguel complementar para esta competência teremos o seguinte cálculo:

**7% de R$ 50.000 = R$ 3500**

**R$ 3500 (Valor de Aluguel) - R$ 4850 (Valor de Condomínio) - R$ 780 (Fundo Promocional)**

**Total residual = R$ 2130**

O Valor então de **R$ 2130** será gerado para os sócios cadastrados no empreendimento como mostramos acima.

O sistema também faz o rateio de acordo com os percentuais cadastrados no empreendimento.

Estes lançamentos são gerados durante o processo do aluguel complementar.

Os lançamentos do sócio podem ser acessados na aba de lançamentos financeiros do contrato de aluguel.

O faturamento na competência 01/21 passa a ter o status "Valor residual para sócios" exemplificando que não tivemos geração de aluguel complementar, mas sim apenas a geração dos lançamentos para os sócios do empreendimento.

Quando o lançamento do sócio é gerado o sistema irá fazer o recálculo do lançamento financeiro de condomínio e irá utilizar um valor de integração com a ação de desconta para refletir este valor que será pago no condomínio.

Este valor de integração é definido por sócio do empreendimento e refletirá no lançamento de condomínio com seu devido rateio.

O rateio dos valores de integração referente aos sócios, será exibido na tela de apurações de cálculos do condomínio, como mostra a imagem abaixo:

Para cadastrar um valor de integração para o sócio do empreendimento, [siga este exemplo (clique aqui).](https://tdn.totvs.com/display/LRM/Empreendimento+-+Anexo+-+Dados+de+Repasse+Empreendimento)

Os lançamentos gerados para os sócios do empreendimento irão respeitar o Centro de Custo e a Natureza Orçamentária cadastradas no parâmetro de integração financeira do Empreendimento.

Quando a soma do valor residual for maior que o valor do próprio condomínio, por exemplo, quando o fundo promocional em alguma competência tiver o seu valor maior que o próprio condomínio, Não serão gerados lançamentos para o sócio do empreendimento e o sistema irá emitir uma mensagem de erro na geração.

Quando o lançamento de sócio é excluído através do processo de cancelar aluguel complementar, todos os valores de integração serão removidos do lançamento de condomínio. Além disso, na apuração deste cálculo, teremos a informação de que estes valores foram removidos.

O lançamento do condomínio, quando possuir valores de integração referentes aos lançamentos residuais para os sócios, não poderá ser cancelado sem que antes sejam excluídas as parcelas do sócio via processo. Para detalhes sobre a exclusão dos lançamentos de sócio, verificar a documentação abaixo.

No [**fechamento de condomínio individualizado**](https://tdn.totvs.com/pages/viewpage.action?pageId=857578505) os valores de integração serão distribuídos respeitando a seguinte ordem fixa de abatimentos:

1. Orçamento
2. Cobrança Direta
3. Despesa Financeira
4. Reserva
5. Consumo

Caso na cobrança do Orçamento não seja possível distribuir todo o valor do a ser pago pelo Sócio, a diferença passa para o próximo item da ordem acima.

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

Faturamento da bilheteria: **R$ 250.000,00**

Porcentagem de faturamento da bilheteria: **8%**

8% de R$ 250.000,00 = R$ 20.000,00

Faturamento do bomboniere: **R$ 78.000,00**

Porcentagem de faturamento do bomboniere: **15%**

15% de R$ 78.000,00 = R$ 11.700,00

Total de faturamento: R$ 20.000,00 + R$ 11.700,00 = **R$ 31.700,00**

Valor do condomínio: **R$ 3.500,00**

Valor do fundo promocional: **R$ 750,00**

Valor do aluguel: **R$ 15.000,00**

Valor do aluguel complementar = Valor do faturamento - (condomínio + fundo promocional + aluguel mensal)

Valor do aluguel complementar = R$ 31.700,00 - (R$ 3.500,00 + R$ 750,00 + R$ 15.000,00)

Valor do aluguel complementar = R$ 12.450,00

Portanto o sistema irá gerar um aluguel complementar no valor de **R$ 12.450,00**.

#FF9000CONSIDERAR DOBRO APENAS PARA CTO

Este recurso, disponível *a partir da versão 12.1.2306*, oferece uma nova opção para otimizar o processo de geração do aluguel complementar. Durante a execução do processo, é possível selecionar a opção "Considerar dobro apenas para CTO" na configuração do aluguel em dobro para o mês de competência.

Para aplicar esta melhoria no processo, siga os seguintes passos:

Ao acessar o contrato certifique-se de que no menu do aluguel complementar o valor do CTO mensal está informado;

No menu de Aluguel em Dobro, selecione a opção 'Considerar dobro apenas para CTO'. No exemplo abaixo, observe que a competência informada foi o mês de setembro;

Uma observação a respeito desta tela diz **respeito ao campo Percentual**. Ao informar um valor neste campo, **este percentual *(em destaque na imágem)* não é considerado no cálculo do valor do CTO**, mas sim no cálculo do valor da parcela do contrato de locação.

Além disso, ao marcar esta opção não será gerado o valor em dobro para aluguel, este cenário aplica-se aos contratos que além do CTO mensal, possuem em sua configuração um valor de contrato maior que zero.

Após realizar a geração do aluguel complementar, acesse o evento financeiro correspondente e edite a parcela referente à competência do mês 09 (que utilizamos em nosso teste). No print abaixo, é possível observar que a memória de cálculo demonstra a informação de que o valor do CTO está dobrado para a competência informada no momento da inclusão do aluguel em dobro.

**Observações:**

* Caso exista um escalonamento para a mesma competência do faturamento, então será considerado o valor do escalonamento, e não o valor do aluguel.
* Com a execução da geração dos valores de Aluguel Complementar, serão criados automaticamente os registros de Eventos Financeiros com o tipo de Locação Complementar.
* Em caso de necessidade de cancelamento do lançamento do aluguel complementar e a sua regeração com novos dados, o usuário deverá ir no controle do faturamento, alterar qualquer campo editável na tela conforme desejado e salvar. O sistema irá solicitar uma confirmação de regeração do lançamento. Após a confirmação, o lançamento antigo será cancelado e excluído e o novo lançamento será criado e vinculado à medição. Este procedimento não é possível de ser realizado quando o lançamento estiver baixado.
* Ao incluir um faturamento de aluguel complementar, o registro fica com o status de 'Pendente', porém ao gerar os lançamentos do aluguel complementar, quando o faturamento não atingir o percentual necessário para incluir o lançamento complementar, a medição terá o status da medição alterado para 'Sem valor complementar'
* Ao gerar um aluguel complementar com o parâmetro **Considera condomínio** marcado porém sem valores de condomínio relacionados para o período do faturamento, o processo ira concluir com a mensagem de alerta, informando que não existe condomínio para a competência correspondente.
* **A partir da versão 12.1.2302**, ao realizar as parametrizações do aluguel complementar para um contrato de locação, se a opção **"Considera valor contrato"** estiver desmarcada, o cálculo para a geração do aluguel complementar não considerará o valor do contrato ao calcular o faturamento.  
  Além disso, é importante destacar que, quando a opção **"Considera valor contrato"** estiver desmarcada, e existir um **CTO** (Custo Total de operação) com o contrato zerado ou que possua um escalonamento que zere o valor do contrato, o valor da parcela do aluguel também será zerado.
* **Variáveis pré definidas (Histórico do lançamento)** Quando selecionadas estas possibilitará listar informações no Histórico dos Lançamentos  
  financeiros gerados no sistema, cada variável possui sua respectiva função:

  |  |  |
  | --- | --- |
  | **[CADM]** | Código do Contrato de Administração; |
  | **[CALG]** | Código do contrato de Locação; ***(Obs: Na confissão de dívida só será preenchido quando a confissão for gerada por contrato)*** |
  | **[IMOV]** | Código do Imóvel; ***(Obs: Na confissão de dívida só será preenchido quando a confissão for gerada por contrato)*** |
  | **[NUMLOC]** | Número do contrato de locação |
  | **[IPER]** | Início do Período |
  | **[FPER]** | Fim do Período |
  | **[ICOMP]** | Inicio da Competência |
  | **[FCOMP]** | Fim da Competência |
  | **[DIMO]** | Descrição do Imóvel |
  | **[COBR]** | Ítem de Cobrança |

Para obter maiores informações sobre Aluguel Complementar

Tópicos relacionados:

---
