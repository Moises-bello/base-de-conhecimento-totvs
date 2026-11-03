---
article_id: 360024976731
category: Encargos
content_hash: 4ee10b36b6ed188930d6179e9e31f1c2f27c2672b94855edaecf92da45714c25
fetched_at: '2026-06-28T22:46:53.342758+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP - SEFIP: Existem tomadores com códigos diferentes cadastrados
  com o mesmo CEI'
type: support-article
updated_at: '2024-10-11T19:54:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024976731-RH-RM-FOP-SEFIP-Existem-tomadores-com-c%C3%B3digos-diferentes-cadastrados-com-o-mesmo-CEI
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**  
Ao gerar a Sefip é apresentada a mensagem abaixo:  
  
**ATENÇÃO! Existem Tomadores com Códigos diferentes cadastrados com o mesmo CEI, ou o mesmo Código de Tomador com o mesmo CEI utilizando máscaras diferentes. Funcionários com rateios nestes Tomadores podem deixar de ser processados. Favor verificar a lista no Log de Erros, e ajustar o cadastro.**  
  
**Sugestão:** Verificar Históricos de afastamentos e Rateio de Tomadores se o CEI está cadastrado corretamente para os funcionários. Após o ajuste deve executar a Distribuição do Sefip**.  
  
Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causas**  
Ao gerar a Sefip o sistema não estava atualizando o CEI no histórico de afastamento. Devido a este ocorrido, foi necessário criar o processo **Atualizar CEI Tomador** para atualizar o CEI do histórico de afastamento do funcionário e para atualizar o CEI do rateio de tomador no cadastro de funcionário conforme tabela **FCFOCEI**.  
  
**Solução**  
Para solucionar este incidente, siga os passos abaixo:  
  
1. Acesse **Encargos | Sefip | Atualizar CEI Tomador**;

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10789466592535)**

2. Marque o check box **Atualizar o CEI no rateio de tomadores do cadastro de funcionários**;  
3. Marque o check box **Atualizar o CEI no cadastro de afastamento do funcionário**;  
4. Execute o processo.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10789481610519)
