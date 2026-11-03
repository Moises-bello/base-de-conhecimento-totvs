---
article_id: 4421126537879
category: SIGAEST - LEGAIS
content_hash: 44bfa202821851b00dd30e812b8615b6043c77c7d363bf7c6c47587794e19baf
fetched_at: '2026-06-28T22:38:51.494136+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Bloco K- Conceito
  e configurações mínimas
type: support-article
updated_at: '2025-11-27T22:59:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421126537879-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Bloco-K-Conceito-e-configura%C3%A7%C3%B5es-m%C3%ADnimas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28806785237911)**Tempo aproximado para leitura: **00:05:10 min**

**Dúvida**  
Quais são as configurações mínimas do ambiente *Protheus* para geração do Bloco K (inclusive o 2023) do SPED Fiscal?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Neste artigo abordaremos as informações mais relevantes sobre o Bloco K

**Gravação - Webinar Bloco K (Realizado em Dezembro/2024)**

* [Bloco K: Layout de 2025](https://youtu.be/gBpvRO1pc2s?si=W7JLhlRLHsKneIiu)
* [Bloco K: Registro K200](https://youtu.be/d7xyzU14w7s?si=XrIeNeBxw4u66dUQ)
* [Bloco K: K200 divergente do Saldo Final do Estoque](https://youtu.be/4Ykj5v34I7c?si=bzt_6x6LG-18cwZ5)
* [Bloco K: Duplicidade no Registro K200](https://youtu.be/jokpTCAlBkA?si=JA2yKWE3dGrWp9wY)
* [Bloco K: Registro K220](https://youtu.be/AenLMb943iE?si=Ikzcki0Jq_bU2PKF)
* [Bloco K: Registro K280](https://youtu.be/VbPaB1awvcs?si=ePiHV2RcI88IUOCc)
* [Bloco K: Registros K250 e K255](https://youtu.be/-MoFQ0hrISw?si=6sZ3eofW4kZmnY-x)
* [Bloco K: Registros K270 e K275](https://youtu.be/G2-h86I1kKc?si=ycvPNLu_ye6jgBvI)
* [Bloco K: Tipos de Produtos](https://youtu.be/cfG4j5EVyrs?si=ADcGlbL8TU6mEtjW)
* [Bloco K: Mesmo tipo de Produto MV\_BLKTP](https://youtu.be/uXtHoe9PZTU?si=d9xqI0a2gnorodLX)
* [Bloco K: Produto não aparece](https://youtu.be/wW5FQskg1TE?si=Fn4ef12N2Nt6YBsb)
* [Bloco K: Saldo de terceiros a distribuir MATA037](https://youtu.be/3wjR6n3aj7A?si=--gd-IczuDzSrrIy)

Eventos anteriores:

* [Webinar Blcoo K (Janeiro/2023)](https://youtu.be/GunB7GiJljA?si=AyeRXm5aEGGarJVv)
* [Eventos Tira Dúvidas - Suporte Técnico](https://tdn.totvs.com/x/ZwXNI)

**Registros do Bloco K**

O Bloco K do SPED basicamente escritura o Estoque bem como algumas situações em que o mesmo envolve durante um período de apuração (normalmente mensal), dividido nos seguintes registros.

|  |  |  |
| --- | --- | --- |
| **Bloco** | **Descrição** | **Registro** |
| **K** | [**Abertura do Bloco K**](https://tdn.totvs.com/display/public/PROT/Registro+K001%3A+Abertura+do+Bloco+K) | **K001** |
| **K** | [**Informação sobre o tipo de leiaute (simplificado / completo)**](https://tdn.totvs.com/pages/releaseview.action?pageId=715149444) | **K010** |
| **K** | [**Período de Apuração do ICMS/IPI**](https://tdn.totvs.com/pages/releaseview.action?pageId=259560064) | **K100** |
| **K** | [**Estoque Escriturado**](https://tdn.totvs.com/display/public/PROT/Registro+K200%3A+Estoque+Escriturado) | **K200** |
| **K** | [**Desmontagem de mercadorias – Item de Origem**](https://tdn.totvs.com/display/public/PROT/Registro+K210%3A+Desmontagem+de+Mercadorias+-+Itens+de+Origem) | **K210** |
| **K** | [**Desmontagem de mercadorias – Item de Destino**](https://tdn.totvs.com/display/public/PROT/Registro+K215%3A+Desmontagem+de+Mercadorias+-+Itens+de+Destino) | **K215** |
| **K** | [**Outras Movimentações Internas entre Mercadorias**](https://tdn.totvs.com/pages/releaseview.action?pageId=259560142) | **K220** |
| **K** | [**Itens Produzidos**](https://tdn.totvs.com/display/public/PROT/Registro+K230%3A+Itens+Produzidos) | **K230** |
| **K** | [**Itens Consumidos**](https://tdn.totvs.com/pages/releaseview.action?pageId=259560161) | **K235** |
| **K** | [**Industrialização Efetuada por Terceiros – Itens Produzidos**](https://tdn.totvs.com/pages/releaseview.action?pageId=259560200) | **K250** |
| **K** | [**Industrialização em Terceiros – Insumos Consumidos**](https://tdn.totvs.com/pages/releaseview.action?pageId=259560350) | **K255** |
| **K** | [**Reprocessamento/Reparo de Produto/Insumo**](https://tdn.totvs.com/pages/releaseview.action?pageId=259560367) | **K260** |
| **K** | [**Reprocessamento/Reparo – Mercadorias Consumidas e/ou Retornadas**](https://tdn.totvs.com/pages/releaseview.action?pageId=259560508) | **K265** |
| **K** | [**Correção de Apontamento dos Registros K210, K220, K230, K250 e K260**](https://tdn.totvs.com/pages/releaseview.action?pageId=259560564) | **K270** |
| **K** | [**Correção de Apontamento e Retorno de Insumos dos Registros K215, K220, K235, K255 e K265**](https://tdn.totvs.com/pages/releaseview.action?pageId=259560530) | **K275** |
| **K** | [**Correção de Apontamento – Estoque Escriturado**](https://tdn.totvs.com/pages/releaseview.action?pageId=259560569) | **K280** |
| **K** | [**Produção Conjunta – Ordem de Produção**](https://tdn.totvs.com/pages/releaseview.action?pageId=425454429) | **K290** |
| **K** | [**Produção Conjunta – Itens Produzidos**](https://tdn.totvs.com/pages/releaseview.action?pageId=425454929) | **K291** |
| **K** | [**Produção Conjunta – Insumos Consumidos**](https://tdn.totvs.com/pages/releaseview.action?pageId=425455043) | **K292** |
| **K** | [**Produção Conjunta – Industrialização Efetuada por Terceiros**](https://tdn.totvs.com/pages/releaseview.action?pageId=415706361) | **K300** |
| **K** | [**Produção Conjunta – Industrialização Efetuada por Terceiros – Itens Produzidos**](https://tdn.totvs.com/pages/releaseview.action?pageId=415706382) | **K301** |
| **K** | [**Produção Conjunta – Industrialização Efetuada por Terceiros – Insumos Consumidos**](https://tdn.totvs.com/pages/releaseview.action?pageId=415706402) | **K302** |
| **K** | [**Encerramento do Bloco K**](https://tdn.totvs.com/pages/releaseview.action?pageId=415706402) | **K990** |

Informações extraídas do Guia Prático da Escrituração Fiscal Digital - EFD.

Link para baixar o Guia Prático da Escrituração Fiscal Digital - EFD na última versão - [**Clique Aqui**](http://sped.rfb.gov.br/pasta/show/1573)

**Quais os Leiautes do Bloco K?**

De acordo com a imagem abaixo, assim discrimina-se os Leiautes do Bloco K e respectivos Registros gerados por cada um. Lembrando que a definição do Leiaute é feito pela Equipe Fiscal da empresa:

![ESCOPOS.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12726238225943)

Para obter maiores detalhes sobre cada Registro nos 3 Leiautes, [**clique aqui**](https://tdn.totvs.com/pages/releaseview.action?pageId=727365029)

**O que é necessário para gerar o Bloco K?**

**Mantenha seu ambiente atualizado**

O primeiro ponto a se analisar antes de começar a gerar o Bloco K é certificar-se de que os fontes de Livros Fiscais, Estoque e Manufatura (para empresas que vão entregar o Bloco K completo) estejam plenamente atualizados.

|  |
| --- |
| [**Pacote Acumulado Estoque/Custos**](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/EST_expedicao_continua) |
| [**Pacote Acumulado Livros Fiscais**](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/FIS_expedicao_continua) |
| [**Pacote Acumulado Manufatura (PCP)**](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/PCP_expedicao_continua) |

**Avalie os Tipos de Produto que são padrões do Bloco K**

Por padrão o SPED Fiscal considera os seguintes tipos de produto a serem levados no arquivo fiscal:

|  |  |  |
| --- | --- | --- |
| **Tipo** | **Descrição** | **Tipo Padrão no Protheus** |
| 00 | Mercadoria para Revenda | ME |
| 01 | Matéria-Prima | MP |
| 02 | Embalagem | EM |
| 03 | Produto em Processo | PP |
| 04 | Produto Acabado | PA |
| 05 | Subproduto | SP |
| 06 | Produto Intermediário | PI |
| 10 | Outros Insumos | OI |

Porém, em algumas situações é necessário a utilização de outros tipos de produtos, conforme a regra de negócio da empresa. Por este motivo foi criado o parâmetro **MV\_BLKTP\*\*** que, conforme tipo do produto poderá informar o conteúdo e assim ele poderá ser considerado no Bloco K. O detalhamento do uso do parâmetro pode ser acessado [**clicando aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033136554)

**Gere o SPED Fiscal com o Bloco K**

A partir das verificações acima, o usuário já poderá gerar o SPED Fiscal com o Bloco K. Para isso, basta acessar ao módulo *Menu 09 - Livros Fiscais -> Arquivos Magnéticos-> Sped Fiscal*

No *Wizard*da rotina SPEDFISCAL, preencha o período de apuração, local do arquivo e nome do arquivo e atente-se em preencher o campo "Gera Bloco K". As opções **0 (Leiaute Simplificado), 1 (Leiaute Completo) e 3 (Leiaute restrito aos Saldos de Estoque - K200 e K280)** gerarão o Bloco K ao final do processamento.

![bloco k wizard.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12725253089303)

Importante: A definição do Leiaute a ser gerado deve ser confirmada com o Fiscal interno da empresa.

**Rotinas e Fontes envolvidos na geração do BLOCO K**

|  |  |
| --- | --- |
| **Rotina** | **Descrição** |
| MATXSPED.PRW | Contém as funções para geração dos registros 0210, K200, K220, K250, K255, K270, K275, K280, K300, K301 e K302. |
| PCPXSPED.PRW | Contém as funções para geração dos registros K230, K235, K260, K265, K270, K275, K290, K291 e K292 |
| SPEDFISCAL.PRW,  SPEDXFUN.PRW | Rotina responsável pela geração de todos os blocos utilizados para entrega do SPEDFISCAL.  No caso do Bloco K, esta rotina é responsável pela geração dos registros K001, K100 e K990. |
| MATR241 | O relatório de Relação do Bloco K. |

**Relatório Relação do Bloco K - MATR241**

O relatório de Relação do **Bloco****K** (**MATR241**) que lista todos os dados processados e que serão gravados nos Registros do Bloco K do SPED Fiscal, utilizam o mesmo componente responsável pelo processamento do Bloco K presente na rotina SPEDFISCAL, dessa forma, os dados resultantes entre ambas as rotinas são os mesmos. Ele tem como objetivo facilitar a análise dos dados gerados pelo Bloco K, isolando os pontos processados pela equipe de Materiais e Fiscal e apresentar as informações ao usuário de forma amigável. Os componentes responsáveis pela geração do Bloco K, geram os registros K001, K100 e K990, porém, quando o processamento é realizado através da rotina SPEDFISCAL, eles são ignorados e gerados dentro do próprio SPEDFISCAL. Dentro do relatório eles são apenas informativos.

O relatório possui os seguintes parâmetros:

* **Do período:**Período inicial do processamento.
* **Até o período**: Período final do processamento.
* **Reg. 0210 por movimento**: Indica se gera o registro 0210 por movimentação. Caso marcado como NÃO, o registro 0210 é gerado **Por Estrutura**.
* **Detalhar K250/K255**: Indica se detalha ou não os Registros K250/K255. Por padrão os registros são gerados no SPEDFISCAL sem detalhamento.

**Saiba mais:**

[*Guia de Referência do Bloco K - TDN*](https://tdn.totvs.com/pages/releaseview.action?pageId=235589625)

[*Link para download do Guia Prático da Escrituração Fiscal Digital - EFD na última versão*](http://sped.rfb.gov.br/pasta/show/1573)

[*MP - SIGAEST- Como definir um tipo de produto que não seja padrão do sistema para que seja considerado no Bloco K (K200)?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033136554-MP-SIGAEST-Como-definir-um-tipo-de-produto-que-n%C3%A3o-seja-padr%C3%A3o-do-sistema-para-que-seja-considerado-no-Bloco-K-K200-?source=search)

[*Clique aqui e veja mais artigos sobre Legais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)
