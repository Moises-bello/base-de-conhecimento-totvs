---
article_id: 39401925847703
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: be69e3e6a1c8e3f4b7477c67035092b63436e0749c6138db6a1df620e62a8bea
fetched_at: '2026-06-28T22:39:08.245996+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Facilitador do Cadastro
  de Produtos, como utilizar?
type: support-article
updated_at: '2026-05-27T19:03:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39401925847703-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Facilitador-do-Cadastro-de-Produtos-como-utilizar
---

O Facilitador no Cadastro de Produtos (MATA010) do Protheus permite alterar em lote campos específicos, como Conta Contábil, aplicando filtros para manter a integridade dos registros. O processo envolve acessar o cadastro, ativar o Facilitador, selecionar o campo, aplicar filtros, configurar a alteração e finalizar a atualização, que é confirmada pelo sistema sem erros.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39401925824535) Tempo aproximado para leitura: **00:02:50 min**  
  
**Dúvida**

Como utilizar o Facilitador no Cadastro de Produtos (MATA010)?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos- Todas as versões  
  
**Solução**

O Facilitador é uma ferramenta poderosa dentro do módulo de Estoque e Custos do Protheus que permite a alteração em lote de campos específicos no cadastro de produtos, aplicando filtros e regras de substituição sem a necessidade de scripts manuais no banco de dados.

Segue abaixo vídeo demonstrativo do processo, seguido das informações descritas neste artigo:

### **1. Contexto**

Necessidade de alterar uma informação específica (ex: Conta Contábil) em diversos registros do Cadastro de Produtos que compartilham um valor comum, mantendo a integridade dos demais registros.

### 

### **2. Passo a Passo**

1. **Acesse o Cadastro:** No módulo de **Estoque e Custos**, vá em `Atualizações > Cadastros > Produto`.
2. **Ative a Ferramenta:** Clique no botão **Outras Ações** e selecione a opção **Facilitador**.
3. **Seleção do Campo:** Na tela inicial do Facilitador, clique em "Avançar". Pesquise e selecione o campo que deseja alterar (no exemplo do vídeo, o campo `B1_CONTA`). Clique em "Avançar".
4. **Aplicação do Filtro:** \* Clique em **Filtrar**.

   * Escolha o campo (ex: `B1_CONTA`), a expressão (ex: `Igual a`) e informe o valor atual que deseja localizar (ex: a conta antiga `115800003`).
   * Clique em **Incluir**, depois em **Ok** e **Avançar**.
5. **Configuração da Alteração:**

   * O sistema exibirá os registros encontrados.
   * Selecione novamente o campo que sofrerá a alteração (`B1_CONTA`) na lista de campos para edição e clique em **Avançar**.
   * No campo **Cta Contabil (Novo)**, insira o novo valor desejado (ex: `115800006`).
6. **Finalização:**

   * Clique em **Avançar** e depois em **Finalizar**.
   * Confirme a execução da atualização. O sistema processará os registros e exibirá um log de conclusão sem erros.

***Saiba Mais:***

[SIGAEST - MATA010 - É possível adicionar campo customizado no Facilitador de Produtos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21461416880023-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-%C3%89-poss%C3%ADvel-adicionar-campo-customizado-no-Facilitador-de-Produtos)

[Clique aqui e veja mais artigos sobre CADASTROS E CONFIGURAÇÕES GERAIS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
