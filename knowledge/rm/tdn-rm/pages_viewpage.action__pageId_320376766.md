---
content_hash: d0cb290356f32eee17df23dea41d14a33986e1da0b9b15a376ebda29531efe06
fetched_at: '2026-06-29T00:08:47.790810+00:00'
page_id: '320376766'
product: rm
source: tdn-rm
title: FOPROTINAS01-2748 Adequações no TRCT Referentes à Reforma Trabalhista
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=320376766
version: 4
---

# INCLUSÃO DA NOVA DESCRIÇÃO 'Acordo Empregado e Empregador' PARA O CAMPO 22

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | TRCT Portaria 1621/2010 |
| **Situação/Requisito:** | No dia  , a Caixa Econômica Federal emitiu a circular 789/2017, referente às alterações no SEFIP e GRRF decorrentes da Reforma Trabalhista (lei 13.467/2017). As alterações estão descritas na versão 5 do Manual de Orientações Recolhimentos Mensais e Rescisórios ao FGTS e das Contribuições Sociais. Dentre as mudanças geradas, o manual apresenta no 'ANEXO V - TABELA DE CONVERSÃO PARA OS CÓDIGOS DE MOVIMENTAÇÃO CRIADO PELO MTE - NOVO TRCT X FGTS' um novo descritivo correspondente ao código de movimentação 'I5 - Rescisão de contrato por acordo entre empregado e empregador' na GRRF. O novo descritivo (campo '22-Causa do Afastamento') é 'Acordo Empregado e Empregador' e ainda não possui código próprio na TRCT (campo '27-Cód. Afastamento'). |
| **Solução/Implementação:** | O de/para interno do processo de geração do TRCT Portaria 1621/2010 foi ajustado para reconhecer rescisões cadastradas com o tipo 'V - Comum acordo' para um funcionário:        Assim, ao gerar o relatório TRCT Portaria 1621/2010, o novo descritivo será levado no campo 22 e o campo 27 será deixado em branco: |
| **Tickets relacionados:** | - |
