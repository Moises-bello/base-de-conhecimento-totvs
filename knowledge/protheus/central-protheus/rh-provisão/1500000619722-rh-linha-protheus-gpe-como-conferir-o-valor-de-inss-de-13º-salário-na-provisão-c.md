---
article_id: 1500000619722
category: RH - Provisão
content_hash: 066ef01fa753cc5ac208926be794d8c0c1a9e82b8c39254213648e534fa1b4ab
fetched_at: '2026-06-28T22:43:55.774112+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como Conferir o valor de INSS de 13º Salário na
  Provisão com Desoneração Pura
type: support-article
updated_at: '2025-10-24T13:20:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000619722-RH-Linha-Protheus-GPE-Como-Conferir-o-valor-de-INSS-de-13%C2%BA-Sal%C3%A1rio-na-Provis%C3%A3o-com-Desonera%C3%A7%C3%A3o-Pura
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32903769156887)**Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como Conferir o valor de INSS de 13º Salário na Provisão com Desoneração Pura?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**

Para empresas com **Desoneração da Folha de Pagamento Pura**, o sistema não provisiona nenhum valor referente ao Percentual de INSS Empresa (20%) e esta mesma tratativa é aplicada para os cálculos de **Provisão de 13º Salário**, portanto apenas os valores de **Acidente de Trabalho** e **Terceiros** serão considerados para a Provisão.

Para saber como conferir o INSS na Provisão, realize os seguintes passos:

1. Realize a configuração para Cálculo da Folha de Pagamento com Desoneração Pura.  
Para mais informações sobre a configuração [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053888253-MP-GPE-C%C3%A1lculo-de-Desonera%C3%A7%C3%A3o-Pura).  
  
2. Acesse: Atualizações / Definições de Cálculo / **Manutenção de Tabelas** (**GPEA320**), selecione a tabela **S037** - Encargos Empresa, e clique em Visualizar e verifique qual é o percentual informado no campo "**%Acid. Trab.**".  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000720182)  
  
3. Acesse: Atualizações / Definições de Cálculo / **Manutenção de Tabelas** (**GPEA320**), selecione a tabela **S038** - Outras Entidades, e clique em Visualizar e verifique qual é o percentual informado no campo "**% Terceiros**".  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101824313)   
  
4. Acesse: Relatórios / Provisões / **Provisão 13º Salário** (**GPER090**) e preencha os parâmetros para emissão do relatório de provisão;  
  
5. Aplique a soma dos percentuais indicados nos passos 2 e 3, para conferência da linha "Atual" da coluna de "INSS" no relatório de provisão.  
No exemplo Abaixo, a Memória de Cálculo é: Total de 13º x **7,80%**:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099612594)  
  
**Saiba Mais:**[RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o) [Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
