---
content_hash: d273bf90af696347373cb4ab5896be38d0a9062e5dd9e030e04568dfdd2fc767
fetched_at: '2026-06-29T00:10:16.458873+00:00'
page_id: '469451357'
product: rm
source: tdn-rm
title: S-2240 - Condições Ambientais do Trabalho - Fatores de Risco
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=469451357
version: 42
---

Este evento tem a finalidade de registrar e indicar as condições ambientais de trabalho do trabalhador, indicando a prestação de serviços nos ambientes de trabalho, assim como informar a exposição aos fatores de riscos constantes na Tabela 24 – Fatores de Risco e Atividades – Aposentadoria Especial. E nesse evento também é informado se a exposição aos fatores de risco, cria condições de insalubridade ou periculosidade no ambiente de trabalho, assim como possibilita o dever de recolhimento adicional para financiamento de aposentadoria especial.

Para o envio do evento é necessário que os eventos S-2190 (ou, alternativamente, do S-2200) ou do S-2300 já constem na base do governo. O envio do registro inicial desse evento é até o dia 15 (quinze) do mês subsequente ao início da obrigatoriedade dos eventos de SST ou do ingresso/admissão do trabalhador, e no caso de registros de alteração do inicial, devem ser enviados até o dia 15 (quinze) do mês subsequente à alteração.

**GERAÇÃO DOS REGISTROS**

Através do processo de geração de gatilhos iniciais o evento será gerado para todos os funcionários da coligada selecionada. O arquivo levará as informações dos funcionários, considerando os ambientes de trabalho, riscos, atividades periculosas e EPI’s/EPC’s vinculados direta e indiretamente ao funcionário.

**CONFIGURAÇÕES PRÉVIAS NECESSÁRIAS**

No módulo TOTVS Segurança e Saúde Ocupacional:

**Validação da Profissiografia**

Com base no tipo de prossiografia utilizado, será enviadas as informações da descrição da atividades realizadas pelos funcionários. Para avaliar acesse o menu: Opções | Parametrizador | Profissiografia 

**Atividades Desempenhadas e Atividades Periculosas e Insalubres**

Com base no(s) tipo(s) de profissiografia selecionado(s), a descrição das atividades desempenhadas pelo funcionário e as atividade periculosas e Insalubres deve ser preenchida, de acordo com a tabela 24-Fatores de Risco e Atividades – Aposentadoria Especial., as atividades desempenhadas pelo funcionário.

A informação da atividade periculosa e insalubre, seguirá a profissiografia informada no parametrizador, podendo ser por: Função, Quadro de Lotação, Funções do Posto de Trabalho, Tarefas da função, Tarefas do Quadro de Lotação, Tarefas das Funções do Posto de Trabalho e/ou Tarefas do Funcionário. **Caso não seja encontrada correspondência de atividades periculosas ou insalubres, o sistema  atribuirá o código de ausência de correspondência no momento da geração do XML.**

**Função**

Acesse o menu Cadastros | Funções - Aba Outras Informações – Descrição para o PPP , para informar as atividades periculosas e Insalubre.

