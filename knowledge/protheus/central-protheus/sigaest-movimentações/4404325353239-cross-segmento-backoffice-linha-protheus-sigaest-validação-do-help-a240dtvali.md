---
article_id: 4404325353239
category: SIGAEST - MOVIMENTAÇÕES
content_hash: e8dbf70e9c716117acfdc8012adb9ddf887f40d5804d5b7becec082841e13e34
fetched_at: '2026-06-28T22:38:58.444671+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Validação do Help
  A240DTVALI
type: support-article
updated_at: '2025-08-01T13:17:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404325353239-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Valida%C3%A7%C3%A3o-do-Help-A240DTVALI
---

Ao realizar movimentações, como em rotinas de Pré-Nota de Entrada ou Documento de Entrada, pode ocorrer o erro Help A240DTVALI, geralmente quando se tenta alterar a data de validade de um lote já existente. Para evitar o erro, a data de validade deve coincidir com a do lote original. Caso contrário, a correção deve ser feita na rotina de Manutenção de Lotes (MATA390). Se o erro persistir sem alterações no lote, recomenda-se desabilitar customizações e atualizar o módulo correspondente. Links para desabilitar customizações e atualizar o sistema estão disponíveis.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33873490059415) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**  
Ao efetuar movimentações por meio de rotinas como: Pré-Nota de Entrada (MATA140), Documento de Entrada (MATA103), Movimentos Internos (MATA240/MATA241), Pedido de Venda (MATA410) e afins, ocorre o Help A240DTVALI. Como corrigir este problema?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33873490060439)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
Este help normalmente é apresentado quando, no ato de alguma movimentação (na rotina que está gerando o erro), o usuário tentou alterar a data de validade de um Lote já existente selecionado no movimento. ***Ou seja, quando é incluído o mesmo lote que já possui em saldo, porém com datas diferentes.***

|  |
| --- |
| Exemplo: Saldo em estoque: **Lote**300323 - **Validade**03/05/2023 - **Saldo**20un **Incluir**20un **Lote**300323 - **Validade**05/05/2023 Observe que a data de validade está diferente da principal, que é a primeira, ou seja, nesse cenário será gerado o HELP.  Então: Caso precise incluir, por exemplo, mais 20 unidades deste mesmo lote, é necessário que a data de validade seja a mesma.  **Incluir**20un **Lote**300323 - **Validade**03/05/2023 Observe que a data é a mesma que a primeira, ou seja, Neste caso não acontecerá o HELP |

Ao tentar efetuar uma movimentação utilizando o mesmo Lote, porém com validade diferente, o sistema exibe o help notificando que a data de validade será corrigida, conforme a primeira entrada do lote.

**Atenção,**

Por padrão, o Protheus impede que o usuário altere data de validade no ato da rotina do movimento, reservando esta operação apenas para a rotina **Manutenção de Lotes (MATA390)**, onde nela o usuário consegue selecionar o lote desejado e assim alterar a data de validade.

**Observação:**

Caso o help seja apresentado, mesmo sem o usuário ter alterado o lote dentro da rotina que gera o erro, certifique de estar executando a rotina livre de Customizações e Pontos de Entrada. Para desabilitar e testar no padrão, veja o boletim: [**MP - FRAME - Desabilitar Customizações e Pontos de Entrada pelo Catálogo de Personalização**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024863633-MP-FRAME-Desabilitar-Customiza%C3%A7%C3%B5es-e-Pontos-de-Entrada-pelo-Cat%C3%A1logo-de-Personaliza%C3%A7%C3%A3o)

Caso mesmo assim persistir, recomendamos que atualize o pacote acumulado do módulo ao qual a rotina que está gerando o erro pertence. Segue link da Central de Atualizações onde contempla os pacotes de expedição contínua de todos os módulos do Protheus, além de outros artefatos do Produto: [**Central de Atualizações - LIB - Acumulados - Binários**](https://tdn.totvs.com/pages/releaseview.action?pageId=550332596)

Saiba mais:  
[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
