---
article_id: 1500003512962
category: Inspeção de Processos (SIGAQIP)
content_hash: 79130b827471a1a8e701f0eeac013c6d10f2d5acb4af883d1de29a1439f119c6
fetched_at: '2026-06-28T22:42:25.804720+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Inclusão de roteiro gerando nova especificação
  no QIPA010
type: support-article
updated_at: '2021-10-01T13:12:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003512962-Manufatura-Linha-Protheus-SIGAQIP-Inclus%C3%A3o-de-roteiro-gerando-nova-especifica%C3%A7%C3%A3o-no-QIPA010
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:50 min**  
**Dúvida**Por que é gerada uma nova especificação de produto quando é incluído um roteiro no **MATA632 - Roteiro de Operações**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Todas as versões  
  
**Solução**Seguindo o conceito do módulo **PCP - Planejamento e Controle da Produção**, ao realizar uma inclusão de roteiro na rotina **MATA632** é gerada uma nova revisão da especificação do produto na rotina **QIPA010 - Especificação do Produto** quando o parâmetro **MV\_QIPOPEP - Define a prioridade dos dados em relação à operação entre os ambientes QIP e PCP** estiver com conteúdo igual à **1 - PCP**.   
  
Desta forma, é verificado primeiramente se o produto em questão possui roteiro padrão definido no **MATA010 - Cadastro de Produto**, no campo **Rt Op Padrão** da aba **MRP/Suprimentos**. Esta informação é registrada na tabela **SB1 - Descrição Genérica do Produto** no campo **B1\_OPERPAD - Rt Op Padrão**. Se possuir roteiro padrão definido, o código do roteiro do **QIPA010** no campo **Roteiro** assumirá este código do roteiro padrão, desconsiderando o código do roteiro criado no **MATA632**. Caso o produto não possua roteiro padrão definido no **MATA010**, o campo **Roteiro** assumirá o código do roteiro criado no **MATA632**. A informação do campo Roteiro é registrada na tabela **QP6 - Histórico dos Produtos** no campo **QP6\_CODREC - Roteiro**.  
  
E quanto ao código do roteiro primário e secundário do **QIPA010**, para o roteiro primário seguirá a mesma regra de validação do roteiro padrão do **MATA010**. Se o produto possuir roteiro padrão, o código do roteiro primário será o roteiro padrão, e os roteiros secundários serão os demais roteiros existentes no **MATA632**. Mas, se o produto não possuir roteiro padrão definido, o roteiro primário será o código 01, e os secundários, os demais roteiros existentes no **MATA632**.
