---
content_hash: e56ef107f907b067c3589910f5d56280efda0be7d3dbe68b1cd46aee005b5024
fetched_at: '2026-06-29T00:08:33.425159+00:00'
page_id: '274316716'
product: rm
source: tdn-rm
title: DT_Geracao_Certificado_Novos_Tipos
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Geracao_Certificado_Novos_Tipos
version: 106
---

## Geração de certificado - Novos tipos de certificado

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Geração de certificados / Diplomas* | *Geração de certificados / Diplomas* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Certificados / Diplomas* | *Certificados / Diplomas* | |  |  | |
| **Tickets relacionados** | *726324* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | EDUCACIONAL01-149 |
| **País(es):** | *Brasil* |

## Descrição

Inclusão de novos tipos para emissão de certificados, permitindo a rastreabilidade entre os novos tipos e o registro correspondente selecionado para a geração.

## Procedimento para Utilização

       1.            No TOTVS Educacional acesse a funcionalidade através do menu "Atividades Acadêmicas" | "Certificados / Diplomas" | "Geração de certificados / diplomas"

O sistema apresentará a tela com os diversos tipos de certificados/diplomas disponibilizados. Acessar a guia "Participação" e os novos tipos serão visualizados para seleção.

       2.            Pra cada novo tipo disponibilizado será possível selecionar o papel para desempenhado pela pessoa no certificado. Ex: Aluno, Coordenador, Professor, etc.

       3.            Após selecionar o tipo do certificado  e clicar na opção selecionar será exibido os registros para a geração do certificado, baseado no tipo de certificado escolhido.

       4.           Após a listagem dos registros retornados é possível selecionar quais os registros irão ser utilizados na geração dos certificados/diplomas.

       5.            Após a geração do certificado/diploma é possível visualizar o registro gerado e a rastreabilidade para o tipo selecionado no momento da geração através da visão de "Certificados/Diplomas" | Guia: Certificado.

## Informações técnicas

Através da tabela **SCERTIFICADO** é possível identificar para quem o certificado foi gerado. Em todos os certificados é registrado o código da pessoa que recebeu o certificado e se ela é um aluno, um professor e/ou uma pessoa.

Campos:

**CODPESSOA** - Código da pessoa que recebeu o certificado

**CODPROFESSOR** - Código de professor da pessoa

**RA** - Registro acadêmico da pessoa

**DATASERVER** - Dataserver que demandou a geração do certificado emitido

**CHAVERM** - Campo com a chave primária do registro que demandou a geração do verificado. As informações desse campo são compostas pela concatenação da chave primária da tabela utilizada pelo seu "***Dataserver***".

Exemplo:

Foi emitido um certificado de conclusão de estágio para um aluno e para seu orientador.

Para esse cenário, teremos dois registros na tabela **SCERTIFICADO** que indicarão a emissão desses certificados:

1. 1. 1. Certificado para o aluno:
         1. Coligada: 1
         2. Id. Certificado: 1
         3. RA (Registro acadêmico): RA-0100
         4. Dataserver: EduEstagioContratoData
         5. ChaveRM: 1;1;RA-0100
      2. Certificado para o professor:
         1. Coligada: 1
         2. Id. Certificado: 2
         3. Código do professor: P00200
         4. Dataserver: EduEstagioContratoData
         5. ChaveRM: 1;1;RA-0100

Dessa forma, conseguimos rastrear que foram emitidos dois certificados para contrato de estágio **1** da coligada **1** em que o aluno **RA-0100** participou, através da ChaveRM **"1;1;RA-0100"**.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Processo** | **Dataserver** | **ChaveRM** | **Tabela principal** | **Foco** |
| Grupo de Estudos | EduExtParticpantesGrupoData | SEXTPARTICIPANTESGRUPO.IDGRUPOESTUDO; SEXTPARTICIPANTESGRUPO.CODPESSOA | SEXTPARTICIPANTESGRUPO | Participante do grupo |
| Visita Técnica | EduExtInscricaoVisitaData | SEXTINSCRICAOVISITA.CODCOLIGADA; SEXTINSCRICAOVISITA.IDVISITAEVENTO; SEXTINSCRICAOVISITA.RA | SEXTINSCRICAOVISITA | Aluno |
| Visita Técnica | EduExtVisitaEventoData | SEXTVISITAEVENTO.CODCOLIGADA; SEXTVISITAEVENTO.IDVISITAEVENTO | SEXTVISITAEVENTO | Pessoa e Professor |
| Estágio | EduEstagioContratoData | SESTAGIOCONTRATO.IDESTAGIOCONTRATO; SESTAGIOCONTRATO.CODCOLIGADA; SESTAGIOCONTRATO.RA | SESTAGIOCONTRATO | Aluno e Orientador |
| Estágio | EduEstagioParticipanteBancaData | SESTAGIOPARTICIPANTEBANCA.CODCOLIGADA; SESTAGIOPARTICIPANTEBANCA.IDPARTICIPANTEBANCA | SESTAGIOPARTICIPANTEBANCA | Participante de banca |
| Ação de Extensão | EduProjParticipantesData | SPROJPARTICIPANTES.CODCOLIGADA; SPROJPARTICIPANTES.IDPROJETO; SPROJPARTICIPANTES.CODPESSOA | SPROJPARTICIPANTES | Participante da ação de extensão |
| Ação de Extensão | EduProjBolsistaData | SPROJBOLSISTA.CODCOLIGADA; SPROJBOLSISTA.IDPROJETO; SPROJBOLSISTA.CODPESSOA | SPROJBOLSISTA | Bolsista ação de extensão e Bolsista Voluntário |
| Ação de Extensão | EduExtComissaoAvalData | SEXTCOMISSAOAVAL.CODCOLIGADA; SEXTCOMISSAOAVAL.IDEDITAL; SEXTCOMISSAOAVAL.CODPESSOA | SEXTCOMISSAOAVAL | Comissão avaliadora de edital |
| Ação de Extensão | EduProjProjetoData | SPROJPROJETO.CODCOLIGADA; SPROJPROJETO.IDPROJETO | SPROJPROJETO | Coordenador de proposta de ação |
|  |  |  |  |  |
| Para a entidade Curso os campos dataserver e chaverm não são preenchidos | | |  |  |
| **Processo** |  | **Vinculo** | **Tabela** | **Foco** |
| Curso |  | SCERTIFICADO.CODCOLIGADA; SCERTIFICADO.IDHABILITACAOFILIAL; SCERTIFICADO.RA | SCERTIFICADO | Aluno |

divs
