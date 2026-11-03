---
article_id: 360049726394
category: Inspeção de Processos (SIGAQIP)
content_hash: 0a1f76b1f21b2a1ad6afd2c98719f0f24d41b8c788500dc465c68443de2d662f
fetched_at: '2026-06-28T22:42:25.943913+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Skip-lote
type: support-article
updated_at: '2026-06-09T11:54:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049726394-Manufatura-Linha-Protheus-SIGAQIP-Skip-lote
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27215025154583)*** Tempo aproximado para leitura: **00:04:55 min**  
  
**Dúvida**  
Quais as configurações necessárias para utilizar o conceito de *skip-lote* no módulo **SIGAQIP - Inspeção de Processos**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Solução**  
Para utilizar o conceito de *skip-lote*, seguir os passos descritos a seguir:  
1. Quando o parâmetro **MV\_QINSPEC - Indica, onde será realizada a Inspeção do Material quando houver integração QIP x PCP** tiver o conteúdo igual a **1 - Produção** deverá**:**

* Informar o conteúdo do parâmetro **MV\_QPSKLPR - No.de Produções iniciais para a aplicação do Skip-lote (**[**MV\_QPSKLPR - Informações Complementares sobre o uso do parâmetro**](https://tdn.totvs.com/pages/releaseview.action?pageId=1037968061)**)**;
* Verificar qual tipo de *skip-lote* será aplicado ao produto na rotina **QIPA130 - Skip-Lote (**[**Skip-lote**](https://tdn.totvs.com/pages/releaseview.action?pageId=545645324)**)**;
* Na rotina **QIPA010 - Especificação do Produto**, informar qual tipo de *skip-lote* será utilizado no campo **Skip-lote**.

2. Quando o parâmetro **MV\_QINSPEC - Indica, onde será realizada a Inspeção do Material quando houver integração QIP x PCP** tiver o conteúdo igual a **2 - Apontamento** deverá**:**

* Configurar o parâmetro MV\_PRAPONT - Define Prioridade no Apontamento de Produção x Envio para CQ   SIGAQIP - Inspeção de Processos. ([MV\_PRAPONT - Informações Complementares sobre o uso do parâmetro)](https://tdn.totvs.com/pages/releaseview.action?pageId=1037967492)

  **Observação**  
  Caso o parâmetro **MV\_PRAPONT tenha conteúdo igual a 1** e o campo **Envia produção para C.Q.? tenha conteúdo igual a Não** marcado na rotina **MATA230 – Tipos de Movimentação**, ou **MV\_PRAPONT com conteúdo igual a 2** e o campo **Produção CQ com conteúdo igual a 0** na rotina **MATA010 -Produtos**, a inspeção entrará no fluxo do Laudo Aprovado Automaticamente ([Manufatura - Linha Protheus - SIGAQIP - Laudo aprovado automaticamente em Apontamento de Produção)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8338110088343-Manufatura-Linha-Protheus-SIGAQIP-Laudo-aprovado-automaticamente-em-Apontamento-de-Produ%C3%A7%C3%A3o).
* Informar o conteúdo do parâmetro **MV\_QPSKLPR - No.de Produções iniciais para a aplicação do Skip-lote (**[**MV\_QPSKLPR - Informações Complementares sobre o uso do parâmetro**](https://tdn.totvs.com/pages/releaseview.action?pageId=1037968061)**)**;
* Verificar qual tipo de *skip-lote* será aplicado ao produto na rotina **QIPA130 - Skip-Lote (**[**Skip-lote**](https://tdn.totvs.com/pages/releaseview.action?pageId=545645324)**)**;
* Na rotina **QIPA010 - Especificação do Produto**, informar qual tipo de *skip-lote* será utilizado no campo **Skip-lote**.  
    
  **Importante**
* Quando a especificação for configurada com **Skip-Lote Free-Pass**, o campo **QP6\_TMPLIM - Tempo Limite** é desconsiderado na aplicação da regra, desta forma independentemente do **Tempo Limite**, todos os resultados serão **Certificados**.
* Quando o parâmetro **MV\_QPSKLPR** estiver com conteúdo igual à **0**, será considerado apenas o tipo de *skip-lote* informado no campo **Skip-lote** da rotina **QIPA010**.  
  Porém, se o parâmetro citado acima estiver com conteúdo maior do que zero, o Sistema irá iniciar a contagem de produções com base nesta parametrização para então, considerar o tipo de *skip-lote* definido na rotina **QIPA010**. Por exemplo: se o conteúdo do parâmetro for 2, o Sistema irá aplicar o conceito de *skip-lote* somente a partir da terceira produção.  
  Desta forma, os resultados de inspeção aprovados automaticamente pelo conceito de *skip-lote* terão o texto **Laudo aprovado em funcao do skip-lote** inserido no campo **Just. Laudo** da rotina **QIPA215 - Resultados**. Este texto é sugerido como padrão e informado no conteúdo do parâmetro **MV\_QPJUSLA - Justificativa para o laudo de Ordens de Produção certificadas, pela avaliação do skip-lote**, porém seu conteúdo pode ser editado.  
    
  **Observação**  
  O parâmetro **MV\_QPSKLPR - No.de Produções iniciais para a aplicação do Skip-lote**não possui validade quando há utilização do conceito de **Free-Pass**. Ao selecionar o Free-Pass seu efeito é imediato, pois, Free-Pass é uma evolução do conceito de Skip-Lote, ou seja, há histórico do relacionamento, o processo é auditado e têm níveis elevados de qualidade na entrega do produto específico.

3. Quando utilizado a **Especificação por Grupo**, o skip-lote não será válido. O processo ocorrerá via **Skip-Teste** com cadastro na rotina[**QIPA190 - Skip-Teste em Grupo**](https://tdn.totvs.com/pages/viewpage.action?pageId=545649275), onde ocorrerá vínculo entre os ensaios da Especificação por Grupo e a regra de Skip-Teste aplicada.

* **Observação**  
  O parâmetro **MV\_QPSKLPR - No.de Produções iniciais para a aplicação do Skip-lote**possui validade quando há utilização do conceito de Skip-Teste. Também será preciso validar o parâmetro **MV\_QPSKPTE - Indica se irá calcular o Skip-Teste para todas as produções (=1) ou para as as produções inspecionada somente (=2).**
