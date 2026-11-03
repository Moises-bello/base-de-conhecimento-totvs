---
content_hash: bd75a21063b07174220313d7d8f2427d92b5c3c14ad3642c6d556b0e1323e3a1
fetched_at: '2026-06-29T00:10:27.631149+00:00'
page_id: '516629933'
product: rm
source: tdn-rm
title: Prontuário do Paciente CIH
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=516629933
version: 10
---

LGPD - Lei Geral de Proteção de Dados

Informamos que os dados pessoais contidos nesta entidade foram colhidos para emissão de documentos fiscais e geração de rotinas legais e são retidos por determinação legal de normas fiscais e de transparência. Os mesmos não poderão ser eliminados em virtude de obrigação legal de retenção. O cumprimento de obrigação legal é hipótese legítima do tratamento dos seus dados conforme a Lei Geral de Proteção de Dados Pessoais (Lei n° 13.709/2018).

Para mais informações sobre a LGPD e as soluções oferecidas pela TOTVS consulte nossa página neste link ([https://tdn.totvs.com/pages/releaseview.action?pageId=514427789](https://tdn.totvs.com/pages/releaseview.action?pageId=514427789 "Follow link")).

## **01. PROCESSOS E ANEXOS**

## **02. VISÃO GERAL**

A manutenção dos dados pessoais dos pacientes que têm passagem pela instituição é realizada, via lançamento manual, ou importação de dados do sistema de gestão hospitalar. Este item deve ser usado apenas para manutenção de pacientes que são **internados** na instituição. Os pacientes externos terão seu registro no sistema por meio do item de registro de População (Admissões).   
Lembre-se: o prontuário é o identificador do paciente dentro do sistema, portanto, deve ser único para cada um.

## **03. EXEMPLO DE UTILIZAÇÃO**

Saúde > controle de infecção hospitalar > paciente

## **04. TELA INICIAL**

**Outras Ações / Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| Procedimento para inclusão | 1. Após acessar o sistema, clique em **Paciente/Paciente**. 2. Será exibida a tela de filtro, nela preencha o nome do paciente. 3. Clique em **OK**. 4. Caso mais de um paciente corresponda ao nome informado, serão listados na tela de Prontuário. 5. Dê duplo clique sobre o prontuário que deseja acessar. 6. Será exibido o Prontuário do paciente selecionado. 7. Na opção **Paciente,** clique em "+''. 8. As opções de menu do Prontuário serão expandidas, basta clicar sobre elas para acessá-las. |

## **05. TABELAS UTILIZADAS**

* **O que é o item Internações?**

Através desse item é possível visualizar em relatórios BI, quais foram os tipos de passagem do paciente pelo hospital, identificando a sua Unidade Clínica com as suas respectivas movimentações e procedimentos.

* **O que é item Procedimentos Invasivos?**

Nesse item estão registrados os procedimentos invasivos relativos à internação do paciente e seu período.

* **O que é o item Antibiótico?**

Todo o histórico de consumo de antibiótico do paciente internado é registrado nesse item. Só tem valor epidemiológico o consumo de antibiótico em pacientes internados e, por isso, o sistema não acompanha consumo de antibiótico de pacientes antes ou após seu período de internação na instituição.  Nele são registradas todas as dispensações feitas pela farmácia da instituição, viabilizando o cálculo de dosagem total consumida pelo paciente e tempo de consumo do antibiótico.  
Neste item pode haver o registro do motivo da prescrição médica, que pode ser para tratar uma infecção, uma profilaxia cirúrgica ou por indicação clínica. Também pode-se detalhar o motivo, com a opção de definir o tipo de profilaxia e o tipo de infecção para o qual o medicamento foi prescrito.  Caso a prescrição tenha sido feita para tratar uma infecção deverão ser informados em quais sítios de infecção os antibióticos prescritos irão atuar.   
É possível relacionar a prescrição de antibiótico com os resultados de cultura e as infecções hospitalares registradas no período de internação do paciente na instituição e até 365 dias da Internação. As prescrições importadas ficam com o estado "a validar", para que a equipe da CIH possa saber quais prescrições estão carentes de dados epidemiológicos e informá-los.   
A consistência no lançamento ocorre quando há lançamento de antibiótico terapêutico para o tratamento de uma infecção hospitalar (IH) exigindo-se o lançamento do sítio secundário da infecção.   
O sistema continua permitindo a classificação de um antibiótico terapêutico para infecção comunitária sem o lançamento do sítio secundário. Todavia, caso a indicação de antibiótico seja terapêutica e o tipo de infecção seja Hospitalar, deve se incluir pelo menos um sítio secundário.   
O sistema automatiza a classificação dos antibióticos profiláticos em conformidade com as cirurgias realizadas e protocolo de antibioticoprofilaxia do hospital. As culturas são classificadas automaticamente a partir dos cadastros de antibióticos e de infecções hospitalares.

* **O que é o item Cultura Final?**

Nessa opção são registrados os resultados de exames laboratoriais, coletados no período de internação do paciente na instituição, com ou sem crescimento bacteriano e antibiograma.  
Caso o resultado aponte crescimento bacteriano no material colhido, deve ser informada a relevância clínica do resultado obtido. A relevância pode ser:

* Patogênica: caso o germe seja infectante e, neste caso, deve ser informado qual o tipo da infecção (Hospitalar ou Comunitária) e seu sítio.
* Colonizante/ Contaminante: caso o germe seja nativo da flora do paciente.
* Vigilância Epidemiológica: caso o exame tenha sido pedido para tal fim.

A data da cultura corresponde à data da coleta do material de cultura. É possível relacionar o resultado da cultura com as prescrições de antibiótico e as infecções hospitalares registradas no período de internação do paciente na instituição.   
Os exames laboratoriais importados ficam com o estado "a validar", para que a equipe da CCIH possa saber quais exames estão carentes de dados epidemiológicos e informá-los.

* **O que é o item Cultura Parcial?**

Neste item é realizado o acompanhamento dos exames laboratoriais, coletados no período de internação do paciente na instituição desde a coleta do material até seu resultado. Nas atualizações é possível fazer o acompanhamento do crescimento bacteriano no material colhido.

O registro de uma Cultura Parcial, só será possível, nas seguintes condições:

1. Quando a data/hora da coleta for anterior à internação ou posterior a alta, o sistema não deverá permitir salvar o registro e criticar através de uma mensagem;
2. Quando a data/hora da coleta estiver dentro do período da internação (maior ou igual à internação e menor ou igual a alta) deixar registrar com a hora digitada (hoje o sistema está substituindo a hora digitada por 23:59)
3. Quando a data da coleta for no mesmo dia da internação ou da alta, obrigar o usuário digitar a hora da coleta (somente na mesma data de internação ou alta) e após digitar fazer a consistência da opção 1.

* **O que é o item Cirurgia?**

Nessa opção são registradas as intervenções cirúrgicas as quais o paciente é submetido em seu período de internação. Este item suporta dados referentes à cirurgia, às vias de acesso, à ferida cirúrgica, aos cirurgiões, procedimentos cirúrgicos, anestesista e anestesia e ASA. Por meio dele também, é possível registrar:

* Infecções cirúrgicas.
* Risco cirúrgico, que é uma pontuação baseada na natureza do procedimento e na condição clínica pré-operatória do paciente.
* Tempo de ferida aberta, por via de acesso.
* Tipo de ferida, também por via de acesso, que é uma variável usada no cálculo do IRIC.

O IRIC é um preditor de infecção em sítio cirúrgico baseado no risco cirúrgico, no tipo de ferida e no tempo de cirurgia, que é calculado pelo sistema através desta opção.   
As cirurgias importadas ficam com o estado "a validar", para que a equipe da CCIH possa saber quais cirurgias estão carentes de dados epidemiológicos e informá-los.

* **O que é o item Infecção?**

Neste item estão registradas as infecções hospitalares, comunitárias ou de outras instituições. Podem ser registradas infecções até 365 dias após a alta Hospitalar.   
Para que se possa registrar uma infecção hospitalar relacionada à cirurgia é necessário cadastrar a cirurgia antes da infecção e para que se possa registrar uma infecção hospitalar relacionada aos procedimentos invasivos é necessário informar antes a internação. As infecções cirúrgicas também podem ser registradas a partir do item de cirurgia do sistema.   
É possível relacionar a infecção hospitalar com os resultados de cultura e com as prescrições de antibiótico registradas no período de internação do paciente na instituição.

No momento da inclusão de infecção, se o paciente estiver na unidade por menos de 48hs, será sugerida a unidade clínica anterior a transferência, a partir de 48hs, será sugerida a unidade clínica atual. 

* **O que é o item Eventos Adversos?**

Eventos adversos são incidentes que resultam em danos à saúde decorrentes do cuidado prestado aos pacientes, não atribuídas à evolução natural da doença de base. Os eventos adversos não infecciosos que ocorrem na instituição no período de internação do paciente estão registrados neste cadastro, assim como seu motivo/ consequência.

* **O que é o item Apache II?**

O APACHE I (Acute Physiology and Chronic Health Disease Classification System II) é um escore clínico para predição estimada de mortalidade em pacientes adultos com passagens em unidades de terapia intensiva na instituição.   
Tal predição é obtida com base em variáveis clínico-laboratoriais do paciente obtidas nas primeiras 24 horas de internação nas unidades de terapia intensiva. Essas variáveis são convertidas em pontos e o total deles é utilizado em uma equação de regressão logística para obter a probabilidade de óbito. Deve ser informada a pior condição de cada variável durante o período das primeiras 24 horas de internação. 

* **O que é o item CRIB?**

O **Índice Clínico de Risco para Recém-nascidos** (Clinical risk index for babies - CRIB) é um instrumento para avaliar o risco na admissão de gravidade da doença, que inclui o peso ao nascer, idade gestacional, presença de malformações congênitas, excesso máximo de bases e frações máxima e mínima de oxigênio inspirado. Com estes critérios pode-se estimar a probabilidade de óbito do RN.

* **O que é o item PRISM?**

Trata-se de escore preditor de mortalidade em pacientes pediátricos sendo utilizado para comparar e avaliar a resolutividade e utilização de recursos terapêuticos em unidades de terapia intensiva pediátricas (UTIP).

* **O que é o item EuroScore?**

O EuroScore é um modelo de estratificação de risco com a finalidade de prever a mortalidade na cirurgia cardíaca.   
Cada paciente é avaliado quanto à presença ou não dos fatores de risco estabelecidos pelo EuroScore, respeitando-se a definição de cada um deles e atribuindo-lhes o peso apropriado.   
A estratificação de risco permite estimar o risco operatório a ser enfrentado por determinado indivíduo e tem grande importância na análise retrospectiva dos resultados cirúrgicos, permitindo a comparação não só entre instituições, como também entre cirurgiões individualmente.
