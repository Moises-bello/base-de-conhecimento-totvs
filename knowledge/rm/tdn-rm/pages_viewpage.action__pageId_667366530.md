---
content_hash: 9baa618661b091158d65be1ad5f92c98544907a89bcbf2add8fb753c0459bbf4
fetched_at: '2026-06-29T00:11:16.382372+00:00'
page_id: '667366530'
product: rm
source: tdn-rm
title: FISCAL01-17290 - DT - Alterar Regra de Validação do Cadastro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=667366530
version: 3
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | EFD-REINF |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17290 |

## **02. SITUAÇÃO/REQUISITO**

Criar uma permissão no perfil do usuário para permitir sobrescrever as regras de validação do Evento da EFD-Reinf

Alterar as regras de validação de Exclusão/Edição no cadastro de Eventos da EFD-Reinf para respeitar a  
permissão criada e permitir a Exclusão/Edição sem aplicar validação de regras de negocio.

**Regras:**

Criar uma permissão no perfil do usuário para permitir sobrescrever as regras de validação do Evento da EFD-Reinf.  
O cadastro dos Eventos periódicos e cadastrais devem permitir a Exclusão/Edição de qualquer Evento sem validar nenhuma regra.  
No caso de edição, deve ser gravado um histórico indicando que ocorreu alteração manual.  
Ao clicar em excluir os Eventos, deverá ser informado ao usuário que a exclusão do registro na base não terá nenhum efeito no   
ambiente da SEFAZ e não poderá ser revertida.

## **03. SOLUÇÃO**

Implementado Conforme Solicitado.

Disponível a partir da 12.1.34
