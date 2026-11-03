---
article_id: 19634781653143
category: TAF - REINF
content_hash: 292e7c307688a74c1792a1638f5381511f34ff7128cc1fa3d433ec6298f3c2cf
fetched_at: '2026-06-28T22:41:34.647113+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Erro de integração T154
type: support-article
updated_at: '2025-09-09T15:50:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19634781653143-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Erro-de-integra%C3%A7%C3%A3o-T154
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19634770938519) Tempo aproximado para leitura: 00:04:00 min****Ocorrência**Ao integrar os movimentos do bloco 40  para o TAF ocorre o erro abaixo no Layout  T154:

![mceclip0 (1).png](https://centraldeatendimento.totvs.com/hc/article_attachments/19634767082135)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATAF - Todas as versões  
  
**Causa**Essa situação pode surgir devido ao layout T154 estar associado à nota fiscal  e o layout responsável pelas notas (T013) não foi integrado.

**Solução**

Verifique se o layout T013 foi gerado corretamente no gerenciador de integração. Caso não tenha sido gerado, isso pode ocorrer por diversos motivos:

1- Quando a nota não gera livro fiscal (TES sem livro), ou seja, a nota não é incluída na tabela **SFT**. Para corrigir, é necessário alterar o livro na TES e reprocessar a nota para que seja registrada na **SFT**.

2- Se qualquer filtro na aba Movimento do extrator fiscal for utilizado, o que pode impedir a geração do T013 (por exemplo, espécie, série, número da nota ou se é entrada ou saída).

3- Quando a data de entrada **(FT\_ENTRADA)** da nota difere da data informada no filtro do extrator. Nesse caso, é necessário informar o mesmo período da **FT\_ENTRADA** no extrator fiscal.

4-  Outra possibilidade reside no **TAFAINTEG**, ao utilizar multithread, caso o parâmetro **MV\_TAFLPRC** esteja vazio e não contenha o conteúdo padrão "2000". Isso pode causar um problema onde o T013 ficará pendente na **TAFST2**.

**Após identificar a causa de não integrar o T013 e corrigir, valide o passo 3 da documentação abaixo do time financeiro, todas faturas e pagamentos do financeiro após integradas no TAF precisa tirar o bloqueio para uma nova integração.**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - O que fazer quando executamos o Extrator Fiscal e o registro do título não aparece no painel do TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19677367875607-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-O-que-fazer-quando-executamos-o-Extrator-Fiscal-e-o-registro-do-t%C3%ADtulo-n%C3%A3o-aparece-no-painel-do-TAF)

Caso tenha duvidas sobre bloqueio, por favor contatar suporte financeiro para maiores esclarecimentos.
