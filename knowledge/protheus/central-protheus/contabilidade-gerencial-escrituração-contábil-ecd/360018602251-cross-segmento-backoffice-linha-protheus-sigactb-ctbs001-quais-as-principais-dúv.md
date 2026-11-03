---
article_id: 360018602251
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 3eec447fd1581f664898fa2a50cdf6723f76766818048f646d76d5bb34579611
fetched_at: '2026-06-28T22:40:44.593866+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBS001 : Quais as
  principais dúvidas relacionadas a ECD?'
type: support-article
updated_at: '2021-12-03T15:04:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018602251-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Quais-as-principais-d%C3%BAvidas-relacionadas-a-ECD
---

* **Ao executar o compatibilizador U\_UPDCTB referente ao pacote do SPED ECD 2016 no protheus 11 é apresentado a data de 10/03/2015.  Estou com a ultima versão de update, posso realmente aplica-lo?**

Sim a nossa ultima liberação com as atualizações para o leiaute 4.0 tem essa data de atualização.

* **Recebi no pacote do ECD os arquivos leiaute\_moeda\_funcional.txt, moed\_func\_e\_raz\_aux\_subcta\_cfg\_mile.xml, raz\_aux\_subcta\_ctb.txt, devo utilizá-los? Como proceder com esses arquivos?**

Estes arquivos somente devem ser utilizados por empresas obrigadas a considerar o ECD com leiaute de MOEDA FUNCIONAL (leiaute\_moeda\_funcional.txt) ou  cliente que entregão o ECD com o Razão de sub contas auxiliar (raz\_aux\_subcta\_ctb.txt). Lembrando que no caso do razão de subconta auxiliar o mesmo é apenas um modelo disponibilizado pela TOTVS, podendo ser personalizado conforme necessidade do contribuinte.

Em ambos os casos, para utilização dos arquivos deve-se acessar o modulo SIGACFG (Modulo Configurador) seguindo os passos abaixo:

Ambiente-> Aceleradores-> Mile->Layouts(CFGA600).

Dentro da rotina deve seguir as opções:

Ações Relacionadas-> Layouts-> Importar à Procurar pelo arquivo “moed\_func\_e\_raz\_aux\_subcta\_cfg\_mile.xml” à Selecionar o mesmo e confirmar sua importação.

Após isso, acessar o módulo SIGACTB (Contabilidade Gerencial), via opção de menu:

Atualizações-> Escrituração Cont.-> Cadastros-> Layout Auxiliar(CTBS100).

Dentro desta rotina, deve ser seguir as opções: Ações Relacionadas-> Outros-> Importar.

Na tela que será apresentada, deve-se utilizar o campo “Arquivo” para selecionar o arquivo TXT “leiaute\_moeda\_funcional.txt” ou “raz\_aux\_subcta\_ctb.txt” e, após a escolha, clicar no botão “Importar”. Com isso, tem-se a estrutura do leiaute auxiliar cadastrado.

 

