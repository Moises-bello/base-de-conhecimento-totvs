---
article_id: 360022031372
category: SIGAEST - MOVIMENTAÇÕES
content_hash: b81cc88c4af61042ec222c5a203326ccc5fcb6e2d828d625f5ba052c1c6b7063
fetched_at: '2026-06-28T22:38:55.531523+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Execauto rotina MATA241
  Movimentacao Multipla
type: support-article
updated_at: '2026-02-04T17:58:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022031372-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Execauto-rotina-MATA241-Movimentacao-Multipla
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29671584071703) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Qual o exemplo de Execauto utilizado para executar automaticamente a rotina de Movimentos Multiplos Modelo 2?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Todas as versões  
  
**Solução**

Abaixo segue um exemplo de inclusão de movimentação através da rotina automática:

```
#INCLUDE "RWMAKE.CH"
#INCLUDE "TBICONN.CH"
// Função principal para gerar um movimento de estoque
User Function TMATA241()
   Local _aCab1 := {}       // Array para o cabeçalho do movimento
   Local _aItem := {}       // Array para os itens do movimento
   Local _atotitem := {}    // Array para agrupar todos os itens
   Local cCodigoTM := "015" // Código do tipo de movimento (TM)
   Local cCodProd := "H002" // Código do produto
   Local cUnid := "MP"      // Unidade de medida do produto
   // Variáveis para controle de execução automática
   Private lMsHelpAuto := .T. // Se .T., exibe mensagens de help
   Private lMsErroAuto := .F. // Se .F., não exibe erros automáticos
   // Prepara o ambiente (empresa, filial e módulo)
   Prepare Environment Empresa "T1" Filial "D MG 01" Modulo "EST"
   // Monta o cabeçalho do movimento
   _aCab1 := {;
       {"D3_DOC", NextNumero("SD3", 2, "D3_DOC", .T.), NIL},; // Número do documento 
                                                             // gerado automaticamente
       {"D3_TM", cCodigoTM, NIL},;                           // Tipo de movimento
       {"D3_CC", "        ", NIL},;                          // Centro de custo (vazio)
       {"D3_EMISSAO", dDatabase, NIL};                       // Data de emissão (data atual)
   }
   // Monta os itens do movimento
   _aItem := {;
       {"D3_COD", cCodProd, NIL},;   // Código do produto
       {"D3_UM", cUnid, NIL},;       // Unidade de medida
       {"D3_QUANT", 1.99, NIL},;     // Quantidade do item (1.99)
       {"D3_LOCAL", "01", NIL},;     // Local de estoque
       {"D3_CUSTO1", 1, NIL};        // Custo do item
   }
   // Adiciona o item ao array de itens
   aAdd(_atotitem, _aItem)
   // Executa a rotina de inclusão de movimento (MATA241)
   // Certifique-se de que _aCab1 e _atotitem são arrays válidos
   If ValType(_aCab1) == "A" .AND. ValType(_atotitem) == "A"
       MSExecAuto({|x, y, z| MATA241(x, y, z)}, _aCab1, _atotitem, 3)
   Else
       MsgStop("Erro: Arrays inválidos para execução automática.", "Erro")
       Return
   EndIf
   // Verifica se houve erro na execução automática
   If lMsErroAuto
       MostraErro()          // Exibe mensagem de erro
       DisarmTransaction()   // Desfaz a transação em caso de erro
       Break                // Interrompe a execução
   EndIf
   Return
```

Você também pode usar para movimentar Lote/Endereço/Movimento valorizado, basta incluir os campos correspondentes a sua necessidade, valide com seu analista Desenvolvedor.

**Video funcional ao final do boletim.**

**Saiba mais:**

* [Criação de gatilho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021876611-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Cria%C3%A7%C3%A3o-de-gatilho)
* [Como criar um gatilho em MVC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051029514-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-criar-um-gatilho-em-MVC)
* [Retirar o gatilho (SX7) de uma rotina MVC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020439811-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Retirar-o-gatilho-SX7-de-uma-rotina-MVC)
* [Gatilho entre tabelas em rotina mvc](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018867011-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Gatilho-entre-tabelas-em-rotina-mvc)
* [Como utilizar gatilhos para preenchimento dos campos em rotinas MVC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018580812-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-utilizar-gatilhos-para-preenchimento-dos-campos-em-rotinas-MVC)
* [Retornar o campo que esta sendo alterado em rotina MVC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019002512-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Retornar-o-campo-que-esta-sendo-alterado-em-rotina-MVC)
* [Gatilho do cabeçalho para o item na rotina MATA415](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025839851-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Gatilho-do-cabe%C3%A7alho-para-o-item-na-rotina-MATA415)
* [Execução de Gatilho sem a necessidade de enter no campo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019797791-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Execu%C3%A7%C3%A3o-de-Gatilho-sem-a-necessidade-de-enter-no-campo)
* [Instrução não cabe no campo do gatilho ou formulas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020884771-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Instru%C3%A7%C3%A3o-n%C3%A3o-cabe-no-campo-do-gatilho-ou-formulas)
* [Criando gatilho com User Function para validar a execução em rotina especifica](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021541971-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Criando-gatilho-com-User-Function-para-validar-a-execu%C3%A7%C3%A3o-em-rotina-especifica)
