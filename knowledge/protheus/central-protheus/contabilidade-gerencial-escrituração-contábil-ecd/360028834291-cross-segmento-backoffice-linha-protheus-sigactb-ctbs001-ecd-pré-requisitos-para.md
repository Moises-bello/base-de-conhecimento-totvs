---
article_id: 360028834291
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 2c2a9f456aa1e03701f392fa859f60838823f0172a3b839c7680f116dae939fa
fetched_at: '2026-06-28T22:40:44.397260+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 - ECD Pré-requisitos
  para entrega
type: support-article
updated_at: '2024-05-06T19:49:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028834291-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-Pr%C3%A9-requisitos-para-entrega
---

**Dúvida**Quais os Pré-Requisitos e parametrização para entrega da ECD? 

**Ambiente**Cross Segmento - Backoffice Linha Protheus – Contabilidade gerencial – A partir da versão P12.1.25    
  
**Solução**

**Importante :** Caso não tenha visto a trilha de Geração do ECD, é recomendado que verifique primeiro a documentação**: [Trilha ECD LEIAUTE 9](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004099501-MP-SIGACTB-ECD-2021-Trilha-de-gera%C3%A7%C3%A3o-da-ECD-LAYOUT-9-?source=search)** e também que tenha realizado [**as Atualizações necessárias.**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025142372-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Pacote-de-atualiza%C3%A7%C3%A3o-e-como-realizar-a-atualiza%C3%A7%C3%A3o-da-ECD-2024-leiaute-9)

**1º** **Passo:** **Calendário Contábil Cadastrado** (CTBA010) conforme o período de apuração:

* [CADASTRO DE CALENDÁRIO CONTABIL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028525872-MP-SIGACTB-ECD-CADASTRO-DE-CALEND%C3%81RIO-CONTABIL?source=search)

**2º** **Passo:** **Cadastro do plano de contas** (CTBA020)

* Campos  tabela "CT1", CT1\_NATCTA ,CT1\_NTSPED ,CVN\_CLASSE e CVD\_NATCTA devem estar preenchidos: [COMO GERAR O REGISTRO I050: PLANO DE CONTAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022515312-MP-SIGACTB-ECD-COMO-GERAR-O-REGISTRO-I050-PLANO-DE-CONTAS-?source=search)
* O mapeamento para os planos de contas referenciais é facultativo, se optar por fazer o relacionamento segue link com modelos:  
  [Arquivos Modelos - Plano Referencial / Visões Gerenciais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006687252-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA161-Arquivos-modelos-Vis%C3%A3o-Gerencial?source=search)  
  Para importar veja [Como importar Plano referencial?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007547712-MP-SIGACTB-Como-importar-Plano-referencial-?source=search)

**3º** **Passo:** **Verifique o Cadastro do Contabilista** (CTBA015) :

* [CTBA015 REGISTRO J930: Identificação dos Signatários da Escrituração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020083171-MP-SIGACTB-ECD-CTBA015-REGISTRO-J930-Identifica%C3%A7%C3%A3o-dos-Signat%C3%A1rios-da-Escritura%C3%A7%C3%A3o?source=search)

**4º** **Passo:** **Verifique o****cadastro do participante** (CTBA016) :

* [CTBA016 Cadastro de Participantes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019986171-MP-SIGACTB-ECD-CTBA016-Cadastro-de-Participantes?source=search)**e  [Registro 0150: Tabela de Cadastro do Participante como gerar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023383752-MP-SIGACTB-ECD-Registro-0150-Tabela-de-Cadastro-do-Participante-como-gerar-?source=search)**

**5º** **Passo:** **Verifique o c****adastro da Visão Gerencial** (CTBA161), deve ser configurada por um analista in loco de acordo com a regra da empresa, temos disponíveis visões genéricas como modelo que podem ser alteradas;

* [Arquivos modelos Visão Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006687252-MP-SIGACTB-CTBA161-Arquivos-modelos-Vis%C3%A3o-Gerencial?source=search)
* [Como importar Visão Gerencial?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007545672-MP-SIGACTB-Como-importar-Vis%C3%A3o-Gerencial-?source=search)
* Através da rotina CTBA130 realize a[Amarração Visão Gerencial ao Livro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006908012-MP-SIGACTB-CTBA161-CTBA130-Amarra%C3%A7%C3%A3o-Vis%C3%A3o-Gerencial-ao-Livro?source=search)
* Verifique todos os pontos  [ECD : J150 ​](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028247351-MP-SIGACTB-ECD-J150-LAYOUT-6?source=search)  e  [ECD : J100](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023992791-MP-SIGACTB-ECD-J100?source=search)

