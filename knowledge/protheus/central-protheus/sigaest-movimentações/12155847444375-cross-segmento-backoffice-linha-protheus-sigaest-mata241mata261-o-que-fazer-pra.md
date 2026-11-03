---
article_id: 12155847444375
category: SIGAEST - MOVIMENTAÇÕES
content_hash: a515002e970e223aa00a24f0b935a465bbd5737706026a7dc6e13205715f483b
fetched_at: '2026-06-28T22:38:56.994850+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA241/MATA261 -
  O que fazer pra corrigir o Help A240DOC?
type: support-article
updated_at: '2025-01-10T11:32:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12155847444375-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA241-MATA261-O-que-fazer-pra-corrigir-o-Help-A240DOC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16942780186007) Tempo aproximado para leitura: **00:01:26 min****Dúvida**Ao efetuar movimentações por meio de rotinas como: Movimentação Interna (MATA241), Transferência Múltipla (MATA261), e afins, ocorre o Help A240DOC. Como corrigir este problema?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12155498507543)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Este help normalmente é apresentado quando, o número do documento (D3\_COD) que o sistema está tentando inserir na tabela (SD3), **já existe dentro do ambiente, impedindo de concluir a inclusão.**

Essas rotinas obrigam que seja informado um número de documento e usa a função **NEXTNUMERO** para controle de sequencia para o campo 'cDocumento' que será gravado na tabela SD3 no campo D3\_DOC

A função **NEXTNUMERO** (**[Clique aqui para maiores informações](https://tdn.totvs.com/pages/releaseview.action?pageId=6814928)**) usa recursos de eliminar intervalos de sequencia, onde havendo uma sequencia 1, 2, 3, 10 existente na tabela irá trazer o 4, 5, 6, 7, 8, 9 e 11 como próxima sequencia.

**Importante:**

A movimentação com caractere especial no documento, como por exemplo: '[', pode interferir na busca de sequencias pela função NEXTNUMERO, pois o caractere '[' encontra-se classificado na tabela ASCII após as letras maiúsculas e antes das letras minúsculas, portanto no fim da classificação e a próxima sequencia numérica valida para o campo com tamanho de 6 é 000001 e enquanto existir este D3\_DOC = '[' o controle de numeração irá trazer o próximo 000001 **pois '[' seria o maior código de documento possível**

Considerando que o documento '[' não é um dado correto e nem pode ser considerado como um número de documento, a melhor opção é atualizar este documento com um número valido e a sequencia voltará a funcionar.

|  |
| --- |
| **Sabendo disso, quando no ambiente existe caractere especial no campo D3\_DOC, a função NEXTNUMERO não consegue seguir a sequencia correta de numeração do campo, buscando um número já existente.** |

**Proposta de Solução do Suporte para esta ocorrência**

Para este cenário é orientado ajustar os registros da SD3 retirando os caracteres especiais e espaços em branco, para correto funcionamento da função NEXTNUMERO e resolução do Help, porém o Suporte Padrão não atua neste tipo de orientação, pois no padrão não existe uma rotina para tratamento de alteração do Documento da SD3. 

Para este cenário recomendamos avaliar internamente com consultores/área de TI da empresa efetuar tais validações. Caso a empresa não queira/não tenha conhecimento para efetuar, é recomendável acionar um consultor especialista para que seja feito de maneira a não causar colaterais.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
