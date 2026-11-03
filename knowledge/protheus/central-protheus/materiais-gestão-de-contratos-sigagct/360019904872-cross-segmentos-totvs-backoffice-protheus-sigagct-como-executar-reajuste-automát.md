---
article_id: 360019904872
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: c2aa01ae5443882fcf7cba5a6e46bc677572b2cf42899bbd4ef44b15e9ddaefd
fetched_at: '2026-06-28T22:37:19.998541+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como Executar Reajuste
  Automático via Índices ?
type: support-article
updated_at: '2022-05-19T20:47:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019904872-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-Executar-Reajuste-Autom%C3%A1tico-via-%C3%8Dndices
---

**Dúvida**

Como Executar Reajuste Automático via Índices ?  
  
**Ambiente**

Protheus - Gestão de contratos - Release 12.1.17

**Solução**

Para solucionar essa dúvida, realize os seguintes passos:

1. Efetue o cadastros:

```
SIGAGCT->Cadastros->Financeiro->Índices (CNTA070)  
SIGAGCT->Cadastros->Financeiro->Histórico de Índices(CNTA080)  
CN7_VLREAL  
CN7_VLPROJ  
CN7_TPPROJ
```

2. Cadastre um novo Contrato de Venda/Compras conforme segue e deixe-o vigente;

```
- Vincule o índice de reajuste no campo CN9_INDICE  
- Atenção para o preenchimento dos campos do cabeçalho da planilha:  
  CNA_FLREAJ = Sim; CNA_PERI; CNA_MODORJ = 1; CNA_PROXRJ
```

3. Acesse o módulo GCT com uma data base igual a data do campo CNA\_PROXRJ;

4- Acesse a rotina de Reajuste Automático (CNTA310), e configure as perguntas dos parâmetros;

**\*Atenção para as datas de Referência e Aplicação do Reajuste!**

5. Verifique os resultados do Reajuste nas Planilhas e Cronogramas do Contrato

**Saiba Mais:**

* [Reajuste automático - CNTA310 - Gestão de Contratos - P12](https://tdn.totvs.com/pages/viewpage.action?pageId=333777355)
* [MP - SIGAGCT - Como realizar a Configuração e Revisão de Reajuste em Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059174393-MP-SIGAGCT-Como-realizar-a-Configura%C3%A7%C3%A3o-e-Revis%C3%A3o-de-Reajuste-em-Contratos-)
* [Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
