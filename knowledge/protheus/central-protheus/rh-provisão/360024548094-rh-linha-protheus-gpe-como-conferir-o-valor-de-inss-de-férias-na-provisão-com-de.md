---
article_id: 360024548094
category: RH - Provisão
content_hash: 4282c39e3e164c553b901199552062872b72189697ffccc8c64e5b7e396590e3
fetched_at: '2026-06-28T22:43:55.778562+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como Conferir o valor de INSS de Férias na Provisão
  com Desoneração Pura
type: support-article
updated_at: '2025-10-24T12:55:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024548094-RH-Linha-Protheus-GPE-Como-Conferir-o-valor-de-INSS-de-F%C3%A9rias-na-Provis%C3%A3o-com-Desonera%C3%A7%C3%A3o-Pura
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32998049599383)**Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Como Conferir o valor de INSS de Férias na Provisão com Desoneração Pura?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**

Para empresas com **Desoneração da Folha de Pagamento Pura**, o sistema não provisiona nenhum valor referente ao Percentual de INSS Empresa (20%) e esta mesma tratativa é aplicada para os cálculos de **Provisão de Férias**, portanto apenas os valores de **Acidente de Trabalho** e **Terceiros** serão considerados para a Provisão.

Para saber como conferir o INSS na Provisão, realize os seguintes passos:

1. Realize a configuração para Cálculo da Folha de Pagamento com Desoneração Pura.  
Para mais informações sobre a configuração [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053888253-MP-GPE-C%C3%A1lculo-de-Desonera%C3%A7%C3%A3o-Pura).  
   
2. Acesse: Atualizações / Definições de Cálculo / **Manutenção de Tabelas** (**GPEA320**), selecione a tabela **S037** - Encargos Empresa, e clique em Visualizar e verifique qual é o percentual informado no campo "**%Acid. Trab.**".  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099510034)  
  
3. Acesse: Atualizações / Definições de Cálculo / **Manutenção de Tabelas** (**GPEA320**), selecione a tabela **S038** - Outras Entidades, e clique em Visualizar e verifique qual é o percentual informado no campo "**% Terceiros**".  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000623822)  
  
4. Acesse: Relatórios / Provisões / **Provisão de Férias** (**GPER070**) e preencha os parâmetros para emissão do relatório de provisão;  
  
5. Aplique a soma dos percentuais indicados nos passos 2 e 3, para conferência da linha "Atual" da coluna de "INSS" no relatório de provisão.  
No exemplo Abaixo, a Memória de Cálculo é: Total de Férias x **7,80%**:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099510094)

**Saiba Mais:**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
