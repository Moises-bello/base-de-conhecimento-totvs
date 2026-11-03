---
article_id: 38991568118295
category: Financeiro - Movimentação Bancária
content_hash: 1170965c1c64cf86e0498cb19f81bf95b6985214ec146ebca658d295367899f3
fetched_at: '2026-06-28T22:38:19.338056+00:00'
product: protheus
section_id: 1500001550402
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA100 - Fixar a pergunta
  contabiliza online como "Sim"
type: support-article
updated_at: '2026-03-19T11:43:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38991568118295-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA100-Fixar-a-pergunta-contabiliza-online-como-Sim
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38991544782743) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como fixar a pergunta "Contabiliza Online" para que sempre venha preenchida com o conteúdo "Sim" por padrão ao acessar a rotina FINA100?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro (SIGAFIN) - Todas as versões  
  
**Solução**  
Para que a pergunta "Contabiliza Online" seja apresentada automaticamente como "Sim" durante a execução da rotina FINA100, é necessário ajustar a definição padrão do grupo de perguntas **AFI100** diretamente pelo módulo Configurador (SIGACFG).

### **Passos**

1. Acesse o módulo **Configurador (SIGACFG)**.
2. No menu principal, navegue até **Base de Dados** > **Dicionário** > **Base de Dados**.
3. No menu lateral esquerdo, clique em **Perguntas**.
4. Clique no ícone de pesquisa e busque pelo Grupo de Perguntas **AFI100**.
5. Clique em **Editar** no grupo localizado.
6. Na lista de perguntas, localize aquela referente a **Contabiliza Online** (geralmente a pergunta de número 04, dependendo da release).

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38991568103831)
7. Altere o valor do campo Pre Seleção (Combo)para o número correspondente à opção "Sim" (neste caso, preencha com o número **1**).
8. Clique em **Salvar** (ou Confirmar) para gravar as alterações da pergunta.
9. Salve a alteração do dicionário e clique no disquete para atualizar a base de dados.
10. Acesse novamente o módulo **Financeiro (SIGAFIN)**, abra a rotina **FINA100** e confirme que a pergunta agora vem preenchida como "Sim" por padrão.

    ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38991544786711)
