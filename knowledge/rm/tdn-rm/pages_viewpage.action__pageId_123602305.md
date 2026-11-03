---
content_hash: 58285c2d54f632b33ba6ef2fd99e730037cc9ceabcabf832cd3dd72e076048c8
fetched_at: '2026-06-29T00:05:55.073418+00:00'
page_id: '123602305'
product: rm
source: tdn-rm
title: RMCTB000011_SPED Contábil - Alterações do Layout 2.0
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=123602305
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | RM TOTVS Gestão Contábil 11.52/11.80 |
| **Processo** | : | SPED Contábil |
| **Subprocesso** | : | RM TOTVS Gestão Contábil |
| **Data da publicação** | : | 14/02/2014 |

Foram realizadas evoluções no produto da linha RM para contemplar as alterações necessárias para geração do arquivo do Sped Contábil no novo layout disponibilizado pela Receita Federal, que será utilizado na entrega das informações a partir do ano-calendário 2013. No novo layout (chamado pela RFB de layout 2.00) foram feitas várias alterações, como inclusão de novos campos em alguns registros já existentes e criação de novos registros.

**Procedimento para Implementação**

Para gerar o arquivo do Sped Contábil no layout 2.0 é necessário estar com o ambiente atualizado com os últimos patch especifico (11.52 /11.82). Nesta mesma versão o usuário poderá optar em gerar o arquivo no layout da versão 1.0 ou 2.0.

**Procedimentos para Utilização**

1. **1.** **O que mudou no Sped Contábil?**

A Receita Federal liberou a versão 3.x do PVA do Sped Contábil. O novo PVA prevê a importação de dois layouts (1.0 e 2.0).

Sendo que, a versão 1.0 é usada na entrega do ano-calendário 2012.

A versão 2.0 é nova, trata-se de um novo layout que será utilizado para as entregas do Sped Contábil a partir do ano-calendário 2013.

Além disso, o novo PVA permite a edição da escrituração.

1. **2.** **O que mudou no layout do Sped Contábil?**

Na tela de geração do SPED Contábil foi incluída uma opção para que seja informada a versão do layout (1.0 ou 2.0) em que o arquivo será gerado.

Se for escolhido layout 1.0 o arquivo será gerado no layout antigo, mesmo formato utilizado na entrega das informações do ano-calendário 2012.

Se for escolhido layout 2.0 será habilitada uma nova etapa com os novos campos que irão compor as informações do novo layout.

Abaixo detalhamento das alterações no layout 2.00 e tratamento no sistema:

**2.1** **Registro 0000 (ABERTURA DO ARQUIVO DIGITAL E IDENTIFICAÇÃO DO EMPRESÁRIO OU DA SOCIEDADE EMPRESÁRIA) – Inclusão dos campos:**

1. ***a.*** ***Indicador do início do período*** **(IND\_SIT\_INI\_PER)**

*0 - Normal (início no primeiro dia do ano)*

*1 - Abertura*

*2 - Resultante de cisão/fusão ou remanescente de cisão, ou realizou incorporação.*

*3 - Início de obrigatoriedade da entrega da ECD no curso do ano calendário.*

1. ***b.*** ***Indicador de finalidade da escrituração (*****IND\_FIN\_ESC)**

*0 - Original*

*1 - Substituta da escrituração com NIRE*

*2 - Substituta da escrituração sem NIRE*

*3 - Substituta da escrituração com troca de NIRE*

1. ***c.*** ***Indicador de empresa de grande porte (IND\_GRANDE\_PORTE)***

*0 - Empresa não é de grande porte*

*1 - Empresa de grande porte - Ativo Total superior a R$ 240.000.000,00 ou Receita Bruta Anual superior     R$300.000.000,00.*

1. ***d.*** ***Hash da escrituração substituída (*COD\_HASH\_SUB)**

*Deverá ser informado quando o IND\_FIN\_ESC for igual a 1, 2 ou 3*

1. ***e.*** ***. NIRE da escrituração que está sendo Substituída (*****NIRE\_SUBS)**

*Deverá ser informado quando o IND\_FIN\_ESC for igual a 3*

1. ***f.*** ***Indicador de existência de NIRE (*****IND\_NIRE)**

*0 - Escrituração não possui registro na junta comercial (não possui NIRE)*

*1 - Escrituração possui registro na junta comercial (possui NIRE)*

***Como foi tratado no sistema?***

Para os itens “a” até “e” foram incluídos campos na tela de geração do SPED Contábil para que sejam informados. Esses campos só ficarão habilitados quando for escolhido o layout 2.0 para geração do arquivo.

As opções escolhidas na tela serão geradas no arquivo no registro 0000.

O item “e” será gerado automaticamente no arquivo, obedecendo a seguinte regra: se o campo Nire do estabelecimento (tabela Estabelecimento Extensão) estiver preenchido será gerado 1 no arquivo e se não estiver preenchido será gerado 0 no arquivo.

**2.2** **Registro I030 (TERMO DE ABERTURA) – Inclusão do campo:**

**DT\_EX\_SOCIAL** *- Data de encerramento do exercício social;*

**NOME\_AUDITOR** - Nome do auditor independente;

**COD\_CVM\_AUDITOR** - Registro do auditor independente na CVM.

***Como foi*** ***tratado no sistema?***

Foram incluídos novos campos no cadastro da Escrituração Contábil (Aba Layout 2.0) para que sejam informados. Para empresas de grande porte (IND\_GRANDE\_PORTE =1) os campos “Nome Auditor” e “Registro do auditor” serão obrigatórios.

