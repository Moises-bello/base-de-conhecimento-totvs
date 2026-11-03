---
article_id: 360051919493
category: RH - Leitura e Apontamento
content_hash: 1c7b691839c311eafd7c48d8d24e1f712b331eddd780a4abfc501be37f7dc944
fetched_at: '2026-06-28T22:44:46.009406+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON - Segunda leitura das marcações não é executada
type: support-article
updated_at: '2025-06-16T17:45:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051919493-RH-Linha-Protheus-PON-Segunda-leitura-das-marca%C3%A7%C3%B5es-n%C3%A3o-%C3%A9-executada
---

**Ocorrência**No módulo Ponto Eletrônico, só consigo realizar uma nova Leitura se apagar o conteúdo da tabela RFB  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**  
1) Cada REP deve ter um arquivo.txt diferente do outro, sem repetir o nome e nunca lermos mais de um relógio no mesmo cadastro. Ou seja, se a Empresa tiver 10 relógios, serão 10 arquivo txt diferentes e 10 cadastros de relógios no Protheus distintos;  
2) O próprio REP físico está "restartando" a sequência inicial no NSR (número sequencial de registro), assim a RFB iria ter registros lidos maiores que os atuais a ler, impossibilitando a leitura.  
  
**Solução**Cada REP físico deverá ter seu cadastro de relógio diferente no Protheus, por isso, deverão cadastrar outros relógios no Sistema e ler, individualmente com um arquivo.txt diferente do outro;  
Verificar com o fornecedor do relógio ou no próprio aparelho, se por algum problema de *hardware*o NSR não está reiniciando a cada extração das marcações  
  
**Saiba mais em:**  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013080592-MP-PON-Erros-frequentes-no-processo-de-Leitura-e-Apontamento-no-m%C3%B3dulo-Ponto-Eletr%C3%B4nico?source=search>  
  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016068372-MP-PON-Funcionalidade-da-tabela-RFB-e-como-controlar-a-leitura-para-que-o-NSR-n%C3%A3o-ocasione-erros-no-processo?source=search>  
  
**Informações complementares**  
Pacote de Expedição Contínua do RH: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>  
  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