Obs : Caso J150 esta sendo gerado desordenado verifique : [J100 e J150 MV\_GRVISOR ORDEM DA VISAO GERENCIAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026127292-MP-SIGACTB-ECD-J100-e-J150-MV-GRVISOR-ORDEM-DA-VISAO-GERENCIAL?source=search) e [RELATORIO J150 (DRE) NO PGE NÃO CORRESPONDE AO EMITIDO NO PROTHEUS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026626772-MP-SIGACTB-ECD-RELATORIO-J150-DRE-NO-PGE-N%C3%83O-CORRESPONDE-AO-EMITIDO-NO-PROTHEUS?source=search)

**6º Passo:** **Validações de ambiente**

* O compartilhamento das tabelas CTG, CTO, CQD e CTE estejam iguais [Compartilhamento de Tabelas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007377851-MP-SIGACTB-Compartilhamento-de-Tabelas-?source=search)
* O compartilhamento das tabelas CQ0, CQ1, CQ2, CQ3, CQ4, CQ5, CQ6, CQ07 CQ8, CQ9, CT2 e CTC. estejam iguais, conforme orientado no link [MP - SIGACTB: Como realizar compartilhamento de tabelas no Contabilidade Gerencial (SIGACTB)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018270032-MP-SIGACTB-Como-realizar-compartilhamento-de-tabelas-no-Contabilidade-Gerencial-SIGACTB-?source=search)

**O compartilhamento das tabelas do CTB devem estar conforme** **Tabela De/Para das Tabelas CTx para CSx para elaboração ECD :**[TABELAS ECD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026989572-MP-SIGACTB-ECD-TABELAS-ECD?source=search)

* [Como alterar o compartilhamento de tabelas após bloqueio realizado a partir da LIB versão 20181015](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026077191-MP-SIGACTB-Como-alterar-o-compartilhamento-de-tabelas-ap%C3%B3s-bloqueio-realizado-a-partir-da-LIB-vers%C3%A3o-20181015?source=search)
* Verifique o tamanho dos campos "Conta contábil" ,"Centro de Custo", "Item Contábil" e "Classe Valor"   
  [ALTERAÇÃO DO TAMANHO DAS ENTIDADES CONTÁBEIS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015543251-MP-SIGACTB-ALTERA%C3%87%C3%83O-DO-TAMANHO-DAS-ENTIDADES-CONT%C3%81BEIS?source=search) e [Tamanho do campo código das entidades contábeis Adicionais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024401031-MP-SIGACTB-Alterar-o-tamanho-do-campo-c%C3%B3digo-das-entidades-cont%C3%A1beis-adicionais?source=search)e [GRUPO DE PERGUNTAS CTB211](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028526532-MP-SIGACTB-CTBA211-GRUPO-DE-PERGUNTAS-?source=search)

Os campos CTT\_CUSTO, CTD\_ITEM e CTH\_CLVL consultado via APSDU na tabela SX3 devem ter o mesmo tamanho do informado no respectivo grupo de campos.

**7º Passo:** **Conferência dos dados**  
Imprima no período que irá realizar a apuração e confira os dados dos relatórios, "Razão Contábil (CTBR400)", " Balancete(CTBR040)", "DRE (CTBR510)" e "Balanço Patrimonial (CTBR500)".

**8º Passo:** **Execução dos processos**

Verifique apuração de resultados foi executada e se as conta de receita e despesa foram zeradas, se precisar de auxilio veja: **[Como realizar a apuração de resultados no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005048472-MP-SIGACTB-Como-realizar-Apura%C3%A7%C3%A3o-de-resultados-dentro-do-Protheus)**

Observações adicionais sobre a apuração:

* Ao consultar a chave LP na rotina Dados Auxiliares CTB (CTBA007) deve conter 1 registro de apuração com final Z, para cada apuração, com montagem da **[CHAVE DE APURAÇÃO CTBA211](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024134092-MP-SIGACTB-CHAVE-DE-APURA%C3%87%C3%83O-CTBA211?source=search)**
* Caso a rotina de apuração não esteja sendo finalizada verifique a**[Limitação número documento na apuração de resultado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018247651-MP-SIGACTB-CTBA211-Limita%C3%A7%C3%A3o-n%C3%BAmero-documento-na-apura%C3%A7%C3%A3o-de-resultado?source=search)****e [Tabela Processadas na execução da apuração de resultado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360009345312-MP-SIGACTB-CTBA211-Tabela-Processadas-na-execu%C3%A7%C3%A3o-da-apura%C3%A7%C3%A3o-de-resultado?source=search)**

