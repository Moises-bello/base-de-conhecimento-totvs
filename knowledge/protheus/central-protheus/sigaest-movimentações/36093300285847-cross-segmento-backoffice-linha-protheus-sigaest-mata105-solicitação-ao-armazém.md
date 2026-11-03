---
article_id: 36093300285847
category: SIGAEST - MOVIMENTAÇÕES
content_hash: f6769e8ca980384a99ce6f09f390b4f35e5bffe55425cca34ddc2cf0ce0b4c2d
fetched_at: '2026-06-28T22:38:55.714888+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA105 - Solicitação
  ao Armazém não entra em aprovação por controle de alçada quando não há saldo em
  estoque
type: support-article
updated_at: '2025-11-04T14:42:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36093300285847-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA105-Solicita%C3%A7%C3%A3o-ao-Armaz%C3%A9m-n%C3%A3o-entra-em-aprova%C3%A7%C3%A3o-por-controle-de-al%C3%A7ada-quando-n%C3%A3o-h%C3%A1-saldo-em-estoque
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36093330633751) Tempo aproximado para leitura: 00:01**:**00 **min**  
  
**Dúvida**  
Ao confirmar uma **Solicitação ao Armazém (MATA105)** para um produto **sem saldo em estoque**, o sistema **não envia a solicitação para aprovação por alçada,** o que fazer?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
O processo de **aprovação por alçada** é baseado na **análise de valores** e **não de quantidades**.  
Assim, o fato de o item **não possuir saldo em estoque** e permitir **estoque negativo** **não impede** a entrada em aprovação.

O motivo real ocorre quando o **item não possui valor associado** — ou seja, **não há valor histórico** preenchido para o produto.

### **Solução:**

1. **Verifique se o produto possui valor no campo** `B2_CM1` **(Custo Médio)**, na tabela **SB2**.

   * Caso o campo esteja **vazio**, a solicitação **não será enviada para aprovação**.
   * É necessário **preencher o campo B2\_CM1** com um valor válido para que o sistema **considere o item no processo de aprovação por alçada**.
2. Faça um teste:

   * Mesmo que o **saldo em estoque esteja zerado**, confirme se o **campo B2\_CM1 está preenchido**.
   * Após o preenchimento, **gere uma nova solicitação** e **valide se passa a entrar na aprovação por alçada**.
3. Essa lógica segue o comportamento padrão documentado pela TOTVS, disponível no link:  
   🔗 [TOTVS TDN - Solicitação de Compras/Armazém - Cálculo de Valor para Aprovação](https://tdn.totvs.com/pages/viewpage.action?pageId=284348332)

   Observação: A solução acima pedimos para validar o campo B2\_CM1, porém se aplica a outros campos de cálculo conforme descrito na documentação acima

   > “Ao confirmar a Solicitação de Compras (MATA110) ou Solicitação ao Armazém (MATA105), é realizado o cálculo dos valores dos itens informados na solicitação, com aglutinação por Entidades Contábeis, considerando o campo de valor total e verificando o rateio por entidades contábeis (opção não integrada ao módulo PCO).
   >
   > Para obter o valor total do item da solicitação, é obedecida a seguinte ordem de prioridade:
   >
   > 1. Preço Estimado da SA (CP\_VUNIT) ou SC (C1\_VUNIT) multiplicado pela Quantidade (CP\_QUANT / C1\_QUANT);
   > 2. Último Preço de Compra (B1\_UPRC);
   > 3. Preço Standard (B1\_CUSTD);
   > 4. Custo Médio (B2\_CM1).”

---

### **Observação:**

* O comportamento é **padrão do sistema** e **não configura erro**.
* Caso o produto não possua nenhum dos campos de valor (estimado, último preço, preço standard ou custo médio) preenchidos, **a solicitação não entrará em aprovação por alçada**.
* Recomenda-se sempre manter os **valores atualizados** para garantir a correta análise do processo de aprovação.

**Saiba mais:**

[*Configuração para Controle de Alçadas por Entidade Contábil - Solicitação de Compras e Armazém*](https://tdn.totvs.com/pages/releaseview.action?pageId=284348332)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA105 - Como configurar Controle de Alçada para Solicitação ao Armazém?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17440776514711-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA105-Como-configurar-Controle-de-Al%C3%A7ada-para-Solicita%C3%A7%C3%A3o-ao-Armaz%C3%A9m)

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
