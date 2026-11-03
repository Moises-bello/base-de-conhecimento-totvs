---
article_id: 15368195042455
category: SIGAEST - FECHAMENTO DE ESTOQUE (VIRADA DOS SALDOS)
content_hash: 3e07e15d44f8bc4530184e60954f430e81245f15d5b61d89366d4c74cfa721ce
fetched_at: '2026-06-28T22:38:52.725598+00:00'
product: protheus
section_id: 1500001538921
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Execauto para rotina
  Virada de Saldos - MATA280
type: support-article
updated_at: '2025-03-12T12:20:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15368195042455-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Execauto-para-rotina-Virada-de-Saldos-MATA280
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15368211432855) Tempo aproximado para leitura: **00:02:40min** **Dúvida**É possivel efetuar o processamento da rotina Virada de Saldos - MATA280, de forma automatica via execauto? como fazer.  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Para que o fechamento do final do período seja executado é necessário executar a rotina Virada de Saldos. Esta rotina faz com que os saldos finais, calculados pelas rotinas de Recálculo do Custo Médio ou Saldo Atual para Final, sejam transferidos como saldo inicial da data estipulada.

Com a rotina automática é possível configurar informações como: Data do Fechamento, Usuário, Grupo de perguntas e Filial a ser processado a Virada de Saldos.

Segue exemplo:

```
#INCLUDE "PROTHEUS.CH"  
#INCLUDE "RWMAKE.CH"  
#INCLUDE "TBICONN.CH"  
  
User Function MyMta280()  
  
Local aItem := {} //Filial  
Local aListaFil := {} //Filial  
Local aParAuto := {} //Execucao Automatica  
Local cUserNamej := ""  
Local dDate  
Local lBat   
Local oJourney  
  
ConOut(Repl("-",80))  
ConOut(PadC("Fechamento - Virada de Saldos",80))  
ConOut(PadC("Conectando Ambiente.....",80))  
  
PREPARE ENVIRONMENT EMPRESA "T1" FILIAL "D MG 01" MODULO "EST" TABLES "SB2", "SB3", "SD1", "SD2", "SD3", "SB9", "SBD", "SC2", "SF1", "SF2"  
  
ConOut(PadC("Ambiente Conectado com Sucesso...",80))  
ConOut(Repl("-",80))  
  
cUserNamej := "Administrador" //Usuario  
dDate := CTOD("31/01/2023") //Data do Fechamento  
lBat := .T. //Define que a rotina será executada em Batch  
oJourney := JsonObject():new() //Grupo de perguntas  
  
//Filial  
aadd(aItem, .T.)  
aadd(aItem, "D MG 01 ") //filial  
aadd(aItem, "Filial BELO HOR ") //descricao  
aadd(aItem, "53485215000106") //cgc  
aadd(aItem, .F.)  
  
aadd(aListaFil, aItem)  
  
//Execucao Automatica  
aadd(aParAuto, 2)  
aadd(aParAuto, 2)  
aadd(aParAuto, 2)  
aadd(aParAuto, 2)  
  
MATA280(lBat,dDate,,,,,,,, aListaFil, aParAuto,, .F., cUserNamej)  
  
RESET ENVIRONMENT  
  
ConOut(Repl("-",80))  
ConOut(PadC("Fechamento - Virada de Saldos CONCLUIDO",80))  
ConOut(PadC("Encerrando Ambiente.....",80))  
  
Return
```

**Importante**

* Para verificar se na base de dados existe saldo pendente de distribuição. Se o cliente não quiser executar o relatório, deverá criar/alterar o parâmetro [MV\_A280SDA](https://tdn.totvs.com.br/pages/viewpage.action?pageId=312165032), configurando com o conteúdo F (False).
* O relatório Saldo a Distribuir somente verifica o saldo pendente de distribuição dentro do período de fechamento de estoque. Deverá ser utilizada a data do período de fechamento.

**Importante**

O parâmetro [MV\_A280GRV](https://tdn.totvs.com.br/pages/viewpage.action?pageId=312165032) define se o cliente gera os registros de saldos iniciais das tabelas SB9, SBJ e SBK, para produtos que não possuem movimentação dentro do período ou que possuam saldo zerado em quantidade ou valor.

Se .T (True/Verdadeiro) todos os produtos e armazéns têm seus saldos levados para as tabelas de saldos iniciais (SB9, SBJ e SBK).

Se .F.(False/ Falso) somente os produtos e armazéns que possuem movimentação dentro do período de processamento e produtos e armazéns que não possuam quantidades e custos zerados, tem seus registros de saldos iniciais gravados. Os produtos que não se enquadrarem nesta regra (obsoletos) não são mais levados pela rotina.

## **ASSUNTOS RELACIONADOS**

* [Acompanha Custos](https://tdn.totvs.com/pages/viewpage.action?pageId=572493785)
* [Acompanha Custos - FAQs](https://tdn.totvs.com/pages/viewpage.action?pageId=684348538)
* [Virada de saldos (MATA280 - SIGAEST)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=450141831)
* [Saldos em Estoque](https://tdn.totvs.com.br/pages/viewpage.action?pageId=430722859)

Todos os exemplos disponibilizados de execauto, pontos de entrada, são inteiramente para demonstração da possibilidade de utilização.

Para assuntos sobre customizações TOTVS, o time de Suporte consistirá em fornecer as documentações que possibilitem a utilização de pontos de entrada e rotinas automáticas documentadas  no portal TDN/KCS(Boletins) para uso no produto padrão.

Estas documentações possuem exemplos de utilização previamente testados, caso utilize estes e o resultado seja diferente do documentado ou apresente falha, caso não disponha de analista programador para realizar os ajustes, dispomos do serviço do time Hub Plataformas ([hub.plataformas@totvs.com.br](mailto:hub.plataformas@totvs.com.br)).

Esta equipe oferece os serviços de criação e manutenção de fontes Protheus, que tem como característica a disponibilidade de um recurso remoto para realização desta atividade em horários comerciais (dias úteis das 08:00 às 18:00).

**Saiba mais:**

*[MP - SIGAEST - Como fazer uma análise de Custos no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020860771)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
