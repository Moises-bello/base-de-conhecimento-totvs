---
article_id: 38293927833623
category: Financeiro
content_hash: db7114ca8d3fa7a11998870c64397d28bd4fa67d193d4c2acd1a374f049b3683
fetched_at: '2026-06-28T22:38:00.867480+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACFG - Foi identificado
  uma inconsistência entre o dicionário e a base de dados e por este motivo as baixas
  não poderão ser realizadas
type: support-article
updated_at: '2026-02-10T12:42:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38293927833623-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACFG-Foi-identificado-uma-inconsist%C3%AAncia-entre-o-dicion%C3%A1rio-e-a-base-de-dados-e-por-este-motivo-as-baixas-n%C3%A3o-poder%C3%A3o-ser-realizadas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38293927822999) Tempo aproximado para leitura: **00:08 min**  
  
**Dúvida**  
Ao tentar realizar baixas no sistema, é apresentada a mensagem informando que foi identificada uma inconsistência entre o dicionário e a base de dados, impedindo a continuidade do processo. Como ajustar as sequências já baixadas para permitir novas operações?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Esta situação ocorre quando há necessidade de aumentar o tamanho dos campos contidos no **Grupo (SXG) 134 - Sequência de baixa**. Quando o tamanho do campo é alterado no dicionário de dados, o conteúdo já gravado no banco de dados precisa ser preenchido com zeros à esquerda para manter a integridade e evitar erros de duplicidade ou chave primária.

Para solucionar esta inconsistência, deve-se utilizar o **RDMAKE** **FIXSEQBX**, que ajusta automaticamente o conteúdo dos campos conforme o novo tamanho definido.

**Exemplo de ajuste:**

* **Antes:** O conteúdo do campo (ex: `E5_SEQ`) era `02` (Tamanho 2).
* **Alteração:** O campo foi expandido para tamanho 4.
* **Após RDMAKE:** O conteúdo será gravado como `0002`.

**Para alteração de um campo individual:**

1. No **Configurador**, acesse **Base de Dados > Dicionário > Base de Dados**;
2. Clique em **Dicionário de Dados** e localize a tabela desejada (Ex: **SE5**);
3. Clique em **Editar (Lápis)**;
4. Abra a pasta **Campos**, localize o campo específico (Ex: **E5\_SEQ**) e clique em **Editar**;

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38293927823767)
5. Localizará o grupo de campos 134 - sequência de baixa;
6. Para ajustar o tamanho do campo **Sequência de Baixa**, retorne à base de dados, utilize a seta para baixo para acessar o **Grupo de Campos**, localize a opção **Sequência de Baixa**, clique em **Editar** e altere o tamanho do campo para **4 caracteres**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38293939563543)

Após o ajuste, clique em salvar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38293939563927)

O sistema realizará o ajuste em todas as tabelas que envolvem o grupo de campos da **Sequência de Baixa**.

> **Importante:** Sugerimos que a execução seja feita primeiramente em um ambiente de homologação e, somente após a validação, executada em ambiente de produção. **Realize um backup completo da base de dados antes de iniciar.**

1. Copie o código-fonte do [RDMAKE](https://tdn.totvs.com.br/pages/releaseview.action?pageId=622668372)
2. Compile o programa no ambiente desejado utilizando o **TOTVS Developer Studio (TDS)**;
3. No **SmartClient**, informe no campo Programa Inicial: `U_FIXSEQBX`;
4. Clique em **OK**;
5. Siga as instruções do **Wizard** (assistente) que será apresentado na tela;
6. Aguarde a finalização do processamento das atualizações.

**Importante**  
No escopo de atendimento padrão, atuamos especificamente em problemas pontuais das rotinas do sistema. Desta forma, nosso escopo não abrange customizações, pois trata-se de um processo específico por empresa e deve ser realizado por analista in loco.
