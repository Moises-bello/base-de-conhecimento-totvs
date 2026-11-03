---
content_hash: 4028e4cf218033f1a4f0d3718e497172313c4bf2bcb1502617bdfbb8fae20adb
fetched_at: '2026-06-29T00:05:58.505059+00:00'
page_id: '187534251'
product: rm
source: tdn-rm
title: RMCTB00009_Roteiro para Geração de Demonstração de Lucros/Prej. Acumulados
  – DLPA para o SPED Contábil.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=187534251
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | RM TOTVS Gestão Contábil 11.52/11.82 |
| **Processo** | : | Demonstração Contábil |
| **Subprocesso** | : | Geração de Demonstração de Lucros/Prej. Acumulados – DLPA para o SPED Contábil |
| **Data da publicação** | : | 12/06/2014 |

A partir do layout **2.0** do SPED Contábil passa a existir dois registros que correspondem a **DLPA - Demonstração de Lucros ou Prejuízos Acumulados** e **DMPL – Demonstração das Mutações do Patrimônio Líquido**. Se a empresa for uma **S/A** ou de **grande porte** pode enviar no arquivo do SPED Contábil a **DMPL**. Caso contrário, se a empresa não for S/A ou de grande porte, poderá enviar no arquivo do SPED Contábil **a DLPA**.

O envio destas demonstrações é **facultativo.** Portanto, caso as empresas não queiram enviar estas demonstrações, o validador do SPED Contábil não acusará erros na validação do arquivo, apenas advertência. Se a empresa deseja enviar as demonstrações, disponibilizamos no TOTVS Gestão Contábil uma ferramenta bem prática e flexível, que permite a criação de qualquer demonstração ou relatório contábil/gerencial, e que viabilizará o envio da **DLPA** ou **DMPL** para o SPED Contábil. Também foram disponibilizados no sistema, templates padrões de DPLA e DMPL para auxiliar os usuários na criação das demonstrações e posterior envio para o SPED Contábil.

O objetivo deste roteiro é explicar como importar e ajustar estes templates, para a criação da DLPA da empresa. Iremos explicar as opções existentes na ferramenta para que a montagem funcione de forma fácil e prática.

***(clique no tópico/seta para expandir o conteúdo)***

1. O primeiro passo é importar o template padrão. Vamos iniciar nosso exemplo importando o template de DLPA. Acesse o sistema pela RM.exe que se encontra dentro da pasta RM.Net (chamamos este acesso de "Acesso pela tela MDI"). Depois escolha a opção de TOTVS Gestão Contábil.

1.1 – Na parte direita da tela existe a opção chamada **"TOTVS By you" -** acesse este recurso e digite no campo de pesquisa a palavra "**DLPA"**. Feito isto clique no ícone localizado abaixo do nome **"By you"**. O sistema irá localizar o template de **DLPA** atualizado. Então baixe o template para sua máquina para posterior importação no sistema.  
  
1.2 – Depois de salvar o Arquivo, acesse o menu **Escrituração Contábil/Demonstração Contábil/Estrutura**, realize o filtro e permaneça na **visão de estruturas.**  
  
1.3 – Clique no botão **"Incluir"** como se fosse incluir uma nova demonstração - porém iremos importar o template salvo no passo **1.1**.  
  
1.4 – Clique no ícone **"Importar Estrutura"** e busque o arquivo com o template de **DLPA**. Ao selecionar o arquivo e executar, informe um código para a estrutura. Pronto, o template padrão já foi importado e agora o próximo passo é analisar quais são as movimentações da conta de **Lucros/Prejuízos Acumulados** da empresa para definição dos fatos contábeis que serão mantidos ou alterados.

O objetivo do template é auxiliar as empresas na elaboração de seus relatórios. Mas cada empresa tem sua movimentação da conta e isto faz com que alguns fatos contábeis sugeridos não necessitem ser utilizados para a demonstração. Portanto, os fatos contábeis que não forem utilizados podem continuar no template e não serão configurados. Os fatos existentes que não são configurados não são processados para geração da demonstração. Caso a empresa não deseje visualizar os fatos contábeis zerados que não foram configurados, a opção de enviar para o SPED Contábil poderá ser desmarcada ou se desejado podem ser excluídos para que não mais faça parte da estrutura da demonstração.

2. Para melhor entendimento vamos apresentar a estrutura do template padrão de DLPA. A DLPA padrão possui a seguinte estrutura:

1 - **Saldo em 31.12.XO (início do período)**  
2- (+/-) Ajuste de Exercícios Anteriores  
2.01 - Mudança de política contábil  
2.02 - Retificação de erros  
3 -  Lucro líquido do exercício  
4 - Lucro total disponível  
5 -  Transferências para reservas de lucros  
5.01 - Reserva legal  
5.02 - Reserva estatutária  
5.03 - Reserva para contingências  
5.04 - Reserva de incentivo fiscal  
5.05 - Reserva orçamentária (Retenção de Lucros)  
5.06 - Reserva de lucros a realizar  
6 -  Lucros ou Dividendos a distribuir  
7 - **Saldo Final do Período**

Conforme já informado, caso a empresa não possua algum fato contábil descrito acima, basta **não configurar o fato contábil** **(veremos posteriormente como configurar), se não desejar que o fato seja apresentado zerado, a opção de envio para o SPED Contábil deverá ficar desmarcada, caso não deseje que o fato faça parte da estrutura o mesmo deve ser excluído** . No caso da **DPLA** na aba **"Colunas da Demonstração"** existe somente uma coluna denominada **"R$".**

2.1 Antes de explicarmos a estrutura de fatos acima, vamos apresentar as opções que existem ao editar o fato contábil:

**Grau – Sintético ou Analítico** – podemos totalizar os valores que estão abaixo de um fato contábil - neste caso utilizamos a opção de grau **"sintético" -** ou podemos totalizar os valores que estão acima de um fato contábil - neste caso utilizamos a opção de grau **"analítico",** ou simplesmente teremos um fato contábil que irá apresentar um valor, onde ele será considerado **"analítico".**

**Mostrar no SPED Contábil** – Significa que o fato contábil será apresentado na estrutura que será enviada para o SPED Contábil.  
Tipo:

* **Fato Contábil** – no caso da **DLPA**, vamos apresentar a movimentação de uma conta contábil - a conta de **Lucros/Prejuízos Acumulados.** Então, nossa sugestão é que seja emitido um razão analítico desta conta para montagem dos fatos, a **DLPA** pode ser configurada utilizando contas e filtros genéricos. Sugerimos que seja utilizado a configuração por contas, pois assim caso a empresa trabalhe com apuração trimestral, poderá criar apenas **1 DLPA**, pois o processamento dos valores estará configurado por conta contábil e não por filtros específicos.
* **Totalizador** – são fatos que tem a função de totalizar os valores, acima ou abaixo de sua estrutura, conforme definição do grau.

2.2 Agora vamos apresentar cada fato do template padrão de DLPA e explicar as opções que estão marcadas para facilitar o entendimento:

**1 - Saldo em 31.12.XO (início do período)**  
O fato **1** está configurado como **"analítico"** , se trata do saldo inicial da conta de **Lucros/Prejuízos Acumulados**. Para a **DLPA** o SPED Contábil **não calcula automaticamente o saldo inicial e final**. Neste fato em nossos templates padrões vamos configurar o saldo inicial da conta de **Lucros/Prejuízos Acumulados**.

**2- (+/-) Ajuste de Exercícios Anteriores**  
O fato **2** se trata de um fato **totalizador sintético -** isto significa que irá totalizar todos os fatos que estão abaixo do código **2**, que são os códigos **2.01 e 2.02**. O sistema já está preparado para gerar corretamente este fato contábil para o arquivo do SPED Contábil. 

* **2.01 - Mudança de política contábil:**
* **2.02 - Retificação de erros :**

Conforme já informado o código **"2.01 e 2.02"** são fatos contábeis, então esta opção deve estar marcada ao editar os registros. Em nossos templates padrão estes fatos não estão configurados, mas sugerimos que caso seja possível,  deve-se buscar os valores destes por contas contábeis. Ou seja, existindo valores para estes fatos registrados em contas contábeis, deve-se buscar as movimentações das contas que represente estes valores (Débito, Crédito, etc). Caso contrário, se os valores estivem registrados somente na conta de **Lucros/Prejuízos Acumulados** pode-se fazer filtros genéricos. Porém, como os filtros são específicos, se a empresa necessitar da **DLPA trimestral**, o filtro poderá não processar valor em determinado trimestre.

**3 -  Lucro líquido do exercício**  
Também vamos marcar a opção "**Fato Contábil".** Em nossos templates padrões podemos buscar este fato por filtro genérico ou conta, porém sugerimos que o valor seja buscado por conta. Por exemplo, o total de crédito da conta de Lucro/Prejuízos Acumulados. Emitindo um razão da conta identificamos que a movimentação à crédito corresponde ao Lucro, por este motivo definimos esta configuração no nosso template configurado por contas. Em uma possível **DLPA trimestral,** a configuração por conta atenderia a todos os trimestres.

