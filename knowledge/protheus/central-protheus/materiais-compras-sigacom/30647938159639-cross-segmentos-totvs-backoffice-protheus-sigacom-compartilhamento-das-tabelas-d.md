---
article_id: 30647938159639
category: Materiais - Compras (SIGACOM)
content_hash: f65ec04b9313f44025b83c7796d599c6aee649ad9e14ede0d26bd9c885b28fa6
fetched_at: '2026-06-28T22:41:12.987487+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM -  Compartilhamento das
  tabelas de Alçada
type: support-article
updated_at: '2026-03-02T14:27:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30647938159639-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Compartilhamento-das-tabelas-de-Al%C3%A7ada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30647974445079) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Compartilhando as tabelas de alçada, para poder utilizar as mesmas configurações de alçadas em todas as filiais e aprovar pedidos de filiais diferentes sem precisar trocar de filial, o sistema funcionaria normalmente?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus compras - Todas as versões

**Solução**

Segue tabelas abaixo, que em caso de compartilhamento precisam ter o mesmo tipo de compartilhamento:

**DBLT10**- Entidades Contábeis X Grp Apr

**DBMT10**- Itens de Doc. com Alçada

**DHLT10**- Perfil de Aprovadores

**SAKT10**- Aprovadores

**SALT10**- Grupos de Aprovação

**SCRT10**- Documentos com Alçada

**SCST10**- Saldos dos Aprovadores

**SC7T10** - Pedido de compras

**SC1T10** - Solicitação de compras

##### **Análise interna:**

Ao compartilhar as tabelas de alçada, é crucial considerar a integridade e a eficiência do sistema como um todo. É fundamental reconhecer que, ao compartilhar as tabelas de alçada, outras tabelas correlacionadas, como **SC7**e **SC1**, também devem ser compartilhadas para garantir a consistência dos dados e evitar conflitos operacionais. **No entanto, é sugerido que as tabelas de alçada operem no modo exclusivo**, assim como as tabelas mencionadas,  contudo, caso a decisão seja manter o compartilhamento das tabelas, é imprescindível configurar o parâmetro: **[MV\_PCFILEN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022158251-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-o-conceito-do-MV-PCFILEN-e-sua-interfer%C3%AAncia-na-numera%C3%A7%C3%A3o-do-Pedido-de-Compras)** para evitar erros colaterais no sistema.

**Observação 1:**

As tabelas **SC7** e **SC1** devem possuir o mesmo tipo de compartilhamento das "tabelas de alçada mencionadas acima" para garantir a consistência dos dados e evitar conflitos operacionais.

**Observação 2:**

Hoje no padrão do sistema, o compartilhamento das tabelas mencionadas nesse artigo, são de modo "exclusivo" e a questão de alteração de compartilhamento é delicada, pois, deve ser realizada por um analista "in loco" e com base em um exemplo documentado para evitar ocorrências no sistema.

**Obs:** Ao realizar ajustes no compartilhamento de tabelas, é importante se atentar para os campos de filial. Caso o campo de filial não seja configurado corretamente de acordo com o compartilhamento, os registros não serão exibidos no sistema.

**Observação 3:**

O que fazer quando ocorrer o Help **EMPTYFORM** ao realizar a aprovação da alçada pelo usuário superior?

*1ª Possibilidade:*

Aplicar o pacote mais atual do SIGACOM do  link abaixo, conforme sua versão para validação em ambiente de teste.

COM/BACKOFFICE: <https://tdn.totvs.com/pages/viewpage.action?pageId=522011099>

**Obs:** Após aplicar o pacote acima, será necessário ser recriada a alçada do Pedido/Solicitação de Compras, onde para isso pode-se incluir um novo documento desde o inicio, ou, no documento existente realizar uma alteração sem ajustar nenhuma informação e Salvar para que possa ser recriado a alçada (SCR) para realizar um novo teste.

*2ª Possibilidade:*

Encaminhamos um cenário para equipe de produto com compartilhamento da tabela SC7 divergente das demais tabelas acima mencionadas com o Help EMPTYFORM , na solução do ticket, a resposta final reforçaram  **que todas as tabelas DBL, DBM, DHL, SAK, SAL, SCR, SCS, SC7 e SC1** precisam estar com o mesmo "tipo de compartilhamento" para evitar conflitos operacionais, conforme orientado na "Observação 1" desse artigo

Para mais informações: [PCOM09019 - Compartilhamento das tabelas de alçada](https://tdn.totvs.com/x/P9uJMg)

***Saiba Mais:***

[PCOM09019 - Compartilhamento das tabelas de alçada](https://tdn.totvs.com/pages/releaseview.action?pageId=847895359)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Trilha de Videos Controle de Alçadas no Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9058852149399-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Trilha-de-Videos-Controle-de-Al%C3%A7adas-no-Compras?source=search)

[PCOM09012 - Configuração alçada versão 12.1.14, 12.1.16 e 12.1.17](http://tdn.totvs.com/pages/viewpage.action?pageId=286209197)

[Controle de Alçadas - FAQs](https://tdn.totvs.com/pages/viewpage.action?pageId=270095502)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
