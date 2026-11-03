---
article_id: 4416255197591
category: Gestão
content_hash: 23b45098907da7d93e2b3237003396959968f579252d8184d890d60b7c8c1154
fetched_at: '2026-06-28T22:46:48.327731+00:00'
product: rm
section_id: 1500000861162
source: central-rm
title: 'RH - RM - FOP - Gerador de Saídas: exportação de layout'
type: support-article
updated_at: '2025-03-13T11:11:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416255197591-RH-RM-FOP-Gerador-de-Sa%C3%ADdas-exporta%C3%A7%C3%A3o-de-layout
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:06:00 min****Dúvida**Como realizar a exportação de layout padrão da Folha de Pagamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Primeiramente, será necessário verificar se possui permissão para o gerador de saída, como também criar a categoria. Portanto, acesse: **Serviços globais | Segurança | Usuário** e verifique no cadastro de usuário qual é o perfil que se encontra associado no usuário no sistema **Integração.  
  
![](https://totvssuporte.zendesk.com/attachments/token/0yZ3z3sQgxx2vQf5JLEJsyd7Z/?name=inline-1504724120.png)**2. Logo, ainda em **Serviços Globais**, acesse o perfil no sistema **Integração** e libere a permissão em **Acesso a Menus**.   
  
![](https://totvssuporte.zendesk.com/attachments/token/Dftm1ZBOW1ny25OIg5OSmZQ2z/?name=inline-967995182.png)  
  
3. Com as permissões liberadas, acesse: **Gestão | Gerador de saídas | Processos | Importar estrutura de relatórios.  
  
![](https://totvssuporte.zendesk.com/attachments/token/W13S95eq3BtoFIgZuCIJpzQCm/?name=inline182710021.png)**

4. Importe o layout desejado. Para isso, acesse o caminho onde se encontra os *layouts* padrões TOTVS: **C:\TOTVS\CorporeRM\ObjetosGerenciais\Layouts.  
  
![](https://totvssuporte.zendesk.com/attachments/token/L03c9ViBv8Y5aaJngyeXC6ufT/?name=inline-1269657091.png)**  
**Importante**  
Normalmente, o sistema solicita a vinculação de uma Categoria para concluir o processo de importação de *layout*, conforme imagem abaixo.   
  
![](https://totvssuporte.zendesk.com/attachments/token/BZ8H4JuXqiMFyFEU811SopfPb/?name=inline-2106880407.png)  
  
![](https://totvssuporte.zendesk.com/attachments/token/IKqJBP7cjyaMPpOxHRdoKT7dN/?name=inline303726377.png)  
  
Caso apresenta essa mensagem ao tentar vincular a categoria, será necessário criar uma categoria. Para maiores informações quanto ao processo de criação de categoria, [clique aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014001391-RH-RM-FOP-Gerador-de-Sa%C3%ADdas-Cria%C3%A7%C3%A3o-de-categoria)  
  
5. Após importação do *layout,* será necessário realizar a geração desse, para que depois possa exportar. Para isso, acesse: **Gestão | Gerados de Saídas | selecione o layout | Processos | Gerador de Saídas.** Logo, informe diretório e avance.  
  
![](https://totvssuporte.zendesk.com/attachments/token/FT1mlSx4UF1d8rre4anhgB7lI/?name=inline501478609.png)  
  
6. Na tela **Parâmetros da Geração** poderá informar através de um filtro a chapa ou todas as chapas que deseja gerar e executar.  
  
![](https://totvssuporte.zendesk.com/attachments/token/yxTcoxskR1LYYxU7vPLJQb7lz/?name=inline860523680.png)  
  
7. Após o passo 6, acesse o local onde informou para salvar o arquivo. Irá observar que, o arquivo foi salvo um arquivo txt com as informações do *layout* desejado dos funcionários para a geração dos holerites.  
  
![](https://totvssuporte.zendesk.com/attachments/token/axiOZgLimHqwD1jgysBKqSkel/?name=inline-1822242258.png)  
  
**Saiba Mais**  
[RH - RM - FOP - Como alterar a extensão dos arquivos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011392121-RH-RM-FOP-Como-alterar-a-extens%C3%A3o-dos-arquivos-?source=search)  
[RH - RM - FOP - Gerador de Saídas: Criação de categoria](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014001391-RH-RM-FOP-Gerador-de-Sa%C3%ADdas-Cria%C3%A7%C3%A3o-de-categoria)
