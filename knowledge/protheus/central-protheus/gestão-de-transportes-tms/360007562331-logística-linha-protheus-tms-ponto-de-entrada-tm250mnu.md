---
article_id: 360007562331
category: Gestão de Transportes (TMS)
content_hash: 01afd5f191476c2f47b8fe0a3dd6a5255728ebb852afbd6db7ad7744dd22d8e6
fetched_at: '2026-06-28T22:45:32.226004+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM250MNU
type: support-article
updated_at: '2022-11-29T20:30:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007562331-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM250MNU
---

**Dúvida**Como implementar o ponto de entrada TM250MNU?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM250MNU** é disparado antes da abertura do *Browse*, caso *Browse* inicial da rotina esteja habilitado, ou antes da apresentação do **Menu de opções**, caso *Browse* inicial esteja desabilitado.  
  
**Programa** **Fonte**: TMSA250.PRW  
  
**Sintaxe**: TM250MNU ( ) --> Nil  
  
**Retorno**:

* **Nil** - Não tem

**Observações**: Para habilitar ou desabilitar o *Browse*, entre na rotina, clique em **Configurações/ Browse Inicial** e selecione a opção desejada:

* Sim - Habilitar *Browse* Inicial
* Não - Desabilitar *Browse* Inicial

Este ponto de entrada pode ser utilizado para inserir novas opções no array aRotina.

**Exemplos:**

aadd(aRotina,{'TEXTO DO BOTÃO','NOME DA FUNÇÃO' , 0 , 3,0,NIL})

 ONDE: Parâmetros do array a Rotina:

     1. Nome a aparecer no cabeçalho  
     2. Nome da Rotina associada  
     3. Reservado  
     4. Tipo de Transação a ser efetuada:  
             1 - Pesquisa e Posiciona em um Banco de Dados  
             2 - Simplesmente Mostra os Campos  
             3 - Inclui registros no Bancos de Dados  
             4 - Altera o registro corrente  
             5 - Remove o registro corrente do Banco de Dados  
     5. Nível de acesso  
     6. Habilita Menu Funcional
