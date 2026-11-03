---
content_hash: 900bd60127eb3491e30e07a2294ca6ce3cb9862b509c47001588104f316bec66
fetched_at: '2026-06-29T00:05:58.488978+00:00'
page_id: '187534249'
product: rm
source: tdn-rm
title: RMCTB00008_Reestruturação de Lançamentos por Fato Contábil.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=187534249
version: 7
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | TOTVS Gestão Contábil |
| **Processo** | : | Reestruturação de Lançamentos por Fato Contábil |
| **Subprocesso** | : | SPED Contábil |
| **Data da publicação** | : | 12/09/2014 |

**Introdução**

O processo analisa os Lançamentos/Partidas já cadastrados na base e reorganiza as partidas conforme o período informado, distribuindo as mesmas em novos lançamentos.A reestruturação irá atender a resolução CFC nº1299/2010, que define as formalidades da Escrituração Contábil Digital - ECD.

**Desenvolvimento/Procedimento**

Para a reestruturação dos lançamentos os mesmos serão agrupados mediante algumas características que permitam identificar todos os registros que se integram, conforme a regra:

1º pelo Identificador da Operação (IDOPERACAO, sendo débito = crédito);

2º pela Chave de Integração (INTEGRACHAVE, sendo débito = crédito);

3º pelo Código do Histórico Padrão (CODHISTP, sendo débito = crédito);

4º pelo Número do Documento (DOCUMENTO, sendo débito = crédito).

Além disso, os lançamentos devem ser do mesmo sistema de origem. O processo analisará e aplicarão as regras acima a todos os lançamentos do lote zero correspondentes ao período (mês/ano) informado.

**Processo**1º - O acesso deverá ser feito através do aplicativo da nova MDI (c: / tovs / corporeRM / RM.net / RM.exe). Após abrir o aplicativo acesse o menu principal / backoffice / totvs gestão contábil / escrituração contábil / ferramentas / Reestruturação de Lançamentos por Fato Contábil.

Execute a primeira vez informando apenas o período, marcando apenas a opção 'Manter Padrão de Análise' (ver figura abaixo):  
  
 **Observação**Salve o log que será apresentado após a execução do processo, pois nele serão apresentados os novos ID's de lançamentos.

2º - Gere novamente o arquivo para validação do SPED ECD. Caso a advertência no pré-validador seja apresentada novamente, será devido aos lançamentos que não foram reestruturados.

Realize o procedimento a seguir:  
Para a execução da Reestruturação de Lançamentos por Fato Contábil deverá ser informado um Histórico Padrão ou Números de Documentos (de acordo com a necessidade da empresa) para 70 partidas de um ID de lançamento (ex: o ID de lançamento 1571 está com 140 partidas, você deverá incluir um mesmo Histórico Padrão ou mesmo Número de Documento para as 70 primeiras partidas, e outro Histórico Padrão ou outro Número de Documento para as outras 70 partidas), ou seja, somente 70 partidas de um determinado ID de lançamento poderão ter o mesmo Histórico Padrão ou Números de Documentos.

Para informar de forma rápida um Histórico Padrão ou Número de Documento para uma quantidade determinada de partidas de um ID lançamento, siga o passo abaixo:   
Acesse o menu Lançamentos > Manutenção de Lançamentos > Selecione as partidas que sofrerão a alteração > Processos > Alteração de Partidas em Grupo > Inserir/Modificar Campo > Preencha somente o campo de "Histórico" > Executar.  
**Obervação**   
Nas linhas das advertências estarão informados os ID's de lançamentos, assim poderemos usá-los como referência.

**Atenção!**

O processo não poderá ser executado mais de uma vez para mês/ano.

Não serão considerados os lançamentos:

* Lançamentos agrupados;
* Lançamentos gerados pelo processo de transferência de grupos contábeis;
* Lançamento com diferença de débito x crédito.

Ao finalizar a classificação das partidas onde foram inseridos os Históricos Padrões ou Números de Documentos, execute novamente o processo de "Reestruturação de Lançamentos por Fato Contábil" sem informar nenhum período, você deverá informar os respectivos ID's de Lançamento.

3º - Faça um teste executando a reestruturação para conferir se está sendo realizada a Reestruturação.

Acesse novamente a nova MDI (c: / tovs / corporeRM / RM.net / RM.exe). Após abrir o aplicativo acesse o menu principal / backoffice / totvs gestão contábil / escrituração contábil / ferramentas / Reestruturação de Lançamentos por Fato Contábil. Informe um determinado ID de lançamento que foi apresentado na advertência do SPED (ECD), marcando uma das opções 'Priorizar Numero de Documento' ou 'Priorizar Histórico Padrão' (de acordo com a necessidade da empresa) conforme orientado no 1º item. Ver figura abaixo:  
  
  
**Observação**Será criado um novo ID de lançamento para as partidas que foram alteradas, e será informado no log após a execução da Reestruturação. Salve o arquivo para a necessidade de realizar consultas.

Para maiores informações:

[Consulte o Help TOTVS](https://tdn.totvs.com/pages/viewpage.action?pageId=423938526)

**COMUNIDADE** [**R@Controladoria**](http://fluig.totvs.com/portal/p/10097/subject/rcontbil)

**Canais** **de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 2 – (Controladoria e Finanças), 5 – (Planejamento e Controle Orçamentário), 2 – (RM Saldus).