* **Ao aplicar o pacote da ECD disponível no portal do cliente, é apresentada a tela abaixo, nesse caso basta clicar na opção “Aceito somente Fontes Atualizados”.**  
  **O aviso e exibido quando o cliente possui em seu repositório uma rotina mais atual que a liberada no pacote (devido a atualização pontual) ou quando o cliente esta utilizando o RPO disponibilizado no portal do ultimo dia 30/03/16.**  
    
  ![](http://tdn.totvs.com/download/attachments/187531745/Tela.jpg?version=1&modificationDate=1459957307000&api=v2)

* **Campo “CS0\_LEIAUT não existe”**

Verifique se o programa **CTB.PRW** esta com data posterior a 22/10/2013, caso afirmativo, será necessário rodar o compatibilizador do**U\_UPDCTB** e atualizar os **XMLs**

* **Campo “COD\_ASSIN”| Código de qualificação do assinante não encontrado na tabela de qualificação do assinante.**

Verifique se no campo Cod. Qualif. está cadastrado corretamente. O contador precisará estar como 900 (exemplo).

* **Registro I010 não encontrado**

Verifique se o arquivo TXT, está sendo gerado para a versão correta do SPED contábil.

* **Registro M030 não é gerado**

Provavelmente o usuário está informando conta de 1 a 5 do plano de contas e mencionando como conta de apuração uma conta 6. Desta forma o registro **M030** não estava sendo gerado, pois conta de apuração (6) não estava presente no plano de contas.

O usuário deverá informar uma conta de apuração dentro do *range* do plano de contas, exemplo:

Plano de contas de 1 a 5;

Contas de Apuração: 2 (Lucros e Prejuízos), conta a qual foi utilizada para apuração de resultados (zerando as contas de receita e despesa), não utilizando a conta transitória.

* **Registro I150 - Total dos débitos diferente do total de créditos no período informado nos registros de Saldos Periódicos**

Verifique se os saldos das contas de receita e despesa foram zerados corretamente no momento da apuração de resultados.

* **Registro I150 – Registro encontrado é diferente do registro esperado ou o tipo de registro e desconhecido**

O erro ocorre porque não foram gerados os arquivos **I150**, **I155** que são obrigatórios para escriturações do tipo G, para isso é necessário efetuar as rotinas de processamento de saldos. Além disso, verificar se o foi criado um único calendário contábil onde o mesmo encontra-se com 12 períodos, (Um para cada Mês).  Caso ainda assim o problema persista, verifique se as tabelas CTs estão com o mesmo compartilhamento (Exclusivo ou compartilhada)

* **Registro I250  (Campo HIST) – Conteúdo do campo invalido**

Verifique se no histórico do lançamento na finalização do texto existe um espaço entre o fim do texto e o PIPE, necessário retirar esse espaço. Em seguida para manter a paridade das informações verifique se no lançamento contábil (CT2) esse registro possui espaço.

* Advertência I200 | Fato Contábil

A advertência **I200** é a soma das partidas do lançamento a crédito, caso tenha diferença do valor informado, no registro do Lançamento Contábil. Ela ocorre devido ao fato do validador interpretar as informações do lote contábil por operação/processo, que não era validado.

Para esclarecer maiores dúvidas, acesse [Advertência I200 | Fato contábil](http://tdn.totvs.com.br/pages/releaseview.action?pageId=145362299)

* **Mensagem “A conta referencial utilizada é sintética”**

Verifique a classificação da conta contábil e a respectiva amarração da conta no plano de contas referencial as contas so podem estar amarradas a contas analíticas.

* **"Layout não encontrado"**

O erro de layout não encontrado, ocorre em dois momentos:

Grave a pasta *system* com os seus arquivos, dentro desta pasta **Protheus Data**.

Na pasta *system***Protheus / Protheus Data**, os arquivos abaixo, precisarão constar. Caso não estejam, efetue o *download* no portal do cliente.

ECDLIVRO\_A.xml

ECDLIVRO\_B.xml

ECDLIVRO\_G.xml

ECDLIVRO\_R.xml

ECDLIVRO\_S.xml

ECDLIVRO\_Z.xml

Caso não exista os arquivos acima, efetue o *download* no Portal do Cliente:

Palavra: ECD

Categoria: TODAS

CTB - SPED Contábil

Arquivos modelos de configuração XML, para o SPED Contábil. (ecdlivroA.xml, ecdlivroB.xml, ecdlivroR.xml, ecdlivroG.xml, ecdlivroZ.xml)

* **Layout Não encontrado – Parte 2**

Mensagem também ocorre quando os arquivos ou configuração no INI não estão corretos.

Exemplo de configuração do INI:

RootPath=C:\Protheus\_10\Protheus\_Data\

StartPath=\system

Alterar para :

RootPath=C:\Protheus\_10\Protheus\_Data

StartPath=\system\

Veja que a barra “\” ao final é essencial para o Protheus encontrar os arquivos XML.

Importante: Efetuar o Backup antes da atualização.

* **Erro na função EXPORTAMOV(CTBS011.PRW)**

Verifique se houve a mudança no tamanho dos campos padrões da TOTVS. Outra medida é ativar o parâmetro **MV\_CTBSPRC** para **.T.** (True), para que o processo seja realizado através da procedure dinâmica.

* **DATA WIDTH ERROR – FIELD NIVEL VALUE: 10.000000 on CTBPLGEREN(CTBXFUN.PRX)**

O motivo de estouro refere-se a quantidade de subníveis da visão gerencial. O recomendado é utilizar até 9 subníveis, e estruturar a DRE e a BP de forma que não fique igual ao Plano de contas e sim à exibição dos relatórios

* **ARRAY OUT OF BOUNDS ON CT11POPCSL(CTBS011.PRW**

Existem campos que incorretos no ambiente, fazendo necessário execução do compatibilizador **U\_UPDCTB**.

* **REGISTRO J001 (não gera os registros J005, J100 e J150)**

Esse erro está relacionado a visão gerencial, será necessário revisá-la. Abaixo, disponibilizamos alguns *links*que auxiliarão na montagem da visão gerencial.

* [Visão Gerencial - Modos de exibição da Visão Gerencial -- 30178](http://tdn.totvs.com/pages/viewpage.action?pageId=6068447)
* [Visão Gerencial - Impressão de balanços em diversos tipos de saldo -- 24242](http://tdn.totvs.com/pages/viewpage.action?pageId=6068435)
* [Visão Gerencial - Expressões especiais -- 10909](http://tdn.totvs.com/pages/viewpage.action?pageId=6068417)
* [Visão Gerencial - Uso de fórmulas -- 11348](http://tdn.totvs.com/pages/viewpage.action?pageId=6068421)

Demonstrativo de resultados, acesse o link abaixo ou nosso help online, disponível no portal de clientes TOTVS.

* [Demonstração do Resultado do Exercício DRE -- 30098](http://tdn.totvs.com/pages/viewpage.action?pageId=6068466)

Balanço Patrimonial, acesse o link abaixo ou nosso help online, disponível no portal de clientes TOTVS.

* [Demonstração - Balanço Patrimonial BP](http://tdn.totvs.com.br/pages/releaseview.action?pageId=6068467)

Como sugestão, gere uma base teste com apenas alguns lançamentos de **DRE** e **BP** e verifique se os registros **J001**, **J005**, **J100** e **J150** são gerados corretamente.

Abaixo descrição dos registros

ABERTURA DO BLOCO J = J001

DEMONSTRAÇÕES CONTÁBEIS = J005

BALANÇO PATRIMONIAL = J100

DEMONSTRAÇÃO DO RESULTADO DO EXERCÍCIO = J150

* **Em que consiste o Registro - I053 (Subcontas Correlatas)?**

Este cadastro consiste em amarrar uma conta pai (analítica) do Plano de Contas da empresa, a uma ou mais subcontas correlatas (analítica), identificados por um ID único, e para as quais devem ser criados os códigos no Configurador (SX5), na tabela ST (Identificador de Subcontas Correlatas*),*de acordo com a necessidade levantada pelo contador de cada cliente.

Mais detalhes: [Cadastro de SubContas Correlatas](http://www.tdn.totvs.com/display/PROT/CTB0081_ECD_SUBCONTAS_CORRELATAS)

* **Podem explicar melhor, como funcionam as subcontas?**

Na data da adoção inicial das regras definidas pela Lei 12.973, deve se apurar a diferença entre os valores do Ativo e do Passivo na Contabilidade Societária e no FCont.

A diferença positiva ou negativa encontrada é adicionada ou excluída na apuração da Base de Cálculo do IRPJ e da CSLL.

* **Quem deve registrar as Subcontas Correlatas?**

A responsabilidade é das Pessoas Jurídicas que se enquadrem nas Leis 11.638/2007 e 11.941/2009, leis estas em que foi instituído o Regime Tributário de Transição (RTT).

A data da adoção inicial das regras da Lei 12.973 é:

– 1-1-2014, para as Pessoas Jurídicas optantes pela extinção do RTT, já no ano-calendário de 2014, observado o disposto no item 5 desta orientação; ou

– 1-1- 2015, para as Não Optantes.

E as empresas não obrigadas ao registro na Junta Comercial, registradas por meio de Atas em Cartório? Não possuem NIRE.

Na rotina CENTRAL DE ESCRITURAÇÃO (CTBS001), informe que não possui NIRE.

* **O plano de contas informado no boletim, refere-se apenas a Pessoa Jurídica normal, deveria haver referência a outros tipos?**

A TOTVS disponibilizou os modelos atuais dos planos referenciais liberados pela Receita Federal. A manutenção das contas referenciais tais como Data de Vigência é de responsabilidade do cliente.

* **Registro – I030 (Campo NIRE)**

Verifique no SIGAMAT, que o campo NIRE precisa ser preenchido

* **Registro - I050 (Campo COD\_NAT)**

Verifique a natureza das Contas Contábeis nos campos **Natureza da Conta** e **Natureza da Conta SPED**, no cadastro de Plano de Contas.

* **Registro – J210**

Informe uma das Demonstrações **DMPL** ou **DLPA** no assistente. É necessária a configuração de uma visão gerencial para obter essas informações.

* **Registro I030 – (DT\_ARQ)**

O campo pode estar com a data incorreta, exemplo de 01/01/2049.

* **Registro – 0150 (Campo COD\_PAIS)**

No Cadastro do Participante, preencha o código correto **01058**, ou seja, deve conter 5 números.

* **Registro - J100 (Balanço Patrimonial):**

Analise a estrutura da Visão Gerencial referente ao Balanço Patrimonial;

* **Preenchimento do campo CS6\_CODAGL**

 Verifique que o campo **CS6\_CODAGL** é preenchido com o cod da visão + cod da entidade da visão

* **Existe algum modelo das demonstrações DMPL?**

Sim, existe o arquivo [dmpl.zip](http://tdn.totvs.com/download/attachments/187531745/dmpl.zip?version=1&modificationDate=1430332200000&api=v2), onde o cliente pode fazer a adaptação conforme sua necessidade.

* **Registro – 0035**

Este registro é gerado no livro G, a partir do cadastro de Sociedade Conta de Participação - SCP

* **O que significa SCP?**

A sigla SCP significa “Sociedade em Conta de Participação”.

Refere-se a uma sociedade criada entre duas ou mais pessoas (das quais pelo menos uma das partes precisa ser uma pessoa jurídica) para a realização de uma atividade comercial pré-determinada.

A sociedade é terminada quando a prática da atividade finaliza, ou quando o objetivo pré-determinado da sociedade é atingido. Ou seja, é uma sociedade que pode ou não ter um prazo de validade, e é realizado apenas para que todas as partes lucrem mediante uma ou mais atividades.

O empreendimento é realizado por dois tipos de sócios: O Sócio Ostensivo e o Sócio Participativo.

O sócio ostensivo (necessariamente empresário ou sociedade empresária) realiza em seu nome os negócios necessários para fazer acontecer o empreendimento, e responde sozinho para os terceiros (clientes, outros parceiros de negócios, etc.).

O sócio participativo, em contraposição, fica unicamente obrigado por todos os resultados das transações e obrigações sociais empreendidas nos termos precisos do contrato.

A partir de 03.06.2014, por força da revogação do artigo 4 da [IN SRF 179/1987](http://www.normaslegais.com.br/legislacao/instrucao-normativa-in-srf-179-1987.htm) pela [IN RFB 1.470/2014](http://www.normaslegais.com.br/legislacao/instrucao-normativa-rfb-1470-2014.htm), as SCPs são obrigadas a inscrever-se no Cadastro Nacional da Pessoa Jurídica - CNPJ.

* **Como proceder para converter o arquivo TXT do Plano de Contas Referencial (disponibilizado pela Receita Federal) em CVE?**

Para proceder corretamente acesse a seguinte publicação [Como converter e importar o plano referencial da Receita Federal](http://tdn.totvs.com.br/display/public/mp/Como+converter+e+importar+o+plano+referencial+da+Receita+Federal)

* **Como dar *performance* à geração do SPED CONTABIL?**

Pelo parâmetro **MV\_CTBSPRC**é possível parametrizar o uso da *procedure* dinâmica do SPED Contábil. De acordo com o volume de dados a ser gerado, recomendamos que o processo seja executado diretamente no servidor Protheus, para evitar a latência de rede.

* **A conta referencial informada não está vigente no período da escrituração definido no registro 0000.**

Nesta situação esclarecemos que existem contas no Plano de Contas Referencial, disponibilizado pela Receita Federal, que não podem mais ser utilizadas no período executado. Portanto efetue a manutenção no Plano de Contas Referencial, fazendo os ajustes necessários, de modo a não mais utilizar essas contas.

* **A ECD possui *procedure*?**

Sim, existe uma *procedure* dinâmica, ativada ao configurar o parâmetro **MV\_CTBSPRC** como**.T.**(*True**/Verdadeiro*)

* **Geração com centralização / sem centralização, qual a diferença entre elas?**

Sem centralização: Quando as tabelas de saldos, como a **CT7**, estão compartilhadas com a demais tabelas de saldo, requer gerar "Sem Centralização".

Com centralização: Quando as tabelas de saldos estão marcadas como Exclusiva.

* **TABELA CVD - não existe amarração do Plano de Contas como Plano de Contas Referencial.**

A amarração entre as tabelas **CT1** e **CVN** alimenta a tabela **CVD**.

* **A rotina Cadastro de Planos de Contas Referencial, não está disponível no menu.**

Descrevemos o procedimento para criar pelo módulo Configurador:

No **Configurador** , acesse **Ambiente / Cadastros / Menus**, crie-o conforme abaixo:

**Nome do Menu > Atualizações > Submenu > Cadastros;**

**Nome da Rotina:**Plano de Contas Ref.;

**Programa*:***CTBA025;

**Tabelas:**CVN;

* **Qual o procedimento para gerar os registros J001, J005, J100, J150 e J900****?**

**Rotina: Cadastro Calendário Contábil.**

Acesse: Atualizações / Cadastros / Calendário Contábil clique em: Efetuar os cadastros / manutenção devidos.

**Rotina: Cadastro Visão Gerencial.**

Acesse: Atualizações / Cadastros / Visão Gerencial  clique em: Efetuar os cadastros / manutenção devidos.

**Rotina: Configuração de Livro.**

Acesse: Atualizações / Cadastros / Config. Contábeis / Configuração de Livros e faça a amarração da Visão Gerencial com a configuração do livro.

**Rotina: Apuração de Resultado.**

Acesse: Atualizações / Miscelânea / Encerramentos / Apuração de Resultado

**Rotina: Central de Escrituração.**

Acesse Atualizações / Escriturações Cont. / Central de Escrituração, na Parametrização informe o código do Balanço Patrimonial e da DRE já parametrizadas. Em seguida, defina o nome do arquivo e o diretório para salvar o TXT e verifiquei se no TXT, foi gerado o registros J.

* **Qual o procedimento para a geração do diário auxiliar?**

Escolha no tipo de escrituração, Com ou Sem escrituração.

Na situação especial, informe se existem outras inscrições.

Escolha o diário auxiliar.

Defina o período que será gerado, (normalmente anual).

Escolha o nome do TXT e o diretório de gravação.

* **Como gerar o Código Hash?**

Após importar o TXT no validador da Receita, e validá-lo pelo código hash, gera-se o Diário Resumido – R.

* **Qual o procedimento para a geração do Diário Resumido?**

Escolha o tipo de escrituração, Com ou Sem escrituração.

Escolha a situação especial, informe se existem outras inscrições.

Escolha o diário resumido, defina o período de geração (normalmente anual), clique no botão Hash e informe o código hash, do arquivo diário A, ao gerar o TXT.

* **É obrigatório a entrega da escrituração contábil em partida dobrada?**

O método das partidas dobradas é um princípio fundamental do registro na Contabilidade, de uso universal. Tem como premissa, o equilíbrio patrimonial entre origem e aplicação de recursos de um mesmo fato contábil.

Porém a resolução CFC 1299/2010 definiu as formalidades da escrituração contábil Digital – ECD, da seguinte forma:

 “Um lançamento pode ter vários registros a débito e vários registros a crédito somente quando relativos ao mesmo fato contábil”

Sendo assim, ao assumir uma escrituração contábil com lançamentos de quarta fórmula está sujeito a advertência que será tratada a seguir.

* Advertência: Lançamentos de quarta fórmula devem se referir a um mesmo fato contábil. Verifique se a situação está correta.

É uma advertência para que verifique se o lançamento efetuado está correto (se refere a um único fato contábil, apesar de ser de quarta fórmula).

1ª fórmula: Quando há apenas 1 conta debitada e 1 conta creditada;

2ª fórmula: Quando há 1 conta debitada e várias creditadas;

3ª fórmula: Quando aparecem várias contas debitas e apenas 1 conta creditada;

4ª fórmula: Quando aparecem várias contas debitadas e creditadas.

Se o lançamento refere-se a um único fato contábil, não impede a entrega da escrituração. Porém se o lançamento refere-se a vários fatos contábeis, deve ser feito o ajuste.

* **Quais são os pontos impactantes nesta mudança do ECD 3.0?**

Mudança do Plano de Contas Referencial;

Fazer o mapeamento entre o Plano de Contas e o Plano de Contas Referencial;

Geração do livro S – SCP (se houver)

Subcontas Correlatas.

* **Há algum problema quando o período  é aberto quinzenalmente?**

Para a entrega da ECD o calendário contábil (CTBA010) deve ter 12 períodos ou, em situações especiais, deve haver um calendário contendo exatamente o período da situação especial e outro com o período remanescente.

Caso não possua um calendário neste modelo, basta criá-lo pela rotina CTBA010, sem amarrar moedas, e informá-lo no momento da geração da escrituração.

* **Esta nova estrutura para o ECD e o ECF,  utiliza o TAF dentro do Protheus 11 para consolidar as informações na geração do arquivo magnético?**

Não, a correlação das escriturações é feita diretamente pelo PVA e por enquanto somente o ECF é gerado pelo TAF.

* **No caso do Plano de Contas Referencial sem amarração, será impeditivo na geração do arquivo no sistema?**

Não é impeditivo, atualmente a entrega do plano referencial é facultativo para a ECD.

* **Que alterações de sistema precisamos fazer para conseguir gerar o SPED com as mudanças?**

Para versão 11 a aplicação do *Patch* TSDGQZ e execução do compatibilizador U\_UPDCTB (> ou = 02/04/15)

* **Sobre Centro de Custo foi dito que a apuração também deve ser por centro de custo. No caso seria a criação na Visão Gerencial ou na rotina de apuração propriamente?**

A empresa que entrega a escrituração contábil por centro de custo, deve ter feito a apuração de resultados por centro de custo também (CTBA211).

A Visão Gerencial com centro de custo não é demonstrada para composição do TXT para o Sped ECD.

* **O sistema permite fazer o "de-para" por centro de custo?**

Sim, a amarração da Conta Referencial pode ser feita para o centro de custo também.

Uma conta contábil pode ser amarrada a mais de uma Conta Referencial desde que possua centro de custos diferentes e de mesma natureza, em relação ao plano referencial.

* **Teremos novos cadastros para compor os registros novos (SCP,Auditores, Subcontas, etc)?**

Sim, o pacote SPED Contábil, do boletim técnico contêm todas as informações de tabelas e campos novos.

* **Tanto contas correlatas quanto referencial tem um padrão liberado pela receita para que eu****possa importar?**

Somente existe padrão da Receita para Contas Referenciais. Contas correlatas ficam a cargo de cada empresa, relacionado com a estrutura e nomenclatura mas, existe uma tabela do SPED para informar a natureza da conta correlata (importado para tabela SQ do SX5).

* **Se eu informar DLPA no J210 tenho que informar a visão em outras demonstrações?**

Não. Somente DLPA ou DMPL. Informe no campo apropriado a configuração referente à Visão Gerencial que fica logo após a pergunta "DLPA ou DMPL?".

* O fato contábil é obrigatório para o SPED?

Sim, desde que enviadas a DMPL ou DLPA.

* **Por que o sistema busca os valores da DRE e Balanço e não busca para DMPL?**

Porque não temos conceito de fato contábil no movimentos contábil (tabela CT2).

O código da configuração de visão gerencial do DMPL ou DLPA somente serve como estrutura para detalhamento do registro J210.

* **Com relação aos Fatos contábeis: eu terei de informar todas as vezes que voltar a executar a escrituração?**

Caso a estrutura da visão gerencial não seja alterada, a rotina possui um facilitador (tecla F12) para importar os fatos contábeis e detalhes cadastrados em uma revisão anterior.

* **Sempre que eu escrituro o ECD é gerada uma nova revisão automaticamente?**

Sim. Este é o controle que o sistema de escrituração do SIGACTB permite.

* **O campo M0\_NOMECOM (61 caracteres) não comporta o nome/razão social da minha empresa/filial, como faço para que o nome seja apresentado por completo?**

Basta substituir o campo CS2\_NOMEEM pelo o nome da empresa no arquivo ECDLIVRO\_G.xml.

* **Erro Registro J215 (DMPL)**

A Soma dos fatos contábeis (somatório do campo 03 dos registros J215 filhos) deve ser igual ao valor total de aglutinação (campo 05 do registro J210) mais saldo inicial do código de aglutinação (campo 07 do registro J210). Maiores detalhes: [Clique Aqui](http://tdn.totvs.com/display/PROT/CTB069_ECD_ERRO_Registro_J210)

* **Erro Registro J150 (DRE) | Saldo Anterior retornando valores desconhecidos**

Para corrigir esse erro e necessário aplicar o patch do chamado [TV4896](http://tdn.totvs.com/download/attachments/187531745/01tv4896_1.zip?version=1&modificationDate=1463746667000&api=v2), e em seguida reprocessar o saldos desde o ano anterior o qual o saldo esta incorreto. (Certififique-se que esta utilizando as procedures de atualização de saldos, para garantir uma boa performance durante o processamento)

* **Erro Registro J150 (DRE) | Saldo Anterior Zerado**

A correção desta não conformidade foi disponibilizada no RPO que esta disponivel no portal de clientes TOTVS.

* **Como efetuar o detalhamento do fato contábil e do histórico do fato contábil**

Para ter acesso ao vídeo instrutivo de como realizar o detalhamento do fato contábil [Clique aqui](http://tdn.totvs.com/pages/releaseview.action?pageId=237372094)

* **Como cadastrar o registro J800**

Para ter acesso ao vídeo instrutivo de como cadastrar o registro J800 [Clique aqui](http://tdn.totvs.com/download/attachments/187531745/ECD-J800.zip?version=1&modificationDate=1463747570000&api=v2)

* **Minha empresa apura os resultados de forma trimestral, como devo proceder?**

Para gerar o arquivo magnetico do ECD de forma trimestral será necessário gerar cada trimestre em um arquivo texto separado e valida-los um de cada vez no PVA.   
É importante ter o calendário contábil (CTBA010) com 12 períodos e caso não possua um calendário neste formato, basta inclui-lo (sem amarração de moedas) e informa-lo nos parâmetros da escrituração

* **O Protheus está habilitado para gerar as informações do Registro I157 Transferência de Saldos de Plano de Contas Anterior?**

Não, o Protheus não tem a funcionalidade de Transferência de Saldos de Plano de Contas Anterior pois só trabalhamos com um plano de contas.

 Como não é permitido a troca do plano de contas no meio do exercício contábil não há a possibilidade  de se realizar uma transferência de saldos de plano de contas e com não temos nenhum dado para geração o arquivo I157.
