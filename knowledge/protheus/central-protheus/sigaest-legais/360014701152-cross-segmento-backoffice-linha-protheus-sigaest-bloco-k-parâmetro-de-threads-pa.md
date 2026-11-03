---
article_id: 360014701152
category: SIGAEST - LEGAIS
content_hash: 5c7f5872f6684afc516b40616151d693966b9d2241443ab5179a37138d09967b
fetched_at: '2026-06-28T22:38:51.432286+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Bloco K -  Parâmetro
  de threads para ganho de performance
type: support-article
updated_at: '2025-03-12T12:23:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014701152-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Bloco-K-Par%C3%A2metro-de-threads-para-ganho-de-performance
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28806550053655)** Tempo aproximado para leitura: **00:09:10 min**

**Dúvida**Existe a possibilidade de quebrar o bloco K em threads para ganho de perofrmance?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**Para melhoria de performance no registro **K200**, verifique se o Processo **14 de Stored Procedures está instalado.**

**Para consulta, acesse o módulo Configurador (SIGACFG).**

Para configuração de multi-threads no processamento do Registro K200, é necessário incluir o parâmetro **MV\_BLKMTHR** via configurador com as seguintes informações:

| **Variável** | MV\_BLKMTHR |
| **Tipo** | Numérico |
| **Descrição** | Define o número de threads que serão utilizadas  No processamento do **Bloco K** do SPED Fiscal.  (1 a 20 threads) |
| **Conteúdo** | 1 |

O processamento multi-threads está limitado ao **máximo de 20 threads nesse processo**. A alteração da quantidade de threads deve ser feita com critério, **pois pode impactar na performance do sistema como um todo, pois depende da infraestrutura que o suporta.**

Sugerimos que para definir a quantidade final de threads que serão utilizadas no ambiente, sejam realizados testes incrementando o valor do parâmetro para encontrar a maior quantidade de threads com a melhor performance.

**Lembramos que o processamento Multi-Threads não consome licenças do Protheus, no entanto, caso o cliente utilize Ctree Server será consumida uma licença por Thread aberta.**

**Saiba mais:**

*[Guia de Referência do Bloco K - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=235589625)*

*[Link para download do Guia Prático da Escrituração Fiscal Digital - EFD na última versão](http://sped.rfb.gov.br/pasta/show/1573)*

*[MP - SIGAEST- Como definir um tipo de produto que não seja padrão do sistema para que seja considerado no Bloco K (K200)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033136554-MP-SIGAEST-Como-definir-um-tipo-de-produto-que-n%C3%A3o-seja-padr%C3%A3o-do-sistema-para-que-seja-considerado-no-Bloco-K-K200-?source=search)*

*[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)*