**9º Passo:** **Performance**

* **[Habilitar procedures dinâmica na geração da ECD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007132632-MP-SIGACTB-Habilitar-procedures-din%C3%A2mica-na-gera%C3%A7%C3%A3o-da-ECD?source=search)**
* Verifique todos os pontos descrito na documentação:  <http://tdn.totvs.com/pages/releaseview.action?pageId=235586425>

**10º Passo: Limpeza da tabelas da ECD**

Caso sua revisão esteja sendo gerada com informações já exclusa do cadastro e ou movimento  realize a **[LIMPEZA TABELA CSB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026508851-MP-SIGACTB-ECD-LIMPEZA-TABELA-CSB?source=search)**, posteriormente gere uma nova revisão.

**Erros mapeados:**

**[Como preencher os parâmetros para geração da ECD?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009296382-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Como-preencher-os-par%C3%A2metros-para-gera%C3%A7%C3%A3o-da-ECD-?source=search)**

[ECD: ERRO NA INCLUSÃO DE DADOS NA CSA e/ou CSB VIA PROCEDURE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027070511-MP-SIGACTB-ERRO-NA-INCLUS%C3%83O-DE-DADOS-NA-CSA-e-ou-CSB-VIA-PROCEDURE?source=search)

[ECD : I155 Pelo menos um dos campos (saldo inicial, total de débitos, total de créditos ou saldo final) deve conter valor diferente de zero.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028360771-MP-SIGACTB-ECD-I155-Pelo-menos-um-dos-campos-saldo-inicial-total-de-d%C3%A9bitos-total-de-cr%C3%A9ditos-ou-saldo-final-deve-conter-valor-diferente-de-zero-?source=search)

[I050 : 5 - NIVEL O plano de contas com todas as suas contas sintéticas e analíticas deve conter no mínimo 4 níveis (Resolução CFC 1299/2010).](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028148692-MP-SIGACTB-ECD-I050-5-NIVEL-O-plano-de-contas-com-todas-as-suas-contas-sint%C3%A9ticas-e-anal%C3%ADticas-deve-conter-no-m%C3%ADnimo-4-n%C3%ADveis-Resolu%C3%A7%C3%A3o-CFC-1299-2010-?source=search)

Se  o arquivo J100 e J150 estiver desordenado verifique o parâmetro  [MV\_GRVISOR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026127292-MP-SIGACTB-ECD-J100-e-J150-MV-GRVISOR-ORDEM-DA-VISAO-GERENCIAL?source=search)

Se o arquivo estiver correto , porem o validador apresenta desordena veja :[MP-SIGACTB-ECD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026626772-MP-SIGACTB-ECD-RELATORIO-J150-DRE-NO-PGE-N%C3%83O-CORRESPONDE-AO-EMITIDO-NO-PROTHEUS?source=search)

[RELATORIO J150 (DRE) NO PGE NÃO CORRESPONDE AO EMITIDO NO PROTHEUS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026626772-MP-SIGACTB-ECD-RELATORIO-J150-DRE-NO-PGE-N%C3%83O-CORRESPONDE-AO-EMITIDO-NO-PROTHEUS?source=search)

[ECD : J005 IND\_COD\_AGL ,VL\_CTA\_INI e IND\_GRP\_BAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028866271-MP-SIGACTB-ECD-J005-IND-COD-AGL-VL-CTA-INI-e-IND-GRP-BAL?source=search)

[ECD ERRO BLOCOS J150  7-VL\_CTA e I052 COD\_AGL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028548031-MP-SIGACTB-ECD-ERRO-BLOCOS-J150-7-VL-CTA-e-I052-COD-AGL?source=search)

[ECD ERRO BLOCOS J150  VALORES ZERADO 7-VL\_CTA e I052 COD\_AGL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028553812-MP-SIGACTB-ECD-ERRO-BLOCOS-J150-VALORES-ZERADO-7-VL-CTA-e-I052-COD-AGL?source=search)