Para maiores informações acesse o link: [Funções - SMT](https://tdn.totvs.com/pages/viewpage.action?pageId=452719127)

**Quadro de lotação**  
Acesse o menu Cadastros | Funções e acesse a opção Anexos | Quadro de lotação, selecione e edite uma lotação desejada e a descrição vai estar disponível na aba Informação sobre a função e Atividades para as atividades periculosas e Insalubre:  
  
  
  
Para maiores informações acesse o link: [Quadro de Lotação da Função](https://tdn.totvs.com/pages/viewpage.action?pageId=452719127)

**Funções do Posto de Trabalho**  
Acesse o menu Cadastros | Postos de Trabalho e selecione o posto desejado e acesse a opção Anexos | Funções vinculadas ao posto de trabalho e descreva a atividade na identificação campo descrição e na aba atividades eSocial, para informar as atividades periculosas e Insalubre.  
  
  
**OBSERVAÇÃO:** O posto de trabalho que está situado no menu Cadastros serve como um agrupador de funções para localização, do funcionário na empresa dada suas funções. Nesse cadastro é importante relacionar funções nos anexos. Esses postos poderão depois ser vinculados ao funcionário de acordo com sua função.

**Tarefas**  
O cadastro geral das tarefas é realizada no modulo de Gestão de Pessoas, dessa forma acesse o menu Gestão Organizacional | Tarefas e selecione e edite um tarefa e na aba identificação informe as atividades no campo descrição e na aba atividades para informar as atividades periculosas e Insalubre.

Para maiores informações acesse o link: [Tarefas](https://tdn.totvs.com/display/LRM/Tarefas+-+RHU)

Após informar a atividade eSocial à tarefa é necessário vincular a tarefa por funcionário, função, lotação ou posto de trabalho através do assistente de gerenciamento de tarefas do menu Gestão Organizacional | Administração de Tarefas.

Para maiores informações acesse o link: [Administração de tarefas](https://tdn.totvs.com/pages/viewpage.action?pageId=452720055)

**Tipos de Agentes**

No cadastro do tipo de agente é necessário informar um código de agente nocivo e uma descrição ao qual o funcionário esteja exposto de acordo com a Tabela 24 do eSocial (Fatores de Risco e Atividades – Aposentadoria Especial). Menu PPRA | Tipos de Agentes.

**OBSERVAÇÃO:** Para o caso onde não houver Fator de Risco, não deverá criar o tipo de agente. Na geração do evento S-2240 o sistema irá informar automaticamente a Ausência de Agente Nocivo (Anexo IV do Decreto 3.048/1999). Código 09.01.001.

**Riscos**

No cadastro do risco é necessário informar um tipo de agente nocivo que já esteja vinculado a tabela 24, com base no Tipo de Agente Nocivo bem como mapear os EPI ‘s e EPC ‘s necessários. Menu PPRA | Riscos.

Aqui será necessário preencher o ‘Tipo de Agente Nocivo’. Após essa definição, acessar o Anexo EPI/EPC e informar os EPI ‘s aqui e é importante que a flag "Eficaz" esteja marcada. Vale também informar que no risco há os níveis de risco que podem ter EPI‘s específicos e segue a mesma regra.

Para maiores informações acesse o link: [Riscos](https://tdn.totvs.com/display/LRM/Risco)

**Responsável pelos Registros Ambientais**

São as informações do responsável pelos registros ambientais. Menu PPRA | Resp. Reg. Ambientais.

Para o envio ao eSocial é obrigatório o envio do CPF (Cadastro no Registro da Pessoa), NIS, nome, Órgão de Classe, Número de Inscrição no Órgão de Classe e UF do órgão de Classe. Este responsável pode ser responsável por toda a coligada (caso não seja informada seção e filial), para uma filial (caso não seja informada a seção) ou até mesmo para uma seção. Para maiores informações acesse o link:  
[Responsável pelos Registros Ambientais](https://tdn.totvs.com/pages/viewpage.action?pageId=452718849)

****EPIs e EPCs****Caso utilizem EPIs ou EPCs é necessário que o registro cadastrado esteja definido como EPI ou EPC. Para validar acesse o menu EPI/EPC | Catálogo.

Em caso de EPI é necessário informar o CA ou Documento de Avaliação. Para o cadastro do CA ou Doc. Aval. será necessário que esteja válido e que o EPI/EPC esteja também dentro da validade. E ao fornecer um EPI flag "Eficaz" esteja marcada. Para maiores informações acesse os links: [Catálogo de EPI](https://tdn.totvs.com/pages/viewpage.action?pageId=452719192)  e  [Assistente para Fornecimento Automático de EPI](https://tdn.totvs.com/pages/viewpage.action?pageId=452719515).

****Avaliação de Riscos****A finalidade será identificar os riscos que o funcionário está exposto. Este cadastro serve como mapeamento. Importante dizer que somente ‘Avaliações’ são consideradas. É necessário também que ao criar uma avaliação sejam informados os campos de "Valor Quantitativo" ou "Valor Qualitativo" e a Unidade de Medida eSocial.

Após os cadastros prévios, deve cadastrar as  **avaliações/reconhecimentos de risco**. **Caso não haja avaliação de risco VIGENTE, o sistema irá considerar que não há fatores de riscos relacionados e consequentemente atribuirá ao mesmo o código de ausência de risco.** O cadastro da avaliação de risco e realizado no menu PPRA| Reconhecimento/Avaliação de Risco. Para maiores detalhes sobre o cadastro de reconhecimento/avaliação de risco acesse o link: [Reconhecimento e Avaliação de Risco](https://tdn.totvs.com/pages/viewpage.action?pageId=452719929)

**Observações relativas a registros ambientais**A finalidade será informar Observações Complementares referentes a registros Ambientais.

                                                                                                                                                                                                                                 

**ALTERAÇÕES QUE GERAM GATILHOS PARA O EVENTO S-2240:**

Para a geração dos gatilhos serão consideradas as seguintes alterações:

Registros unitários são aqueles que alteram apenas um funcionário por vez. São eles:

* **Funcionário**
  + Rescisão tipo Transferência
* **Alterações de Campos do Cadastro**
  + Alteração de Função
  + Alteração de Seção
* **Posto de Trabalho**

+ Vinculação e Desvinculação.

Registros Massivos são os registros que afetam um ou mais funcionários por alteração e consequentemente podem gerar vários registros na fila de eventos. São eles:

* **Alterações na Função** 
  + Incluir/Excluir um Quadro de Lotação
  + Alteração das Informações sobre a Função

+ Alteração na Descrição para o PPP
+ Anexo Quadro de Lotação

* **Atividades**
  + Inclusão/Exclusão de Atividade na Tarefa
  + Inclusão/Exclusão de Atividade ao Quadro de Lotação
  + Inclusão/Exclusão de Atividade na Função
  + Inclusão/Exclusão de Atividade nas Funções do Posto de Trabalho

* **Tarefas** 
  + Alteração na Descrição das Tarefas
  + Administração de Tarefas

* **Avaliações de Risco**

* + Inclusão/Exclusão/Alteração em Avaliações de Risco (alteração apenas dos campos pertinentes ao eSocial)

* **Riscos** 
  + Alteração no Tipo de Agente
  + Anexo EPI / EPC - Inclusão/Exclusão/Alteração
  + Anexo Níveis de Risco
  + Alteração no Limite de Tolerância
  + Anexo EPI Nível de Risco - Inclusão/Exclusão/Alteração

* **Tipo de Agente Nocivo** 
  + Alteração do Tipo de Agente Nocivo eSocial

* **EPI**

+ Alteração do CA ou Nome

* **Responsável pelos Registros Ambientais** 
  + Inclusão/Exclusão/Alteração de Responsáveis

* **Posto de Trabalho**

+ Vinculação e Desvinculação através do Assistente
+ Alteração na Descrição da Função do Posto

* **Alterações Globais de Campos do Cadastro**
  + Alteração global de Função
  + Alteração global de Seção

* **Alteração nas Observações Complementares referentes a registros Ambientais**  
  + Alteração no campo Observação

false

**ATENÇÃO:**

* Todas as alterações que geram gatilhos massivos serão geradas via *JobServer* em *background*.
* Quando existir duas alterações na mesma data, ambos os gatilhos serão gerados com a operação Inclusão. O controle de retificação da tag <indRetif> será realizado na geração do XML.