**4 - Lucro total disponível**  
O Lucro total disponível é um "**totalizado analítico" -** isto significa que todos os fatos acima serão calculados para se chegar ao resultado do **Lucro disponível**.

**5 -  Transferências para reservas de lucros**  
Este fato é um "**totalizador sintético"** que irá calcular o valor de todas as transferências para a **Reserva de Lucros**.   
Todas as Reservas possuirão também a opção "**Fato Contábil",** pois são valores que estão saindo da conta de **Lucros/Prejuízos Acumulados** e **entrando nas contas de Reservas**,  em nossos templates de DLPA estes valores podem ser configurados via contas contábeis,  filtrando as movimentações à crédito que estão entrando nas contas de reservas por exemplo, ou buscando os valores por filtros genéricos através de filtros com os valores das partidas que estão saindo da conta de Lucros/Prejuízos Acumulados. Porém, conforme já informado, a sugestão é buscar sempre por movimentações da conta.

5.01 - Reserva legal  
5.02 - Reserva estatutária  
5.03 - Reserva para contingências  
5.04 - Reserva de incentivo fiscal  
5.05 - Reserva orçamentária (Retenção de Lucros)  
5.06 - Reserva de lucros a realizar

**6 -  Lucros ou Dividendos a distribuir**  
O fato acima também é uma movimentação que está saindo da conta **de Lucros/Prejuízos Acumulados** e entrando **na conta de Dividendos.** Portanto podemos buscar o valor à crédito existente na conta de Dividendos.

**7 - Saldo Final do Período**  
O saldo final é um fato que irá totalizar todos os fatos que estão acima, portanto se trata de um **"totalizador analítico".** Este fato também já está preparado para ser enviado para o arquivo do SPED Contábil corretamente.

Conforme citamos anteriormente, aqui mostramos todas as opções disponíveis em nossa sugestão de template de **DLPA**, mas dependerá de como foi a movimentação da conta de **Lucros/Prejuízos** **Acumulados** de cada empresa.

Importante: O validador do SPED Contábil realiza a seguinte validação:

Saldo inicial da DLPA **(Registro J210)** + fatos contábeis **(Registro J215)** = **Saldo final da DLPA**

Se esta regra não respeitada ocorre erro na validação.

Outra validação que será feita pelo validador é verificar se o **saldo inicial e final da DLPA** **(Registro J210)** estão de acordo com o **saldo inicial e final da conta contábil no registro de saldos Periódicos** **(Registro I155).** Na configuração do **saldo inicial da DLPA (primeiro fato)** é muito importante que seja vinculada corretamente a conta de **Lucros/Prejuízos Acumulados,** pois o sistema irá somar o saldo inicial desta conta com as movimentações existentes nos fatos para chegar nos saldo finais. Estes valores serão enviados para o arquivo do SPED Contábil no registro J210. Se os mesmos não fecharem com o valor conta de Lucros/Prejuízos Acumulados existente no registro I155 ocorrerá erros. Por isto é muito importante que seja vinculado corretamente a conta no saldo inicial. Existindo outros fatos contábeis configurados por conta como no exemplo acima, onde citamos os valores das reservas sendo buscados por movimentação à crédito não ocorrerá problema para a correta geração dos valores, o sistema já está preparado para trabalhar com mais de uma conta configurada em sua estrutura, o importante é definir a conta correta no fato de saldo inicial. Este procedimento é válido também para os templates de DMPL, nos fatos de saldos iniciais deverá ser configurado corretamente as contas para que os valores gerados coincidam com os valores do registro I155.

3. O próximo passo é configurar os fatos contábeis analíticos. Os fatos que são totalizadores (sintéticos ou analíticos) não precisam ser configurados. Configurar um fato é definir de onde serão buscados os valores desejados.

* 3.1 Na parte superior da estrutura existe a aba de **"Configuração de Layout".** Ao clicar nesta aba, todos os fatos que podem ser configurados estão com o **símbolo de exclamação**, então basta clicar no símbolo e configurar o fato conforme desejado.
* 3.2 Em nosso exemplo, o fato de "**1 - Saldo em 31.12.XO (início do período):"** será configurado com o **Saldo inicial da conta de Lucros/Prejuízos Acumulados**. Os demais fatos podem ser configurados por contas e também por filtros genéricos. Mas sugerimos a configuração por contas. **Por que?**

Podemos por exemplo realizar um filtro com o campo **"Referência**" de cada valor de movimentação da conta de Lucros/Prejuízos Acumulados, buscando a respectiva partida contábil. Se a empresa necessita da Demonstração (DLPA ou DMPL) trimestral este filtro não existirá em algum trimestre, pois é específico, está buscando uma determinada partida. A configuração por contas busca movimentações da conta (Débito, Crédito, etc), assim os valores existirão em todos os trimestres.

