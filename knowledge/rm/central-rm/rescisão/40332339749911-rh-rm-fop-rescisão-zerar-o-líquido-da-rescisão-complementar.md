---
article_id: 40332339749911
category: Rescisão
content_hash: 069fdbd3f2def05113a36f63a47e2e280a2026cb1566d619469e6f65d0a86d0c
fetched_at: '2026-06-28T22:46:54.115413+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - Rescisão: Zerar o Líquido da Rescisão Complementar'
type: support-article
updated_at: '2026-05-08T19:18:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40332339749911-RH-RM-FOP-Rescis%C3%A3o-Zerar-o-L%C3%ADquido-da-Rescis%C3%A3o-Complementar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40332346383511) Tempo aproximado para leitura: 00**:01:45 min**  
  
**Dúvida**  
Como realizar a parametrização e o processo para zerar os valores de uma rescisão complementar no RM Folha de Pagamento?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Para zerar uma rescisão complementar, é necessário configurar eventos específicos de provento e desconto para o líquido complementar no parametrizador do sistema e, posteriormente, executar o processo de lançamento do líquido selecionando a flag correspondente. Veja os exemplos dos passos abaixo:  
  
1. Parametrização de Eventos:

* Acesse o menu **Configurações**;
* Selecione **Parametrizador**;
* Navegue até a etapa **Folha de Pagamento | Rescisão | Líquido de Rescisão**;
* Nos campos **Evento Provento para Líquido de Rescisão Complementar** e **Evento Desconto para Líquido de Rescisão Complementar**, informe os respectivos eventos criados para esta finalidade. Em seguida, salve as alterações.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40337367866391)

2. Cálculo e Geração:

* Realize o cálculo da rescisão complementar conforme a necessidade;
* Gere o Termo de Rescisão do Contrato de Trabalho (TRCT).

3. Lançamento do Líquido:

* Acesse o menu **Rescisão**;
* Selecione a rotina **Lançamento do Líquido**;
* Na tela de parâmetros, marque obrigatoriamente a opção **Rescisão Complementar**;
* Informe o período e os funcionários desejados e clique em **Executar**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40337367868567)

**Saiba Mais**

Para mais informações sobre rescisões no RM, acesse:

[RH - RM - FOP - Calcular Rescisão Complementar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004150252-RH-RM-FOP-Calcular-Rescis%C3%A3o-Complementar)  
  
[RH - RM - FOP - TRCT: Rescisão Complementar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414113319831-RH-RM-FOP-TRCT-Rescis%C3%A3o-Complementar)
