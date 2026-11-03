---
content_hash: bcb8dd0381b233ddb79ecb20fb5bade98efbe738f384cf6cfd8b37a8f40b3f32
fetched_at: '2026-06-29T00:10:52.851039+00:00'
page_id: '572953897'
product: rm
source: tdn-rm
title: Layout - Dados dos Funcionários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=572953897
version: 5
---

**Parâmetros  
  
Movimentos**Tabela que o sistema irá preencher: AMOVFUN  
Dados a informar: CHAPA;INICIOPER;FIMPER;CODEVE;MESCOMP;ANOCOMP;NUMHORAS;VALOR;IDMOVTEMP;CODCUSTO;IDITEMCONTABIL;IDCLASSEVALOR  
Exemplo de layout: 00001;01/10/2020;31/10/2020;0001;10;2020;15:00;0;0;;;;  
Campos que não podem ser nulos: CHAPA;INICIOPER;FIMPER;CODEVE;ANOCOMP;MESCOMP **Abonos**Tabela que o sistema irá preencher: AABONFUN  
Dados a informar: CHAPA;DATA;CODABONO;HORAINICIO;HORAFIM;DESCONSIDERA;RESPONSAVEL;ABONOFUTURO;COLIGADARESP;SOLUCAOCONFLITO;JUSTIFICATIVA  
Exemplo de layout: 00001;01/01/2020;0001;08:00;17:00;0;00002;0;1;1;inclusão  
Exemplo de layout com campos não obrigatórios em branco: 00001;14/02/2023;0001;08:00;17:00;0;;0;;1;inclusão  
Exemplo de layout com campos não obrigatórios com o texto NULL: 00001;14/02/2023;0001;08:00;17:00;0;NULL;0;NULL;1;inclusão  
Campos que não podem ser nulos: CHAPA;DATA;CODABONO;HORAINICIO;ABONOFUTURO **Abonos Futuros**Tabela que o sistema irá preencher: AABONFUTURO  
Dados a informar: CHAPA;CODABONO;DATAINICIO;DATAFIM;HORAINICIO;HORAFIM;NUMHORAS;DESCONSIDERA  
Exemplo de layout: 00001;0001;01/01/2020;03/01/2020;00:00;23:59;;0  
Campos que não podem ser nulos: CHAPA;DATAINICIO;CODABONO;HORAINICIO **Banco de horas por dia**Tabela que o sistema irá preencher: ABANCOHORFUN  
Dados a informar: CHAPA;DATA;EXTRAFAIXA1;EXTRAFAIXA2;EXTRAFAIXA3;EXTRAFAIXA4;EXTRAFAIXA5;EXTRADESC1;EXTRADESC2;EXTRAFER1;EXTRAFER2;EXTRACOMP1;EXTRACOMP2;FALTA;ATRASO;CALCPORFORMULA  
Exemplo de layout: 00001;19/11/2020;10:00;00:00;00:00;00:00;00:00;00:00;00:00;00:00;00:00;00:00;00:00;00:00;00:00;0  
Campos que não podem ser nulos: CHAPA;DATA **Sobreavisos**Tabela que o sistema irá preencher: AEESPFUN  
Dados a informar: CODCOLIGADA;CHAPA;DATA;HORAINICIO;HORAFIM  
Exemplo de layout: 1;00001;01/01/2020;18:00;23:00  
Campos que não podem ser nulos: CODCOLIGADA;CHAPA;DATA;HORAINICIO **Descanso**Tabela que o sistema irá preencher: ADTTABFOLGA  
Dados a informar: CODTABFOLGA;DATA;HORAINICIO;HORAFIM;CONSEXTRAINTER  
Exemplo de layout: 01;01/01/2020;00:00;23:59;0  
Campos que não podem ser nulos: CODTABFOLGA;DATA;HORAINICIO **Extras** **Autorizadas**  
Tabela que o sistema irá preencher: AEAUTFUN  
Dados a informar: CODCOLIGADA;CHAPA;DATA;HORAINICIO;HORAFIM;AUTORIZADO;MOTIVO;COLIGADARESP;RESPONSAVEL;JUSTIFICATIVA;  
Exemplo de layout: 1;00001;19/11/2020;15:00;15:30;00:30;  ;  ;  ;Autorização;  
Campos que não podem ser nulos: CODCOLIGADA;CHAPA;DATA;HORAINICIO;SOLUCAOCONFLITO
