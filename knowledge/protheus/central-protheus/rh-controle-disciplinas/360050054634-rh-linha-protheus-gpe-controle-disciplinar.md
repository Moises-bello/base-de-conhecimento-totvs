---
article_id: 360050054634
category: RH - Controle Disciplinas
content_hash: 3b1c5a3a34eaafbafc2b170126948cf803df811d8095e707301a7cc1729a4fa1
fetched_at: '2026-06-28T22:43:10.242836+00:00'
product: protheus
section_id: 360012003633
source: central-protheus
title: RH - Linha Protheus - GPE - Controle Disciplinar
type: support-article
updated_at: '2026-06-25T13:04:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050054634-RH-Linha-Protheus-GPE-Controle-Disciplinar
---

**Dúvida**  
Como realizar o cadastro de **controle disciplinar?** Como **cadastrar advertências?**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**

* **Tipos de Disciplinas**

**Atualizações > Controle Disciplinar > Tipos de Disciplina - GPEA641**  
  
Os tipos de disciplina podem ser classificados como **Punição ou Mérito** e para cada um é necessário descrever o motivo pelo qual os funcionários receberão Méritos ou Punições, como no exemplo da imagem abaixo. As informações serão utilizadas no momento da aplicação disciplinar. ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077264993)

Os campos deste cadastro - **Tabela TIS** são:  
  
. **Tipo (TIS\_TIPO):** selecione entre **1-Punição ou 2-Mérito.** Se deixado em branco, é emitida uma mensagem de alerta "Preencher com o Tipo de Disciplina. 1=Punição ou 2=Disciplina". Campo obrigatório.

. **Código (TIS\_CODIGO):** campo gerado automaticamente pelo sistema. Não pode ser alterado.

. **Descrição (TIS\_DESCRI):** descreva um motivo pelo qual os funcionários receberão Méritos ou Punições. Campo obrigatório.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077266653)

Exemplo:

**Tipo**: Punição  
**Código**: 000001  
**Descrição**: Abandono de posto durante o expediente.

Para alterar, excluir ou copiar um registro, posicione o cursor sobre um registro do browse na tela inicial e clique em Alterar, Outras Ações > Excluir ou Outras Ações > Copiar, respectivamente.

* **Disciplina**

**Atualizações > Controle Disciplinar > Disciplina - GPEA645**  
  
A disciplina não é apenas um processo de punição (advertência ou suspensão), ela engloba também pontuações periódicas oferecidas como méritos a todos os funcionários da corporação.

Por exemplo, no início do ano de 2014, a empresa atribui 100 pontos para todos os funcionários. Porém, um determinado funcionário durante este mesmo ano recebeu uma advertência que tem peso 10 pontos e duas faltas injustificadas que tem peso 5 pontos (parametrizados também pelas condições internas de cada empresa), contudo, este funcionário passará a ter uma pontuação negativa de 20 pontos que deve ser abatida dos 100 pontos iniciais que recebeu no início do ano.

Cada funcionário deverá ter seu próprio histórico o qual deve apresentar os números de sua pontuação, constando as punições e os méritos que conquistou.

O histórico deve apresentar a vida profissional durante sua permanência na empresa, com pontos positivos e negativos, contendo a descrição do ocorrido com a data e horário do fato, bem como, o posto em que o funcionário estava alocado durante o evento. Os dados de quem aplicou a punição também é muito importante neste histórico. 

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076128814)

A tela é dividida em duas partes: a parte de cima onde se informa os dados da disciplina e a parte de baixo onde pode (opcional) ser feito o cadastramento da regra,  definindo a quantidade de punições que o funcionário pode receber e qual será a próxima punição sugerida a aplicar, conforme a parametrização.  
  
- Os campos da parte de cima, **tabela TIQ** são:   
  
**. Tipo** (TIQ\_TIPO): selecione entre 1-Punição ou 2-Mérito. Se deixado em branco, é emitida uma mensagem de alerta "Preencher com o Tipo de Disciplina".Campo obrigatório.

