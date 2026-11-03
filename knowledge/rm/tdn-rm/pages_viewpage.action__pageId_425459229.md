---
content_hash: ee1950e30916b2f5035cc66cd3e926c7a021de10909f509a0be25943e4098b96
fetched_at: '2026-06-29T00:09:34.712934+00:00'
page_id: '425459229'
product: rm
source: tdn-rm
title: Fato - RH - Reclamações de Colaboradores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459229
version: 3
---

**Reclamações dos Colaboradores**

---

Não possui descrição.  
   
 **Tabela: HLF.**

|  |  |  |
| --- | --- | --- |
| **DESCRIÇÃO** | **CAMPO**   **STAGE ÁREA** | **CAMPO NO RM** |
| NÚMERO REGISTRO - PK | HLF\_RECNO | AUTOINC |
| LINHA DE PRODUTO | HLF\_LINPRO | R |
| INSTÂNCIA | HLF\_ISTCIA | 1 |
| EMPRESA - FK | HLF\_EMPRES | MD5 (CODCOLIGADA) |
| ESTABELECIMENTO - CÓDIGO | HLF\_FILIAL | - |
| ESTABELECIMENTO - FK | HLF\_ESTABL | MD5 (CODCOLIGADA + -) |
| COLABORADOR - FK | HLF\_COLABR | MD5(CODPESSOA) |
| GRAU DE INSTRUÇÃO - FK | HLF\_GRAINS | MD5(PCODINSTRUCAO.CODCLIENTE) |
| NÍVEL HIERÁRQUICO - FK | HLF\_NIVHIE | O RM NÃO POSSUI ESTA ENTIDADE |
| SINDICATO - FK | HLF\_SINDIC | MD5(PSINDIC.CODIGO) |
| SITUAÇÃO COLABORADOR - FK | HLF\_SITCLB | MD5(PCODSITUACAO.CODCLIENTE) |
| TEMPO CASA - FK | HLF\_TPCASA | MD5(COLIGADA + CHAPA + DATAADMISSAO) |
| TEMPO CARGO - FK | HLF\_TPCARG | MD5(COLIGADA + CHAPA + DATAMUDANCA) |
| SEÇÃO – FK | HLF\_SECAO | MD5(COLIGADA + CODSECAO) |
| DATA DA ABERTURA DO PROCESSO | HLF\_DTPROC | VPROCESSOS.DATAABERTURA |
| DATA DE ENCERRAMENTO DO PROCESSO | HLF\_DTFIMP | VPROCESSOS.DATAENCERRAMENTO |
| DATA DA RECLAMAÇÃO | HLF\_DATA | VRECLAMANTE.RECCREATEDON |
| NÚMERO PROCESSO | HLF\_NUMPRC | VPROCESSOS.NUMPROCESSO |
| QTDE RECLAMAÇÕES | HLF\_QTRECL | 1 |

**Data de Extração:** -.  
    
 **Conceito de Extração:** Fato - RH - Reclamações de Colaboradores.  
    
 **View:** HLF\_RECLAMACOESCOLABORADORES.  
    
 **Informações Adicionais:** Estes dados não são por filial Para esta analise são realizados consultas no Vitae (Sistema de Gestão de Pessoas)  
    
 **Parâmetros:** Será utilizado somente os parâmetros de extração gerais
