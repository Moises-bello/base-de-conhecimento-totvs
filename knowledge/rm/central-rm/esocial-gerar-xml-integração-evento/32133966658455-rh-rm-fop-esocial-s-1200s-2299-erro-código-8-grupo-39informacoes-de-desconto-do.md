---
article_id: 32133966658455
category: eSocial - Gerar XML/ Integração Evento
content_hash: a65f9e56a737fab41ca8949fc2aa4ce70535f6659a7b684ed4681e46bcc2c4a8
fetched_at: '2026-06-28T22:47:13.125604+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - S-1200/S-2299 Erro código 8: Grupo #39;Informacoes
  de desconto do emprestimo em folha#39; deve ser preenchido.'
type: support-article
updated_at: '2026-05-27T20:23:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32133966658455-RH-RM-FOP-eSocial-S-1200-S-2299-Erro-c%C3%B3digo-8-Grupo-39-Informacoes-de-desconto-do-emprestimo-em-folha-39-deve-ser-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32133937842455) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao enviar o evento S-1210 para o Governo, ocorre o **erro código 8: Grupo #39;Informacoes de desconto do empréstimo em folha#39; deve ser preenchido. Verifique as condições de preenchimento no leiaute.**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir das versões - Todas as versões  
  
**Causa**  
O erro ocorre quando existe no XML S-1200/S-2299 alguma rubrica com natureza 9253 - Empréstimos eConsignado - desconto, porém não foi gerado no XML o grupo de Informações de desconto do empréstimo em folha(tag *descFolha*). A tag não é gerada quando não foi preenchido a modalidade correta no cadastro do empréstimo ou quando no evento de provisão do crédito do trabalhador nas férias, o evento está com a natureza de rubrica 9253.  
  
**Solução 1:**  
  
1. Para correção do erro acesse o cadastro do empréstimo em **Administração de Pessoal | Funcionários | Anexos | Folha de Pagamento | Empréstimo.**

2. Selecione o empréstimo Crédito Trabalhador do funcionário e edite-o.

3. Altere o campo modalidade do Empréstimo para **'Crédito Trabalhador eSocial',** conforme print abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32133937842839)

4. Salve a alteração e regere e envie o XML.

Observação: Somente deve ser usado a modalidade 'Empréstimo Consignado com garantia FGTS' quando for **empréstimo direto com o banco**. Quando se tratar do empréstimo Crédito do Trabalhador - Medida Provisória nº 1.292, de 12 de Março de 2025, deve ser usado a opção **'Crédito Trabalhador eSocial'.**  
  
**Solução 2:**

1. Para correção do erro acesse o cadastro dos eventos de códigos de cálculo 485, 486, 487 e 488.  
Em **Administração de Pessoal | Eventos.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/34346336623127)**

2. Valide as naturezas de rubrica dos eventos com esses códigos e cálculo, e caso esteja com a natureza 9253, informar uma natureza de rubrica diferente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34346336626711)

3. Após correção, gere um S-1010 com data igual ou anterior ao período de apuração do S-1010 e integre o mesmo ao Governo.

4. Regere o XML S-1200, e o integre ao Governo.

**Observação:**A natureza de rubrica **9253**somente deve ser utilizada no evento do efetivo desconto do crédito do trabalhador que também deve conter o código de cálculo 480.  
  
**Saiba Mais:**

[MANUAL DE ORIENTAÇÃO DO EMPREGADOR - CRÉDITO DO TRABALHADOR](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-operacional-do-empregador-programa-credito-do-trabalhador-v2-16-05-25.pdf)  
[Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março de 2025](https://tdn.totvs.com.br/pages/releaseview.action?pageId=925361639)
