---
article_id: 39636714422039
category: RH - Transferência
content_hash: 166f915b4a5ba1a355621c20f945d15aa1cfad78e0928e36e276be963eead89c
fetched_at: '2026-06-28T22:43:23.341732+00:00'
product: protheus
section_id: 360010781974
source: central-protheus
title: RH - Linha Protheus - GPE - Gravação de campos customizados na Transferência
  de Funcionário - Ponto de Entrada GP180CPOS
type: support-article
updated_at: '2026-04-09T19:28:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39636714422039-RH-Linha-Protheus-GPE-Grava%C3%A7%C3%A3o-de-campos-customizados-na-Transfer%C3%AAncia-de-Funcion%C3%A1rio-Ponto-de-Entrada-GP180CPOS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39636698008215) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Gravação de campos customizados na Transferência de Funcionário - Ponto de Entrada GP180CPOS.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
O ponto de entrada GP180CPOS foi criado para realizar a gravação de campos customizados quando há transferência de funcionário entre empresas e o dicionário de dados e divergente entre as empresas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39637692489111)

**Exemplo:**

#Include "Protheus.ch"

User Function GP180CPOS()  
Local cAlias as Character  
Local aRet as Array  
Local nPos as Numeric

cAlias := ParamIXB[1] // Recebe tabela que será gravada  
aRet := ParamIXB[2] // Recebe array que contém os campos que serão gravados  
nPos := 0

// Verifica qual tabela será processada  
If (cAlias == "SRA")  
// Exemplo de remoção de campo indesejado  
// Procura campo customizado (RA\_XCAMPO) existente somente na tabela SRA da empresa T1  
nPos := aScan(aRet, {|x| AllTrim(x[1]) == "RA\_XCAMPO"})

// Se campo existe, retira do array que contém os campos que serão gravados  
If (nPos > 0)  
aDel(aRet, nPos)  
aSize(aRet, (Len(aRet) - 1))  
Endif

// Exemplo de adição de campos  
// Através das variáveis cEmpAnt (Empresa de Origem), cFilAnt (Filial de Origem), cEmpAte (Empresa de Destino) e cFilAte (Filial de Destino)  
// Verifica qual Empresa/Filial o funcionário será transferido para gravar os campos customizados (RA\_XCMP01 e RA\_XCMP02).  
If (AllTrim(cEmpAte) == "T2")  
aAdd(aRet,{"RA\_XCMP01", 123.77, "N"})  
aAdd(aRet,{"RA\_XCMP02", "TESTE", "C"})  
Endif  
Endif  
Return(aRet) // Retorna array que contém os campos que serão gravados

**Saiba Mais**  
[Boletim Técnico](https://tdn.totvs.com/pages/viewpage.action?pageId=570049216)  
[RH - Transferência](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010781974-RH-Transfer%C3%AAncia)
