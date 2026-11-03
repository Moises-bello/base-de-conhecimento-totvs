---
article_id: 360007722711
category: Gestão de Transportes (TMS)
content_hash: 620878fa29dc5513f96a194051c26da1e2ad701bafadd6799c52ede2b1718c2d
fetched_at: '2026-06-28T22:45:32.325509+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM300MNU Inserir Novas
  Opções no Array
type: support-article
updated_at: '2023-03-01T20:03:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007722711-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM300MNU-Inserir-Novas-Op%C3%A7%C3%B5es-no-Array
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:10 min  
  
Dúvida**Como implementar o ponto de entrada **TM300MNU -**Inserir Novas Opções no Array?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM300MNU** e é disparado antes da abertura do *Browse*, caso *Browse* inicial da rotina esteja habilitado, ou antes da apresentação do **Menu de opções**, caso *Browse* inicial esteja desabilitado.  
  
**Programa** **Fonte**: TMSA300.PRW  
  
**Sintaxe**: TM300MNU - Inserir Novas Opções no Array ( ) --> Nil  
  
**Retorno**:  
  
**Nil**

(nulo)* Nil

**Observações**: Para habilitar ou desabilitar o Browse, entre na rotina, clique em Configurações/Browse Inicial e selecione a opção desejada:

* Sim - Habilitar Browse Inicial
* Não - Desabilitar Browse Inicial

Este ponto de entrada pode ser utilizado para inserir novas opções no array aRotina.  
  
**Exemplos**:  
  
aadd(aRotina,{'TEXTO DO BOTÃO','NOME DA FUNÇÃO' , 0 , 3,0,NIL})

ONDE: Parâmetros do array a Rotina:

* 1. Nome a aparecer no cabeçalho
* 2. Nome da Rotina associada
* 3. Reservado
* 4. Tipo de Transação a ser efetuada: 
  + 1 - Pesquisa e Posiciona em um Banco de Dados
  + 2 - Simplesmente Mostra os Campos
  + 3 - Inclui registros no Bancos de Dados
  + 4 - Altera o registro corrente
  + 5 - Remove o registro corrente do Banco de Dados
* 5. Nível de acesso
* 6. Habilita Menu Funcional
