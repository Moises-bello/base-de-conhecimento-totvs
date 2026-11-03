---
article_id: 26097133481239
category: Financeiro - Consultas / Relatórios
content_hash: e6baef64108dec9ee771fc4e5b6b4511ef523699d05548fe6c05c3d69bb5fa00
fetched_at: '2026-06-28T22:37:58.384188+00:00'
product: protheus
section_id: 1500001539561
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINSV051 - Como usar
  o Relatorio de Retorno CNAB para pré-validar a baixa
type: support-article
updated_at: '2026-02-18T16:18:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26097133481239-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINSV051-Como-usar-o-Relatorio-de-Retorno-CNAB-para-pr%C3%A9-validar-a-baixa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26097133463319) Tempo aproximado para leitura: **00:07:00 min**  
  
**Dúvida**  
Como usar o Relatório de Retorno CNAB para validação do retorno?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - a partir da release 12.1.2510  
  
**Solução**

Com a evolução das rotinas financeiras no Protheus, o relatório padrão e recomendado para a pré-validação de baixas e leitura de arquivos de retorno CNAB (incluindo a leitura de arquivos no disco C) é o **FINSV051**, desenvolvido na plataforma **Smart View**. A utilização do Smart View garante o acesso às novas funcionalidades, métodos e visões de relatórios.

O relatório legado **FINR650** (Relatório de Retorno CNAB) passou a ser uma opção alternativa. Sua utilização é indicada apenas para os cenários onde o cliente possui a necessidade de customizar o relatório legado. Para isso, o FINR650 deve ser convertido e utilizado como uma *User Function* (Exemplo: `U_FIN650`).

Mais informações:  <https://suporte.totvs.com/portal/p/10098/download?e=1120373>

Visando melhorar as rotinas de relatório, trouxemos abaixo no link os relatórios que serão descontinuados.

[Relatórios do BackOffice Protheus - Descontinuados a partir de 31/10/2024](https://tdn.totvs.com/pages/releaseview.action?pageId=823815318)

O Intuito do Smart View é trazer as novas funcionalidades do Protheus relacionados a novos métodos e visões, como, por exemplo, a API para movimentações bancárias **Relação de baixas (FINSV010)** é possível listar todas as baixas realizadas pelo job **(FINA715) e pelo** CNAB pós processamento do arquivo de retorno.

O histórico padrão gravado nos movimentos de baixa é **"Baixa por processo automático (API)"** e a origem do movimento FINA715 (**E5\_ORIGEM**).

**Mais informações:** [**Smart View - Relação de Baixas**](https://tdn.totvs.com/pages/releaseview.action?pageId=769164286)

**Saiba mais:**  
[**Smart View - Financeiro**](https://tdn.totvs.com/display/public/PROT/Smart+View+-+Financeiro)

[Smart View - Retorno CNAB](https://tdn.totvs.com/display/public/PROT/Smart+View+-+Retorno+CNAB)

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINSV051 - Leitura de arquivos no disco C:\](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37673949169687-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINSV051-Leitura-de-arquivos-no-disco-C)
