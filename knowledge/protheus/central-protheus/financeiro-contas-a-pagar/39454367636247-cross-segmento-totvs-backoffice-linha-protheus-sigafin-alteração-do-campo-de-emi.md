---
article_id: 39454367636247
category: Financeiro - Contas a Pagar
content_hash: a0766c1c9f79a871861827491b104fc741668f14d8dcd04f467051e1aec3c373
fetched_at: '2026-06-28T22:38:08.385440+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Alteração do
  campo de emissão no Contas a Pagar
type: support-article
updated_at: '2026-04-02T10:08:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39454367636247-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Altera%C3%A7%C3%A3o-do-campo-de-emiss%C3%A3o-no-Contas-a-Pagar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39454367620119) Tempo aproximado para leitura: 00**:05:00 min**  
  
**Dúvida**  
Após salvar um título no Contas a Pagar (FINA050), é possível alterar a data de emissão?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39454367621399)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice Linha Protheus - Financeiro - Todas as versões.  
  
**Solução**  
Por padrão de sistema, o campo de data de emissão (**E2\_EMISSAO** no Contas a Pagar) é bloqueados para edição após a gravação do título. Isso ocorre para garantir a integridade dos dados financeiros e a rastreabilidade contábil.

Caso exista uma necessidade de negócio que justifique a edição desse ou de outros campos bloqueados na rotina de Alteração, é possível utilizar pontos de entrada para habilitar o campo na interface.

* **Utilização do F050MCP (Contas a Pagar):** Para a rotina de Contas a Pagar (FINA050), pode-se utilizar o ponto de entrada **F050MCP**. Ele permite complementar a tela de alteração com campos adicionais ou modificar o status de campos existentes conforme a regra de negócio do cliente.

```
//Exemplo

#Include 'Protheus.ch'

User Function F050MCP()
Local aTeste := paramixb
AADD(aTeste,"E2_EMISSAO")	
Return aTeste
```

* Documentação técnica: [DT\_F050MCP\_Adiciona\_campos\_na\_alteracao\_do\_Contas\_a\_pagar](http://tdn.totvs.com/display/PROT/DT_F050MCP_Adiciona_campos_na_alteracao_do_Contas_a_pagar)
