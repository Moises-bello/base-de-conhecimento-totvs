---
content_hash: 7d935fb72b7f0af6a932cbce14e725b949d7bc9e16c0dd4bbfa426257c57e84b
fetched_at: '2026-06-29T00:10:02.485297+00:00'
page_id: '452718921'
product: rm
source: tdn-rm
title: Rescisão Complementar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718921
version: 15
---

Se os direitos do funcionário na demissão não foram totalmente pagos, seja por falta de dados, exemplo Hora Extra ou Comissão, por alteração salarial por convenção coletiva ou outro motivo, a rescisão complementar será devida.  
  
A rescisão complementar é a diferença devida ao ex-funcionário de um ou mais direitos trabalhistas.  
  
Particularmente o módulo de Rescisão Complementar do TOTVS Folha de Pagamento calcula as verbas quando:  
1.     Houve aumento salarial após a data de demissão e até o término do Aviso Prévio, diferença de:  
Aviso Prévio + fórmulas adicionais de aviso prévio;   
Férias (vencidas, proporcionais, 1/3 de Férias, médias, fórmulas e eventos adicionais de férias);  
13º Salário (rescisão, indenizado, fórmulas adicionais e eventos adicionais de 13º salário)  
Códigos fixos da rescisão.  
  
**Observação:**  
Para o cálculo das diferenças, são verificados os eventos de rescisão com os códigos de cálculos abaixo mais os eventos de médias do Sindicato e os eventos adicionais (Férias, 13º Salário e Aviso Prévio):   
048 – 13º Salário  
071 – 13º Salário indenizado  
063 – 1/3 de Férias Rescisão  
024 – Férias Indenizadas  
025 – Férias Proporcionais  
062 – Avisos Prévios  
  
2.     Houve aumento salarial até a data de demissão e a rescisão já tenha sido calculada, paga as diferenças de todos os eventos de rescisão.  
  
3.     Houve aumento salarial retroativo após a data do termino do aviso prévio e a rescisão já tenha sido calculada/paga, deve pagar diferenças.  
  
4.     Quando alterar o tipo da demissão, mesmo que não tenha ocorrido aumento salarial.  
  
Quando o parâmetro 'Calcula somente eventos informados' está marcado, mesmo que o funcionário tenha alteração salarial, o sistema não paga nenhuma diferença desta alteração apenas calcula eventos informados.  
O parâmetro 'Pagamento de verbas de natureza salarial ou não salarial devidas após o desligamento' será utilizado para o eSocial e ficará habilitado somente se o 'Calcula somente eventos informados' estiver marcado. Servirá para informar valores devidos de pagamentos a funcionários após seu desligamento. Quando o parâmetro estiver marcado deverá ser preenchido os dados do dissídio/convenção/acordo coletivo, sendo que o Tipo do acordo deve ser F - Outras verbas de natureza salarial ou não salarial devidas após o desligamento.

O parâmetro 'Pagamento de dissídio na competência do desligamento após o envio do S-2299' será utilizado para o eSocial, este parâmetro deve ser marcado somente quando o pagamento do dissídio for realizado na mesma competência da demissão do funcionário e após ter enviado o evento S-2299 para o governo. Marcando este parâmetro, as informações do dissídio serão levadas no evento S-1200. Se fizer o lançamento do dissídio sem marcar este parâmetro, caso o pagamento do dissídio seja na mesma competência da demissão do funcionário, será necessário fazer uma retificação do evento S-2299 para contemplar as informações do dissídio.

Quando for digitado algum evento em 'Eventos a serem somados a todas rescisões complementares', verifica se as médias foram alteradas devido ao lançamento do evento, caso este evento deva ser considerado nas médias.  
  
Caso o valor do evento inserido em 'Eventos a serem somados a todas rescisões complementares' seja alterado e não possa ser recalculado existe a possibilidade de marcar que deve ter o valor forçado no envelope de rescisão complementar.  
  
Para que as bases de cálculo (salário família, vale transporte, etc) sejam calculadas corretamente, sempre que processar uma diferença com o intuito de substituir a diferença já existente no envelope, é recomendado que cancele os eventos de diferenças antes de processar novamente.  
  
**Exemplo:**  
Foi calculada rescisão complementar para o funcionário lançando o evento de comissão no valor de R$700,00, e este evento incide salário família e o funcionário recebeu o salário família devido por estar dentro da faixa.   
Porém o usuário verificou que o valor correto da comissão é de R$70,00, caso o usuário não cancele a rescisão complementar, ao processá-la novamente informando o valor de R$70,00, o sistema considera a base de salário família R$770,00, porque o valor de 700,00 ainda está gravado no banco. Para ficar correto o usuário deve recalcular a rescisão complementar ou cancelar antes de lançar o valor correto.  
  
  
Os eventos de diferenças não podem incidir em Vale Transporte, Salário Família, devido no próprio recálculo o sistema já considerar o salário novo para as bases de cálculo.  
  
A integridade dos valores da rescisão é mantida através do módulo Lançamento do Líquido de Rescisão que tem o objetivo de proporcionar maior automação e agilidade do cálculo, considerando que não é mais necessária a utilização de fórmulas, fazendo com que o envelope não seja recalculado. Esse recurso também abrange a Rescisão Complementar.  
  
Quando houver diferença de pensão alimentícia, estes valores serão gravados no movimento de pensão (Funcionários | Folha de Pagamento | Dependente | Anexo Movimentação da Pensão de Dependente) com os tipos: '7-Férias Rescisão' e/ou '8-Dif. Férias Rescisão'.

Dica:

Veja também informação importante no cálculo de diferença quando envolve Pensão Alimentícia nos respectivos códigos de cálculo de pensão alimentícia como por exemplo: 

