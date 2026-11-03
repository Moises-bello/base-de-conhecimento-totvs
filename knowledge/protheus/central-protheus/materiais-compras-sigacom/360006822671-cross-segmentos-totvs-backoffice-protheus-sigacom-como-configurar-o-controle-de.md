---
article_id: 360006822671
category: Materiais - Compras (SIGACOM)
content_hash: a3999438bae62e3551429842f36737dc066936c7ad31542700ff2d8f3aa6830f
fetched_at: '2026-06-28T22:41:07.561687+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como configurar o Controle
  de Alçadas Padrão?
type: support-article
updated_at: '2025-11-18T17:13:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006822671-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-configurar-o-Controle-de-Al%C3%A7adas-Padr%C3%A3o
---

**Dúvida**Como configurar o controle de alçada Padrão ?  
  
**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Solução**

O controle de Alçada Padrão é utilizado para determinar se um Pedido de Compras (PC) ou Autorização de Entrega (AE) incluso no sistema, será liberado ou não para compra efetiva do material, através de um fluxo de aprovação. A regra desse fluxo será determinada de acordo com as configurações criadas no Grupo de Aprovação.

Para saber mais sobre o conceito de alçada, acesse nossa pagina no YouTube:

[How To | MP - SIGACOM - Introdução Alçada Padrão](https://www.youtube.com/watch?v=O8HCipQ2mSM)

[How To | MP - SIGACOM - Alçada Padrão](https://www.youtube.com/watch?v=GXYL5sgXQ_k)

[Webinar | MP-SIGACOM - Alçada Padrão](https://www.youtube.com/watch?v=Il44O6TXIk4)

[Webinar | Tira dúvidas - Fluxo de alçadas (PC x IP)](https://www.youtube.com/watch?v=tktv4rmQwbI)

**Configurações:**

**1. Cadastrar os Aprovadores (MATA095):**

- Acesse o módulo SIGACOM > Atualizações > Administração de Compras > Aprovadores > Clique em Incluir > Vincule o usuário desejado>  Informe o limite do valor disponível para aprovação e defina se esse valor será: Diário, Semanal ou Mensal.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416746948503)

**2. Cadastrar Perfil de Aprovação (COMA210):**

- Acesse o módulo SIGACOM > Atualizações > Adminstração de Compras > Perfis de Aprovação > Clique em Incluir > Informe o range de aprovação para o bloqueio do pedido, valor mínimo e máximo e a moeda.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416755023383)

**3. Criar Grupo de Aprovação (MATA114):**

- Acesse o módulo SIGACOM > Atualizações > Administração de Compras > Grupo de Aprovação> Clique em Incluir > Na pasta cadastrais informar o(s) aprovador(es) que participarão do grupo, nível, tipo de aprovador se é apenas um Vistador (não consome saldo do aprovador) ou Aprovador (consome saldo do aprovador), Limite Automático (Se "Sim" irá validar o range informado no perfil de aprovação para o bloqueio, Se "Não" bloqueará qualquer valor), Tipo de liberação Usuário, Nível ou Documento e o perfil de aprovação.

Na pasta Tipos de Documentos flegar a opção ***"Ped. Compra"***.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416739880215)

**Importante**: Para habilitar a aba "Tipos de Documentos", deve habilitar o parâmetro MV\_ALTPDOC = .T.

**4. Cadastrar os Compradores (COMA087):**

- Acesse o módulo SIGACOM > Atualizações > Administração de Compras > Compradores > Clique em Incluir > Preencha o campo Grupo Aprov (***Y1\_GRAPROV**).* Ex: 000001.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416746926487)

**Importante**: Cada comprador pode ter um grupo diferente. O PC/AE incluso por esse comprador será destinado ao fluxo de alçada do grupo informado em seu cadastro.

Porém, para o fluxo de alçada funcionar, é possível definir um grupo de alçada padrão no parâmetro **MV\_PCAPROV**. Assim, caso algum usuário que não seja comprador incluir um PC/AE, esse registro será encaminhado para o fluxo do grupo determinado no parâmetro.

**Mais Informações:**

Estando os pedidos com os dados em que caia em um processo de bloqueio por alçada, qualquer alteração que for feita no pedido, ele retornará para o inicio da alçada, independente da alteração que for realizada, mesmo que apenas se clique em "Alterar" e posteriormente "Salvar" sem realizar nenhuma alteração. Pelo conceito do sistema, não há como se alterar esta característica no padrão do sistema.

**5. Contrato de Parceria (MATA125)**

Para aprovação por alçada de ***"Contratos de Parceria" (MATA125)***, a configurações seguem as mesmas regras, com a diferença em que no Cadastro do Comprador que inclui o Contrato, deve-se haver o grupo de Aprovação vinculado no campo "Grp Aprov CP" (***Y1\_GRAPRCP***) referente a Contrato de Parceria:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416740503191)

E também neste Grupo de Aprovação Vinculado no comprador, deve estar "flegado" o Tipo de Documento "Contr. Parcer": 

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416740512151)

Também é possível definir um grupo de aprovação padrão no parâmetro **MV\_CPAPROV**.

Na alçada do Contrato de Parceria, ela não possui uma funcionalidade ou configuração no padrão do sistema para uso de Alçada por Entidaeds Contabeis.

***Obs:***

No controale de alçada padrão, ele não possui uma funcionalidade para se ter alçadas por grupo de compras, sendo no padrão apenas conforme as funcionalidades acima descritas.

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Trilha de Videos Controle de Alçadas no Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9058852149399-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Trilha-de-Videos-Controle-de-Al%C3%A7adas-no-Compras?source=search)

[PCOM09012 - Configuração alçada versão 12.1.14, 12.1.16 e 12.1.17](http://tdn.totvs.com/pages/viewpage.action?pageId=286209197)

[Controle de Alçadas - FAQs](https://tdn.totvs.com/pages/viewpage.action?pageId=270095502)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
