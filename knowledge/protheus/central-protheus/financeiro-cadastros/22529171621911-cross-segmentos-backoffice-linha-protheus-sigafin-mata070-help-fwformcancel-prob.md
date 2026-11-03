---
article_id: 22529171621911
category: Financeiro - Cadastros
content_hash: e1f7bcf3d17df5830e7a52dd0094c70719d3c6a0a2d4adeec3647b2354983c9b
fetched_at: '2026-06-28T22:37:53.198233+00:00'
product: protheus
section_id: 1500001550722
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - MATA070 - Help: FWFORMCANCEL
  Problema: Violação de Integridade. Foi encontrada referência de Código (A6_COD)
  + Nro Agencia (A6_AGENCIA) na tabela SRA - Funcionários'
type: support-article
updated_at: '2024-04-03T12:24:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22529171621911-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-MATA070-Help-FWFORMCANCEL-Problema-Viola%C3%A7%C3%A3o-de-Integridade-Foi-encontrada-refer%C3%AAncia-de-C%C3%B3digo-A6-COD-Nro-Agencia-A6-AGENCIA-na-tabela-SRA-Funcion%C3%A1rios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22529171615127) Tempo aproximado para leitura: **00****:03:00 min  
  
Ocorrência**  
Help: FWFORMCANCEL  
Problema: Violação de Integridade. Foi encontrada referência de Código (A6\_COD) + Nro Agencia (A6\_AGENCIA) na tabela SRA - Funcionários  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Causa**O HELP em questão é apresentado por uma validação de integridade, via de regra não é possível excluir um cadastro de banco que possui algum tipo de vinculo, seja de movimentações ou associações de tabelas. Nestes casos, não sugerimos a exclusão do mesmo via banco e não é possível excluir via sistema.  
  
**Solução**

O HELP ocorre, pois na tabela **SRA** de Funcionários que pertence ao RH, há um relacionamento da tabela **SX9**.

Veja a mensagem apresentada:  
Help: *FWFORMCANCEL*  
Problema: Violação de Integridade. Foi encontrada referência de **Código** (**A6\_COD**) + **Nro Agencia** (**A6\_AGENCIA**) na tabela **SRA** - **Funcionários**.  
Formulário **MATA070\_SA6**

Segue print do relacionamento em questão na tabela **SX9**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22529202921879)

Deve ser validado se o banco que está sendo excluído esta vinculado a algum funcionário nas rotinas do **SIGAGPE**.  
   
   
Uma sugestão seria apenas permanece a conta como bloqueada altera o cadastro e ajusta o campo "**Bloqueado**".
