---
content_hash: 48ddd17416e000b679f1eb9e7240c3b7fb32a1be551e87ac4e44d1ff0dca6d83
fetched_at: '2026-06-29T00:12:13.403779+00:00'
page_id: '954098730'
product: rm
source: tdn-rm
title: Importância do Saneamento de Dados no Sistema RM (Expurgo de dados)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=954098730
version: 21
---

O sistema **RM** oferece recursos especializados para o expurgo de dados e a transferência de registros antigos para tabelas de arquivo morto. Esses processos desempenham um papel essencial na manutenção do desempenho do sistema e na otimização do ambiente de banco de dados.

Ao remover ou arquivar registros que não são mais utilizados nas operações diárias, diversas vantagens podem ser obtidas, incluindo:

* **Melhoria do desempenho do sistema:** Consultas e operações se tornam mais ágeis, promovendo maior eficiência no uso da solução.
* **Redução no tempo de backup e restauração:** Com menor volume de dados ativos, as rotinas de backup e recuperação de dados são significativamente aceleradas.
* **Simplificação da manutenção do banco de dados:** A diminuição na complexidade administrativa facilita ajustes e intervenções no ambiente.

A seguir, são apresentados os processos e tabelas que contam com funcionalidades de expurgo e arquivamento no sistema.

