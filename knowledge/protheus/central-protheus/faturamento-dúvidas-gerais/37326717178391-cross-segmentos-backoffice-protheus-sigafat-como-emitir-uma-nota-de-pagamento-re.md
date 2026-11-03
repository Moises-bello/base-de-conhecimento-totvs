---
article_id: 37326717178391
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: fdb2385255a2946c19861e1edc77bb85ca42c33b3367f0171b97d45bd2e1b187
fetched_at: '2026-06-28T22:38:29.757773+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como emitir uma nota de Pagamento
  / Recebimento Antecipado (tpNFDebito = 06)
type: support-article
updated_at: '2026-06-11T14:57:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37326717178391-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-emitir-uma-nota-de-Pagamento-Recebimento-Antecipado-tpNFDebito-06
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37326717154839) Tempo aproximado para leitura:**00:03:00 min**  
  
**Dúvida**  
Como emitir uma nota de Pagamento Antecipado (**tpNFDebito = 06**)?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da versão 12.1.2210  
  
**Solução**  
A Nota Fiscal de Débito Tipo "**Pagamento Antecipado**" deve ser emitida pelo Fornecedor no momento em que ele recebe o pagamento por um produto ou serviço que será fornecido no futuro. Essa nota serve para que o Fornecedor destaque os tributos sobre o valor recebido antecipadamente, usando a mesma alíquota que seria aplicada na emissão da nota de fornecimento. O débito de IBS é registrado na apuração do mês do recebimento. Por fim, o Cliente (Adquirente) só pode tomar o crédito de IBS correspondente quando o Fornecedor registrar esse débito da antecipação.

**Importante:** Veja que no caso, quem emite o documento é que recebe o valor pago, portanto para fins sistêmicos o registro do Pagamento Antecipado do lado do Fornecedor é um **Recebimento Antecipado**.

Quando o Fornecedor realiza a entrega final do bem ou serviço, ele deve emitir a nota fiscal de fornecimento e esta nota deve referenciar as chaves de acesso das Notas Fiscais de Débito Tipo 06 (Pagamento Antecipado) emitidas anteriormente. Ao processar essa nota final, o sistema do IBS deduzirá automaticamente o valor do imposto já pago na antecipação, evitando que o Fornecedor pague o mesmo débito duas vezes.

#### **Processo**:

|  |
| --- |
| Assista nosso vídeo How To explicativo do passo a passo abaixo:  [How To | MP - SIGAFAT - Nota de Débito de Recebimento Antecipado](https://www.youtube.com/watch?v=Fv0KPZyO-wk) |

* Ao incluir o documento de débito deve ser informado no campo de tipo "**Tipo Compl.**" como “**6 - Pagamento Antecipado**”;

(A numeração e série não são editáveis, pois serão geradas na confirmação.)

* Informe o **Cliente**e **Loja**, este deve ser o Pagador (Adquirente do fornecimento futuro);
* Informe uma **Condição de Pagamento**(meramente informativa, pois não haverá geração de financeiro);
* Informe na grid:

  **Produto -** Devem ser informados todos os produtos e/ou serviços do fornecimento futuro;

  **Quantidade -** Deve ser informada a quantidade referente ao bem ou serviço que será fornecido futuramente;
* Informe o **Valor**. Será sobre este valor que haverá incidência do calculo de tributos;
* Informe uma **TES** que**não movimenta estoque** e **não gera financeiro**;
* Clique na opção **Vincular**;

  + Na parte superior, em **Filtros**, informe os dados para a busca do **Título de Recebimento Antecipado** a ser referenciado nesta nota;
  + Clique em **Buscar**. Serão listados os **títulos**(**tipo RA**) de acordo com os filtros
  + **Marque** o título e **Confirme**;
* Clique em **Confirmar**;
* Selecione a **Série**e **Numeração**para geração do documento.

#### **Referenciamento da Nota de Débito:**

O referenciamento da Nota de Débito, utilizada para **Pagamento / Recebimento Antecipado**, é realizado por meio da vinculação com o **Documento de Saída**, estabelecendo o relacionamento com o respectivo **RA (Recebimento Antecipado)** gerando a Tag **"refNFe"** no XML.

* Realize a transmissão da Nota de Débito referente ao **Recebimento/Pagamento Antecipado,** para queseja gerada a respectiva **Chave de Acesso da NF-e.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38805268475543)![](https://centraldeatendimento.totvs.com/hc/article_attachments/38805268480919)

* Realize a inclusão do **Pedido de Venda** no sistema, com a vinculação ao respectivo **Título de RA (Recebimento Antecipado).**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38805252871319)

* Realize a preparação do **Documento de Saída** e, em seguida, acesse a rotina **Documento de Saída Manual (MATA920)**.

  - Localize o **Documento de Saída** previamente gerado.  
     **Exemplo:** `000000401`.

  - Acesse o menu **Outras Ações** e selecione a opção **Complementos**.

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38805252871831)
* Acesse **Informações Complementares** e localize a opção **Documentos Fiscais**.

Em **Informações Complementares – Documentos Fiscais Referenciados**:

      No campo **Docto. ref.**, localize o **Documento de Saída** gerado a partir da **Nota de Débito** e selecione-o.

      No campo **Inf. Compl**, preencha o complemento.

      Salve as alterações realizadas para garantir que as informações adicionais fiquem registradas e vinculadas corretamente ao documento fiscal.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38805252876823)

* Após realizar o **referenciamento das Notas**, proceda com a **transmissão do Documento de Saída** correspondente.

       No **XML do Documento de Saída** vinculado ao **RA (Recebimento Antecipado)**, será criada a tag `<refNFe>`.

     Essa tag conterá a **Chave de Acesso da NF-e** correspondente ao **Documento de Saída** gerado a partir da **Nota de Débito**, garantindo o correto referenciamento e rastreabilidade entre os documentos fiscais no sistema e perante os órgãos fiscais.

    O uso da tag `<refNFe>` é essencial para assegurar que o documento fiscal vinculado ao RA esteja formalmente referenciado e validado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38805268486935)

**Observação sobre Suporte:**

Caso surjam dúvidas durante o **processo de Referenciamento (MATA920)**, entre em contato com a **equipe do Protheus Fiscal**.

Em situações de **rejeição de nota fiscal**, acione a **equipe de SPED** para análise e orientação sobre o tratamento adequado do documento.

**Saiba mais:**

* [Notas de Débito (NF-e: finNFe = 6 - NT 2025.002)](https://tdn.totvs.com/pages/viewpage.action?pageId=1013620273)
* [Webinar TOTVS | SIGAFAT- Nota de Débito](https://www.youtube.com/watch?v=XbjR3mzXRp8)
