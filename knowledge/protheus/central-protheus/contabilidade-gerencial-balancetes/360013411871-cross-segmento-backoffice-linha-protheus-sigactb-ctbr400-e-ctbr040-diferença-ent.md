---
article_id: 360013411871
category: Contabilidade Gerencial - Balancetes
content_hash: 00afe92118502a915a80fc0ef0f69963fbe51cc56846a6bed1abc714c30b9b8c
fetched_at: '2026-06-28T22:41:04.214344+00:00'
product: protheus
section_id: 1500001537281
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBR400 e CTBR040 diferença
  entre os relatórios
type: support-article
updated_at: '2023-03-21T12:33:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013411871-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR400-e-CTBR040-diferen%C3%A7a-entre-os-relat%C3%B3rios
---

**Dúvida**Origem das informações nos relatórios CTBR400 e CTBR040.  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Solução**

Diferença entre relatório de movimento e relatório de saldo.

* Relatório de movimento: Razão contabil (CTBR400) - Considera a tabela CT2 para apresentação de movimentos e saldos;

Saldo anterior: utiliza funções internas onde carrega saldos das tabelas CQ´s;

Movimentos: Baseia-se nos movimentos existentes na tabela CT2 (CT2\_VALOR);

Saldo atual: Saldo Anterior + ou - Movimentos.

* + Relatório de saldo: Balancete (CTBR040) - Considera as tabelas CQ0,CQ1....CQ9, para apresentação de saldos.

Veja : [MV\_TPVALOR RELATÓRIO DE SALDO E RELATÓRIO DE MOVIMENTO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407458674327-MP-SIGACTB-MV-TPVALOR-RELAT%C3%93RIO-DE-SALDO-E-RELAT%C3%93RIO-DE-MOVIMENTO-?source=search)

Necessário verificar 

* se o compartilhamento das tabelas estão corretos
* As tabelas abaixo precisam obrigatoriamente possuir o mesmo modo de compartilhamento.:
* CTE, CTG, CQD,CTO,CTP
* Veja o compartilhamento das tabelas [CT2,CQ0,CQ1(..)CQ9, CTC,CTF, CTC,CV7,CV8, CVX, CVY, CVZ](http://tdn.totvs.com/display/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB) estão corretas
* Realize o procedimento [MP - SIGACTB - Saldos não estão sendo atualizados de forma online.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019534772-MP-SIGACTB-Saldos-n%C3%A3o-est%C3%A3o-sendo-atualizados-de-forma-online-?source=search)
* Confira o compartilhamento das tabelas [MP - SIGACTB: Reestruturação dos Saldos Contábeis](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018467872-MP-SIGACTB-Reestrutura%C3%A7%C3%A3o-dos-Saldos-Cont%C3%A1beis?source=search)
* Verifique se esta sendo preenchido [MP - SIGACTB - CTBA190 Campo Filial das tabelas CQ não estão sendo alimentadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018497311-MP-SIGACTB-CTBA190-Campo-Filial-das-tabelas-CQ-n%C3%A3o-est%C3%A3o-sendo-alimentadas-?source=search)
* Realize o reprocessamento de saldo [MP - SIGACTB - Reprocessamento não atualiza saldos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006689012-MP-SIGACTB-Reprocessamento-n%C3%A3o-atualiza-saldos?source=search) , da data que esta correta até a data de hoje [MP - SIGACTB - CTBA 190 Como realizar o reprocessamento de saldos no SIGACTB?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007452371-MP-SIGACTB-CTBA-190-Como-realizar-o-reprocessamento-de-saldos-no-SIGACTB-?source=search)

Valide se seu ambiente está com as ultimas atualizações disponíveis:  
**[Pacote Dicionário + Procedure](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777)**  
  
Em modo exclusivo:  
1º Reinicie o serviço.  
2º Desinstale as procedures existente em seu ambiente.  
3º Verifique se o sistema desinstalou do configurador.  
4º Verifique se o sistema [desinstalou do Banco](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019534772-MP-SIGACTB-Saldos-n%C3%A3o-est%C3%A3o-sendo-atualizados-de-forma-online-?source=search) antes de instalar novamente.  
5º Copie as procedures atualizadas na pasta system.  
6º Instale as procedures .  
7º Reinicie o serviço.  
  
**[Pacotes LIB](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/search/searchAll)**  
**[Pacotes DBAccess](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/search/searchAll)**  
[**Binário AppServer**](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/)  
[**Binário SmartClient**](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFSC/)

Segue abaixo documentações relacionadas :

[MP - SIGACTB - Como realizar a extração/impressão do Razão Contábil no PROTHEUS (CTBR400)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006683712-MP-SIGACTB-Como-realizar-a-extra%C3%A7%C3%A3o-impress%C3%A3o-do-Raz%C3%A3o-Cont%C3%A1bil-no-PROTHEUS-CTBR400-)

[MP - SIGACTB - CTBR400: Lentidão na impressão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006983291-MP-SIGACTB-CTBR400-Lentid%C3%A3o-na-impress%C3%A3o)

[MP - SIGACTB - Como realizar Apuração de resultados dentro do Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005048472-MP-SIGACTB-Como-realizar-Apura%C3%A7%C3%A3o-de-resultados-dentro-do-Protheus-)

[MP - SIGACTB - CTBA 190 Como realizar o reprocessamento de saldos no SIGACTB?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007452371-MP-SIGACTB-CTBA-190-Como-realizar-o-reprocessamento-de-saldos-no-SIGACTB-)

[MP - SIGACTB - Reprocessamento não atualiza saldos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006689012-MP-SIGACTB-Reprocessamento-n%C3%A3o-atualiza-saldos)

[MP - SIGACTB - Reprocessamento de Saldos: Erro na Chamado do Processo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115016125428-MP-SIGACTB-Reprocessamento-de-Saldos-Erro-na-Chamado-do-Processo)

[MP - SIGACTB - Saldo anterior zerado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115016115388-MP-SIGACTB-Saldo-anterior-zerado)

[MP - SIGACTB/SIGAATF - Instalação de Procedure](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011410951-MP-SIGACTB-SIGAATF-Instala%C3%A7%C3%A3o-de-Procedure-)

[MP-SIGACTB - CTBR040 - Não a dados a serem impressos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006986251-MP-SIGACTB-CTBR040-N%C3%A3o-a-dados-a-serem-impressos)

[MP - SIGACTB - Configuração do parâmetro MV\_TPVALOR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000607668-MP-SIGACTB-Configura%C3%A7%C3%A3o-do-par%C3%A2metro-MV-TPVALOR)

[MP - SIGACTB - Compartilhamento de Tabelas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007377851-MP-SIGACTB-Compartilhamento-de-Tabelas-)

[Razão por Item (CTBR480 - SIGACTB) - Saldo Anterior MV\_TPVALOR](https://tdn.totvs.com/pages/viewpage.action?pageId=630003385)
