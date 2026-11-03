---
article_id: 40055418280727
category: Rental by ItUp Business
content_hash: 309d7b8216555ce35983e5ca9a41104b3297c908431ba8c084d85b41b693221a
fetched_at: '2026-06-28T22:36:20.699568+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - SIGALOC - RENTAL: LOCA00157 ao buscar
  o equipamento (BEM) para alocação'
type: support-article
updated_at: '2026-04-27T21:36:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40055418280727-Cross-Segmentos-Backoffice-Protheus-SIGALOC-RENTAL-LOCA00157-ao-buscar-o-equipamento-BEM-para-aloca%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40055430538647) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Ao tentar realizar a alocação de um equipamento em um Orçamento, o sistema apresenta o help "RENTAL: LOCA00157 - Problema: Inconsistência nos dados. Solução: O equipamento: [Nome/Código do Equipamento] Indisponível". Como resolver esta inconsistência que impede a alocação do bem?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - Todas as versões  
  
**Causa**  
Esta inconsistência ocorre porque o status do equipamento no Cadastro de Bens (presente no módulo de Manutenção de Ativos - SIGAMNT / Locação - SIGALOC) não está definido com o código padrão de disponibilidade exigido pela rotina, ou os códigos de status entre os módulos não estão devidamente alinhados.  
  
**Solução**  
Para que o equipamento seja alocado em um orçamento, é obrigatório que o status do bem corresponda ao status "00" (Disponível). A criação de status alternativos (como 01, 02, etc.) no cadastro sem a respectiva integração causará bloqueio na alocação.

**Passos**

1. Acesse o módulo **Manutenção de Ativos (19 - SIGAMNT)**.
2. Navegue até a rotina de Cadastro de Status de Bens (Atualizações > Bens > Status).
3. Certifique-se de que o status **00** existe. Caso não exista, clique em **Incluir** e crie o status com o código **00** e a descrição **DISPONÍVEL**.
4. Em seguida, acesse a rotina de Cadastro de Bens (Atualizações > Cadastros > Bens).
5. Localize o equipamento que apresentou o help no momento da alocação e clique em **Alterar**.
6. No formulário do bem, localize o campo referente ao Status do Bem e altere a informação para o código **00** (Disponível).
7. Confirme a alteração para gravar o registro.
8. Acesse o módulo **Locação de Equipamentos (94 - SIGALOC)**.
9. Navegue até a rotina de Cadastro de Status de Bens (Atualizações > Cadastro > Cadastro Básico > Cadastro de Status).
10. Valide se tem configurado um STATUS **00** vinculado com o STATUS **00** do módulo SIGAMNT.
