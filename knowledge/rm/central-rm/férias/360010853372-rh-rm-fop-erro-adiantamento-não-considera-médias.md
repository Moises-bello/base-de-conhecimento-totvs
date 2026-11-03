---
article_id: 360010853372
category: Férias
content_hash: f688af03ccb20a60e2831e8925aeeb2fa4ac3f5ed97f2008928a3dabfc81bf0a
fetched_at: '2026-06-28T22:46:56.495465+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Erro: Adiantamento não considera médias'
type: support-article
updated_at: '2025-03-12T20:04:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010853372-RH-RM-FOP-Erro-Adiantamento-n%C3%A3o-considera-m%C3%A9dias
---

**Ocorrência**Ao lançar as férias, o valor do recibo é lançado corretamente. Porém, no envelope do funcionário o valor do **Adiantamento Conforme Recibo** (código de cálculo 43) não está considerando os valores da **Média de Abono de Férias** (código de cálculo 47).  
   
 **Ambiente**RM - Totvs Folha de Pagamento - Todas as versões  
   
 **Causa** O erro foi confirmado como uma não conformidade no sistema e corrigido nos patchs 320 ou superiores. Como as férias já foram pagas e não podem ser recalculadas é necessário realizar os procedimentos abaixo como saída de contorno.  
   
 **Solução**Para solucionar este caso, siga os passos abaixo:  
   
 **01.** Atualizar o RM para o patches 320 ou superior. Os patches 320 encontram-se disponíveis para download na Central de Downloads. **[Clique aqui](https://suporte.totvs.com/portal/p/10098/download#000023/12.1/all/)** para acessar o site e realizar o download;  
 **02.** Cancelar o movimento das férias no envelope em **Folha mensal | Cancelamento**;  
 **03.** Alterar a situação do funcionário manualmente de F para A;  
 **04.** Excluir o histórico de situação das férias;  
 **05.** Alterar a situação das férias para **Marcadas**;  
 **06.** Dentro do recibo de férias, marque a flag **Não recalcular** e depois clique em **Atualizar informações.**Em seguida, lance as férias novamente.  
  
![ferias.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008436811/ferias.png)
