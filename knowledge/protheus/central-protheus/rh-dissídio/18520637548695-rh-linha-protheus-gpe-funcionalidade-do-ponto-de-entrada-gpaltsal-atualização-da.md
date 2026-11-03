---
article_id: 18520637548695
category: RH - Dissídio
content_hash: 5ebdce54384fa0d05df2e37ed4433a6be5e8cfa75d1b30fa3d65500263b72e4e
fetched_at: '2026-06-28T22:43:43.369893+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Funcionalidade do Ponto de Entrada GPALTSAL - Atualização
  da Tabela para Salário Alterado
type: support-article
updated_at: '2025-08-06T18:22:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18520637548695-RH-Linha-Protheus-GPE-Funcionalidade-do-Ponto-de-Entrada-GPALTSAL-Atualiza%C3%A7%C3%A3o-da-Tabela-para-Sal%C3%A1rio-Alterado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18520674163095) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Funcionalidade do Ponto de Entrada GPALTSAL - Atualização da Tabela para Salário Alterado.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Permite atualizar uma tabela personalizada quando o salário do funcionário for alterado.

**Eventos**Nas rotinas GPEA010 (Cadastro de Funcionários), GPEM690 (Dissídio Retroativo), CSAM080 (Atualização do Aumento Programado), GPER200 (Aumento Salarial) e TRMA100 (Cadastro de Funcionários acessado pelo módulo Cargos e Salários e Arquitetura Organizacional).

**Programa Fonte**GPEA010.PRX, GPEM690.PRX, CSAM080.PRX, GPER200.PRX, TRMA100.PRX

**Sintaxe**GPALTSAL - Atualização da Tabela para Salário Alterado ( [ nOpcx ] )

Retorno

()

**Observações**

O ponto de entrada tem função genérica e será executado após a atualização da tabela SR3 em todas as rotinas citadas acima.

#### **EXEMPLO DE UTILIZAÇÃO** #INCLUDE 'PROTHEUS.CH' User Function GPALTSAL() Local aSaveArea := GetArea() Local dData := DATE() Local nOpcao := ParamIxb[1] If nOpcao == 3 dbSelectArea("XXX") If Reclock("XXX",.T.) XXX\_DATA := dData XXX\_CAMPO := SRA->RA\_MAT XXX->( MsUnlock() ) EndIf XXX->( dbCloseArea() ) EndIf RestArea(aSaveArea) Return()

**Parâmetros**

**Outras Ações / Ações relacionadas**

| Nome | Tipo | Descrição |
| --- | --- | --- |
| nOpcx | Numérico | Operação da rotina (Inclusão, Alteração) |

#### 

#### **Variáveis**

**Principais Campos e Parâmetros**

| Nome | Tipo | Escopo | Pode Alterar |
| --- | --- | --- | --- |
| ``` ParamIxb ``` | Array of Record | Global | Não |

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Quais são os pontos de entrada disponíveis na rotina GPEM650](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036110113-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEM650)

[Página Centralizadora do Dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
