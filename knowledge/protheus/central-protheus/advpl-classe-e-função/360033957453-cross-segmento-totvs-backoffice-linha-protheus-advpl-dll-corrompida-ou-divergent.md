---
article_id: 360033957453
category: ADVPL - Classe e Função
content_hash: 342081bc6a406d673b5ce5e0935d39c801b1a5f0a88250c5a591bfa3224d668b
fetched_at: '2026-06-28T22:40:15.771710+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - DLL corrompida ou
  divergente para arquitetura da aplicação smartclient
type: support-article
updated_at: '2022-04-11T11:36:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033957453-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-DLL-corrompida-ou-divergente-para-arquitetura-da-aplica%C3%A7%C3%A3o-smartclient
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**É retornado erro ao utilizar as funções de manipulação de .DLL (ex: ExecInDLLOpen()).  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.23  
  
**Causa**Isto ocorre quando o sistema não consegue realizar a troca de informações corretamente, assim sendo gerado o retorno -1.  
  
**Solução**Validar se a .DLL corrompida ou divergente para a arquitetura da aplicação (SmartClient).  
  
**Exemplo**Em um SmartClient 64 *bits* (IsRmt64() == .T.) temos uma .DLL (*Dynamic-Link Library*) que retorna o código -1 em um *remote* x64, porém retorna 1 em *remote* x86.  
Com base neste cenário, executaremos o comando FILE (presente em ambientes Linux ou aplicações que simulem o ambiente, neste caso, utilizamos o Git Bash) para validar a arquitetura:

```
$ file MINHA_BIBLIOTECA.dll  
MINHA_BIBLIOTECA.dll: PE32 executable (DLL) (GUI) Intel 80386, for MS Windows
```

Como pode ser visto, esta .DLL foi desenvolvida com base na arquitetura x86 (803**86**), assim sendo, não será executada com sucesso em um ambiente x64. Desta forma, tornando necessária a recompilação com base na arquitetura x64.  
  
**Saiba mais**  
[ExecInDLLOpen](http://tdn.totvs.com/display/tec/ExecInDLLOpen)
