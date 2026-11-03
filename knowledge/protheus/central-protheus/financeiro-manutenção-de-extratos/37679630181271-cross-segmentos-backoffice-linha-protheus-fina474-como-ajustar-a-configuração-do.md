---
article_id: 37679630181271
category: Financeiro - Manutenção de Extratos
content_hash: fd5ed1a17b7e168861a200158963305a0e67cb191d26a4b0ee171c36a661201a
fetched_at: '2026-06-28T22:37:31.133977+00:00'
product: protheus
section_id: 35057672519319
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINA474 - Como ajustar a configuração
  do arquivo retorno do extrato bancário
type: support-article
updated_at: '2026-01-14T21:00:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37679630181271-Cross-Segmentos-Backoffice-Linha-Protheus-FINA474-Como-ajustar-a-configura%C3%A7%C3%A3o-do-arquivo-retorno-do-extrato-banc%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37679630162711) Tempo aproximado para leitura: **00:08 min**  
  
**Dúvida**  
Como ajustar a configuração do arquivo retorno do extrato bancário?  
  
**Ambiente**  
Cross Segmento - TOTVS BackOffice (Linha Protheus) - FINA474 - A partir da versão 12.1.33.  
  
**Solução**  
O sistema disponibiliza a funcionalidade de **reconciliação bancária automática** no módulo **Financeiro**, utilizando o padrão **FEBRABAN (Federação Brasileira de Bancos)**. Esse recurso permite a recepção de informações de **extrato bancário por meio de arquivo eletrônico**, possibilitando a conferência e validação dos dados registrados no sistema.

Para a correta utilização dessa funcionalidade, é necessário que o **administrador do sistema** realize previamente a **configuração dos arquivos de retorno** por meio do **Configurador**.

### **Importante**

**O sistema processa o retorno de extrato bancário por meio de um layout que contempla os registros de Header, Detalhes (Lançamentos) e Trailer, com 240 bytes por linha, conforme o padrão FEBRABAN.**

**Procedimentos para Configuração do Extrato FEBRABAN**

Ao acessar a rotina de **Extrato FEBRABAN**, é necessário informar a operação a ser executada:

* **Novo**: permite configurar um novo arquivo de retorno, que pode possuir a extensão **.RET**;
* **Restaurar**: carrega um arquivo previamente configurado;
* **Excluir**: remove um arquivo configurado;
* **Cancelar**: interrompe o procedimento.

1. Selecione a opção **Novo**, informe o **caminho** e o **nome do arquivo**, e confirme.
2. Defina os dados do **arquivo de retorno**, conforme o **manual fornecido pelo banco**.
3. Configure os seguintes registros:

   * **Header**: corresponde ao primeiro registro do arquivo e deve conter as informações do banco;
   * **Lançamentos**: configure os campos necessários para obtenção dos dados dos lançamentos da conta;
   * **Trailer**: configure os campos para obtenção dos totais de entradas e saídas.
4. Selecione a pasta **Header** e clique em **Editar** para definir o layout do extrato.
5. Preencha os campos conforme descrito abaixo:

   * **Campo**: sugerido automaticamente pelo sistema; pode ser alterado pelo usuário, porém o nome apresentado é essencial para o correto processamento do arquivo eletrônico enviado pelo banco;
   * **Posição Inicial**: informe a coluna inicial da informação, conforme o manual do banco;
   * **Posição Final**: informe a coluna final da informação, conforme o manual do banco;
   * **Decimais**: informe a quantidade de casas decimais, conforme o manual do banco;
   * **Conteúdo**: não é necessário o preenchimento para arquivos de retorno.
6. Revise as informações configuradas e clique em **Confirmar** para concluir o processo.

Observação

A validação das configurações não está contemplada no escopo do suporte padrão, sendo recomendada a realização dessa verificação pela equipe de **TI da empresa**.
