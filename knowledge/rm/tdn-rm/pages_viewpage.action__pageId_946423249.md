---
content_hash: 371fb0da5753ee4bc489989bb7e5e0c1c13a4682ebbfcb9afc1a5a1c257d4f62
fetched_at: '2026-06-29T00:12:09.471972+00:00'
page_id: '946423249'
product: rm
source: tdn-rm
title: FAQ - Crédito do Trabalhador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=946423249
version: 32
---

**Importante**: Esta FAQ está em constante evolução. Desta forma, novas perguntas serão adicionadas com o tempo.

**Material do Webinar:** [TOTVS\_Responde\_Credito-do-Trabalhador\_Jun-25\_Linha-RM.pdf](https://tdn.totvs.com/pages/viewpage.action?pageId=840389446&preview=/840389446/956638589/Suporte_Responde_Credito_do_Trabalhador_Jun-25_Linha-RM.pdf#EventosSuporteT%C3%A9cnico--1877355269)

**DOCUMENTAÇÃO**

* [Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março de 2025](https://tdn.totvs.com/pages/releaseview.action?pageId=925361639)
* [Espaço Legislação - Crédito do Trabalhador](https://espacolegislacao.totvs.com/credito-do-trabalhador/)
* [Gov.br - Manual Operacional do Empregador](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/credito-do-trabalhador/empregador/)
* [MTE - Portal Emprega Brasil](https://servicos.mte.gov.br/empregador/#/login)

**PERGUNTAS FREQUENTES - ÍNDICE**

#### **01 - Versão e Atualizações**

**01.001 - Qual a versão mais atual que contempla o Crédito do Trabalhador (antigo eConsignado)?**

Alterações e documentação foram liberadas de forma faseada, conforme abaixo:

* 1a Fase: 26/03/2025 **-**  eSocial - [DT - Crédito do Trabalhador eSocial](https://tdn.totvs.com/pages/releaseview.action?pageId=925346824)
* 2a Fase: 30/04/2025- Cadastro do Empréstimo, Importação de Empréstimos Crédito do Trabalhador, Cálculos de Folha e Rescisão e Importação/Exportação - [DT - Crédito do Trabalhador eSocial - Cálculos](https://tdn.totvs.com/pages/viewpage.action?pageId=939246677)
* 3ª Fase: 09/05/2025 -Cancelamento de Movimento e rescisão - [DT - Crédito do Trabalhador eSocial - Cálculos](https://tdn.totvs.com/pages/viewpage.action?pageId=939246677)
* 4ª Fase: 16/05/2025 - Provisionamento de Férias - [DT - Crédito do Trabalhador eSocial - Cálculos](https://tdn.totvs.com/pages/viewpage.action?pageId=939246677)

Abaixo, os patches com as liberações mais atuais. Sugerimos atualização para estes os patches superiores aos listados:

* + 12.1.2406.277
  + 12.1.2410.229
  + 12.1.2502.145
  + 12.1.2506 e superiores

**01.002 - Para clientes que utilizam o Middleware, é necessária a atualização do TAF/TSS?**

Clientes que utilizam o Middleware precisam realizar a atualização apenas dos Schemas do TSS, conforme documentação a seguir: [TSS - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552)

**01.003 - Para clientes que o TAF Full (padrão), é necessária atualização do TAF/TSS?**

Sim. Importante que verifique se o seu TAF esta na ultima expedição de 04/2025, caso não esteja nessa atualização utilize os matérias abaixo para **atualização do sistema TAF**:

**1º** - [RH - Linha Protheus - TAF - ATUALIZAÇÃO - Como atualizar o TAF E-social (Expedição Contínua)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18972648169239-RH-Linha-Protheus-TAF-ATUALIZA%C3%87%C3%83O-Como-atualizar-o-TAF-E-social-Expedi%C3%A7%C3%A3o-Cont%C3%ADnua)   
**2º -** Pacote pontual para correção de erro referente à instituição financeira no TAF - Aplique o pacote de acordo com sua VERSÃO do TAF:   
     12.1.2210:<https://r.totvs.io/p/1196137> ;   
     12.1.2310:<https://r.totvs.io/p/1196136> ;   
     12.1.2410:<https://r.totvs.io/p/1196138>  
     **Obs**.: deve ser executado a **atualização das tabelas autocontidas** após aplicação do pacote pontual e deve ser integrado um novo XML do ERP ao TAF. 

Também é necessária **atualização dos Schemas do TSS** conforme documentação: [TSS - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552)

**01.004 - Existe algum procedimento específico a ser realizado antes de iniciar as parametrizações do sistema?**

Sim! É extremamente importante que, após atualização do sistema para um dos Patches citados no item 01.001, seja realizada a execução dos scripts específicos através do **[RM.Atualizador.exe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5893403025687)**.

#### **02 - Novos Códigos de Cálculo**

**02.001 - Quais os novos códigos de cálculo necessários e quais são suas especificidades?**

No menu Administração de Pessoal | Eventos, será necessário criar os eventos utilizando os novos códigos de cálculo listados abaixo. Clique no nome de cada item para visualizar sua documentação.

* [480 - Desconto Empréstimo Crédito do Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=937704422)
* [481 - Provisão Empréstimo Crédito do Trabalhador Folha](https://tdn.totvs.com.br/pages/viewpage.action?pageId=938311697)
* [482 - Remuneração Base Empréstimo Crédito do Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=938311709)
* [483 - Insuficiência Saldo Empréstimo Crédito Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=938311723)
* [484 - Provento Provisão Empréstimo Créd.Trab.Folha](https://tdn.totvs.com.br/pages/viewpage.action?pageId=938311735)
* [485 - Provisão Crédito Do Trabalhador Férias 1º Mês](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707652)
* [486 - Provisão Crédito Do Trabalhador Férias 2º Mês](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707666)
* [487 - Provisão Crédito Trab. Férias 1º Mês Envelope](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707675)
* [488 - Provisão Crédito Trab. Férias 2º Mês Envelope](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707680)
* [489 - Adiantamento Provisão Emprést.Crédito](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707701)

**02.002 - Já atualizei o sistema porém os novos códigos de cálculo não aparecem. O que fazer?**

Se seu ambiente já está atualizado conforme item 01.001, verifique se o RM. Atualizador.exe também foi executado (item 01.004).

Além disso, a criação do código de cálculo na base é feita com a execução de um recálculo para os patches das versões 12.1.2406, 12.1.2410 e 12.1.2502. Sendo assim, é necessário **executar algum recálculo** na base para, depois, inserir os eventos no cadastro de eventos com os respectivos códigos de cálculo.

**02.003 - Qual natureza de rubrica eSocial utilizar nos novos eventos?**

A partir do Leiaute S-1.3 do eSocial, foi disponibilizada a natureza de rubrica "**9253 - Empréstimos eConsignado - Desconto**" para diferenciar a rubrica de desconto do Crédito do Trabalhador dos demais empréstimos consignados. Sendo assim, essa natureza deve ser utiliza no evento de CC 480, visto orientação do Governo. Contudo, as demais verbas não possuem orientação direta do Governo quanto às naturezas de rubrica, sendo assim, fica à cargo do usuário do sistema definir a natureza que entende mais adequada.

A TOTVS não orienta a natureza de rubrica a ser utilizada em cada verba, mas sugerimos validar o [Manual de Orientação do Empregador](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-operacional-do-empregador-programa-credito-do-trabalhador-v2-16-05-25.pdf) em que, a partir da página 27 (item **5.2.1 Exemplos de Apuração da Remuneração Disponível**) contam exemplos de cálculos, apresentando algumas naturezas também.

#### **03 - Parametrizador**

**03.001 -  Existe a possibilidade de copiar entre coligadas o parametrizador somente do crédito do trabalhador?**

Sim, através do menu Configurações | Copiar Parâmetros Entre Coligadas, selecionar na árvore a opção "06.01.03 - Folha Normal | Crédito Trabalhador" e avançar o processo.

#### **04 - Importação do Empréstimo - Crédito do Trabalhador**

**04.001 - Como faço para importar para o sistema o arquivo do Crédito do Trabalhador baixado no Portal Emprega Brasil?**

No menu Folha Mensal | Importações | Importação de Empréstimo Consignado FEBRABAN deverá ser importado o arquivo fornecido pelo Portal Emprega Brasil, conforme orientações descritas na documentação: [Importação Empréstimos FEBRABAN / Crédito do Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719677&draft=true).

**04.002 - A importação precisa ser realizada manualmente todos os meses?**

Sim. O governo realizou a liberação de uma API para que os fornecedores de Software implementem uma importação automatizada direto do Governo. Contudo, até que isso seja disponibilizado, será necessária a importação manual todos os meses para que o sistema atualize informações sobre as parcelas, saldo, entre outros dados. Acompanhe as novidades de liberações do produto através do [TOTVS Informa](https://informa.totvs.com/rh/) e [Novidades da Release](https://tdn.totvs.com/display/LRM/Novidades+da+Release).

**04.003 - Qual o processo de importação de arquivo? É possível importar arquivo da competência posterior a folha aberta?**

O arquivo fornecido pelo Portal Emprega Brasil, deverá ser importado para a folha através do módulo "Importação de Empréstimos FEBRABAN/ Crédito Trabalhador".Poderá ser importado um novo arquivo, sem sobreposição, somente quando já houver realizado o lançamento do empréstimo.

Ainda não é possível realizar a importação para competências futuras, mas essa implementação já está sendo avaliação pelo time de desenvolvimento do produto.

Documentação: [Importação Empréstimos FEBRABAN / Crédito do Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719677).

**04.004- Como é feito a gravação e quitação das parcelas?**

Após o lançamento e cálculo do empréstimo, a gravação é feita como alteração no cadastro de empréstimos, registrando no anexo "Descontos de Empréstimos" a competência, o período, o valor descontado e o valor da insuficiência de saldo (quando houver).

**04.005-Como é o tratamento para importação de arquivos entre coligadas?**

O arquivo deverá ser importado por coligada, selecionando o arquivo e qual coligada a ser importada. Documentação:  [Importação Empréstimos FEBRABAN / Crédito do Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719677).  
O time de desenvolvimento do produto já está trabalhando numa importação de multi-arquivos, para que seja possível importar todos os arquivos de uma vez. Acompanhe as novidades de liberações do produto através do [TOTVS Informa](https://informa.totvs.com/rh/) e [Novidades da Release](https://tdn.totvs.com/display/LRM/Novidades+da+Release).

**04.006- Qual o processo de importação  de arquivo para funcionário que foi transferido entre coligadas?**

O arquivo é importado mensalmente e validada a raiz do CNPJ. Desta forma, após a transferência de coligada deverá ser importado o novo arquivo da coligada em questão, conforme disponibilizado pelo governo.

**04.007- Como é tratado múltiplos vínculos na importação do arquivo?**

No layout do arquivo do Portal Emprega Brasil, o empréstimo é informado por matrícula eSocial. Como cada vínculo tem sua matrícula eSocial específica, a importação fará essa validação. Inclusive, para identificar se já existe o empréstimo cadastrado para o colaborador, será verificado a existência de empréstimo com o mesmo número de contrato e matrícula eSocial do cadastro de funcionários, e assim processar a alteração do cadastro de empréstimo.

**04.008 - Como deve ser a geração da Guia para recolhimento do valor do Credito do Trabalhador realizado em folha de pagamento?**

No FGTS Digital, o empregador poderá gerar guias com valores de empréstimo consignado por meio das funcionalidades "EMISSÃO DE GUIA RÁPIDA" ou "EMISSÃO DE GUIA PARAMETRIZADA". O sistema exibirá todos os valores de FGTS e empréstimo consignado do mês selecionado, separados em blocos. Nesta opção, não será possível alterar a seleção dos débitos (inclusão/exclusão) que irão compor a guia a ser gerada. Basta clicar em "Emitir Guia" e será gerada uma guia com os valores de FGTS e de empréstimo consignado escriturados no eSocial daquele mês.   
Ver exemplo na página a seguir: [Espaço Legislação - Crédito do Trabalhador](https://espacolegislacao.totvs.com/credito-do-trabalhador/#operacionalizacao-no-fgts-digital).

#### **05 - Desconto do Empréstimo - Crédito do Trabalhador**

**05.001 - Qual o valor da margem consignável? Como será considerada essa margem no sistema?**

A margem consignável é de 35%. Ao realizar o lançamento do empréstimo, o sistema irá lançar o desconto da parcela através do evento de **código de cálculo 480**, e também irá lançar a base de remuneração considerada através do evento de **código de cálculo 482**. Também são exibidos detalhes sobre o cálculo no Log de Cálculo do envelope do funcionário.  
Veja mais detalhes do cálculo na documentação a seguir: [Crédito do Trabalhador - Cálculo 35% da Margem Consignável](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32152995698071)

**05.002 - Qual é o comportamento do sistema quando não houver margem consignável?**

Quando não houver margem consignável, será informado no anexo "Desconto do empréstimo", no campo "Valor da Insuficiência de saldo", o valor que não foi descontado do funcionário. Neste caso, o funcionário deverá entrar em contato com a instituição financeira vinculada ao contrato para renegociação.   
Nosso time de desenvolvimento do produto está avaliando a liberação de comunicado sobre a insuficiência de saldo no envelope do funcionário. Acompanhe as novidades de liberações do produto através do [TOTVS Informa](https://informa.totvs.com/rh/) e [Novidades da Release](https://tdn.totvs.com/display/LRM/Novidades+da+Release).

**05.003 - Como será o comportamento do sistema quando o funcionário não tiver saldo suficiente para desconto da parcela em folha de pagamento?**

Foi criado novo código de cálculo (CC 483) para armazenar o valor não descontado do funcionário por motivo de insuficiência de saldo. Este código de cálculo tem a possibilidade de impressão no recibo de pagamento, além disso foi disponibilizado um relatório para listagem dos funcionários nesta situação: . Nosso time de desenvolvimento do produto está avaliando também a liberação de comunicado sobre a insuficiência de saldo no envelope do funcionário. Acompanhe as novidades de liberações do produto através do [TOTVS Informa](https://informa.totvs.com/rh/) e [Novidades da Release](https://tdn.totvs.com/display/LRM/Novidades+da+Release).  
***Obs**.: O valor não descontado no mês, **não poderá ser descontado acumulativo na próxima competência**, o funcionário deverá procurar a instituição financeira para renegociação.*

**05.004 - Como é realizado o desconto para funcionários afastados?**

Para funcionários afastados pelo INSS, conforme descrito na Medida Provisória, não há responsabilidade do empregador pelo repasse da remuneração, e, portanto, não há como realizar o desconto da parcela consignada nesse período.

**05.005 - Qual a prioridade do desconto do crédito do trabalhador em relação às demais verbas?**

A prioridade de cálculo será 98 e pode ser verificada no log de cálculo. É uma prioridade interna específica do Código de Cálculo "480 - Desconto Empréstimo Crédito do Trabalhador", que deve ser o último evento a ser calculado. Eventos como "Pensão Alimentícia", por exemplo, devem ser calculados antes.   
Para saber sobre a prioridade de desconto, se deve priorizar o desconto do empréstimo ao invés da pensão alimentícia, por exemplo, vai depender do entendimento da empresa e da parametrização realizada.

Cenário 01 - Não há valores informados no parametrizador da folha de pagamento, etapa "Folha Normal | Eventos do Crédito do Trabalhador" - Neste caso, o sistema irá somar todos os proventos e diminuir todos os descontos. Como não há eventos no parametrizador, os descontos terão prioridade sobre o empréstimo. Assim, se o valor líquido desse cálculo for insuficiente para o desconto do empréstimo, será realizado o desconto parcial.

Cenário 02 - Informando verbas no parametrizador da folha de pagamento, etapa "Folha Normal | Eventos do Crédito do Trabalhador" -  Vamos considerar que no parametrizador tenha sido informado somente a verba de "Dias trabalhados", por exemplo. O sistema considerará esse evento menos INSS e IRRF. Sendo assim, provavelmente terá valor suficiente para o desconto do total do empréstimo. Nesse caso, os outros descontos, independente de quais forem, ou seja, até mesmo a pensão alimentícia, ficam com o líquido que restou do movimento do funcionário. Pode ser que esse líquido tenha vários descontos e gere arredondamentos a serem descontados no próximo movimento do funcionário que houver saldo.

#### **06 - Provisão do Empréstimo - Crédito do Trabalhador**

**06.001 - Qual a função do provisionamento no adiantamento? É obrigatório realizar a provisão?**

Não é obrigatório. O provisionamento serve para reservar um saldo no pagamento do funcionário, evitando líquidos zerados ou negativos ao realizar o desconto do empréstimo.   
Para realizar o provisionamento no adiantamento, é necessário marcar o parâmetro "Lançar Provisionamento do Empréstimo do Crédito do Trabalhador eSocial" no grupo de eventos.  
Veja mais detalhes no TDN:

**06.002 - Qual a função do provisionamento de férias? É obrigatório realizar a provisão?**

Não é obrigatório. Para lançar a provisão do empréstimo Crédito Trabalhador nas férias deve marcar o parâmetro "Lança provisionamento do empréstimo Crédito Trabalhador nas férias" no menu No menu Configurações | Parametrizador | Férias | Empréstimos.   
O lançamento do valor referente a provisão do empréstimo Crédito Trabalhador nas férias do funcionário deverá ser realizado automaticamente por meio do cálculo das férias, acessado pelo menu Administração de Pessoal | Funcionários | Movimento | Férias.   
Veja mais detalhes no TDN:

#### **07 - Rescisão - Crédito do Trabalhador**

**07.001 - Como será o desconto do emprestimo na rescisão??**

Será descontado o valor da parcela conforme arquivo importado, levando em consideração a margem consignável para limitar o desconto. Não será descontado o valor total do emprestimo, somente a parcela mensal.

**07.002 - Como fazer em caso de desligamentos realizados antes da importação do arquivo (Portal Emprega Brasil)?**

Conforme manual Operacional do Empregador, existem algumas regras conforme abaixo:

Situação 1 – Desligamento anterior à competência de referência: Se o trabalhador for desligado antes do início da competência de referência para o desconto da primeira parcela do empréstimo consignado, não deve haver escrituração do consignado no eSocial, nem de retenção de salário, tampouco de pagamento da parcela, ainda que os dados do contrato constem no Portal Emprega Brasil.   
Situação 2 – Desligamento na competência de referência ou na competência seguinte: Se o desligamento ocorrer na primeira competência de referência para desconto da parcela ou na competência imediatamente subsequente, o empregador deverá adotar os procedimentos correspondentes ao empréstimo consignado do Programa Crédito do Trabalhador. A depender da data de desligamento, poderá ser necessário realizar o desconto em folha e o recolhimento daparcela em uma ou duas competências distintas.

**07.003 - Verbas de 13º entram no cálculo da margem na rescisão?**

Não, conforme MP verbas de 13° salário não podem sofrer desconto referente ao credito do trabalhador.

#### **08 - eSocial - Crédito do Trabalhador**

**08.001 - A planilha de empréstimo está trazendo o número do contrato com mais de 12 dígitos, mas no layout do eSocial o limite era de 12. Existe alguma orientação sobre isso?**

De acordo com a última Nota Técnica do eSocial, o campo "número do contrato" foi ampliado para até 15 posições. Recomendamos que verifique se o seu schema está atualizado conforme a versão mais recente. Para mais detalhes, consulte a documentação no seguinte [Link](https://centraldeatendimento.totvs.com/hc/pt-br/articles/31996414541975-RH-RM-FOP-eSocial-Erro-de-Schema-nrDoc-na-transmiss%C3%A3o-dos-eventos-S-2299-S-1200-com-o-Governo).

**08.002 -  Poderiam informar quais são as naturezas de rubricas corretas do eSocial que devem ser utilizadas nos eventos relacionados ao Crédito do Trabalhador, incluindo provisões, proventos, descontos e códigos de cálculo como 481, 482, 483 e 484? Além disso, todos os eventos criados precisam ter rubrica vinculada?**

Todos os eventos criados precisam ter natureza de rubrica, pois é uma informação obrigatória no XML do "S-1010 - Tabelas de Rubricas".

A partir do Leiaute S-1.3 do eSocial, foi disponibilizada a natureza de rubrica "**9253 - Empréstimos eConsignado - Desconto**" para diferenciar a rubrica de desconto do Crédito do Trabalhador dos demais empréstimos consignados. Sendo assim, essa natureza deve ser utiliza no evento de CC 480, visto orientação do Governo. Contudo, as demais verbas não possuem orientação direta do Governo quanto às naturezas de rubrica, sendo assim, fica à cargo do usuário do sistema definir a natureza que entende mais adequada.

A TOTVS não orienta a natureza de rubrica a ser utilizada em cada verba, mas sugerimos validar o [Manual de Orientação do Empregador](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-operacional-do-empregador-programa-credito-do-trabalhador-v2-16-05-25.pdf) em que, a partir da página 27 (item **5.2.1 Exemplos de Apuração da Remuneração Disponível**) contam exemplos de cálculos, apresentando algumas naturezas também.

**08.003 - O evento de desconto do Crédito do Trabalhador tem incidência de FGTS ou não?**

Na geração do eventoS-1010, quando o campo *`PEVENTO.NATRUBRICA`* está preenchido com o valor 9253, o sistema envia o código "**31 - Desconto consignado**" na tag *`codIncFGTS`*. Ou seja, há sim incidência de FGTS conforme essa configuração.

**08.004 - Os valores descontados, com as rubricas devidamente parametrizadas, serão enviados automaticamente ao eSocial por meio do evento S-1200? E a guia será emitida separadamente?**

Sim, os valores descontados devem ser informados ao eSocial por meio do evento **S-1200**, conforme orientações disponíveis na [DT - Crédito do Trabalhador - eSocial](https://example.com).  
A emissão da guia não é feita automaticamente: ela deve ser **escriturada manualmente no FGTS Digital**, conforme descrito no item **4.4.1 – Geração de Guias no FGTS Digital** do **Manual do Crédito do Trabalhador**.

**08.005 - Os eventos que não possuem natureza de rubrica precisam ser enviados para o eSocial?**

Nem todos os eventos precisam ser enviados ao eSocial. Foram criados os seguintes códigos de cálculo para viabilizar o funcionamento do Crédito do Trabalhador:

* **Eventos que devem ser enviados ao eSocial** (por serem do tipo *desconto* ou *provento* e afetarem o valor líquido):

  + 480 – Desconto Empréstimo Crédito do Trabalhador
  + 481 – Provisão Empréstimo Crédito do Trabalhador Folha
  + 484 – Provento Provisão Empréstimo Créd.Trab.Folha
  + 485 a 489 – Eventos de Provisão para Férias e Adiantamento
* **Eventos que não precisam ser enviados ao eSocial**, por serem apenas utilizados como base de cálculo:

  + 482 – Remuneração Base Empréstimo Crédito do Trabalhador
  + 483 – Insuficiência de Saldo Empréstimo Crédito do Trabalhador

Esses eventos de base podem ser desconsiderados na geração dos eventos para o eSocial.

**08.006 - Em caso de insuficiência de saldo do Crédito do Trabalhador, o valor será descontado no mês seguinte ou informado no eSocial?**

Conforme orientações do Manual do Crédito do Trabalhador, a insuficiência de saldo não deve ser automaticamente descontada no mês seguinte nem enviada ao eSocial. Nesses casos, o trabalhador deve ser notificado para renegociar diretamente com a instituição financeira.

Mensagem sugerida ao trabalhador:

> **ATENÇÃO TRABALHADOR:** Não foi possível realizar o desconto total ou parcial do seu empréstimo consignado, por exceder o percentual (35%) da remuneração disponível, conforme a Lei nº 10.820/2003 e a Portaria MTE nº 435/2025. Procure sua instituição financeira para regularizar o pagamento desse empréstimo.

Essa orientação está descrita no **Exemplo 02 – Página 28** do Manual do Crédito do Trabalhador.

**08.007 - Mesmo após a atualização do sistema, ainda é necessário criarmos manualmente as tabelas e os eventos de rubricas?**

A rubrica **9253 - Empréstimos eConsignado - Desconto** será criada automaticamente por meio do RM.Atualizador.exe. Após a criação, será necessário apenas associá-la ao evento correspondente.

Para mais detalhes sobre as parametrizações, acesse: [Documentação TOTVS - Crédito do Trabalhador](https://tdn.totvs.com/pages/viewpage.action?pageId=925361639)

**08.008 - Quando a transmissão do eSocial ainda é feita via TAF (com o middleware não ativado), como deve ser feita a integração com a instituição financeira? Onde essa informação deve ser cadastrada no TAF?**

Não é necessário cadastrar, precisa apenas atualizar atualizar a tabela a partir do pacote informado no [Link](https://tdn.totvs.com/pages/releaseview.action?pageId=942050358) .

#### **09 - Erros/Dúvidas Comuns x Soluções**

**09.001 - Ao enviar o S-1200 e/ou S-2299 ocorre o erro de schema: Element '{<http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00}nrDoc>': [facet 'pattern'] The value 'xxxxxxxxxxxxxxx' is not accepted by the pattern '\d{8,12}'.**

O erro ocorre devido aos *Schemas* do TSS estarem desatualizados, não estando em conformidade com a versão do leiaute S-1.3 NT 03/2025. Os novos Schemas aceitam na tag nrDoc 15 dígitos no número do contrato do empréstimo do Crédito do Trabalhador. Siga as orientações da documentação abaixo para **atualizar os *Schemas* do TSS**, e após conclusão, reenviar o evento S-1200/S-2299. **Obs**.: Tanto clientes Middleware quanto clientes TAF Full precisam atualizar o TSS.

[Cross Segmentos - TSS - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552)

**09.002 - Ao realizar a importação do arquivo do Portal Emprega Brasil, os valores do empréstimo ficaram incorretos.**

Geralmente este problema ocorre devido ao separador do arquivo de importação estar incorreto. O arquivo exportado no Portal Emprega Brasil apresenta o caractere "," enquanto o RM considerava o caractere "." gerando assim divergência de valores na importação. Para ajuste, é necessário **atualização do Patch** conforme disponibilização abaixo na [Central de Downloads](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/searchAll) do Portal do Cliente. Com a atualização, o sistema fará a conversão automática dos caracteres passando a importar corretamente os valores.  
*- 12.1.2502.150*  
*- 12.1.2410.238*  
*- 12.1.2406.280*

[Como realizar atualização de patches da biblioteca](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004983291)

**Obs**.: Cliente CLOUD - Solicite atualização do seu ambiente abrindo um novo Ticket para a equipe Cloud RM ou, caso possua acesso ao TCloud, realize a atualização seguindo a documentação a seguir: [Atualizar Patch do RM via T-Cloud](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035834573)

**09.003 - Observei que no arquivo do Portal Emprega Brasil os números de CPF e CNPJ estão sem os zeros à esquerda. Qual procedimento realizar para ajuste?**

O Ministério do Trabalho e Emprego divulgou um comunicado aos empregadores alertando um ajuste técnico necessário nos arquivos disponibilizados no Portal Emprega Brasil. Esses arquivos contêm os contratos de empréstimos consignados averbados entre 21 de março e 20 de abril de 2025, cujas parcelas devem ser descontadas na folha de pagamento de maio. No entanto, foi identificado que alguns registros apresentaram o campo de CPF dos trabalhadores **sem os zeros à esquerda**, o que resultou em CPFs com menos de 11 dígitos.

O MTE orienta os empregadores a ajustarem esses CPFs, inserindo os zeros à esquerda, para garantir que o número tenha a formatação correta. Além disso, o código da instituição financeira consignatária, presente nos arquivos, deve ser mantido exatamente como consta, preservando qualquer zero à esquerda, e não deve ser substituído por códigos de outras fontes.

Veja orientação completa no documento a seguir: Crédito do Trabalhador : [CPF/CNPJ dos trabalhadores sem os zeros à esquerda](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32044630941975)

**09.004 - Ao realizar a importação do arquivo do Portal Emprega Brasil é apresentada a mensagem de erro "Erro na leitura do Excel: [ diretório\arquivo.xlsx ] Mensagem: Falha na recuperação de fábrica de classes COM do componente com CLSID {xxxxxxxxxxxxxxx} devido ao seguinte erro: 80070005 Acesso negado. (Exceção de HRESULT: 0x80070005 (E\_ACCESSDENIED)). - não está instalado no servidor". Como resolver?**

Para este erro é necessária atualização do Patch conforme disponibilização abaixo na [Central de Downloads](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/searchAll) do Portal do Cliente.  
<https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/searchAll>  
    *- 12.1.2502.150*  
*- 12.1.2410.238*  
*- 12.1.2406.280*

[Como realizar atualização de patches da biblioteca](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004983291)

**Obs**.: Cliente CLOUD - Solicite atualização do seu ambiente abrindo um novo Ticket para a equipe Cloud RM ou, caso possua acesso ao TCloud, realize a atualização seguindo a documentação a seguir: [Atualizar Patch do RM via T-Cloud](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035834573)

**09.005 - Ao realizar o lançamento de verbas pelo Grupo de Eventos é apresentada mensagem "Chapa XXXX: Parcela do empréstimo EMPT0000002 não foi lançada porque o evento XXXX já existe no envelope". Como resolver?**

O erro ocorre pois o evento informado para compor a base de cálculo da remuneração do crédito trabalhador já está presente no envelope de pagamento, lançado por outro meio — como grupo de eventos, eventos adicionais ou códigos fixos. Quando o mesmo evento é incluído novamente via parametrizador do crédito trabalhador, o sistema impede o lançamento duplicado para evitar inconsistências. Veja orientações de ajuste na documentação a seguir: [Crédito do Trabalhador - Chapa XXXX: Parcela do empréstimo não foi lançada porque o evento XXXX já existe no envelope](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32422106756119)

**09.005 - Como será o lançamento financeiro dos eventos do Credito do Trabalhador?**

Para geração de Títulos de Lançamentos Financeiros, o mesmo pode ser customizado por fórmula, onde a mesma irá retornar o valor do evento. Conforme exemplificado no item 01 do tdn:
