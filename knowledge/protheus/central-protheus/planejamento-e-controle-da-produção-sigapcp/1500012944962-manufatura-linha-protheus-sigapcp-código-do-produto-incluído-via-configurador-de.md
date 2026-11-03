---
article_id: 1500012944962
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 14c77138aae65087817c7a2115aa5a3aeb9507c71b25e7b6a4c2863e82774e09
fetched_at: '2026-06-28T22:42:41.057636+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Código do produto incluído via configurador
  de produtos
type: support-article
updated_at: '2021-06-07T11:16:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012944962-Manufatura-Linha-Protheus-SIGAPCP-C%C3%B3digo-do-produto-inclu%C3%ADdo-via-configurador-de-produtos
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Como mudar a forma de apresentação dos códigos de produtos incluídos via configurador de produtos?  
Por padrão o código é uma concatenação de caracteres contendo o código da família e as opções selecionadas, é possível incluir caracteres no meio desse código? Como uma máscara?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
1. Na rotina **MATA093 - Configurador de produtos**, selecione a família clique em **Alterar** e preencha o campo **BP\_DISPUSO - Disponível para Uso** com o conteúdo **Não**, salve a alteração;  
2. Novamente na rotina **MATA093**, selecione a **família** clique em **Alterar** e preencha o campo **BP\_CODPAD - Cod. Padrão** com o conteúdo **Não**, salve a alteração;  
3. Ainda no **MATA093**, selecione novamente a **família** e em **Outras Ações** selecione a opção **Descrição**,  
em **Resultado - Estrutura do Código** preencha a forma de apresentação da família e salve a alteração;  
4. Ainda no **MATA093**, selecione a **família**, clique em **Alterar** e preencha o campo **BP\_DISPUSO** com o conteúdo **Sim**, salve a alteração.  
  
**Exemplo**Supondo que o código da família é **TVE**, a família possui 6 características e deseja que entre as opções selecionadas e que compõem o código, tenha sempre o **ponto - .**, seguindo os passos acima teremos:  
  
1. Alteração do campo **BP\_DISPUSO** para **Não** e salvar;

![Imagem01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019961402/Imagem01.png)

2.  Alteração do campo **BP\_CODPAD** para **Não** e salvar;

![Imagem02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500020233261/Imagem02.png)

3. Ainda no **MATA093**, selecione novamente a família e em **Outras Ações** selecione a opção **Descrição**,  
em **Resultado - Estrutura do Código** preencha a forma de apresentação da família e salve a alteração, observe que preenchemos entre as opções o **ponto** desejado;

![Imagem03.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500020233321/Imagem03.png)

4. Ainda no **MATA093**, selecione a **família**, clique em **Alterar** e preencha o campo **BP\_DISPUSO** com o conteúdo **Sim**, salve a alteração

![Imagem04.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500020233421/Imagem04.png)

Podemos usar a opção **Simulação** existente em **Outras Ações** para observar os códigos gerados;

![Imagem05.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500020233521/Imagem05.png)
