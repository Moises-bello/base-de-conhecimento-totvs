---
article_id: 360035929453
category: Materiais - Compras (SIGACOM)
content_hash: c1420a9949f727b7069bad2387b6838c603f945d65e967ca6db217557d0ea773
fetched_at: '2026-06-28T22:41:25.309549+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Rotina MATA086: Grupo
  de Compradores - Fim do Ciclo de Vida'
type: support-article
updated_at: '2022-05-18T21:22:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035929453-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Rotina-MATA086-Grupo-de-Compradores-Fim-do-Ciclo-de-Vida
---

**Dúvida**

Substituição - Rotina MATA086: Grupo de Compradores - Fim do Ciclo de Vida  
  
**Ambiente**Microsiga Protheus - a partir da versão 12.1.23  
  
**Solução**

Desde de Julho/2019, somente a nova rotina possibilitará o Grupo de Compradores.  
A rotina de Grupo de Compradores foi substituída por uma nova rotina, com mesma finalidade, e já está disponível no repositório de objetos.   
A substituição da rotina visa a evolução do produto.

**Rotina Substituída:** MATA086 - Grupo de Compradores

**Rotina Substituta:** COMA086 - Grupo de Compradores

**Vantagens:** Performance.

**Procedimentos para utilização:** Não há a necessidade de realizar nenhum procedimento para utilização da nova rotina. A rotina estará disponível a partir da versão 12.1.23. Caso o usuário tente executar a rotina em versões anteriores, será apresentado help informando que a rotina não está disponível na versão corrente.

Para utilização do Novo Programa, deve-se estar com os pacotes do módulo atualizados, e então realizar através do Módulo Configurador a alteração do cadastro de Menu utilizado, modificando a chamada do programa antigo (**MATA086**) pelo programa novo **(COMA086):**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407775607319/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407775867287/mceclip1.png)

Caso haja dúvidas na utilização da rotina de Menus, pode-se solicitar o apoio junto ao suporte ao Módulo Configurador.

**Customizações:**Caso possua customizações na rotina antiga, será necessário revisa-las pois a estrutura e a tecnologia da rotina nova é diferente. Os pontos de entrada legados foram substituídos pelos pontos de entrada disponibilizados pelo MVC.

**Estrutura de Dados:**SAJ - Grupo de Compradores.

**Aviso:**  
A partir do momento em que a rotina antiga for descontinuada, não serão mais abertas manutenções para a mesma. Recomendamos que a migração seja feita o mais breve possível para que a descontinuação não impacte sua operação.

***Saiba Mais :***

[MATA086: Grupo de Compradores](https://tdn.totvs.com/display/public/PROT/MATA086%3A+Grupo+de+Compradores)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
