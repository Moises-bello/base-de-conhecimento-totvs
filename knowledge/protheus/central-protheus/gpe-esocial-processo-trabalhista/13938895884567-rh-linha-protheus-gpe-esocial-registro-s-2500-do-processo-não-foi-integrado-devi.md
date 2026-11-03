---
article_id: 13938895884567
category: GPE - eSocial - Processo Trabalhista
content_hash: 46239e3da7615fdf015b185b788b67bb12e4c6be4d9412ab13c5a31d3190840e
fetched_at: '2026-06-28T22:45:00.617867+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - Registro S-2500 do Processo: não foi
  integrado devido ao(s) erro(s) abaixo: Erro 1 - O valor ''XXXXXX'' informado na
  tag codCBO não existe na base de dados'
type: support-article
updated_at: '2024-06-19T18:10:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13938895884567-RH-Linha-Protheus-GPE-eSocial-Registro-S-2500-do-Processo-n%C3%A3o-foi-integrado-devido-ao-s-erro-s-abaixo-Erro-1-O-valor-XXXXXX-informado-na-tag-codCBO-n%C3%A3o-existe-na-base-de-dados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24294430795415) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**O que verificar quando ocorrer o erro: Registro S-2500 do Processo: não foi integrado devido ao(s) erro(s) abaixo: Erro 1 - O valor 'XXXXXX' informado na *tag* codCBO não existe na base de dados?  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para verificar o CBO gerado no evento S-2500, acesse a rotina de Dados eSocial (TAFA552D).  
Clique nos três pontinhos para **editar o processo**:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/13938490285079)**Na aba **Contrato de Trabalho**, edite o contrato em questão gerado com erro no S-2500:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/13938286997399)**Na aba **Informações** **Complementares**, ajuste o campo Classificação Brasileira de Ocupações - CBO.   
**Salve** a alteração.  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/13938341434647)**Após salvar a alteração, gere novamente o evento S-2500 em Geração Processos Trabalhistas (GPEM038):  
[RH - Linha Protheus - GPE - eSocial - Processos Trabalhistas - Como realizar a geração dos eventos S-2500, S-2501 e S-3500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12412564333719)  
  
**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[Artigos RH Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971467-RH-Processos-Trabalhistas)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
  
**Próximos Treinamentos**  
[TOTVS RESPONDE TOTVS RH (TODAS AS LINHAS) ESOCIAL](https://rhinforma.totvs.com/2023/04/04/totvs-responde-totvs-rh-todas-as-linhas-esocial-processo-trabalhista/)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
