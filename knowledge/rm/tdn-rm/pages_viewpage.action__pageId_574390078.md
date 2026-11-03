---
content_hash: ba1862b6986b1246ad92a2dead6053de787182107ed46599a61eedf7516ced9a
fetched_at: '2026-06-29T00:10:53.053093+00:00'
page_id: '574390078'
product: rm
source: tdn-rm
title: FISCAL01-13783 DT Cópia de Regras Tributárias entre coligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=574390078
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Cópia de Regras tributárias entre coligadas |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13783 |

## **02. SITUAÇÃO/REQUISITO**

**Cenário:** Criar a cópia de Evento tributário entre coligadas conforme regras abaixo

* Se não existir um tributo com mesmo código e tipo no destino a cópia do Evento será abortada;
* A cópia será realizada somente para os itens de origem contábil e somente se conta for global ou se existir na coligada de destino;
* O Evento tributário referenciado em algum item como: Atividade Rural ou Lucro da exploração, não será copiado;
* A cópia não permitirá sobreposição;
* Resultado contábil, Lançamento Manual, e Lalur Parte B não serão copiados;
* Os identificadores das tabelas dinâmicas devem ser copiados;
* Os processos, Histórico Padrão, Departamento, Centro de Custo e Filial serão copiados somente se existir no destino. No caso da Filial deve ser avaliado se ela é um item impeditivo, se sim, a copia não será realizada e a situação será logada;
* A seleção de dados da origem já deve prever a cópia de origem Cloud.

## **03. SOLUÇÃO**

Implementação do Processo de Cópia de Regras Tributários entre Coligadas conforme regras descritas no cenário.

O processo foi disponibilizado em **Gestão Fiscal -> Obrigações Principais -> Eventos Tributários -> Estrutura -> Processos -> Cópia de Regras Tributárias entre Coligadas.**

Este processo também poderá ser utilizado no modulo Serviços Globais no processo Cópia de Coligada.

**Configuração da Entidade:**

Descrição: Evento Tributário  
Action Name: **Não se Aplica**  
Wizard Parâmetro: **GlbParamsProcFormCopyColig**  
Server Name: **FisCopiaEventoTrbColigadaProc**  
Tabela Principal: **DEVCTRB**  
Cód Sistema: D - **Totvs Gestão Fiscal**

**Observação:** Na tela genérica do processo de cópia entre coligadas será exibida a opção de "Substituir registros no destino se eles já existirem" este processo não permitira Sobreposição de Eventos Tributários. A situação será apenas logada pelo processo, e se caso o registro já existir, o mesmo não será sobreposto e caso não existir o mesmo será copiado.

O processo também está preparado para cópia de Eventos tributários com origem Cloud.
