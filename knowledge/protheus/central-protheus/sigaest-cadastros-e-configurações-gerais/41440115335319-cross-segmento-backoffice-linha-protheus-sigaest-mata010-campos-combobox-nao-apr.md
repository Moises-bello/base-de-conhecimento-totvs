---
article_id: 41440115335319
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 468732933c42bc410a59832d8c1ee80b38829602d91ae553f4c7c07e9404c298
fetched_at: '2026-06-28T22:39:09.405813+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - Campos combobox
  nao apresentam dados no browser
type: support-article
updated_at: '2026-06-23T20:59:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41440115335319-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Campos-combobox-nao-apresentam-dados-no-browser
---

O preenchimento de opções em campos Combobox no Protheus falha quando informado apenas a lista de descrições (ex: TESTE1;TESTE2;TESTE3) porque o sistema exige o formato "Chave=Valor" no atributo X3\_CBOX do Dicionário de Dados. A chave é o valor armazenado no banco (ex: T1), e o valor é a descrição exibida (ex: TESTE1). Sem essa estrutura, a interface não associa o dado visual ao real, causando falha na exibição.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41440138609943) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Por que o preenchimento de opções em campos do tipo Combobox (CBOX) no Dicionário de Dados falha ao informar apenas a lista de descrições (como TESTE1;TESTE2;TESTE3), resultando em campo vazio na interface ou quebra de renderização no Browser, não apresentado o conteudo contido nele?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O comportamento ocorre porque a arquitetura do Protheus em ADVPL para campos do tipo Combobox exige o formato de **"Chave=Valor"** no atributo de opções **(X3\_CBOX)** do Dicionário de Dados.

Quando são informadas apenas as descrições sem o sinal de igualdade, o framework de interface (FWmBrowse) não consegue montar a matriz interna de opções, pois não identifica o que deve ser gravado no banco de dados em relação ao que foi selecionado pelo usuário.

A estrutura correta deve separar explicitamente o dado de armazenamento e o dado de exibição, conforme a regra abaixo:

* **Chave (antes do sinal de igual):** É a chave relacional e o dado real que será armazenado fisicamente na coluna da tabela no banco de dados (exemplo: T1, T2, T3). Esse valor geralmente corresponde e otimiza o tamanho exato do campo (X3\_TAMANHO).
* **Valor (depois do sinal de igual):** É a descrição visual ou rótulo que será renderizado no SmartClient para leitura do usuário final (exemplo: TESTE1;TESTE2;TESTE3).

A ausência deste mapeamento impede o componente de tela de associar a descrição visual ao valor real do banco de dados, quebrando a integridade de exibição.

**OBS:** Não esqueça de marcar como "Usado/Browser" para que ele seja apresentado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41440115329431)

**Maneira incorreta:**

TESTE1;TESTE2;TESTE3

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41440138612247)

**Maneira correta:**

T1=TESTE1;T2=TESTE2;T3=TESTE3

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41440138612887)

**Saiba mais:**

[*Clique aqui para mais informações sobre a MATA010*](https://tdn.totvs.com/display/public/PROT/Produtos+-+MATA010#ProdutosMATA010-PastaCadastrais)

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