**2.3** **Alterações no campo “Situação Especial” – registro 0000:**

Além das opções já existentes no campo “Situação Especial” da tela de geração do arquivo, foi incluída a opção 5 (Transformação) que poderá ser utilizada nos dois layouts (1.0 e 2.0);

 Segundo o Guia, “O código 5 deve ser utilizado quando, por exemplo, a empresa passar de limitada (Ltda.) para sociedade anônima (S.A.).”.

Outra alteração é em relação à opção 0 – Abertura (também do campo Situação Especial) que não poderá mais ser utilizada no layout 2.0;

***Como foi tratado no sistema?***

1. Foi incluída a opção 5 – Transformação na lista de valores possíveis do campo Situação Especial na aba Parâmetros da tela de geração do arquivo. Quando selecionada essa opção, será gerado o valor correspondente (no caso, 5) no campo situação especial do registro 0000.

1. Na geração do arquivo, quando for layout 2.0 e o campo situação especial informado na tela de geração for igual a 0 (Abertura) o sistema apresentara uma mensagem de erro.

**2.4** **Registro I051 (PLANO DE CONTAS REFERENCIAL) – não existe mais referência ao plano de contas referencial da RFB, apenas Banco Central.**

O registro I051 (Plano de Contas Referencial) é gerado com base na relação (DE-PARA) entre as contas do plano de contas da empresa e um plano de contas padrão.

Esse plano de contas padrão pode ser o da Receita Federal (Entidade Responsável 10) ou do Banco Central do Brasil (Entidade Responsável 20).

Esse registro não é obrigatório, mesmo no layout 1.00.

Contudo, no layout 2.0, o plano de contas referencial da RFB (Entidade Responsável 10) não poderá mais ser informado no arquivo do Sped Contábil, sendo que o PVA apresentará erro. Apenas quem utiliza o plano de contas referencial do Banco Central (Cosif) poderá continuar informando o registro I051 no arquivo.

***Como foi tratado no sistema?***

Este campo já era disponibilizado no sistema sendo facultativo, o seu preenchimento e neste caso não haverá nenhuma alteração, o preenchimento deverá ser realizado apenas por empresas que utiliza o plano de contas referencial do Banco Central (Cosif).

**2.5** **Registro J100 (BALANÇO PATRIMONIAL) - Inclusão dos campos:**

**VL\_CTA\_INI** - Valor inicial do Código de aglutinação no Balanço Patrimonial

**IND\_DC\_BAL\_INI**- Indicador da situação do saldo inicial informado no campo anterior: D - Devedor; C – Credor.

***Como foi tratado no sistema?***

Durante a geração do arquivo o sistema realizara o calculo das informações automaticamente e preencherá o registro J100.

**2.6** **Registro J930 (IDENTIFICAÇÃO DOS SIGNATÁRIOS DA ESCRITURAÇÃO) - Inclusão dos campos:**

**FONE** - *Telefone do signatário*

**EMAIL** - *E-mail do signatário*

**UF\_CRC** - *Indicação da unidade da federação que expediu o CRC*

**NUM\_SEQ\_CRC** - *Número sequencial no seguinte formato: UF/ano/número*

**DT\_CRC** - *Data de validade do CRC do contador*

***Como foi tratado no sistema?***

Foi criada uma aba (Dados adicionais – Layout 2.0) no cadastro do Signatário disponível dentro do cadastro de Escrituração Contábil, para que sejam informados os novos campos que serão obrigatórios no layout 2.0 para o signatário contador/contabilista.

*Lembrando que, essas informações só são obrigatórias para o Signatário Contador/Contabilista. Ao gerar o arquivo no layout 2.00, as novas informações serão geradas no arquivo, no registro J930.*

**2.7** **Criação dos registros:**

Registro J200 – Tabela de Histórico de Fatos Contábeis que modifica a conta de lucros acumulados ou a conta de prejuízos acumulados ou todo o Patrimônio Liquido.

Registro J210 - DLPA – Demonstrações de lucros ou prejuízos acumulados / DMPL – Demonstração de mutações do Patrimônio.

Registro J215 – Fato Contábil que altera a conta de lucros acumulados ou a conta de prejuízos acumulados ou todo o patrimônio.

Os registros J200 e J210 estão no mesmo nível do registro J100 (Balanço Patrimonial) já existente.

O registro J215 é filho do registro J210.

Na estrutura fica assim:

J005

J100

J150

J200 (novo)

J210 (novo)

J215 (novo)

***Como foi tratado no sistema?***

1. Foi criada no módulo TOTVS Gestão Contábil uma ferramenta de criação de Demonstrações Contábeis, nesta ferramenta o usuário deverá criar a estrutura (Layout) que irão compor a DMPL ou DLPA.

Através das informações parametrizadas o sistema irá compor os registros J200, J210 e J215.

Para maiores informações consulte o help.

1. No processo de geração do arquivo do SPED Contábil para o layout 2.0 o sistema disponibilizara campos para que o usuário informe a estrutura da demonstração que foi criada e seu respectivo tipo (DMPL ou DLPA).

*Quando o campo Data de encerramento do exercício social do Registro I030 estiver preenchido e o campo IND\_ESC do Registro I010 for igual a “G”, “R” ou “B”, o registro é obrigatório, caso não seja informado será apresentado no validador como advertência.*

Para maiores informações:

[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE**[**R@Contábil**](https://totvs.byyou.com/?space=rcontabil)

**Canais** **de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:**4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 2 – (Controladoria e Finanças), 5 – (Planejamento e Controle Orçamentário), 2 – (RM Saldus).