. **Código** (TIQ\_CODIGO): campo gerado automaticamente pelo sistema. Não pode ser alterado.

. **Descrição** (TIQ\_DESCR): informe o motivo da punição ou mérito. Campo obrigatório.

. **Cabeçalho** (TIQ\_TEXTO1): preencher com o texto do cabeçalho para disciplina. Este Texto será incorporado na impressão da disciplina e estará disposto abaixo das informações do funcionário que receberá a disciplina. Campo não é obrigatório.

. **Complemento** (TIQ­\_TEXTO2): preencher com o texto complemento da disciplina. Este Texto será incorporado na impressão da disciplina e estará disposto abaixo do campo cabeçalho. Campo não é obrigatório.

 - Os campos da parte de baixo, **tabela TIR** são:  
  
 . **Código** (TIR\_CODIGO):  campo gerado automaticamente pelo sistema. Não pode ser alterado.

. **Quantidade** (TIR\_QTD): quantidade de disciplina do mesmo tipo a serem aplicadas. Campo obrigatório.

. **Sugere** (TIR\_SUGERI): preencha com 1=Sim ou 2=Não se será sugerida a aplicação para próxima disciplina.

. **Disciplina** (TIR\_SUGEST): preencher com a Disciplina que deve ser sugerida para nova aplicação, levando em consideração a quantidade da mesma disciplina que já foi aplicada. Consulta padrão na tabela TIQ-Tipo de Disciplina. Campo obrigatório.

. **% Perda** PLR (TIR\_PPERDA): preencha com percentual que o funcionário irá perder em PLR. Aceita números positivos ou negativos. Esse campo não será exibido se a rotina for acessado pelo módulo SIGAGPE e o parâmetro MV\_TECXRH for .F..

Observação:  o parâmetro MV\_TECXRH  define se o Gestão de Serviços está integrado com o RH do Microsiga Protheus e seus valores podem ser .T. quando houver a integração e .F. quando não existir a integração.

. **Pontuação** (TIR\_PONTO): preencher com pontuação que deverá receber ao receber a disciplina. Aceita números positivos ou negativos. Campo obrigatório.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076129174)

Exemplo:

**Tipo**: Punição  
**Código**: 000001  
**Descrição**: Advertência Verbal.

**Cabeçalho**:

A responsabilidade profissional é requisito básico para o desempenho de toda e qualquer função. Porém, este não tem sido o seu procedimento, muito embora tenha sido sistematicamente orientado quanto a esta necessidade, pois, deixou de cumprir seu dever quando:

**Complemento**:

Portanto, considerando-se todo o acima exposto, estamos ADVERTINDO-O que, em caso de reincidência ou mesmo outro ato de indisciplina ou insubordinação, seremos compelidos a aplicar-lhe punição disciplinar com rigor que no faculta a legislação pertinente.

Ou

Portanto, considerando-se todo o acima exposto, estamos aplicando-lhe punição disciplinar, com a sua SUSPENSÃO do trabalho, por dias a contar desta data, devendo o senhor retornar ao trabalho no dia seguinte imediato ao do cumprimento desta presente punição, apresentando-se em seu horário normal de jornada, no posto de serviços. Salientamos que, em caso de reincidência, seremos compelidos a aplicar-lhe punição severa, dentro do que nos é permitido pela legislação vigente.

**Observação:**Antes de criar as regras do grid, cadastre antecipadamente todos os tipos de disciplina (advertência Verbal, Advertência Formal, Suspensão, Suspensão 3 dias, Demissão etc.)., e depois pode ser efetuada uma alteração incluindo a regra utilizando essas disciplinas cadastradas anteriormente.

Para alterar, excluir ou copiar um registro, posicione o cursor sobre um registro do browse na tela inicial e clique em Alterar, Outras Ações > Excluir ou Outras Ações > Copiar, respectivamente.

