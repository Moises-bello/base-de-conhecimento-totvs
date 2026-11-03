---
content_hash: 4d3b4c11947f6e1e67e70965649484467a50beb404b917308c7ef786c047409f
fetched_at: '2026-06-29T00:10:03.972620+00:00'
page_id: '452719181'
product: rm
source: tdn-rm
title: Informações para o cálculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719181
version: 8
---

As informações para o cálculo da folha de pagamento é muito importante para o departamento pessoal, porque são dados que serão transformados mensalmente em valores para o empregado.  
   
**Situação**  
Preencher dados referentes a posição atual do funcionário, tais como: Situação, Aposentadoria, Tipo de Aposentadoria e dados referente à Estabilidade.  
   
**Atenção:**  
1. Quando houver integração com o Gestão de Pessoas, o funcionário poderá ser afastado pelo Gestão de Pessoas e automaticamente será preenchido o campo 'Situação' e os históricos de Situação e Afastamento no Folha de Pagamento.  
   
2. Quando no 'Histórico de Afastamento' o campo 'Data Final' estiver preenchido, ao liberar a competência do mês do retorno do afastamento o sistema irá atualizar automaticamente a 'Situação' para 'A-Ativo', assim como incluir o 'Histórico de Situação'.  
   
3. **"Tipo de regime previdenciário"** este campo é utilizado para o eSocial leiautes  S-2200 - Admissão /Ingresso de Trabalhador e  S2209 - Desligamento .  
   
   
4. Quando a situação do Funcionário for 'D' - Demitido e o tipo de demissão for  5 - Transferência sem ônus p/ Cedente, é habilitado o campo 'Motivo da Transferência' com o mesmo motivo informado no processo de transferência através do processo de rescisão, podendo ser 'Sucessão, incorporação, cisão ou fusão', 'Empresa do mesmo grupo econômico' ou 'Estabelecimentos da própria empresa'.  
   
**Observações:**  
1. Se o parâmetro 'Aposentadoria' será utilizado no SEFIP quando o funcionário tiver a movimentação por aposentadoria  
   
2. O sistema irá conciliar os códigos de aposentadoria do sistema com os códigos oficiais da RAIS, sendo:  
**Código Oficial da RAIS                                                                     Códigos do Sistema**  
71-Aposentadoria por tempo de contribuição, sem rescisão contratual      1-Aposentadoria por Tempo de Serviço  
78-Aposentadoria por idade, sem rescisão contratual                              2-Aposentadoria por Idade                            
80-Aposentadoria especial, sem rescisão contratual                                3-Aposentadoria Especial                              
   
   
3. Quando o funcionário aposentar por tempo de serviço com rescisão, ou seja, não terá mais vínculo empregatício, o usuário não deverá marcar o parâmetro 'Aposentadoria', deverá cadastrar/calcular a rescisão para este funcionário.  
Caso a aposentadoria seja por tempo de serviço porém sem rescisão, deverá preencher este parâmetro e os dados da   
aposentadoria para correta informação no SEFIP.  
   
4. Para Aposentadoria por Invalidez deverá alterar a situação do funcionário para 'I–Aposentadoria por Invalidez' e não  deverá marcar o parâmetro 'Aposentadoria'.  
   
5. Quando houver integração com o Gestão de Pessoas será disponibilizada a visualização das informações das estabilidades   provisória, por exemplo, estabilidade por ser Membro da CIPA, por afastamentos por Licença Maternidade, Acidente de Trabalho, Doença Ocupacional, Serviço Militar, Mandato Sindical, além da estabilidade controlada por fórmula.  
   
