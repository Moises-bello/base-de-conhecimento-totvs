---
article_id: 360017595612
category: Financeiro
content_hash: e61e3e567760344c459694de28f51919391fa34e1eaed01458c9ec53205911eb
fetched_at: '2026-06-28T22:38:03.415986+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Não será possível gravar
  Complemento de Imposto
type: support-article
updated_at: '2022-06-15T00:50:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017595612-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-N%C3%A3o-ser%C3%A1-poss%C3%ADvel-gravar-Complemento-de-Imposto
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:00 min****Ocorrência**No módulo **Financeiro,** ao incluir o complemento de imposto na rotina **Contas a Pagar** ou a **Contas a Receber** é apresentado a mensagem**: Não será possível gravar Complemento de Imposto, pois a Natureza e/ou Fornecedor do título não possuem configuração para geração de imposto. Portanto, altere os cadastros caso queira que o Sistema efetue os cálculos.**Segue imagem abaixo **![REINF.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360013193412/REINF.JPG)  
  
Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**É apresentado esta mensagem quando as parametrização do cadastro da **Natureza** e/ou cadastro do **Fornecedor** não estão de acordo para calcular o INSS.   
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o **módulo Financeiro**, **Atualizações**, **Cadastros**, **Fornecedores**  
2. No cadastro do **Fornecedor**, Aba **Fiscais** o campo **Calc. INSS** (**A2\_RECINSS**) conteúdo = Sim.   
3. Acesse o **módulo Financeiro**, **Atualizações**, **Cadastros**, **Naturezas.**  
4. No cadastro da **Natureza**, Aba **Impostos** o campo **Calcula INSS** (**ED\_CALCINS**) conteúdo = Sim.  
  
**Importante**Apesar da ferramenta de cadastro de **complemento de imposto** flexibilizar várias combinações de ações, todas devem estar coerentes com a legislação vigente. Ou seja, os dados configurados e informados serão validados pelo governo na entrega de obrigações como o **REINF**.
