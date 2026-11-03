---
article_id: 360056642613
category: RH - Dissídio
content_hash: ea97bf77b9bd5621806604d47361f5a7c575d6f74c6d9ebc41ea3a105824446a
fetched_at: '2026-06-28T22:43:43.311238+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar os valores de Dissidio retroativo para
  demitidos
type: support-article
updated_at: '2025-08-15T18:31:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056642613-RH-Linha-Protheus-GPE-Como-gerar-os-valores-de-Dissidio-retroativo-para-demitidos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34214585693079) Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Como gerar os valores calculados de dissidio retroativo para os demitidos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**O cálculo de dissídio processará dois tipos de funcionários demitidos. Os funcionários demitidos após a data de base de dissídio terão as competências anteriores a rescisão recalculadas e demonstradas na manutenção do cálculo. Os funcionários que foram demitidos no mês da data base de dissídio, terão apenas a verba 000 demonstrada na manutenção do cálculo, que servirá apenas para atualização do salário nas rotinas de cadastro de funcionário e histórico salarial.  
A rotina de dissídio retroativo calcula diferenças apenas da folha de pagamento, diferenças rescisórias são geradas na rescisão complementar.  
  
Após calculo e conferência será necessário executar os passos:  
  
1. Na rotina Dissidio Retroativo, clique em >Outras Ações >Geração:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094900113)

2. Clique em Perguntas na tela abaixo:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094900153)

3. Preencha os parâmetros abaixo de acordo com a necessidade de geração se atentando as observações abaixo:  
Obrigatoriamente a pergunta Atualiza Lançamento deve ser preenchida com a opção de Valores Futuros e Situações com D.  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094902153)

4. Confirme os parâmetros e clique no botão abaixo:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094902553)

Sistema gerará os valores calculados de dissidio dos demitidos para valores Futuros.

Observação.: Após gerar os valores do dissidio para Valores Futuros, não é possível desfazer esse processo. Portanto, é de extrema importância que os valores sejam conferidos corretamente antes dessa geração.  
  
**Saiba mais:**

[MANUAL GPE - Dissídio Retroativo](https://tdn.totvs.com/pages/releaseview.action?pageId=220889925)  
[MP - GPE - Exclusão do cálculo de dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037259774-MP-GPE-Exclus%C3%A3o-do-c%C3%A1lculo-de-diss%C3%ADdio-)  
[MP - GPE - Geração dos valores de dissídio retroativo para folha de pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034659053-MP-GPE-Gera%C3%A7%C3%A3o-dos-valores-de-diss%C3%ADdio-retroativo-para-folha-de-pagamento)
