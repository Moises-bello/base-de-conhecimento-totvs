---
article_id: 360035003473
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 4ca212964d0309d782988ce1357764f63f4fd83f90b5c2947d3b71cf889a68ef
fetched_at: '2026-06-28T22:45:20.948665+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Configuração - Como realizar limpeza
  de inconsistências
type: support-article
updated_at: '2026-06-26T11:54:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035003473-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Como-realizar-limpeza-de-inconsist%C3%AAncias
---

**Ocorrência**Ao consultar o status de integração no ERP RM e-Social para um ou mais eventos, não é possível obter as informações de status corretas, pois elas não são atualizadas.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Rotinas Comuns - Todas as versões.  
  
  
**Causa**Esse erro ocorre devido ao histórico de erros de integração.  
  
**Solução**

Para solucionar esse problema, siga as etapas abaixo:

1. Acesse a rotina de ajuste de inconsistência, localizada no menu Miscelânea ► ajuste de base ► Limpeza de inconsistência.
2. Na nova janela que se abre, marque apenas as opções "**Apagar Rejeitados da TAFST2**" e "**Somente Integrados**" e clique em Confirmar.  
   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044738534)
3. Confirme novamente a execução da rotina e aguarde o término do processo. Dependendo da quantidade de registros em seu sistema, esse processo pode demorar alguns minutos para ser concluído.  
   ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045594733)
4. Após a conclusão, consulte novamente o status de integração no ERP para verificar se as mensagens estão sendo exibidas corretamente.