Quando houver afastamento por Acidente de trabalho, Doença Ocupacional, Mandato sindical e Serviço Militar sem data de retorno o campo 'Referente Estabilidade' ficará em branco ou apresentará somente a mensagem da estabilidade que possuir data de término.  
**Exemplo:**  
Funcionário foi Membro da CIPA e ainda está dentro do período de estabilidade e tem um acidente de trabalho sem data de retorno. No histórico será apresentada somente a mensagem da estabilidade de Membro da CIPA até que a data de retorno do afastamento por acidente de trabalho seja informada.   
Para estabilidade por Acidente do Trabalho ou Doença Ocupacional que, por qualquer motivo, tenha a estabilidade estendida por mais de um ano, deverá ser controlada por fórmula e a mensagem da fórmula será apresentada juntamente com a mensagem da estabilidade prevista por lei.   
Para efeitos de histórico, quando a estabilidade do Membro da CIPA terminar ainda será visualizada a mensagem neste campo.  
   
   
**Códigos Fixos**   
São eventos que serão lançados mensalmente no envelope de pagamento do funcionário por um tempo determinado ou permanentes e que não é comum a todos funcionários. Exemplo, Pensão Alimentícia, Vantagem Pessoal, etc.  
   
   
**Eventos Programados**  
São eventos da folha que tem uma competência inicial e final para lançamento, semelhante aos códigos fixos do funcionário, porém este cadastro tem um campo para informar o centro de custo do evento programado e a competência inicial e final, e o evento poderá ser cadastrado mais de uma vez para o mesmo funcionário.  
   
   
**Empréstimos**  
Com estas informações poderão ser visualizados todos empréstimos do funcionário assim como os históricos dos descontos já realizados.   
**Atenção:**  
Após o lançamento dos empréstimos, o sistema irá registrar os valores descontados no anexo 'Descontos de Empréstimos'. Estes valores somente são atualizados no lançamento dos empréstimos, no recálculo não é atualizado.  
   
**Parâmetros**  
Nas informações dos Parâmetros define-se os dados relativos ao funcionário, tais como: Dados do INSS, Controle de Saldo de Verbas, Vale Transporte, visualização do número de Dependente de IRRF e Salário Família e etc.  
**Observações:**  
1. Com o parâmetro **INSS Não Calcula** marcado o sistema não irá calcular o desconto do INSS (Folha de Pagamento, Férias e 13º  salário), inclusive parte empresa na GPS, independente do tipo do funcionário e mesmo se na movimentação houver eventos que incidem no INSS, INSS Férias ou INSS 13º Salário.   
   
2. Com o parâmetro **IRRF Não Calcula** marcado o sistema não irá calcular o desconto do IRRF (Folha de Pagamento, Férias e 13º  salário), independente do tipo do funcionário e mesmo se na movimentação houver eventos que incidem no IRRF , IRRF Férias ou IRRF 13º Salário.   
   
3.Indicador de Contribuição Substituída: Este campo é utilizado para o eSocial leiautes  S-1200-Remuneração do Trabalhador , S-2299-Desligamento e S-2399-Trabalhador sem Vínculo de emprego/Estatutário.  
   
4. Com o parâmetro **Utiliza Controle de Saldo de Verbas** marcado o sistema irá armazena os descontos dos eventos lançados nas verbas do mês/período anterior que causaram insuficiência de saldo.  
**Exemplo I:**  
O funcionário está com débito de R$ 700,00 de farmácia conveniada à empresa, e possui total de proventos R$ 500,00, o sistema armazena o saldo relativo a diferença entre proventos e descontos(R$ 200,00) na tabela PFVERBAS.   
No caso do funcionário não possuir saldo para desconto da verba no mês atual, o desconto é efetuado no meses posteriores.   
**Atenção I:**  
A ordem de lançamento dos eventos de descontos que geraram saldo negativo é por ordem de prioridade do evento. Quando os eventos tem a mesma prioridade, a segunda ordem é o código do evento. Porém o INSS, IRRF e Pensão Alimentícia tem prioridade de desconto superior a qualquer ordem.  
   
**Atenção II:**  
Os descontos do período ou competência anterior somente serão lançados quando o parâmetro Lança eventos da integração com insuf. saldo do mês/período anterior estiver marcado. Porém para o envelope atual a cada recálculo, o sistema verifica se existe saldo para lançamento dos eventos de insuficiente de saldo do envelope atual.  
   
**Atenção III:**  
A cada recálculo o sistema verifica a necessidade de guarda os descontos na aba Verbas c/ Insuficiência de Saldo tabela PFVERBAS.  
   
