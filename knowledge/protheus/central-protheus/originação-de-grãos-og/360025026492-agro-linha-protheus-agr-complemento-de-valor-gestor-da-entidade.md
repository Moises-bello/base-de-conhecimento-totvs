---
article_id: 360025026492
category: Originação de Grãos (OG)
content_hash: dede72a99c83644d117a96ff188352a7bd95f21f05fab3625631e2bf03fce2a6
fetched_at: '2026-06-28T22:45:37.680533+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Complemento de Valor Gestor da Entidade
type: support-article
updated_at: '2025-06-25T11:11:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025026492-Agro-Linha-Protheus-AGR-Complemento-de-Valor-Gestor-da-Entidade
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20177132763799)*** Tempo aproximado para leitura: **00:02:30 min****Dúvida**Qual é o procedimento para efetuar o **Complemento de Valor da Entidade**, na rotina **Gestor da Entidade - OGA450**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Para solucionar essa dúvida, siga os seguintes passos:  
  
1. Gerar um **Contrato**.

![GEST.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7897023131671)

2. Gerar um romaneio com divergência de fixação, com valor de entrega menor do que o fixado.

![GEST1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7897122931351)

3. Na rotina de **Gestor da Entidade** informar a entidade e pressionar o botão **Atualizar**, avaliar se é uma **Compra**, **Venda**, **Armazenagem** e selecionar o **contrato** desejado. Após a escolha, acessar **Ações Relacionadas >****Financeiro**.

![GEST2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7897126430231)

4. Após ter selecionado o contrato desejado será necessário vincular o romaneio por meio das **Ações Relacionadas - > Vincula Doc**.

![GEST3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7897221799959)

5. Como exemplo, no contrato gerado anteriormente, o valor fixado foi de **R$0,80/Kg**, e o romaneio foi entregue com o preço de **R$0,20/Kg**, desta forma o sistema identifica que necessita uma **NF - Nota Fiscal** de **Complemento**.  
**Complemento Próprio** é gerado quando o tipo de formulário for igual a **Sim**.  
**Complemento Produtor** é gerado quando o tipo de formulário for igual a **Não**.  
Caso o valor seja maior do que a fixação será gerado um desconto financeiro, igualando os valores com base no contrato.

![GEST4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7897203519511)

6. Clicar em **Pendências**.

![GEST5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7897247680151)

7. Selecionar as pendências e clicar em **Ajustar Pendências**.

![GEST6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7897256981271)

8. É exibida uma mensagem que ocorreu o processo com sucesso e é demonstrado o valor que foi gerado o complemento.

![GEST7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7897252073239)

9. **Status Atua**l, não possui pendências fiscal/financeira.

![GEST8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7897261363607)