**Período da Rescisão**  
A data final não poderá ser superior ao último dia da competência corrente.  
  
  
**Data do Último Movimento**  
Quando o parâmetro "Altera data para:" está marcado o sistema ajusta a data de último movimento do cadastro de rescisão para a data informada neste campo.  
Caso contrário, o sistema ajusta com a data dos Parâmetros Locais.  
  
**Observação:**  
Além do campo "Data do Último Movimento" do cadastro de rescisão do funcionário ser ajustada, as datas de pagamento dos eventos da rescisão complementar também terão esta data.  
  
**Atenção:**  
Para filtrar os funcionários a serem processados, o sistema faz a seguinte verificação:  
Caso o parâmetro "Alterar data para:", estiver MARCADO o sistema retornar os funcionários que tem data de demissão dentro do período informado no campo "Período da Rescisão".  
  
Caso o parâmetro "Alterar data para:", estiver DESMARCADO o sistema além de verificar o campo "Período da Rescisão", verifica se no cadastro da rescisão do funcionário (Funcionários | Movimento | Rescisão) o campo "Data do Último Movimento" é igual ou superior ao mês e ano do caixa atual.

**Recalcula FGTS com base nos eventos de diferença**

Com esse parâmetro marcado o sistema irá realizar o cálculo do FGTS com base nos eventos de diferença, caso contrário, irá considerar o valor original.

Veja em: **[Recalcula FGTS com base nos eventos de diferença](https://tdn.totvs.com.br/pages/viewpage.action?pageId=520677554)**

**Calcular todas as diferenças juntas**

Quando a alteração salarial é referente a um mês anterior, ou a meses anteriores à rescisão, o usuário deverá calcular além da rescisão complementar, as diferenças de salário, férias e/ou 13º salário que existirem nesse intervalo entre a data do aumento retroativo e a data de desligamento do funcionário.

Ao marcar esse parâmetro haverá mais um passo para informar quais diferenças serão calculadas junto com a rescisão complementar, de acordo com a seleção do usuário.

Primeiro deve ser selecionado o mês que as diferenças deverão iniciar o cálculo.

Logo depois deverá ser selecionado o cálculo que será realizado:

* Diferença Salarial
* Diferença de férias – Se a 1ª parcela do 13º salário foi paga junto com as férias, será necessário informar um evento com código de cálculo '9-1ª Parcela de 13º Salário' para que a diferença da 1ª parcela seja lançada.
* Diferença de 13º salário - Se a diferença for paga no mês de Janeiro será habilitado o combo apresentando os eventos com CC (66) com incidência em INSS folha para o cálculo da diferença.

Não marcando esse parâmetro deverá calcular cada uma das diferenças pelos seus respectivos módulos, ou seja, diferença salarial, diferença de férias e diferença de 13º salário, em períodos diferentes do período da rescisão complementar para evitar conflitos entre os valores de determinados códigos de cálculo. Por exemplo: diferença de pensão alimentícia e INSS.

**Retificar rescisão**  
Para retificar uma rescisão no e-Social deve ser marcado o parâmetro "Retificar rescisão", escolher o período de lançamento que será gravado a rescisão complementar no mês competência da rescisão. Este período será por default o período selecionado no parametrizador anteriormente e poderá ser selecionado pelo usuário o período a partir deste default. Os eventos informados devem ser aqueles que se quer retificar, ou seja, caso haja um aumento de salário que não seja por dissidio ou não seja algum caso tratado pelo e-Social e afeta todos os eventos de pagamento da rescisão.  
  
O parâmetro "Período sequencial" deverá ser utilizado quando tem várias retificações em períodos diferentes. Marcando este parâmetro o sistema busca o maior período existente com retificação calculada e lança no período posterior.  
  
**Observações:**

* A "Data de Último Movimento" e o parâmetro "Pagamento de verbas de natureza salarial ou não salarial devidas após o desligamento" ficarão desabilitados quando o parâmetro "Retificar rescisão" estiver marcado.
* A diferença entre outras verbas de natureza salarial ou não salarial devidas após o desligamento e a retificação da rescisão é que na primeira o evento será devido por exemplo na apuração de hora extra ou comissão após a rescisão e no segundo foi alguma verba paga incorretamente e deve ser retificada.
* Não será possível recálculo da retificação, caso seja necessário deve cancelar através do cancelamento de folha e depois lançar novamente.
* O calculo de INSS será feito conforme tabela da época e será enviado nos eventos  S-1200 e S-1210 de retificação.
* O calculo de IRRF será feito na competência atual (onde o calculo da rescisão complementar está sendo realizado), deverá ser enviado os eventos S-1200 e S-1210 do período para o eSocial.
* Quando este parâmetro "**Não Lançar Liquido de Retificação no Envelope da Competência Atual**" estiver marcado o sistema passa a lançar os valores com a data de pagamento atual no período da retificação, dessa forma não é informado nenhum valor no período atual.
* Quando ocorrer uma rescisão por dissidio sim e uma retificação de rescisão no mês competência, deverá ser lançado o calculo em períodos diferentes.
* Quando calcula a retificação da rescisão somente informa na PFVERBASDIS os eventos que teve algum valor de diferença lançado no envelope.
* Caso existam duas retificações com cálculo de média, por exemplo a primeira retificação foi paga em Março e a outra em Abril e a primeira retificação existe antes do preenchimento automático da tabela PFVERBASDIS, será necessário recalcular a primeira retificação e depois a segunda retificação porque na primeira tem que ser preenchida a PFVERBASDIS para abater no cálculo das médias da segunda retificação. Ou então deve ser feito o preenchimento manual.
