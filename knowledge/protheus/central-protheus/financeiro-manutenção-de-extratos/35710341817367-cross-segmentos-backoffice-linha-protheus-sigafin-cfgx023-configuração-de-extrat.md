---
article_id: 35710341817367
category: Financeiro - Manutenção de Extratos
content_hash: 339d80cef9dafb25a212e7673a769b015937ec82e82887ec77be5d074e369e78
fetched_at: '2026-06-28T22:37:31.195898+00:00'
product: protheus
section_id: 35057672519319
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN -  CFGX023 -Configuração
  de Extratos Bancários
type: support-article
updated_at: '2026-02-04T14:50:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35710341817367-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CFGX023-Configura%C3%A7%C3%A3o-de-Extratos-Banc%C3%A1rios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35710341805463) Tempo aproximado para leitura: **00:08 min**  
  
**Dúvida**  
Qual o procedimento recomendado para efetuar a configuração de extratos bancários?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

O **Microsiga Protheus** conta com o recurso de **Reconciliação Bancária Automática** no módulo **Financeiro**, que permite importar extratos bancários em arquivo eletrônico e comparar as informações com os lançamentos já registrados no sistema.

**Acesse o Configurador (SIGACFG)**  
Vá até o menu:  **Ambiente → Cadastros → Conf. Extrato Banc.**

1. Ao acessar **Conf. Extrato Banc.** é necessário definir os tipos de operações que serão executadas:
   1. **Novo:** configura um novo arquivo que pode assumir a extensão ".RET" (Retorno).
   2. **Restaura:** carrega um arquivo configurado.
   3. **Excluir:** exclui um arquivo configurado.
   4. **Cancelar:** abandona essa opção.
2. Clique em **Novo**.
3. Informe o caminho, o nome do arquivo e confirme.
4. Em seguida, é necessário definir os dados do arquivo de retorno conforme manual do Banco:
   * ***Header:*** primeira configuração que deve conter as informações sobre o banco.
   * **Saldo Inicial:** informe a configuração para obter os dados sobre o saldo inicial.
   * **Lançamentos:** informe a configuração para obter os dados sobre os lançamentos na conta.
   * **Saldo Final:** informe a configuração para obter dados sobre o saldo final da conta.
   * ***Trailler:*** informe a configuração para obter dados das somatórias de entradas e saídas.
5. Selecione a opção ***Header*** e clique em **Editar**para definir o ***Layout*****do Extrato**. Preencha os dados:
   * **Campo:** é sugerido automaticamente pelo sistema e pode ser alterado pelo usuário, porém o nome apresentado é necessário para o processamento do arquivo eletrônico enviado pelo Banco.
   * **Posição Inicial:** informe o número da coluna do registro que inicia a informação conforme manual do Banco.
   * **Posição Final:** informe o número da coluna do registro que finaliza a informação conforme manual do Banco.
   * **Decimais:** informe o número de decimais da informação conforme manual do Banco.
   * **Conteúdo:** não é necessário o preenchimento desse campo para o retorno.
6. **Repita o processo** para os cinco blocos (Header, Saldo Inicial, Lançamentos, Saldo Final e Trailler).
7. **Clique em OK** para confirmar a inclusão do layout.

⚠️ **Observações importantes**

* A **configuração deve seguir exatamente o layout fornecido pelo banco** — qualquer diferença de posição ou tamanho de campo impedirá a leitura correta.
* Caso o extrato possua **hífen (“-”)** em campos de conta ou agência, recomenda-se cadastrar esses dados **sem o caractere especial** no sistema.
* Após configurado, o arquivo pode ser importado na rotina **FINA474 – Manutenção de Extrato Bancário** para execução da reconciliação.

**Saiba Mais**

[Configuração de Extratos Bancários (CFGX023 - SIGACFG)](https://tdn.totvs.com/pages/releaseview.action?pageId=312158241)
