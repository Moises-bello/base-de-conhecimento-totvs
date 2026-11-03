---
article_id: 360006976931
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 944fcd998d6b71650aaed654474f8c6b6894310ee6987978fe2820b4705ef9b3
fetched_at: '2026-06-28T22:37:55.147426+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus  - CNAB - Como configurar CNAB a
  Pagar
type: support-article
updated_at: '2022-06-28T14:06:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006976931-Cross-Segmento-Backoffice-Linha-Protheus-CNAB-Como-configurar-CNAB-a-Pagar
---

**Dúvida**Como configurar CNAB a Pagar?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro – A partir da versão 11  
  
**Solução**Para configurar CNAB a Pagar:

1. No menu principal, clique em CNAB Pagar.

2. Selecione uma das opções:

* Remessa: configura o padrão dos dados que devem ser remetidos ao Banco via arquivo; como: cobrança de título, solicitação de baixas, alteração de vencimentos, protestos de títulos e outros.
* Retorno: configura o padrão dos dados que devem ser recebidos do Banco. Quando há movimentações, o Banco gera o arquivo de Retorno que confirma os títulos que entraram, os títulos pagos, baixas e alterações processadas.

3. Selecione o tipo de movimentação bancária que deve ser configurada.

4. Clique em Novo e informe o nome do arquivo que armazena os dados.

5. Ao confirmar o arquivo é necessário configurar os itens:

* *Header*: é a primeira informação do arquivo. Apresenta dados sobre o serviço, Banco, empresa, etc.
* Detalhe: local onde são gravados os dados dos títulos, documentos, duplicatas, etc.
* *Trailler*: finaliza o arquivo.

6. Selecione a pasta *Header*.

7. Clique em Incluir para informar a configuração de *Header* de CNAB. Preencha os seguintes dados:

* Campo: nome do campo conforme padrão CNAB.
* Pos. Inicial: número da coluna do registro CNAB que inicia a informação.
* Pos. Final: número da coluna do registro CNAB que finaliza a informação.
* Decimais: número de decimais da informação do arquivo padrão CNAB, se for em formato numérico.
* Conteúdo: informação que deve ser enviada pelo Sistema para o arquivo padrão CNAB. Pode ser preenchido com:
* Nulo: conforme descrição exibida no manual do Banco. Exemplo: “ ”.
* Fixo: conteúdo fixo estipulado pelo Banco. Exemplo: 422.
* Campo: quando há necessidade de utilizar um campo dos arquivos do Advanced Protheus. Exemplo: **SE2->E2\_NUM**.
* Expressão AdvPL: pode ser utilizada qualquer expressão AdvPl válida. Exemplo: **IIF(SA2->E2\_TIPO=“J”,SA2->A2\_CGC).**
* Função: quando há necessidade de utilização de função desenvolvida no Sistema. Exemplo: Incrementa( ).

8. Após a informação do *Header*, execute a formatação do Detalhe e, em seguida, a do *Trailler*.

9. Confirme a configuração.

**Editar uma configuração de *Header***

1. Posicione o cursor no registro desejado e clique em Editar.

2. São exibidos os dados do registro.

3. Confira e confirme a edição.

**Excluir uma configuração de *Header***

1. Posicione o cursor no registro desejado e clique em Excluir.

2. Confira os dados e confirme a exclusão.

**Veja mais**

* [Página Centralizadora do CNAB](http://tdn.totvs.com/display/PROT/CNAB)
* [Como Parametrizar o sistema para a geração do CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006611532-MP-SIGAFIN-CNAB-Como-parametrizar-o-sistema-para-gera%C3%A7%C3%A3o-do-CNAB-)
* [Principais mensagens do CNAB](http://tdn.totvs.com.br/pages/viewpage.action?pageId=353280222)