Se por algum motivo o fato não existir na realidade da empresa, o mesmo pode ficar sem configuração **(com o símbolo de exclamação)** que não será processado pelo sistema. Se a empresa não quiser que o fato contábil que não foi configurado não seja apresentado, a opção de envio para o SPED Contábil pode ser desmarcada, se desejar que o fato não faça parte da estrutura o mesmo deve ser excluído.

***Nota: Conforme já citado, é muito importante que a configuração do fato que representa o saldo inicial na DLPA e os fatos que representam os saldos iniciais das colunas na DMPL sejam configuradas corretamente com as respectivas contas, pois o SPED Contábil cruza os valores de saldo da conta informada na DLPA/DMPL (registro J210) com os valores no registro de saldos periódicos (registro I155).***

Dentro das opções de Configuração, existe a opção para definição do sinal do saldo. Vamos dar um exemplo de como funciona esta opção para melhor entendimento:

Na definição do saldo inicial da conta de **Lucro/Prejuízos Acumulados,** se informamos a opção de saldo inicial e **sinal = original**, caso o saldo da conta for **credor,** o sistema irá apresentar um sinal de negativo à frente do valor na geração da demonstração. Internamente para o sistema, todos os saldos credores possuem o sinal de **menos** antes dos valores. Portanto, se desejamos apresentar o saldo inicial da conta de **Lucro/Prejuízos Acumulados** **sem o sinal de menos**, a opção a ser escolhida será "**Efeito Positivo – Aumenta" -** Vamos explicar:

Se internamente o saldo credor possui o sinal de menos à frente dos valores quando escolheremos a opção acima, o sinal de menos será retirado**.** Com isso, se a conta de Lucros está credora, o valor apresentado não possuirá mais sinal.

**Se for o inverso**, uma conta com saldo devedor e pedimos o **saldo original**, será apresentado o valor sem nenhum sinal. Então, se o usuário desejar que o valor seja apresentado com o sinal de menos à frente, deverá escolher a opção **"Efeito Negativo – Diminui".** 

**Exemplo:** Em nosso template padrão de DLPA configurado por conta buscamos o **valor de crédito no fato de Reserva Legal** e configuramos o efeito para **"Efeito Negativo (Diminui)".** Com esta configuração os valores das reservas serão apresentados com **sinal de menos à frente do valor.**

Para o SPED contábil os valores positivos na DLPA/DMPL são considerados **"Créditos**" e os valores negativos são considerados "**Débitos".**

Portanto, devemos lembrar que a opção **"Efeito Negativo – Diminui" irá colocar o sinal de menos nos valores** e o "**Efeito Positivo – Aumenta" irá retirar o sinal de menos.** Se a opção for **"original"** sempre que o saldo de uma conta **for credor**, o sinal de  será apresentado à frente do valor.

***Nota: Em nossos templates padrões utilizamos a opção de Buscar Saldo Inicial para a conta de Lucros/Prejuízos Acumulados e para os fatos contábeis, utilizamos a opção de "filtro genérico".*** ***Entretanto, existem várias opções disponíveis na configuração dos valores - inclusive o usuário pode criar expressões para buscar valores conforme necessidade - a ferramenta é bastante flexível e a busca dos valores poderá ser feita de várias formas, sempre lembrando que para geração do SPED Contábil conforme já informado, o validador irá confrontar os valores de saldos das contas.*** ***Por este motivo é importante definir os valores dos fatos contábeis de saldos iniciais corretamente.***

**Informações Importantes:** Este roteiro apresentou os passos para geração e ajuste do template de **DLPA.** Para o template padrão de **DMPL,** os procedimentos para importação são os mesmos e as opções dos fatos contábeis também. A diferença da **DMPL** é que esta demonstração irá apresentar as **mutações das contas do patrimônio líquido**, portanto existirão mais de uma coluna nesta demonstração. Mas a lógica para a montagem será a mesma da DLPA.

Para a **DMPL** o SPED Contábil gera automaticamente o saldo inicial e final das contas, mas mesmo assim o sistema precisa que na estrutura sejam configurados os fatos de saldos iniciais/finais e a opção **"Mostrar no SPED"** precisa estar marcada.

Para maiores informações:

[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE**[**R@Contábil**](https://totvs.byyou.com/?space=rcontabil)

**Canais** **de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:**4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 2 – (Controladoria e Finanças), 5 – (Planejamento e Controle Orçamentário), 2 – (RM Saldus).