* **Pontuação**

**Atualizações > Controle Disciplinar > Pontuação - GPEA642**  
  
Permite a aplicação de pontos para os funcionários, a partir da data de admissão.

Não há restrições sobre a quantidade de pontos que cada um pode receber e nem sobre o período que será contemplado. Os parâmetros devem ser definidos conforme as regras internas da empresa.

Ao acessar a rotina é exibido um browse com os registros cadastrados. As opções são: Incluir, Alterar, Imprimir browse e Outras Ações, que por sua vez, possui os itens Excluir, Imprimir e Copiar.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076133014)

Os campos apresentados, tabela **TIV** são:  
  
. **Código**(TIV\_CODIGO): campo gerado automaticamente pelo sistema. Não pode ser alterado.  
. **Disciplina**(TIV\_CODTIQ): informe o código da disciplina a ser aplicada, conforme a tabela TIQ-Tipos de Disciplina. Campo obrigatório.  
. **Motivo**(TIV\_CODTIS): informe o código do motivo da disciplina, conforme a tabela TIS-Motivos para Disciplina. Campo obrigatório.  
. **Descrição**(TIV\_DESCRI): preencha com uma descrição para o tipo da pontuação. Campo obrigatório.  
. **Qtd.Pontos**(TIV\_PONTOS): preencha com os pontos que serão atribuídos aos funcionários. Campo obrigatório.  
. **Admissão Até**(TIV\_ADMITI): preencha com a data de admissão. Somente receberão os pontos os funcionários admitidos anteriormente a data informada.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077274173)

Exemplo:

**Código:**000001  
**Disciplina:**000001  
**Motivo:**000001  
**Descrição:**Pontuação periódica 2014  
**Qtd.Pontos:**100  
**Admissão Até:**28/02/2015  
  
Para alterar, excluir ou copiar um registro, posicione o cursor sobre um registro do browse na tela inicial e clique em Alterar, Outras Ações > Excluir ou Outras Ações > Copiar, respectivamente.  
  
**Atualizações > Controle Disciplinar > Gestão Disciplinar - GPEA643**

Permite a aplicação de Disciplinas para os funcionários. Ao acessar a rotina é exibido um browse com os registros cadastrados. As opções são: Incluir, Alterar, Visualizar e Outras Ações, que por sua vez, possui os itens Excluir, Imprimir , Copiar e Imprimir Browse.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409203012631)  
  
Ao incluir, deve informar os campos obrigatórios conforme destacados na imagem abaixo e confirme  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409203102359)

Exemplo:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409203122071)  
  
OBS: Caso a Disciplina gere afastamento, altere o campo **Afastamento para Sim**, onde consequentemente o Sistema habilita os campos **Tipo Ausência e Dias Afast para preenchimento**  
  
Para alterar, excluir ou copiar um registro, posicione o cursor sobre um registro do browse na tela inicial e clique em Alterar, Outras Ações > Excluir ou Outras Ações > Copiar, respectivamente.  
  
**Saiba Mais**  
[Documentação Técnica](https://tdn.totvs.com/pages/viewpage.action?pageId=255755761)  
[RH - Linha Protheus - GPE - O que verificar quando não imprime a disciplina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403482246295-RH-Linha-Protheus-GPE-O-que-verificar-quando-n%C3%A3o-imprime-a-disciplina?source=search)  
[RH - Linha Protheus - GPE - Alteração do HTML do Controle Disciplinar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051018014-RH-Linha-Protheus-GPE-Altera%C3%A7%C3%A3o-do-HTML-do-Controle-Disciplinar?source=search)  
[RH - Linha Protheus - GPE - Controle Disciplinar - Como imprimir formulário de Disciplina aplicada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409207341719-RH-Linha-Protheus-GPE-Controle-Disciplinar-Como-imprimir-formul%C3%A1rio-de-Disciplina-aplicada?source=search)
