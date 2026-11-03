---
article_id: 360052170574
category: NFe - Nota Fiscal Eletrônica
content_hash: d55f9944543f17c07dad0a9a7ff281c5f2ed570a63b0bdadfdf12cab21666c19
fetched_at: '2026-06-28T22:40:01.758448+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar o LogProfiler'
type: support-article
updated_at: '2023-10-04T19:01:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052170574--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-o-LogProfiler
---

**Dúvida**Como gerar o LogProfiler nas rotinas de transmissão de documentos eletrônicos?  
**Ambiente**Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - A partir da versão 12.1.XX.

**Solução**Para gerar o arquivo de LogProfiler é necessário acessar a rotina que gera a lentidão ou alguma inconsistência de performance no produto:  
  
Para evidenciar o processo será usado como exemplo a rotina SPEDNFE responsável pela transmissão de NF-e:  
  
Acesse o modulo do faturamento > Atualizações > NF-e e NFS-e > NF-e SEFAZ > dentro da rotina execute o SHIFT+F6(antes de realizar o processo) > No Profiler de execução clicar em INICIAR.

Obs.: Após iniciar o processo, avançar até concluir.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083946434)

Após iniciar o processo de geração do LogProfiler, reproduza o erro que gera a inconsistência no ambiente e finalize a geração do log executando novamente o SHIFT+F6 > No Profiler de execução clicar em Finalizar.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085133013)

Salve o arquivo enviado em um diretório de fácil acesso e envie o mesmo ao suporte para prosseguir com a analise.  
  
Existe outro forma de gerar logs profile, realizando a configuração pelo Appserve.ini da aplicação conforme o procedimento da documentação:   
- <https://tdn.totvs.com/display/public/PROT/LogProfiler+-+Como+executar>

Obs.: É recomendado para processos mais longos como geração do SPEDFISCAL ou em rotinas que utilizam multi-threads.   
  
Nas rotinas de transmissão de NF-e, MDF-e, MD-e, CC-e, GNR-e, NFS-e e CTE-OS gere direto pela rotina.