**Atenção IV:**  
O código de cálculo 20-ARREDONDAMENTO PROVENTO somente é lançado quando o funcionário utiliza arredondamento no cadastro de funcionário.  
   
**Atenção V:**  
Quando o parâmetro Desconto Perdoado existente em Cadastros | Eventos | Aba Inc. Descontos estiver marcado este evento é gravado na tabela PFVERBAS com o campo DESCONTADO igual a 1, para não ser lançado no movimento.  
   
**Atenção VI:**  
No lançamento do Vale Transporte (código de cálculo 6) e Contribuição Sindical (código de cálculo 12) o sistema calcula o valor e abate o valor já descontado.  
   
**Atenção VII:**  
A insuficiência de saldo não verifica data de pagamento.   
**Exemplo:**   
O desconto de faltas foi lançada no movimento com data de pagamento 31/12/2010 (Período 1) e o funcionário foi demitido em 30/12/2010 (Período 2), mesmo as faltas tendo sido descontada com data posterior a rescisão, o sistema desconta as faltas na rescisão.  
O mesmo ocorre com o lançamento do movimento para o próximo mês. Se lançarmos faltas com insuficiência de saldo para o próximo mês e se no mês atual recalcularmos o envelope com saldo, o sistema desconta as faltas na competência atual.  
**Observação I:**  
Para visualizar o saldo de verbas é preciso selecionar em Cadastros | Funcionários | Ficha Financeira | aba Verbas com Insuficiência de Saldo.  
   
**Observação II:**  
Para lançar o débito do mês anterior, é necessário marcar o campo 'Lança Desconto com Insuficiência de Saldo do mês anterior' no módulo Movimento | Folha de Pagamento | Lançamentos Automáticos | Grupo de Eventos.

**Desconsiderar desconto simplificado do IRRF**

Ao marcar este parametro sistema passa a considerar o valor do desconto de IRRF pela tabela de IRRF vigente sem considerar IRRF Simplificado. Mais informações para o calculo [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=761006653).

**Prefixo Período (eSocial)**  
Utilize esta informação para que no momento da geração dos eventos S-1200 e S-1210 os eventos possam ser separados por funcionário que tem múltiplos vínculos e os mesmos têm lançamentos no mesmo período de pagamento. Este campo aceita até 10 caracteres.  
   
**Exemplo:**  
Funcionário Pessoa 1 chapa 00001 tem honorários como diretor lançado no envelope período 1  
Funcionário Pessoa 1 chapa 99991 tem salário como funcionário lançado no envelope período 1  
   
Como exemplo, nesse campo em cada funcionário foi informado a sua própria chapa.  
Após a geração do XML a Tag <ideDmDev> será apresentada da seguinte forma:  
   
Para o Diretor categoria 721  
<ideDmDev>100001<\ideDmDev>  
   
Para o Funcionário categoria 101  
<ideDmDev>199991<\ideDmDev>  
   
**Observações:**  
1.     A informação da Tag <ideDmDev>.será a união do período com a informação do campo no cadastro de funcionários. Caso o campo não seja preenchido somente o número do período será informado na Tag <ideDmDev>.  
2.     O campo pode ser preenchido com números ou letras.

**Não calcula Recibo de Férias**  
Ao ser marcado o parâmetro, o sistema não irá calcular o Recibo de férias para o funcionário.

**Observações:**

1. Ao ser marcado o parâmetro, o sistema não irá calcular o recibo de férias para o funcionário.

2. Não serão exibidos no cadastro de férias o campo '**Data Pagamento**' e os botões de '**Calcular**' e '**Visualizar Recibo**' de férias.

3. A mudança da situação do funcionário para 'Férias', continuará sendo feito pelo processo 'Lançar' férias'.

4. O processo 'Finalizar' férias vai mudar a situação do funcionário de 'Férias' para 'Ativo' e atualizar os dados cadastrais do período aquisitivo de férias.

5. O sistema não irá consistir na liberação de competência se constam no envelope do funcionário os códigos de cálculo específicos de férias para funcionários com o parâmetro marcado.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funcionários  
Empréstimos
