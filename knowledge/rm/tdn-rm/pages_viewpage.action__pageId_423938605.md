---
content_hash: 35fb3cc863a2c6301775f667ae733a0c598f414b4eae3f34a8c11f6c40568c8f
fetched_at: '2026-06-29T00:09:27.992003+00:00'
page_id: '423938605'
product: rm
source: tdn-rm
title: Vinculações/Adiantamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938605
version: 4
---

Visando proporcionar ao Gestor um melhor controle das movimentações onde houveram adiantamentos envolvidos nos processos, o sistema TOTVS Gestão de Estoque, Compras e Faturamento disponibiliza um novo recurso, Vinculações.   
Este recurso tem por finalidade a associação de um movimento em outro, associar o movimento classificado como adiantamento em um movimento classificado como controla adiantamento.   
Para este processo será necessário trabalhar com dois tipos de movimentos distintos, onde um tipo de movimento, em sua parametrização, estará classificado como "Adiantamento" e o outro, classificado "Controla Adiantamento".   
Ao classificar um tipo de movimento para Adiantamento, não será possível gravar movimentações que controlem adiantamento neste tipo de movimento e vice-versa.  
Apenas tipos de movimento 1.2.XX e 2.2.XX podem ser parametrizados para trabalhar com Vinculações/Adiantamentos.   
Tanto o tipo de movimento parametrizado com classificação "Controla Adiantamento" quanto "Adiantamento" devem estar parametrizados para gerar lançamento financeiro.   
Só será possível associar um movimento de adiantamento em um movimento que controla adiantamento caso o cli/for de ambos os movimentos sejam os mesmos e se o lançamento financeiro gerado a partir do movimento de adiantamento esteja baixado.   
Também será possível associar mais de um movimento de adiantamento ao movimento que controla adiantamentos, considerando que podemos ter mais de um adiantamento para o mesmo cli/for.   
O valor do adiantamento disponível para vínculo será o "Valor Líquido" do próprio movimento de adiantamento.   
O vinculo será feito por item de movimento, cada item presente no movimento que controla adiantamento, pode ser associado um valor do movimento de adiantamento.  
Atenção!  
No caso do tipo de movimento parametrizado com classificação "Adiantamento", o sistema não irá realizar nenhuma consistência quanto à classificação do tipo de documento utilizado para geração do lançamento financeiro, mas sugerimos que utilizem a classificação "Adiantamento", desta forma, será possível realizar o vínculo dos movimentos e dos lançamentos financeiros envolvidos.  
O vínculo de movimentos realizado pelo sistema TOTVS Gestão de Estoque, Compras e Faturamento não é consistido para o processo de vínculo de lançamentos de adiantamentos realizado pelo sistema TOTVS Gestão Financeira.   
O usuário será responsável por vincular o lançamento financeiro ao lançamento de adiantamento, conforme o movimento de adiantamento vinculado ao movimento que controla adiantamento.

Caso o movimento classificado como "Controla Adiantamento" seja parametrizado para criar movimentos com status "Não processado" ao executar o processo de "Processar Grupo de Movimentos" não será exibida a opção de vínculo de adiantamentos. Desta forma, o usuário precisará realizar a edição do movimento após o processamento para que isso seja realizado.