[ECD I200 PORQUE NÃO ESTA CONSIDERANDO O NUMERO DO LOTE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025883891-MP-SIGACTB-ECD-I200-PORQUE-N%C3%83O-ESTA-CONSIDERANDO-O-NUMERO-DO-LOTE?source=search)

[ECD: Erro no validador registro I200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028621892-MP-SIGACTB-Erro-no-validador-registro-I200?source=search)

[ECD : J005 - Registro/Campo não informado ou invalido (No Balanço Patrimonial, o somatório do saldo final...)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028626232-MP-SIGACTB-ECD-J005-Registro-Campo-n%C3%A3o-informado-ou-invalido-No-Balan%C3%A7o-Patrimonial-o-somat%C3%B3rio-do-saldo-final-?source=search)

[ECD : I155 trás contas que tiveram movimentações em anos anteriores porém estão com saldos zerados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028711472-MP-SIGACTB-ECD-I155-tr%C3%A1s-contas-que-tiveram-movimenta%C3%A7%C3%B5es-em-anos-anteriores-por%C3%A9m-est%C3%A3o-com-saldos-zerados?source=search)

**Principais dúvidas:**

[Eventos ECD Responde](http://tdn.totvs.com/display/public/PROT/Eventos+ECD+Responde)

[Vídeos HOW TO (ECD, Apuração, Visão gerencial)](http://tdn.totvs.com/pages/releaseview.action?pageId=337362744)

[ECD LAYOUT 7 TRIMESTRAL UNIFICADA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025347591-MP-SIGACTB-ECD-LAYOUT-7-TRIMESTRAL-UNIFICADA-?source=search)

[ECD – LAYOUT 1 ao 6 Como gerar o arquivo da ECD com Apuração trimestral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016231592-MP-SIGACTB-ECD-LAYOUT-1-ao-6-Como-gerar-o-arquivo-da-ECD-com-Apura%C3%A7%C3%A3o-trimestral-?source=search)

[ECD CHATBOT COMO ACESSAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027658692--MP-SIGACTB-ECD-CHATBOT?source=search)

[ECF e ECD - Centralização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007125892-MP-SIGACTB-ECF-e-ECD-Centraliza%C3%A7%C3%A3o?source=search)

[ECD: Quais as principais dúvidas relacionadas a ECD?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018602251-MP-SIGACTB-Quais-as-principais-d%C3%BAvidas-relacionadas-a-ECD-?source=search)

[ECD: NÃO GERA REGISTROS I350 - I355 - I150 - I155](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016508952-MP-SIGACTB-N%C3%83O-GERA-REGISTROS-I350-I355-I150-I155?source=search)

[ECD : J150](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028247351-MP-SIGACTB-ECD-J150-LAYOUT-6?source=search)

[ECD : J100](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023992791-MP-SIGACTB-ECD-J100?source=search)

[ECD SPED CONTABIL TABELA E ROTINA Bloco K](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013554251-MP-SIGACTB-ECD-SPED-CONTABIL-TABELA-E-ROTINA-Bloco-K?source=search)

[ECD Layout 7 SPED Bloco K saldos consolidados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026403252-MP-SIGACTB-ECD-Layout-7-SPED-Bloco-K-saldos-consolidados?source=search)

[ECD Registro 0020: Escrituração Contábil Descentralizada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024400351-MP-SIGACTB-ECD-Registro-0020-Escritura%C3%A7%C3%A3o-Cont%C3%A1bil-Descentralizada?source=search)

[EXECAUTO ECD BLOCO K PARA EMPRESAS QUE NÃO ESTÃO NÃO SIGAMAT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028545311-MP-SIGACTB-EXECAUTO-ECD-BLOCO-K-PARA-EMPRESAS-QUE-N%C3%83O-EST%C3%83O-N%C3%83O-SIGAMAT-?source=search)

[ECD LAYOUT 7 COMO GERAR OS REGISTROS J200 J210 J215](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026412372-MP-SIGACTB-ECD-LAYOUT-7-COMO-GERAR-OS-REGISTROS-J200-J210-J215-?source=search)

[ECD 2019 : SITUAÇÃO ESPECIAL OCORRIDA DE MAIO A DEZEMBRO DE 2018](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022028772-MP-SIGACTB-ECD-2019-SITUA%C3%87%C3%83O-ESPECIAL-OCORRIDA-DE-MAIO-A-DEZEMBRO-DE-2018?source=search)

[ECD : J800 LAYOUT 7 COMO GERAR NOTA EXPLICATIVA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025129432-MP-SIGACTB-ECD-J800-LAYOUT-7-COMO-GERAR-NOTA-EXPLICATIVA?source=search)

[ECD COMO GERAR LANÇAMENTOS EXTEMPORANEOS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025053772-MP-SIGACTB-ECD-COMO-GERAR-LAN%C3%87AMENTOS-EXTEMPORANEOS?source=search)

[ECD NÃO GERA REGISTROS I250](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007337292-MP-SIGACTB-ECD-N%C3%83O-GERA-REGISTROS-I250?source=search)

[ECD COMO HABILITAR/GERAR DFC e DVA REGISTRO J800?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025891212-MP-SIGACTB-ECD-COMO-HABILITAR-GERAR-DFC-e-DVA-REGISTRO-J800-?source=search)

[ECD : J800 LAYOUT 7 COMO GERAR NOTA EXPLICATIVA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025129432-MP-SIGACTB-ECD-J800-LAYOUT-7-COMO-GERAR-NOTA-EXPLICATIVA?source=search)

[ECD-SIGACTB ECD REGISTRO I300 e I310](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026160292-MP-SIGACTB-ECD-SIGACTB-ECD-REGISTRO-I300-e-I310?source=search)

[ECD : J150 LAYOUT 6](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028247351-MP-SIGACTB-ECD-J150-LAYOUT-6?source=search)

[ECD I050 : 5 - NIVEL O plano de contas com todas as suas contas sintéticas e analíticas deve conter no mínimo 4 níveis (Resolução CFC 1299/2010).](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028148692-MP-SIGACTB-ECD-I050-5-NIVEL-O-plano-de-contas-com-todas-as-suas-contas-sint%C3%A9ticas-e-anal%C3%ADticas-deve-conter-no-m%C3%ADnimo-4-n%C3%ADveis-Resolu%C3%A7%C3%A3o-CFC-1299-2010-?source=search)

[ECD MOEDA FUNCIONAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025045771-MP-SIGACTB-ECD-MOEDA-FUNCIONAL?source=search)

[ECD VOCE ESCOLHEU A OPÇÃO DE ARQUIVO TRIMESTRAL. O CALENDÁRIO DEVE CONTER NO MAXIMO QUATRO PERÍODOS.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025128172-MP-SIGACTB-ECD-VOCE-ESCOLHEU-A-OP%C3%87%C3%83O-DE-ARQUIVO-TRIMESTRAL-O-CALEND%C3%81RIO-DEVE-CONTER-NO-MAXIMO-QUATRO-PER%C3%8DODOS-?source=search)

[ECD - POR QUE OCORRE VALIDAÇÃO: HELP: BALANCETE PARCIAL ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016597051-MP-SIGACTB-ECD-POR-QUE-OCORRE-VALIDA%C3%87%C3%83O-HELP-BALANCETE-PARCIAL-?source=search)

[ECD TODOS OS CAMPOS DA WIZARD ESTAO DESABILITADOS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025608451-MP-SIGACTB-ECD-TODOS-OS-CAMPOS-DA-WIZARD-ESTAO-DESABILITADOS?source=search)

[ECD ADVERTENCIA I200| FATO CONTABIL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016244152-MP-SIGACTB-ECD-ADVERTENCIA-I200-FATO-CONTABIL?source=search)

[ECD - 4-VL\_LCTO - REGISTRO I200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008353712-MP-SIGACTB-ECD-4-VL-LCTO-REGISTRO-I200?source=search)

[ECD A DATA DE LANÇAMENTO EXTEMPORANEO (I200 DT\_LCTO\_EXT) DEVE SER ANTERIOR À DATA DE INICIO DA ESCRITURAÇÃO.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025392431-MP-SIGACTB-ECD-A-DATA-DE-LAN%C3%87AMENTO-EXTEMPORANEO-I200-DT-LCTO-EXT-DEVE-SER-ANTERIOR-%C3%80-DATA-DE-INICIO-DA-ESCRITURA%C3%87%C3%83O-?source=search)

[ECD : Deve existir pelo menos um registro J100 (Balanço) e um J150 (DRE) para cada registro J005 (Demonstração Contábil) informado.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049318233-MP-SIGACTB-ECD-Deve-existir-pelo-menos-um-registro-J100-Balan%C3%A7o-e-um-J150-DRE-para-cada-registro-J005-Demonstra%C3%A7%C3%A3o-Cont%C3%A1bil-informado-?source=search)
