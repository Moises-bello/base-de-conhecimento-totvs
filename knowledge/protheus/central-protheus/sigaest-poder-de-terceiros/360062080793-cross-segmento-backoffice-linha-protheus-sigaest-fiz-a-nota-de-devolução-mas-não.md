---
article_id: 360062080793
category: SIGAEST - PODER DE TERCEIROS
content_hash: b5ce694a6e3a68d66bc22c698ef7772e33afe186ec09d662bce471c2120794ea
fetched_at: '2026-06-28T22:39:03.192027+00:00'
product: protheus
section_id: 1500001538881
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Fiz a nota de devolução
  mas não deu baixa no Poder de Terceiros. O que fazer?
type: support-article
updated_at: '2021-06-14T14:26:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062080793-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Fiz-a-nota-de-devolu%C3%A7%C3%A3o-mas-n%C3%A3o-deu-baixa-no-Poder-de-Terceiros-O-que-fazer
---

**Dúvida**Fiz a nota de devolução para dar baixa no Poder de Terceiros mas no meu relatório MATR460 (P7) o saldo ainda continua lá. O que fazer para resolver este problema?  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Para solucionar este problema, siga os passos abaixo.

**Valide se de fato o movimento da nota de devolução foi feito com as informações corretas.**

Para haver uma baixa da devolução do poder de terceiros, existem algumas coisas que correlacionam esta com a remessa, tais como:

- TES de Devolução precisa estar "amarrada" à TES de Remessa. Exemplo: ao enviar produto ao terceiro usa TES com **F4\_ESTOQUE = S e F4\_PODER3 = Remessa**. Na devolução, deve-se utilizar TES com **F4\_ESTOQUE = S e F4\_PODER3 = Devolução**;

- Avalie o tipo da nota. Se a devolução for feita via Documento de Entrada, sendo N (Normal), habilitará o campo de Fornecedor (Tabela SA2) e se for B (Beneficiamento), habilitará o campo de Cliente (Tabela SA1);

- Avalie se na tabela SB6, ao efetuar a devolução foi gerado o campo movimento com o campo B6\_IDENT idêntico ao do movimento da Remessa. Essa é uma premissa de análise para entender se o sistema está correlacionando os movimentos.

- Avalie se o movimento foi com TES que não atualiza estoque. Pois, se o TES não atualiza, é necessário validar o parâmetro MV\_SDTESN3 para que a impressão do MATR460 satisfaça o seu objetivo. **[Clique aqui e saiba mais sobre este parâmetro.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060289014)**

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Poder de Terceiros no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538881-SIGAEST-PODER-DE-TERCEIROS)*

*[Clique aqui e veja mais artigos sobre Bloco H/MATR460 (P7) no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000219382-LEGAIS-BLOCO-H-MATR460-P7-)*