| Produto | Processo | Classe do Processo | Tipo de Expurgo | Documentação | Tabelas Envolvidas |
| --- | --- | --- | --- | --- | --- |
| Framework | Limpar Log de Execução de Processos | GlbProcClearJobs | Exclusão de Dados | <https://tdn.totvs.com/x/-zwtE> | GJOBX ; GJOBXEXECUCAO ; GKNOWNJOBSERVERDIAGNOSTIC;GRELBATCH |
| Framework | Limpar Histórico de Execução de Conceitos, para Integração TOTVSAPP 1.0 | ConTotvsAppCleanHstProcess | Exclusão de Dados | <https://tdn.totvs.com/x/CqviM> | GTOTVSAPPCONCEITOHST |
| Framework | Limpar dados | RM.Host.Cleanner | Exclusão de Dados | <https://tdn.totvs.com/x/dHbXIQ> | QCUBODATA |
| Folha de Pagamento | eSocial - Fila de Eventos | FopRotinasTransfereFilaEventosESocialProcess | Move p/ tabela de histórico | <https://tdn.totvs.com/x/3yQrHg> | PESOCIALEVENTOS, PESOCIALEVENTOSCOMPL |
| Folha de Pagamento | Gerenciador de Log de Cálculo | FopGerLogComplementarProcess | Move p/ tabela de histórico | <https://tdn.totvs.com/x/GPT7Gg> | PLOGCALCULO; PLOGFUNCIONARIO; PLOGCALCTEXTO |
| Folha de Pagamento | Gerenciador de Logs Complementares | FopRemoveLogComplementarProcess | Exclusão de Dados | <https://tdn.totvs.com/x/z-P7Gg> | PLOGCALCULOSUPL; PLOGFUNCIONARIOSUPL; PLOGCALCTEXTOSUPL |
| Folha de Pagamento | Transferência Ficha Financeira | FopRotinasLibCompetenciaProcess | Move p/ tabela de histórico | <https://tdn.totvs.com/x/n-H7Gg> | PFPERFF;PFFINANC;PFVERBAS;PFVERBASDIS   PFVERBASDISFER;PFMOVCC;PFRETIFICACAOPERIODO;PFPERFFCOMPL   PFFINANCCOMPL;PFVERBASCOMPL;PFVERBASDISHIST;PFVERBASDISFERHIST   PFMOVCCCOMPL;PFRETIFICACAOPERIODOCOMPL |
| Folha de Pagamento | Remover eventos zerados de competências anteriores | FopRemoveEventosZeradosProcess | Exclusão de Dados | <https://tdn.totvs.com/x/K4gqDQ> | PFFINANC |
| Folha de Pagamento | Folha Agrária - Transferência de Produção x Histórico | FopTransfProducaoHistoricoProcess | Move p/ tabela de histórico | <https://tdn.totvs.com/x/RiabJg> | PPRODUCAOAGRARIA; PHSTPRODUCAOAGRARIA |
| Folha de Pagamento | Liberação de competência (Transfere ou remove eventos da Ficha Ficha Financeira, Log de Cálculo, Gerenciador de Movimentos, códigos fixos - depende da parametrização) | FopRotinasLibCompetenciaProcess | Exclusão de Dados | <https://tdn.totvs.com/x/RPL7Gg> | PLOGCALCULO;PLOGFUNCIONARIO;PLOGCALCTEXTO;PFPERFF   PFFINANC;PFVERBAS;PFVERBASDIS;PFVERBASDISFER   PFMOVCC;PFRETIFICACAOPERIODO;PFPERFFCOMPL;PFFINANCCOMPL   PFVERBASCOMPL;PFVERBASDISHIST;PFVERBASDISFERHIST;PFMOVCCCOMPL   PFRETIFICACAOPERIODOCOMPL;PFCODFIX;PFENTMOV |
| TOTVS Gestão de Ponto | Logs de Importação de Batida | PtoProcImportacaoBatidas | Exclusão de Dados | <https://tdn.totvs.com/x/dPX7Gg> | AIMPORTACAOBATIDALOG |
| TOTVS Gestão de Ponto | Transferir dados para tabelas de Arquivo morto | PtoProcTransferirDadosArquivoMorto | Move p/ tabela de histórico | <https://tdn.totvs.com/x/J-L7Gg> | AABONFUN;AABONFUNAM;AABONOCALCULADO;AABONOCALCULADOAM   AAFHTFUN;AAFHTFUNAM;AATRFALTA;AATRFALTAAM   AAVISOCALCULADO;AAVISOCALCULADOAM;ABATFUN;ABATFUNAM   AJORNADACALCULADA;AJORNADACALCULADAAM;AJUSTFUN;AJUSTFUNAM   AMODIFICAOCORRENCIACALCULADA;AMODIFICAOCORRENCIACALCULADAAM;AMOVFUN;AMOVFUNAM  AMOVFUNDIA;AMOVFUNDIAAM;AOCORRENCIACALCULADA;AOCORRENCIACALCULADAAM |
| Gestão Contábil | Fechar Exercício Contábil | CtbFecharExercicioContabilDataProc | Move p/ tabela de histórico | <https://tdn.totvs.com/x/vslEGQ> | CCONTRAT;CCONT;CRATEIOLCMULTIMOEDA;CRATEIOLC;CLCOMPL; CPARTIDAMULTIMOEDA;CDIMENSAOFCFO;CDIMENSAOTPRODUTO; CDIMENSAORATEIO;CPARTIDA;CLANCAMENTO |
| Gestão Contábil | Liberar Exercício Contábil | CtbLiberarExercicioContabilDataProc | Exclusão de Dados | <https://tdn.totvs.com/x/AspEGQ> | CCONTRATHIST;CCONTHIST;CRATEIOLCMULTIMOEDAHIST;CRATEIOLCHIST; CLCOMPLHIST;CPARTIDAMULTIMOEDAHIST;CDIMENSAOFCFO;CDIMENSAOTPRODUTO; CDIMENSAORATEIO;CPARTIDAHIST;CHISTTGCPROC;CHISTEPPROC;CHISTRATEIOLAN; CLANCAMENTOHIST |
| Gestão Patrimonial | Fechamento de Período | PatFechamentoPeriodoProc | Move p/ tabela de histórico | <https://tdn.totvs.com/x/4shEGQ> | ICALCULORAZAO;ICALCULORAZAOFILIAL;IOCORRENCIA |
| Gestão de Imóveis | Limpeza de Tabelas de Log | ImbProcessoLimpezaLogProc | Move p/ tabela de histórico | <https://tdn.totvs.com/x/1_qrN> | XLOGVENDAPARCELA;FTRBLANHST;FLANINTEGRACAOHST;FLANRATCCUHST   FLANRATDEPHST;FRELLANHST;FRETENCAOACUMULADARATEIOHST;FRETENCAOACUMULADAHST   FRETENCAOIRRFHST;FLANBAIXAINTEGRACAOHST;FLANBAIXARATCCUHST;FLANBAIXARATDEPHST   FLANBAIXATRBHST;FLANBAIXAHST;FHISTVALORESINTEGRACAOHST;FLOGVALORESHST   FLANHST |
| TOTVS Gestão de Pessoas | Excluir currículos em anexo obsoletos |  | Exclusão de Dados | <https://tdn.totvs.com/x/WO-7Gg> |  |
| TOTVS Saúde Hospitais e Clínicas | Farmácia - Movimentação de Estoque | SauStockArchivingProcessAction | Move p/ tabela de histórico | <https://tdn.totvs.com/x/OJW9Ng> | SZAPRAZAMENTO;SZATENDMATMED;SZCINCOCERTOSCHECK;SZCINCOCERTOSCHECKINGTIMES   SZCINCOCERTOSGRUPO;SZMOVIESTOQUEITEM;SZMOVITMAPRAZNAPLIC;SZMOVITMAPRAZ   SZRELEXAMEMATMEDCONTA;SZRELEXAMEMOVIESTOQUE;SZMOVIESTOQUE;SZREQUISICAOREGINF   SZESTOQUEPACIENTE;SZMOVIESTMAN;SZREGINFCIRURGIAFOLHASALA;SZMOVIESTOQUEPROC   SZITENSCIRURGIA;SZAGENDACIRURGICAMOV |
| Totvs Gestão Estoque, Compras e Faturamento | Liberação de Movimento | MovLiberacaoProc | Exclusão de Dados | <https://tdn.totvs.com/x/xsdEGQ> | Todas as tabelas que o movimento possuir ligação, são muitas tabelas e pode variar |
| TOTVS Gestão Fiscal | Período Fiscal | FisPerFiscalFecharProcData | Move p/ tabela de histórico | <https://tdn.totvs.com/x/bIkvGQ> | DLAFAGRUP;DLAF;DLAFTRANSP;DEVENTOREINFLANC;DLAFEXTERIOR   DCTRC;DCOMPONENTECARGA;DCTEEMISSOR;DCTEDOC;DCTESEGURO   DCTEMOTORISTA;DLAFCOMPLEMENTOCTRC;DLAFDISPOSITIVO;DLAFAGRUPFLX;DITEM   DLAFNFECAMPOSLIVRES;DLAFAJUSTESPED;DTRBITEM;DITEMAJUSTESPED;DITEMTRIBDISCUTIDOS   DTRBITEMCALCCONTRPREV;DITEMLOTEPRD;DITEMBEM;DITEMCOMPL;DHISTITEM   DLAFMOVPROCESSOJUD;DTRBLAF;DLAFNORMA;DLAFRATCCU;DLAFRATDEP   DNFTERCEIROS;DITEMCUPOMCANC;DLAFCOMPL;DLAFGUIA;DLAFMOVNOTAEMPENHO   DLAFENQUADRAMENTOS;DHISTLAF;DLAFCTB |
| TOTVS Gestão Financeira | Liberação de Período | FinLanLiberacaoPeriodoAction | Exclusão de Dados | <https://tdn.totvs.com/x/J_EdGQ> | FINTEGRACAOXCX;FXCX;FCONCILCARTAOTRANS;FCONCILIACAOGRPOPER   FCONCILCARTAO;FXCXCOMPL;FRECONCILRELAC;FXCXCONTOLD   FRECONCIL;FFAT;FLANANTECIPAXCX;FLANANTECIPA   FLANRATOLD;FLANCONTOLD;FLANRATCCU;FLANRATDEP   FREPASSE;FLANLOG;FLANCOMPL;FRELLAN   FTRBLAN;FRETENCAOACUMULADA;FACORDOREL;FLANBAIXATRB   FLANBAIXARATCCU;FLANBAIXARATDEP;FLANBAIXAINTEGRACAO;FLANINTEGRACAO   FLOGVALORES;FLOGSESSAOCAIXA;FLANBOLETOBAIXA;FLANBAIXA   TMOVLAN;FLANBOLETO;FRELLANPAI;FRELLANPAI   FADIANTAMENTORETENCAO;FRETENCAOACUMULADARATEIO;SCONTACORRENTE;SBOLSALAN   SLAN;FXCX;FLAN;FLANLIQDUVIDOSA   DLANFIN;FLANHST;FTRBLANHST;FLANINTEGRACAOHST   FLANRATCCUHST;FLANRATDEPHST;FRELLANHST;FRETENCAOACUMULADARATEIOHST   FRETENCAOACUMULADAHST;FRETENCAOIRRFHST;FLANBAIXAINTEGRACAOHST;FLANBAIXARATCCUHST   FLANBAIXARATDEPHST;FLANBAIXATRBHST;FLANBAIXAHST;FHISTVALORESINTEGRACAOHST   FLOGVALORESHST;FACORDOREL;FACORDOLANRATCCU;FACORDOLANRATDEP   FLANACORDO;FACORDO |
| TOTVS Audit | Expurgo Total do Log De Auditoria | EngActionFullCleanAuditoriaProcessData | Exclusão de Dados | <https://tdn.totvs.com/x/ikF_LQ> | ZAUDITCHANGES |

Visitas

[![Contador de visitas](https://megacontador.com.br/img-B1vGMUCDDWhLzjuS-15.gif)](https://megacontador.com.br/ "Contador de Visitas do MegaContador")

]]>
