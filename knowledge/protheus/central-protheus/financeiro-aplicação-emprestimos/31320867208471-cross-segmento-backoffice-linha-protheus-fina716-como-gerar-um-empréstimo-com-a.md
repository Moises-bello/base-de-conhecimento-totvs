---
article_id: 31320867208471
category: Financeiro - Aplicação / Emprestimos
content_hash: aaf20499429114776b92aad32aa41af25e4ad3292a1a0438a5e1c5a3827a915c
fetched_at: '2026-06-28T22:37:59.299904+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA716 - Como gerar um empréstimo
  com a taxa Selic
type: support-article
updated_at: '2025-12-17T13:52:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31320867208471-Cross-Segmento-Backoffice-Linha-Protheus-FINA716-Como-gerar-um-empr%C3%A9stimo-com-a-taxa-Selic
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31320882340759) Tempo aproximado para leitura: **00:08 min****Dúvida**Como gerar um empréstimo com a taxa Selic?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões  
  
**Solução** **1.** Realizar o cadastro do índice Financeiro na rotina **FINA017**  
Campo FIT\_BACEN = 11  
Logo após esse cadastro, executar o Job FINXTAXA para atualizar os índices, na rotina **Atualização de Índice (****FINA018)**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31320882342423)  
  
**2.** Realizar o cadastro do template na rotina FINA716, utilizando o índice criado na rotina **FINA017**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31320882344215)  
  
**3.** Nesse exemplo vamos incluir um empréstimo e salvar com os valores abaixo;  
Data da inclusão: 01/01/2025  
Vlr. Operação: 10.000,00  
Operação: TEM (**selecionar o template criado no passo 2**)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31320882345751)  
  
**4.** Vamos simular a amortização desse empréstimo no dia 31/01/2025  
Valor com a correção **R$ 10.096,37.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31320867186455)

Corresponde ao mesmo valor obtido na Calculadora do Cidadão, disponibilizada pelo Banco Central.  
<https://www3.bcb.gov.br/CALCIDADAO/publico/corrigirPelaSelic.do?method=corrigirPelaSelic>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31320882347287)

**Saiba mais**[Job atualização de taxas BACEN - FINXTAXA](https://tdn.totvs.com/pages/releaseview.action?pageId=680255528#Jobatualiza%C3%A7%C3%A3odetaxasBACENFINXTAXA-05.%C3%8DNDICESFINANCEIROS)

[Cadastro de templates - FINA716](https://tdn.totvs.com.br/display/public/PROT/Cadastro+de+templates+-+FINA716)
