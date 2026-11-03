---
article_id: 21682946726295
category: eSocial
content_hash: 2c803dce3b1664fe68062453d55065ba2a1ac07f4cd05189a711d95d7276075d
fetched_at: '2026-06-28T22:47:39.060770+00:00'
product: rm
section_id: 1500000912221
source: central-rm
title: 'RH - RM - SMT - S-2210 - Erro na validação do campo ''codAgntCausador'': Se
  dtAcid = [2024-01-22] e se tpAcid = [1, 3]'
type: support-article
updated_at: '2025-09-25T14:50:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21682946726295-RH-RM-SMT-S-2210-Erro-na-valida%C3%A7%C3%A3o-do-campo-codAgntCausador-Se-dtAcid-2024-01-22-e-se-tpAcid-1-3
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21682946698647) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**  
Ao gerar o XML do evento S-2210, é exibido a seguinte mensagem: **Erro na validação do campo 'codAgntCausador': Se dtAcid = [2024-01-22] e se tpAcid = [1, 3], deve ser um código válido e existente na Tabela 14.**

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional - A partir das versões **12.1.2302.235, 12.1.2306.182, 12.1.2310.116 e superiores.**  
  
**Causa**  
Este erro ocorre pois o código gerado na tag **'codAgntCausador'** é diferente do que pertence a tabela 14 do eSocial. Segundo regra do Leiaute S-1.3, para este campo quando **dtAcid >= [2024-01-22] e se tpAcid = [1, 3], o código deverá estar presente na tabela 14.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21682952243223)  
  
**Solução**  
Para correção, basta acessar o cadastro da CAT, e excluir o código do agente causador que foi informado para que possa incluí-lo novamente na visão.  
   
![image.png](https://totvssuporte.zendesk.com/attachments/token/4L06WawXu8ozdFVKcovkKt388/?name=image.png&lotus_request=true)  
   
Ao ir em incluir um novo, pesquise pelo código do agente causador desejado e edite-o:  
   
![image.png](https://totvssuporte.zendesk.com/attachments/token/OK0VG6dbnOaJ9figRrLDvWCEM/?name=image.png)  
   
Assim, será aberta uma nova janela e deverá alterar o **'Tipo de agente'** para **'Agente Causador Acidente de Trabalho'**.  Dessa forma, no campo **'Cód. eSocial Agente Causador Acidente de Trabalho'** serão listados os códigos presentes na **Tabela 14 do eSocial.**  
  
![image.png](https://totvssuporte.zendesk.com/attachments/token/u4msinU2iuV5Voc9B9abOreso/?name=image.png)  
  
Ao selecionar um dos itens da tabela 14 para preenchimento do campo **'Cód. eSocial Agente Causador Acidente de Trabalho'**, salve as alterações feitas, gere o XML novamente e ao ser gerado poderá realizar o envio do S-2210.   
 

**Saiba Mais:**

- [eSocial - Tabela 14](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-nt-02-2024/tabelas.html#14)

- [RH - RM - SMT - Evento S-2210 - CAT (Comunicação de Acidente de Trabalho)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028898652)
