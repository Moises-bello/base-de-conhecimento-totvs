---
article_id: 360006976531
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 62ddb7203a1a742599f92d58a9c525744e2506bd5514edfb864844e26176fceb
fetched_at: '2026-06-28T22:37:55.321957+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB - Como configurar
  CNAB a Receber
type: support-article
updated_at: '2022-05-31T02:04:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006976531-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-Como-configurar-CNAB-a-Receber
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:05:00 min  
  
Dúvida**Como configurar CNAB a Receber?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Para configurar CNAB a Receber:

1. No menu principal, clique em CNAB Receber.

2. Selecione uma das opções:

* Remessa: configura o padrão dos dados que devem ser remetidos ao Banco via arquivo; como: cobrança de título, solicitação de baixas, alteração de vencimentos, protestos de títulos e outros.
* Retorno: configura o padrão dos dados que devem ser recebidos do Banco. Quando há movimentações, o Banco gera o arquivo de Retorno que confirma os títulos que entraram, os títulos pagos, baixas e alterações processadas.

3. Selecione o tipo de movimentação bancária que deve ser configurada:

* Novo: disponível para configurar um novo arquivo. O Sistema solicita um nome para o arquivo que pode assumir a extensão .REM (Remessa) ou .RET (Retorno).
* Restaura: disponível para carregar um arquivo configurado ou o anterior àquele que está em processo de configuração.
* Excluir: exclui um arquivo configurado.
* Cancelar: interrompe o procedimento sem gravar.

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
* Fixo: conteúdo fixo estipulado pelo Banco. Exemplo: 341.
* Campo: quando há necessidade de utilizar um campo dos arquivos do *Advanced* **Protheus**. Exemplo: **SE1->E1\_NUM**.
* Expressão **AdvPL**: pode ser utilizada qualquer expressão *Adv*Pl válida. Exemplo: **IIF(SA2->E2\_TIPO=“J”,SA2->A2\_CGC).**
* Função: quando há necessidade de utilização de função desenvolvida no Sistema. Exemplo: Incrementa( ).

8. Após a informação do *Header*, execute a formatação do Detalhe e, em seguida, a do *Trailler*.

9. Confirme a configuração.  
Editar uma configuração de *Header*

1. Posicione o cursor no registro desejado e clique em Editar.
2. São exibidos os dados do registro.
3. Confira e confirme a edição.  
     
   **Excluir uma configuração de *Header***

1. Posicione o cursor no registro desejado e clique em Excluir.

2. Confira os dados e confirme a exclusão.

**Saiba Mais**

* [Página Centralizadora do CNAB](http://tdn.totvs.com/display/PROT/CNAB)
* [Como Parametrizar o sistema para a geração do CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006611532-MP-SIGAFIN-CNAB-Como-parametrizar-o-sistema-para-gera%C3%A7%C3%A3o-do-CNAB-)
* [Principais mensagens do CNAB](http://tdn.totvs.com.br/pages/viewpage.action?pageId=353280222)
