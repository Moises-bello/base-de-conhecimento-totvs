---
article_id: 41327213126295
category: Financeiro - Smart View
content_hash: 587ff6de0618beea5bde0ab7fcab5e4e94de8545a6c9db302bf4ecb1e97ae908
fetched_at: '2026-06-28T22:37:44.879670+00:00'
product: protheus
section_id: 32632656432151
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Como incluir
  novos campos em um Objeto de Negócio existente no Smart View
type: support-article
updated_at: '2026-06-19T11:13:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41327213126295-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Como-incluir-novos-campos-em-um-Objeto-de-Neg%C3%B3cio-existente-no-Smart-View
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41327213092887)** Tempo aproximado para leitura: **00:06:00 min**  
  
**Dúvida**  
Como realizar a inclusão de um campo em um Objeto de Negócio padrão já disponibilizado pelo produto no Smart View, como por exemplo a rotina de Posição de Títulos a Pagar (FINSV013)?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - A partir da release 12.1.2210  
  
**Solução**

O processo padrão para a inserção de novos campos em objetos de negócio do Smart View é realizado de forma nativa através do módulo Configurador. Mas existem premissas e regras de negócio estruturais que devem ser observadas antes de iniciar a configuração:

* **Acesso Prévio:** O Objeto de Negócio em questão deve ter sido acessado no Protheus pelo menos uma vez no ambiente para que sua estrutura seja devidamente reconhecida.
* **Tipos de Objetos Suportados:** A inclusão de campos é válida exclusivamente para recursos do tipo **Visão de Dados**  e **Tabela Dinâmica**. Objetos cadastrados como **Relatório**, que geram arquivos em modelo PDF, possuem uma estrutura de layout predefinida no código-fonte e não permitem a adição dinâmica de colunas por este painel.
* **Propriedades do Campo:** O campo desejado deve pertencer estritamente às tabelas que compõem o Objeto de Negócio e estar configurado como **Usado** no Dicionário de Dados. Campos de uso interno do sistema não são listados para exibição.

1. Acesse o módulo **Configurador (SIGACFG)**.
2. Siga pelo menu **Ambiente** > **Smart View** > **Integração Smart View**.
3. Aguarde o carregamento completo da interface de gerenciamento de objetos do Smart View.  
   ![sv 1.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/41327213094295)
4. No menu superior da janela aberta, clique na opção **Personalização de Campos**.
5. No campo de pesquisa localizado no canto superior direito, insira o nome do Objeto de Negócio correspondente (por exemplo, digite "pagar" para localizar a rotina de Posição de Títulos a Pagar).  
   Importante: A pesquisa deve respeitar acentuação e maiúsculas/minúsculas do nome original
6. O sistema apresentará a relação do objeto encontrado juntamente com a lista de suas **Tabelas customizáveis** (como SE2, SA2, SED). Certifique-se de que a tabela do campo que você precisa está mapeada como elegível.
7. Clique sobre o botão **Editar** na linha do Objeto de Negócio que receberá a alteração.
8. Na tela de edição, vá até a seção de adição de campos:

   * No campo **Tabela**, selecione a tabela de origem correspondente (ex: *SED - Naturezas*).
   * No campo **Campo**, abra a lista e selecione o componente técnico que deseja disponibilizar (ex: *ED\_CODIGO*).
9. Clique no botão **Adicionar**. O campo passará a constar na listagem inferior com a marcação de customização ativa.
10. Clique em **Salvar** e confirme a operação na mensagem subsequente gerada pelo sistema.  
    ![sv2.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/41327213098775)
11. Para validar o resultado, retorne ao módulo financeiro, feche a janela da rotina do Smart View caso ela estivesse aberta e execute-a novamente para que os metadados atualizados sejam recarregados.
12. O campo deve ser apresentado na última posição.
